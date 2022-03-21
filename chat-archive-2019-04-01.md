### Mon, Apr 1st, 2019

**walter** <span style="color: grey; font-size: 90%;">18:30:29 UTC</span>

<span style="font-size: 90%;">uh oh :stuck_out_tongue: I guess I will do the needful then</span>

**walter** <span style="color: grey; font-size: 90%;">18:30:37 UTC</span>

<span style="font-size: 90%;">hello everybody, who is here?!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:30:58 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**fgs** <span style="color: grey; font-size: 90%;">18:32:39 UTC</span>

<span style="font-size: 90%;">Not sure how long I will be around (it’s almost time for dinner) but I will try to stay as much as possible</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:58 UTC</span>

<span style="font-size: 90%;">well it’s you and me, we can make quick decisions :wink:</span>

**fgs** <span style="color: grey; font-size: 90%;">18:34:06 UTC</span>

<span style="font-size: 90%;">Yay!</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:40 UTC</span>

<span style="font-size: 90%;">the first vote will be granting a research salary of $10k/m to developers fgs and walter, everyone agree?</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:52 UTC</span>

<span style="font-size: 90%;">let me dig up the agenda…</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:23 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1333> there it is!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:35:58 UTC</span>

<span style="font-size: 90%;">hi all! (little bit busy but I’m reading, sorry :/)</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:14 UTC</span>

<span style="font-size: 90%;">reading is good!</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:48 UTC</span>

<span style="font-size: 90%;">I’ve also been offline a bit more than I would like this month b/c family issues..</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:55 UTC</span>

<span style="font-size: 90%;">but let’s see :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:56 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1113></span>

**walter** <span style="color: grey; font-size: 90%;">18:36:58 UTC</span>

<span style="font-size: 90%;">first issue?</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:15 UTC</span>

<span style="font-size: 90%;">if csanders is waiting for a car then let’s skip this for now</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:35 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1329></span>

**walter** <span style="color: grey; font-size: 90%;">18:38:35 UTC</span>

<span style="font-size: 90%;">this is an interesting add</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:38:54 UTC</span>

<span style="font-size: 90%;">yep, but seems to be prone to a ton of fps</span>

**fgs** <span style="color: grey; font-size: 90%;">18:39:11 UTC</span>

<span style="font-size: 90%;">I’d blame libinjection :confused:</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:28 UTC</span>

<span style="font-size: 90%;">emphazer has some examples yeah..</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:31 UTC</span>

<span style="font-size: 90%;">Matched Data: 1c found within ARGS:token: 9--6nVTjusWqO8_f84sNRMwXlmDvt9J_JDLV6rWzoCc

Matched Data: 1c found within ARGS:AesGroup[_token]: 9--CeqpjEHcaUuZKr24FPQNqGeTfcl4yDkQitZKd_KQ</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:36 UTC</span>

<span style="font-size: 90%;">seems to be the `--` SQL comment :pensive:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:39:40 UTC</span>

<span style="font-size: 90%;">agree with the author for the pl3</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:45 UTC</span>

<span style="font-size: 90%;">`--` is pretty common in paths yeah…</span>

**fgs** <span style="color: grey; font-size: 90%;">18:39:50 UTC</span>

<span style="font-size: 90%;">yeah</span>

**fgs** <span style="color: grey; font-size: 90%;">18:39:57 UTC</span>

<span style="font-size: 90%;">I think worse case it could be moved to PL4</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:53 UTC</span>

<span style="font-size: 90%;">yeah, I think it’s worthwhile at PL3 or maybe even PL2</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:07 UTC</span>

<span style="font-size: 90%;">we have various rules in PL2 with a comparable profile I think</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:14 UTC</span>

<span style="font-size: 90%;">stuff like the `0x` “SQL hex” detection</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:42:31 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:31 UTC</span>

<span style="font-size: 90%;">I see there’s a comment waiting for resolution by the author, once it’s resolved, we accept it in PL3?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:42:36 UTC</span>

<span style="font-size: 90%;">Sorry, I am late...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:40 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:43:56 UTC</span>

<span style="font-size: 90%;">_@walter_ he’s still working on it so let’s wait to hear back from him</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:06 UTC</span>

<span style="font-size: 90%;">cool!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:44:51 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1327> is mine so :+1: from me :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:35 UTC</span>

<span style="font-size: 90%;">oh wow</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:41 UTC</span>

<span style="font-size: 90%;">this removes a lot of stuff</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:52 UTC</span>

<span style="font-size: 90%;">it looks super dangerous :smile:</span>

**fgs** <span style="color: grey; font-size: 90%;">18:46:02 UTC</span>

<span style="font-size: 90%;">:smile:
Def not important so we can move on if it needs discussion</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:22 UTC</span>

<span style="font-size: 90%;">but according to Felipe setting variables is expensive in modsec so this would help us on the performance front</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:37 UTC</span>

<span style="font-size: 90%;">I wonder why we are doing that `tx.%` …</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:48 UTC</span>

<span style="font-size: 90%;">oh, I wonder if this was for the (old) regression test mode…</span>

**fgs** <span style="color: grey; font-size: 90%;">18:47:19 UTC</span>

<span style="font-size: 90%;">Did you see the comments in [#1121](https://github.com/coreruleset/coreruleset/issues/#1121)?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:47:27 UTC</span>

<span style="font-size: 90%;">How did you decide which values we need and which not?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:47:59 UTC</span>

<span style="font-size: 90%;">That PR just removes ~2, `tx.msg` and `tx.%{rule.id}-*`</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:14 UTC</span>

<span style="font-size: 90%;">ah, ok.</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:14 UTC</span>

<span style="font-size: 90%;">I think the `tx.%{rule.id}` is/was for RESPONSE-981-DEBUG.conf</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:57 UTC</span>

<span style="font-size: 90%;">`SecRule TX:/^\d*\-/ "." \`</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:02 UTC</span>

<span style="font-size: 90%;">that seems to iterate over these variables</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:10 UTC</span>

<span style="font-size: 90%;">now I don’t know if anyone besides me uses that debug mode…</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:17 UTC</span>

<span style="font-size: 90%;">do you even know about it? :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:34 UTC</span>

<span style="font-size: 90%;">it’s pretty cool, it gives you the matched rules and scores back in HTTP response headers</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:37 UTC</span>

<span style="font-size: 90%;">:TIL:</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:49 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/v3.2/dev/crs-setup.conf.example#L806>    see here for example</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:12 UTC</span>

<span style="font-size: 90%;">I think this will break without it… but… its usefulness might be debated</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:25 UTC</span>

<span style="font-size: 90%;">if you all are not using it, then maybe nobody does…</span>

**fgs** <span style="color: grey; font-size: 90%;">18:50:36 UTC</span>

<span style="font-size: 90%;">it’s apache specific</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:40 UTC</span>

<span style="font-size: 90%;">yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:50:40 UTC</span>

<span style="font-size: 90%;">Oh, I didn't know that.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:41 UTC</span>

<span style="font-size: 90%;">ah… ehm… really? :smile: but for apache only or is modsec itself to set the response header?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">18:50:41 UTC</span>

<span style="font-size: 90%;">ah… ehm… really? :smile: but for apache only or is modsec itself to set the response header?</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:50 UTC</span>

<span style="font-size: 90%;">yeah it’s apache only, it uses mod_headers</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:57 UTC</span>

<span style="font-size: 90%;">it’s a dirty but lovely trick :smile:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:59 UTC</span>

<span style="font-size: 90%;">ah oky :confused:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:51:05 UTC</span>

<span style="font-size: 90%;">Should we really break a feature?</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:21 UTC</span>

<span style="font-size: 90%;">but I’m not very emotionally invested in it… we have real tests now…</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:37 UTC</span>

<span style="font-size: 90%;">parsing the audit log is more robust….</span>

**fgs** <span style="color: grey; font-size: 90%;">18:51:39 UTC</span>

<span style="font-size: 90%;">I wasn’t aware of that. I can exclude `tx.%{rule.id}` from that PR too</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:32 UTC</span>

<span style="font-size: 90%;">won’t we lose log information with `tx.msg`? it will only repeat the last match right</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:42 UTC</span>

<span style="font-size: 90%;">so I guess it’s a little bit double…</span>

**fgs** <span style="color: grey; font-size: 90%;">18:53:05 UTC</span>

<span style="font-size: 90%;">It’s only used in one rule</span>

**fgs** <span style="color: grey; font-size: 90%;">18:53:17 UTC</span>

<span style="font-size: 90%;">And it’s somewhat limited afaict</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:14 UTC</span>

<span style="font-size: 90%;">I think all things considered I am a fan of this PR</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:51 UTC</span>

<span style="font-size: 90%;">but maybe we should get a bit input on whether people are using that debug hack..</span>

**fgs** <span style="color: grey; font-size: 90%;">18:55:05 UTC</span>

<span style="font-size: 90%;">wfm</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:31 UTC</span>

<span style="font-size: 90%;">I’ll note it in the comments, maybe I’ll ask on the mailinglist if anyone is using it?</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:42 UTC</span>

<span style="font-size: 90%;">then we can come back to it next month, that seems enough time for responses</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:43 UTC</span>

<span style="font-size: 90%;">That's a good plan!</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:49 UTC</span>

<span style="font-size: 90%;">alright!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:57:48 UTC</span>

<span style="font-size: 90%;">Ok, next is <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1320>?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:58:34 UTC</span>

<span style="font-size: 90%;">The numbers in the agenda ticket are off</span>

↳ **fgs** <span style="color: grey; font-size: 90%;">19:00:37 UTC</span>

<span style="font-size: 90%;">Updated</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:58:35 UTC</span>

<span style="font-size: 90%;">haven’t tested it too much :confused: I need a little more time, I would love to push it in production in detection only and see what happen</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:59:03 UTC</span>

<span style="font-size: 90%;">#bestpractice :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:38 UTC</span>

<span style="font-size: 90%;">I like this work :+1:</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:05 UTC</span>

<span style="font-size: 90%;">alright, a little more time is okay :slightly_smiling_face: quality over quantity!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:01:14 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:01:28 UTC</span>

<span style="font-size: 90%;">Ok, then yours, <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1330></span>

**walter** <span style="color: grey; font-size: 90%;">19:01:45 UTC</span>

<span style="font-size: 90%;">I have this in production and it WFM</span>

**fgs** <span style="color: grey; font-size: 90%;">19:01:48 UTC</span>

<span style="font-size: 90%;">That looks ready to merge</span>

**fgs** <span style="color: grey; font-size: 90%;">19:02:35 UTC</span>

<span style="font-size: 90%;">Same for <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1332> if I can say so myself</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:38 UTC</span>

<span style="font-size: 90%;">( trying to email the maillist but having trouble changing my From address :sweat_smile: )</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:52 UTC</span>

<span style="font-size: 90%;">oh yeah that XML soap encoding :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:59 UTC</span>

<span style="font-size: 90%;">I remember we talked about this right</span>

**fgs** <span style="color: grey; font-size: 90%;">19:04:23 UTC</span>

<span style="font-size: 90%;">We did :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:46 UTC</span>

<span style="font-size: 90%;">looking good on a first look</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:20 UTC</span>

<span style="font-size: 90%;">++ for merge!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:07:30 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:02 UTC</span>

<span style="font-size: 90%;">done :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:08:15 UTC</span>

<span style="font-size: 90%;">great!</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:48 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ we skipped discussing <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1113> because Csanders was finding a cab or something :smile:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:09:22 UTC</span>

<span style="font-size: 90%;">btw, I take there are no updates for _@theMiddle_ access, right? :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:28 UTC</span>

<span style="font-size: 90%;">_@fgs_ sadly no :disappointed:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:10:16 UTC</span>

<span style="font-size: 90%;">Ok, yes, we are still working on the containers.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:20 UTC</span>

<span style="font-size: 90%;">alright!</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:22 UTC</span>

<span style="font-size: 90%;">alright :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:23 UTC</span>

<span style="font-size: 90%;">sorry about that</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:23 UTC</span>

<span style="font-size: 90%;">haha</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:10:24 UTC</span>

<span style="font-size: 90%;">But I hope we will finish our work soon :wink:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:10:35 UTC</span>

<span style="font-size: 90%;">Ahhh, he's here!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:38 UTC</span>

<span style="font-size: 90%;">i think we are making good progress :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:53 UTC</span>

<span style="font-size: 90%;">I’m seeing lots of commits here and there :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:55 UTC</span>

<span style="font-size: 90%;">i'm gonna merge them upstream to our dockerhub today</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:00 UTC</span>

<span style="font-size: 90%;">cool!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:11:03 UTC</span>

<span style="font-size: 90%;">Yeahhh!!!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:11 UTC</span>

<span style="font-size: 90%;">and then make the modifications to our crs image (which is really just one line</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:18 UTC</span>

<span style="font-size: 90%;">and then poof we're cookin</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:28 UTC</span>

<span style="font-size: 90%;">then i have to add a few features back with _@franbuehler_’s help</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:35 UTC</span>

<span style="font-size: 90%;">but she's been very helpful in testing</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:38 UTC</span>

<span style="font-size: 90%;">and suggesting</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:11:41 UTC</span>

<span style="font-size: 90%;">That would be cool.
Then, I or you can add my changes from franbuehler/modsecurity-crs-rp</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:49 UTC</span>

<span style="font-size: 90%;">yup :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:00 UTC</span>

<span style="font-size: 90%;">and i also want to have a wafelz build</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:06 UTC</span>

<span style="font-size: 90%;">but all the ubuntu builds can probably die</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:17 UTC</span>

<span style="font-size: 90%;">since apache/nginx are built ontop of it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:41 UTC</span>

<span style="font-size: 90%;">thoughts _@franbuehler_</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:47 UTC</span>

<span style="font-size: 90%;">Wafelz -> would be cool</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:13 UTC</span>

<span style="font-size: 90%;">they have a docker image so it'd be really simple</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:14:19 UTC</span>

<span style="font-size: 90%;">ah okk</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">then we just modify our tests to run</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:29 UTC</span>

<span style="font-size: 90%;">then... profit!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:15:17 UTC</span>

<span style="font-size: 90%;">I dont't know them. I must have a look at them.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:10 UTC</span>

<span style="font-size: 90%;">Why do the ubuntu builds die, _@csanders_?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:24 UTC</span>

<span style="font-size: 90%;">lets talk offline :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:32 UTC</span>

<span style="font-size: 90%;">sure</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:34 UTC</span>

<span style="font-size: 90%;">i think its a lot to support but i can be swayed</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:58 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:10 UTC</span>

<span style="font-size: 90%;">alpine linux maybe? :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:17:11 UTC</span>

<span style="font-size: 90%;">In the meantime I have come to the conviction that it is too much work :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">people did request a smaller build, so alpine might be a good choice</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:43 UTC</span>

<span style="font-size: 90%;">well it’s probably a lot of work to convert it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:49 UTC</span>

<span style="font-size: 90%;">although we could MAYBE do it on scratch as a multistage if we're feeling ballsy</span>

**csanders** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">i'll take a look tonight</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:21 UTC</span>

<span style="font-size: 90%;">ok</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:37 UTC</span>

<span style="font-size: 90%;">in any case I wish you good luck :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:20:56 UTC</span>

<span style="font-size: 90%;">Another question, Federico, has your baby been born?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:21:09 UTC</span>

<span style="font-size: 90%;">Christian asked me :wink:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:21:22 UTC</span>

<span style="font-size: 90%;">No, today is her due date but no news</span>

**fgs** <span style="color: grey; font-size: 90%;">19:21:23 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**fgs** <span style="color: grey; font-size: 90%;">19:21:41 UTC</span>

<span style="font-size: 90%;">Playing the waiting game now</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:21:59 UTC</span>

<span style="font-size: 90%;">Yes, I know that game :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:01 UTC</span>

<span style="font-size: 90%;">hahaha</span>

**fgs** <span style="color: grey; font-size: 90%;">19:22:15 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:22:27 UTC</span>

<span style="font-size: 90%;">omgosh</span>

**csanders** <span style="color: grey; font-size: 90%;">19:22:30 UTC</span>

<span style="font-size: 90%;">congrats dude</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:22:48 UTC</span>

<span style="font-size: 90%;">Good luck for the birth :heart:</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:00 UTC</span>

<span style="font-size: 90%;">same :smile:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:23:03 UTC</span>

<span style="font-size: 90%;">Thanks. I will keep you posted :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:10 UTC</span>

<span style="font-size: 90%;">yes, please :heart:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:23:20 UTC</span>

<span style="font-size: 90%;">congrats!! :baby::skin-tone-2::baby_bottle:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:23:53 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**fgs** <span style="color: grey; font-size: 90%;">19:24:09 UTC</span>

<span style="font-size: 90%;">Need to go now, it’s dinner time and I’m cooking</span>

**fgs** <span style="color: grey; font-size: 90%;">19:24:11 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:24:23 UTC</span>

<span style="font-size: 90%;">Bye :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:24:52 UTC</span>

<span style="font-size: 90%;">Next point is CRS summit?</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:05 UTC</span>

<span style="font-size: 90%;">yeah let’s speed up again :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:07 UTC</span>

<span style="font-size: 90%;">CRS summit!!</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:10 UTC</span>

<span style="font-size: 90%;">CRS Community Summit: Nobody seems to be eager to go to Tel Aviv and they say we might be charged 2K for a room for half a day.
Proposal: Community Summit in Amsterdam at AppSecEU in September</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:16 UTC</span>

<span style="font-size: 90%;">well I agree with this</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:06 UTC</span>

<span style="font-size: 90%;">personally, I’d liked to visit Tel Aviv, but Amsterdam would be much easier :sweat_smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:26:31 UTC</span>

<span style="font-size: 90%;">Amsterdam is easier for me too.
Did anyone plan to go to Tel Aviv?</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:09 UTC</span>

<span style="font-size: 90%;">crickets…</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:18 UTC</span>

<span style="font-size: 90%;">well, then I guess this point is non controversial :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:29 UTC</span>

<span style="font-size: 90%;">yay Amsterdam?!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:27:39 UTC</span>

<span style="font-size: 90%;">Amsterdam sounds good!</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:00 UTC</span>

<span style="font-size: 90%;">the yays have it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:04 UTC</span>

<span style="font-size: 90%;">i'll prob be in tel aviv</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:13 UTC</span>

<span style="font-size: 90%;">but we'll see about that -- only if my talk gets accepted</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:44 UTC</span>

<span style="font-size: 90%;">I would go only for CRS stuff, if we’re not summiting then probably I’ll just take a vacation finally :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:53 UTC</span>

<span style="font-size: 90%;">haha</span>

**csanders** <span style="color: grey; font-size: 90%;">19:29:21 UTC</span>

<span style="font-size: 90%;">i'll try and sneak out to amsterdam</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:24 UTC</span>

<span style="font-size: 90%;">Flight to Amsterdam is much cheaper for me than Tel Aviv.
So going only for meeting you CRS-people is an option</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:43 UTC</span>

<span style="font-size: 90%;">In Amsterdam...</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:24 UTC</span>

<span style="font-size: 90%;">woot!</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:53 UTC</span>

<span style="font-size: 90%;">theeeeeennn the next point…</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:54 UTC</span>

<span style="font-size: 90%;">Should we open a paypal account to receive our share of the swag if we sell anything? <https://github.com/fzipi/owasp-swag/tree/add-coreruleset-logos/projects/coreruleset></span>

**walter** <span style="color: grey; font-size: 90%;">19:32:19 UTC</span>

<span style="font-size: 90%;">I have no opinions on this myself, Christian mentioned something about OWASP but I’m not sure exactly what was meant, I would think having it OWASP managed would make it harder to use it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:21 UTC</span>

<span style="font-size: 90%;">i noted earlier i have no objection to this, its just annoying to do it in the US for tax reasons :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:52 UTC</span>

<span style="font-size: 90%;">yeah we’re not a 501(c)(3) or something like that :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:10 UTC</span>

<span style="font-size: 90%;">if we just sell stickers… it probably won’t matter</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:14 UTC</span>

<span style="font-size: 90%;">yup</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:23 UTC</span>

<span style="font-size: 90%;">if we want to receive corporate donations, we could still point those people to our box at the OWASP</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">exactly</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">so we could have a little account for little things, sure</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:53 UTC</span>

<span style="font-size: 90%;">if we need something like buying a little domain name or a VPS or something</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">its much easier than going through red tape at OWASP</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">yup, makes sense</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:39 UTC</span>

<span style="font-size: 90%;">minimal effort</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:42 UTC</span>

<span style="font-size: 90%;">i say lets do it</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:50 UTC</span>

<span style="font-size: 90%;">I guess if the paypal account has a Swiss owner, we won’t get in trouble :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:35:02 UTC</span>

<span style="font-size: 90%;">Haha</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:35:26 UTC</span>

<span style="font-size: 90%;">Does OWASP allow us to do that?</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:35 UTC</span>

<span style="font-size: 90%;">that’s a good question</span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:41 UTC</span>

<span style="font-size: 90%;">probably not offically</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:36:00 UTC</span>

<span style="font-size: 90%;">Ok. Should we ask or just do it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:40 UTC</span>

<span style="font-size: 90%;">what was the saying again… it’s easier to go undetected than get permission :smile:</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:37:15 UTC</span>

<span style="font-size: 90%;">we call it “the italian way” :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:36:49 UTC</span>

<span style="font-size: 90%;">yay!</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:08 UTC</span>

<span style="font-size: 90%;">but yeah I’m an OWASP noob, I’ve just became a member so I don’t know how they work</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:37:13 UTC</span>

<span style="font-size: 90%;">it's easier to ask for forgiveness than it is to ask for permission :wink:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:15 UTC</span>

<span style="font-size: 90%;">we call it “the italian way” :smile:</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:37:15 UTC</span>

<span style="font-size: 90%;">we call it “the italian way” :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:20 UTC</span>

<span style="font-size: 90%;">okay so nobody here object so I guess we’ll take this issue to the back</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:39:08 UTC</span>

<span style="font-size: 90%;">Ok. I don't have an opinion here, sorry :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:54 UTC</span>

<span style="font-size: 90%;">then we go to the next issue!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">CRS containers...</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:20 UTC</span>

<span style="font-size: 90%;">well we sort of handled that between the lines :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:40:24 UTC</span>

<span style="font-size: 90%;">yes.</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:30 UTC</span>

<span style="font-size: 90%;">very interested to see the results :heart_eyes:</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:39 UTC</span>

<span style="font-size: 90%;">thennnnn the last one:</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:39 UTC</span>

<span style="font-size: 90%;">theMiddleBlue commented an hour ago
to remind myself: talk about RomHack 2019 :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:43 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ pls talk!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:40:44 UTC</span>

<span style="font-size: 90%;">I hope we will finish the work soon :wink:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:44 UTC</span>

<span style="font-size: 90%;">oh yes</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:50 UTC</span>

<span style="font-size: 90%;">last year I went to RomHack (cybersecurity convention in Rome <https://www.romhack.io/index_en.html>) for a talk</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:01 UTC</span>

<span style="font-size: 90%;">This year they ask me if I know someone that I would love to invite for a talk, and I’ve proposed someone of you :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:06 UTC</span>

<span style="font-size: 90%;">is this university roma 1, 2, or 3?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:11 UTC</span>

<span style="font-size: 90%;">If anyone wants to come to Rome to talk about CRS, they can pay for the travel and the hotel. This was the 2018 event <https://2018.romhack.io/></span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:16 UTC</span>

<span style="font-size: 90%;">link campus university</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">together with you? :smile:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:01 UTC</span>

<span style="font-size: 90%;">no I can’t :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:06 UTC</span>

<span style="font-size: 90%;">AppSec Amsterdam, Sept 23-27, 2019, Netherlands</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:15 UTC</span>

<span style="font-size: 90%;">yes that’s the problem</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:17 UTC</span>

<span style="font-size: 90%;">it will be two days after Appsec A’dam so for me it might be kind of hard</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:26 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:39 UTC</span>

<span style="font-size: 90%;">but maybe some of us will just go to the CRS summit in amsterdam, and not the whole conference</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:43:12 UTC</span>

<span style="font-size: 90%;">It's not possible for me. I can't travel a lot with my family?
We should aks Christian?</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:12 UTC</span>

<span style="font-size: 90%;">I’m very interested in spreading the gospel of CRS but with a low % of actually going to make it to this :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:34 UTC</span>

<span style="font-size: 90%;">sure, he can catch up later with this discussion :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:44 UTC</span>

<span style="font-size: 90%;">but a nice opportunity _@theMiddle_ :+1:</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:58 UTC</span>

<span style="font-size: 90%;">long time since I’ve been to Rome…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:02 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2: no problem! if anyone interested just poke me</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:26 UTC</span>

<span style="font-size: 90%;">alright! then that solves our agenda :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:27 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ can you Pm me your email</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:33 UTC</span>

<span style="font-size: 90%;">sure</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:44:43 UTC</span>

<span style="font-size: 90%;">I had a presentation at DevOps Fusion (Zurich Switzerland) last week:
<https://www.slideshare.net/FranBuehler/waf-in-devops-devopsfusion2019>
:tada:</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:57 UTC</span>

<span style="font-size: 90%;">nice, I’m going to check that out :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:11 UTC</span>

<span style="font-size: 90%;">WAF in the whole app dev cycle is something I’m struggling a bit with still</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:46 UTC</span>

<span style="font-size: 90%;">I’ll send out that email about the debug .conf file tomorrow, have to run now….</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:53 UTC</span>

<span style="font-size: 90%;">alright any other comments? questions? love? hate?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:36 UTC</span>

<span style="font-size: 90%;">Please let me know, if I can help you, _@walter_
At least I'll try :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:16 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ well you can give a man a fish.. but ultimately I just gotta get more experience with fishing :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:25 UTC</span>

<span style="font-size: 90%;">alright!!!</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">I’m closing this meeting!</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:35 UTC</span>

<span style="font-size: 90%;">thank you all for your great contributions and input :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:37 UTC</span>

<span style="font-size: 90%;">alright</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:39 UTC</span>

<span style="font-size: 90%;">thanks for your helpo</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:47:41 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:47:50 UTC</span>

<span style="font-size: 90%;">Bye everyone</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:47:52 UTC</span>

<span style="font-size: 90%;">thanks! bye!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:54 UTC</span>

<span style="font-size: 90%;">bye!</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:57 UTC</span>

<span style="font-size: 90%;">bye bye!!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:25 UTC</span>

<span style="font-size: 90%;">Sorry, missed the last part of the meeting</span>

