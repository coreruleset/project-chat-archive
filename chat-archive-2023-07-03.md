### Mon, Jul 3rd, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:31:04 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's the first Monday of the month and we're starting our CRS chat.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:15 UTC</span>

<span style="font-size: 90%;">Please find the agenda at [https://github.com/coreruleset/coreruleset/issues/3240](https://github.com/coreruleset/coreruleset/issues/3240)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:27 UTC</span>

<span style="font-size: 90%;">So who's around for our meeting?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:31:50 UTC</span>

<span style="font-size: 90%;">Hi hi</span>

**airween** <span style="color: grey; font-size: 90%;">18:32:01 UTC</span>

<span style="font-size: 90%;">hi all!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:07 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:20 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:32 UTC</span>

<span style="font-size: 90%;">Good to see you around.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:04 UTC</span>

<span style="font-size: 90%;">Franziska is celebrating, Walter is off-screen and Felipe seems to be above the clouds. So let's get going.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:42 UTC</span>

<span style="font-size: 90%;">In the non-project section there is this new openresty approach at running CRS without ModSec. This has been around before, but this time it looks more serious.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:23 UTC</span>

<span style="font-size: 90%;">Coraza reports movement with regards to the libCoraza port towards Nginx. Quite good to hear.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:05 UTC</span>

<span style="font-size: 90%;">If you look through the subprojects you'll see that things are moving forward steadily. Namely our GSoC project is very promising.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:27 UTC</span>

<span style="font-size: 90%;">And we're getting closer with the final rule updates in direction of CRS v4, more about this later.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:44 UTC</span>

<span style="font-size: 90%;">Any questions / updates about sub-projects?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:40 UTC</span>

<span style="font-size: 90%;">I do not see anybody typing, so I presume we're good.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:44 UTC</span>

<span style="font-size: 90%;">_@xanadu_ (?) asked about the potential CVE for one of the open security issues. I have updated that directly in the agenda. Researcher did not confirm, but we would prefer to go without CVE (namely because it's primarily a platform issue and our reference platform is not affected)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:40:26 UTC</span>

<span style="font-size: 90%;">(That was me :slightly_smiling_face: Thanks for the update.)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:53 UTC</span>

<span style="font-size: 90%;">You're welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:59 UTC</span>

<span style="font-size: 90%;">Continue with the PHP function calls?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:16 UTC</span>

<span style="font-size: 90%;">The entry point into said thread is this: [https://github.com/coreruleset/coreruleset/pull/3228#issuecomment-1604929859](https://github.com/coreruleset/coreruleset/pull/3228#issuecomment-1604929859)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:07 UTC</span>

<span style="font-size: 90%;">If you scroll upwards you find a graphic of what we agreed to do. Turns out the status quo is not quite what the comment says. But I still think the plan is correct, yet spell.sh is skipping a few words we have to include (because they are natural language in an IT context without being in the Merriam Webster dictionary. Think "basename". So _@maxleske_ proposed to add a hardcoded list of terms to the output of spell.sh.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:32 UTC</span>

<span style="font-size: 90%;">What do you all think about this? Please take 3-4 minutes to read through the thread and understanding the situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:01 UTC</span>

<span style="font-size: 90%;">So what do you think?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:46:11 UTC</span>

<span style="font-size: 90%;">The plan still sounds sensible.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:46:51 UTC</span>

<span style="font-size: 90%;">I agree about an hardcoded list of terms. It might be an extra burden to maintain it, but I guess sooner or later IT specific terms will came up and require specific care</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:12 UTC</span>

<span style="font-size: 90%;">I do not think maintenance is a problem. This list will hardly ever change.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:12 UTC</span>

<span style="font-size: 90%;">Where I am a bit unsure is the fact that the existing rules are substantially larger than what we want to deliver for CRSv4. But that was manual and mostly based on Walter's judgement. Now it is clearer and more consistent.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:41 UTC</span>

<span style="font-size: 90%;">I just hope we do not give up a lot of detection power.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:59 UTC</span>

<span style="font-size: 90%;">I think iterative improvement is unavoidable. But doing that on a solidly automated base is much better than playing the guessing game and living in fear of changing anything. That's not sustainable.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:08 UTC</span>

<span style="font-size: 90%;">Nicely put. So we continue on the path we've taken.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:04 UTC</span>

<span style="font-size: 90%;">_@Matteo Pace_ I am mostly done with the wrapper script. I can hand this over to you for polishing and connecting with existing files etc. Are you ready to take over?
If yes, we only have to discuss who will perform the spell.sh extension.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:20 UTC</span>

<span style="font-size: 90%;">Is the existing spell.sh that adopts WordNet still open or already merged?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:35 UTC</span>

<span style="font-size: 90%;">It's still open: [https://github.com/coreruleset/coreruleset/pull/3242](https://github.com/coreruleset/coreruleset/pull/3242)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:05 UTC</span>

<span style="font-size: 90%;">I'm still waiting for an approving review</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:22 UTC</span>

<span style="font-size: 90%;">All we need here is a review and then merge, correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:35 UTC</span>

<span style="font-size: 90%;">yes</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:55:27 UTC</span>

<span style="font-size: 90%;">Are you ready to take over?Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:16 UTC</span>

<span style="font-size: 90%;">Thanks _@Matteo Pace_. So who will review the existing spell.sh PR and who will write the extension for the hardcoded items? (good description in discussion in PR 3228.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:05 UTC</span>

<span style="font-size: 90%;">I can finish the script. Just create the list of words you want to check and tell me where it is.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:22 UTC</span>

<span style="font-size: 90%;">OK, I will do the wordlist and you update the spell.sh script. Can you also review the existing PR?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:49 UTC</span>

<span style="font-size: 90%;">[#3228](https://github.com/coreruleset/coreruleset/issues/#3228) you mean?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:04 UTC</span>

<span style="font-size: 90%;">No, [#3242](https://github.com/coreruleset/coreruleset/issues/#3242). We need to merge that spell.sh PR before we can do another one.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:23 UTC</span>

<span style="font-size: 90%;">Then I hand you over my php function script (that relies on spell.sh).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:23 UTC</span>

<span style="font-size: 90%;">It's my PR, I can't do the review :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:29 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:08 UTC</span>

<span style="font-size: 90%;">I'll ping _@fzipitria_ to do the review.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:09 UTC</span>

<span style="font-size: 90%;">OK. So we prepare everything and _@Matteo Pace_ can then create the function list PR. That sounds reasonable.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:36 UTC</span>

<span style="font-size: 90%;">Afterwards, only your issues open, I think _@maxleske_. Or am I overlooking somehting?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:31 UTC</span>

<span style="font-size: 90%;">That's correct. I'm waiting for feedback from you and _@theMiddle_. I'm currently working on the second issue and should have a PR ready this week.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:03 UTC</span>

<span style="font-size: 90%;">Feeback here please: [https://github.com/coreruleset/coreruleset/issues/2644](https://github.com/coreruleset/coreruleset/issues/2644)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:04 UTC</span>

<span style="font-size: 90%;">Oops. Thanks for the reminder. Did not have that on my list. I'll try respond asap.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:46 UTC</span>

<span style="font-size: 90%;">So it looks like this is all settled.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:54 UTC</span>

<span style="font-size: 90%;">Any other PRs we should discuss as a group?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:35 UTC</span>

<span style="font-size: 90%;">If that's not the case, then please let me add the observation, that we're piling up issues since we no longer auto-closing them.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:46 UTC</span>

<span style="font-size: 90%;">Other than that, I think we're done.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:17 UTC</span>

<span style="font-size: 90%;">That was quick! Good night everyone!</span>

**jit** <span style="color: grey; font-size: 90%;">19:09:50 UTC</span>

<span style="font-size: 90%;">Good night everyone! :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:03 UTC</span>

<span style="font-size: 90%;">Night!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:10:18 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:24 UTC</span>

<span style="font-size: 90%;">Good night and thank you for attending!</span>

**airween** <span style="color: grey; font-size: 90%;">19:10:51 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:11:00 UTC</span>

<span style="font-size: 90%;">Good night</span>

