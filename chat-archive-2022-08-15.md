### Mon, Aug 15th, 2022

**dune73** <span style="color: grey; font-size: 90%;">18:30:40 UTC</span>

<span style="font-size: 90%;">Hello, hello, it's CRS chat time. So who's around? And what's better to spend a Monday night with than CRS findings ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:21 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:23 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:54 UTC</span>

<span style="font-size: 90%;">Heyhoooo!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:10 UTC</span>

<span style="font-size: 90%;">Hello! I’m here, but I have to leave in about 30 minutes to my mother’s new care home cause there are problems with the tv that I installed, and she can’t sleep without it on :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:31 UTC</span>

<span style="font-size: 90%;">So let’s start with the most important things :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:57 UTC</span>

<span style="font-size: 90%;">Yes, so let's look at the bug bounty finding stats.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:34 UTC</span>

<span style="font-size: 90%;">I think we're at 33 open and 11 issue created.</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:01 UTC</span>

<span style="font-size: 90%;">That is already a good improvement! Slowly but we’re making progress!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:17 UTC</span>

<span style="font-size: 90%;">And 12 additional ones with PRs.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:34:25 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:37 UTC</span>

<span style="font-size: 90%;">Hey Paul!</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:53 UTC</span>

<span style="font-size: 90%;">Nice to see you</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:02 UTC</span>

<span style="font-size: 90%;">I think we're like 2/3 through and now we need to address the remaining ones.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:45 UTC</span>

<span style="font-size: 90%;">I attacked 3 hard ones last week and I think I was lucky to cover them in 1-2 hours. Well maybe 3, but we'll get there eventually. But it's real work.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:09 UTC</span>

<span style="font-size: 90%;">Proposal : Let's see what we can merge from the bug bounty right now then look into what we can do with the remaining ones.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:50 UTC</span>

<span style="font-size: 90%;">Here are the PRs tagged bug bounty.
[https://github.com/coreruleset/coreruleset/pulls?q=is%3Apr+is%3Aopen+label%3A%22bug+bounty%22](https://github.com/coreruleset/coreruleset/pulls?q=is%3Apr+is%3Aopen+label%3A%22bug+bounty%22)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:59 UTC</span>

<span style="font-size: 90%;">Apparently 4 additional ones must be there too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:25 UTC</span>

<span style="font-size: 90%;">[#2747](https://github.com/coreruleset/coreruleset/issues/#2747) is my PR to address the HTTP parameter pollution. _@xanadu_ reviewed with positive results.
I'm introducing a new rule at PL3 that denies some bypasses and there is a new rule at PL4 that forbids array parameter names (RE if you need them).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:29 UTC</span>

<span style="font-size: 90%;">Ready to merge?</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:51 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:01 UTC</span>

<span style="font-size: 90%;">I like it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:29 UTC</span>

<span style="font-size: 90%;">I’m always a bit scared about rules concerning foo[1] cause in PHP land this is very normal. But I think it won’t break a lot of applications.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:55 UTC</span>

<span style="font-size: 90%;">And, of course, people running at PL2+ can help themselves out of a situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:30 UTC</span>

<span style="font-size: 90%;">Exactly. At this PL, people need to be able to help themselves.</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:35 UTC</span>

<span style="font-size: 90%;">So I would say this is looking good!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:05 UTC</span>

<span style="font-size: 90%;">If we want to really allow it, there has got to be a complex multi-rule construct with more variables and that would mean a performance impact for everybody else. It's better this way, I am sure.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:31 UTC</span>

<span style="font-size: 90%;">So merge time? :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:40 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:47 UTC</span>

<span style="font-size: 90%;">Done! :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:58 UTC</span>

<span style="font-size: 90%;">Thank you for these nice new rules!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:22 UTC</span>

<span style="font-size: 90%;">You're welcome.

[#2730](https://github.com/coreruleset/coreruleset/issues/#2730) is an anti-XSS rule by @walter. No review yet. Do we have a volunteer?</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:10 UTC</span>

<span style="font-size: 90%;">I added REQUEST_FILENAME to a number of XSS rules that did not look too dangerous. But it has to be tested. But that can happen during the RC phase. I wouldn’t be surprised if, maybe, I have to revert one or two rules (or move them to a higher PL) because common filename patterns give FP.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:54 UTC</span>

<span style="font-size: 90%;">You tagged this as bug bounty, but then no bug bounty findings referenced. Does thi address something directly?</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:23 UTC</span>

<span style="font-size: 90%;">Oh sorry did I not reference it? It’s ULYKOFYK-1.</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:00 UTC</span>

<span style="font-size: 90%;">EOJQZ6XX also noted. I think those are duplicates.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:24 UTC</span>

<span style="font-size: 90%;">Cool. Please update.</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:43 UTC</span>

<span style="font-size: 90%;">done</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:05 UTC</span>

<span style="font-size: 90%;">Looks simple enough. There's at least one other change in there though (probably because you did ./regexp-assemble.py update --all)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:36 UTC</span>

<span style="font-size: 90%;">I can do a formal review without testing it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:51 UTC</span>

<span style="font-size: 90%;">Please do and let me know what I should fix!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:58 UTC</span>

<span style="font-size: 90%;">How did you come up with the list of rules to update? Did you look at the regexes and decide this could happen in REQUEST_FILENAME, bc it's not every XSS rules or is it?</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:46 UTC</span>

<span style="font-size: 90%;">I just went over the xss conf file. I added it to almost all of the rules, except the one that in my memory blew up and we moved that to PL2.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:23 UTC</span>

<span style="font-size: 90%;">Hey :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:28 UTC</span>

<span style="font-size: 90%;">OK, got you.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:29 UTC</span>

<span style="font-size: 90%;">It’s quite a big change. But I think there is no way to move forward than to just try it out, and revert where we’re being too strict.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:36 UTC</span>

<span style="font-size: 90%;">Hey _@fzipitria_, still in Europe?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:59 UTC</span>

<span style="font-size: 90%;">I agree with you _@walter_.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:01 UTC</span>

<span style="font-size: 90%;">Yes, I'm around still in CEST</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:11 UTC</span>

<span style="font-size: 90%;">Do we need a different review than the one by Max?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:36 UTC</span>

<span style="font-size: 90%;">You're still welcome to visit, you know (just not this week...)</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:40 UTC</span>

<span style="font-size: 90%;">It’s not very special but if you look at it visually it will be 5 minutes max</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:56 UTC</span>

<span style="font-size: 90%;">That means 30min without max.</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:34 UTC</span>

<span style="font-size: 90%;">I didn’t change anything about the regexps, or at least, I didn’t intend to - if I did, then that would be very nice to review :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:01 UTC</span>

<span style="font-size: 90%;">I can review it, if you need</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:05 UTC</span>

<span style="font-size: 90%;">Jokes aside, I think it makes sense visually. If Max can confirm the small regex change is OK, we're good to merge, I think. So I think we just assign Max and he can merge afterwards and then as Walter explained.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:14 UTC</span>

<span style="font-size: 90%;">Feel free to assign it to me</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:16 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:46 UTC</span>

<span style="font-size: 90%;">Good, next one.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:23 UTC</span>

<span style="font-size: 90%;">[#2595](https://github.com/coreruleset/coreruleset/issues/#2595) has been lingering a long time. It's not really working, checks failing and  _@xanadu_ thinks not even the exploit really works.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:37 UTC</span>

<span style="font-size: 90%;">I couldn't reproduce the original report/exploit.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">But, I'm not a Windows person, so I could be missing something obvious…</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:02 UTC</span>

<span style="font-size: 90%;">This was very strange, I couldn’t reproduce, could it be a sandbox problem?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:07 UTC</span>

<span style="font-size: 90%;">Intigriti was able to reproduce. I am a bit reluctant to discuss about the viability of a payload. The resources as perhaps better spent on the rules.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:56:17 UTC</span>

<span style="font-size: 90%;">Ohhhhh, I wonder: does Intigriti saying "we successfully reproduced" simply mean it passed through the sandbox?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:56:23 UTC</span>

<span style="font-size: 90%;">As opposed to actually testing on a Windows machine?</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:24 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">Well I think mostly yes. Although they did use their own machines also and performed requests. They did a little more than that.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:40 UTC</span>

<span style="font-size: 90%;">I think a Windows-person is needed here to verify or rule out the bypass. I can't take this issue any further, I don't think.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:02 UTC</span>

<span style="font-size: 90%;">Certainly, I couldn't make it work.</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:30 UTC</span>

<span style="font-size: 90%;">I think I can take a look at this issue, but I have very little time in the next 2-3 weeks… At the other hand, the issue is from May. Assign to me and accept a delay?</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:15 UTC</span>

<span style="font-size: 90%;">We SHOULD detect this also in the former release, so I really want to know what the h*ll is going on…</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:59:56 UTC</span>

<span style="font-size: 90%;">The "fix" is also very broken, IMO, as a note. I think the proposed regex pattern change breaks the regex.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:00:14 UTC</span>

<span style="font-size: 90%;">I can see the intention, I think, but the execution is wrong.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:00:42 UTC</span>

<span style="font-size: 90%;">Hi</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:43 UTC</span>

<span style="font-size: 90%;">Yes I saw that. Maybe the solution will look a little different. But maybe it’s also a false alarm due to the sandbox. Or a problem with shell quoting somewhere..</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:11 UTC</span>

<span style="font-size: 90%;">Proposal: We close the PR, we open an issue, explain the situation with reference to the closed PR and then we assign to _@walter_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:20 UTC</span>

<span style="font-size: 90%;">Hey, hey _@franbuehler_</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:28 UTC</span>

<span style="font-size: 90%;">Great!</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:32 UTC</span>

<span style="font-size: 90%;">Then I will dive into it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:46 UTC</span>

<span style="font-size: 90%;">Thank you. Can you execute as proposed?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:52 UTC</span>

<span style="font-size: 90%;">Issue and all, I mean?</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:03 UTC</span>

<span style="font-size: 90%;">Yes, let me do it quickly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:30 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:48 UTC</span>

<span style="font-size: 90%;">[#2591](https://github.com/coreruleset/coreruleset/issues/#2591) was covered two weeks ago, I think we can skip for tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:27 UTC</span>

<span style="font-size: 90%;">[#2581](https://github.com/coreruleset/coreruleset/issues/#2581) is under review by _@fzipitria_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:50 UTC</span>

<span style="font-size: 90%;">Anything we can do here, or all on good tracks and you merge once you've done the review?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:25 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ seems to be busy. Let's turn to [#2573](https://github.com/coreruleset/coreruleset/issues/#2573).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:13 UTC</span>

<span style="font-size: 90%;">_@maxleske_, if I get this right, after a long discussion there are only a few changes open that you requested during your review. Karel did not implement these, but afterwards it's ready to fly. Correct=</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:15 UTC</span>

<span style="font-size: 90%;">?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:53 UTC</span>

<span style="font-size: 90%;">yes, I think so</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:03 UTC</span>

<span style="font-size: 90%;">Do you want to ping Karel? I have his email, just in case. He's not very active on slack and may have overlooked GH.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:56 UTC</span>

<span style="font-size: 90%;">He used to be very responsive. I'll ping him.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:15 UTC</span>

<span style="font-size: 90%;">Please do. I'm sure he'll return his attention.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:58 UTC</span>

<span style="font-size: 90%;">[#2572](https://github.com/coreruleset/coreruleset/issues/#2572) is a similar situation. Here we have _@fzipitria_ assigned. Not entirely sure this is ready to be merged after a small change, but it looks good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:54 UTC</span>

<span style="font-size: 90%;">[#2562](https://github.com/coreruleset/coreruleset/issues/#2562) is a bit more complicated. _@xanadu_ has good arguments that suggest the PR is going into the wrong direction or is futile. So what do we do now? I do not really have an opinion, personally.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:21 UTC</span>

<span style="font-size: 90%;">The PR is complete, I think. But the PR does not address the original issue. Indeed, the original issue has been fixed and merged elsewhere.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:13:04 UTC</span>

<span style="font-size: 90%;">The question is, do we want a new rule and new crs-setup.conf variable to block archive files? Is there a compelling reason to do so? Does that cause lots of FPs? Or not?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:13:15 UTC</span>

<span style="font-size: 90%;">It feels like a new rule that we don't really need, maybe.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:13:51 UTC</span>

<span style="font-size: 90%;">There was an argument of "maybe you leave a tarball on your server containing config, setup files etc. and maybe an attacker downloads it". But is that a strong enough reason for a new rule?</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:28 UTC</span>

<span style="font-size: 90%;">I think in that case, the admin can just add the archive extensions to the forbidden extensions setting, right?</span>

**airween** <span style="color: grey; font-size: 90%;">19:14:35 UTC</span>

<span style="font-size: 90%;">we can offer to the rule maker that he can create a new plugin with this function, not a new rule</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:39 UTC</span>

<span style="font-size: 90%;">It feels a bit unnecessary to introduce a new mechanism for it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:50 UTC</span>

<span style="font-size: 90%;">Well technically it's the same as forbidding bak files, etc. Is not it?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:15:52 UTC</span>

<span style="font-size: 90%;">I think this fixes a non-existent problem for 99.9% of users. But maybe a comment with the list of archive files in the config file as an optional addition?</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:54 UTC</span>

<span style="font-size: 90%;">Yes, so we already offer that functionality. We could add an extra example line in the conf file for the restricted extensions to give people the idea.</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:09 UTC</span>

<span style="font-size: 90%;">Yes that was my proposal!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:10 UTC</span>

<span style="font-size: 90%;">It's just too bloody complicated for an edge case, that's why I think we should not merge. But existing extension list is somewhat arbitrary.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:35 UTC</span>

<span style="font-size: 90%;">Additional doc in crs-setup that explains the options would be a good idea, I agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:47 UTC</span>

<span style="font-size: 90%;">But we should not rely on the hacker to provide that anymore.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:50 UTC</span>

<span style="font-size: 90%;">Any takers?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:56 UTC</span>

<span style="font-size: 90%;">After this, I agree</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:17:03 UTC</span>

<span style="font-size: 90%;">I can make a new issue and a new PR.</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:15 UTC</span>

<span style="font-size: 90%;">ашесоме</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:16 UTC</span>

<span style="font-size: 90%;">ho</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:17 UTC</span>

<span style="font-size: 90%;">Many thanks _@xanadu_. Very helpful.</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:17 UTC</span>

<span style="font-size: 90%;">awesome</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:17:26 UTC</span>

<span style="font-size: 90%;">(I'll sort it tomorrow.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ there were two issues where we mentioned you above.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:41 UTC</span>

<span style="font-size: 90%;">[#2572](https://github.com/coreruleset/coreruleset/issues/#2572) is a similar situation. Here we have _@fzipitria_ assigned. Not entirely sure this is ready to be merged after a small change, but it looks good.</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:02 UTC</span>

<span style="font-size: 90%;">I have to run now! If you want to assign me something, especially PHP related, please feel free, but please don’t expect a very quick solution.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:04 UTC</span>

<span style="font-size: 90%;">And then "[#2581](https://github.com/coreruleset/coreruleset/issues/#2581) is under review by _@fzipitria_.
[9:03 PM] Anything we can do here, or all on good tracks and you merge once you've done the review?"</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:15 UTC</span>

<span style="font-size: 90%;">bye _@walter_, thank you for your support.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:20:24 UTC</span>

<span style="font-size: 90%;">Ok, I'll do it this week</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:09 UTC</span>

<span style="font-size: 90%;">Both?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:46 UTC</span>

<span style="font-size: 90%;">I'm behind in stuff, need to catch up</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:22 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:43 UTC</span>

<span style="font-size: 90%;">I am not sure we touched on all the bug bounty PRs now. Some address more than one finding. Is there something still open there?=</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:37 UTC</span>

<span style="font-size: 90%;">Looking over it once more, I think we're good. What we may want to do is cleaning up old and idle PRs that are not being finished. I might do a session with Andrea sooner or later, he started a few and left them unfinished.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:47 UTC</span>

<span style="font-size: 90%;">_@xanadu_, do you know what the issue was with [https://github.com/coreruleset/coreruleset/issues/2725](https://github.com/coreruleset/coreruleset/issues/2725)?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:25:18 UTC</span>

<span style="font-size: 90%;">PFK4711C?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:23 UTC</span>

<span style="font-size: 90%;">Why the complex regex instead of simply adding $SHELL and ${SHELL} to the list?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:31 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:26:05 UTC</span>

<span style="font-size: 90%;">Is that that PR?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:26:14 UTC</span>

<span style="font-size: 90%;">I just see ksh</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:07 UTC</span>

<span style="font-size: 90%;">Hm. Yes. It's mentioned in that issue. Just a sec</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:25 UTC</span>

<span style="font-size: 90%;">This one: [https://github.com/coreruleset/coreruleset/pull/2728](https://github.com/coreruleset/coreruleset/pull/2728)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:52 UTC</span>

<span style="font-size: 90%;">Ah, yes. Two issues</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:04 UTC</span>

<span style="font-size: 90%;">regexp-assemble seemed to output a regex that crashed Apache</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:46 UTC</span>

<span style="font-size: 90%;">Weird. Well ok :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:48 UTC</span>

<span style="font-size: 90%;">:shrug:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:53 UTC</span>

<span style="font-size: 90%;">The SHELL thing was something to do with evasions…</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:04 UTC</span>

<span style="font-size: 90%;">cmdline wasn't working with ${</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:07 UTC</span>

<span style="font-size: 90%;">Maybe that was it</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:35 UTC</span>

<span style="font-size: 90%;">I can dig through my notes and get back to you later</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:42 UTC</span>

<span style="font-size: 90%;">With a full answer :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:29:59 UTC</span>

<span style="font-size: 90%;">I think I see the problem. I would have liked a better explanation in the data file.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">If you have notes, that would be helpful</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:24 UTC</span>

<span style="font-size: 90%;">_@dune73_ we can move on</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:58 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:46 UTC</span>

<span style="font-size: 90%;">With some 30+ bug bounty issues still open and about a dozen, do we want to open issues for the remaining ones. Or is this too early and it will only blur the view?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">We accelerated a bit in early August with the virtual hackathon, but we have now slowed down again and I do not readily see how we can get rid of the remaining findings.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:45 UTC</span>

<span style="font-size: 90%;">Low hanging fruits are gone and what's open really is still open.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:51 UTC</span>

<span style="font-size: 90%;">I see, you do not have an easy answer either. Well...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:59 UTC</span>

<span style="font-size: 90%;">Let's turn to something else then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">_@xanadu_ confirmed what I have reported too. Sometimes, the sandbox reports alerts that do not exist in local installations. And that is actually quite frequent.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:44 UTC</span>

<span style="font-size: 90%;">I think some findings are still maybe invalid. 2 or 3</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:05 UTC</span>

<span style="font-size: 90%;">Yes, that may be the case, but we'll only find out when addressing them, I guess.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:11 UTC</span>

<span style="font-size: 90%;">But many issues require specialist knowledge I feel, like PHP or JS etc. to be able to understand the payload etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:25 UTC</span>

<span style="font-size: 90%;">I agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:45 UTC</span>

<span style="font-size: 90%;">Now in order to really understand the sandbox situation, I think we need to fire the entire test suite against the sandbox and record all the rules triggered by test, and then do the same against a local installation, record the alerts and then compare the two. They ought to be identical and if there is a diff, we need to address it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:09 UTC</span>

<span style="font-size: 90%;">Is there somebody interesting in performing such an exercise (bonus: This is not about the bug bounty)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:47 UTC</span>

<span style="font-size: 90%;">The sandbox supports different versions, right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:59 UTC</span>

<span style="font-size: 90%;">So that would have to be done multiple times?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:19 UTC</span>

<span style="font-size: 90%;">Once you have the script, that should be easy. And maybe it's isolated to one backend.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:34 UTC</span>

<span style="font-size: 90%;">I encountered the diff with nightly -> modsec 2.9/apache</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:45 UTC</span>

<span style="font-size: 90%;">I'll give it a try. Haven't used the sandbox yet.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:56 UTC</span>

<span style="font-size: 90%;">Thank you very much.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:22 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2750](https://github.com/coreruleset/coreruleset/issues/2750)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:41 UTC</span>

<span style="font-size: 90%;">_@xanadu_, _@dune73_ Please add anything useful there.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:54 UTC</span>

<span style="font-size: 90%;">Anybody has an issue he / she wants to discuss? Or something else. If not, I suggest to close this meeting.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:12 UTC</span>

<span style="font-size: 90%;">Yes: [https://github.com/coreruleset/coreruleset/issues/2719](https://github.com/coreruleset/coreruleset/issues/2719)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">I think we should close this as FP that user has to deal with.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:52 UTC</span>

<span style="font-size: 90%;">yes, I asked help for a BB issue, and still need it. I do not want to share here the documentation what I've made, but if somebody can help me, let me know</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:37 UTC</span>

<span style="font-size: 90%;">_@airween_: Please DM or share in dev channel.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:26 UTC</span>

<span style="font-size: 90%;">@max I did not look too close into this, but this is a can of worms and I think at PL2, it's probably acceptable to leave it as is and have the user deal with FPs. Everything else could be too complicated.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:31 UTC</span>

<span style="font-size: 90%;">That's my take and _@theMiddle_ seems to agree. I'll close the issue in that case.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:25 UTC</span>

<span style="font-size: 90%;">Just for the record, I also need a review from _@walter_ on [https://github.com/coreruleset/coreruleset/pull/2746#pullrequestreview-1072546843](https://github.com/coreruleset/coreruleset/pull/2746#pullrequestreview-1072546843). I need to merge that so I can enable the linter for regexp-assemble.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:44 UTC</span>

<span style="font-size: 90%;">If there is nothing else, then let's close.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:25 UTC</span>

<span style="font-size: 90%;">Good bye and thank you all for joining!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:40 UTC</span>

<span style="font-size: 90%;">Thanks, bye</span>

**airween** <span style="color: grey; font-size: 90%;">19:54:45 UTC</span>

<span style="font-size: 90%;">thanks, bye!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:54:45 UTC</span>

<span style="font-size: 90%;">Good night :wave:</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:54:56 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:55:05 UTC</span>

<span style="font-size: 90%;">Night!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:55:43 UTC</span>

<span style="font-size: 90%;">Good night</span>

