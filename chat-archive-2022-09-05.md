### Mon, Sep 5th, 2022

**dune73** <span style="color: grey; font-size: 90%;">18:30:15 UTC</span>

<span style="font-size: 90%;">Hello everybody, it's CRS chat time!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:30:22 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:30:31 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:30:51 UTC</span>

<span style="font-size: 90%;">Heyhooooo!</span>

**Vandan** <span style="color: grey; font-size: 90%;">18:30:54 UTC</span>

<span style="font-size: 90%;">Hello:wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:30:54 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:11 UTC</span>

<span style="font-size: 90%;">Hey ho!</span>

**jptosso** <span style="color: grey; font-size: 90%;">18:31:11 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:14 UTC</span>

<span style="font-size: 90%;">Hey _@jptosso_, _@Paul Beckett_, _@theMiddle_, _@emphazer_, _@xanadu_, good to have you all here tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:25 UTC</span>

<span style="font-size: 90%;">Hello _@Vandan_, thank you for joining!</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">Hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:30 UTC</span>

<span style="font-size: 90%;">Hey _@fzipitria_</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:41 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:08 UTC</span>

<span style="font-size: 90%;">Hello _@airween_!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:20 UTC</span>

<span style="font-size: 90%;">Please everybody welcome _@Alessandro Monachesi_ who is working on marketing for us!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:22 UTC</span>

<span style="font-size: 90%;">hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:24 UTC</span>

<span style="font-size: 90%;">Or PR!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:32 UTC</span>

<span style="font-size: 90%;">Hi _@walter_</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">18:32:33 UTC</span>

<span style="font-size: 90%;">Or whatever</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:49 UTC</span>

<span style="font-size: 90%;">PR is already taken by pull request, so better call it marketing or communication</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">18:33:06 UTC</span>

<span style="font-size: 90%;">I prefer communication, then.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:03 UTC</span>

<span style="font-size: 90%;">So this meeting is a bit special for various reasons. The biggest one perhaps is that we are preparing a security release. This is due to the security findings we received via the bug bounty program and it's now time to push this out the door. If things work out during the week.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:28 UTC</span>

<span style="font-size: 90%;">But before we get started, let's look at the preliminary agenda at
[https://github.com/coreruleset/coreruleset/issues/2755](https://github.com/coreruleset/coreruleset/issues/2755)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:11 UTC</span>

<span style="font-size: 90%;">There are a couple of new blog posts listed, one is particularly interesting, since it provides a how to guide for CRS, Coraza and Caddy. Written by _@jptosso_ himself.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:23 UTC</span>

<span style="font-size: 90%;">I hope this also allow n00bs like me to run Coraza at last.</span>

↳ **jptosso** <span style="color: grey; font-size: 90%;">18:37:31 UTC</span>

<span style="font-size: 90%;">You can download a precompiled copy of coraza+caddy from here: [https://caddyserver.com/download](https://caddyserver.com/download)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:56 UTC</span>

<span style="font-size: 90%;">That article is at [https://medium.com/@jptosso/oss-waf-stack-using-coraza-caddy-and-elastic-3a715dcbf2f2](https://medium.com/@jptosso/oss-waf-stack-using-coraza-caddy-and-elastic-3a715dcbf2f2)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:58 UTC</span>

<span style="font-size: 90%;">I am starting to do monthly webcasts with CRS news and hands-on operation demos. 30min every month. First edition:Tue Sep 13, 2pm CET.
Subscription at [https://www.meetup.com/meetup-group-ungjkskv/events/287901911/](https://www.meetup.com/meetup-group-ungjkskv/events/287901911/)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:26 UTC</span>

<span style="font-size: 90%;">Researcher Somdev also published a blog post about his bug bounty findings.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:47 UTC</span>

<span style="font-size: 90%;">He gave us proper credit:
ModSecurity with the OWASP Core Rule Set on top is an open-source WAF and if you ask me, it's as good as WAFs get. It is almost impossible to bypass it for XSS, the rules are that good.

Shoutouts to them for maintaining such an important and free project responsibly and thanks to intigriti for hosting this hacking event and inviting me.</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:52 UTC</span>

<span style="font-size: 90%;">Fortunately he only talked about ModSecurity and little about CRS :sunglasses:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:00 UTC</span>

<span style="font-size: 90%;">-> [https://s0md3v.github.io/blog/modsecurity-rce-bypass](https://s0md3v.github.io/blog/modsecurity-rce-bypass)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:19 UTC</span>

<span style="font-size: 90%;">Then, before we dive into the bug bounty findings, there is also something to say about one of the bug bounty hunters: Karel Orgin.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:30 UTC</span>

<span style="font-size: 90%;">What is his handle again? (Been in touch via email with him)</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:38 UTC</span>

<span style="font-size: 90%;">_@Karel_?!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:05 UTC</span>

<span style="font-size: 90%;">Sounds like a hit. _@Karel_ is in a 2nd meeting or so, but he said to call him at the important moments.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:10 UTC</span>

<span style="font-size: 90%;">Now seems to be such a moment.</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:20 UTC</span>

<span style="font-size: 90%;">tumbleweed rolls by</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:37 UTC</span>

<span style="font-size: 90%;">So the point is that Karel provided us with several PR for his bug bounty findings, we talked a big deal with him at various occasion and unlike the other hunters he did not simply wander off once he cashed in the bounty. So we think it's time he add his name somewhere near the developers in the CONTRIBUTORS.md file.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:10 UTC</span>

<span style="font-size: 90%;">(I'm petting our cat, 2 children, calling _@franbuehler_ and solving 2 customer incidents in parallel here)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:20 UTC</span>

<span style="font-size: 90%;">Hey _@franbuehler_!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:25 UTC</span>

<span style="font-size: 90%;">Good to seeyou</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:15 UTC</span>

<span style="font-size: 90%;">We'll see if he reads on the log of this chat, but either way, we're really quite happy he is reinforcing the offensive side of our project.</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:33 UTC</span>

<span style="font-size: 90%;">Yes! Awesome!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:37 UTC</span>

<span style="font-size: 90%;">Ready for bug bounty tasklist?</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:50 UTC</span>

<span style="font-size: 90%;">Yes let’s get cracking!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:53 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:18 UTC</span>

<span style="font-size: 90%;">So there is a ModSecurity release approaching, both release lines. We're not sharing the date in public, but it's time to get ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:36 UTC</span>

<span style="font-size: 90%;">This will cover several of the bug bounty findings we have shared with the project.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:03 UTC</span>

<span style="font-size: 90%;">We will follow suit with a more or less coordinated release for the release lines v.3.2.x and v3.3.x.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:41 UTC</span>

<span style="font-size: 90%;">Covering some other findings. Some of our fixes is already in the nightly builds, some is not.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:18 UTC</span>

<span style="font-size: 90%;">We now need to discuss a few of the open items. We will try to do this in public without sharing too much technical details of the weaknesses, more who is in charge, timeframes etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:38 UTC</span>

<span style="font-size: 90%;">Developers have the separate task list in our google drive, security 2022 folder.</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:47 UTC</span>

<span style="font-size: 90%;">[https://docs.google.com/spreadsheets/d/1Jg8CH7n_mRdj48m1MJZ5u46iQL0IDPpPG0BBUHRsiPw/edit#gid=0](https://docs.google.com/spreadsheets/d/1Jg8CH7n_mRdj48m1MJZ5u46iQL0IDPpPG0BBUHRsiPw/edit#gid=0)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:53 UTC</span>

<span style="font-size: 90%;">One finding that is open is PA09KYZT. We did not come to a conclusion there, but there is a pending PR at [https://github.com/coreruleset/coreruleset-private/pull/2](https://github.com/coreruleset/coreruleset-private/pull/2) by _@studersi_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:20 UTC</span>

<span style="font-size: 90%;">_@xanadu_ and _@fzipitria_ and I think _@theMiddle_ participated in the discussion.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:39 UTC</span>

<span style="font-size: 90%;">I lost track a bit. Can we get this polished / merged in time?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:53:29 UTC</span>

<span style="font-size: 90%;">yep, IMO there's no reason to inspect a text/plain request with "generic" rules looking for sqli or rce or something like that</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:53:46 UTC</span>

<span style="font-size: 90%;">and moreover, I'm expecting a lot of false positive anyway</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:54:18 UTC</span>

<span style="font-size: 90%;">in my prod, I globally block text/plain request ct by default and I allow it on specific path</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:21 UTC</span>

<span style="font-size: 90%;">I think we should expect the same: lots of FP</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">So, remove text/plain from the default allowed_request_content_type?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">But probably have it documented there on the why enabling it is a bad idea</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:55:29 UTC</span>

<span style="font-size: 90%;">I think it would be the best security approach, and let the user choose where allow it</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:47 UTC</span>

<span style="font-size: 90%;">Sounds reasonable and understandable to the user</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:53 UTC</span>

<span style="font-size: 90%;">I'm happy with that and it's relatively easy to describe in the announcement.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:04 UTC</span>

<span style="font-size: 90%;">Who does the PR? Who will review / merge?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">Worst case scenario, if lots of people complain, we can always re-visit…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:42 UTC</span>

<span style="font-size: 90%;">I can help review/merge</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:56:54 UTC</span>

<span style="font-size: 90%;">I can help too if _@studersi_ can't</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:23 UTC</span>

<span style="font-size: 90%;">Studersi is unlikely to attack this before Thu and we better have a PR tomorrow.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:29 UTC</span>

<span style="font-size: 90%;">Can you PR _@theMiddle_?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:57:57 UTC</span>

<span style="font-size: 90%;">you mean from scratch to remove text/plain from the default allowed?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:12 UTC</span>

<span style="font-size: 90%;">I think that's what we decided, if I am not mistaken.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:17 UTC</span>

<span style="font-size: 90%;">Hi :wave:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:58:26 UTC</span>

<span style="font-size: 90%;">yep, I can pr</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:02 UTC</span>

<span style="font-size: 90%;">Hello _@maxleske_, very pleased to see you!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:25 UTC</span>

<span style="font-size: 90%;">Thank you _@theMiddle_. When can you provide the PR, so _@fzipitria_ can review/merge?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:59:51 UTC</span>

<span style="font-size: 90%;">it should be really quick, I can do it tomorrow</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:56 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:15 UTC</span>

<span style="font-size: 90%;">_@airween_, you worked on this before as well. Or am I missing things up now?</span>

**airween** <span style="color: grey; font-size: 90%;">19:00:57 UTC</span>

<span style="font-size: 90%;">I just made some inspect, and helped a bit to _@studersi_</span>

**airween** <span style="color: grey; font-size: 90%;">19:01:06 UTC</span>

<span style="font-size: 90%;">but wasn't any significant work</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:24 UTC</span>

<span style="font-size: 90%;">Got you. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:49 UTC</span>

<span style="font-size: 90%;">The tasklist was wrong.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:52 UTC</span>

<span style="font-size: 90%;">My bad.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:57 UTC</span>

<span style="font-size: 90%;">Then we have a new PR superseding this tricky 2591. The new number is [#2766](https://github.com/coreruleset/coreruleset/issues/#2766).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:16 UTC</span>

<span style="font-size: 90%;">_@maxleske_ you marked it a draft. It is meant to cover two of the open findings, correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:14 UTC</span>

<span style="font-size: 90%;">Not sure what the findings are. It's _@Karel_’s PR with my anchored regex, as discussed. There's still an error in the expression though.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:33 UTC</span>

<span style="font-size: 90%;">I should be able to get it working soon though.</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:44 UTC</span>

<span style="font-size: 90%;">That is great news :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:00 UTC</span>

<span style="font-size: 90%;">That would be FBAZCKVI and 5LT92MNR</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:03 UTC</span>

<span style="font-size: 90%;">FBAZCKVI yes, the other one I'm not sure about.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:09 UTC</span>

<span style="font-size: 90%;">Who is going to review this? I think we should not depend on _@Karel_ even if he is really close.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:25 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ already did a pass on the original PR</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:30 UTC</span>

<span style="font-size: 90%;">I can review also</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:02 UTC</span>

<span style="font-size: 90%;">2591 was meant to cover these two, so I presumed it would cover both as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:06 UTC</span>

<span style="font-size: 90%;">Can you guys check?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:14 UTC</span>

<span style="font-size: 90%;">If not, it's breaking our release, I think.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:27 UTC</span>

<span style="font-size: 90%;">I see. The other one is covered by a separate rule. Give me a moment</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:31 UTC</span>

<span style="font-size: 90%;">I'm checking this also</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:45 UTC</span>

<span style="font-size: 90%;">Thank you both.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:48 UTC</span>

<span style="font-size: 90%;">Yeah, that one should be good. I don't need to touch it</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:54 UTC</span>

<span style="font-size: 90%;">It's part of the same PR</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:14:08 UTC</span>

<span style="font-size: 90%;">Confirmed this also.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:59 UTC</span>

<span style="font-size: 90%;">feeling relieved</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:40 UTC</span>

<span style="font-size: 90%;">Good so you guys will shepherd this. Is Tuesday night realistic (_@walter_ is the release manager and he needs to backport...)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:18 UTC</span>

<span style="font-size: 90%;">Yes, I think so.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:22 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:23 UTC</span>

<span style="font-size: 90%;">Ideally I would do this on Wednesday, so it would be grand if the PRs could be merged Tuesday 23:59 :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:43 UTC</span>

<span style="font-size: 90%;">Ok, these were the easy ones.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:08 UTC</span>

<span style="font-size: 90%;">Anything else you need me for? Otherwise I'll go back into holiday mode :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:14 UTC</span>

<span style="font-size: 90%;">Now let's look at  3UWMWA6W-1 / 3UWMWA6W-2.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:35 UTC</span>

<span style="font-size: 90%;">I think you have done far more than your share. Enjoy! Thank you Max.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:08 UTC</span>

<span style="font-size: 90%;">Trustwave / ModSecurity is covering this with a new directive.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:13:08 UTC</span>

<span style="font-size: 90%;">We have to extend the used parsers with it (seclang-parser, msc_pyparser) - don't forget it :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:09 UTC</span>

<span style="font-size: 90%;">Great, thanks! Talk to you soon! (_@fzipitria_ I'll prepare the PR and let you know).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:40 UTC</span>

<span style="font-size: 90%;">If our backport depends on this directive you need to upgrade your engine to support this or it will stop to work.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:07 UTC</span>

<span style="font-size: 90%;">If the engine is ModSec, upgrade. If your engine is different, you will have to wait.</span>

**airween** <span style="color: grey; font-size: 90%;">19:13:08 UTC</span>

<span style="font-size: 90%;">We have to extend the used parsers with it (seclang-parser, msc_pyparser) - don't forget it :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:13:08 UTC</span>

<span style="font-size: 90%;">We have to extend the used parsers with it (seclang-parser, msc_pyparser) - don't forget it :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:28 UTC</span>

<span style="font-size: 90%;">Good thinking _@airween_. Did not htink of that. Thanks.</span>

**airween** <span style="color: grey; font-size: 90%;">19:13:37 UTC</span>

<span style="font-size: 90%;">I'll take it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:44 UTC</span>

<span style="font-size: 90%;">Now the problem is what are we doing in this situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:17 UTC</span>

<span style="font-size: 90%;">If we had plugin functionality in 3.x, we could do a plugin. But since we don't it's really hard.</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:10 UTC</span>

<span style="font-size: 90%;">Fzipi mentioned a possible Apache specific solution with setting an environment variable (in crs-setup.conf perhaps) and using <IfDefine>. But then we tie ourselves to Apache and make it harder for other engines.</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:21 UTC</span>

<span style="font-size: 90%;">+1 for the plugin. I wouldn't use the new variables for a while longer</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:40 UTC</span>

<span style="font-size: 90%;">We don't have plugins on 3.x</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:02 UTC</span>

<span style="font-size: 90%;">And backporting them is..... dangerous</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:04 UTC</span>

<span style="font-size: 90%;">We can also expect / set an env variable at the engine compile time (thanks to good relations with packagers), but it's really brittle.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:48 UTC</span>

<span style="font-size: 90%;">The proper fix is a breaking fix, so that comes in 4.0.0 only, right?</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:24 UTC</span>

<span style="font-size: 90%;">Or 3.4…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">Personally, I am leaning on releasing without the functionality and providing a mechanism (copy&paste would qualify, patch as well) to update the ruleset by hand once the engine is ready.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:16 UTC</span>

<span style="font-size: 90%;">Well, we can do that.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:32 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ What's wrong with a plugin that sets v3 and v4 scoring variable and include it with a special new include for CRS v3?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:42 UTC</span>

<span style="font-size: 90%;">Breaking change</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:50 UTC</span>

<span style="font-size: 90%;">In what sense?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:09 UTC</span>

<span style="font-size: 90%;">Plugins are part of the v3 major?</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:44 UTC</span>

<span style="font-size: 90%;">We could put the rule in a file by itself and put instructions to remove the file when running on old ModSec?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:19:48 UTC</span>

<span style="font-size: 90%;">Could take the view that modsec engine upgrade is essential due to vulnerability, and just include instructions on how to disable if they want latest 3.x without upgrading engine</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:19 UTC</span>

<span style="font-size: 90%;">Now, they are not. But let's assume CRS v3.x is release with an additional rule file and then we announce how to load it via  new include. The additional rule file happens to be the plugin rule file.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:41 UTC</span>

<span style="font-size: 90%;">That's an interesting thought, _@Paul Beckett_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:00 UTC</span>

<span style="font-size: 90%;">Yes, good point</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">Personally I think given crs is for security, it would be nice if the default was secure.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:57 UTC</span>

<span style="font-size: 90%;">New rule file REQUEST-922-3UWMWA6W, remove if not running latest ModSec?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:22:12 UTC</span>

<span style="font-size: 90%;">I tend to agree, but then we depend on upstream packagers to follow</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:28 UTC</span>

<span style="font-size: 90%;">_@airween_, any news on that?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">But on the CVE release we can state what is the proper fix for it.</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">from Debian? Unfortunately nothing :disappointed:</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:30 UTC</span>

<span style="font-size: 90%;">I thought today that will contact Alberto again, what can we do now...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:32 UTC</span>

<span style="font-size: 90%;">But you have Alberto on your side, don't you?</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:37 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:59 UTC</span>

<span style="font-size: 90%;">Remember today is labor day in the US</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:01 UTC</span>

<span style="font-size: 90%;">theoretically (based on his message) we can upload the fixes to stable releases too</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:07 UTC</span>

<span style="font-size: 90%;">I guess he has the means to push this and the other distros will probably look at Debian how to handle it, when we explain why we are doing it this way.</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:36 UTC</span>

<span style="font-size: 90%;">and then (I guess) Ubuntu will get them</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:57 UTC</span>

<span style="font-size: 90%;">I’m hoping Ubuntu will backport all the modsec patches…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:25:30 UTC</span>

<span style="font-size: 90%;">Once there is a CVE, things are going to be easier</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:32 UTC</span>

<span style="font-size: 90%;">I think it's save to say that we can release it this way and indicate that the package depends on a given ModSec package version.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:43 UTC</span>

<span style="font-size: 90%;">And the release notes explain how to remove by hand.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:25:59 UTC</span>

<span style="font-size: 90%;">I like this approach</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:02 UTC</span>

<span style="font-size: 90%;">Me too. It's so good to discuss these things with everybody and then suddenly we get new solutions.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:22 UTC</span>

<span style="font-size: 90%;">This is really quite neat. (Given the bad situation.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:18 UTC</span>

<span style="font-size: 90%;">Now the question is, who is developing the rules to cover for these two findings. The rules will be practically identical. I have the patch. All we need is a volunteer with some time to kill.</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:20 UTC</span>

<span style="font-size: 90%;">I talked with xanadu and he made a salient point from our security declaration: “CRS Change Policy
The Core Rule Set project endeavors not to make breaking changes in minor releases…”</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:26 UTC</span>

<span style="font-size: 90%;">We “endeavor” but we don’t absolutely guarantee</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:22 UTC</span>

<span style="font-size: 90%;">There is a reason for flexible wording. I would not have it any other way. We need some legroom sometimes. And it's obvious why it applies in this situaiton.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:59 UTC</span>

<span style="font-size: 90%;">I would volunteer to write these rules, but I am teaching tomorrow and then a 2h meeting and then a hyper important meeting Wednesday morning. So I am really busy.</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:09 UTC</span>

<span style="font-size: 90%;">You already have a patch, it just needs to be turned into two PRs?</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:22 UTC</span>

<span style="font-size: 90%;">I am also terribly busy but if nobody has the time, I can try…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:36 UTC</span>

<span style="font-size: 90%;">If there is a patch, I can push it</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:53 UTC</span>

<span style="font-size: 90%;">that would be my preference, I’m not sure I would make it in time</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:24 UTC</span>

<span style="font-size: 90%;">How can it be reviewed and tested if it uses a new ModSecurity directive?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:33:36 UTC</span>

<span style="font-size: 90%;">We can use the sandbox</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:34:20 UTC</span>

<span style="font-size: 90%;">agree</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:25 UTC</span>

<span style="font-size: 90%;">We have the ModSec Patch that brings the new collection once you compile ModSec yourself. We need the rule now that says now to certain items in the collection.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:33 UTC</span>

<span style="font-size: 90%;">Ah :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:49 UTC</span>

<span style="font-size: 90%;">ahhh</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:54 UTC</span>

<span style="font-size: 90%;">Felipe and Walter have the patch so, so have _@theMiddle_ and _@airween_.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:58 UTC</span>

<span style="font-size: 90%;">So we need the rule</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">Ack</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:48 UTC</span>

<span style="font-size: 90%;">For the record: it's 3 items that need to be denied. Look at 3UWMWA6W-1 and 3UWMWA6W-2 and don't forget the less critical 3UWMWA6W-3.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:45 UTC</span>

<span style="font-size: 90%;">One problem is that testing will fail until we have the docker containers patched</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:55 UTC</span>

<span style="font-size: 90%;">Assuming we simply deny this stuff at PL1 or at PL2 if we are conservative. (If PL2, it's even easier to tell people to remove it unless they are running PL2, but then we are less secure by default).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">And we cannot patch until the official release</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:11 UTC</span>

<span style="font-size: 90%;">That is indeed a problem.</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:11 UTC</span>

<span style="font-size: 90%;">Yes… that’s troubling…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:23 UTC</span>

<span style="font-size: 90%;">I mean we can test using the sandbox</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">But if you test locally and sacrifice something to github gods?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:40 UTC</span>

<span style="font-size: 90%;">But the release will be delayed probably until we have it merged</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">We can always force push</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:00 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:06 UTC</span>

<span style="font-size: 90%;">We're releasing after ModSec anyways I guess.</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:06 UTC</span>

<span style="font-size: 90%;">I’m wondering if it wouldn’t be better to release a bit later than ModSecurity… The tempo is fast, we are doing wild changes, we do not have good testing capabilities. The time between PRs and release would be less than a day. I’m scared of having a faulty release.</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:44 UTC</span>

<span style="font-size: 90%;">Ideally at least I would want to test it out on some traffic… Even then it will be short…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:00 UTC</span>

<span style="font-size: 90%;">I agree with you.</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:00 UTC</span>

<span style="font-size: 90%;">I agree with _@walter_ - I think we can afford some delay for us</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">Also, maybe more people will have upgraded their ModSecurity</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:20 UTC</span>

<span style="font-size: 90%;">But technically you can start to test immediately. As soon as you compile ModSec with the patches.</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:01 UTC</span>

<span style="font-size: 90%;">I will prepare the parsers tomorrow (they also part of our CI system)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:17 UTC</span>

<span style="font-size: 90%;">The problem is you do not want to release Friday afternoon, nor on the weekend and depending on the ModSec release date it's suddenly a 5-7 days with people attacking servers.</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:13 UTC</span>

<span style="font-size: 90%;">That is true.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">How about 30 hours after ModSec?</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:49 UTC</span>

<span style="font-size: 90%;">So Thursday? That would give us a day for testing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:58 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:29 UTC</span>

<span style="font-size: 90%;">30 hours?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:49 UTC</span>

<span style="font-size: 90%;">On top, most of the things discussed here are meant to be merged by Tues night. So you can start on live traffic before the ModSec release outside of the infamous new collection.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:50 UTC</span>

<span style="font-size: 90%;">That would depend on when they release</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:25 UTC</span>

<span style="font-size: 90%;">also I'm expecting that researchers will share information just after the new modsec release</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:38 UTC</span>

<span style="font-size: 90%;">Very well possible.</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:13 UTC</span>

<span style="font-size: 90%;">We could ask them to hold off maybe</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:44 UTC</span>

<span style="font-size: 90%;">Just for 48 houyrs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:48 UTC</span>

<span style="font-size: 90%;">The researchers? Yes, that could be an option.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:05 UTC</span>

<span style="font-size: 90%;">It's only a handful of them and I've been in touch with regards of our announcement.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:21 UTC</span>

<span style="font-size: 90%;">So I can ask them to postpone until after our release.</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:30 UTC</span>

<span style="font-size: 90%;">After all the CRS was their scope, so it seems reasonable to wait after our patch</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:41 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:13 UTC</span>

<span style="font-size: 90%;">Releasing doesn't mean people will install anything</span>

↳ **Paul Beckett** <span style="color: grey; font-size: 90%;">19:46:24 UTC</span>

<span style="font-size: 90%;">Well that's the age old problem of people not patching/maintaining their systems, but not much we can do about that other than provide fix and announcement</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:45 UTC</span>

<span style="font-size: 90%;">The real showstopper is going to be the CVEs out</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:49 UTC</span>

<span style="font-size: 90%;">Correct, but that's why we write the announcement.
For non-devs: There will be CVEs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:40 UTC</span>

<span style="font-size: 90%;">_@walter_ is releasing Thu night after a day of live traffic with full backports realistic?</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:06 UTC</span>

<span style="font-size: 90%;">It’s a bit crazy, but it might just work…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:47:44 UTC</span>

<span style="font-size: 90%;">(lame question: full backports also means that patch+new-crs-release will not breaks anything?)</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:59 UTC</span>

<span style="font-size: 90%;">it will break on old ModSec</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:05 UTC</span>

<span style="font-size: 90%;">k</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:09 UTC</span>

<span style="font-size: 90%;">tnx</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:31 UTC</span>

<span style="font-size: 90%;">so we have to inform people how to remove those rules if they run old ModSec. I guess we will get a lot of issues about this</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:43 UTC</span>

<span style="font-size: 90%;">but our recommendation would be to upgrade ModSec asap</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:54 UTC</span>

<span style="font-size: 90%;">of course then there are the integrators who will have to deal with it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:05 UTC</span>

<span style="font-size: 90%;">I'm feeling uneasy with all of this as well. But honestly, the situation is overwhelming and has been like this all Summer. If we stumble we re-release. Happened before. But look at the Apache guys last Winter ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:30 UTC</span>

<span style="font-size: 90%;">that’s true!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:51 UTC</span>

<span style="font-size: 90%;">I think we can handle this just fine. Announcement and dev-on-duty will cover for any questions.</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:18 UTC</span>

<span style="font-size: 90%;">okay, so I think we made a decision, right? we are going to use the new modsec variable, but we will put it in a separate file for easy removal. just, somebody has to write the rules tomorrow :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:54 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ kind of volunteered, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:03 UTC</span>

<span style="font-size: 90%;">And in the end, we blame it all on _@Paul Beckett_.</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:11 UTC</span>

<span style="font-size: 90%;">ack, first said counts</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:48 UTC</span>

<span style="font-size: 90%;">Very good. Looking over the task list looks like the findings are covered.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:52 UTC</span>

<span style="font-size: 90%;">what if we rename the new file with something human understandable like "patch-for-x.y.z" ?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:13 UTC</span>

<span style="font-size: 90%;">request-922-patch-for-x.y.z ?</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:14 UTC</span>

<span style="font-size: 90%;">or MODSEC-2.9.8-3.0.8-ONLY.conf</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:22 UTC</span>

<span style="font-size: 90%;">looks good!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:31 UTC</span>

<span style="font-size: 90%;">more easier to understand</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:36 UTC</span>

<span style="font-size: 90%;">I keep forgetting their numbers, these should be corrected :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:50 UTC</span>

<span style="font-size: 90%;">Please prefix with REQUEST-92x, I do not care about the rest.</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:02 UTC</span>

<span style="font-size: 90%;">wait, will we release two versions (or more)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:04 UTC</span>

<span style="font-size: 90%;">For 4.0 we will probably want to shift the rule to 921.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:24 UTC</span>

<span style="font-size: 90%;">4.0 is unreleased, so there's more time there</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:35 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:51 UTC</span>

<span style="font-size: 90%;">_@airween_ yes, our policy is to support 2 latest versions. so that would mean, we would get 3.3.3 and 3.2.2 (with breaking change that’s easy to mitigate for old ModSec users)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:54:01 UTC</span>

<span style="font-size: 90%;">So, if someone cannot perform an engine upgrade, they simply must live with the 3UWMWA6W vuln.?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:54:12 UTC</span>

<span style="font-size: 90%;">Or are we providing an alternative workaround?</span>

**airween** <span style="color: grey; font-size: 90%;">19:54:14 UTC</span>

<span style="font-size: 90%;">sorry, I mean will we have two configuration files?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:54 UTC</span>

<span style="font-size: 90%;">The announcement might also include a description how to disable the type of request that allows this. Might help a few people while killing other systems.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:00 UTC</span>

<span style="font-size: 90%;">They really should updated.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:55:23 UTC</span>

<span style="font-size: 90%;">Understood. That seems like a fair approach.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:36 UTC</span>

<span style="font-size: 90%;">_@xanadu_ has prepared the CVE advisory text. I will review this, ideally with the help of _@Alessandro Monachesi_. We can then write the announcement, ideally together.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:26 UTC</span>

<span style="font-size: 90%;">Our bug bounty program partner is probably happy to be named, but they would like to read the announcement beforehand. I will try to do this, or maybe delegate to _@xanadu_ with the right contacts.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:56:45 UTC</span>

<span style="font-size: 90%;">I'll help whichever way I can.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:56 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:05 UTC</span>

<span style="font-size: 90%;">With this, I think the release planning is over.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:16 UTC</span>

<span style="font-size: 90%;">Anything we forgot in this direction?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:42 UTC</span>

<span style="font-size: 90%;">I hear nothing and I reckon our communication partner _@Alessandro Monachesi_ petrified while trying to follow our conversation. If you read this, please move your right hand or some other sign ... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:28 UTC</span>

<span style="font-size: 90%;">We merged 30 PRs since our last meeting which is really impressive. Even if this all feels so slow, we are actually very productive.</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:14 UTC</span>

<span style="font-size: 90%;">for the 3UWMWA6W group: there would be an another way to fix it, as I wrote - make rules with t:base64decode. But that would be hard, and generates few questions.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:00:43 UTC</span>

<span style="font-size: 90%;">Indeed.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:00:57 UTC</span>

<span style="font-size: 90%;">And we can't rely on multiMatch</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:01:18 UTC</span>

<span style="font-size: 90%;">yes, for example...</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:01:22 UTC</span>

<span style="font-size: 90%;">would that not require changes to hundreds of rules?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:01:42 UTC</span>

<span style="font-size: 90%;">That would only cover base64, right? Other examples would not be stopped?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:01:48 UTC</span>

<span style="font-size: 90%;">no, that's one of the questions: which rules do we have to copy?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:01:50 UTC</span>

<span style="font-size: 90%;">(I don't want to say too much in the public channel.)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:02:25 UTC</span>

<span style="font-size: 90%;">Let’s move this to another channel</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:00:26 UTC</span>

<span style="font-size: 90%;">Absolutely!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:42 UTC</span>

<span style="font-size: 90%;">Ah, sorry _@airween_. We should have discussed this here as well. I think  - and I think I am not alone - your workaround is really complex. Overly complex and risky for a backport. It is a cool idea, but given we have the new directives after the update, I think it is an unnecessary risk for those users who are willing and able to update ModSec.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:03:03 UTC</span>

<span style="font-size: 90%;">yes, agree - that's very complex.

Right, then we will use the new ModSec feature</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:53 UTC</span>

<span style="font-size: 90%;">Sorry, I have to go. Good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:05 UTC</span>

<span style="font-size: 90%;">Bye, bye _@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:00 UTC</span>

<span style="font-size: 90%;">Thank you _@airween_. I knew you would understand.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:25 UTC</span>

<span style="font-size: 90%;">So there are quite a few PRs open, but I also think they are moving forward and I do not see any that needs our particular attention. Opinions?</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:56 UTC</span>

<span style="font-size: 90%;">there is a new PR which fixes a BB issue</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:56 UTC</span>

<span style="font-size: 90%;">I only want to spend time on the release if possible, if not I prefer to take some rest which I’ll need this week :)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:56 UTC</span>

<span style="font-size: 90%;">We are also seeing idle issues being closed automatically. This is unfortunate, but we really need to set our priorities and the bug bounty is burying everything.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:07 UTC</span>

<span style="font-size: 90%;">That makes a lot of sense.</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/2763](https://github.com/coreruleset/coreruleset/pull/2763)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:19 UTC</span>

<span style="font-size: 90%;">Thank you _@walter_. We won't be to olong any more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:01 UTC</span>

<span style="font-size: 90%;">Yes, true. This needs to go into the release as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:04 UTC</span>

<span style="font-size: 90%;">I will either review myself or get Simon to review and merge. OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:14 UTC</span>

<span style="font-size: 90%;">Adding it to the release task list as well.</span>

**airween** <span style="color: grey; font-size: 90%;">20:07:20 UTC</span>

<span style="font-size: 90%;">yes, thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:27 UTC</span>

<span style="font-size: 90%;">Let's look at the list of sub-projects quickly.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:08:32 UTC</span>

<span style="font-size: 90%;">BTW, ModSecurity updated their security policy to:
# Security Policy

## Supported Versions

The latest versions of both v2.9.x and v3.0.x are supported.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:08:46 UTC</span>

<span style="font-size: 90%;">What did they say before?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:48 UTC</span>

<span style="font-size: 90%;">Wow. No longer legacy?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:10 UTC</span>

<span style="font-size: 90%;">The file didn’t existed on their repo</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:16 UTC</span>

<span style="font-size: 90%;">SECURITY.md                                              |  9 +++++++++</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:16 UTC</span>

<span style="font-size: 90%;">Oooh</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:33 UTC</span>

<span style="font-size: 90%;">Good to read 2.9 is a full citizen.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:42 UTC</span>

<span style="font-size: 90%;">v3.x.y - YYYY-MMM-DD (to be released)
-------------------------------------

  - Prevent LMDB related segfault
    [Issue [#2755](https://github.com/coreruleset/coreruleset/issues/#2755), [#2761](https://github.com/coreruleset/coreruleset/issues/#2761) - @dvershinin]
  - Fix msc_transaction_cleanup function comment typo
    [Issue [#2788](https://github.com/coreruleset/coreruleset/issues/#2788) - @lookat23]
  - Fix: MULTIPART_INVALID_PART connected to wrong internal variable
    [Issue [#2785](https://github.com/coreruleset/coreruleset/issues/#2785) - @martinhsv]
  - Restore Unique_id to include random portion after timestamp
    [Issue [#2752](https://github.com/coreruleset/coreruleset/issues/#2752), [#2758](https://github.com/coreruleset/coreruleset/issues/#2758) - @datkps11, @martinhsv]</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:10:30 UTC</span>

<span style="font-size: 90%;">hm they already push the commit in the public repo?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:00 UTC</span>

<span style="font-size: 90%;">❯ more CHANGES
DD mmm YYYY - 2.9.x (to be released)
-------------------

 * IIS: Update dependencies for next planned release
   [@martinhsv]
 * XML parser cleanup: NULL duplicate pointer
   [Issue [#2760](https://github.com/coreruleset/coreruleset/issues/#2760) - @martinhsv]
 * Properly cleanup XML parser contexts upon completion
   [Issue [#2239](https://github.com/coreruleset/coreruleset/issues/#2239) - @argenet]
 * Fix memory leak in streams
   [Issue [#2208](https://github.com/coreruleset/coreruleset/issues/#2208) - @marcstern, @vloup, @JamesColeman-LW]
 * Fix: negative usec on log line when data type long is 32b
   [Issue [#2753](https://github.com/coreruleset/coreruleset/issues/#2753) - @ABrauer-CPT, @martinhsv]
 * mlogc log-line parsing fails due to enhanced timestamp
   [Issue [#2682](https://github.com/coreruleset/coreruleset/issues/#2682) - @bozhinov, @ABrauer-CPT, @martinhsv]
 * Allow no-key, single-value JSON body
   [Issue [#2735](https://github.com/coreruleset/coreruleset/issues/#2735) - @marcstern, @martinhsv]
 * Set SecStatusEngine Off in modsecurity.conf-recommended
   [Issue [#2717](https://github.com/coreruleset/coreruleset/issues/#2717) - @un99known99, @martinhsv]
 * Fix memory leak that occurs on JSON parsing error
   [Issue [#2236](https://github.com/coreruleset/coreruleset/issues/#2236) @argenet, @vloup, @martinhsv]
 * Multipart names/filenames may include single quote if double-quote enclosed
   [Issue [#2352](https://github.com/coreruleset/coreruleset/issues/#2352) @martinhsv]
 * Add SecRequestBodyJsonDepthLimit to modsecurity.conf-recommended
   [Issue [#2647](https://github.com/coreruleset/coreruleset/issues/#2647) @theMiddleBlue, @airween, @877509395 ,@martinhsv]
 * IIS: Update dependencies for Windows build as of v2.9.5
   [@martinhsv]</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:20 UTC</span>

<span style="font-size: 90%;">Yes, they announced they would do this sooner or later without making too much noise ...</span>

**airween** <span style="color: grey; font-size: 90%;">20:11:47 UTC</span>

<span style="font-size: 90%;">but the commit does not have any relevant code
[https://github.com/SpiderLabs/ModSecurity/commit/b41139acd6eb7eb1844ec5c4245ad810f23cbfa0](https://github.com/SpiderLabs/ModSecurity/commit/b41139acd6eb7eb1844ec5c4245ad810f23cbfa0)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:48 UTC</span>

<span style="font-size: 90%;">2352 is really helpful!</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:06 UTC</span>

<span style="font-size: 90%;">just saying "hi, I'm coming..."</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:11 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:12:13 UTC</span>

<span style="font-size: 90%;">Oooh! That fixes the Italian/French file names issue?</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:13 UTC</span>

<span style="font-size: 90%;">about...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:19 UTC</span>

<span style="font-size: 90%;">That's the one.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:11 UTC</span>

<span style="font-size: 90%;">Now looking at the subproject, the sandbox already has the ModSec patches. Unfortunately, Coraza backend is no longer working. What I am understanding, we will not debug until Coraza v3 replaces our existing backend.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:39 UTC</span>

<span style="font-size: 90%;">Anything else on the sandbox front _@theMiddle_ / _@fzipitria_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:05 UTC</span>

<span style="font-size: 90%;">Not much I guess. :slightly_smiling_face:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:15:41 UTC</span>

<span style="font-size: 90%;">Not a priority for now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:28 UTC</span>

<span style="font-size: 90%;">Unless _@xanadu_ corrects me, there are little updates to technical blog posts and documentation.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:39 UTC</span>

<span style="font-size: 90%;">Equally status page.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:47 UTC</span>

<span style="font-size: 90%;">But interesting updates to Coraza: Coraza is moving towards v3 and claims to have improved the performance a big deal bringing it on par with ModSec3 on NGINX (which is still way slower than ModSec2 on Apache). Juan Pablo also claims he is closer to solving fundamental problems with NGINX integration of Coraza.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:13 UTC</span>

<span style="font-size: 90%;">The two Google Summer of Code projects are coming to an end soon. The first one by _@Vandan_ is really impressive and we will get a separate demo and a presentation about it. Given the time zone, I guess our student is back to sleep.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:21 UTC</span>

<span style="font-size: 90%;">The 2nd one, the ML plugin, is available as a PR for the plugin. Azurit is actively commenting the PR and after being really slow in the beginning this took up some pace in late July and August and I think it looks quite presentable now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:47 UTC</span>

<span style="font-size: 90%;">There is not much left to say outside of two things.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:51 UTC</span>

<span style="font-size: 90%;">As you know we are doing our dev retreat late October / early November in Northern Italy. We have plenty of (single bed) rooms and I hope to see as many of you as possible. It's time to sort out participation and we will start to work on the program for the week. Volunteers welcome!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:10 UTC</span>

<span style="font-size: 90%;">There is a separate channel "crs-it-retreat-2022".</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:41 UTC</span>

<span style="font-size: 90%;">Please tell me about your plans via DM or I will get in touch with you individually.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:09 UTC</span>

<span style="font-size: 90%;">And finally communication: _@Alessandro Monachesi_. We shared our plans with communication before.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:54 UTC</span>

<span style="font-size: 90%;">As one of his first jobs, Alessandro set up a linkedin page: [https://www.linkedin.com/company/87169854](https://www.linkedin.com/company/87169854)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:27 UTC</span>

<span style="font-size: 90%;">He is slowly taking up social media coverage for us. But will probably take some time to feel at ease with the topics we are covering and how to push them.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:50 UTC</span>

<span style="font-size: 90%;">What else is up _@Alessandro Monachesi_?</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:22:19 UTC</span>

<span style="font-size: 90%;">Exactly. There are four "employees" registered on the LinkedIn profile as of now. Would it make sense to have more?</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:22:54 UTC</span>

<span style="font-size: 90%;">Else we have planned to do some blog posts, especially some developer portraits.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:55 UTC</span>

<span style="font-size: 90%;">Absolutely.</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:56 UTC</span>

<span style="font-size: 90%;">I think so yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:38 UTC</span>

<span style="font-size: 90%;">So if you do not mind, please go to Linkedin if you are active there, and use CRS as one of your employers.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:23:41 UTC</span>

<span style="font-size: 90%;">Should everybody put "OWASP ModSecurity Core Rule Set as employer in their LinkedIn profiles?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:48 UTC</span>

<span style="font-size: 90%;">Unfortunately no benefits or salary...</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:24:18 UTC</span>

<span style="font-size: 90%;">365 days of unpaid holiday every year!</span>

↳ **Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:24:31 UTC</span>

<span style="font-size: 90%;">Yessss!</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:41 UTC</span>

<span style="font-size: 90%;">Once you've completed your tasks.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:49 UTC</span>

<span style="font-size: 90%;">A bit like home office at Tesla.</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:49 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:11 UTC</span>

<span style="font-size: 90%;">Blog Post will start sooner or later too. It's a bit a resource question as Alessandro is mainly the editor.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:27 UTC</span>

<span style="font-size: 90%;">And then there is this idea of developer portraits. We will publish 3 of them this year.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:25:51 UTC</span>

<span style="font-size: 90%;">And we want to do an interview with _@dune73_ for the Swiss IT trade press</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:53 UTC</span>

<span style="font-size: 90%;">The idea - as you may recall - was to promote the coolness of becoming a CRS developer.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:19 UTC</span>

<span style="font-size: 90%;">(We'll see how that  interview goes ...)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:48 UTC</span>

<span style="font-size: 90%;">Alessandro will contact you directly with reagrds to these portraits.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:26:58 UTC</span>

<span style="font-size: 90%;">And then there is the maybe not so aptly named "succes story".</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:27:13 UTC</span>

<span style="font-size: 90%;">success</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:21 UTC</span>

<span style="font-size: 90%;">Which will be a Coraza / CRS success story. _@fzipitria_ is setting this up for us.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:28:07 UTC</span>

<span style="font-size: 90%;">I think that's it for the rest of this year.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:29 UTC</span>

<span style="font-size: 90%;">That will keep us busy, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:47 UTC</span>

<span style="font-size: 90%;">And unless there is anything else, I think we can call it a day / night and close this meeting.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:29:21 UTC</span>

<span style="font-size: 90%;">Oh, yes ...!:sweat_smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:46 UTC</span>

<span style="font-size: 90%;">:partying_face: good chat!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:01 UTC</span>

<span style="font-size: 90%;">Thank you all for attending. This was super productive tonight!</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:18 UTC</span>

<span style="font-size: 90%;">Yes thanks all!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:33 UTC</span>

<span style="font-size: 90%;">thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:50 UTC</span>

<span style="font-size: 90%;">See all around, looking forward to this release - and good night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:54 UTC</span>

<span style="font-size: 90%;">Bye!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:30:56 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:31:03 UTC</span>

<span style="font-size: 90%;">Cheers!</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:11 UTC</span>

<span style="font-size: 90%;">good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:31:11 UTC</span>

<span style="font-size: 90%;">good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:43 UTC</span>

<span style="font-size: 90%;">good nigth?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:32:50 UTC</span>

<span style="font-size: 90%;">Good night</span>

