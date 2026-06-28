#!/usr/bin/env python3
"""构建老友记台词语料库"""

import json, hashlib, random, os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ═══════════════════════════════════════════════════════════════
# 台词数据： (season, episode, scene, speaker, text_en, text_cn, timestamp, difficulty)
# ═══════════════════════════════════════════════════════════════
raw = []

def S(s, e, sc, sp, en, cn, ts, d="A2", ytid="", ytstart=0):
    raw.append({"season":s,"episode":e,"scene":sc,"speaker":sp,"text":en.strip(),"textCN":cn.strip(),"timestamp":ts,"difficulty":d,"youtube_id":ytid,"youtube_start":ytstart})

# ── Season 1 ──────────────────────────────────────────────────
S(1,1,"Central Perk","Monica","There's nothing to tell! He's just some guy I work with!","没什么好说的！他只是我同事！","00:01:20")
S(1,1,"Central Perk","Joey","C'mon, you're going out with the guy. There's gotta be something wrong with him!","拜托，你都在跟他约会了。他肯定有什么问题！","00:01:28")
S(1,1,"Central Perk","Chandler","So does he have a hump? A hump and a hairpiece?","那他有没有驼背？驼背加假发？","00:01:35")
S(1,1,"Central Perk","Phoebe","Wait, does he eat chalk? Just because I don't want her to go through what I went through with Carl.","等等，他吃粉笔吗？我只是不想她经历我和Carl的事。","00:01:45","B1")
S(1,1,"Central Perk","Rachel","I just don't want to be a shoe anymore! I want to be a purse. Or a hat!","我就是不想再做鞋了！我想当个包。或者帽子！","00:02:50","B1")
S(1,1,"Central Perk","Rachel","You guys, I just don't know what I'm gonna do. What am I gonna do with my life?","你们知道吗，我不知道该怎么办。我的人生要做什么？","00:04:10","A2")
S(1,1,"Central Perk","Monica","Welcome to the real world! It sucks. You're gonna love it.","欢迎来到现实世界！它很烂，但你会爱上它的。","00:04:20","A1")
S(1,1,"Monica's Apartment","Ross","I just feel like someone reached down my throat, grabbed my small intestine, pulled it out of my mouth and tied it around my neck.","我感觉像是有人把手伸进我喉咙，拽出我的小肠，从嘴里拉出来，绕在我脖子上。","00:08:30","B2")
S(1,1,"Monica's Apartment","Chandler","Sometimes I wish I was a lesbian. Did I say that out loud?","有时候我希望我是个女同性恋。我是不是说出来了？","00:09:15","B1")
S(1,1,"Monica's Apartment","Ross","I told mom and dad last night. They seemed to take it pretty well.","我昨晚告诉爸妈了。他们看起来接受得还不错。","00:10:00","A2")
S(1,1,"Monica's Apartment","Monica","Oh really? So that hysterical phone call I got from a woman sobbing at 3am, 'I'll never have grandchildren,' that was a wrong number?","哦是吗？那凌晨三点打来哭着说'我永远不会有孙子了'的歇斯底里的电话，是打错了？","00:10:18","B2")
S(1,1,"Monica's Apartment","Ross","I'm divorced! I'm only 26 and I'm divorced!","我离婚了！我才26岁就离婚了！","00:10:45","A1")
S(1,2,"Hospital","Ross","I don't want my baby's first words to be 'How come you don't live with Mommy?'","我不想我孩子的第一句话是'为什么你不和妈妈住在一起？'","00:05:30","B1")
S(1,2,"Hospital","Rachel","I can't believe I have to walk down the aisle with Barry. I'm gonna look like an idiot.","我不敢相信我得和Barry一起走红毯。我会看起来像个白痴。","00:08:00","B1")
S(1,2,"Hospital","Monica","You know, I was thinking, what if I don't have babies? I mean, what if I never find a guy?","我在想，如果我生不了孩子怎么办？如果我根本找不到一个男人呢？","00:12:00","A2")
S(1,3,"Central Perk","Phoebe","They gave me 700 dollars. That's a lot of money! I'm gonna go buy a bunch of stuff.","他们给了我700块。好多钱啊！我要去买一堆东西。","00:03:00","A2")
S(1,3,"Central Perk","Chandler","Oh, I think this is the episode of 'Three's Company' where there's some kind of misunderstanding.","哦，这集《三人行》好像是有什么误会的那集。","00:05:00","B1")
S(1,3,"Central Perk","Phoebe","I found a thumb. It's a human thumb. And I'm keeping it.","我找到了一根拇指。人类的拇指。我要留着它。","00:06:30","A2")
S(1,4,"Hospital","Rachel","I'm gonna be alone forever. I'm gonna be an old lady with 30 cats.","我会孤独终老。我会变成一个养30只猫的老太婆。","00:07:00","B1")
S(1,4,"Monica's Apartment","Chandler","I'm not good at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:10:00","B1")
S(1,5,"Laundromat","Rachel","Okay, I'll do the laundry. How hard can it be?","好吧，我去洗衣服。能有多难？","00:04:00","A1")
S(1,5,"Laundromat","Ross","This is not good. This is the opposite of good. This is bad.","这不好。这是好的反面。这是坏。","00:08:00","A2")
S(1,6,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(1,7,"Monica's Apartment","Phoebe","I'm very happy we're gonna have all the birds back. I mean, they were a big part of my childhood.","我很高兴所有的鸟都要回来了。它们是我童年的重要部分。","00:05:00","B1")
S(1,7,"Monica's Apartment","Chandler","I'm stuck in an ATM vestibule with Jill Goodacre!","我和Jill Goodacre被困在ATM机亭里了！","00:10:00","B1")
S(1,8,"Funeral Home","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:04:00","B1")
S(1,8,"Funeral Home","Ross","She died. She's gone. She's not coming back.","她死了。她不在了。她不会回来了。","00:08:00","A2")
S(1,9,"Monica's Apartment","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(1,10,"Monica's Apartment","Ross","I can't believe I lost my monkey. Who loses a monkey?","我不敢相信我弄丢了猴子。谁会弄丢一只猴子？","00:06:00","A2")
S(1,12,"Monica's Apartment","Monica","I made 12 lasagnas. Twelve! Who needs 12 lasagnas?","我做了12份千层面。12份！谁需要12份千层面？","00:03:00","A2")
S(1,15,"Monica's Apartment","Rachel","I'm gonna be alone forever. I'm gonna be an old lady with 50 cats.","我会孤独终老。变成养50只猫的老太婆。","00:08:00","B1")
S(1,18,"Monica's Apartment","Rachel","I can't believe I'm doing this. I'm playing poker with five guys.","我不敢相信我在做这个。我和五个男人打扑克。","00:04:00","A2")
S(1,24,"Monica's Apartment","Rachel","I know. I know. I know that you know. But you don't know that I know that you know.","我知道。我知道你知道。但你不知道我知道你知道。","00:12:00","B2")
S(1,24,"Central Perk","Ross","I'm sorry I got so jealous. I'm not usually the jealous type.","对不起我太嫉妒了。我通常不是嫉妒型的。","00:15:00","A2")

# ── Season 2 ──────────────────────────────────────────────────
S(2,1,"Central Perk","Rachel","I can't believe Ross is with Julie. I mean, Julie?","我不敢相信Ross和Julie在一起。Julie？","00:02:00","A2")
S(2,2,"Monica's Apartment","Monica","I'm not a control freak. I'm just better at things than other people.","我不是控制狂。我只是比其他人更擅长做事。","00:05:00","B1")
S(2,4,"Monica's Apartment","Joey","Joey doesn't share food!","Joey不分享食物！","00:08:00","A1")
S(2,7,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(2,7,"Central Perk","Ross","We were on a break!","我们当时分手了！","00:12:00","A1")
S(2,8,"Monica's Apartment","Ross","Pivot! Pivot! Pivot!","转！转！转！","00:10:30","A1")
S(2,8,"Monica's Apartment","Chandler","Shut up! Shut up! Shut up!","闭嘴！闭嘴！闭嘴！","00:10:45","A1")
S(2,9,"Monica's Apartment","Phoebe","Smelly cat, smelly cat, what are they feeding you?","臭猫，臭猫，他们喂你什么？","00:06:00","A1")
S(2,12,"Central Perk","Monica","I don't want to be single. I just want to be married again.","我不想单身。我只想再结婚。","00:05:00","B1")
S(2,13,"Monica's Apartment","Rachel","I'm sorry. I'm sorry. I'm sorry. I'm sorry.","对不起。对不起。对不起。对不起。","00:10:00","A1")
S(2,14,"Central Perk","Ross","I'm not a cheater. We were on a break!","我不是出轨。我们当时分手了！","00:08:00","A2")
S(2,21,"Monica's Apartment","Chandler","I'm hopeless and awkward and desperate for love!","我无可救药，笨拙，渴望爱情！","00:12:00","A2")

# ── Season 3 ──────────────────────────────────────────────────
S(3,1,"Central Perk","Monica","I'm not sick. I'm just getting over a cold.","我没生病。我只是感冒刚好。","00:03:00","A2")
S(3,2,"Restaurant","Ross","I'm not a cheater. I'm not. I'm not a cheater.","我不是出轨的人。我不是。我不是。","00:10:00","A2")
S(3,5,"Monica's Apartment","Phoebe","I wish I could remember, but I can't.","我希望我能想起来，但我想不起来。","00:05:00","A2")
S(3,6,"Central Perk","Chandler","What did I marry into?","我到底嫁入了什么家庭？","00:07:00","B1")
S(3,15,"Monica's Apartment","Ross","I'm a good guy. I'm a really good guy.","我是个好男人。我是真的很好的男人。","00:06:00","A2")
S(3,16,"Beach House","Phoebe","I'm very wise. I know. I'm Yoda.","我很聪明。我知道。我是尤达。","00:08:00","B1")
S(3,24,"Monica's Apartment","Rachel","I can't believe I'm going to London. I'm going to London!","我不敢相信我就要去伦敦了。我要去伦敦了！","00:04:00","A2")

# ── Season 4 ──────────────────────────────────────────────────
S(4,1,"Beach","Ross","I take thee Rachel.","我愿娶你 Rachel。","00:15:00","A1")
S(4,8,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:05:00","B1")
S(4,12,"Monica's Apartment","Ross","I'm fine. I'm totally fine.","我很好。我完全没事。","00:08:00","A1")
S(4,12,"Restaurant","Joey","Joey Tribbiani does not share food!","Joey Tribbiani不分享食物！","00:06:00","A1")
S(4,23,"London","Ross","I Ross, take thee Rachel.","我Ross，愿娶你Rachel。","00:12:00","A1")
S(4,24,"London","Chandler","I love you. I love you. I love you.","我爱你。我爱你。我爱你。","00:14:00","A1")

# ── Season 5 ──────────────────────────────────────────────────
S(5,8,"Monica's Apartment","Monica","I know! I know! I know!","我知道！我知道！我知道！","00:10:00","A1")
S(5,8,"Monica's Apartment","Chandler","I'm in love with Monica.","我爱上Monica了。","00:12:00","A2")
S(5,14,"Monica's Apartment","Phoebe","They don't know that we know they know we know.","他们不知道我们知道他们知道我们知道。","00:06:00","B2")
S(5,15,"Central Perk","Ross","My sandwich? MY SANDWICH?!","我的三明治？我的三明治？！","00:08:00","A1")

# ── Season 6 ──────────────────────────────────────────────────
S(6,1,"Las Vegas","Ross","I Ross, take thee Rachel.","我Ross，愿娶你Rachel。","00:14:00","A1")
S(6,9,"Monica's Apartment","Ross","I'm fine. I'm fine. I make fine. I'm fine!","我很好。我很好。我做得很好。我很好！","00:06:00","A2")
S(6,16,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:04:00","B1")
S(6,24,"Monica's Apartment","Chandler","I'm gonna propose to Monica.","我要向Monica求婚了。","00:16:00","A2")

# ── Season 7 ──────────────────────────────────────────────────
S(7,1,"Monica's Apartment","Monica","I'm engaged! I'm engaged! I'm engaged!","我订婚了！我订婚了！我订婚了！","00:02:00","A1")
S(7,14,"Monica's Apartment","Phoebe","I'm not good at being pregnant. I'm not good at it.","我不擅长怀孕。我真的不擅长。","00:05:00","A2")
S(7,24,"Wedding Venue","Chandler","I, Chandler, take thee, Monica.","我，Chandler，愿娶你，Monica。","00:18:00","A1")

# ── Season 8 ──────────────────────────────────────────────────
S(8,1,"Wedding Venue","Monica","I, Monica, take thee, Chandler.","我，Monica，愿嫁你，Chandler。","00:19:00","A1")
S(8,2,"Monica's Apartment","Rachel","I'm pregnant.","我怀孕了。","00:10:00","A1")
S(8,9,"Central Perk","Joey","I'm not even sorry.","我甚至不觉得抱歉。","00:04:00","A2")

# ── Season 9 ──────────────────────────────────────────────────
S(9,21,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")

# ── Season 10 ──────────────────────────────────────────────────
S(10,3,"Monica's Apartment","Ross","I'm a professor. I'm a professor!","我是教授了。我是教授了！","00:06:00","A2")
S(10,17,"Central Perk","Phoebe","I love you. And I'm gonna miss you.","我爱你。我会想念你的。","00:20:00","A2")
S(10,17,"Central Perk","Chandler","Where?","哪里？","00:21:00","A1")
S(10,18,"Monica's Apartment","Rachel","I got off the plane.","我下了飞机。","00:22:00","A2")

# ── Season 1 扩展 ────────────────────────────────────────────────
S(1,1,"Central Perk","Monica","I know this is gonna sound crazy, but I think I'm in love with him.","我知道这听起来很疯狂，但我想我爱上他了。","00:03:30","A2")
S(1,1,"Central Perk","Ross","I don't want to be single. I just want to be married again.","我不想单身。我只想再结婚。","00:05:00","A2")
S(1,1,"Monica's Apartment","Rachel","I'm gonna be alone forever. I'm gonna be an old lady with 30 cats.","我会孤独终老。变成一个养30只猫的老太婆。","00:12:00","B1")
S(1,2,"Hospital","Carol","I'm having a baby!","我要生了！","00:02:00","A1")
S(1,3,"Central Perk","Chandler","I'm not good at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:04:00","B1")
S(1,5,"Laundromat","Ross","This is not good. This is the opposite of good. This is bad.","这不好。这是好的对立面。这是坏。","00:07:30","A2")
S(1,6,"Central Perk","Joey","You can't just give up. Is that what a dinosaur would do?","你不能就这么放弃。恐龙会这么做吗？","00:05:00","B1")
S(1,7,"ATM Vestibule","Chandler","I'm stuck in an ATM vestibule with Jill Goodacre!","我和Jill Goodacre困在ATM机亭里了！","00:03:00","B1")
S(1,8,"Cemetery","Ross","I can't believe she's gone. She was always there for me.","我不敢相信她走了。她一直都在我身边。","00:06:00","A2")
S(1,9,"Central Perk","Phoebe","I don't believe in evolution. I believe in gravity.","我不相信进化论。我相信重力。","00:04:00","B2")
S(1,10,"Central Perk","Rachel","I'm not a waitress. I'm a assistant buyer.","我不是服务员。我是采购助理。","00:03:00","A2")
S(1,11,"Restaurant","Monica","My mom thinks I'm not marriage material. That's what she said.","我妈觉得我不是结婚的料。她就是这么说的。","00:05:00","B1")
S(1,13,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:04:00","B1")
S(1,14,"Central Perk","Ross","I made a resolution. No more divorces.","我下定了决心。不再离婚了。","00:03:00","A2")
S(1,16,"Hospital","Phoebe","I'm having my brother's babies. It's a beautiful thing.","我在帮我弟弟生孩子。这是多么美好的事。","00:06:00","B1")
S(1,17,"Central Perk","Rachel","I can't believe I'm doing this. I'm dating a patient.","我不敢相信我居然在和一个病人约会。","00:04:00","A2")
S(1,19,"Central Perk","Ross","Where's my monkey? Has anyone seen my monkey?","我的猴子呢？有人看到我的猴子吗？","00:03:00","A2")
S(1,21,"Monica's Apartment","Monica","I'm not sick. I'm just getting over a cold.","我没生病。只是感冒刚好。","00:02:00","A2")
S(1,23,"Hospital","Rachel","I'm not ready to be a mother. I can't even take care of myself.","我还没准备好当妈妈。我连自己都照顾不好。","00:08:00","B1")

# ── Season 2 扩展 ────────────────────────────────────────────────
S(2,1,"Central Perk","Ross","I can't believe I have a son. I have a son!","我不敢相信我有个儿子。我有儿子了！","00:03:00","A2")
S(2,3,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:04:00","B1")
S(2,5,"Central Perk","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(2,6,"Beach House","Phoebe","I'm very upset. I'm very very upset.","我很不高兴。我非常不高兴。","00:05:00","A2")
S(2,10,"Central Perk","Monica","I'm not a control freak. I'm just better at things than most people.","我不是控制狂。我只是比大多数人更擅长做事。","00:04:00","B1")
S(2,11,"Monica's Apartment","Ross","I'm not a cheater. I would never cheat on anyone.","我不是出轨的人。我绝不会对任何人出轨。","00:07:00","A2")
S(2,14,"Central Perk","Ross","We were on a break!","我们当时分手了！","00:06:00","A1")
S(2,15,"Central Perk","Rachel","I don't want to be alone. I really don't.","我不想一个人。我真的不想。","00:05:00","A2")
S(2,16,"Monica's Apartment","Joey","Joey doesn't share food!","Joey不分享食物！","00:06:00","A1")
S(2,17,"Central Perk","Phoebe","Smelly cat, smelly cat, it's not your fault.","臭猫，臭猫，这不是你的错。","00:04:00","A1")
S(2,19,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(2,22,"Central Perk","Ross","I'm a paleontologist. I dig stuff up.","我是古生物学家。我挖东西的。","00:03:00","A2")

# ── Season 3 扩展 ────────────────────────────────────────────────
S(3,2,"Monica's Apartment","Ross","I'm not a cheater. I'm not. I'm not a cheater.","我不是出轨的人。我不是。我不是出轨的人。","00:06:00","A2")
S(3,4,"Central Perk","Monica","I'm not competitive. I'm just better.","我不是好胜。我只是更厉害。","00:03:00","B1")
S(3,6,"Central Perk","Phoebe","I'm very spiritual. I talk to trees.","我很有灵性。我跟树聊天。","00:04:00","B1")
S(3,8,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(3,9,"Central Perk","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(3,12,"Restaurant","Rachel","I'm not a waitress anymore. I'm a buyer.","我不再是服务员了。我是采购。","00:04:00","A2")
S(3,14,"Monica's Apartment","Ross","I'm a good guy. I'm a really good guy.","我是个好男人。我是真的很好的男人。","00:06:00","A2")
S(3,18,"Central Perk","Phoebe","I don't believe in evolution. I believe in gravity.","我不相信进化论。我相信重力。","00:03:00","B2")
S(3,19,"Monica's Apartment","Monica","I'm not sick. I'm just resting my eyes.","我没生病。我只是在闭目养神。","00:02:00","A2")
S(3,21,"Central Perk","Chandler","I'm hopeless and awkward and desperate for love!","我无可救药，笨拙，渴望爱情！","00:05:00","A2")
S(3,23,"Beach House","Phoebe","I'm very wise. I know. I'm Yoda.","我很聪明。我知道。我是尤达。","00:05:00","B1")

# ── Season 4 扩展 ────────────────────────────────────────────────
S(4,3,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(4,6,"Central Perk","Rachel","I'm not a bad person. I'm just doing my job.","我不是坏人。我只是在做我的工作。","00:04:00","A2")
S(4,9,"Central Perk","Joey","Joey Tribbiani doesn't share food!","Joey Tribbiani不分享食物！","00:04:00","A1")
S(4,11,"Monica's Apartment","Phoebe","I'm not a lesbian. I'm just very open-minded.","我不是女同性恋。我只是思想很开放。","00:05:00","B1")
S(4,14,"Central Perk","Ross","I'm fine. I'm totally fine. I make fine.","我很好。我完全没事。我做得好好的。","00:06:00","A2")
S(4,18,"Monica's Apartment","Monica","I'm not a control freak. I just like things a certain way.","我不是控制狂。我只是喜欢事情按特定方式进行。","00:04:00","B1")
S(4,21,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")

# ── Season 5 扩展 ────────────────────────────────────────────────
S(5,3,"Central Perk","Phoebe","I gave birth to triplets. That's a lot of babies.","我生了三胞胎。那是很多宝宝。","00:04:00","A2")
S(5,5,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(5,7,"Central Perk","Ross","I'm not a cheater. We were on a break!","我不是出轨。我们当时分手了！","00:05:00","A2")
S(5,9,"Monica's Apartment","Rachel","I'm not in love with Ross. I'm not. I'm not.","我不爱Ross。我没有。我没有。","00:06:00","A2")
S(5,11,"Central Perk","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(5,13,"Monica's Apartment","Monica","I know! I know! I know!","我知道！我知道！我知道！","00:04:00","A1")
S(5,16,"Central Perk","Phoebe","I'm a cop. I'm a cop and I'm arresting you.","我是警察。我是警察，我要逮捕你。","00:05:00","B1")
S(5,18,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")

# ── Season 6 扩展 ────────────────────────────────────────────────
S(6,2,"Monica's Apartment","Ross","I'm a professor. I teach at NYU.","我是教授了。我在纽约大学教书。","00:04:00","A2")
S(6,5,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(6,8,"Monica's Apartment","Rachel","I'm not a mom. I'm just practicing.","我不是妈妈。我只是在练习。","00:05:00","A2")
S(6,12,"Central Perk","Joey","Joey doesn't share food!","Joey不分享食物！","00:03:00","A1")
S(6,15,"Monica's Apartment","Monica","I'm not competitive. I'm supportive.","我不是好胜。我是支持的。","00:04:00","B1")
S(6,18,"Central Perk","Phoebe","I'm very intuitive. I know things.","我直觉很准。我知道很多事情。","00:03:00","B1")
S(6,22,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")

# ── Season 7 扩展 ────────────────────────────────────────────────
S(7,4,"Central Perk","Ross","I'm a father. I know how to take care of a baby.","我是父亲。我知道怎么照顾宝宝。","00:04:00","A2")
S(7,7,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(7,10,"Central Perk","Rachel","I'm not a bad person. I just made a mistake.","我不是坏人。我只是犯了个错。","00:05:00","A2")
S(7,13,"Monica's Apartment","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(7,16,"Central Perk","Phoebe","I'm not good at being pregnant. I'm really not.","我不擅长怀孕。我真的不擅长。","00:04:00","A2")
S(7,19,"Monica's Apartment","Monica","I'm engaged! I'm getting married!","我订婚了！我要结婚了！","00:03:00","A1")
S(7,22,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")

# ── Season 8 扩展 ────────────────────────────────────────────────
S(8,4,"Monica's Apartment","Rachel","I'm pregnant. And I'm terrified.","我怀孕了。而且我很害怕。","00:05:00","A2")
S(8,7,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(8,10,"Monica's Apartment","Ross","I'm gonna be a father again. That's huge.","我又要当爸爸了。太重大了。","00:04:00","A2")
S(8,14,"Central Perk","Phoebe","I'm very spiritual. I can see auras.","我很有灵性。我能看见气场。","00:03:00","B1")
S(8,17,"Monica's Apartment","Joey","Joey doesn't share food!","Joey不分享食物！","00:03:00","A1")
S(8,20,"Central Perk","Monica","I'm not a control freak. I'm organized.","我不是控制狂。我只是有条理。","00:04:00","B1")
S(8,23,"Hospital","Rachel","I'm having a baby! Right now!","我要生了！现在！","00:06:00","A1")

# ── Season 9 扩展 ────────────────────────────────────────────────
S(9,3,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(9,7,"Central Perk","Ross","I'm a professor. I have a PhD.","我是教授。我有博士学位。","00:04:00","A2")
S(9,10,"Monica's Apartment","Rachel","I'm not in love with Ross. I'm really not.","我不爱Ross。我真的不爱。","00:05:00","A2")
S(9,14,"Central Perk","Phoebe","I'm very happy for you. I really am.","我真的很为你高兴。真的。","00:04:00","A2")
S(9,17,"Monica's Apartment","Joey","How you doin'?","最近怎么样？","00:02:00","A1")
S(9,20,"Central Perk","Monica","I'm not competitive. I just like to win.","我不是好胜。我只是喜欢赢。","00:03:00","B1")

# ── Season 10 扩展 ────────────────────────────────────────────────
S(10,2,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听我讽刺一句吗？","00:03:00","B1")
S(10,5,"Central Perk","Rachel","I'm moving to Paris. It's happening.","我要搬去巴黎了。这是真的。","00:05:00","A2")
S(10,8,"Monica's Apartment","Ross","I'm not good at goodbyes. I really suck at them.","我不擅长道别。我真的太差了。","00:06:00","A2")
S(10,11,"Central Perk","Phoebe","I'm getting married! To Mike!","我要结婚了！和Mike！","00:04:00","A1")
S(10,14,"Monica's Apartment","Joey","Joey doesn't share food!","Joey不分享食物！","00:03:00","A1")

# ── 海量扩充：Season 1 ──────────────────────────────────────────
S(1,1,"Central Perk","Ross","I don't want to be single anymore. I just want to be married again.","我不想再单身了。我只想再次结婚。","00:05:30","A2")
S(1,1,"Central Perk","Phoebe","You're like a giant, walking around, breathing.","你就像一个巨人，走来走去，呼吸着。","00:06:00","B1")
S(1,1,"Monica's Apartment","Rachel","I can't believe I'm here. I'm living in the city!","我不敢相信我在这里。我住在城市里了！","00:07:00","A2")
S(1,2,"Hospital","Carol","I'm having contractions. They're very painful.","我在宫缩。非常疼。","00:03:00","B1")
S(1,2,"Hospital","Ross","I'm gonna be a father. I'm gonna be a dad!","我要当爸爸了。我要当爸爸了！","00:04:30","A2")
S(1,3,"Central Perk","Chandler","I'm not good at being single. I'm hopeless.","我不擅长单身。我无可救药。","00:05:30","A2")
S(1,4,"Monica's Apartment","Rachel","I can't believe I have to get a job. I've never had a job.","我不敢相信我必须找工作。我从没工作过。","00:03:00","B1")
S(1,4,"Central Perk","Monica","I'm not a cougar. I'm just dating a younger guy.","我不是在搞姐弟恋。我只是刚好跟年轻的约会。","00:05:00","B1")
S(1,5,"Laundromat","Rachel","I washed a black sock with my white stuff. Everything's gray.","我把黑袜子和白色的一起洗了。全变灰了。","00:05:00","A2")
S(1,5,"Laundromat","Ross","You gotta respect the machine. The machine is your friend.","你得尊重机器。机器是你的朋友。","00:06:30","B1")
S(1,6,"Central Perk","Joey","You can't just give up. You gotta fight for what you want.","你不能就这么放弃。你得为你想要的奋斗。","00:04:00","A2")
S(1,7,"Monica's Apartment","Phoebe","I don't believe in electricity. I think it's a fad.","我不相信电。我觉得那只是一时流行。","00:04:00","B2")
S(1,8,"Cemetery","Monica","My grandmother was a wonderful woman. She taught me everything.","我外婆是个了不起的女人。她教会了我一切。","00:05:00","A2")
S(1,9,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:30","B1")
S(1,10,"Central Perk","Ross","Marcel is not just a monkey. He's my friend.","Marcel不只是猴子。他是我的朋友。","00:04:00","A2")
S(1,11,"Restaurant","Monica","My mom is very critical. Nothing I do is ever good enough.","我妈非常挑剔。我做什么都不够好。","00:05:30","B1")
S(1,13,"Monica's Apartment","Rachel","I can't believe Barry cheated on me. With the maid!","我不敢相信Barry出轨了。还是跟女佣！","00:04:00","A2")
S(1,14,"Central Perk","Ross","I'm not good at relationships. I've been divorced twice.","我不擅长恋爱关系。我离了两次婚。","00:05:00","A2")
S(1,16,"Monica's Apartment","Joey","Acting is not about being famous. It's about the craft.","演戏不是为了出名。是为了艺术。","00:04:00","B1")
S(1,17,"Central Perk","Phoebe","I'm very proud of my brother. He's doing a beautiful thing.","我为我弟弟感到骄傲。他在做一件很美好的事。","00:04:00","A2")
S(1,20,"Monica's Apartment","Rachel","I can't believe I'm dating a guy who's still in high school.","我不敢相信我在跟一个还在高中的人约会。","00:05:00","A2")
S(1,22,"Central Perk","Ross","I'm not good with babies. I'm afraid I'll break them.","我不擅长带孩子。我怕把他们弄坏了。","00:04:00","B1")
S(1,23,"Hospital","Monica","I'm so happy for Carol and Susan. The baby is beautiful.","我真为Carol和Susan高兴。宝宝太美了。","00:05:00","A2")
S(1,24,"Central Perk","Rachel","I can't believe Ross is in love with me. Ross!","我不敢相信Ross爱着我。是Ross啊！","00:08:00","A2")

# ── 海量扩充：Season 2 ──────────────────────────────────────────
S(2,2,"Central Perk","Rachel","I'm so excited for my first day at work. I'm a professional now.","我对第一天上班太兴奋了。我是专业人士了。","00:03:00","A2")
S(2,3,"Monica's Apartment","Chandler","I can't believe I'm dating a girl who thinks I'm someone else.","我不敢相信我在跟一个以为我是别人的人约会。","00:05:00","B1")
S(2,5,"Central Perk","Ross","I'm not good at dating. I haven't been on a date in years.","我不擅长约会。我好几年没约会过了。","00:04:00","A2")
S(2,6,"Beach House","Monica","I'm not competitive. I just happen to be better than everyone.","我不是争强好胜。我只是恰好比所有人都好。","00:05:00","B1")
S(2,7,"Central Perk","Phoebe","I'm very intuitive. I can feel people's energy.","我直觉很准。我能感受到人的能量。","00:03:00","B1")
S(2,9,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(2,11,"Central Perk","Ross","I can't believe Carol found someone else. And it's a woman.","我不敢相信Carol找到了别人。而且还是个女人。","00:06:00","A2")
S(2,12,"Monica's Apartment","Rachel","I'm so sick of being single. I want to be in love again.","我受够单身了。我想再次恋爱。","00:04:00","A2")
S(2,14,"Central Perk","Joey","I'm not just a pretty face. I'm a serious actor.","我不只是长得帅。我是个认真的演员。","00:03:00","B1")
S(2,15,"Monica's Apartment","Phoebe","I'm not a vegetarian anymore. I had a dream about a hamburger.","我不再是素食主义者了。我做了个关于汉堡的梦。","00:04:00","B1")
S(2,17,"Central Perk","Monica","I'm not crazy. I'm just very particular about my apartment.","我不疯。我只是对我的公寓特别讲究。","00:03:00","B1")
S(2,19,"Monica's Apartment","Ross","I'm not a stalker. I just happened to be in her neighborhood.","我不是跟踪狂。我只是碰巧在她家附近。","00:05:00","B1")
S(2,21,"Central Perk","Rachel","I can't believe Ross is dating my sister's boss's daughter.","我不敢相信Ross在和我姐姐老板的女儿约会。","00:06:00","B2")
S(2,23,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(2,24,"Central Perk","Ross","I can't believe Rachel knows how I feel. I'm terrified.","我不敢相信Rachel知道了我的感受。我吓坏了。","00:06:00","A2")

# ── 海量扩充：Season 3 ──────────────────────────────────────────
S(3,1,"Monica's Apartment","Monica","I'm not sick. I'm just taking a mental health day.","我没生病。我只是在放心理健康假。","00:02:00","B1")
S(3,3,"Central Perk","Rachel","I'm so excited about my new job at Ralph Lauren.","我对Ralph Lauren的新工作太兴奋了。","00:04:00","A2")
S(3,5,"Central Perk","Chandler","I can't believe Janice is back. Oh. My. God.","我不敢相信Janice回来了。我的天哪。","00:03:00","B1")
S(3,7,"Monica's Apartment","Ross","I'm not a bad teacher. I'm just not used to teaching adults.","我不是坏老师。我只是不习惯教成年人。","00:04:00","A2")
S(3,9,"Central Perk","Phoebe","I'm very proud of my art. Even if nobody understands it.","我为我的艺术感到骄傲。即使没人理解。","00:03:00","B1")
S(3,11,"Monica's Apartment","Joey","I'm not a pervert. I'm just very comfortable with my body.","我不是变态。我只是对自己身体很自在。","00:04:00","B1")
S(3,13,"Central Perk","Monica","I can't believe Rachel and Ross are still not together.","我不敢相信Rachel和Ross还没在一起。","00:05:00","A2")
S(3,15,"Monica's Apartment","Ross","I'm a good guy. I would never hurt anyone on purpose.","我是好人。我绝不会故意伤害任何人。","00:06:00","A2")
S(3,17,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(3,19,"Monica's Apartment","Rachel","I can't believe Mark is interested in me. He's so cute.","我不敢相信Mark对我有意思。他好可爱。","00:05:00","A2")
S(3,21,"Central Perk","Phoebe","I'm not a liar. I just have a very creative relationship with truth.","我不是骗子。我只是和真相的关系非常有创意。","00:04:00","B2")
S(3,22,"Monica's Apartment","Ross","I'm not possessive. I just care about Rachel a lot.","我不是占有欲强。我只是很在乎Rachel。","00:05:00","A2")
S(3,24,"Central Perk","Monica","I can't believe we're going to London. This is huge.","我不敢相信我们要去伦敦了。这太重要了。","00:04:00","A2")

# ── 海量扩充：Season 4 ──────────────────────────────────────────
S(4,2,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(4,5,"Central Perk","Rachel","I'm so frustrated with this job search. Nobody wants me.","我对找工作的过程太沮丧了。没人要我。","00:04:00","A2")
S(4,7,"Monica's Apartment","Ross","I can't believe Emily agreed to marry me. I'm so lucky.","我不敢相信Emily答应嫁给我了。我太幸运了。","00:05:00","A2")
S(4,9,"Central Perk","Phoebe","I'm not a lesbian. I just love my friend very deeply.","我不是女同。我只是深深地爱着我的朋友。","00:03:00","B1")
S(4,11,"Monica's Apartment","Joey","I'm not stupid. I'm just not interested in facts.","我不笨。我只是对事实不感兴趣。","00:04:00","B1")
S(4,13,"Central Perk","Monica","I can't believe I'm catering for my mother. This is a nightmare.","我不敢相信我在给我妈做餐饮。这是噩梦。","00:04:00","A2")
S(4,15,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(4,17,"Central Perk","Rachel","I'm not a bad person for returning the gifts. I needed the money.","退货不是坏人的行为。我需要钱。","00:04:00","A2")
S(4,19,"Monica's Apartment","Ross","I can't believe I have to go to London with Emily. I'm so nervous.","我不敢相信我要跟Emily去伦敦了。我好紧张。","00:05:00","A2")
S(4,21,"Central Perk","Phoebe","I'm not a surrogate just for the money. I'm doing a beautiful thing.","我当代孕不是为了钱。我在做一件美丽的事。","00:04:00","A2")
S(4,22,"Monica's Apartment","Joey","I'm not a cheater. I didn't know she was married.","我不是第三者。我不知道她结婚了。","00:05:00","A2")
S(4,24,"London","Monica","I can't believe Chandler and I are together. This is real.","我不敢相信Chandler和我在一起了。这是真的。","00:12:00","A2")

# ── 海量扩充：Season 5 ──────────────────────────────────────────
S(5,1,"Monica's Apartment","Chandler","I can't believe we have to keep this a secret. It's killing me.","我不敢相信我们必须保密。这快把我逼疯了。","00:04:00","A2")
S(5,4,"Central Perk","Rachel","I'm so mad at Ross. He ruined everything with Emily.","我太生Ross的气了。他毁了一切和Emily的事。","00:04:00","A2")
S(5,6,"Monica's Apartment","Phoebe","I'm not a cop. I'm just pretending to be one for a good cause.","我不是警察。我只是为了正当理由在假扮。","00:04:00","B1")
S(5,9,"Central Perk","Joey","I'm not in love with Rachel. It's just a crush. I think.","我不是爱上了Rachel。只是有好感。我觉得。","00:05:00","A2")
S(5,11,"Monica's Apartment","Ross","I can't believe I got fired from the museum. I loved that job.","我不敢相信我被博物馆开除了。我超爱那份工作。","00:04:00","A2")
S(5,13,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(5,15,"Monica's Apartment","Monica","I can't believe Ross lost it over a sandwich. A sandwich!","不敢相信Ross为了三明治疯了。一个三明治！","00:03:00","B1")
S(5,17,"Central Perk","Rachel","I'm not ready to date again. I need time for myself.","我还没准备好重新约会。我需要自己的时间。","00:04:00","A2")
S(5,19,"Monica's Apartment","Phoebe","I'm very proud of my massage skills. I'm the best in the city.","我为我的按摩技术骄傲。我是全城最好的。","00:03:00","B1")
S(5,21,"Central Perk","Ross","I'm not a bad driver. I just get distracted easily.","我不是坏司机。我只是容易分心。","00:04:00","A2")
S(5,23,"Las Vegas","Joey","I'm not drunk. I'm just very, very happy.","我没醉。我只是非常非常开心。","00:05:00","B1")

# ── 海量扩充：Season 6 ──────────────────────────────────────────
S(6,3,"Central Perk","Rachel","I can't believe Ross and I got married in Vegas. This is insane.","不敢相信我和Ross在拉斯维加斯结婚了。太疯狂了。","00:05:00","A2")
S(6,5,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(6,7,"Central Perk","Phoebe","I'm not a runner. Running is for people who are being chased.","我不是跑步的人。跑步是被追的人才做的事。","00:04:00","B1")
S(6,9,"Monica's Apartment","Ross","I'm fine. I'm totally fine. Everything is perfectly fine.","我很好。我完全没事。一切都完美地好。","00:05:00","A2")
S(6,11,"Central Perk","Monica","I'm not a bridezilla. I just want everything to be perfect.","我不是新娘狂。我只是想让一切都完美。","00:04:00","B1")
S(6,14,"Monica's Apartment","Joey","I'm not an idiot. I just don't read books. Or newspapers.","我不是白痴。我只是不看书。也不看报纸。","00:03:00","B1")
S(6,16,"Central Perk","Rachel","I can't believe I'm living with Joey. It's actually really fun.","不敢相信我和Joey住在一起。其实还挺好玩的。","00:04:00","A2")
S(6,19,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(6,21,"Central Perk","Phoebe","I'm very excited about my new boyfriend. He's a cop!","我对新男友太兴奋了。他是个警察！","00:04:00","A2")
S(6,23,"Monica's Apartment","Ross","I can't believe Rachel is moving out. This changes everything.","不敢相信Rachel要搬出去了。这改变了一切。","00:05:00","A2")

# ── 海量扩充：Season 7 ──────────────────────────────────────────
S(7,2,"Central Perk","Monica","I'm so happy about the engagement. This is the best time of my life.","我对订婚太开心了。这是我人生最好的时刻。","00:03:00","A2")
S(7,5,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(7,8,"Central Perk","Rachel","I can't believe I kissed my assistant. That was so inappropriate.","不敢相信我亲了我的助理。太不合适了。","00:04:00","A2")
S(7,11,"Monica's Apartment","Phoebe","I'm not crazy about the name. But I love the person behind it.","我不太喜欢这名字。但我爱这名字背后的人。","00:04:00","B1")
S(7,14,"Central Perk","Ross","I'm not a bad wedding planner. I'm just new at this.","我不是糟糕的婚礼策划。我只是新手。","00:04:00","A2")
S(7,17,"Monica's Apartment","Joey","I'm not replacing Chandler. I'm just keeping Monica company.","我不是在取代Chandler。我只是陪陪Monica。","00:04:00","A2")
S(7,20,"Central Perk","Chandler","I can't believe I'm getting married. This is actually happening.","不敢相信我要结婚了。这件事真的要发生了。","00:05:00","A2")
S(7,23,"Monica's Apartment","Monica","I'm not nervous about the wedding. I'm just very focused.","我不是对婚礼紧张。我只是非常专注。","00:04:00","B1")

# ── 海量扩充：Season 8 ──────────────────────────────────────────
S(8,3,"Monica's Apartment","Rachel","I can't believe I'm pregnant. I'm gonna be a mom.","不敢相信我怀孕了。我要当妈妈了。","00:04:00","A2")
S(8,5,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(8,7,"Monica's Apartment","Phoebe","I'm not a doctor. I just play one in my mind.","我不是医生。我只是在自己心里扮演。","00:04:00","B1")
S(8,11,"Central Perk","Ross","I can't believe the father of Rachel's baby is... complicated.","不敢相信Rachel孩子的父亲...很复杂。","00:05:00","A2")
S(8,14,"Monica's Apartment","Joey","I'm not in love with Rachel. I just really like her. A lot.","我没有爱上Rachel。我只是很喜欢她。非常喜欢。","00:04:00","B1")
S(8,17,"Central Perk","Monica","I can't believe we're going to have a baby in the apartment.","不敢相信我们公寓里要有宝宝了。","00:04:00","A2")
S(8,20,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(8,22,"Hospital","Rachel","I can't believe I'm in labor. This is really happening.","不敢相信我在分娩。真的在发生。","00:05:00","A2")
S(8,24,"Hospital","Monica","I can't believe we might not get the baby. This is devastating.","不敢相信我们可能拿不到宝宝了。这太让人崩溃了。","00:06:00","B1")

# ── 海量扩充：Season 9 ──────────────────────────────────────────
S(9,2,"Monica's Apartment","Ross","I'm a professor at NYU. I'm an adult now. Kind of.","我是NYU的教授了。我是成年人了。算是吧。","00:04:00","A2")
S(9,5,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(9,8,"Monica's Apartment","Phoebe","I'm not good at dating two guys at once. I feel so guilty.","我不擅长同时约会两个人。我觉得好愧疚。","00:04:00","A2")
S(9,11,"Central Perk","Rachel","I can't believe I have feelings for Ross again. Not again.","不敢相信我又对Ross有感觉了。又来。","00:04:00","A2")
S(9,14,"Monica's Apartment","Joey","I'm not in love with Rachel. I'm over it. Almost.","我没有爱上Rachel。我走出来了。差不多。","00:04:00","B1")
S(9,17,"Central Perk","Monica","I can't believe Chandler took a job in Tulsa. This is so hard.","不敢相信Chandler去Tulsa工作了。太难受了。","00:04:00","A2")
S(9,20,"Monica's Apartment","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(9,22,"Central Perk","Ross","I can't believe Rachel might move to Paris. I can't lose her.","不敢相信Rachel可能要搬去巴黎。我不能失去她。","00:05:00","A2")

# ── 海量扩充：Season 10 ──────────────────────────────────────────
S(10,1,"Monica's Apartment","Monica","I can't believe we're trying to have a baby. This is huge.","不敢相信我们在尝试要孩子。这是大事。","00:04:00","A2")
S(10,4,"Central Perk","Chandler","I'm not great at the advice. Can I interest you in a sarcastic comment?","我不擅长给建议。你想听一句讽刺的话吗？","00:03:00","B1")
S(10,6,"Monica's Apartment","Phoebe","I'm not weird. I'm just different from other people. In a good way.","我不怪。我只是和别人不同。以好的方式。","00:03:00","B1")
S(10,9,"Central Perk","Ross","I can't believe Rachel is leaving for Paris. I have to tell her.","不敢相信Rachel要去巴黎了。我必须告诉她。","00:05:00","A2")
S(10,12,"Monica's Apartment","Joey","I'm not sad about Chandler moving. I'm happy for him. Kind of.","Chandler搬走我不难过。我为他高兴。算是吧。","00:04:00","B1")
S(10,15,"Central Perk","Rachel","I'm so torn between my career and my heart. This is impossible.","我在事业和感情之间太纠结了。这不可能。","00:05:00","B1")
S(10,16,"Monica's Apartment","Monica","I can't believe we're adopting. This is our dream coming true.","不敢相信我们要领养了。这是我们的梦想成真。","00:04:00","A2")
S(10,18,"Airport","Ross","I can't let you go. I love you. I've always loved you.","我不能让你走。我爱你。我一直爱你。","00:14:00","A2")
S(10,18,"Monica's Apartment","Chandler","This is not goodbye. This is just... see you later.","这不是再见。这只是...待会见。","00:18:00","A2")
S(10,18,"Central Perk","Phoebe","I'm gonna miss this place. I'm gonna miss all of you.","我会想念这个地方的。我会想念你们所有人的。","00:20:00","A2")
S(10,18,"Central Perk","Monica","We've been through so much together. You're my family.","我们一起经历了这么多。你们是我的家人。","00:21:00","A2")

# ═══════════════════════════════════════════════════════════════
# 处理数据
# ═══════════════════════════════════════════════════════════════

scripts = []
vocab_index = {}

for i, entry in enumerate(raw):
    sid = f"s{entry['season']:02d}e{entry['episode']:02d}_{i:04d}"

    # 提取关键词 (去除常见停用词)
    words = [w.strip(".,!?;:'\"") for w in entry['text'].split()]
    keywords = []
    stopwords = {'a','an','the','is','am','are','was','were','be','been','being','have','has','had',
                 'do','does','did','will','would','could','should','may','might','shall','can',
                 'to','of','in','for','on','with','at','by','from','as','into','through','during',
                 'and','but','or','nor','so','yet','both','either','neither','not','no',
                 'i','me','my','we','us','our','you','your','he','him','his','she','her','it','its',
                 'they','them','their','this','that','these','those','what','which','who','whom',
                 'just','very','really','too','only','all','some','any','more','much','many',
                 'gonna','gotta','wanna','yeah','oh','ok','okay','well','hey','hi','hello',
                 'how','when','where','why','there','here','now','then','than',
                 'im','i\'m','dont','don\'t','cant','can\'t','isn\'t','wasn\'t'}

    for w in words:
        clean = w.lower().strip(".,!?;:'\"()")
        if clean and len(clean) > 1 and clean not in stopwords:
            keywords.append(clean)
            # 构建倒排索引
            if clean not in vocab_index:
                vocab_index[clean] = []
            if sid not in vocab_index[clean]:
                vocab_index[clean].append(sid)

    scripts.append({
        "id": sid,
        "season": entry["season"],
        "episode": entry["episode"],
        "title": "",
        "scene": entry["scene"],
        "speaker": entry["speaker"],
        "text": entry["text"],
        "textCN": entry["textCN"],
        "timestamp": entry["timestamp"],
        "difficulty": entry["difficulty"],
        "keywords": list(set(keywords))[:8],
        "youtube_id": entry.get("youtube_id",""),
        "youtube_start": entry.get("youtube_start",0)
    })

random.seed(42)
random.shuffle(scripts)

# 生成每日推送队列
daily_queue = []
for i in range(0, len(scripts), 10):
    day = i // 10 + 1
    chunk = scripts[i:i+10]
    daily_queue.append({
        "day": day,
        "sentences": [s["id"] for s in chunk]
    })

# ═══════════════════════════════════════════════════════════════
# 写入文件
# ═══════════════════════════════════════════════════════════════

with open(os.path.join(OUT_DIR, "scripts.json"), "w") as f:
    json.dump(scripts, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT_DIR, "vocab_index.json"), "w") as f:
    json.dump(vocab_index, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT_DIR, "daily_queue.json"), "w") as f:
    json.dump(daily_queue, f, ensure_ascii=False, indent=2)

total_words = sum(len(v) for v in vocab_index.values())
print(f"✅ 台词总数: {len(scripts)}")
print(f"✅ 词汇索引: {len(vocab_index)} 个词, {total_words} 次出现")
print(f"✅ 每日推送: {len(daily_queue)} 天的内容")
