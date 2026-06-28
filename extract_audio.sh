#!/bin/bash
# 从 Friends 剧集视频中截取音频片段
# 用法: bash extract_audio.sh <视频文件> <季> <集>
# 例: bash extract_audio.sh ~/Desktop/friends视频/S01E01.mp4 1 1

VIDEO="$1"
SEASON="$2"
EPISODE="$3"
FFMPEG="${FFMPEG:-ffmpeg}"
OUTDIR="$(dirname "$0")/audio/clips"
DATA="$(dirname "$0")/data/scripts.json"

mkdir -p "$OUTDIR"

echo "🎬 从 $(basename "$VIDEO") 提取 S${SEASON}E${EPISODE} 音频片段..."
echo ""

# 用 Python 解析 JSON 并调用 ffmpeg
python3 << PYEOF
import json, subprocess, os, sys

video = "$VIDEO"
season = int("$SEASON")
episode = int("$EPISODE")
outdir = "$OUTDIR"
ffmpeg = "$FFMPEG"

if not os.path.exists(video):
    print(f"❌ 视频文件不存在: {video}")
    sys.exit(1)

with open("$DATA") as f:
    scripts = json.load(f)

# 筛选当前季/集的句子
targets = [s for s in scripts if s['season']==season and s['episode']==episode]
print(f"📋 找到 {len(targets)} 句台词\n")

success = 0
for i, s in enumerate(targets):
    # 解析时间戳
    ts = s['timestamp']  # "00:04:20"
    parts = ts.split(':')
    if len(parts) == 3:
        start_sec = int(parts[0])*3600 + int(parts[1])*60 + int(parts[2])
    else:
        start_sec = int(parts[0])*60 + int(parts[1])

    # 提前 1 秒开始，截取 6 秒
    clip_start = max(0, start_sec - 1)
    duration = 6

    # 输出文件名
    outfile = os.path.join(outdir, f"{s['id']}.mp3")

    # 避免重复
    if os.path.exists(outfile):
        print(f"  ⏭ 跳过: {s['id']} (已存在)")
        success += 1
        continue

    # ffmpeg 截取
    cmd = [
        ffmpeg, '-y', '-loglevel', 'error',
        '-ss', str(clip_start),
        '-i', video,
        '-t', str(duration),
        '-vn',                    # 只要音频
        '-acodec', 'libmp3lame',
        '-q:a', '4',             # 高质量 (~160kbps)
        outfile
    ]

    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0:
        size = os.path.getsize(outfile)
        print(f"  ✅ [{i+1}/{len(targets)}] {s['speaker']}: {s['text'][:40]}... ({size//1024}KB)")
        success += 1
    else:
        err = result.stderr.decode()[:100] if result.stderr else 'unknown'
        print(f"  ❌ [{i+1}/{len(targets)}] {s['id']}: {err}")

print(f"\n{'='*50}")
print(f"✅ 完成! {success}/{len(targets)} 个音频片段 → {outdir}/")
PYEOF
