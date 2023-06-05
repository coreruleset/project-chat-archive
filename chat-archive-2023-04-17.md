### Mon, Apr 17th, 2023

**maxleske** <span style="color: grey; font-size: 90%;">18:30:17 UTC</span>

<span style="font-size: 90%;">:blob-wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:11 UTC</span>

<span style="font-size: 90%;">Hello _@maxleske_, hello everybody!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">hello everybody</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:35 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:56 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:59 UTC</span>

<span style="font-size: 90%;">Hey ho!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:19 UTC</span>

<span style="font-size: 90%;">hello!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:32:30 UTC</span>

<span style="font-size: 90%;">hey!</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">18:32:51 UTC</span>

<span style="font-size: 90%;">Hi everyone. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:02 UTC</span>

<span style="font-size: 90%;">Hey _@jit(Xhoenix)_ great to see you again. Welcome.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:33:37 UTC</span>

<span style="font-size: 90%;">hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:28 UTC</span>

<span style="font-size: 90%;">So our agenda is at [https://github.com/coreruleset/coreruleset/issues/3159](https://github.com/coreruleset/coreruleset/issues/3159)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:39 UTC</span>

<span style="font-size: 90%;">Franziska is not around, I'll try to write down decisions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:58 UTC</span>

<span style="font-size: 90%;">As it stands we'll going to look into 7 PRs, most of them stale and see what we can do.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:42 UTC</span>

<span style="font-size: 90%;">I merged a few ones today and the infamous nextcloud PR is about to be resolved thanks to _@jit(Xhoenix)_ and _@azurIt_ who covered it all in their work on the RE plugin.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">18:49:16 UTC</span>

<span style="font-size: 90%;">Also _@maxleske_ helped a lot!</span>

↳ **jit(Xhoenix)** <span style="color: grey; font-size: 90%;">18:51:28 UTC</span>

<span style="font-size: 90%;">Yeah, _@azurIt_ is right, _@maxleske_ really helped a lot.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:19 UTC</span>

<span style="font-size: 90%;">So chances are we'll get below 10 PRs in a week or two. (Still above 105 issues, though).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:25 UTC</span>

<span style="font-size: 90%;">Anything else to add to the agenda?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:29 UTC</span>

<span style="font-size: 90%;">We've updated the container image.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:00 UTC</span>

<span style="font-size: 90%;">And I managed to fix the nightly builds.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:11 UTC</span>

<span style="font-size: 90%;">That's very good news.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:17 UTC</span>

<span style="font-size: 90%;">(they would sometimes be marked as draft release)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:38 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ are you making progress with Coraza? It sounds more difficult than we anticipated ...</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:39:10 UTC</span>

<span style="font-size: 90%;">It kind of is because silly issues in my image. The concept is simpler tho.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:39:31 UTC</span>

<span style="font-size: 90%;">yes today I've started to integrate it on sandbox, but I would like to replace the container entrypoint as we already do for apache and nginx</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:45 UTC</span>

<span style="font-size: 90%;">Thanks. So I guess we'll get there and you get top support from the experts.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:59 UTC</span>

<span style="font-size: 90%;">OK, then I suggest we get started with the PRs. I'm taking them from the top of the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:19 UTC</span>

<span style="font-size: 90%;">2878 goes first. [https://github.com/coreruleset/coreruleset/pull/2878](https://github.com/coreruleset/coreruleset/pull/2878)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:33 UTC</span>

<span style="font-size: 90%;">This one was previously marked as "postpone the discussion after 4.0", FWIW.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:39 UTC</span>

<span style="font-size: 90%;">But maybe it can be re-evaluated</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:44:29 UTC</span>

<span style="font-size: 90%;">not really clear the context for me, but I'm reading the conversation</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:45 UTC</span>

<span style="font-size: 90%;">We know there is a problem and we have this documented. So I think we can just drop the PR and follow our plan to return to this issue after 4.0.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:08 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ It's a very long thread. Better look at the minimal change: a comment.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:30 UTC</span>

<span style="font-size: 90%;">There is a documentation issue open "for future consideration after 4.0" ([https://github.com/coreruleset/documentation/issues/79](https://github.com/coreruleset/documentation/issues/79)). Maybe just keeping that open will suffice.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;">I'd say so, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:52 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:51 UTC</span>

<span style="font-size: 90%;">I do not see anybody typing. So let's close this. _@xanadu_ could you please explain this briefly, link to the issue and then close it?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:47:19 UTC</span>

<span style="font-size: 90%;">Explain it here in the chat? Or in the issue?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:09 UTC</span>

<span style="font-size: 90%;">Explain our decision in the PR.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:48:16 UTC</span>

<span style="font-size: 90%;">I see. Yes, I will do that.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:16 UTC</span>

<span style="font-size: 90%;">And link the docs issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:22 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:33 UTC</span>

<span style="font-size: 90%;">Next one: 2637
[https://github.com/coreruleset/coreruleset/pull/2637/files](https://github.com/coreruleset/coreruleset/pull/2637/files)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:49:32 UTC</span>

<span style="font-size: 90%;">This is a PR from an external contributor. I tried to rescue it in October with a rebase. Unfortunately, it requires more attention than a rebase. It also probably needs another rebase by now :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:35 UTC</span>

<span style="font-size: 90%;">If I get this right, this is an incomplete PR that needs the tests moved too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:49 UTC</span>

<span style="font-size: 90%;">Agree on the rebase.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:18 UTC</span>

<span style="font-size: 90%;">External contributor is founder of CRS integrator [securely.ai](http://securely.ai).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:47 UTC</span>

<span style="font-size: 90%;">He probably gave up on this PR when we did not merge as is, or whatever. We can try to bring him back into the conversation, or somebody grabs it and does the job.
Yet, we have not yet discussed if the desired change really is what we aim for. It's apparently (?) a FP fix.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:44 UTC</span>

<span style="font-size: 90%;">It's an improvement on a change that _@Paul Beckett_ made in Varese. The PR is in a good state IIRC and I just wanted another review from _@xanadu_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:55 UTC</span>

<span style="font-size: 90%;">After that we can probably merge it.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:10 UTC</span>

<span style="font-size: 90%;">I think it needs more attention than a review. It's failing tests.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:20 UTC</span>

<span style="font-size: 90%;">Thanks for that background info _@maxleske_</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:48 UTC</span>

<span style="font-size: 90%;">Oh. Well than that's my job. Let me fix it.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:54:32 UTC</span>

<span style="font-size: 90%;">Well, it's the job of anyone who has time to sort out a series of tests, it doesn't need to fall on you :slightly_smiling_face:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:54:47 UTC</span>

<span style="font-size: 90%;">I don't have time to give it attention at the minute.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:55:15 UTC</span>

<span style="font-size: 90%;">Yeah but I made the latest changes to the PR and I self assigned it :slightly_smiling_face:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:55:38 UTC</span>

<span style="font-size: 90%;">Oh, I see, fair enough.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:53:58 UTC</span>

<span style="font-size: 90%;">Good evening. Sorry I'm late</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:59 UTC</span>

<span style="font-size: 90%;">I’m also not 100% sure we should do it. --> was moved to PL2 because it’s reasonably common in text fields and also closing a comment would probably not be so dangerous as opening one. Do we want to move this to PL2 at all?</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:42 UTC</span>

<span style="font-size: 90%;"><!-- is not so FP sensitive, but perhaps could trigger interesting behaviors…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:49 UTC</span>

<span style="font-size: 90%;">I agree with _@walter_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:18 UTC</span>

<span style="font-size: 90%;">Anybody understand the reasoning by the contributor? Is it really FPs?</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:52 UTC</span>

<span style="font-size: 90%;">Consistency is not really a good reason. We have to make balanced choices between FP and security</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">and that differs between these two strings…</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:53 UTC</span>

<span style="font-size: 90%;">Let me look over it and think about it. I'll trigger the conversation in the PR and we can decide then.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:41 UTC</span>

<span style="font-size: 90%;">Sounds good. Thank you very much.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:15 UTC</span>

<span style="font-size: 90%;">We come to a set of 3 PRs by _@theMiddle_. Let's start with [#2303](https://github.com/coreruleset/coreruleset/issues/#2303).
[https://github.com/coreruleset/coreruleset/pull/2303](https://github.com/coreruleset/coreruleset/pull/2303)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:29 UTC</span>

<span style="font-size: 90%;">Or should we start with [#2301](https://github.com/coreruleset/coreruleset/issues/#2301). It seems there is more explanation in that PR...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:02:09 UTC</span>

<span style="font-size: 90%;">this PR is dated 2021 :sob:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:02:13 UTC</span>

<span style="font-size: 90%;">shame on me</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:41 UTC</span>

<span style="font-size: 90%;">Those seemed like simple fixes, but then we discovered issues...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:34 UTC</span>

<span style="font-size: 90%;">I get the feeling this is all a bit hairy, probably needs a rebase, touches on the PHP rules we are working on because of the keyword list and after 1.5 years without much action, it's probably not overly important...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:36 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ and I agreed that we could not solve the aliasing issue, so the PR's should not focus on that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:31 UTC</span>

<span style="font-size: 90%;">The original intention seemed to be to make the regex match only valid PHP syntax</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:52 UTC</span>

<span style="font-size: 90%;">yes but the main point was fixing redos problems IIRC</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:18 UTC</span>

<span style="font-size: 90%;">That is a worthwhile endeavor (that would not trigger much interest by a wider community for 1.5 years).</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:07:58 UTC</span>

<span style="font-size: 90%;">yeah, since a redos is not a FP nobody really cares I guess (me first)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:05 UTC</span>

<span style="font-size: 90%;">but it worth a try to fix</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:26 UTC</span>

<span style="font-size: 90%;">Can you replicate the supposed ReDoS problem(s)?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:30 UTC</span>

<span style="font-size: 90%;">yes, I've not added information on the issue, but yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:49 UTC</span>

<span style="font-size: 90%;">OK, so the problem is real and the information is available.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:38 UTC</span>

<span style="font-size: 90%;">But we are unsure we can fix it -  or do you guys see a solution without introducing FPs/FNs? (Sorry if it is obvious, but I do not fully understand the conversation in the PRs and the reviews)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:58 UTC</span>

<span style="font-size: 90%;">?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:13:13 UTC</span>

<span style="font-size: 90%;">I really need to review it maybe with the help of crs toolchain I can fix the regex in a better way</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:13:37 UTC</span>

<span style="font-size: 90%;">since this is opened for 1.5 y I really want to solve/close in this week</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:53 UTC</span>

<span style="font-size: 90%;">I'll try to help if I can</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:14:18 UTC</span>

<span style="font-size: 90%;">tnx</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:49 UTC</span>

<span style="font-size: 90%;">Thank you guys. Much appreciated.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:15 UTC</span>

<span style="font-size: 90%;">Next one 2217: [https://github.com/coreruleset/coreruleset/pull/2217](https://github.com/coreruleset/coreruleset/pull/2217)</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:49 UTC</span>

<span style="font-size: 90%;">well, this is older than _@theMiddle_'s PR's above...</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:51 UTC</span>

<span style="font-size: 90%;">This should be a plugin now, right</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:11 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:18 UTC</span>

<span style="font-size: 90%;">What do we do?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:23 UTC</span>

<span style="font-size: 90%;">Any roundcube users around?</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:28 UTC</span>

<span style="font-size: 90%;">yes, that's the plan. I would take care of it (with help of _@azurIt_?)</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:17:58 UTC</span>

<span style="font-size: 90%;">Sure thing!</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:39 UTC</span>

<span style="font-size: 90%;">We are using RoundCube heavily</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:46 UTC</span>

<span style="font-size: 90%;">Good news.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:02 UTC</span>

<span style="font-size: 90%;">(Last time I used that software was probably 2005 ...)</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:07 UTC</span>

<span style="font-size: 90%;">I put in to my to-do list</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">No, RC (RoundCube) is actively developed</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:37 UTC</span>

<span style="font-size: 90%;">Visually it looks normal, I run Roundcube and made some exclusions for it myself (although sadly DirectAdmin seems to have disabled ModSecurity on it which I haven’t resolved yet). I would probably removeTargetByTag=OWASP_CRS on _message though.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:41 UTC</span>

<span style="font-size: 90%;">Is that to-do list very long these days (asking for a friend)?</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:22 UTC</span>

<span style="font-size: 90%;">A new version of Roundcube has been released 2-3 years ago but fortunately they did not change too much about the API</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:47 UTC</span>

<span style="font-size: 90%;">_@azurIt_ can you give _@airween_ a  hand just in case?</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:18:55 UTC</span>

<span style="font-size: 90%;">Of course</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:06 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:30 UTC</span>

<span style="font-size: 90%;">Final one: 3190</span>

**airween** <span style="color: grey; font-size: 90%;">19:20:42 UTC</span>

<span style="font-size: 90%;">Sometimes I feel that's an infinity list... But I'm working on a huge migration: I joined more and more of our servers to the "ModSecurity" family. Our mail server does not have ModSec yet, but now it's time to migrate it. I can configure it separately from the users, and can involve some users to help the testing</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:20:42 UTC</span>

<span style="font-size: 90%;">Sometimes I feel that's an infinity list... But I'm working on a huge migration: I joined more and more of our servers to the "ModSecurity" family. Our mail server does not have ModSec yet, but now it's time to migrate it. I can configure it separately from the users, and can involve some users to help the testing</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:42 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3910](https://github.com/coreruleset/coreruleset/pull/3910)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:21:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3190](https://github.com/coreruleset/coreruleset/pull/3190) is the correct URL :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3190](https://github.com/coreruleset/coreruleset/pull/3190) is the correct URL :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:21:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3190](https://github.com/coreruleset/coreruleset/pull/3190) is the correct URL :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:42 UTC</span>

<span style="font-size: 90%;">please see this comment:

[https://github.com/coreruleset/coreruleset/pull/3190#issuecomment-1511236192](https://github.com/coreruleset/coreruleset/pull/3190#issuecomment-1511236192)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:42 UTC</span>

<span style="font-size: 90%;">Yes, that one. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:58 UTC</span>

<span style="font-size: 90%;">So that's not really stale.</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:00 UTC</span>

<span style="font-size: 90%;">If we want to allow the indents (rather we would expect them) before comments which are between parts of chained rules, we have to modified the msc_pyparser too.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:36 UTC</span>

<span style="font-size: 90%;">The case is this:
SecRule...
    chain"
    #comment
    SecRule ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:02 UTC</span>

<span style="font-size: 90%;">Does that even work on all platforms?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:23:33 UTC</span>

<span style="font-size: 90%;">hmm... good question! Let me check!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:02 UTC</span>

<span style="font-size: 90%;">This is currently valid:
SecRule...
    chain"
#comment
    SecRule ...</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:23:15 UTC</span>

<span style="font-size: 90%;">Curious!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:23:20 UTC</span>

<span style="font-size: 90%;">Never thought about that.</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:33 UTC</span>

<span style="font-size: 90%;">hmm... good question! Let me check!</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:23:33 UTC</span>

<span style="font-size: 90%;">hmm... good question! Let me check!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:40 UTC</span>

<span style="font-size: 90%;">Well actually, I think ModSec will be fine with this - but I hate it. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:51 UTC</span>

<span style="font-size: 90%;">hate what?</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:03 UTC</span>

<span style="font-size: 90%;">insert comments between parts of a chained rule?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:11 UTC</span>

<span style="font-size: 90%;">It's a matter of context. The comment does not belong to the starter rule.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:24:12 UTC</span>

<span style="font-size: 90%;">we have problems with 932200 too with "let" from let's encrypt. but I will open an issue for that tomorrow</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:28 UTC</span>

<span style="font-size: 90%;">I think chained rules should be kept together visually. If you add comments people will read the rules wrong. The chain directive is easy to overlook.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:26:02 UTC</span>

<span style="font-size: 90%;">I also prefer this way. But if majority wants to use the other form, I accept that. But it would be fine to put the rule to our documentation: [https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:30 UTC</span>

<span style="font-size: 90%;">_@emphazer_ There's already an open issue for that</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:24:37 UTC</span>

<span style="font-size: 90%;">ah ok</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:50 UTC</span>

<span style="font-size: 90%;">Came across httpie today ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:01 UTC</span>

<span style="font-size: 90%;">-> same list / issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:30 UTC</span>

<span style="font-size: 90%;">I personally think we should steer clear of comments between chained rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:35 UTC</span>

<span style="font-size: 90%;">Or is there a strong reason to do so?</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:37 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:25:39 UTC</span>

<span style="font-size: 90%;">I think the comments should be mentioned at the top and in detail, rather then in between the rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:50 UTC</span>

<span style="font-size: 90%;">With the reworked PR those should be straight forward to handle. Just add them to the benign-user-agents.data list.</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:02 UTC</span>

<span style="font-size: 90%;">I also prefer this way. But if majority wants to use the other form, I accept that. But it would be fine to put the rule to our documentation: [https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:26:02 UTC</span>

<span style="font-size: 90%;">I also prefer this way. But if majority wants to use the other form, I accept that. But it would be fine to put the rule to our documentation: [https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/CONTRIBUTING.md#general-formatting-guidelines-for-rules-contributions)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:16 UTC</span>

<span style="font-size: 90%;">Just to be absolutely clear what we are talking about:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:48 UTC</span>

<span style="font-size: 90%;">chain should be immediately followed by SecRule in my eyes.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:23 UTC</span>

<span style="font-size: 90%;">Unless there is a very good reason to put an uber important comment above a chain rule?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:25 UTC</span>

<span style="font-size: 90%;">Is there such a reason here?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:29 UTC</span>

<span style="font-size: 90%;">SecRule REQUEST_HEADERS:User-Agent "!@pmFromFile benign-user-agents.data" \
    "id:932239,\
    phase:2,\
    block,\
    t:none,\
    chain"
# Regular expression generated from regex-assembly/932239-chain1.ra.
# To update the regular expression run the following shell script
# (consult [https://coreruleset.org/docs/development/regex_assembly/](https://coreruleset.org/docs/development/regex_assembly/) for details):
#   crs-toolchain regex update 932239-chain1
    SecRule REQUEST_HEADERS:User-Agent "@rx ..."</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:40 UTC</span>

<span style="font-size: 90%;">Now imagine this:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:23 UTC</span>

<span style="font-size: 90%;"># Regular expression generated from regex-assembly/932239.ra.
# To update the regular expression run the following shell script
# (consult [https://coreruleset.org/docs/development/regex_assembly/](https://coreruleset.org/docs/development/regex_assembly/) for details):
#   crs-toolchain regex update 932239
# Regular expression generated from regex-assembly/932239-chain1.ra.
# To update the regular expression run the following shell script
# (consult [https://coreruleset.org/docs/development/regex_assembly/](https://coreruleset.org/docs/development/regex_assembly/) for details):
#   crs-toolchain regex update 932239-chain1

SecRule REQUEST_HEADERS:User-Agent "@rx ..." \
    "id:932239,\
    phase:2,\
    block,\
    t:none,\
    chain"
    SecRule REQUEST_HEADERS:User-Agent "@rx ..."</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:31 UTC</span>

<span style="font-size: 90%;">Now tell me again that's readable... :wink:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:28:52 UTC</span>

<span style="font-size: 90%;">uhmm I see</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:01 UTC</span>

<span style="font-size: 90%;">I don’t have so much problems with it…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:22 UTC</span>

<span style="font-size: 90%;">I like the 2nd option much better. The comments could be made clearer, but rules are easier to read.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:40 UTC</span>

<span style="font-size: 90%;">But I agree it might be a question of being used to one way or the other.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:43 UTC</span>

<span style="font-size: 90%;">Could we say
# Regular expression for part 2 / chain rule 2 generated from regex-assembly/932239-chain1.ra.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:44 UTC</span>

<span style="font-size: 90%;">or something?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:12 UTC</span>

<span style="font-size: 90%;">Ok. I can live with it. Just wanted to make the situation clear.</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:25 UTC</span>

<span style="font-size: 90%;">about a year ago I've started to work about a CRS meta-documentation maker. [https://crsdoc.digitalwave.hu](https://crsdoc.digitalwave.hu) uses that parser.

If the comments would be between the chained parts, that would be a huge s*ck to parse them...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:57 UTC</span>

<span style="font-size: 90%;">So let's enforce this then: no comments between chains</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:00 UTC</span>

<span style="font-size: 90%;">We could do "932239-SecRule-1" in case of a chain. Or "932239" for the 1st one and then "932239-SecRule-n" on subsequent ones.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:31:40 UTC</span>

<span style="font-size: 90%;">-chain<n> is actually mandatory</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:31:03 UTC</span>

<span style="font-size: 90%;">I don't find any problems with any chain rules as they're written right now.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:28 UTC</span>

<span style="font-size: 90%;">I can update the contributing guidelines to reflect "no comments between chains, always at the top of the rule chain."</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:48 UTC</span>

<span style="font-size: 90%;">So that's settled then?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:02 UTC</span>

<span style="font-size: 90%;">I'll revise the PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:28 UTC</span>

<span style="font-size: 90%;">Thank you _@maxleske_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:47 UTC</span>

<span style="font-size: 90%;">We're mostly done with the agenda it seems. During the chat, there was a thing that occurred to me, though.</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:57 UTC</span>

<span style="font-size: 90%;">should I add this contribution rule to [rules-check](https://github.com/coreruleset/coreruleset/tree/v4.0/dev/util/crs-rules-check) as a new action?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:07 UTC</span>

<span style="font-size: 90%;">If possible!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:10 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">Good.</span>

**Part of the conversation here was removed since it did not cover CRS, but Coraza development.**

**dune73** <span style="color: grey; font-size: 90%;">20:32:58 UTC</span>

<span style="font-size: 90%;">Thank you all for attending, and _@Juan Pablo Tosso_ for joining the conversation.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:36 UTC</span>

<span style="font-size: 90%;">Awesome Emoji.</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:52 UTC</span>

<span style="font-size: 90%;">Thank you for leading!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:34:40 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">20:34:44 UTC</span>

<span style="font-size: 90%;">Goodnight everyone.</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:45 UTC</span>

<span style="font-size: 90%;">GN!</span>

**airween** <span style="color: grey; font-size: 90%;">20:34:49 UTC</span>

<span style="font-size: 90%;">good night!</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:35:22 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:36:36 UTC</span>

<span style="font-size: 90%;">Good night</span>

