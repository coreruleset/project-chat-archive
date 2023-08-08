### Mon, Aug 7th, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:31:13 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:26 UTC</span>

<span style="font-size: 90%;">Welcome to the chat everyone. So who's around?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:31:43 UTC</span>

<span style="font-size: 90%;">Good evening :wave:</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:51 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:56 UTC</span>

<span style="font-size: 90%;">Hello Matteo! Hi Airween</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:07 UTC</span>

<span style="font-size: 90%;">hi, I’m still sick so expect not too much bright input from me but I’d like to chat along</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:22 UTC</span>

<span style="font-size: 90%;">Hello Walter, very nice to see you!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:36 UTC</span>

<span style="font-size: 90%;">Good evening :wave: :grin: </span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:43 UTC</span>

<span style="font-size: 90%;">Franziska sends her regards, she will be late for the meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:46 UTC</span>

<span style="font-size: 90%;">Hi Emphazer!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:32:57 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:13 UTC</span>

<span style="font-size: 90%;">Hey _@azurIt_, cool to see you around!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:40 UTC</span>

<span style="font-size: 90%;">So our agenda is at [https://github.com/coreruleset/coreruleset/issues/3252](https://github.com/coreruleset/coreruleset/issues/3252)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:00 UTC</span>

<span style="font-size: 90%;">We worked with an draft in the wiki and I hope we did not overwrite our changes this time. :slightly_smiling_face:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:36:05 UTC</span>

<span style="font-size: 90%;">Sorry I'm out with kids this evening as it's school holidays</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:33 UTC</span>

<span style="font-size: 90%;">As you probably know, we had a CVE that we knew about. What we did not know was that the researcher planned to go out with the CVE without coordinating. This caught us on the wrong foot. He apologized, though. Newbie, did not expect Mitre to publish immediately ...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:55 UTC</span>

<span style="font-size: 90%;">Then the ModSecurity v3 CVE that affects our users as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:28 UTC</span>

<span style="font-size: 90%;">_@airween_ do we have any knowledge about the Debian / Ubuntu package situation. Will they ever update any of the packages?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:45 UTC</span>

<span style="font-size: 90%;">Thanks for letting us know _@Paul Beckett_</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:37 UTC</span>

<span style="font-size: 90%;">yes, the security team told me at last in the next release will contain the upgraded versions - but not with the newer versions, I have to add the necessary patches to the packages (CRS 3.3.4 and libmodsecurity3 3.0.9)</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:03 UTC</span>

<span style="font-size: 90%;">in the development release (and in the testing) the new packages are there</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:13 UTC</span>

<span style="font-size: 90%;">3.3.5 and 3.0.10</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:32 UTC</span>

<span style="font-size: 90%;">it's Debian, I do not know anything about Ubuntu :neutral_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:34 UTC</span>

<span style="font-size: 90%;">What about CRS?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:53 UTC</span>

<span style="font-size: 90%;">Ubuntu adopts the Debian packages AFAIK in this area.</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:03 UTC</span>

<span style="font-size: 90%;">yes, but I don't know about the latency</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:26 UTC</span>

<span style="font-size: 90%;">yes they fork testing for their new release, but I don’t know if they will backport it as a security release</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:36 UTC</span>

<span style="font-size: 90%;">I think probably not unless they are actively alerted to it</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:59 UTC</span>

<span style="font-size: 90%;">I don’t even know if modsecurity is in their ‘supported’ packages which they backport for</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:11 UTC</span>

<span style="font-size: 90%;">What about CRS? - as I wrote, CRS 3.3.5 is part of Debian SID, and security team told me in next stable releases (12.2 and 11.10 (I guess)) will contain the patched 3.3.4</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:26 UTC</span>

<span style="font-size: 90%;">they only do security errata for old Ubuntu versions for a small subset of packages</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:30 UTC</span>

<span style="font-size: 90%;">Thanks (and sorry overlooked that line)</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:35 UTC</span>

<span style="font-size: 90%;">np</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:12 UTC</span>

<span style="font-size: 90%;">Then we have opened the subscription for the dev retreat. See link in agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:32 UTC</span>

<span style="font-size: 90%;">There are a couple of guests we are inviting, also the sponsors but no news from them so far.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:43 UTC</span>

<span style="font-size: 90%;">I don’t know if I will be well enough to attend :cry: guess it will be a last minute decision</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:59 UTC</span>

<span style="font-size: 90%;">As shared on the dev channel earlier today, we want devs to make a statement about their contributions to the project. This follows a discussion at the retreat last year. There are no formal minimal requirements, but we want you to think about it and write something you have done for the project.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:15 UTC</span>

<span style="font-size: 90%;">Also: If you think you do not qualify so far, there are still a couple of months to contribute ...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:14 UTC</span>

<span style="font-size: 90%;">Do you all understand the reasoning, or do you think we need to discuss this?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:57 UTC</span>

<span style="font-size: 90%;">I remember the group discussion. It makes sense.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:46:03 UTC</span>

<span style="font-size: 90%;">I think it’s clear</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:25 UTC</span>

<span style="font-size: 90%;">Thank you for your understanding.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:40 UTC</span>

<span style="font-size: 90%;">DM is also an option, just in case.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:07 UTC</span>

<span style="font-size: 90%;">The status of the sub projects is in the agenda. We have news from all the areas with the exception of the container, but development is active in that area too - based on the PRs being committed.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:18 UTC</span>

<span style="font-size: 90%;">Any questions on the status?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:06 UTC</span>

<span style="font-size: 90%;">That does not seem to be the case. So let's move on.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:13 UTC</span>

<span style="font-size: 90%;">There are a couple of discussions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:49 UTC</span>

<span style="font-size: 90%;">One open question is the status of CRS 3.2.x. We stated that we would rather not backport the stuff we added to 3.3.x.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:13 UTC</span>

<span style="font-size: 90%;">The question is now if we still want to do that for 3.2, or if we want to declare 3.2 as legacy.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:50:18 UTC</span>

<span style="font-size: 90%;">Hello</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:23 UTC</span>

<span style="font-size: 90%;">is there any reason why not? Would it be too hard work?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:14 UTC</span>

<span style="font-size: 90%;">More boring than hard, but somebody has to do the work and volunteers are scarce in this regard.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:35 UTC</span>

<span style="font-size: 90%;">A sponsor specifically asked for 3.2 backports, though. So there is definitely interest.</span>

**airween** <span style="color: grey; font-size: 90%;">18:51:57 UTC</span>

<span style="font-size: 90%;">yes, I thought about CVE affected rules at least</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:52:12 UTC</span>

<span style="font-size: 90%;">If any sponsor asked for it, we should do it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:14 UTC</span>

<span style="font-size: 90%;">I also don’t want to support 3.2, but I would want to set a policy for that first, as a courtesy to enterprise users. So, if we’d say we drop support for it, we should announce this change in advance (let’s say 6 months) and I’m afraid we should backport until that pre-announced day comes.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:53 UTC</span>

<span style="font-size: 90%;">(And we could still deviate from it if a sponsor asks. Microsoft even issued patches for Windows XP for really serious issues, years after EOL date)</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:31 UTC</span>

<span style="font-size: 90%;">on dev channel I noticed you guys that I work on a new tool which makes a comparison between versions. With that I can make the necessary modifications, I guess</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">_@walter_ a policy would be fine!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:12 UTC</span>

<span style="font-size: 90%;">I would second a policy as well. And a clear roadmap.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:38 UTC</span>

<span style="font-size: 90%;">We do already have a policy, but no roadmap</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">I guess what we're suggesting is to change the policy</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:56 UTC</span>

<span style="font-size: 90%;">(Personally, I also think we should aim for a strict release cycle after 4.0 comes out. Like every 6 or 9 or 12 months and then backports for 2 former releases or so.)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:51 UTC</span>

<span style="font-size: 90%;">But let's discuss that at the retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">So do we do a backport and release 3.2.x?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:32 UTC</span>

<span style="font-size: 90%;">I mean we managed 3.3, so the release itself is doable.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:05 UTC</span>

<span style="font-size: 90%;">It took a week, and at least 3 people to accomplish :sweat_smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:19 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ Was a release hero</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:23 UTC</span>

<span style="font-size: 90%;">We need more training.:)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:24 UTC</span>

<span style="font-size: 90%;">Backporting to 3.2 will be way worse</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:52 UTC</span>

<span style="font-size: 90%;">Hasn't been touched in years</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:53 UTC</span>

<span style="font-size: 90%;">Why is it worse? The diff is not so big in this area or am I wrong?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:06 UTC</span>

<span style="font-size: 90%;">No auto-linting, no go-ftw compatibility for 3.3</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:08 UTC</span>

<span style="font-size: 90%;">I think</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:17 UTC</span>

<span style="font-size: 90%;">yeah basically a cross your fingers appraoch..</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:28 UTC</span>

<span style="font-size: 90%;">which is manageable for small patches</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:31 UTC</span>

<span style="font-size: 90%;">just annoying</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:45 UTC</span>

<span style="font-size: 90%;">Yes, certainly by hand. That's troubling, I agree.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:58:58 UTC</span>

<span style="font-size: 90%;">The question is… what are we going to Backbort?
Just rule fixes/changes and cve‘s?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:13 UTC</span>

<span style="font-size: 90%;">Same as v3.3 I guess.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:46 UTC</span>

<span style="font-size: 90%;">No tests</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:59:50 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:00:45 UTC</span>

<span style="font-size: 90%;">So no new rules… just changed rules. And the question is what is with the regex assembly stuff?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:33 UTC</span>

<span style="font-size: 90%;">Why would we change additional regexes? It's only a bugfix / security release after all?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:02:38 UTC</span>

<span style="font-size: 90%;">Ok, so we focus just on security fixes and bugfixes.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:03 UTC</span>

<span style="font-size: 90%;">At least this is what I think would be useful (and in line with the 3.3 release)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:09 UTC</span>

<span style="font-size: 90%;">For context, this was the full 3.3.5 change list:
</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:03:25 UTC</span>

<span style="font-size: 90%;">Well, I will take a look at 3.2. maybe I will do the backport.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:26 UTC</span>

<span style="font-size: 90%;">Maybe you could only do the CVE and PL scoring bug, ignore everything else.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:39 UTC</span>

<span style="font-size: 90%;">(And sponsors list, easy update.)</span>

**airween** <span style="color: grey; font-size: 90%;">19:03:41 UTC</span>

<span style="font-size: 90%;">I would focused only the CVE fix</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:46 UTC</span>

<span style="font-size: 90%;">yep make it really minimal</span>

**airween** <span style="color: grey; font-size: 90%;">19:03:51 UTC</span>

<span style="font-size: 90%;">and yes, there are some PL fix</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:45 UTC</span>

<span style="font-size: 90%;">Thanks for volunteering _@emphazer_. Is there a timeframe you can commit to if you do it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:57 UTC</span>

<span style="font-size: 90%;">There are a couple of people to support you know, I guess.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:59 UTC</span>

<span style="font-size: 90%;">Oh yeah, that's a good point: 3.2 is already missing some extra PL scoring fixes that 3.3 already had. Hmm.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:06:54 UTC</span>

<span style="font-size: 90%;">I think I sent a PR to 3.2 too, and it merged - but was not released</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:05:10 UTC</span>

<span style="font-size: 90%;">3.3.4 and 3.3.3 fixed some scoring bugs, IIRC.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:20 UTC</span>

<span style="font-size: 90%;">That is relatively easy to do, I think.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:05:42 UTC</span>

<span style="font-size: 90%;">I will give you a response until next week.
</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:06:45 UTC</span>

<span style="font-size: 90%;">But I’m pretty sure I will do it… 
</span>

**airween** <span style="color: grey; font-size: 90%;">19:06:54 UTC</span>

<span style="font-size: 90%;">I think I sent a PR to 3.2 too, and it merged - but was not released</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:06:54 UTC</span>

<span style="font-size: 90%;">I think I sent a PR to 3.2 too, and it merged - but was not released</span>

**airween** <span style="color: grey; font-size: 90%;">19:07:39 UTC</span>

<span style="font-size: 90%;">now I took a quick look to 3.2 with rules_check.py script, and the PL scores seems correct</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:53 UTC</span>

<span style="font-size: 90%;">Very good news.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:01 UTC</span>

<span style="font-size: 90%;">Let's move on then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:17 UTC</span>

<span style="font-size: 90%;">After removing the stale-issue-bot, we agreed to review the situation every six month. We have the numbers in the agenda. Things look stable (contrary to my gloomy predicitions :sunglasses:) so I think we can keep it as is. What do you think?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:49 UTC</span>

<span style="font-size: 90%;">It would be good to see issues going down</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:56 UTC</span>

<span style="font-size: 90%;">Things haven't gotten better, which was the hope.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:17 UTC</span>

<span style="font-size: 90%;">I wondered what the numbers would be if the stale issues had auto-closed, but I don't know how to easily get those numbers.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:25 UTC</span>

<span style="font-size: 90%;">You really expected the issues to go down when we remove the stale-issue-bot?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:29 UTC</span>

<span style="font-size: 90%;">Maybe there's some github magic.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">Microsoft fixes the issues in the background... :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:40 UTC</span>

<span style="font-size: 90%;">We were down to 22 or so before the bug bounty hit.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">The change was sold as 'let's turn off auto-closure and then we actively close stuff'</span>

**airween** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">Microsoft fixes the issues in the background... :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">Microsoft fixes the issues in the background... :smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:07 UTC</span>

<span style="font-size: 90%;">But it never really took off.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:23 UTC</span>

<span style="font-size: 90%;">But things haven't gotten worse.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:12 UTC</span>

<span style="font-size: 90%;">Auto-closure is automatic. If we want to actively close things then we need that work to happen.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:21 UTC</span>

<span style="font-size: 90%;">Automatic is good :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:53 UTC</span>

<span style="font-size: 90%;">Actively closing is a hard. I suggest we leave the policy as is and brainstorm about a plan during the retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:23 UTC</span>

<span style="font-size: 90%;">I forgot something from the communication department during the status: Alessandro will give us a proposal how to go about renaming our project during August so we can take a decision at the September meeting.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:18 UTC</span>

<span style="font-size: 90%;">Excellent</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:05 UTC</span>

<span style="font-size: 90%;">Next item on the agenda: Max has a draft PR ready. It's one of the final wordlist PRs. He is asking for feedback at [#3276](https://github.com/coreruleset/coreruleset/issues/#3276).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:11 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3276](https://github.com/coreruleset/coreruleset/pull/3276)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:50 UTC</span>

<span style="font-size: 90%;">I do not think we can discuss it here without him, but we could do with 2 people promising to take a look tomorrow and provide feedback, so Max can finalize his PR.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:21:13 UTC</span>

<span style="font-size: 90%;">I can have alook at it and add some feedback tomorrow.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:19 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:10 UTC</span>

<span style="font-size: 90%;">Any other volunteer?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:26:38 UTC</span>

<span style="font-size: 90%;">Is it okay if I provide feedback the day after tomorrow?</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:28:21 UTC</span>

<span style="font-size: 90%;">Certainly. It's probably best if you add a comment now that you are actively reviewing. Max is not in the meeting, so he will learn you are working on this. Thanks for volunteering.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">The PR seems interesting as it's related to Unix/Linux. I'll love to help. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:54 UTC</span>

<span style="font-size: 90%;">Well it seems the PR is a bit too intimidating. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:07 UTC</span>

<span style="font-size: 90%;">Next one: [https://github.com/coreruleset/coreruleset/pull/3273](https://github.com/coreruleset/coreruleset/pull/3273)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:46 UTC</span>

<span style="font-size: 90%;">Also wordlist updates. And here it's 4 rules in one. _@Matteo Pace_ is mostly done, I provided some feedback. Next step is either more feedback for finalizing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:53 UTC</span>

<span style="font-size: 90%;">What is your plan _@Matteo Pace_?</span>

**jit** <span style="color: grey; font-size: 90%;">19:26:38 UTC</span>

<span style="font-size: 90%;">Is it okay if I provide feedback the day after tomorrow?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:26:38 UTC</span>

<span style="font-size: 90%;">Is it okay if I provide feedback the day after tomorrow?</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:28:21 UTC</span>

<span style="font-size: 90%;">Certainly. It's probably best if you add a comment now that you are actively reviewing. Max is not in the meeting, so he will learn you are working on this. Thanks for volunteering.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">The PR seems interesting as it's related to Unix/Linux. I'll love to help. :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:28:33 UTC</span>

<span style="font-size: 90%;">My last comment should recap the situation and list all the open questions. I wish to close it by this week, any feedback even just about specific bullet points is very welcomed</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:29:43 UTC</span>

<span style="font-size: 90%;">I can also elaborate here each point, if we want to sort things out right now</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:16 UTC</span>

<span style="font-size: 90%;">I'll definitely provide feedback. Tomorrow or so.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:34:30 UTC</span>

<span style="font-size: 90%;">Many thanks Christian</span>

**jit** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">The PR seems interesting as it's related to Unix/Linux. I'll love to help. :slightly_smiling_face:</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:26:38 UTC</span>

<span style="font-size: 90%;">Is it okay if I provide feedback the day after tomorrow?</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:28:21 UTC</span>

<span style="font-size: 90%;">Certainly. It's probably best if you add a comment now that you are actively reviewing. Max is not in the meeting, so he will learn you are working on this. Thanks for volunteering.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">The PR seems interesting as it's related to Unix/Linux. I'll love to help. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:15 UTC</span>

<span style="font-size: 90%;">I'd rather not walk through this rule group here again ( we did so before). I think we should be able to finish this ourselves. But if somebody wants to chime in, let's say you start finalizing on Thu and we try to merge until Sunday. OK?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:33:13 UTC</span>

<span style="font-size: 90%;">Sounds good, let’s try!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:25 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:52 UTC</span>

<span style="font-size: 90%;">We're getting close to the end now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:04 UTC</span>

<span style="font-size: 90%;">There is a contributor who is asking to move a rule to PL2.
[https://github.com/coreruleset/coreruleset/issues/3272](https://github.com/coreruleset/coreruleset/issues/3272)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:55 UTC</span>

<span style="font-size: 90%;">The point is that "information_schema" triggered an FP. And he's correct that information_schema may appear in technical documents without being an SQLi.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:39 UTC</span>

<span style="font-size: 90%;">The word is already surrounded by word-boundaries. Does anybody see a way to make 942140 less prone to this or related FPs?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:56 UTC</span>

<span style="font-size: 90%;">Surely this is a case for a rule exclusion</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:07 UTC</span>

<span style="font-size: 90%;">Or do we call it a day and accept the problem as long as not too many user bump into this at PL1?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:12 UTC</span>

<span style="font-size: 90%;">The pattern information_schema\b cannot reasonably be assumed to occur in natural language</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:36 UTC</span>

<span style="font-size: 90%;">Without the underscore then maybe, as those are a pair of English words</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:40 UTC</span>

<span style="font-size: 90%;">But as a whole thing?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">It can in response body, if it's a blog post.\</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:41:05 UTC</span>

<span style="font-size: 90%;">I think this is a request rule</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:52:42 UTC</span>

<span style="font-size: 90%;">You're right. It's a request rule for a Java vuln</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:53:33 UTC</span>

<span style="font-size: 90%;">Same issue, though: if you're submitting a blog post to e.g. WordPress then the same problem presents itself, in a request body.</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">Only in MySQL tutorials. But if you’re writing SQL tutorials in a CMS you’ll hit so many rules. The solution is a plugin for the CMS.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">But if you talk about technicalities such as tables, then it may appear, don't you think? That's also the use case the user reported.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:50 UTC</span>

<span style="font-size: 90%;">For the record: The Japanese payload translates to jupiter's information_schema system table permissions</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:54 UTC</span>

<span style="font-size: 90%;">But with the underscore? Surely that would be written as "information schema" in a technical document</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:00 UTC</span>

<span style="font-size: 90%;">So we are in an SQL context I guess.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:23 UTC</span>

<span style="font-size: 90%;">Ah, I see, they were describing SQL things.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">That makes more sense.</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:43 UTC</span>

<span style="font-size: 90%;">I think it’s reasonable to block it, it’s an edge case but teeters to the side of block imho.</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:12 UTC</span>

<span style="font-size: 90%;">It’s our eternal curse to have to make these decisions and make 40% of the people unhappy.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:20 UTC</span>

<span style="font-size: 90%;">It sounds like a free text field where someone is discussing SQL functions. That will set off many rules anyway. Rule exclusions required.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:33 UTC</span>

<span style="font-size: 90%;">So we stay at PL1, I guess?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:43 UTC</span>

<span style="font-size: 90%;">(It's a shame the user can't provide more info, but it sounds like it is a free text field.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:06 UTC</span>

<span style="font-size: 90%;">I'm pretty sure of that.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:43:19 UTC</span>

<span style="font-size: 90%;">Can we reply to the user with a rule exclusion? To provide at least some solution.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:43:56 UTC</span>

<span style="font-size: 90%;">I can write it if a user provides all needed info.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:12 UTC</span>

<span style="font-size: 90%;">Ah, yes, good point. The report was very light on info.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:22 UTC</span>

<span style="font-size: 90%;">Hard to give a full answer.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:50 UTC</span>

<span style="font-size: 90%;">We do not have all the infos to write an RE, but _@azurIt_ already offered his support. I think we are good and we only have to share our position on the proposed PL change.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">Final item.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:37 UTC</span>

<span style="font-size: 90%;">The closed issue 3266 warrants more detailed discussion.
[https://github.com/coreruleset/coreruleset/issues/3266](https://github.com/coreruleset/coreruleset/issues/3266)
_@Matteo Pace_ could you provide a quick summary of the problem and how it affects us?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:50:25 UTC</span>

<span style="font-size: 90%;">The reported issue is a false positive (rule 950140, response body), with very little information (no engine details nor the payload).
The user (same guy of the previous issue) was expecting that only the first line was matched, but it is not the case (any new line in matched, not only the first).

The problem seems to be broader, about multiline flag enabled by default by some engines (libmodsec and Coraza) and not by others ModSec v2.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:51:17 UTC</span>

<span style="font-size: 90%;">We need to fix lots of rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:21 UTC</span>

<span style="font-size: 90%;">So we have different behavior depending on the engine in use? I think we have not been aware of this so far.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:52 UTC</span>

<span style="font-size: 90%;">Can you give an example of the / a payload that triggers on one engine, but not on the other one?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:54:19 UTC</span>

<span style="font-size: 90%;">Rule:
SecRule RESPONSE_BODY "@rx ^}" "....

Response body returned:
{
  "origin": "192.168.48.1",
  "url": "[http://localhost/anything](http://localhost/anything)"
} 
Modsec v2: does not trigger the rule
ModSec v3 and Coraza: trigger the rule</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:54:33 UTC</span>

<span style="font-size: 90%;">For the 950140 , this should trigger it on modsec v3 but not on modsec v2: anything\n#!/</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:47 UTC</span>

<span style="font-size: 90%;">_@azurIt_ you think it affects many rules. How many are we talking about?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:13 UTC</span>

<span style="font-size: 90%;">Anything that carries a ^ or $?</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:56:36 UTC</span>

<span style="font-size: 90%;">Probably yes.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:57:36 UTC</span>

<span style="font-size: 90%;">Possible fix is using (?-m) , for example for 950140 : SecRule RESPONSE_BODY "@rx (?-m)^#\!\s?/" \</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:00:13 UTC</span>

<span style="font-size: 90%;">By the way, it should improve performance for v3 and Coraza.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:48 UTC</span>

<span style="font-size: 90%;">Good thinking.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:57:50 UTC</span>

<span style="font-size: 90%;">Should be safe to use for both v2 and v3.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:36 UTC</span>

<span style="font-size: 90%;">_@Matteo Pace_ Do you know why Coraza behaves as this? If it's just a random default behavior, do you think it can be changed?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">It can be changed Coraza side, we explicitly turned multiline on to align Coraza to ModSec (There was a failing CRS test that seemed to require it)
more context: [https://github.com/corazawaf/coraza/pull/732](https://github.com/corazawaf/coraza/pull/732)</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:01:52 UTC</span>

<span style="font-size: 90%;">Do we know which test?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:05:06 UTC</span>

<span style="font-size: 90%;">Do we know which test?Sorry _@azurIt_, I missed it. It was [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107) , indeed about New line bypass . But taking a look at some old notes, I was trying to fix it by adding (?s) . So it might be just a matter of dotall, not multiline  (dotall is enabled by default by both modsec v2 and v3)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:30:50 UTC</span>

<span style="font-size: 90%;">Speaking about Coraza and [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107), I confirm that keeping only dotall does not lead to regressions :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:49 UTC</span>

<span style="font-size: 90%;">_@airween_ Do you know about ModSec3?</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:33 UTC</span>

<span style="font-size: 90%;">no, I didn't know that behavior</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:26 UTC</span>

<span style="font-size: 90%;">now I checked the modsec issue, and the developer suggested a solution:

[https://github.com/SpiderLabs/ModSecurity/issues/2921#issuecomment-1611451302](https://github.com/SpiderLabs/ModSecurity/issues/2921#issuecomment-1611451302)</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:01:10 UTC</span>

<span style="font-size: 90%;">That solution is weird, i think using (?-m) is better.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">It can be changed Coraza side, we explicitly turned multiline on to align Coraza to ModSec (There was a failing CRS test that seemed to require it)
more context: [https://github.com/corazawaf/coraza/pull/732](https://github.com/corazawaf/coraza/pull/732)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">It can be changed Coraza side, we explicitly turned multiline on to align Coraza to ModSec (There was a failing CRS test that seemed to require it)
more context: [https://github.com/corazawaf/coraza/pull/732](https://github.com/corazawaf/coraza/pull/732)</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:01:52 UTC</span>

<span style="font-size: 90%;">Do we know which test?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:05:06 UTC</span>

<span style="font-size: 90%;">Do we know which test?Sorry _@azurIt_, I missed it. It was [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107) , indeed about New line bypass . But taking a look at some old notes, I was trying to fix it by adding (?s) . So it might be just a matter of dotall, not multiline  (dotall is enabled by default by both modsec v2 and v3)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:30:50 UTC</span>

<span style="font-size: 90%;">Speaking about Coraza and [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107), I confirm that keeping only dotall does not lead to regressions :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:20 UTC</span>

<span style="font-size: 90%;">This really the same issue (not only the same reporter)?</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:33 UTC</span>

<span style="font-size: 90%;">yes, he is the same</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:42 UTC</span>

<span style="font-size: 90%;">But is it the same issue?</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:59 UTC</span>

<span style="font-size: 90%;">well, more-or-less...</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:27 UTC</span>

<span style="font-size: 90%;">_@azurIt_ we can check the solutions with [msc_retest](https://github.com/digitalwave/msc_retest) :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:59 UTC</span>

<span style="font-size: 90%;">So what do you all think we should do here?</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:08 UTC</span>

<span style="font-size: 90%;">actually I do not have any idea. I think we should take a look both issues and suggested solutions (including _@azurIt_'s (?-m) (performance, compatibility, etc...))</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:06:03 UTC</span>

<span style="font-size: 90%;">Disabling multiline should improve performance for v3 and Coraza.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:06:50 UTC</span>

<span style="font-size: 90%;">Not sure what it will do for v2, probably nothing but it needs to be tested.</span>

**airween** <span style="color: grey; font-size: 90%;">20:07:21 UTC</span>

<span style="font-size: 90%;">yes, tests needed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:35 UTC</span>

<span style="font-size: 90%;">I propose the following:
* We create an issue with the minimal description by Matteo and the example payloads the the link to ModSec and the proposed solution by _@azurIt_
* We try to work with the engine devs and bring their behavior inline with our reference platform
* If that fails we try to find a solution in our regexes. _@azurIt_'s proposal springs to mind.
I'd prefer not to postpone CRSv4 over this, but I guess this is something we could also fix during a RC period.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:57 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:51 UTC</span>

<span style="font-size: 90%;">Thanks for your approval. _@Matteo Pace_ would you be so kind and create the issue in question? Please add as much information and links as possible.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:13:00 UTC</span>

<span style="font-size: 90%;">Issue created here: [https://github.com/coreruleset/coreruleset/issues/3277](https://github.com/coreruleset/coreruleset/issues/3277)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:11:47 UTC</span>

<span style="font-size: 90%;">Sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:51 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:19 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:49 UTC</span>

<span style="font-size: 90%;">I think there is no imminent need for an overall policy, but I am open for a discussion now or later.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:12:57 UTC</span>

<span style="font-size: 90%;">We should release first version of all existing plugins with v4.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:13:42 UTC</span>

<span style="font-size: 90%;">Well, of those which are tested (i.e. stable and production ready).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:03 UTC</span>

<span style="font-size: 90%;">That sounds good. Afterwards, I think plugins should have their own release rhythm. But we could add guidance for "how" to do a release.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:36 UTC</span>

<span style="font-size: 90%;">It's also a discussion we could have at the retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:25 UTC</span>

<span style="font-size: 90%;">So I guess it's time to close this. Thanks for attending everyone. And please do not forget to subscribe for the dev retreat at [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023)</span>

**jit** <span style="color: grey; font-size: 90%;">20:18:39 UTC</span>

<span style="font-size: 90%;">Good night everyone. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:51 UTC</span>

<span style="font-size: 90%;">good night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:52 UTC</span>

<span style="font-size: 90%;">Good night</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:18:52 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:18:57 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:19:09 UTC</span>

<span style="font-size: 90%;">See you around! Bye!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:19:13 UTC</span>

<span style="font-size: 90%;">Night</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:47 UTC</span>

<span style="font-size: 90%;">Bye!!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:05:06 UTC</span>

<span style="font-size: 90%;">Do we know which test?Sorry _@azurIt_, I missed it. It was [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107) , indeed about New line bypass . But taking a look at some old notes, I was trying to fix it by adding (?s) . So it might be just a matter of dotall, not multiline  (dotall is enabled by default by both modsec v2 and v3)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">It can be changed Coraza side, we explicitly turned multiline on to align Coraza to ModSec (There was a failing CRS test that seemed to require it)
more context: [https://github.com/corazawaf/coraza/pull/732](https://github.com/corazawaf/coraza/pull/732)</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:01:52 UTC</span>

<span style="font-size: 90%;">Do we know which test?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:05:06 UTC</span>

<span style="font-size: 90%;">Do we know which test?Sorry _@azurIt_, I missed it. It was [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107) , indeed about New line bypass . But taking a look at some old notes, I was trying to fix it by adding (?s) . So it might be just a matter of dotall, not multiline  (dotall is enabled by default by both modsec v2 and v3)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:30:50 UTC</span>

<span style="font-size: 90%;">Speaking about Coraza and [942522-7](https://github.com/coreruleset/coreruleset/blob/e36f27e1429a841e91996f4a521d40c996ec74eb/tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942522.yaml#L107), I confirm that keeping only dotall does not lead to regressions :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:13:00 UTC</span>

<span style="font-size: 90%;">Issue created here: [https://github.com/coreruleset/coreruleset/issues/3277](https://github.com/coreruleset/coreruleset/issues/3277)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:13:00 UTC</span>

<span style="font-size: 90%;">Issue created here: [https://github.com/coreruleset/coreruleset/issues/3277](https://github.com/coreruleset/coreruleset/issues/3277)</span>

