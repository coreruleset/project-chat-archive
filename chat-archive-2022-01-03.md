### Mon, Jan 3rd, 2022

**walter** <span style="color: grey; font-size: 90%;">19:30:01 UTC</span>

<span style="font-size: 90%;">hello!</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:27 UTC</span>

<span style="font-size: 90%;">hi everyone! :wave:</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:32 UTC</span>

<span style="font-size: 90%;">I was on time - this deserves an award</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:30:45 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:57 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:17 UTC</span>

<span style="font-size: 90%;">Hello everybody. Welcome to the 3rd 2020 in a row!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:41 UTC</span>

<span style="font-size: 90%;">Covid numbers are rising and CRS is having a blast!</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:16 UTC</span>

<span style="font-size: 90%;">it’s crazy</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:18 UTC</span>

<span style="font-size: 90%;">hello everybody</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:45 UTC</span>

<span style="font-size: 90%;">Good to see you all. _@emphazer_ left for 2 weeks without connection and Azurit has a new year's resolution: Bringing the baby to bed earlier. I reckon the daughter is not yet convinced to join this resolution.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:35 UTC</span>

<span style="font-size: 90%;">_@jptosso_ told me he would join too, and maybe we'll see _@SpartanTri_ as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:30 UTC</span>

<span style="font-size: 90%;">December was apparently a hot month for Infosec. I have assembled several links in the agenda. We released our sandbox and put it to the test immediately with a log4j bypass contest.</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:53 UTC</span>

<span style="font-size: 90%;">Yes. In a lot of ways Log4j was good for us.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:58 UTC</span>

<span style="font-size: 90%;">This got us some very good feedback, since all the commercial vendors did blog posts where they did not share any details about the log4j defenses.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:10 UTC</span>

<span style="font-size: 90%;">We were different and many people noticed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:53 UTC</span>

<span style="font-size: 90%;">Interesting is a link I saw today of a cloud API gateway with CRS support. I'm currently trying to make the contact.</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:22 UTC</span>

<span style="font-size: 90%;">Did't want we open a new issue for monthly chat(s)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:58 UTC</span>

<span style="font-size: 90%;">?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">Use [877509395](https://github.com/877509395) wrote some not related comments there... but never mind...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:49 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2330#issuecomment-990910606](https://github.com/coreruleset/coreruleset/issues/2330#issuecomment-990910606)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:11 UTC</span>

<span style="font-size: 90%;">Our agenda is at
[https://github.com/coreruleset/coreruleset/issues/2330](https://github.com/coreruleset/coreruleset/issues/2330)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:08 UTC</span>

<span style="font-size: 90%;">Let's start with the PRs on the agenda then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:25 UTC</span>

<span style="font-size: 90%;">We merged 14 PRs, which is a slowdown, likely due to log4j and also the xmas holidays.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:33 UTC</span>

<span style="font-size: 90%;">We'll see if the pace accelerates again.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:57 UTC</span>

<span style="font-size: 90%;">First PR to look into tonight is [#2345](https://github.com/coreruleset/coreruleset/issues/#2345) by _@xanadu_.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:40:38 UTC</span>

<span style="font-size: 90%;">Good evening. Sorry I'm late</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:41 UTC</span>

<span style="font-size: 90%;">Hello Paul!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:51 UTC</span>

<span style="font-size: 90%;">No worries, we only just started</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:41:04 UTC</span>

<span style="font-size: 90%;">PR [#2345](https://github.com/coreruleset/coreruleset/issues/#2345) undoes the last [\\\\] change, moving to \x5c. It needs someone to check it and then it is good to go, I think :)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:41:13 UTC</span>

<span style="font-size: 90%;">Hopefully a quick one for someone to do.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:24 UTC</span>

<span style="font-size: 90%;">Who could cast an eye on this?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:41:44 UTC</span>

<span style="font-size: 90%;">me</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:49 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:03 UTC</span>

<span style="font-size: 90%;">[#2343](https://github.com/coreruleset/coreruleset/issues/#2343) is an FP fix at PL4 for phpBB.</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:21 UTC</span>

<span style="font-size: 90%;">LGTM</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:26 UTC</span>

<span style="font-size: 90%;">We don't guarantee absence of FPs at PL3 and 4, but I think there is nothing wrong with adding.</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:42:32 UTC</span>

<span style="font-size: 90%;">Hello</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:55 UTC</span>

<span style="font-size: 90%;">I’m going to merge 2343</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:23 UTC</span>

<span style="font-size: 90%;">I'm not sure about 941100 being removed. He talks of PL4, but that's the PL1 XSS rule on the redirect parameter.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:43:40 UTC</span>

<span style="font-size: 90%;">Hi everyone!</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:33 UTC</span>

<span style="font-size: 90%;">yeah, but that redirect URL can be quite loaded, contain query parameters, etc… I think the possibilities of abusing this in an exploit are rather small..</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:57 UTC</span>

<span style="font-size: 90%;">OK, then let's merge.</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:36 UTC</span>

<span style="font-size: 90%;">done!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:42 UTC</span>

<span style="font-size: 90%;">941100 was already removed before. He removes 942432 now</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:05 UTC</span>

<span style="font-size: 90%;">no 941100 is still in there, it was just moved</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:07 UTC</span>

<span style="font-size: 90%;">Ah, gotcha. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:20 UTC</span>

<span style="font-size: 90%;">He also reorders the REs and I overlooked that.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:29 UTC</span>

<span style="font-size: 90%;">Even better then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">[#2333](https://github.com/coreruleset/coreruleset/issues/#2333) is a fix for the regex assembly of of 920120.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:08 UTC</span>

<span style="font-size: 90%;">What's line 45 of the PR again here, _@maxleske_?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:49 UTC</span>

<span style="font-size: 90%;">Ah, Max is not even here.</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:54 UTC</span>

<span style="font-size: 90%;">oops</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:04 UTC</span>

<span style="font-size: 90%;">looks like a comment that might have gotten accidentally committed</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:48:45 UTC</span>

<span style="font-size: 90%;"> ##!$`: the suffix comment</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:47 UTC</span>

<span style="font-size: 90%;">Not so sure. The new regex assembly syntax is very powerful and expressive</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:13 UTC</span>

<span style="font-size: 90%;">This is a suffix comment.
Should I have a look at this one and talk to Max if I have any questions?</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:21 UTC</span>

<span style="font-size: 90%;">that would be great!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:23 UTC</span>

<span style="font-size: 90%;">That would be most welcome.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:26 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:26 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:25 UTC</span>

<span style="font-size: 90%;">[#2323](https://github.com/coreruleset/coreruleset/issues/#2323) has stalled with broken tests, Max taking a peek and Azurit not responding. I think we need to postpone this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">Let's move to [#2206](https://github.com/coreruleset/coreruleset/issues/#2206). This is the new smtp / pop3 / imap group of rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:23 UTC</span>

<span style="font-size: 90%;">Very welcome initiative by Felipe. It takes a proper review with the RFC in hand. Also because there is an open question about terminating \r\n.</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:27 UTC</span>

<span style="font-size: 90%;">very nice! more exploits!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:43 UTC</span>

<span style="font-size: 90%;">More exploits that we catch!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:35 UTC</span>

<span style="font-size: 90%;">Who would like to take a closer look at this?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:55 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ would you have time for a proper review here?</span>

↳ **SpartanTri** <span style="color: grey; font-size: 90%;">19:54:26 UTC</span>

<span style="font-size: 90%;">which item is it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:38 UTC</span>

<span style="font-size: 90%;">[#2206](https://github.com/coreruleset/coreruleset/issues/#2206)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:52 UTC</span>

<span style="font-size: 90%;">Ah, no. [#2322](https://github.com/coreruleset/coreruleset/issues/#2322)!</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:55:24 UTC</span>

<span style="font-size: 90%;">I can review it</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:49 UTC</span>

<span style="font-size: 90%;">it’s looking quite good already. I would be willing to run it in order to detect FPs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:54 UTC</span>

<span style="font-size: 90%;">Thank you _@SpartanTri_.</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:32 UTC</span>

<span style="font-size: 90%;">my customers can take a little hit, now that they didn’t suffer from log4j</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:08 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ if you like it, ping me and I will run the rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:36 UTC</span>

<span style="font-size: 90%;">[#2299](https://github.com/coreruleset/coreruleset/issues/#2299) is waiting for a review by _@walter_. Any progress there?</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:44 UTC</span>

<span style="font-size: 90%;">totally my fault due to life circumstances. I will take another stab this weekend. OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:03 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:08 UTC</span>

<span style="font-size: 90%;">And [#2288](https://github.com/coreruleset/coreruleset/issues/#2288) is waiting for a review by myself. I've been overly busy will try and merge this during the week.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:31 UTC</span>

<span style="font-size: 90%;">AFAICT [#2259](https://github.com/coreruleset/coreruleset/issues/#2259) is almost ready. But we have lint complaining and a nitpicking comment by myself.</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:54 UTC</span>

<span style="font-size: 90%;">oh that’s strange about lint</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:21 UTC</span>

<span style="font-size: 90%;">======================
20
= Linting YAML files =
21
======================
22
Error: [trailing-spaces] trailing spaces
23
Error: [new-line-at-end-of-file] no new line character at the end of file
24
Error: Process completed with exit code 1.</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:25 UTC</span>

<span style="font-size: 90%;">looks like a small problem</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:28 UTC</span>

<span style="font-size: 90%;">Felipe thinks it's ready to merge, though according to the label. So I do not really know. I'd really like the regex to be fully disassembled to re-assembly.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:53 UTC</span>

<span style="font-size: 90%;">Ah, good that lint is no big deal.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:47 UTC</span>

<span style="font-size: 90%;">Anybody seems something else that is a problem with this PR?
Otherwise we we need to assign a reviewer, wait for Felipe's return so the small issues can be dealt with and then merge.</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:48 UTC</span>

<span style="font-size: 90%;">:rolling_on_the_floor_laughing:
http://⑯⑨。②⑤④。⑯⑨｡②⑤④
 http://⓪ⓧⓐ⑨｡⓪ⓧⓕⓔ｡⓪ⓧⓐ⑨｡⓪ⓧⓕⓔ
 http://⓪ⓧⓐ⑨ⓕⓔⓐ⑨ⓕⓔ
 http://②⑧⑤②⓪③⑨①⑥⑥
 http://④②⑤｡⑤①⓪｡④②⑤｡⑤①⓪
 http://⓪②⑤①。⓪③⑦⑥。⓪②⑤①。⓪③⑦⑥
 http://⓪⓪②⑤①｡⓪⓪⓪③⑦⑥｡⓪⓪⓪⓪②⑤①｡⓪⓪⓪⓪⓪③⑦⑥
 http://[::①⑥⑨｡②⑤④｡⑯⑨｡②⑤④]
 http://[::ⓕⓕⓕⓕ:①⑥⑨。②⑤④。⑯⑨。②⑤④]
 http://⓪ⓧⓐ⑨。⓪③⑦⑥。④③⑤①⑧
 http://⓪ⓧⓐ⑨｡⑯⑥⑧⑨⑥⑥②
 http://⓪⓪②⑤①。⑯⑥⑧⑨⑥⑥②
 http://⓪⓪②⑤①｡⓪ⓧⓕⓔ｡④③⑤①⑧</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:13 UTC</span>

<span style="font-size: 90%;">why oh why do webservers even try to convert this..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:21 UTC</span>

<span style="font-size: 90%;">They've been told to be liberal in what they should accept. It's considered a priority in light of resilience.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:57 UTC</span>

<span style="font-size: 90%;">I guess it’s some apps who might do this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:32 UTC</span>

<span style="font-size: 90%;">Crazy</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">20:06:01 UTC</span>

<span style="font-size: 90%;">I’m now scared of User-agent</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:22 UTC</span>

<span style="font-size: 90%;">I can not really tell. I've really scared of all the rules where we ignore the user-agent!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:16 UTC</span>

<span style="font-size: 90%;">Does anybody have time to review this?</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:18 UTC</span>

<span style="font-size: 90%;">maybe we should start an issue to track those rules</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:39 UTC</span>

<span style="font-size: 90%;">and then on case-by-case basis add the UA’s</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:39 UTC</span>

<span style="font-size: 90%;">... review this PR?</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:13 UTC</span>

<span style="font-size: 90%;">I would love to but I can’t promise. my life is completely hectic. first free timeslot is Jan 22</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:32 UTC</span>

<span style="font-size: 90%;">if that’s acceptable, I can take it</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:52 UTC</span>

<span style="font-size: 90%;">I can review it, just the assembly, the logic and so on. I can't run it in prod.</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:02 UTC</span>

<span style="font-size: 90%;">I can run in prod, no problem</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:15 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ you take a little look and pass it to me?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:24 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:51 UTC</span>

<span style="font-size: 90%;">OK please notify me when I can do it :)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:56 UTC</span>

<span style="font-size: 90%;">Thanks both of you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:00 UTC</span>

<span style="font-size: 90%;">And with that, we're done with the open PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:14 UTC</span>

<span style="font-size: 90%;">There are quite a few that need action, but there is little we can do here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:57 UTC</span>

<span style="font-size: 90%;">It's probably worth walking over them one by one and see how they can be unstalled. 2-3 might also be dead in the water by now. I'll see if I have the time to do this.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:13:25 UTC</span>

<span style="font-size: 90%;">What about 2222?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:51 UTC</span>

<span style="font-size: 90%;">That has just been shifted to "needs action" as your's truly is supposed to schedule a talk with Azurit. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:01 UTC</span>

<span style="font-size: 90%;">Oh no, sorry, my fault. It' not there anymore</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:18 UTC</span>

<span style="font-size: 90%;">Hehe :smiling_imp:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:49 UTC</span>

<span style="font-size: 90%;">It's looking quite good with finishing this meeting within 60 minutes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:03 UTC</span>

<span style="font-size: 90%;">Shall we look at the dev-retreat topics briefly?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:59 UTC</span>

<span style="font-size: 90%;">We released the sandbox and it received positive feedback. It also proofed very useful with the new log4j instance that we were able to set up immediately and use for a contest.</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:36 UTC</span>

<span style="font-size: 90%;">Yes this was so cool! Great work on everybody who worked their a$$es off!</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:00 UTC</span>

<span style="font-size: 90%;">a${s}${s}es</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:40 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ you promised a call to talk about the setup and _@walter_ will contribute the documentation. Is that still the plan?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:22 UTC</span>

<span style="font-size: 90%;">yep, I’m quite free this week if you are too we can schedule</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:42 UTC</span>

<span style="font-size: 90%;">Who wants to participate in such a call?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:52 UTC</span>

<span style="font-size: 90%;">I would.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:10 UTC</span>

<span style="font-size: 90%;">my schedule is a mess, but I did promise this. I planned to work on the documentation on sat 22 jan. a call in the days ahead would be nice like Wed or Fri (Thursday is booked).</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:19:22 UTC</span>

<span style="font-size: 90%;">some stats since collecting</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:19:55 UTC</span>

<span style="font-size: 90%;">Everyone loves a good graph.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:57 UTC</span>

<span style="font-size: 90%;">wow lots of requests!</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:02 UTC</span>

<span style="font-size: 90%;">impressive</span>

**airween** <span style="color: grey; font-size: 90%;">20:20:05 UTC</span>

<span style="font-size: 90%;">does Coraza stand beside Nginx? :open_mouth:</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:15 UTC</span>

<span style="font-size: 90%;">of course 40.000 were test requests from us probably, but still :rolling_on_the_floor_laughing:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:20:31 UTC</span>

<span style="font-size: 90%;">wooow</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:20:57 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">20:21:12 UTC</span>

<span style="font-size: 90%;">Russia :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:19 UTC</span>

<span style="font-size: 90%;">Well, probably not us then.</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:23 UTC</span>

<span style="font-size: 90%;">yes they want to be up2date on the latest bypasses…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:19 UTC</span>

<span style="font-size: 90%;">So _@theMiddle_ will schedule a call, coordinate with @Walter and please let us all know so we can join in too.</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:37 UTC</span>

<span style="font-size: 90%;">yes please</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:59 UTC</span>

<span style="font-size: 90%;">in the weekend i will then prepare the docs for review</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:02 UTC</span>

<span style="font-size: 90%;">_@walter_ so you can the week from 17th to 23rd? is it correct?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:05 UTC</span>

<span style="font-size: 90%;">_@xanadu_ What's the news on documentation. I've seen _@airween_ work on automatic extraction of information from rules. This sounds like a decent base for a start.</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:40 UTC</span>

<span style="font-size: 90%;">I have timeslots available on 19 and 21 in the afternoon</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:25:30 UTC</span>

<span style="font-size: 90%;">19 at 17:00? it could work for me idk for _@dune73_ and _@fzipitria_</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:26:06 UTC</span>

<span style="font-size: 90%;">That should work AFAICT.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:55 UTC</span>

<span style="font-size: 90%;">oky</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:24:53 UTC</span>

<span style="font-size: 90%;">Only very minor documentation updates from my side:
</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:26:27 UTC</span>

<span style="font-size: 90%;">I should have more time in February, hopefully, to start driving the documentation work forward again. It would be nice to have things mostly finished Q1/Q2! :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:51 UTC</span>

<span style="font-size: 90%;">Ready for the new release would be awesome indeed.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:12 UTC</span>

<span style="font-size: 90%;">What do you need to schedule a docker discussion outside of Felipe being back?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:42 UTC</span>

<span style="font-size: 90%;">I guess just figure out who wants to be involved and schedule a date and time.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:44 UTC</span>

<span style="font-size: 90%;">I can also prepare some bullet points to get people thinking about the open questions…I'll put something together for the Feb meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:57 UTC</span>

<span style="font-size: 90%;">Sounds cool.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:58 UTC</span>

<span style="font-size: 90%;">And then ask who wants to be involved, too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:22 UTC</span>

<span style="font-size: 90%;">Let's say you schedule before we meet in Feb and then people can sign up during our chat.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:29:49 UTC</span>

<span style="font-size: 90%;">Ok, that works, too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:29 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:48 UTC</span>

<span style="font-size: 90%;">Tech blog posts: The Plugin post is almost done but was postponed due to log4j and what not.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:54 UTC</span>

<span style="font-size: 90%;">Planning to release on Wed or so.</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:00 UTC</span>

<span style="font-size: 90%;">wow! awesome!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:17 UTC</span>

<span style="font-size: 90%;">Then I'll attack the next topic. Plus 2-3 other blog posts I have in mind.</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:21 UTC</span>

<span style="font-size: 90%;">you are on :fire:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:28 UTC</span>

<span style="font-size: 90%;">With the status page, we're really stalled due to OWASP not really responding in a useful way and Felipe is apparently away. I hope we can pick this up later in January. I have more and more ideas around this, but we need  a minimum-viable-product first.</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:01 UTC</span>

<span style="font-size: 90%;">makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:03 UTC</span>

<span style="font-size: 90%;">Fire: It feels more like I'm doing the bare minimum to keep the ball rolling ...</span>

**airween** <span style="color: grey; font-size: 90%;">20:33:14 UTC</span>

<span style="font-size: 90%;">I thought [CRS documentation](https://github.com/coreruleset/coreruleset/wiki/DevRetreat21UpdateDocumentation) and [CRS rules](https://github.com/coreruleset/coreruleset/wiki/DevRetreat21RuleDocTemplate) are two different projects</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:33:14 UTC</span>

<span style="font-size: 90%;">I thought [CRS documentation](https://github.com/coreruleset/coreruleset/wiki/DevRetreat21UpdateDocumentation) and [CRS rules](https://github.com/coreruleset/coreruleset/wiki/DevRetreat21RuleDocTemplate) are two different projects</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:29 UTC</span>

<span style="font-size: 90%;">don’t underestimate yourself, you are doing amazing work!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:34 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:58 UTC</span>

<span style="font-size: 90%;">_@airween_: as far as github is concerne, they are, yes. What do you mean exactly?</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:51 UTC</span>

<span style="font-size: 90%;">I think fzipi knew a way to include the rule documentation as part of the autogenerated documentation, but I’m not sure how this ties into airween’s work</span>

**airween** <span style="color: grey; font-size: 90%;">20:35:08 UTC</span>

<span style="font-size: 90%;">just as you wrote above, it seems like the rules documentation is a subset of the "big" documentation. Btw: we should discuss about the rules documentation in the future</span>

**airween** <span style="color: grey; font-size: 90%;">20:35:47 UTC</span>

<span style="font-size: 90%;">_@walter_ I started to work on [this](https://github.com/coreruleset/coreruleset/wiki/DevRetreat21RuleDocTemplate)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:00 UTC</span>

<span style="font-size: 90%;">_@airween_ and _@xanadu_ can you sort this out among yourself, or do you think you need additional people joining?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:23 UTC</span>

<span style="font-size: 90%;">I'm very interested, but I know I would only hold you back because I'm not following up in time.</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:46 UTC</span>

<span style="font-size: 90%;">same for me at this time :disappointed: </span>

**xanadu** <span style="color: grey; font-size: 90%;">20:37:53 UTC</span>

<span style="font-size: 90%;">I think they are 95% separate projects, but the rules documentation may end up living in the same places as the /docs documentation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:38:11 UTC</span>

<span style="font-size: 90%;">I am interested in the rules documentation, but I don't have the scripting wizardry to make the autogenerating magic work :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:38:28 UTC</span>

<span style="font-size: 90%;">I guess that's where _@airween_ you can work your magic :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:30 UTC</span>

<span style="font-size: 90%;">This is where _@airween_ comes in :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:32 UTC</span>

<span style="font-size: 90%;">sounds fair. as long as we are self hosting the docs we are very flexible</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:41 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:47 UTC</span>

<span style="font-size: 90%;">OK with you _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">20:39:28 UTC</span>

<span style="font-size: 90%;">yes, it's ok - but I have few questions. I'll collect them, and perhaps I'll open an issue on GH to discuss them</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:31 UTC</span>

<span style="font-size: 90%;">That sounds like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:34 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:05 UTC</span>

<span style="font-size: 90%;">Almost done now.</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:16 UTC</span>

<span style="font-size: 90%;">!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:03 UTC</span>

<span style="font-size: 90%;">[#2319](https://github.com/coreruleset/coreruleset/issues/#2319) is still open. Yet we seem to agree we need to rename the PL variables, respectively how we call the modes. What we now call blocking PL and executing PL.</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:49 UTC</span>

<span style="font-size: 90%;">do we give one week to vote?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:58 UTC</span>

<span style="font-size: 90%;">I can submit to that. And then a few details about which variable to keep and which ones to abandon. And then ready for the PR. Or did more questions / issues come up with anybody since the big discussion on this issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:47 UTC</span>

<span style="font-size: 90%;">Do you want to do a formal vote? I do not mind, yet I accepted that the names need to go. We'll see if we can keep the simple variable name for the blocking PL.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:43:58 UTC</span>

<span style="font-size: 90%;">I re-read the proposal today and it's still not 100% clear, IMO. This might just be me, though :stuck_out_tongue:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:44:07 UTC</span>

<span style="font-size: 90%;">I thought it might help with an example or two‥</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:44:36 UTC</span>

<span style="font-size: 90%;">(That is, the whole proposal, not just the re-naming of variables. That part is clear.)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:03 UTC</span>

<span style="font-size: 90%;">I think it will clear up once we see the PR. And we can always adjust then. For me, this is more the basic direction and I have only small adjustments to the basic direction.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:25 UTC</span>

<span style="font-size: 90%;">I'll also ask Simon - the reporter - if he wants to do the PR. It possible he will.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:45:46 UTC</span>

<span style="font-size: 90%;">Yes, a concrete PR might be easier to understand.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:48 UTC</span>

<span style="font-size: 90%;">Good.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:20 UTC</span>

<span style="font-size: 90%;">Before we close this, can we talk briefly about the next release? We said Q1 2022 and that is somehow starting as we speak ...</span>

**walter** <span style="color: grey; font-size: 90%;">20:47:39 UTC</span>

<span style="font-size: 90%;">yes!</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:33 UTC</span>

<span style="font-size: 90%;">I think it’s good time to start an issue with all the things we have to get in order for the next release, e.g. plugin documentation…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:48 UTC</span>

<span style="font-size: 90%;">RE pkgs to plugins ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:09 UTC</span>

<span style="font-size: 90%;">And a ton of other things ...</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:19 UTC</span>

<span style="font-size: 90%;">yep this will be one of our most impactful releases (for users). people will really need good documentation</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:21 UTC</span>

<span style="font-size: 90%;">An issue with checkboxes would be really helpful.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:01 UTC</span>

<span style="font-size: 90%;">In the past we struggled with RC candidates being tested. I wonder if we can do something about that problem.</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:16 UTC</span>

<span style="font-size: 90%;">I think we need to start the process earlier</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:27 UTC</span>

<span style="font-size: 90%;">but that also means we have to finish all our todos earlier :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:53 UTC</span>

<span style="font-size: 90%;">I have the feeling almost nobody tries our RCs</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:15 UTC</span>

<span style="font-size: 90%;">Same here. So an earlier freeze and longer RC?</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:24 UTC</span>

<span style="font-size: 90%;">still I think it is the royal way</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:31 UTC</span>

<span style="font-size: 90%;">yes, that would be my idea..</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:42 UTC</span>

<span style="font-size: 90%;">for integrators, a few weeks is really not enough</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:51:48 UTC</span>

<span style="font-size: 90%;">when should we do the freeze?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:52:02 UTC</span>

<span style="font-size: 90%;">Doesn't that depend on how much work is outstanding?</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:25 UTC</span>

<span style="font-size: 90%;">hmm can we set time estimates on github isssues?</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:41 UTC</span>

<span style="font-size: 90%;">I guess we can do it if we go full kanban</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:29 UTC</span>

<span style="font-size: 90%;">we have to spend quite some time to make plugins</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:53:58 UTC</span>

<span style="font-size: 90%;">I'd like to help with RE -> plugins; a good way to learn CRS plugins…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:01 UTC</span>

<span style="font-size: 90%;">The problem with a kanban approach is this is a volunteer project and our real jobs overrule any kanban dashboard.</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:13 UTC</span>

<span style="font-size: 90%;">absolutely true</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:22 UTC</span>

<span style="font-size: 90%;">You're my hero _@xanadu_!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:13 UTC</span>

<span style="font-size: 90%;">What about we try to freeze by Mid-February. Or Mid-March and then 2 months to the release, roughly.</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:53 UTC</span>

<span style="font-size: 90%;">mid-march sounds more reasonable…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:55 UTC</span>

<span style="font-size: 90%;">And maybe Federico is right that we should do annual releases with a clear rhythm instead of release "when we have all the features we want"</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:19 UTC</span>

<span style="font-size: 90%;">That would allow us to talk about the last features in the March issue chat and then 10 days to merge them.</span>

**airween** <span style="color: grey; font-size: 90%;">20:56:24 UTC</span>

<span style="font-size: 90%;">just an idea - do we want to use the GH "projects" feature?
[https://github.com/coreruleset/coreruleset/projects](https://github.com/coreruleset/coreruleset/projects)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:26 UTC</span>

<span style="font-size: 90%;">I think that is viable.</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:35 UTC</span>

<span style="font-size: 90%;">me too</span>

**airween** <span style="color: grey; font-size: 90%;">20:56:58 UTC</span>

<span style="font-size: 90%;">ModSecurity uses it:
[https://github.com/SpiderLabs/ModSecurity/projects](https://github.com/SpiderLabs/ModSecurity/projects)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:07 UTC</span>

<span style="font-size: 90%;">I have not looked into the project feature. A release would be a project?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:57:23 UTC</span>

<span style="font-size: 90%;">a milestone maybe</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:39 UTC</span>

<span style="font-size: 90%;">yes milestones</span>

**airween** <span style="color: grey; font-size: 90%;">20:57:49 UTC</span>

<span style="font-size: 90%;">I do not know too, but yes, we can define milestones, and may be that can help to make plans</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:57:58 UTC</span>

<span style="font-size: 90%;">I think milestones would be great</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:58 UTC</span>

<span style="font-size: 90%;">And then you assign issues to projects / milestones. So it's a bit like a VIP label?</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:03 UTC</span>

<span style="font-size: 90%;">users and customers can see where we are</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:58:16 UTC</span>

<span style="font-size: 90%;">issue or pr to milestones yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:28 UTC</span>

<span style="font-size: 90%;">That does not hurt.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:38 UTC</span>

<span style="font-size: 90%;">I'm open to try this for the next release.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:09 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:34 UTC</span>

<span style="font-size: 90%;">So I guess we're done for tonight. Thank you all for joining and thank you _@franbuehler_ for writing down the decisions!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:00:45 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**walter** <span style="color: grey; font-size: 90%;">21:00:52 UTC</span>

<span style="font-size: 90%;">OK :wave: :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">21:01:07 UTC</span>

<span style="font-size: 90%;">thanks guys, good night! :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:01:08 UTC</span>

<span style="font-size: 90%;">Bye!</span>

**walter** <span style="color: grey; font-size: 90%;">21:01:13 UTC</span>

<span style="font-size: 90%;">have a good week!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:18 UTC</span>

<span style="font-size: 90%;">Bye, bye!</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:01:18 UTC</span>

<span style="font-size: 90%;">bye bye</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:01:23 UTC</span>

<span style="font-size: 90%;">Good night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:03:13 UTC</span>

<span style="font-size: 90%;">good night bye</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">21:47:50 UTC</span>

<span style="font-size: 90%;">good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:09:45 UTC</span>

<span style="font-size: 90%;">Sat down and wrote up my thoughts about the blog post on WAF usage linked earlier today. [https://twitter.com/ChrFolini/status/1478123437948383235](https://twitter.com/ChrFolini/status/1478123437948383235)</span>

