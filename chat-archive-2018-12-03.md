### Mon, Dec 3rd, 2018

**emphazer** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">hello everybody</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:30:26 UTC</span>

<span style="font-size: 90%;">Hi everybody</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:31 UTC</span>

<span style="font-size: 90%;">hello all!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">hi all! :sunglasses:</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:17 UTC</span>

<span style="font-size: 90%;">sadly our spiritual leader Christian is not here so we’ll have to behave and do it ourselves :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:27 UTC</span>

<span style="font-size: 90%;">do we have a _@csanders_ though??</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:48 UTC</span>

<span style="font-size: 90%;">haha</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:49 UTC</span>

<span style="font-size: 90%;">yeah</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:51 UTC</span>

<span style="font-size: 90%;">wow</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:05 UTC</span>

<span style="font-size: 90%;">i was hovering in #modsecurity waiting for the meeting --- this is why sleep is important folks</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:13 UTC</span>

<span style="font-size: 90%;">ahah</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:17 UTC</span>

<span style="font-size: 90%;">old habits die hard!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:32 UTC</span>

<span style="font-size: 90%;">fortuantly i’m not sure we have that advanced of an agenda</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:39 UTC</span>

<span style="font-size: 90%;">first some congratulations and thanks for cutting the 3.1 release are in order :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:51 UTC</span>

<span style="font-size: 90%;">i’m running it on a few nodes with no apparent problems</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:06 UTC</span>

<span style="font-size: 90%;">Great!</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:19 UTC</span>

<span style="font-size: 90%;">which makes it one of our most nice releases to upgrade to</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">19:33:48 UTC</span>

<span style="font-size: 90%;">with all the hard work going into this, I find this a really good result!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">Special thanks to every one who committed</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:51 UTC</span>

<span style="font-size: 90%;">On that note, I think it’s a good time to discuss our next release</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:54 UTC</span>

<span style="font-size: 90%;">3.2</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:59 UTC</span>

<span style="font-size: 90%;">there are some good merges going in already</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:13 UTC</span>

<span style="font-size: 90%;">I agree</span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:14 UTC</span>

<span style="font-size: 90%;">I think we are generally looking for the minimum window here to be 6 months and the maximum to be a year</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">19:35:47 UTC</span>

<span style="font-size: 90%;">sounds reasonable</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:07 UTC</span>

<span style="font-size: 90%;">so you should expect something from 3.2 before 2020, i’d bet probably quite a bit before hand if we have good features</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:25 UTC</span>

<span style="font-size: 90%;">I know ModSecruity 3.1 compatibility is a must</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:35 UTC</span>

<span style="font-size: 90%;">*3;.0</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:49 UTC</span>

<span style="font-size: 90%;">On my list, getting the docker engine working and more tests for rule syntax are high</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:27 UTC</span>

<span style="font-size: 90%;">unfortunately the latest 3.0.3 has a lot of new bugs</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:27 UTC</span>

<span style="font-size: 90%;">I wonder if we can get the regression tests also running under modsec, that’s not currently the case right?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:38 UTC</span>

<span style="font-size: 90%;">under modsec v3?</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:49 UTC</span>

<span style="font-size: 90%;">oops yes nginx+modsec v3 I meant</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:58 UTC</span>

<span style="font-size: 90%;">that is correct, i have a half baked PR to support that</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:05 UTC</span>

<span style="font-size: 90%;">but it is somewhat complex</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:16 UTC</span>

<span style="font-size: 90%;">i’d also like to support Apache as it matures</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:26 UTC</span>

<span style="font-size: 90%;">that would be nice too yeah</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:43 UTC</span>

<span style="font-size: 90%;">but I think most of us have Apache on their dev boxes, well at least Folini and I have :stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:49 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:54 UTC</span>

<span style="font-size: 90%;">so if that breaks, we sort of have a backstop</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:56 UTC</span>

<span style="font-size: 90%;">i meant v3/apache</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">ah yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:06 UTC</span>

<span style="font-size: 90%;">which is like not dev’d really at all</span>

**fgs** <span style="color: grey; font-size: 90%;">19:39:58 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:32 UTC</span>

<span style="font-size: 90%;">nginx+modsec3 seems an important target though</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:00 UTC</span>

<span style="font-size: 90%;">for my prod too :confused:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:04 UTC</span>

<span style="font-size: 90%;">yeah i think that’s my 3.1 target</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:09 UTC</span>

<span style="font-size: 90%;">(not apache)</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:11 UTC</span>

<span style="font-size: 90%;">it’s true that modsec 3.0.3 has introduced some new problems, but if we run our test suite on it, we’ll be better in the loop on those kinds of issues</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:32 UTC</span>

<span style="font-size: 90%;">maybe we could even run it on libmodsec master</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:52 UTC</span>

<span style="font-size: 90%;">in some way this is also TW’s problem but they are resource starved, well we are too, but we have our Travis magician</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:19 UTC</span>

<span style="font-size: 90%;">it is mostly a time to get it working thing</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:28 UTC</span>

<span style="font-size: 90%;">and since we maintain the docker images… it’s not so bad</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:28 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:39 UTC</span>

<span style="font-size: 90%;">yes I recently started using that, it looks good</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:50 UTC</span>

<span style="font-size: 90%;">thanks to _@franbuehler_ for her help maintaining those</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">alright :stuck_out_tongue: shall we turn to the agenda?</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:40 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1238></span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:05 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:23 UTC</span>

<span style="font-size: 90%;">some nice PRs, shall we start with the first?</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:27 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1205></span>

**fgs** <span style="color: grey; font-size: 90%;">19:45:59 UTC</span>

<span style="font-size: 90%;">That’d be straight forward</span>

**fgs** <span style="color: grey; font-size: 90%;">19:46:05 UTC</span>

<span style="font-size: 90%;">is a backport of my fix to 3.2</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:11 UTC</span>

<span style="font-size: 90%;">i see that `matched_var_name` is lowercase again in this PR, was that okay?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:46:13 UTC</span>

<span style="font-size: 90%;">With the case added</span>

**fgs** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">don’t remember, checking</span>

**fgs** <span style="color: grey; font-size: 90%;">19:47:40 UTC</span>

<span style="font-size: 90%;">Looks like it’s not</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:00 UTC</span>

<span style="font-size: 90%;">Hi all</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:04 UTC</span>

<span style="font-size: 90%;">hey</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:06 UTC</span>

<span style="font-size: 90%;">Probably an issue with the PR since my original PR was done before the case was changed</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:48:15 UTC</span>

<span style="font-size: 90%;">hi _@fzipitria_</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:23 UTC</span>

<span style="font-size: 90%;">yes we changed those variables back to uppercase in v3.1…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:24 UTC</span>

<span style="font-size: 90%;">Hi Franziska!</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:32 UTC</span>

<span style="font-size: 90%;">I can update it</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:37 UTC</span>

<span style="font-size: 90%;">I think this was a modsec 3.0.<=2 issue</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:44 UTC</span>

<span style="font-size: 90%;">well, maybe if we merge 3.1 into 3.2, it will get corrected</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:50 UTC</span>

<span style="font-size: 90%;">I wonder if we might be missing more small fixes in 3.1 that haven’t made it to 3.2</span>

**fgs** <span style="color: grey; font-size: 90%;">19:49:15 UTC</span>

<span style="font-size: 90%;">Maybe, we should be able to check</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:29 UTC</span>

<span style="font-size: 90%;">i’ll create an issue to comb over the 3.1 branch for those kinds of things in general</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:37 UTC</span>

<span style="font-size: 90%;">can you update this PR with the case only? _@fgs_</span>

**fgs** <span style="color: grey; font-size: 90%;">19:49:52 UTC</span>

<span style="font-size: 90%;">will do</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:17 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ do you want to put time on the calendar for the two of us to go over the suggested docker changes?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:51:20 UTC</span>

<span style="font-size: 90%;">git log says a difference of ~61~ 18 commits between 3.1/dev and 3.2/dev</span>

**fgs** <span style="color: grey; font-size: 90%;">19:52:56 UTC</span>

<span style="font-size: 90%;">ops, got that one reversed</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:53:15 UTC</span>

<span style="font-size: 90%;">_@csanders_ yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:24 UTC</span>

<span style="font-size: 90%;">how does two weeks from now work</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:28 UTC</span>

<span style="font-size: 90%;">i’m out in spain next week</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:55:05 UTC</span>

<span style="font-size: 90%;">_@csanders_ Sounds ok for me</span>

**csanders** <span style="color: grey; font-size: 90%;">19:55:21 UTC</span>

<span style="font-size: 90%;">alright i’ll PM you and we’ll figure out a specific time</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:23 UTC</span>

<span style="font-size: 90%;">alright then I’ll assign you both :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:35 UTC</span>

<span style="font-size: 90%;">the next one is <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1172></span>

**csanders** <span style="color: grey; font-size: 90%;">19:55:54 UTC</span>

<span style="font-size: 90%;">I think that is a really excelent one</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:56 UTC</span>

<span style="font-size: 90%;">I like this!</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:38 UTC</span>

<span style="font-size: 90%;">I would almost just merge it</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:03 UTC</span>

<span style="font-size: 90%;">the only weird thing is, it seems like it has no parent</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:06 UTC</span>

<span style="font-size: 90%;">`theMiddleBlue wants to merge 4 commits into SpiderLabs:v3.2/dev from unknown repository`</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:15 UTC</span>

<span style="font-size: 90%;">so I can’t checkout the code :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:21 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ did you delete your fork maybe?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:21 UTC</span>

<span style="font-size: 90%;">ouch</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:30 UTC</span>

<span style="font-size: 90%;">:disappointed: yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:33 UTC</span>

<span style="font-size: 90%;">haha</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:40 UTC</span>

<span style="font-size: 90%;">well no problem, the diff is still there</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:03 UTC</span>

<span style="font-size: 90%;">we have no tests for it, but it looks so good, I’m willing to take any fallout</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:05 UTC</span>

<span style="font-size: 90%;">I’m merging it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:14 UTC</span>

<span style="font-size: 90%;">sounds good</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:16 UTC</span>

<span style="font-size: 90%;">unless complaints? :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:31 UTC</span>

<span style="font-size: 90%;">if it breaks everything, I’ll take the blame</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:58:38 UTC</span>

<span style="font-size: 90%;">oky, I’m testing that rule in my prod w/o problems</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:42 UTC</span>

<span style="font-size: 90%;">it's ok for me</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:58:45 UTC</span>

<span style="font-size: 90%;">whats the schedule of v3.2?</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:08 UTC</span>

<span style="font-size: 90%;">_@emphazer_ we think of 6 months minimum, 12 max… but I think we all hope for 6 months more likely</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:32 UTC</span>

<span style="font-size: 90%;">whatever we do we should prevent a very long and painful RC phase where we have two branches… that made us do so much extra work (and we still have some; see caps changes!)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:59:34 UTC</span>

<span style="font-size: 90%;">aim for 6 months if there are enough features to start packaging and RCing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:42 UTC</span>

<span style="font-size: 90%;">ok for me also to merge</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:59:43 UTC</span>

<span style="font-size: 90%;">ok sounds good. tested it a bit and had many many giga bytes logs....</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:45 UTC</span>

<span style="font-size: 90%;">1172 is merged! :tada: thanks _@theMiddle_!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:00:58 UTC</span>

<span style="font-size: 90%;">:tada: :+1::skin-tone-2:</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:12 UTC</span>

<span style="font-size: 90%;">next one! <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1156></span>

**walter** <span style="color: grey; font-size: 90%;">20:01:43 UTC</span>

<span style="font-size: 90%;">looks lovely to me</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">and it even fixes the README</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:58 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:10 UTC</span>

<span style="font-size: 90%;">I guess that’s because it came from 3.1 times or so</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:24 UTC</span>

<span style="font-size: 90%;">I say merge!</span>

**fgs** <span style="color: grey; font-size: 90%;">20:02:34 UTC</span>

<span style="font-size: 90%;">it needs to be rebased</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:48 UTC</span>

<span style="font-size: 90%;">it has a conflict</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:57 UTC</span>

<span style="font-size: 90%;">oh shoot</span>

**fgs** <span style="color: grey; font-size: 90%;">20:02:58 UTC</span>

<span style="font-size: 90%;">yup</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:21 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ would you like to update the PR for that? :wink:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:36 UTC</span>

<span style="font-size: 90%;">Java stuff looks good for me</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:53 UTC</span>

<span style="font-size: 90%;">I grepped some stuff and also found some classes to add myself… will make a separate issue for myself to remind me</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:04:57 UTC</span>

<span style="font-size: 90%;">Hi _@walter_ what needs to be updated?</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:40 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ oh sorry :stuck_out_tongue: we want to merge this one <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1156> but it has conflicts</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:34 UTC</span>

<span style="font-size: 90%;">it’s not your fault that the PR spent so long before merging so my apologies</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:13 UTC</span>

<span style="font-size: 90%;">in any case if the PR is clean it would be an instant merge</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:58 UTC</span>

<span style="font-size: 90%;">shall we continue looking at the next PR in the meantime?</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:21 UTC</span>

<span style="font-size: 90%;">which is!!!!</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:29 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1124> Drop unneeded capture groups!!</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">:panda_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">yeah i think that needs to be reviewed, no?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:53 UTC</span>

<span style="font-size: 90%;">to make sure tht it doesn’t have any affects</span>

**fgs** <span style="color: grey; font-size: 90%;">20:09:12 UTC</span>

<span style="font-size: 90%;">yeah</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:21 UTC</span>

<span style="font-size: 90%;">it’s also based on v3.1/dev :see_no_evil:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:30 UTC</span>

<span style="font-size: 90%;">Yes, I should do a review...</span>

**fgs** <span style="color: grey; font-size: 90%;">20:09:55 UTC</span>

<span style="font-size: 90%;">I can rebase it against 3.2</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:31 UTC</span>

<span style="font-size: 90%;">I will review this PR in december, ok?</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:41 UTC</span>

<span style="font-size: 90%;">deal! _@fgs_ _@franbuehler_</span>

**fgs** <span style="color: grey; font-size: 90%;">20:10:53 UTC</span>

<span style="font-size: 90%;">cool</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:23 UTC</span>

<span style="font-size: 90%;">alriiight!</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:32 UTC</span>

<span style="font-size: 90%;">oh <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1113></span>

**walter** <span style="color: grey; font-size: 90%;">20:11:41 UTC</span>

<span style="font-size: 90%;">here is a PR for Nginx testing support :see_no_evil:</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:35 UTC</span>

<span style="font-size: 90%;">alright we just talked about that… it needs some love from _@csanders_ and _@franbuehler_</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:45 UTC</span>

<span style="font-size: 90%;">the plenary continues on to the next PR….</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:51 UTC</span>

<span style="font-size: 90%;">yup</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:52 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:57 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1045></span>

**walter** <span style="color: grey; font-size: 90%;">20:14:06 UTC</span>

<span style="font-size: 90%;">the file upload detection!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:14:28 UTC</span>

<span style="font-size: 90%;">that’s cool</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:04 UTC</span>

<span style="font-size: 90%;">my memory is not perfect but, I merged an earlier version of this, and it turned out to have some trouble in production…</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:12 UTC</span>

<span style="font-size: 90%;">I’m now a bit more hesitant about it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:15:37 UTC</span>

<span style="font-size: 90%;">if i remember well there was problems with file detection?</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:04 UTC</span>

<span style="font-size: 90%;">I tested in detail the .exe upload with some real .exe files, but sadly the exe signature did not have good coverage, and when looking at the MZ specification, what would remain of the signature would be so small that it would cause a lot of FP</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:18 UTC</span>

<span style="font-size: 90%;">I spent a lot of time reviewing this PR. The PR was shortened then. But I am not sure if it's ready for a review.</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:26 UTC</span>

<span style="font-size: 90%;">I think for CRS use case, detecting executable uploads would be very important</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:33 UTC</span>

<span style="font-size: 90%;">various other file types, I’m not so sure about</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:37 UTC</span>

<span style="font-size: 90%;">Or if it still needs some work and testing from _@SpartanTri_?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:16:41 UTC</span>

<span style="font-size: 90%;">_@walter_ <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1205> has been updated in case you want to merge it</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:49 UTC</span>

<span style="font-size: 90%;">I think we have to discuss the ambition level, it was a bit too big I think….</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:17:01 UTC</span>

<span style="font-size: 90%;">i would drop fiöe upload detection. </span>

**emphazer** <span style="color: grey; font-size: 90%;">20:17:06 UTC</span>

<span style="font-size: 90%;">file</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:07 UTC</span>

<span style="font-size: 90%;">for every file type we should have very detailed tests…</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:24 UTC</span>

<span style="font-size: 90%;">yeah I’m also thinking the current approach is too big</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:17:36 UTC</span>

<span style="font-size: 90%;">its definetly too big</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:37 UTC</span>

<span style="font-size: 90%;">maybe we should start just by detecting ELF for instance</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:00 UTC</span>

<span style="font-size: 90%;">(unix executables)</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:15 UTC</span>

<span style="font-size: 90%;">yeah I think it was a bit too big to fail</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:33 UTC</span>

<span style="font-size: 90%;">small steps... sounds good.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:41 UTC</span>

<span style="font-size: 90%;">And it's easier for rewiewing...</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:31 UTC</span>

<span style="font-size: 90%;">yeah I think we should not do PRs so big anymore</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:48 UTC</span>

<span style="font-size: 90%;">it’s scary to review, any single problem makes the whole PR be hold up, get stale, grow conflicts</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:20:30 UTC</span>

<span style="font-size: 90%;">In your installs, who actually runs payload analysis like this in production?</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:12 UTC</span>

<span style="font-size: 90%;">meer :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:15 UTC</span>

<span style="font-size: 90%;">meee*</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:36 UTC</span>

<span style="font-size: 90%;">but pretty adhoc</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:08 UTC</span>

<span style="font-size: 90%;">_@fgs_ thanks for updating [#1205](https://github.com/coreruleset/coreruleset/issues/#1205), looks good now!</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">It would be really good to have usage stats of rules like this. We would potentially disable these by default, because checking uploads will always break something unfortunately.</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">I’ll merge it</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:00 UTC</span>

<span style="font-size: 90%;">after travis is done</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:04 UTC</span>

<span style="font-size: 90%;">_@Christian Treutler_ understandable, maybe we should add a listing of new rules and a summary of their actions in order to make this easier and not create surprises when upgrading</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:11 UTC</span>

<span style="font-size: 90%;">in fact I always loved some kind of rule matrix at all…</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:24 UTC</span>

<span style="font-size: 90%;">we also talked a bit about this during the summer</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:27:27 UTC</span>

<span style="font-size: 90%;">_@walter_ I would love that too - Some external easy to fetch info about every rule.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:27:48 UTC</span>

<span style="font-size: 90%;">hmm</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:48 UTC</span>

<span style="font-size: 90%;">I know F5 sends out super long update notices about every little signature change, that’s too much, ruleId granularity would be good though</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:18 UTC</span>

<span style="font-size: 90%;">I’m wondering if we can use wordpress for this</span>

**csanders** <span style="color: grey; font-size: 90%;">20:29:29 UTC</span>

<span style="font-size: 90%;">there needs to be a REALLY easy solution</span>

**csanders** <span style="color: grey; font-size: 90%;">20:29:34 UTC</span>

<span style="font-size: 90%;">otherwise we’ll not keep it updated</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:39 UTC</span>

<span style="font-size: 90%;">yes it needs to be auto imported :smile:</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:29:59 UTC</span>

<span style="font-size: 90%;">Sure. It must be fed by github changes automatically</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:30:09 UTC</span>

<span style="font-size: 90%;">otherwise it will get stale very quickly</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:10 UTC</span>

<span style="font-size: 90%;">there’s a lot of semi-polished tooling for parsing modsec rules, I wonder if we can also extract the comments from this, if so this would be the best</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:20 UTC</span>

<span style="font-size: 90%;">the rule comment block above it</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:26 UTC</span>

<span style="font-size: 90%;">shall I look into this?</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:31:05 UTC</span>

<span style="font-size: 90%;">_@walter_ lets have a chat about it. I had a couple ideas, but no time yet. I should have more time in the next two weeks. Just ping me and I send an invite!</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:22 UTC</span>

<span style="font-size: 90%;">_@Christian Treutler_ excellent. I will also think about it</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:32:18 UTC</span>

<span style="font-size: 90%;">Everybody who bundles CRS today or in the future will love you for bringing that to fruition :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:21 UTC</span>

<span style="font-size: 90%;">that is true :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:56 UTC</span>

<span style="font-size: 90%;">_@walter_ I can probably add something to the secrules parser</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:35:58 UTC</span>

<span style="font-size: 90%;">It would be nice if in the future the SecRule syntax will be in json or yml… including rule description… it would be easy to parse and maintain</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:24 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ there is a project about that in <#CBR9SAE3H|coreruleset-lang> but it’s a long term project :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:30 UTC</span>

<span style="font-size: 90%;">it’s definitely the way we want to go!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:36:32 UTC</span>

<span style="font-size: 90%;">ye i see</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:36:38 UTC</span>

<span style="font-size: 90%;">If anybody has seen other projects using a good solution for documenting changes, please post. I would think there must be something out there.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:36:45 UTC</span>

<span style="font-size: 90%;">it’s a great project</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:49 UTC</span>

<span style="font-size: 90%;">I created an issue for this rule metadata project :+1: I won’t put it under milestone 3.2 since it can run parallel to it and is not a showstopper for the release</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:11 UTC</span>

<span style="font-size: 90%;">no I will because otherwise I’ll forget about it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:38:23 UTC</span>

<span style="font-size: 90%;">ahaha</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:48 UTC</span>

<span style="font-size: 90%;">okaaayy…</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:07 UTC</span>

<span style="font-size: 90%;">alright the final one on the PR list was the file upload detection</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:46 UTC</span>

<span style="font-size: 90%;">if I read the room right, we are not going to go further with the PR now, but we would like a smaller PR for some cases like executable file uploads?</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:40 UTC</span>

<span style="font-size: 90%;">and then insure ourselves heavily with testcases</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:19 UTC</span>

<span style="font-size: 90%;">I have to run in a few minutes from now… but are you all already gone? :stuck_out_tongue:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:42:36 UTC</span>

<span style="font-size: 90%;">nods</span>

**fgs** <span style="color: grey; font-size: 90%;">20:42:47 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:42:49 UTC</span>

<span style="font-size: 90%;">haha</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:42:59 UTC</span>

<span style="font-size: 90%;">Not yet.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:43:04 UTC</span>

<span style="font-size: 90%;">I'm still here</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:43:09 UTC</span>

<span style="font-size: 90%;">:wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:43:11 UTC</span>

<span style="font-size: 90%;">yeah that sounds we each some things to do now :-</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:44 UTC</span>

<span style="font-size: 90%;">alright I’ll comment on the PR with the bad news :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">20:44:00 UTC</span>

<span style="font-size: 90%;">which brings us to: CRS swag, proposal by _@fzipitria_!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:44:08 UTC</span>

<span style="font-size: 90%;">wooo</span>

**csanders** <span style="color: grey; font-size: 90%;">20:44:10 UTC</span>

<span style="font-size: 90%;">ohh!!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:44:16 UTC</span>

<span style="font-size: 90%;">WE WANT SWAG</span>

**walter** <span style="color: grey; font-size: 90%;">20:44:23 UTC</span>

<span style="font-size: 90%;">yes we demand it</span>

**walter** <span style="color: grey; font-size: 90%;">20:44:26 UTC</span>

<span style="font-size: 90%;">or we fork the project!!!</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:45:09 UTC</span>

<span style="font-size: 90%;">That reminds me our OWASP membership renews very soon, so the project should get half of that right? So hopefully more SWAG!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:45:36 UTC</span>

<span style="font-size: 90%;">we have a bit of a budget already</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:45:49 UTC</span>

<span style="font-size: 90%;">I want to drink my beer on my CRS beer mug :grinning:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:45:49 UTC</span>

<span style="font-size: 90%;">but yeah I know that christian had an idea previously</span>

**csanders** <span style="color: grey; font-size: 90%;">20:45:52 UTC</span>

<span style="font-size: 90%;">but i guess we never made it</span>

**csanders** <span style="color: grey; font-size: 90%;">20:45:59 UTC</span>

<span style="font-size: 90%;">I’d like a poloshirt honestly</span>

**csanders** <span style="color: grey; font-size: 90%;">20:46:03 UTC</span>

<span style="font-size: 90%;">but beer mug isn’t bad</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:46:06 UTC</span>

<span style="font-size: 90%;">ahah</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:10 UTC</span>

<span style="font-size: 90%;">I accept anything</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:12 UTC</span>

<span style="font-size: 90%;">I would like to have stickers</span>

**csanders** <span style="color: grey; font-size: 90%;">20:46:32 UTC</span>

<span style="font-size: 90%;">alright so minimum stickers</span>

**csanders** <span style="color: grey; font-size: 90%;">20:46:45 UTC</span>

<span style="font-size: 90%;">i’ll add it to my list to design some and post them here before next meeting</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:47:01 UTC</span>

<span style="font-size: 90%;">awesome</span>

**walter** <span style="color: grey; font-size: 90%;">20:47:42 UTC</span>

<span style="font-size: 90%;">cool!</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:28 UTC</span>

<span style="font-size: 90%;">then there’s: Bringing the enhancements of _@franbuehler_’s docker container to the official CRS docker container (-> <https://github.com/franbuehler/modsecurity-crs-rp/tree/v3.1>)</span>

**csanders** <span style="color: grey; font-size: 90%;">20:48:41 UTC</span>

<span style="font-size: 90%;">yup, we have that tentativlly scheduled</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:43 UTC</span>

<span style="font-size: 90%;">good!</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:03 UTC</span>

<span style="font-size: 90%;">then we are done with the official agenda :stuck_out_tongue: any other comments, suggestions, remarks, complaints?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:49:17 UTC</span>

<span style="font-size: 90%;">+1 to _@walter_ for leading the meeting today</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:21 UTC</span>

<span style="font-size: 90%;">Sorry. Boarding plane</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:49:28 UTC</span>

<span style="font-size: 90%;">Just again a big thanks for Releasing 3.1!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:41 UTC</span>

<span style="font-size: 90%;">I'll comment on swag when arriving in San Diego</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:47 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ cool!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:49:56 UTC</span>

<span style="font-size: 90%;">just your opinion about a little ruleset in order to log browser policy violation… anyone uses CSP in prod?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:50:06 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ have a good flight</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:15 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:50:26 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ what did you aahve in mind?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:50:34 UTC</span>

<span style="font-size: 90%;">isn’t that what the reporter is for?</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:50:46 UTC</span>

<span style="font-size: 90%;">yeah please explain</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:51:20 UTC</span>

<span style="font-size: 90%;">I’m using this in my prod in order to log all violations that came from CSP report: <https://gist.github.com/theMiddleBlue/f96f2661c76fea101787c5561e86b6cd></span>

**csanders** <span style="color: grey; font-size: 90%;">20:51:44 UTC</span>

<span style="font-size: 90%;">ahh i see</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:51:46 UTC</span>

<span style="font-size: 90%;">but, don’t know if it could be useful for CRS and how many users need this</span>

**csanders** <span style="color: grey; font-size: 90%;">20:51:54 UTC</span>

<span style="font-size: 90%;">not a bad idea, i use ELK for that</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:23 UTC</span>

<span style="font-size: 90%;">not sure how much people will use it but I think it’d make a great blog post at minimum</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:52:28 UTC</span>

<span style="font-size: 90%;">Idea is fine, but I don’t think it should be part of CRS.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:35 UTC</span>

<span style="font-size: 90%;">yeah i feel similarly, HOWEVER</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:44 UTC</span>

<span style="font-size: 90%;">I think we should be able to link to other projects like this</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:45 UTC</span>

<span style="font-size: 90%;">because</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:55 UTC</span>

<span style="font-size: 90%;">if you’re already running ModSec it is a free gain for logging and alerting</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:53:01 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:53:02 UTC</span>

<span style="font-size: 90%;">no need to setup anything else</span>

**csanders** <span style="color: grey; font-size: 90%;">20:53:17 UTC</span>

<span style="font-size: 90%;">what are your thoughts _@theMiddle_</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:26 UTC</span>

<span style="font-size: 90%;">I think this is a very cool rule, but I agree it might not be a perfect fit for CRS…</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:40 UTC</span>

<span style="font-size: 90%;">at the other hand</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:58 UTC</span>

<span style="font-size: 90%;">I could see where I would like this stuff to get into my ELK for free</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:55:00 UTC</span>

<span style="font-size: 90%;">I think that many users don’t want to include rules for logging something like CSP violations… many users don’t use it… maybe it’s not suitable for CRS</span>

**csanders** <span style="color: grey; font-size: 90%;">20:55:14 UTC</span>

<span style="font-size: 90%;">it’s def useful though</span>

**csanders** <span style="color: grey; font-size: 90%;">20:55:22 UTC</span>

<span style="font-size: 90%;">the more i think about it, the more i like it for how slick it is</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:23 UTC</span>

<span style="font-size: 90%;">a bit freaky would be that you’d have to point your report URL header to some (non existent?) endpoint on a CRS protected box</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:46 UTC</span>

<span style="font-size: 90%;">I did like the “optional_rules” in crs2 with this kind of stuff</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:56:00 UTC</span>

<span style="font-size: 90%;">yes, actually I point to the self /</span>

**csanders** <span style="color: grey; font-size: 90%;">20:56:01 UTC</span>

<span style="font-size: 90%;">yeah, the problem was they became unmaintained quickly</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:02 UTC</span>

<span style="font-size: 90%;">some of it I used and most I didn’t</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:45 UTC</span>

<span style="font-size: 90%;">I think it’s better suited as a blog post on <http://coreruleset.org|coreruleset.org></span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:56:54 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2:</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:08 UTC</span>

<span style="font-size: 90%;">if only we had an “ecosystem” :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:57:12 UTC</span>

<span style="font-size: 90%;">Blog post would be great!</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:21 UTC</span>

<span style="font-size: 90%;">I wouldn’t mind doing a `modsec install themiddle/csp-report`</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:35 UTC</span>

<span style="font-size: 90%;">but we’re not in that era yet</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:57:59 UTC</span>

<span style="font-size: 90%;">lol</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:07:24 UTC</span>

<span style="font-size: 90%;">...soooo... bye and good night to everyone</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:34 UTC</span>

<span style="font-size: 90%;">yes!</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:37 UTC</span>

<span style="font-size: 90%;">let’s close the meeting :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:44 UTC</span>

<span style="font-size: 90%;">thank you all for participating, contributing, submitting, etc!!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:08:14 UTC</span>

<span style="font-size: 90%;">bye guys! and thanks to _@walter_ !</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:08:26 UTC</span>

<span style="font-size: 90%;">Thank you _@walter_!</span>

**walter** <span style="color: grey; font-size: 90%;">21:08:47 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:48 UTC</span>

<span style="font-size: 90%;">Seems I am a bit late to the party. Just read up the chat log. Thanks for taking the time for the meeting. Sure looks I missed on a great meeting. And thank you for moderating _@walter_. Very good job.</span>

**fgs** <span style="color: grey; font-size: 90%;">22:17:45 UTC</span>

<span style="font-size: 90%;">I’ve updated <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1124> but I wonder if I should break it into 2 PRs</span>

**fgs** <span style="color: grey; font-size: 90%;">22:17:57 UTC</span>

<span style="font-size: 90%;">One with the straight forward changes, and one with the complicated ones</span>

