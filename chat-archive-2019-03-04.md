### Mon, Mar 4th, 2019

**emphazer** <span style="color: grey; font-size: 90%;">19:30:18 UTC</span>

<span style="font-size: 90%;">hello everybody </span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:23 UTC</span>

<span style="font-size: 90%;">hey hey</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:25 UTC</span>

<span style="font-size: 90%;">Don't know if it makes a point in the agenda</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:49 UTC</span>

<span style="font-size: 90%;">But more trying to know if there is interest in adding Joomla to our supported apps</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">Hello everyone!</span>

**fgs** <span style="color: grey; font-size: 90%;">19:31:02 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:31:17 UTC</span>

<span style="font-size: 90%;">hi all! it’s monday meeting :tada:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">Good to meet you all (and getting a break from by EVoting bug bounty...)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:52 UTC</span>

<span style="font-size: 90%;">Bufrasch sends her regards, she is in the Alps skiiing with her family...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:36 UTC</span>

<span style="font-size: 90%;">Felipe, if you want it discussed, please add it to the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:05 UTC</span>

<span style="font-size: 90%;">Anybody has any news from Walter?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:24 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:25 UTC</span>

<span style="font-size: 90%;">haven't heard from him</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:40 UTC</span>

<span style="font-size: 90%;">I saw it earlier here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:56 UTC</span>

<span style="font-size: 90%;">Maybe he'll show up. Shall we start, the agenda is quite full I dare say</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:11 UTC</span>

<span style="font-size: 90%;">yup :_</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:12 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:49 UTC</span>

<span style="font-size: 90%;">Good, so let's start with PR 1315</span>

**fgs** <span style="color: grey; font-size: 90%;">19:35:20 UTC</span>

<span style="font-size: 90%;">May I suggest that in the future we start with the oldest?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:25 UTC</span>

<span style="font-size: 90%;">It's not passing travis as of this speaking. And Federico added a working exploit PoC.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:35:30 UTC</span>

<span style="font-size: 90%;">It makes more sense to go that way IMO</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:50 UTC</span>

<span style="font-size: 90%;">_@fgs_: You are right. I wanted to reorder. Let's start with 1315 and in the meantime we reorder the other ones.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:35:50 UTC</span>

<span style="font-size: 90%;">(as to not drag things further)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:25 UTC</span>

<span style="font-size: 90%;">Travis didn’t pass because the id, but it’s not the only problem IMHO…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:38 UTC</span>

<span style="font-size: 90%;">I think that we need more information about the CRS configuration used here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:56 UTC</span>

<span style="font-size: 90%;">OK. _@fgs_: you looked into it too?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:37:07 UTC</span>

<span style="font-size: 90%;">Yeah, I agree with _@theMiddle_</span>

**fgs** <span style="color: grey; font-size: 90%;">19:37:18 UTC</span>

<span style="font-size: 90%;">Also _@airween_ posted something here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:23 UTC</span>

<span style="font-size: 90%;">Do you guys want to talk to the submitter?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:37:30 UTC</span>

<span style="font-size: 90%;">That makes me believe that it hits multiple rules</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:36 UTC</span>

<span style="font-size: 90%;">yes I’ve reply with some questions</span>

**fgs** <span style="color: grey; font-size: 90%;">19:37:52 UTC</span>

<span style="font-size: 90%;">_@d1v_ around?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">The submitter was here a moment ago</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:38:10 UTC</span>

<span style="font-size: 90%;">oh oky</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:16 UTC</span>

<span style="font-size: 90%;">Oh, I see. He's the submitter.</span>

**d1v** <span style="color: grey; font-size: 90%;">19:38:20 UTC</span>

<span style="font-size: 90%;">yes :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:31 UTC</span>

<span style="font-size: 90%;">Cool. Welcome and thanks for the submission.</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:31 UTC</span>

<span style="font-size: 90%;">I’m around but distracted by family matters, I won’t take an active role but mention me for specific questions</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:39 UTC</span>

<span style="font-size: 90%;">Hello Walter!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:47 UTC</span>

<span style="font-size: 90%;">We'll shout if we need you. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:52 UTC</span>

<span style="font-size: 90%;">ok :slightly_smiling_face:</span>

**d1v** <span style="color: grey; font-size: 90%;">19:39:08 UTC</span>

<span style="font-size: 90%;">_@dune73_ sorry I haven't been able to answer in the PR, but didn't tests with other rules</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:31 UTC</span>

<span style="font-size: 90%;">_@d1v_: Can you work with _@fgs_ and _@theMiddle_ to make this work, so we can merge afterwards?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">Or would you rather leave it in our hands to make the best out of it?</span>

**d1v** <span style="color: grey; font-size: 90%;">19:40:08 UTC</span>

<span style="font-size: 90%;">totally, juggling a call at work at the moment but afterwards, glad to break off and chat about it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:49 UTC</span>

<span style="font-size: 90%;">Great. Then let's leave it for the time being and move to the next one.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:56 UTC</span>

<span style="font-size: 90%;">That would 1183.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:06 UTC</span>

<span style="font-size: 90%;">Sorry. 1113.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:10 UTC</span>

<span style="font-size: 90%;">_@d1v_ if you can answer to my reply, I will help you to sort it out</span>

↳ **d1v** <span style="color: grey; font-size: 90%;">19:42:04 UTC</span>

<span style="font-size: 90%;">will circle around to it as asap, its been a fun Monday</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:39 UTC</span>

<span style="font-size: 90%;">_@csanders_, I take it that is yours.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:47 UTC</span>

<span style="font-size: 90%;">yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:50 UTC</span>

<span style="font-size: 90%;">let me update you</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:01 UTC</span>

<span style="font-size: 90%;">in the crscontainer channel</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:11 UTC</span>

<span style="font-size: 90%;">i pushed a new v3 version</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:14 UTC</span>

<span style="font-size: 90%;">and a new v2 version</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:23 UTC</span>

<span style="font-size: 90%;">both versions support TLS and reverse proxy via args</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:35 UTC</span>

<span style="font-size: 90%;">i'm gonna wait a couple days for a review</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:48 UTC</span>

<span style="font-size: 90%;">but once that is done i'll add them to dockerhub (with changes)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">then we can start building the testing against them</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:14 UTC</span>

<span style="font-size: 90%;">Makes sense. Will try to review them</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:26 UTC</span>

<span style="font-size: 90%;">the v3 image takes a good 15 minutes to build :confused:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:28 UTC</span>

<span style="font-size: 90%;">I see. Bufrasch told me you were working on that. Afterwards she and Dan can take it from there. Correct?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:30 UTC</span>

<span style="font-size: 90%;">but that's just how it works</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:37 UTC</span>

<span style="font-size: 90%;">yup :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:51 UTC</span>

<span style="font-size: 90%;">fortunatly when folks download it because they're split images it should be quick and tiny</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">Cool. Do you have a timeframe for when you are done?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:35 UTC</span>

<span style="font-size: 90%;">i'd say... we'll give it a week for review</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:40 UTC</span>

<span style="font-size: 90%;">then we can start pushing them</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:44 UTC</span>

<span style="font-size: 90%;">unless there are objections</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:55 UTC</span>

<span style="font-size: 90%;">Is it ready for review already?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:00 UTC</span>

<span style="font-size: 90%;">yup</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:01 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:17 UTC</span>

<span style="font-size: 90%;">posted a zip with them for anyone intersted they can be added to #crscontainer</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:18 UTC</span>

<span style="font-size: 90%;">Ah, that was 6:57pm?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:31 UTC</span>

<span style="font-size: 90%;">yeah i buttoned them up this morning (For me)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:43 UTC</span>

<span style="font-size: 90%;">I see. Very well.
Now back to 1113: Will this PR be replaced or are you updating it?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:18 UTC</span>

<span style="font-size: 90%;">yeah i'll be replacing just the container</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:25 UTC</span>

<span style="font-size: 90%;">so it should be fairly quick</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:33 UTC</span>

<span style="font-size: 90%;">In 1113?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:36 UTC</span>

<span style="font-size: 90%;">yup</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:41 UTC</span>

<span style="font-size: 90%;">i'll probably rebase</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:51 UTC</span>

<span style="font-size: 90%;">OK. Thanks.
See the need for rebase too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:25 UTC</span>

<span style="font-size: 90%;">Good. That is settled.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:29 UTC</span>

<span style="font-size: 90%;">Next tone.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:49 UTC</span>

<span style="font-size: 90%;">1284. Honestly, I do not quite understand what the matter is here.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:27 UTC</span>

<span style="font-size: 90%;">To me this looks like it’s rather stale</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:44 UTC</span>

<span style="font-size: 90%;">And there is nothing actionable</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:57 UTC</span>

<span style="font-size: 90%;">So we just axe it?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:50:08 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fgs** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">If there is something to do it’s certainly outside this PR</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:22 UTC</span>

<span style="font-size: 90%;">The PR kills a rule it should not kill. Then it reorders some IDs, some welcome, some not so welcome.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:51:36 UTC</span>

<span style="font-size: 90%;">That file is no longer in 3.2</span>

**fgs** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">It was removed a while back</span>

**fgs** <span style="color: grey; font-size: 90%;">19:51:53 UTC</span>

<span style="font-size: 90%;">The title refers to updating contributions</span>

**fgs** <span style="color: grey; font-size: 90%;">19:52:02 UTC</span>

<span style="font-size: 90%;">But there is nothing in that PR that changes the contributions</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:06 UTC</span>

<span style="font-size: 90%;">I already promised to take care of it months ago. I'll push through this time.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:52:06 UTC</span>

<span style="font-size: 90%;">We should close and move on really</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:09 UTC</span>

<span style="font-size: 90%;">We're done.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:21 UTC</span>

<span style="font-size: 90%;">1286:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:53:08 UTC</span>

<span style="font-size: 90%;">I don’t follow _@dune73_. Take care of what?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:58 UTC</span>

<span style="font-size: 90%;">Of the 1284 PR. I'm actually assigned and I can take care of the reordering done in the PR. In a better way than the PR does.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:54:20 UTC</span>

<span style="font-size: 90%;">That file _was_ removed.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:54:29 UTC</span>

<span style="font-size: 90%;">There is nothing to do in there but OK.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:54 UTC</span>

<span style="font-size: 90%;">I slowly start to understand what you mean _@fgs_...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:14 UTC</span>

<span style="font-size: 90%;">:exploding_head:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:55:20 UTC</span>

<span style="font-size: 90%;">This is someone updating their branch</span>

**fgs** <span style="color: grey; font-size: 90%;">19:55:23 UTC</span>

<span style="font-size: 90%;">So the PR is no longer valid</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:28 UTC</span>

<span style="font-size: 90%;">Got it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:32 UTC</span>

<span style="font-size: 90%;">At last.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:40 UTC</span>

<span style="font-size: 90%;">_@emphazer_: Want to update on 1286?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:56:26 UTC</span>

<span style="font-size: 90%;">well, was really sick at February.  wasn't able to spend any time at CRS project at all. </span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:46 UTC</span>

<span style="font-size: 90%;">You mentioned you were sick for 10 days in a row. Back to health?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:57:25 UTC</span>

<span style="font-size: 90%;">@fgsch if you want to update it. feel free to do it.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:57:33 UTC</span>

<span style="font-size: 90%;">sure I am</span>

**fgs** <span style="color: grey; font-size: 90%;">19:58:05 UTC</span>

<span style="font-size: 90%;">_@emphazer_ your call really, don’t mind either way. I just would like to see it merged</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:48 UTC</span>

<span style="font-size: 90%;">I'd like it merged too. Can you guys take it from here and we merge by the end of the week?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:58:50 UTC</span>

<span style="font-size: 90%;">the problem is If i get sick for 10 days the work won't get done. so I have to do everything from the past</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:58:55 UTC</span>

<span style="font-size: 90%;">sure</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:59:00 UTC</span>

<span style="font-size: 90%;">I think so</span>

**fgs** <span style="color: grey; font-size: 90%;">19:59:03 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:34 UTC</span>

<span style="font-size: 90%;">Thank you. And I know _@emphazer_: With our jobs, being sick just means that the work piles up on the desk...</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:59:50 UTC</span>

<span style="font-size: 90%;">definitely </span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:49 UTC</span>

<span style="font-size: 90%;">Let's look into 1301!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:12 UTC</span>

<span style="font-size: 90%;">This is actually ready to be merged, is not it?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:38 UTC</span>

<span style="font-size: 90%;">10?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:43 UTC</span>

<span style="font-size: 90%;">oh</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:48 UTC</span>

<span style="font-size: 90%;">yeah i think it is</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:53 UTC</span>

<span style="font-size: 90%;">i know there was a request to change the order</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">if that is it</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:58 UTC</span>

<span style="font-size: 90%;">i can do that and merge it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:04 UTC</span>

<span style="font-size: 90%;">Great. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:35 UTC</span>

<span style="font-size: 90%;">Which brings us to 1306.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:26 UTC</span>

<span style="font-size: 90%;">That's a no-brainer. Thanks _@fgs_. Could you explain, what you did with the test, there?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:03:43 UTC</span>

<span style="font-size: 90%;">In which one, sorry?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:03:52 UTC</span>

<span style="font-size: 90%;">941110-2?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:11 UTC</span>

<span style="font-size: 90%;">1306. The test in util/regression-tests/tests/REQUEST-941-APPLICATION-ATTACK-XSS/941110.yaml</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:23 UTC</span>

<span style="font-size: 90%;">Yes, that one.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:39 UTC</span>

<span style="font-size: 90%;">The test was wrong</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:47 UTC</span>

<span style="font-size: 90%;">You cannot have spaces in the url</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:51 UTC</span>

<span style="font-size: 90%;">But did it pass, when it was wrong?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:05:07 UTC</span>

<span style="font-size: 90%;">It passed because it was no_log_contains</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:10 UTC</span>

<span style="font-size: 90%;">Ah, it would not hit because of the spaces. You fixed that and now the test runs?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:05:17 UTC</span>

<span style="font-size: 90%;">Correct</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:28 UTC</span>

<span style="font-size: 90%;">Got it. Let's merge this.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:05:35 UTC</span>

<span style="font-size: 90%;">There are plenty of those, just fixed a few as I went through</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:36 UTC</span>

<span style="font-size: 90%;">Any opposition?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:44 UTC</span>

<span style="font-size: 90%;">+1</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:06:13 UTC</span>

<span style="font-size: 90%;">should `REQUEST_FILENAME` used in all xxs rules? (idk if already is)</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:21 UTC</span>

<span style="font-size: 90%;">Ideally yes</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:28 UTC</span>

<span style="font-size: 90%;">But there are problems with other checks</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:38 UTC</span>

<span style="font-size: 90%;">Waiting for libinjection PR to be merged really</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:56 UTC</span>

<span style="font-size: 90%;"><https://github.com/client9/libinjection/pull/143></span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:01 UTC</span>

<span style="font-size: 90%;">And then another year or two for the adoption in the ModSec packages in distros.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:29 UTC</span>

<span style="font-size: 90%;">I think we need to look at it in a case by case base.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:21 UTC</span>

<span style="font-size: 90%;">This was a quick win</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:26 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:38 UTC</span>

<span style="font-size: 90%;">OK, I'll merge and we move on.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">For the others we’ll need more testing, so yeah, case by case basis unfortunately :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:29 UTC</span>

<span style="font-size: 90%;">And we're on 1310 already!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:19 UTC</span>

<span style="font-size: 90%;">Here, you want to make sure that C-L and T-E are mutually exclusive.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:10:50 UTC</span>

<span style="font-size: 90%;">Yes, correct</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:09 UTC</span>

<span style="font-size: 90%;">Complements the other rules I mentioned.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:17 UTC</span>

<span style="font-size: 90%;">But the tests and implicit behavior of Apache make it a bit sour.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:50 UTC</span>

<span style="font-size: 90%;">So the rule would not actually work on Apache anyways, but it would work for ModSec on NGINX or other implementations?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:05 UTC</span>

<span style="font-size: 90%;">hmm</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:08 UTC</span>

<span style="font-size: 90%;">It might. FWIW, we have other rules that return status 400</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:23 UTC</span>

<span style="font-size: 90%;">(i.e. apache fails before the rule is evaluated)</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:40 UTC</span>

<span style="font-size: 90%;">I don’t see this being any different</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:00 UTC</span>

<span style="font-size: 90%;">But are we sure there is a need for the rule at all?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:27 UTC</span>

<span style="font-size: 90%;">Define there is a need</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:52 UTC</span>

<span style="font-size: 90%;">If both headers are present (and considered) this could be a bypass</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:53 UTC</span>

<span style="font-size: 90%;">There is a ton of RFC specifics that we do not test for because the webservers take care of it.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:14:23 UTC</span>

<span style="font-size: 90%;">Let’s put it on hold and I will test against nginx</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:23 UTC</span>

<span style="font-size: 90%;">If _all_ webservers make sure requests with both headers are blocked, the rule would be redundant.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:13 UTC</span>

<span style="font-size: 90%;">of course we're unsure how not apache/nginx/iis handle things from a libmodsec side</span>

**fgs** <span style="color: grey; font-size: 90%;">20:15:51 UTC</span>

<span style="font-size: 90%;">the rules can be consumed in many ways</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:03 UTC</span>

<span style="font-size: 90%;">brb</span>

**fgs** <span style="color: grey; font-size: 90%;">20:16:45 UTC</span>

<span style="font-size: 90%;">I will check nginx and update</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:13 UTC</span>

<span style="font-size: 90%;">Please do. I like the rule and if we see a platform that really needs it, then we should add it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:25 UTC</span>

<span style="font-size: 90%;">We're done with the PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:53 UTC</span>

<span style="font-size: 90%;">Next topic is a recurring one: We're piling up more and more issues / feature requests and we're not reducing them.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:21 UTC</span>

<span style="font-size: 90%;">We had a plan to reduce the pile when we met last July, but we have not been very successful. And I am probably worst, I have like 10 issues assigned and I do a 1000 things, but I do not manage to get them done.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:19:29 UTC</span>

<span style="font-size: 90%;">Sorry, need to go now :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:45 UTC</span>

<span style="font-size: 90%;">Bye _@fgs_. Thank you very much for your great work.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">I see nobody has a magic recipe how to get rid of issues...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:22:17 UTC</span>

<span style="font-size: 90%;">what about a weekly check for issues?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:59 UTC</span>

<span style="font-size: 90%;">What would you check?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:33 UTC</span>

<span style="font-size: 90%;">something like the the monthly chat but for issues only</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:48 UTC</span>

<span style="font-size: 90%;">Would you attend that?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:24:05 UTC</span>

<span style="font-size: 90%;">idk, I can try… many issues are really old…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:24:24 UTC</span>

<span style="font-size: 90%;">2013, 2014…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:47 UTC</span>

<span style="font-size: 90%;">Yes, they are. And we would certainly welcome any initiative of somebody willing to work on old issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:56 UTC</span>

<span style="font-size: 90%;">Or orchestrate a joint effort.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:30 UTC</span>

<span style="font-size: 90%;">in the next day I’ll try to get into the oldiest issues</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:48 UTC</span>

<span style="font-size: 90%;">I think the best would be if you try and motivate a group of people to join you and look into old issues. Like 5 per week would be awesome.
And I do not mind killing old issues that nobody cares about.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:09 UTC</span>

<span style="font-size: 90%;">You should probably start with 2-3. :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:27:36 UTC</span>

<span style="font-size: 90%;">It seems reasonable</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:27:38 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:27:42 UTC</span>

<span style="font-size: 90%;">that also seems good to me</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:09 UTC</span>

<span style="font-size: 90%;">What would be a good day to do such an effort _@theMiddle_? If you do it like every week?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:29:04 UTC</span>

<span style="font-size: 90%;">yes, I think I can try to handle a couple of issues a week</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:40 UTC</span>

<span style="font-size: 90%;">Meeting on Monday as well for a check for issues? 3 weeks per month issues, 1 week per month monthly chat?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:46 UTC</span>

<span style="font-size: 90%;">let’s try with “each monday” and see if it works, what do you think?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:26 UTC</span>

<span style="font-size: 90%;">You'd be my hero, that's for sure. I just can't promise you any support from my side. :disappointed:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:38 UTC</span>

<span style="font-size: 90%;">no problem, maybe getting into old issues is a good start and will drive us somewhere for sure :slightly_smiling_face:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:32:50 UTC</span>

<span style="font-size: 90%;">Hi guys, I'm pretty busy with the master and extra certs, training, CTF's, etc but will try to squeeze in some time to help you deal with old issues and join you on monday meetings</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:33:46 UTC</span>

<span style="font-size: 90%;">CTF? where? what? :smile:</span>

↳ **SpartanTri** <span style="color: grey; font-size: 90%;">20:35:41 UTC</span>

<span style="font-size: 90%;">I will do a couple sans trainings, so getting ready for forensics challenges this year, last year I won Paris and Las Vegas and ended 4th in the championship core netwars last</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:36:17 UTC</span>

<span style="font-size: 90%;">WOW! awesome :open_mouth:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:26 UTC</span>

<span style="font-size: 90%;">That's the first time I really see a plan in this regard. Thank you guys!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:50 UTC</span>

<span style="font-size: 90%;">Please make sure you get more people into the boat or you will be exhausted before long.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:13 UTC</span>

<span style="font-size: 90%;">_@airween_ is not around or is he?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:31 UTC</span>

<span style="font-size: 90%;">If not, can you update us on the status of the testsuite vs ModSec3, _@SpartanTri_?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:37:11 UTC</span>

<span style="font-size: 90%;">I will try to build a test modsec+ngnix environment for testing to check issues this weekend</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:43 UTC</span>

<span style="font-size: 90%;">I saw that  _@airween_ made more progress, but there are still issues with ModSec3, if I'm right.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:39:44 UTC</span>

<span style="font-size: 90%;">yes, and _@airween_ (my new personal hero) have fixed the “detection only” issue on v3</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:34 UTC</span>

<span style="font-size: 90%;">Can you guys make any guess as to how far we are from passing the testsuite completely on said platform?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:41:26 UTC</span>

<span style="font-size: 90%;">I think this is quite up-to-date with his progress: <https://docs.google.com/spreadsheets/d/1x_0kDBwJwh94xcwBX3N2YHce9ftgzNOdjyF8yk4YcUg/edit#gid=948831806></span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:10 UTC</span>

<span style="font-size: 90%;">To everyone: Please don't share the google docs outside this channel. _@airween_ asked to keep it amongst us.</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:53 UTC</span>

<span style="font-size: 90%;">hi there :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:58 UTC</span>

<span style="font-size: 90%;">So the Apache connector is actually doing better than NGINX.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:18 UTC</span>

<span style="font-size: 90%;">Hello _@airween_. You must have heard us holler your name. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:39 UTC</span>

<span style="font-size: 90%;">You made some great progress there.</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:50 UTC</span>

<span style="font-size: 90%;">yep, Slack notices me via e-mail</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:00 UTC</span>

<span style="font-size: 90%;">How many ModSec bugs did you solve so far on libModSec3?</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:10 UTC</span>

<span style="font-size: 90%;">it's still 34</span>

**csanders** <span style="color: grey; font-size: 90%;">20:44:12 UTC</span>

<span style="font-size: 90%;">nice, i'll make sure to add an a new docker image for that too</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:35 UTC</span>

<span style="font-size: 90%;">31, sorry</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:37 UTC</span>

<span style="font-size: 90%;">but</span>

**airween** <span style="color: grey; font-size: 90%;">20:45:10 UTC</span>

<span style="font-size: 90%;">I stucked with a bug</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:24 UTC</span>

<span style="font-size: 90%;">I see. On the connector, or ModSec3?</span>

**airween** <span style="color: grey; font-size: 90%;">20:45:47 UTC</span>

<span style="font-size: 90%;">related to 944120</span>

**airween** <span style="color: grey; font-size: 90%;">20:45:49 UTC</span>

<span style="font-size: 90%;">ModSec3</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:10 UTC</span>

<span style="font-size: 90%;">Does this explain this fail, or are there additional ones in the group of 31? I'm asking because I'd like to understand how far you are from completion (or libModSec3 from actually being somewhat production ready).</span>

**airween** <span style="color: grey; font-size: 90%;">20:47:25 UTC</span>

<span style="font-size: 90%;">I couldn't find any relevant info, how request body processor works</span>

**airween** <span style="color: grey; font-size: 90%;">20:47:31 UTC</span>

<span style="font-size: 90%;">exactly</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:04 UTC</span>

<span style="font-size: 90%;">the 31 bug can be divided to 4, or may be 5 big group</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:10 UTC</span>

<span style="font-size: 90%;">one of them is the 944120</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:18 UTC</span>

<span style="font-size: 90%;">That is tricky. I do not really understand either and I take it it's differnt in libModSec3.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:34 UTC</span>

<span style="font-size: 90%;">That's interesting info. So you could say like another 4-5 bugs?</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:40 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:51 UTC</span>

<span style="font-size: 90%;">that's what I wanted to wrote :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:54 UTC</span>

<span style="font-size: 90%;">4-5 bugs</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:00 UTC</span>

<span style="font-size: 90%;">And how many did you encounter / fix so far?</span>

**airween** <span style="color: grey; font-size: 90%;">20:49:27 UTC</span>

<span style="font-size: 90%;">one is exists in connector</span>

**airween** <span style="color: grey; font-size: 90%;">20:49:41 UTC</span>

<span style="font-size: 90%;">sorry, I'm collecting the infos... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:22 UTC</span>

<span style="font-size: 90%;">Nevermind. I think we have a better understanding now and in the end, we'll just wait and watch you in awe. You're a big support here.</span>

**airween** <span style="color: grey; font-size: 90%;">20:50:39 UTC</span>

<span style="font-size: 90%;">the 941330 is caused by connector: looks like mod_security module adds plus escape chars to any string in body</span>

**airween** <span style="color: grey; font-size: 90%;">20:50:56 UTC</span>

<span style="font-size: 90%;">and the new one doesn't do that</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:07 UTC</span>

<span style="font-size: 90%;">reflected to you question, that how many bug can I fix so far: I don't know exactly. I hope I can fix all of them, but few days ago I've discussed with modsec developers, and I heard that Felipe started to refactor the libmodsec3 code</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:17 UTC</span>

<span style="font-size: 90%;">that's a good news and bad too :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:34 UTC</span>

<span style="font-size: 90%;">because there are so many PR pending in ModSec3</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:34 UTC</span>

<span style="font-size: 90%;">Haha.</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:38 UTC</span>

<span style="font-size: 90%;">??</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:50 UTC</span>

<span style="font-size: 90%;">Refactoring was overdue, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:02 UTC</span>

<span style="font-size: 90%;">But all the PRs become stale of course.</span>

**airween** <span style="color: grey; font-size: 90%;">20:53:33 UTC</span>

<span style="font-size: 90%;">and I'm afraid if the code will refactored, the PR's will outdated...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:41 UTC</span>

<span style="font-size: 90%;">Good. Thank you for that insightful report.</span>

**airween** <span style="color: grey; font-size: 90%;">20:54:04 UTC</span>

<span style="font-size: 90%;">sorry that I could't said any better news... :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:21 UTC</span>

<span style="font-size: 90%;">I'd like to update you on the CRS community summit we are re-doing at the AppSec conference. It's now called AppSecGlobal and it's happening in Israel at the end of May.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:34 UTC</span>

<span style="font-size: 90%;">The CRS community summit is scheduled for May 28.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:58 UTC</span>

<span style="font-size: 90%;">We do not have a room yet, though. It seems getting one from OWASP is tricky. But that is my problem for the time being.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:33 UTC</span>

<span style="font-size: 90%;">Does anybody from you guys know if you will be coming to the conference?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:45 UTC</span>

<span style="font-size: 90%;">I'm thinking on going</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:00 UTC</span>

<span style="font-size: 90%;">Don't understand the schedule by OWASP, though</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:20 UTC</span>

<span style="font-size: 90%;">There is a global event on September/Amsterdan?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:08 UTC</span>

<span style="font-size: 90%;">Oh, look at that. Overlooked it, actually.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:15 UTC</span>

<span style="font-size: 90%;">`Global AppSec Amsterdam 	Sept 23-27, 2019 	Netherland `</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:30 UTC</span>

<span style="font-size: 90%;">Hmmm. The schedule is really tricky.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:35 UTC</span>

<span style="font-size: 90%;">Totally</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:40 UTC</span>

<span style="font-size: 90%;">And this: `Global AppSec DC 	Sept 9-13,2019 	Washington, D.C.`</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:58:03 UTC</span>

<span style="font-size: 90%;">Don't know how they are going to handle all those events</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:14 UTC</span>

<span style="font-size: 90%;">I though there would not a conf in Europe and that's how I aimed for Tel Aviv. But I reckon we would have a hard time gathering the community there. While as Amsterdam...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:19 UTC</span>

<span style="font-size: 90%;">What do you guys think?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:47 UTC</span>

<span style="font-size: 90%;">For those who go across the ocean, is not that much time</span>

**csanders** <span style="color: grey; font-size: 90%;">21:00:11 UTC</span>

<span style="font-size: 90%;">There's been an issue over here, I'm gonna have to jump out</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:41 UTC</span>

<span style="font-size: 90%;">See you _@csanders_!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:53 UTC</span>

<span style="font-size: 90%;">See you _@csanders_! Bye.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:30 UTC</span>

<span style="font-size: 90%;">_@emphazer_, _@theMiddle_ and _@airween_: Are you thinking about joining any of these conferences? More likely in Amsterdam?</span>

**airween** <span style="color: grey; font-size: 90%;">21:01:49 UTC</span>

<span style="font-size: 90%;">may be... in Amsterdam...</span>

**airween** <span style="color: grey; font-size: 90%;">21:02:13 UTC</span>

<span style="font-size: 90%;">my boss asked me, where should I/we go some interesting conference :stuck_out_tongue:</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:02:58 UTC</span>

<span style="font-size: 90%;">don't think so</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:03:10 UTC</span>

<span style="font-size: 90%;">it would be nice, but idk if I can in those days, it’s too early for me :confused:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:12 UTC</span>

<span style="font-size: 90%;">Not even Amsterdam? Would love to meet you again...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:32 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Amsterdam would be September.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:04:35 UTC</span>

<span style="font-size: 90%;">sorry, I mean that it’s too early to say if I can :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:01 UTC</span>

<span style="font-size: 90%;">I see.
But I do not see much interest to fly to Tel Aviv in May from you guys?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:17 UTC</span>

<span style="font-size: 90%;">Amsterdam would be a short trip for Walter, so that's a given.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:03 UTC</span>

<span style="font-size: 90%;">I'm trying to see if dates let me go to TLV</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:22 UTC</span>

<span style="font-size: 90%;">But don't know for certain yet</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:44 UTC</span>

<span style="font-size: 90%;">I see. Would you attend Amsterdam too? (And the dev Summit in London in June)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:32 UTC</span>

<span style="font-size: 90%;">Ah nevermind. Let's not spend more time on this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:59 UTC</span>

<span style="font-size: 90%;">Good questions :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:22 UTC</span>

<span style="font-size: 90%;">We agreed to push 3.2 for the next AppSecEU conf. If that's only Amsterdam in September, we still have time. Or maybe better aim for June / July to get into a 6 month release cycle.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:30 UTC</span>

<span style="font-size: 90%;">But nothing to discuss tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:45 UTC</span>

<span style="font-size: 90%;">Next item. The swag!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:08:51 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:09:27 UTC</span>

<span style="font-size: 90%;">I spent a lot of time discussing with people about their success in the world of creating swag :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:09:46 UTC</span>

<span style="font-size: 90%;">But I finally managed to get the first step</span>

**airween** <span style="color: grey; font-size: 90%;">21:09:51 UTC</span>

<span style="font-size: 90%;">(have to goo, see you later - good night!)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:01 UTC</span>

<span style="font-size: 90%;">Bye _@airween_! And thanks!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:21 UTC</span>

<span style="font-size: 90%;">To have vectorial images of the project's logos</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:25 UTC</span>

<span style="font-size: 90%;">Thank you for the SVG files. They were pending for so long.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:54 UTC</span>

<span style="font-size: 90%;">As I said, I suggest you add the vectors to the uses and then merge it to the OWASP swag project.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:10 UTC</span>

<span style="font-size: 90%;">Yes, I have that ready.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:24 UTC</span>

<span style="font-size: 90%;">But I've been reading the readme from the swag repo</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:31 UTC</span>

<span style="font-size: 90%;">I looked through all of them. I think the quality is excellent.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:39 UTC</span>

<span style="font-size: 90%;">Any obstacle in said readme?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:53 UTC</span>

<span style="font-size: 90%;">And they say don't upload multiple sizes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:00 UTC</span>

<span style="font-size: 90%;">Just the one with the best quality</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:24 UTC</span>

<span style="font-size: 90%;">How about only uploading the SVG + biggest resolution and a link to our full repository?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:36 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:40 UTC</span>

<span style="font-size: 90%;">That's the idea</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:47 UTC</span>

<span style="font-size: 90%;">Sounds like a plan then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:51 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:13:04 UTC</span>

<span style="font-size: 90%;">Then I'm going to try with a couple services</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:17 UTC</span>

<span style="font-size: 90%;">Great. I'm much looking forward to that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:13:21 UTC</span>

<span style="font-size: 90%;">To see how they get printed.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:13:33 UTC</span>

<span style="font-size: 90%;">Will be good to have also the poster there, don't you think?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:51 UTC</span>

<span style="font-size: 90%;">I think so. Feel free to add to swag. It's CC anyways.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:13:57 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:07 UTC</span>

<span style="font-size: 90%;">I assume the logos also?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:16 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:21 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:28 UTC</span>

<span style="font-size: 90%;">Great.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:44 UTC</span>

<span style="font-size: 90%;">So this brings us back to _@theMiddle_. Did you get the commit rights as planned?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:15:44 UTC</span>

<span style="font-size: 90%;">uhm is there a fast way to check it?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:23 UTC</span>

<span style="font-size: 90%;">I think somebody would have told you. Felipe Costa or Chaim Sanders who was supposed to get it done for you.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:30 UTC</span>

<span style="font-size: 90%;">No news?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:16:40 UTC</span>

<span style="font-size: 90%;">nope yet</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:26 UTC</span>

<span style="font-size: 90%;">Please go to <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1284>.
Do you have a green merge button near the bottom?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:17:51 UTC</span>

<span style="font-size: 90%;">uhm no</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:49 UTC</span>

<span style="font-size: 90%;">OK. I'll start to bug them myself then. Sorry. It's always such a drag. We are technically hosted under the Trustwave account on github, so Spiderlabs needs to give you commit rights.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:02 UTC</span>

<span style="font-size: 90%;">But we'll get it done.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:19:10 UTC</span>

<span style="font-size: 90%;">no problem!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:22 UTC</span>

<span style="font-size: 90%;">We have cleared up the docker container problems.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:57 UTC</span>

<span style="font-size: 90%;">_@emphazer_ has been sick for much of the month, so I suppose there are more important problems on his task list than blog posts.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:03 UTC</span>

<span style="font-size: 90%;">Looks like we are almost done.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:20:24 UTC</span>

<span style="font-size: 90%;">yes. but didnt lost the focus</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:24 UTC</span>

<span style="font-size: 90%;">There is only the question for Joomla support among our rule exclusions.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:33 UTC</span>

<span style="font-size: 90%;">Thank you _@emphazer_.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:34 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:44 UTC</span>

<span style="font-size: 90%;">I've noticed that the other day</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:51 UTC</span>

<span style="font-size: 90%;">We have drupal/wordpress</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:55 UTC</span>

<span style="font-size: 90%;">But not joomla</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:21:06 UTC</span>

<span style="font-size: 90%;">Is there any interest on pushing that one?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:13 UTC</span>

<span style="font-size: 90%;">_@emphazer_ is joining the head of the Joomla security team at cloudfest in a couple of weeks. Would that be something to discuss with him as well?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:21:25 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:38 UTC</span>

<span style="font-size: 90%;">If you have capacity to work on this _@fzipitria_, it's certainly welcome.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:21:48 UTC</span>

<span style="font-size: 90%;">definetly I think. I will talk with him</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:11 UTC</span>

<span style="font-size: 90%;">I'll try to find out if there is anyone with some rules already</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:21 UTC</span>

<span style="font-size: 90%;">If there is someone in this channel, just ping me</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:27 UTC</span>

<span style="font-size: 90%;">That would be a welcome addition for 3.2.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:04 UTC</span>

<span style="font-size: 90%;">_@David Jardin_ is the Joomla guy if that matters. He was here before in this channel. Just not tonight.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:20 UTC</span>

<span style="font-size: 90%;">Excellent, will ping him then</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:28 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:56 UTC</span>

<span style="font-size: 90%;">And finally, _@theMiddle_ says he has rules to cover for XXE?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:24:37 UTC</span>

<span style="font-size: 90%;">I’ve a working PoC and I’m trying to define a rule</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:25:01 UTC</span>

<span style="font-size: 90%;">I’m working on this: <https://github.com/vulhub/vulhub/tree/master/php/php_xxe></span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:05 UTC</span>

<span style="font-size: 90%;">Would that be a complete rule or just one in a longer series?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:25:40 UTC</span>

<span style="font-size: 90%;">I’m trying to cover a list of payloads that I’ve collected</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:02 UTC</span>

<span style="font-size: 90%;">I see. That would make for a nice contribution. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:19 UTC</span>

<span style="font-size: 90%;">Just share when you think you have something to show. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:53 UTC</span>

<span style="font-size: 90%;">Thank you everyone for 2 very intense and fruitful hours. It's been very productive to talk to you, I think.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:27:23 UTC</span>

<span style="font-size: 90%;">thank you _@dune73_ and thanks all!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:27:52 UTC</span>

<span style="font-size: 90%;">I’ll bugging the chan next monday :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:03 UTC</span>

<span style="font-size: 90%;">Yes, great plan!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:28:17 UTC</span>

<span style="font-size: 90%;">See you around!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:29 UTC</span>

<span style="font-size: 90%;">If this works out, it's the biggest achievement of tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:36 UTC</span>

<span style="font-size: 90%;">See you around and thanks for joining!</span>

**fgs** <span style="color: grey; font-size: 90%;">22:18:38 UTC</span>

<span style="font-size: 90%;">Sigh, the topic today was quite important and closer to home. Too bad I missed it.</span>

