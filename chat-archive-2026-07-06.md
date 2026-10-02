### Mon, Jul 6th, 2026

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:23 UTC</span>

<span style="font-size: 90%;">Hello</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">18:31:22 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**jit** <span style="color: grey; font-size: 90%;">18:31:30 UTC</span>

<span style="font-size: 90%;">Hi everyone!!</span>

**azurit** <span style="color: grey; font-size: 90%;">18:32:56 UTC</span>

<span style="font-size: 90%;">Hi</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:33:26 UTC</span>

<span style="font-size: 90%;">Hello hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:28 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is still travelling from Vienna</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:14 UTC</span>

<span style="font-size: 90%;">It's been a busy week, with our first LTS release of the v4 line, and the Open WAF Day in Vienna.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:41 UTC</span>

<span style="font-size: 90%;">Thanks to everyone who helped to make the Open WAF Day and the LTS release possible! :pray:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:07 UTC</span>

<span style="font-size: 90%;">_@airween_ put a couple of PRs on the agenda for discussion, all by hackingrepo. What did you want to discuss about them, specifically?</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:35 UTC</span>

<span style="font-size: 90%;">what's our aim? :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:25 UTC</span>

<span style="font-size: 90%;">I mean there are a couple of reported issues, and I was the duty, but I think I can't decide which issue is valid and which one is that we don't need to care</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:58 UTC</span>

<span style="font-size: 90%;">for eg take a look at 4698:
[github.com/coreruleset/coreruleset/issues/4698](https://github.com/coreruleset/coreruleset/issues/4698)

I don't think that's a valid issue, but this is just my personal opinion. Hackingrepo finally closed, but I think we should talk about the demand - de we want to give a solution for that request?</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:09 UTC</span>

<span style="font-size: 90%;">and all the others</span>

**azurit** <span style="color: grey; font-size: 90%;">18:42:10 UTC</span>

<span style="font-size: 90%;">We should discuss them all. In this case i think that `du` is going to do lots of FPs. And probably that is why it's blocked from PL3.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:42:43 UTC</span>

<span style="font-size: 90%;">I see the need for this command. But I also see the FPs.</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:46 UTC</span>

<span style="font-size: 90%;">but `du` does not causes any triggered rule, see the PL3 report. The triggered rules were:
920273 PL4 Invalid character in request (outside of very strict set)
949110 PL? Inbound Anomaly Score Exceeded (Total Score: 5)
980170 PL? Anomaly Scores: (Inbound Scores: blocking=5, detection=5, per_pl=0-0-0-5, threshold=5) - (Outbound Scores: blocking=0, detection=0, per_pl=0-0-0-0, threshold=4) - (SQLI=0, XSS=0, RFI=0, LFI=0, RCE=0, PHPI=0, HTTP=0, SESS=0, COMBINED_SCORE=5)or where is the PL3 block?</span>

**airween** <span style="color: grey; font-size: 90%;">18:44:36 UTC</span>

<span style="font-size: 90%;">the issue is about the reporter wants to add `du` itself - not `bin/du`, which is already added:
[github.com/coreruleset/coreruleset/blob/…/unix-shell.data#…](https://github.com/coreruleset/coreruleset/blob/3440bfbe62378c309127a6951aa136a3c94a68c3/rules/unix-shell.data#L183)</span>

**airween** <span style="color: grey; font-size: 90%;">18:44:57 UTC</span>

<span style="font-size: 90%;">so, do we want to add Unix commands without directories?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:44:59 UTC</span>

<span style="font-size: 90%;">Sorry, it's blocked in PL4.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:45:20 UTC</span>

<span style="font-size: 90%;">Well, maybe we should blocked it from PL2 of 3.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:45:32 UTC</span>

<span style="font-size: 90%;">*or</span>

**jit** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;">Can anyone take at look at this issue: [https://github.com/coreruleset/coreruleset/issues/4702](https://github.com/coreruleset/coreruleset/issues/4702)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;">I don't think we can block it at lower levels, especially not without a path prefix.</span>

**airween** <span style="color: grey; font-size: 90%;">18:45:51 UTC</span>

<span style="font-size: 90%;">Sorry, it's blocked in PL4.blocked, because of `Invalid character in request`, and not because of the request contains `du` command</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:05 UTC</span>

<span style="font-size: 90%;">I don't think we can block it at lower levels, especially not without a path prefix.agree</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:30 UTC</span>

<span style="font-size: 90%;">I agree as well</span>

**azurit** <span style="color: grey; font-size: 90%;">18:46:45 UTC</span>

<span style="font-size: 90%;">Lower levels?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:46:48 UTC</span>

<span style="font-size: 90%;">What's that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:00 UTC</span>

<span style="font-size: 90%;">PL</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:01 UTC</span>

<span style="font-size: 90%;">Lower than 4?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:24 UTC</span>

<span style="font-size: 90%;">Well, maybe, but certainly not a PL 2.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:40 UTC</span>

<span style="font-size: 90%;">PL4 is too high.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:42 UTC</span>

<span style="font-size: 90%;">But anyway, for me at least, all of them need a bit more time to analyze.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:54 UTC</span>

<span style="font-size: 90%;">I can take some time this week and look into them.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:55 UTC</span>

<span style="font-size: 90%;">So maybe we can agree on PL3.</span>

**airween** <span style="color: grey; font-size: 90%;">18:48:34 UTC</span>

<span style="font-size: 90%;">we block unix commands on PL1...</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:38 UTC</span>

<span style="font-size: 90%;">As for 4702 (_@jit_), at least the casing argument they make is not valid if the shell is case-insenitive. So that will need some more analysis as well.</span>

**airween** <span style="color: grey; font-size: 90%;">18:48:43 UTC</span>

<span style="font-size: 90%;">$ curl -H "x-format-output: txt-matched-rules" '[https://sandbox.coreruleset.org/?file=bin/du](https://sandbox.coreruleset.org/?file=bin/du)'
932160 PL1 Remote Command Execution: Unix Shell Code Found</span>

**azurit** <span style="color: grey; font-size: 90%;">18:48:54 UTC</span>

<span style="font-size: 90%;">_@airween_ But this one has only 2 chars.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:12 UTC</span>

<span style="font-size: 90%;">Yes, but `du` is a German pronoun</span>

##### Tue, Jul 7th, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">07:31:58 UTC</span>

<span style="font-size: 90%;">`du` is also very much used in french.</span>

### Mon, Jul 6th, 2026

**airween** <span style="color: grey; font-size: 90%;">18:49:59 UTC</span>

<span style="font-size: 90%;">I know - this is why I want to refuse to add `du` itself. And I think adding any Unix command without path is a bad idea</span>

**azurit** <span style="color: grey; font-size: 90%;">18:50:15 UTC</span>

<span style="font-size: 90%;">Well, probably.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:08 UTC</span>

<span style="font-size: 90%;">If any of you could look into those issues in the following days and give your opinion, that would be very helpful. I'll try to do the same.</span>

**airween** <span style="color: grey; font-size: 90%;">18:51:48 UTC</span>

<span style="font-size: 90%;">thank you</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:16 UTC</span>

<span style="font-size: 90%;">Is there anything else to discuss for tonight?</span>

**airween** <span style="color: grey; font-size: 90%;">18:52:35 UTC</span>

<span style="font-size: 90%;">not from me</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:43 UTC</span>

<span style="font-size: 90%;">no</span>

**azurit** <span style="color: grey; font-size: 90%;">18:54:05 UTC</span>

<span style="font-size: 90%;">Do we know anything about this years Dev retreat?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:35 UTC</span>

<span style="font-size: 90%;">Then, I just wanted to thank all of you for your work. I've been very absent for some months and I won't be able to jump back in fully for a while. So thanks for picking up the slack.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:04 UTC</span>

<span style="font-size: 90%;">_@airween_ has offered to organise another retreat in Hungary.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Take care of yourself!</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:31 UTC</span>

<span style="font-size: 90%;">yeah, if _@xanadu_ doesn't want to do that in South UK</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:11 UTC</span>

<span style="font-size: 90%;">Exactly. I haven't heard from him yet. And given his recent absence I think we will need to move forward. I'll try contacting him again and let you know _@airween_</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:25 UTC</span>

<span style="font-size: 90%;">ok, thank you</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:47 UTC</span>

<span style="font-size: 90%;">but anyway, I'm happy to organize the retreat again - welcome guys :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:58 UTC</span>

<span style="font-size: 90%;">Palinka!</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:08 UTC</span>

<span style="font-size: 90%;">Egészségetekre!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:21 UTC</span>

<span style="font-size: 90%;">Yes, cheers!</span>

**azurit** <span style="color: grey; font-size: 90%;">18:57:28 UTC</span>

<span style="font-size: 90%;">It was too low of palenka last time. :confused:</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:40 UTC</span>

<span style="font-size: 90%;">Palinka!oh, I started to collect a few really unique tastes... :stuck_out_tongue:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">When we get to alcohol, I think it's a good time to close the meeting :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:18 UTC</span>

<span style="font-size: 90%;">Enjoy your evening everyone. See you soon!</span>

**azurit** <span style="color: grey; font-size: 90%;">18:58:23 UTC</span>

<span style="font-size: 90%;">We are just TALKING about it.</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:32 UTC</span>

<span style="font-size: 90%;">good night!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:58:36 UTC</span>

<span style="font-size: 90%;">Have a good evening/night all!</span>

**azurit** <span style="color: grey; font-size: 90%;">18:58:40 UTC</span>

<span style="font-size: 90%;">Night.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:41 UTC</span>

<span style="font-size: 90%;">Good night everyone!</span>

**jit** <span style="color: grey; font-size: 90%;">18:58:51 UTC</span>

<span style="font-size: 90%;">Goodnight everyone !! :night_with_stars:</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">18:59:03 UTC</span>

<span style="font-size: 90%;">Goodnight all</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:59:05 UTC</span>

<span style="font-size: 90%;">[github.com/coreruleset/coreruleset/issues/4701#…](https://github.com/coreruleset/coreruleset/issues/4701#issuecomment-4896527809)</span>

**airween** <span style="color: grey; font-size: 90%;">19:00:06 UTC</span>

<span style="font-size: 90%;">We are just TALKING about it.may be you... but...</span>

**airween** <span style="color: grey; font-size: 90%;">19:00:08 UTC</span>

<span style="font-size: 90%;"></span>

**airween** <span style="color: grey; font-size: 90%;">19:00:54 UTC</span>

<span style="font-size: 90%;">(it's home-made plum pálinka)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:01:25 UTC</span>

<span style="font-size: 90%;">Did you say taxi driver? :taxi:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:05:12 UTC</span>

<span style="font-size: 90%;">no, this is from a different source :slightly_smiling_face:</span>

↳ **azurit** <span style="color: grey; font-size: 90%;">19:07:41 UTC</span>

<span style="font-size: 90%;">slivovica</span>

##### Tue, Jul 7th, 2026

↳ **jit** <span style="color: grey; font-size: 90%;">10:22:48 UTC</span>

<span style="font-size: 90%;">Just checked and pálinka has an alcohol content of 37.5 to 86% :smile:</span>

↳ **azurit** <span style="color: grey; font-size: 90%;">11:05:00 UTC</span>

<span style="font-size: 90%;">Home-made are 50+. :grin:</span>

### Mon, Jul 6th, 2026

**Dan Kegel** <span style="color: grey; font-size: 90%;">20:21:34 UTC</span>

<span style="font-size: 90%;">runcon shouldn't have many fps, the rest are a bit harder.</span>

