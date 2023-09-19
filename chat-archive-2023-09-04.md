### Mon, Sep 4th, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:30:51 UTC</span>

<span style="font-size: 90%;">Welcome everybody. It's CRS chat time. Please find our agenda at [https://github.com/coreruleset/coreruleset/issues/3279](https://github.com/coreruleset/coreruleset/issues/3279)</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:06 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:07 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:31:08 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:12 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:16 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:31:34 UTC</span>

<span style="font-size: 90%;">hello!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:41 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:31 UTC</span>

<span style="font-size: 90%;">Hi :wave:</span>

**JC** <span style="color: grey; font-size: 90%;">18:33:04 UTC</span>

<span style="font-size: 90%;">Hallo</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:52 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:05 UTC</span>

<span style="font-size: 90%;">Hey, hey, this looks nice. Great to see you all.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:34:18 UTC</span>

<span style="font-size: 90%;">Evening!</span>

**JC** <span style="color: grey; font-size: 90%;">18:34:29 UTC</span>

<span style="font-size: 90%;">Aloha</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:33 UTC</span>

<span style="font-size: 90%;">We're like a dozen people again.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:18 UTC</span>

<span style="font-size: 90%;">You may have seen there are 2 very interesting links in the agenda about bypasses of CRS. I think they are really worth a read. It would be interesting for us to scan such things systematically. But maybe that's something for after CRSv4. Like a job to process such papers and write abstracts and open issues in case. Boring work, so the project to source this from somebody for money.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:06 UTC</span>

<span style="font-size: 90%;">Then there was not overly interesting CVE against Coraza that has previously been solved with a security release. So no big deal, just mentioning it for the record.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">If we look at the rules part of our project, we're getting closer and closer to a release candidate, but things are really quite slow. This will be a topic afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:39 UTC</span>

<span style="font-size: 90%;">There is new movement in the documentation area. Which is helpful given we are approaching a release.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:25 UTC</span>

<span style="font-size: 90%;">The GSoC project has been finished successfully and chances are our student will join us at the dev retreat. Alessandro is currently interviewing him for a blog post about the performance measurement framework he developed for CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:18 UTC</span>

<span style="font-size: 90%;">I guess that's it as far as sub projects are concerned. Anything noteworthy that I missed?</span>

**JC** <span style="color: grey; font-size: 90%;">18:43:21 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:23 UTC</span>

<span style="font-size: 90%;">That does not seem to be the case.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:30 UTC</span>

<span style="font-size: 90%;">Good, then let's move to discussions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:56 UTC</span>

<span style="font-size: 90%;">Something that bugs me with the sandbox is the version supported. It will not react with an error message if a version is not covered.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:45:57 UTC</span>

<span style="font-size: 90%;">Why not creating an issue?</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">18:46:09 UTC</span>

<span style="font-size: 90%;">I did.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:31 UTC</span>

<span style="font-size: 90%;">It's also not quite clear which ones are really supported. Plus the feature to test against PRs is not documented. I have created an issue in the sandbox project.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:40 UTC</span>

<span style="font-size: 90%;">Is this a problem for you as well, or is this only me?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:18 UTC</span>

<span style="font-size: 90%;">I always test against nightly, but the suggested improvements are good ideas.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:25 UTC</span>

<span style="font-size: 90%;">So the issue is there: [https://github.com/coreruleset/crs-sandbox/issues/67](https://github.com/coreruleset/crs-sandbox/issues/67)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:41 UTC</span>

<span style="font-size: 90%;">I am just wondering if this gains any support and how important it really is.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:46:58 UTC</span>

<span style="font-size: 90%;">Is this a private issue</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:47:24 UTC</span>

<span style="font-size: 90%;">Private repo</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">18:47:35 UTC</span>

<span style="font-size: 90%;">Ah, yes. Sorry, forgot about that.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:47:01 UTC</span>

<span style="font-size: 90%;">I think it's a good idea</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:01 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ is this something you would want to implement?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:47:35 UTC</span>

<span style="font-size: 90%;">yes, and a validation on the version header sounds also legit</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:47:50 UTC</span>

<span style="font-size: 90%;">I self assign it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:57 UTC</span>

<span style="font-size: 90%;">Cool. Do you have time for this in the next few weeks?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:04 UTC</span>

<span style="font-size: 90%;">Then we have issue [#3288](https://github.com/coreruleset/coreruleset/issues/#3288) on the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:05 UTC</span>

<span style="font-size: 90%;">_@xanadu_ could you explain the problem?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:51:07 UTC</span>

<span style="font-size: 90%;">Sorry, I was playing with the sandbox.....</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:51:27 UTC</span>

<span style="font-size: 90%;">Um, yes: some plain English words in a Unix command list are causing FPs.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:51:45 UTC</span>

<span style="font-size: 90%;">e.g.
curl [https://sandbox.coreruleset.org/?word=strings](https://sandbox.coreruleset.org/?word=strings)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:52:13 UTC</span>

<span style="font-size: 90%;">Or the reporter's example:
curl [https://sandbox.coreruleset.org/events?sortBy=scheduledAt](https://sandbox.coreruleset.org/events?sortBy=scheduledAt)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:52:23 UTC</span>

<span style="font-size: 90%;">Because "sched" is being caught, so "scheduled" is causing an FP.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:52:50 UTC</span>

<span style="font-size: 90%;">Specifically, we are discussing rule 932260.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:25 UTC</span>

<span style="font-size: 90%;">So we have naked keyword causing FPs (-> strings). This sounds like a bug to me.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:42 UTC</span>

<span style="font-size: 90%;">The RA file in question is [https://github.com/coreruleset/coreruleset/blob/v4.0/dev/regex-assembly/932260.ra](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/regex-assembly/932260.ra)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:43 UTC</span>

<span style="font-size: 90%;">Also for context, this is at PL 1</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:50 UTC</span>

<span style="font-size: 90%;">Such false positives at a higher PL would be acceptable, perhaps.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:26 UTC</span>

<span style="font-size: 90%;">We probably need to start running that through English word detection as well....</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:00 UTC</span>

<span style="font-size: 90%;">Probably, yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:35 UTC</span>

<span style="font-size: 90%;">There's already a list of manual exclusions to which we can add those words</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:43 UTC</span>

<span style="font-size: 90%;">But the rule also covers `unix-shell-fps`. It seems the keywords in question are simply not part of that list. Or what's the matter here.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:20 UTC</span>

<span style="font-size: 90%;">Yes, they are not in the list because the list is maintained manually</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:19 UTC</span>

<span style="font-size: 90%;">Got you. So what do you propose? Extending the FP list, or running through the dictionary?
Also: For things added to the list / removed via dictionary: Do we want to bring them back at a higher PL?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:56 UTC</span>

<span style="font-size: 90%;">Extending the list with generated entries.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:23 UTC</span>

<span style="font-size: 90%;">They would return automatically (I have a change in a PR), because there are multiple lists for different PLs</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:52 UTC</span>

<span style="font-size: 90%;">OK.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:59:01 UTC</span>

<span style="font-size: 90%;">Ah, this?
#  .932236 (stricter sibling… PL2… - no excluded words)</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:00:08 UTC</span>

<span style="font-size: 90%;">This one also causes a lot of FPs, atleast in WordPress.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:59:03 UTC</span>

<span style="font-size: 90%;">I guess would cover the excluded words.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:59:41 UTC</span>

<span style="font-size: 90%;">And 932237 at PL 3.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:49 UTC</span>

<span style="font-size: 90%;">Sounds cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:04 UTC</span>

<span style="font-size: 90%;">Anybody volunteering to do a PR along the lines proposed by _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:22 UTC</span>

<span style="font-size: 90%;">I'll leave a comment in the issue that a PR should wait for my PR to be merged first</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:00:38 UTC</span>

<span style="font-size: 90%;">please guys just make an effort to minimize FP being moved to PL2, particularly when dealing with values within the range [a-zA-Z0-9]</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:01:21 UTC</span>

<span style="font-size: 90%;">it's a pain when it happens, and the side effect is generating an impossible PL2</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:35 UTC</span>

<span style="font-size: 90%;">I think we really need a PR to fix 3288 before we do a PR...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:53 UTC</span>

<span style="font-size: 90%;">RC, I meant. Sorry.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:53 UTC</span>

<span style="font-size: 90%;">Ah, so 3276 will modify the same list files?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:24 UTC</span>

<span style="font-size: 90%;">Yes, the FP files will also contain some new entries</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:39 UTC</span>

<span style="font-size: 90%;">So, 3288 could already be partly solved?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:24 UTC</span>

<span style="font-size: 90%;">For 3288 we'll still need to add the scan for English words and the extension of the list</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:55 UTC</span>

<span style="font-size: 90%;">I can help with 3288 but I don't really understand the new Unix cmd rule set / construct with all the regexp assemble files. But if someone can review, I guess that could be ok.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:13 UTC</span>

<span style="font-size: 90%;">I'd be happy to review, if we get a PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:22 UTC</span>

<span style="font-size: 90%;">Thank you _@xanadu_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:13 UTC</span>

<span style="font-size: 90%;">Next item on the list: Let me copy from the agenda:
The complex of PRs and issues around curl[ and ](https://github.com/coreruleset/coreruleset/issues/3189)wget[ are matched in User-Agent header #3189](https://github.com/coreruleset/coreruleset/issues/3189), [fix: exclude well known user agents from unix commands #3190](https://github.com/coreruleset/coreruleset/pull/3190) and [feat: update word list for 932232 #3276](https://github.com/coreruleset/coreruleset/pull/3276).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:27 UTC</span>

<span style="font-size: 90%;">We have an issue and several overlapping PRs and I'm losing the overview a bit.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:02 UTC</span>

<span style="font-size: 90%;">The core of the problem is that we block UAs curland wget. Multiple rescue missions were launched, but none of them have been merged so far.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:17 UTC</span>

<span style="font-size: 90%;">_@maxleske_ What is the plan and how can we help?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:43 UTC</span>

<span style="font-size: 90%;">For the record: This seems to be the last real rule-related show-stopper for a CRSv4 release candidate.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:06 UTC</span>

<span style="font-size: 90%;">Someone needs to create a PR for the latest proposal, which is to use include-except. The exceptions would currently only be curl and wget and we would split the current rule in two, handling the User-Agent header separately.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:26 UTC</span>

<span style="font-size: 90%;">My original PR can probably be closed.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:40 UTC</span>

<span style="font-size: 90%;">As _@theMiddle_ has pointed out, that approach is useless.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:51 UTC</span>

<span style="font-size: 90%;">Please be specific with issue and PR numbers.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:07 UTC</span>

<span style="font-size: 90%;">You want to close 3190, don't you?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:29 UTC</span>

<span style="font-size: 90%;">[#3190](https://github.com/coreruleset/coreruleset/issues/#3190) should probably be closed, yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:52 UTC</span>

<span style="font-size: 90%;">The rule is 932232</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:13 UTC</span>

<span style="font-size: 90%;">And 3189 has the proposal for a solution via include-except. You are now asking for a PR in this regard, so you have time to fix 3276 that has been mentioned before. Am I getting this right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:12 UTC</span>

<span style="font-size: 90%;">Yes, I'm working on it (although I should have been finished weeks ago)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:37 UTC</span>

<span style="font-size: 90%;">Do we have volunteers to create the include-except PR?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:12:47 UTC</span>

<span style="font-size: 90%;">I can do that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:56 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:58 UTC</span>

<span style="font-size: 90%;">Thank you _@franbuehler_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:19 UTC</span>

<span style="font-size: 90%;">Ping me if you have questions</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:14:23 UTC</span>

<span style="font-size: 90%;">Thank you. Yes, I'll do.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:34 UTC</span>

<span style="font-size: 90%;">Now with regards to 3276, is there anything we can do to support you _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:51 UTC</span>

<span style="font-size: 90%;">No. I just need to clean up the PR and get my act together.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:09 UTC</span>

<span style="font-size: 90%;">Feet massage? Free meals? Booze?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:21 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:57 UTC</span>

<span style="font-size: 90%;">Nah. A shot of that Hungarian liquor in November would be nice :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:12 UTC</span>

<span style="font-size: 90%;">We'll trust _@airween_ with that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:26 UTC</span>

<span style="font-size: 90%;">s/nice/dangerous</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:46 UTC</span>

<span style="font-size: 90%;">My point is a bit, that most of the hairy PRs implemented in the last 14 months or so are yours.</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:49 UTC</span>

<span style="font-size: 90%;">Hungarian liquor - what kind of liquor do you think? We have tons of it :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:02 UTC</span>

<span style="font-size: 90%;">The stuff from Varese</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:13 UTC</span>

<span style="font-size: 90%;">that's pálinka :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:18 UTC</span>

<span style="font-size: 90%;">Ah yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:33 UTC</span>

<span style="font-size: 90%;">I contributed to two rule overhauls and I feel that a lot boils down on you here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:52 UTC</span>

<span style="font-size: 90%;">Raising the pressure (and admittedly also the danger) ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:21 UTC</span>

<span style="font-size: 90%;">I think the danger exists only while the PRs haven't been merged. The logic itself isn't complicated.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:56 UTC</span>

<span style="font-size: 90%;">The PRs aren't too complicated either (I mean, look at the monster that Matteo's PR has become... :wink: )</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:05 UTC</span>

<span style="font-size: 90%;">It's more an energy issue at the moment</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:25 UTC</span>

<span style="font-size: 90%;">But I have 3 weeks of vacation now, so I should manage</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:39 UTC</span>

<span style="font-size: 90%;">Matteo's PR was relatively simple from my perspective. When compared to the crazy toolchain stuff. But maybe that's just me. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:20 UTC</span>

<span style="font-size: 90%;">I'm not surprised you are exhausted. The work is huge.
How much more work do you think is 3276?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:43 UTC</span>

<span style="font-size: 90%;">To finish? Maybe a day.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:59 UTC</span>

<span style="font-size: 90%;">~ 8 hours</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:25 UTC</span>

<span style="font-size: 90%;">That's substantial.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:37 UTC</span>

<span style="font-size: 90%;">Honestly, if you think there is anything you can offload, please speak up.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:43 UTC</span>

<span style="font-size: 90%;">Will do.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:58 UTC</span>

<span style="font-size: 90%;">OK. Thank you for volunteering once more.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:25 UTC</span>

<span style="font-size: 90%;">Which brings us to the dev retreat, I guess. (50min into the meeting, this is a fast one again. :slightly_smiling_face: )</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:14 UTC</span>

<span style="font-size: 90%;">So there is a separate channel at . The channel is private, but I think it's time to invite the participants. _@airween_, what do you think?</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:54 UTC</span>

<span style="font-size: 90%;">sure, we can invite other members (who wants to join)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:12 UTC</span>

<span style="font-size: 90%;">The big negotiations with hotel are done, so we can now shift the discussion to the topics of the retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:06 UTC</span>

<span style="font-size: 90%;">In previous years we set up a wiki page for everybody to contribute to and I think a retreat committee would then select the workshop topics. Or did everybody get to vote? I am no longer sure.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:24:42 UTC</span>

<span style="font-size: 90%;">I think last year's final list of topics and workshops was chosen by committee, IIRC.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:54 UTC</span>

<span style="font-size: 90%;">If you do not mind, I would prefer to repeat this. The advantage is that it can be discussed within a committee as long as it takes. If everybody is part of that discussion it can become very tiring.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:05 UTC</span>

<span style="font-size: 90%;">But feel free to volunteer into the committee.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:39 UTC</span>

<span style="font-size: 90%;">I think a lot depends on the CRSv4 release date. I would really love it to be before the retreat so we can start a new release cycle at the retreat!!!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:57 UTC</span>

<span style="font-size: 90%;">are sponsors giving us a track for topics?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:21 UTC</span>

<span style="font-size: 90%;">I wrote to all the sponsors, but none of them agreed to join, so I guess not.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:28:02 UTC</span>

<span style="font-size: 90%;">because they never tasted pàlinka</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:23 UTC</span>

<span style="font-size: 90%;">That is one way to look at it ... :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:40 UTC</span>

<span style="font-size: 90%;">don't miss the good food!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:03 UTC</span>

<span style="font-size: 90%;">Looking forward to some great Hungarian food!</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:33 UTC</span>

<span style="font-size: 90%;">I really hope you won't be disappointed :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:45 UTC</span>

<span style="font-size: 90%;">Anyways, I think it important that everybody thinks about potential topics for the dev retreat now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:55 UTC</span>

<span style="font-size: 90%;">_@airween_ can you prepare a wiki page please.</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:03 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:45 UTC</span>

<span style="font-size: 90%;">And there are already several proposals for stuff to do in Budapest. See [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">_@dune73_ You already set up a wiki page for ideas :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023-Topics](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2023-Topics)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:32 UTC</span>

<span style="font-size: 90%;">So far the preference was always historical museum over aqua park. If your taste has changed, please say so or indicate it in the wiki page next to the table with the proposals.</span>

**jit** <span style="color: grey; font-size: 90%;">19:32:04 UTC</span>

<span style="font-size: 90%;">History is cool</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:15 UTC</span>

<span style="font-size: 90%;">We'll see if we can repeat the 500g steak feat of Varese.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:36:15 UTC</span>

<span style="font-size: 90%;">there is a famous "restaurant" here, where the portions are extra huge:

[https://pleh-csarda.hu/galleria/](https://pleh-csarda.hu/galleria/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ missed that the last time, but she is making sure she can share this experience this time. :innocent:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:55 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ we went to a steak house on Friday, and they seriously had 500 - 800g steaks...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:07 UTC</span>

<span style="font-size: 90%;">Oh, wow! That's much too much!!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:27 UTC</span>

<span style="font-size: 90%;">For me too, but certain participants looked like in heaven. :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">And the giant bottle of wine! So tasty :wine_glass:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:51 UTC</span>

<span style="font-size: 90%;">That was good too. But I had to drive ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:09 UTC</span>

<span style="font-size: 90%;">This is winding down slowly. Is there anything else left to add for the dev retreat? Are there things we must not forget, things we need to plan far ahead?</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:15 UTC</span>

<span style="font-size: 90%;">there is a famous "restaurant" here, where the portions are extra huge:

[https://pleh-csarda.hu/galleria/](https://pleh-csarda.hu/galleria/)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:36:15 UTC</span>

<span style="font-size: 90%;">there is a famous "restaurant" here, where the portions are extra huge:

[https://pleh-csarda.hu/galleria/](https://pleh-csarda.hu/galleria/)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:37 UTC</span>

<span style="font-size: 90%;">I'll add topics to that list</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:55 UTC</span>

<span style="font-size: 90%;">Maybe we get a room with daylight this time? :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:14 UTC</span>

<span style="font-size: 90%;">What's daylight?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:30 UTC</span>

<span style="font-size: 90%;">We do.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:34 UTC</span>

<span style="font-size: 90%;">Give me a second.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:22 UTC</span>

<span style="font-size: 90%;">It's this one IIRC: [https://nadaspihenopark.hu/en/conference-venue/event-rooms/panorama-room/](https://nadaspihenopark.hu/en/conference-venue/event-rooms/panorama-room/)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:34 UTC</span>

<span style="font-size: 90%;">Nice</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:50 UTC</span>

<span style="font-size: 90%;">It can be divided, we have our own terrace and it has plenty of sunlight.</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:08 UTC</span>

<span style="font-size: 90%;">don't forget that Hungary is by the right border of its timezone, so in November the Sun rises early (before 7) but sets early too (about 5 PM)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:12 UTC</span>

<span style="font-size: 90%;">So we start work at 0700?</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:44 UTC</span>

<span style="font-size: 90%;">as I see the room has lights :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:08 UTC</span>

<span style="font-size: 90%;">Good. It sounded as if that was off limits with sunlight and all. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:20 UTC</span>

<span style="font-size: 90%;">If there is nothing else, I guess it's time to close the meeting.</span>

**jit** <span style="color: grey; font-size: 90%;">19:45:06 UTC</span>

<span style="font-size: 90%;">Goodnight everyone. :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:16 UTC</span>

<span style="font-size: 90%;">bye!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:45:20 UTC</span>

<span style="font-size: 90%;">Good night</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:22 UTC</span>

<span style="font-size: 90%;">Night night!</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:24 UTC</span>

<span style="font-size: 90%;">good night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:25 UTC</span>

<span style="font-size: 90%;">Good night!!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:27 UTC</span>

<span style="font-size: 90%;">Good night,</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:46:01 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:08 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3279#issuecomment-1705270068](https://github.com/coreruleset/coreruleset/issues/3279#issuecomment-1705270068)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:20 UTC</span>

<span style="font-size: 90%;">Thank you all for joining and _@franbuehler_ for the protocol!</span>

