### Mon, Nov 4th, 2019

**dune73** <span style="color: grey; font-size: 90%;">19:31:28 UTC</span>

<span style="font-size: 90%;">Hello everyone. Great to have new guests: Hello Anna und Ruben!</span>

↳ **anna** <span style="color: grey; font-size: 90%;">19:31:58 UTC</span>

<span style="font-size: 90%;">hallo!</span>

**unknown user** <span style="color: grey; font-size: 90%;">19:31:37 UTC</span>

<span style="font-size: 90%;"></span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:27 UTC</span>

<span style="font-size: 90%;">guess it works</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:35 UTC</span>

<span style="font-size: 90%;">It seems we also have a webhook as a guest. Hello bot.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">19:32:37 UTC</span>

<span style="font-size: 90%;">Yup, works, sorry :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:59 UTC</span>

<span style="font-size: 90%;">No worries.</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:51 UTC</span>

<span style="font-size: 90%;">hi all</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:25 UTC</span>

<span style="font-size: 90%;">We're now lingering around 100 and plan to go further down.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:34:46 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ around?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">So shall we start (I'm happy to attend from Düsseldorf where I am teaching for 2 days. _@emphazer_: We could have gone to a bar together and now look where we both ended up...)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:04 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:10 UTC</span>

<span style="font-size: 90%;">Hi all!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:14 UTC</span>

<span style="font-size: 90%;">Hi _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:35 UTC</span>

<span style="font-size: 90%;">Our agenda is at [https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1604](https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1604)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:52 UTC</span>

<span style="font-size: 90%;">Thanks to _@fzipitria_ for setting this up. I have tried to divide the PRs and the Issues again.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:35:53 UTC</span>

<span style="font-size: 90%;">fwiw, you can also see the topics with this link:
[https://github.com/SpiderLabs/owasp-modsecurity-crs/labels/Meeting%20Agenda](https://github.com/SpiderLabs/owasp-modsecurity-crs/labels/Meeting%20Agenda)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:36:42 UTC</span>

<span style="font-size: 90%;">Just make sure to label the issues and prs correctly :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:45 UTC</span>

<span style="font-size: 90%;">Not all the PRs are listed, though. Those that need more work are not yet listed. If you want them to be discussed, please add them to the agenda, or tag them as _@fgs_ points out.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:37:19 UTC</span>

<span style="font-size: 90%;">_@dune73_ damn it. how long will you stay in Düsseldorf?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:21 UTC</span>

<span style="font-size: 90%;">So how about [#1616](https://github.com/coreruleset/coreruleset/issues/#1616). _@fgs_ you spotted this and want to revert it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:49 UTC</span>

<span style="font-size: 90%;">_@emphazer_: Only until tomorrow 5pm unfortunately. I should have blocked the date and only realized after they booked.. :disappointed:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:37:55 UTC</span>

<span style="font-size: 90%;">Happy to start with that. Yup, basically there were 2 PRs. One was reverted, the other wasn’t.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:38:16 UTC</span>

<span style="font-size: 90%;">ohhhkay</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:18 UTC</span>

<span style="font-size: 90%;">Ah, so that's the thing. And we revert because of double encoding?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:38:25 UTC</span>

<span style="font-size: 90%;">Yup</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:39 UTC</span>

<span style="font-size: 90%;">Then I guess the PR is ready to be merged.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">From what I gathered from the other issue the plan was to revert it but never happened.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:31 UTC</span>

<span style="font-size: 90%;">I see. I just could not quite twist my head around and did not remember the discussion.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:39:54 UTC</span>

<span style="font-size: 90%;">It should be available here: [https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/590](https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/590)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:12 UTC</span>

<span style="font-size: 90%;">Any disagree on merging here?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:40:21 UTC</span>

<span style="font-size: 90%;">I don’t think this is urgent so we can do this async</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:27 UTC</span>

<span style="font-size: 90%;">I would just make sure to note this in the ticket</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:30 UTC</span>

<span style="font-size: 90%;">for anyone who looks back</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:37 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:38 UTC</span>

<span style="font-size: 90%;">because right now it isn't super clear why these were reverted</span>

**fgs** <span style="color: grey; font-size: 90%;">19:40:58 UTC</span>

<span style="font-size: 90%;">That’s fair. I will add the information to the commit message.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:04 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:41:45 UTC</span>

<span style="font-size: 90%;">An explanation would be helpful, because I do not entirely understand why we double encode...</span>

**fgs** <span style="color: grey; font-size: 90%;">19:42:37 UTC</span>

<span style="font-size: 90%;">I will try to cover it, and if needed I can tweak it before merging it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:45 UTC</span>

<span style="font-size: 90%;">OK. So this seems settled, then let's look into [#1610](https://github.com/coreruleset/coreruleset/issues/#1610), which brings a new and very welcome rule. I have not really looked into this nor the CVE behind it, though.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:03 UTC</span>

<span style="font-size: 90%;">[#1610](https://github.com/coreruleset/coreruleset/issues/#1610) blocks HTTP Splitting in PL1, and it's required to exploit the latest php fpm vulnerability</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:47 UTC</span>

<span style="font-size: 90%;">all become possible because a LF in the filename break a common used regex in nginx conf</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:00 UTC</span>

<span style="font-size: 90%;">We have been talking about this in September. But I take it you are focusing on one problem here and not killing the splitting entirely. Correct?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:18 UTC</span>

<span style="font-size: 90%;">Also look at [#1310](https://github.com/coreruleset/coreruleset/issues/#1310), which is open again (and needs work)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:23 UTC</span>

<span style="font-size: 90%;">i mean it looks like it blocks LFs</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:30 UTC</span>

<span style="font-size: 90%;">soo it would break most splitting attacks</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:39 UTC</span>

<span style="font-size: 90%;">yes exactly</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:41 UTC</span>

<span style="font-size: 90%;">looks like a nice rule to me!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:04 UTC</span>

<span style="font-size: 90%;">Looks nice, yeah</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:13 UTC</span>

<span style="font-size: 90%;">it seems resonable to me -- i guess we're about to see how many people use LFs in their regular day to day code :stuck_out_tongue:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:46:25 UTC</span>

<span style="font-size: 90%;">Any reason not to add this to 921140?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">uhm maybe, can we merge both rule in a single rule?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:40 UTC</span>

<span style="font-size: 90%;">Definitely nice, but I would like to know if it covers everything in the AppSecEU talk by James Kettle. The video has now been published.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:40 UTC</span>

<span style="font-size: 90%;">i think it should be low false positive personally, but that would be the reason</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:24 UTC</span>

<span style="font-size: 90%;">ahh i see different question from _@fgs_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">Can we push this to PL1 immediately? It is 6-8 months until 3.3 release. Can we test the FPs in the meantime?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:31 UTC</span>

<span style="font-size: 90%;">yes, i think this is a different attack all together</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:02 UTC</span>

<span style="font-size: 90%;">however, if we want to push it in 3.2.1 we can call it a FN in 921140 as _@fgs_ brought up[</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">uhm maybe, can we merge both rule in a single rule?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">uhm maybe, can we merge both rule in a single rule?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:33 UTC</span>

<span style="font-size: 90%;">we need to change the message rule too</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:36 UTC</span>

<span style="font-size: 90%;">i think it is possible with the right commenting</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:48 UTC</span>

<span style="font-size: 90%;">yeah that's why it is better as its own rule (although ther eis overhead obviusyl)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:48 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ Yeah, that was my thinking</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:49:49 UTC</span>

<span style="font-size: 90%;">HTTP Splitting + HTTP Header Injection, maybe we loose a specific description of the attack in the logs, but it could makes sense</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:18 UTC</span>

<span style="font-size: 90%;">My opiinion: 2 different attacks -> 2 rules</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">I think this is a very good rule. But I think it is worth to discuss it a bit more before merging. And now that the discussion is on, we're on the right track.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:44 UTC</span>

<span style="font-size: 90%;">how do we plan to test for FPs</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:44 UTC</span>

<span style="font-size: 90%;">?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:47 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: But we have a ton of different SQL attacks in single rules.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:49 UTC</span>

<span style="font-size: 90%;">It's a very good rule, yes!</span>

**fgs** <span style="color: grey; font-size: 90%;">19:50:54 UTC</span>

<span style="font-size: 90%;">I’m not sure if these are 2 different attacks</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:12 UTC</span>

<span style="font-size: 90%;">they are very similar if they're different :stuck_out_tongue:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:51:14 UTC</span>

<span style="font-size: 90%;">It is a splitting</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:20 UTC</span>

<span style="font-size: 90%;">one just also includes injecting Methods :wink:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:35 UTC</span>

<span style="font-size: 90%;">I said: it's only one opinion :wink:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:35 UTC</span>

<span style="font-size: 90%;">ok so we can call both HTTP Splitting :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">at best HTTPHeader Injection is a subset of CRLF injection typically</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:47 UTC</span>

<span style="font-size: 90%;">and merge them in a single one</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:51 UTC</span>

<span style="font-size: 90%;">one additional reason to have multiple rules would be if the different variables have different FP rates/profiles. if the filename turns out to contain more newlines, then people could exclude that rule only (and keep the protection of the existing rule)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:09 UTC</span>

<span style="font-size: 90%;">oh, this is a good point</span>

**csanders** <span style="color: grey; font-size: 90%;">19:52:10 UTC</span>

<span style="font-size: 90%;">brb</span>

**fgs** <span style="color: grey; font-size: 90%;">19:52:59 UTC</span>

<span style="font-size: 90%;">That is true, but shouldn’t we consider splitting it at that point? Anyways, this is bikeshedding territory</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:10 UTC</span>

<span style="font-size: 90%;">yes perhaps…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:14 UTC</span>

<span style="font-size: 90%;">Can I assign the PR to somebody to work with _@theMiddle_ to get this into a merging state?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:17 UTC</span>

<span style="font-size: 90%;">Valid point, _@walter_.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:47 UTC</span>

<span style="font-size: 90%;">you could assign it to me but I’d probably want to merge as is :)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:12 UTC</span>

<span style="font-size: 90%;">I'd really like to know about FPs before we merge at PL1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:34 UTC</span>

<span style="font-size: 90%;">But you are the right person to test this in prod ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:51 UTC</span>

<span style="font-size: 90%;">that’s a fair point but we won’t know about it until someone tries it on some traffic, I could do that of course :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:55:01 UTC</span>

<span style="font-size: 90%;">I could too</span>

**fgs** <span style="color: grey; font-size: 90%;">19:55:04 UTC</span>

<span style="font-size: 90%;">Actually, since we also have 921150, I think having it separately might be more inline with what we already have</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:55:13 UTC</span>

<span style="font-size: 90%;">but I've not so much traffic for test</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:33 UTC</span>

<span style="font-size: 90%;">great, so I’ll assign it, _@theMiddle_ and me will test it out, and if we don’t find major pain points, we will merge it as-is!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:44 UTC</span>

<span style="font-size: 90%;">Let's assign to @walter and he will make to test this throughly before merging.</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:48 UTC</span>

<span style="font-size: 90%;">good, next one!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">[#1591](https://github.com/coreruleset/coreruleset/issues/#1591)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:35 UTC</span>

<span style="font-size: 90%;">[#1591](https://github.com/coreruleset/coreruleset/issues/#1591) blocks bkp extension, basically a tilde at the end of file name</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:50 UTC</span>

<span style="font-size: 90%;">Also by _@theMiddle_. Useful new problem that merits its own rule.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:53 UTC</span>

<span style="font-size: 90%;">swap and backup file created by text editor</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:07 UTC</span>

<span style="font-size: 90%;">The regex has been updated 2-3 times and I think it is now ready to be merged.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:12 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:58:14 UTC</span>

<span style="font-size: 90%;">I think this is good to go</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:58:37 UTC</span>

<span style="font-size: 90%;">_@fgs_ already helped me with the regex</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:52 UTC</span>

<span style="font-size: 90%;">Bonus points for brining the 920 rules to id 500!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:03 UTC</span>

<span style="font-size: 90%;">So we merge and move to the next item.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:00:14 UTC</span>

<span style="font-size: 90%;">lol</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:33 UTC</span>

<span style="font-size: 90%;">The other PRs need some more work and [#1590](https://github.com/coreruleset/coreruleset/issues/#1590) is scheduled in the agenda further down below.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:44 UTC</span>

<span style="font-size: 90%;">Is there any other of the open PRs that needs to be discussed here?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:02:02 UTC</span>

<span style="font-size: 90%;">Not that I can see.  We discussed 1310 last time and I haven’t done anything else on it. Not sure if anyone else had time to look into it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:47 UTC</span>

<span style="font-size: 90%;">It's on my todo list, but further down. :disappointed: We'll get back to it, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:05 UTC</span>

<span style="font-size: 90%;">OK, issue [#1600](https://github.com/coreruleset/coreruleset/issues/#1600) then.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:23 UTC</span>

<span style="font-size: 90%;">I kind of expected the original authors of this issue here tonight.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:03:43 UTC</span>

<span style="font-size: 90%;"> [#1600](https://github.com/coreruleset/coreruleset/issues/#1600) is quite controversial in some parts, interesting!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:03:48 UTC</span>

<span style="font-size: 90%;">And/or csanders?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:02 UTC</span>

<span style="font-size: 90%;">However, the reporter attended the CRS meetup last week and we kind of agreed on a common ground.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:03 UTC</span>

<span style="font-size: 90%;">They say they discussed some things with him?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:04:10 UTC</span>

<span style="font-size: 90%;">Especially the folder over branching preference</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:12 UTC</span>

<span style="font-size: 90%;">Part 1: Refactoring CRS is off the table for the time being.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:36 UTC</span>

<span style="font-size: 90%;">But we really had to brush very hard at the meetup. They kind of insisted on the folder versioning for CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:14 UTC</span>

<span style="font-size: 90%;">But they brought up very good arguments for the folder versioning on the myriad of docker folders we are going to get. So many that branching really does not make much sense anymore.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:34 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: Could you summarize the proposal we came up with?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:06:02 UTC</span>

<span style="font-size: 90%;">Is it documented in an issue?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:07:20 UTC</span>

<span style="font-size: 90%;">I still don't see a problem</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:34 UTC</span>

<span style="font-size: 90%;">Now, we did not write it up again, but decided to bring it here. However, it is basically what they proposed under (2) and (3) in the issue.
The controversial part was (1) and that is now no longer part of the discussion / will be addressed in separate issues / PRs if any.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:08:06 UTC</span>

<span style="font-size: 90%;">We will have 8 things to test for a long time</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:38 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ seems to have gone missing...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:08:45 UTC</span>

<span style="font-size: 90%;">2 modsecurity versions: v2/v3, CRS 3.x and 3.y, and nginx/apache</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:11 UTC</span>

<span style="font-size: 90%;">We support only 2 versions back from CRS</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:13 UTC</span>

<span style="font-size: 90%;">Yes, hence the many different docker versions, hence the idea to abandon different branches.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:27 UTC</span>

<span style="font-size: 90%;">I'm thinking about and and kind of....... forgot.....
I think we said part 2 and 3 are ok. And as far as I understood, they will propose PRs now.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:41 UTC</span>

<span style="font-size: 90%;">For docker it makes sense</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:47 UTC</span>

<span style="font-size: 90%;">Yes, docker only</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:51 UTC</span>

<span style="font-size: 90%;">With folder versioning within the master branch, this is easier to maintain for the docker stuff.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:51 UTC</span>

<span style="font-size: 90%;">Just use docker build -f</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:11 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:13 UTC</span>

<span style="font-size: 90%;">But CRS docker will have its own repository.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:10:17 UTC</span>

<span style="font-size: 90%;">Docker build with tags indeed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:34 UTC</span>

<span style="font-size: 90%;">Yes, they plan to do the PRs, but only if we officially agree to their proposal here tonight. So I would like to hear some more votes. This has been controversial and it's time for a decision now.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:54 UTC</span>

<span style="font-size: 90%;">Yes, that's true</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:10:56 UTC</span>

<span style="font-size: 90%;">Quite similar to the php docker, that also builds for many webservers and many versions</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:31 UTC</span>

<span style="font-size: 90%;">Let’s try to break these apart</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:41 UTC</span>

<span style="font-size: 90%;">So 3 - refactor modsecurity-crs-docker</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:49 UTC</span>

<span style="font-size: 90%;">I don’t think there is anything controversial here, is it?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:14 UTC</span>

<span style="font-size: 90%;">Just move things to their own repo + automation, from what I see</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:34 UTC</span>

<span style="font-size: 90%;">YEP</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:41 UTC</span>

<span style="font-size: 90%;">That's the easiest.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:12:52 UTC</span>

<span style="font-size: 90%;">Was there a reason to not build the Docker images from the crs repo?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:53 UTC</span>

<span style="font-size: 90%;">That’s why I started with that :smile:</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:13:39 UTC</span>

<span style="font-size: 90%;">To me, it seems that it is quite convenient to build the artifacts based on a tag</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:05 UTC</span>

<span style="font-size: 90%;">Item (2) brings the re-organising of the branches into folder versions. But I see the need here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:16 UTC</span>

<span style="font-size: 90%;">Others might disagree.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:22 UTC</span>

<span style="font-size: 90%;">_@csanders_?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:14:33 UTC</span>

<span style="font-size: 90%;">I don’t. Perhaps you or _@franbuehler_ can explain what was discussed in the meetup?</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:47 UTC</span>

<span style="font-size: 90%;">I think Chaim will be away for another 30 minutes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:57 UTC</span>

<span style="font-size: 90%;">Ah, true.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:15:22 UTC</span>

<span style="font-size: 90%;">I think we all agreed that changing from branches to folder versions inside modsecurity docker makes sense.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:27 UTC</span>

<span style="font-size: 90%;">We also talked about multi-staged builds, but that was thrown out (after being the preferred solution at a discussion back in June)</span>

**fgs** <span style="color: grey; font-size: 90%;">20:15:38 UTC</span>

<span style="font-size: 90%;">Or anyone can describe what the folder structure would be like?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:04 UTC</span>

<span style="font-size: 90%;">We did not discuss concrete folder names.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:16:12 UTC</span>

<span style="font-size: 90%;">In the modsec crs docker, why not build a container per release?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:16:23 UTC</span>

<span style="font-size: 90%;">v3.1/apache-2.9/
v3.1/apache-3.0/
v3.1/nginx-3.0/
etc.?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:35 UTC</span>

<span style="font-size: 90%;">The folder structure is going to have 3 elements: CRS version, engine version, platform. This CRS3.1 on ModSec 2.9 on Apache.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:53 UTC</span>

<span style="font-size: 90%;">Thus a bit more complicated than your idea _@fgs_.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:05 UTC</span>

<span style="font-size: 90%;">uhmm a lot of folders :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:07 UTC</span>

<span style="font-size: 90%;">_@Ruben van Vreeland_: Because it's more than only that.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:17:07 UTC</span>

<span style="font-size: 90%;">What is the benefit of this?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:29 UTC</span>

<span style="font-size: 90%;">Yes, a lot of folders but better many folders than that many branches.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:17:35 UTC</span>

<span style="font-size: 90%;">[https://hub.docker.com/_/php?tab=tags](https://hub.docker.com/_/php?tab=tags) this is how the PHP project handles it</span>

**fgs** <span style="color: grey; font-size: 90%;">20:17:56 UTC</span>

<span style="font-size: 90%;">That is just tagging</span>

**fgs** <span style="color: grey; font-size: 90%;">20:18:03 UTC</span>

<span style="font-size: 90%;">I want to see where the images are coming from</span>

**fgs** <span style="color: grey; font-size: 90%;">20:18:14 UTC</span>

<span style="font-size: 90%;"> Yes, a lot of folders but better many folders than that many branches.why?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:19:35 UTC</span>

<span style="font-size: 90%;">[https://github.com/docker-library/php/tree/b91cbb666a1a6567226b85d9e43b8b685d47e5bd/7.4-rc](https://github.com/docker-library/php/tree/b91cbb666a1a6567226b85d9e43b8b685d47e5bd/7.4-rc)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:39 UTC</span>

<span style="font-size: 90%;">One of the problems was that modsecurity-docker images came from different branch names. And crs-docker images came from different Dockerfile-2.9-apache.
That is not consistent</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:19:40 UTC</span>

<span style="font-size: 90%;">They have a folder per dockerfile</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:15 UTC</span>

<span style="font-size: 90%;">And that is what we want to have too.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:20:50 UTC</span>

<span style="font-size: 90%;">I do believe it makes sense to do trunk based automation. CI runs on master, and checks out from the branches.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:16 UTC</span>

<span style="font-size: 90%;">_@fgs_: Does that address your question / concerns?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:22:02 UTC</span>

<span style="font-size: 90%;">Not really :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:22:26 UTC</span>

<span style="font-size: 90%;">You wouldn’t normally create images for branches that don’t receive updates</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:51 UTC</span>

<span style="font-size: 90%;">Thought so. :disappointed:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:23:08 UTC</span>

<span style="font-size: 90%;">So not sure what’s the reason to create new images for CRS v3.1</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:23:32 UTC</span>

<span style="font-size: 90%;">_@fgs_ but the underlying platform might (quite likely) be updated right?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:23:34 UTC</span>

<span style="font-size: 90%;">For example</span>

**fgs** <span style="color: grey; font-size: 90%;">20:23:55 UTC</span>

<span style="font-size: 90%;">Then you will be creating images multiple times a day</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:01 UTC</span>

<span style="font-size: 90%;">Now that we have 3.2, that's over. But we'll keep 3.2  around even when 3.3 is out, I guess. At least for a while.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:16 UTC</span>

<span style="font-size: 90%;">And there is 3.2.1 to accomodate for etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:19 UTC</span>

<span style="font-size: 90%;">So I think that plays a role.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:42 UTC</span>

<span style="font-size: 90%;">And if it is for testing, then we need the various engines and platforms, namely if the number of engines grows.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:24:58 UTC</span>

<span style="font-size: 90%;">Yup. So you have CRS patches that trigger builds, and platform patches that trigger builds.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:25:12 UTC</span>

<span style="font-size: 90%;">Or maybe that was not part of the original issue</span>

**fgs** <span style="color: grey; font-size: 90%;">20:25:26 UTC</span>

<span style="font-size: 90%;">And this sounds like a very specific problem</span>

**fgs** <span style="color: grey; font-size: 90%;">20:25:54 UTC</span>

<span style="font-size: 90%;">Who is going to trigger the image updates?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:26:14 UTC</span>

<span style="font-size: 90%;">Just to be clear, I’m not against the idea but I’m trying to understand the reasoning</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:28 UTC</span>

<span style="font-size: 90%;">Thanks. That's very welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:42 UTC</span>

<span style="font-size: 90%;">_@csanders_ is out at a meeting and will be back in 20min or so.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:26:43 UTC</span>

<span style="font-size: 90%;">It feels like this is mainly to address particular concerns</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:26:48 UTC</span>

<span style="font-size: 90%;">I assume daily triggers</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:57 UTC</span>

<span style="font-size: 90%;">Let's keep this open until he returns and we'll revisit then.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:27:04 UTC</span>

<span style="font-size: 90%;">But its quite minor</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:26 UTC</span>

<span style="font-size: 90%;">He has been talking with the guys too. Maybe he has additional arugments. If not, we'll refer everybody to the issue again.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:27:29 UTC</span>

<span style="font-size: 90%;">This might be discussed best in the issue?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:15 UTC</span>

<span style="font-size: 90%;">_@Ruben van Vreeland_: This whole business has been discussed ad nauseam. This is now a new proposal because he have not solved the structural problem with our docker. It's time to get over this, really.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:33 UTC</span>

<span style="font-size: 90%;">So let's move on for the time being.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:40 UTC</span>

<span style="font-size: 90%;">That would be you then _@Ruben van Vreeland_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:09 UTC</span>

<span style="font-size: 90%;">Ruben is working on securely.ai. He demoed in Amsterdam in September and he would now like to show you what he and his colleagues are up to</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:29:21 UTC</span>

<span style="font-size: 90%;">Hi :smile:</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:29:46 UTC</span>

<span style="font-size: 90%;">We're working on a platform on top of modsec logs, that gives insight, alerts, and can push configuration updates to modsec</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:13 UTC</span>

<span style="font-size: 90%;">nice</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:30:27 UTC</span>

<span style="font-size: 90%;">We're looking for feedback, the project is in it's very early phase currently. But, with a few bugs, runs in production :wink:</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:30:55 UTC</span>

<span style="font-size: 90%;">If you want, I have a Kibana environment available online, where you can do some attacks, and see a dasbhaord</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:57 UTC</span>

<span style="font-size: 90%;">can we have access to a demo?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:31:06 UTC</span>

<span style="font-size: 90%;">If not, I have some very limited documentation</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:31:11 UTC</span>

<span style="font-size: 90%;">Let me post the two links</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:31:23 UTC</span>

<span style="font-size: 90%;">[https://dev.securely.ai/s/demo/app/kibana#/dashboard/79072e90-ad55-11e9-b952-6da56fbddb1b](https://dev.securely.ai/s/demo/app/kibana#/dashboard/79072e90-ad55-11e9-b952-6da56fbddb1b)
Username: demo
Password: 30qWsYt1zQNiOeyqFQLDmmRqKNKVGuK4</span>

↳ **fgs** <span style="color: grey; font-size: 90%;">20:38:58 UTC</span>

<span style="font-size: 90%;">_@anna_ :point_up:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:31:35 UTC</span>

<span style="font-size: 90%;">for me this could be really interesting :slightly_smiling_face:
 can push configuration updates to modsec</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:31:48 UTC</span>

<span style="font-size: 90%;">This demo account has all the rights to change dashboards. Powers & responsibility :wink:</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:32:19 UTC</span>

<span style="font-size: 90%;">The wiki is available here</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:32:20 UTC</span>

<span style="font-size: 90%;">[https://git.securely.ai/securely/common/securely-app-oss/wikis/home](https://git.securely.ai/securely/common/securely-app-oss/wikis/home)</span>

**fgs** <span style="color: grey; font-size: 90%;">20:32:38 UTC</span>

<span style="font-size: 90%;">Pretty nice!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:48 UTC</span>

<span style="font-size: 90%;">thanks, cool</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:32:49 UTC</span>

<span style="font-size: 90%;">And, you can trigger Slack alerts, just run some attacks on:
https//hackme.securely.ai</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:52 UTC</span>

<span style="font-size: 90%;">It looks quite slick, does not it.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:32:59 UTC</span>

<span style="font-size: 90%;">[https://hackme.securely.ai/](https://hackme.securely.ai/)</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:33:21 UTC</span>

<span style="font-size: 90%;">It hooked up to a ModSec CRS in Kubernetes (Ingress).</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:33:32 UTC</span>

<span style="font-size: 90%;">It can push Exclusoins in real time too.</span>

**unknown user** <span style="color: grey; font-size: 90%;">20:33:38 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">20:33:55 UTC</span>

<span style="font-size: 90%;">nice!</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:34:43 UTC</span>

<span style="font-size: 90%;">The goal is to make CRS even more foolproof (and used in production) and enable developers to work with it "self-service"</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:34:58 UTC</span>

<span style="font-size: 90%;">And upgrade users from PL1 to PL2</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:11 UTC</span>

<span style="font-size: 90%;">Good plan. Can you tell us a bit about licensing, OSS etc?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:35:16 UTC</span>

<span style="font-size: 90%;">In order to do that, we have a few heuristics.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:35:35 UTC</span>

<span style="font-size: 90%;">Yeah very good question. The answer is... we don't know exactly, and we need your help</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:36:03 UTC</span>

<span style="font-size: 90%;">For this week, i've just copied 90% of the codebase to the "OSS" repo.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:36:47 UTC</span>

<span style="font-size: 90%;">I do like the GitLab model. Everything that a single engineer uses, is free. Everything a organization needs, is subscription.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:37:21 UTC</span>

<span style="font-size: 90%;">So exclusions -> OSS, audit logging for multiple users -> subscription</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:37:55 UTC</span>

<span style="font-size: 90%;">You are way ahead of me in terms of OSS so I think you should help us :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:10 UTC</span>

<span style="font-size: 90%;">Can I run a test-suite against your URL and our slack becomes DoSed? (Asking for a friend)</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:38:34 UTC</span>

<span style="font-size: 90%;">It has an engine that builds sessions. For example, a session per IP.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:38:56 UTC</span>

<span style="font-size: 90%;">Each session sends a new alert if the risk increases.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:07 UTC</span>

<span style="font-size: 90%;">I think your rule of thumb makes a lot of sense. At least for the beginning.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:39:13 UTC</span>

<span style="font-size: 90%;">So you can, at a cost of buying IP addresses.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:39 UTC</span>

<span style="font-size: 90%;">What does audit logging for multiple users mean?</span>

**unknown user** <span style="color: grey; font-size: 90%;">20:39:56 UTC</span>

<span style="font-size: 90%;"></span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:39:56 UTC</span>

<span style="font-size: 90%;">You can open "Profiles" dashboard, there you have the raw profiles</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:40:46 UTC</span>

<span style="font-size: 90%;">So a user can create an exclusion. And delete / update one. Access controls can be added to it.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:41:21 UTC</span>

<span style="font-size: 90%;">That might be a feature that a organization wants.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:41:44 UTC</span>

<span style="font-size: 90%;">Can you describe the underlying architecture a bit?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:45 UTC</span>

<span style="font-size: 90%;">I see. Thanks.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:42:08 UTC</span>

<span style="font-size: 90%;"></span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:42:29 UTC</span>

<span style="font-size: 90%;">So, it starts with access logs and modsec (or other waf) audit logs.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:42:49 UTC</span>

<span style="font-size: 90%;">Shipped with filebeat / rsyslog / ...</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:43:28 UTC</span>

<span style="font-size: 90%;">Then we normalize the logs (ModSec JSON / Audit Log / access log) to ECS. Elastics Common field names.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:44:01 UTC</span>

<span style="font-size: 90%;">We run a few plugins there. For example, try and find the originating controller</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:44:26 UTC</span>

<span style="font-size: 90%;"> /user/134 becomes /user/:id</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:44:40 UTC</span>

<span style="font-size: 90%;">So that is parsing</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:44:57 UTC</span>

<span style="font-size: 90%;">There is also a bit of enriching</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:45:10 UTC</span>

<span style="font-size: 90%;">Double reverse dns, AS numbers, etc.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:45:20 UTC</span>

<span style="font-size: 90%;">Just to make it easy for the analist, and enable searching</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:45:41 UTC</span>

<span style="font-size: 90%;">Then, we have a "rule" that queries all the past ES logs to find similar attacks.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:46:11 UTC</span>

<span style="font-size: 90%;">It queries ES, for example for "<script>alert(1)</script>" to find similar patterns. These are added as document ids.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:46:24 UTC</span>

<span style="font-size: 90%;">And a bunch more, but best to look in the sources.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:47:02 UTC</span>

<span style="font-size: 90%;">Cool, thanks for the detailed explanation.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:47:09 UTC</span>

<span style="font-size: 90%;">The second pipeline is the "correlation" pipeline. Currently runs on IP, and calculates temporal statistics. For example, how many attacks have we seen in the past 1 / 5 /1 5 minutes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:15 UTC</span>

<span style="font-size: 90%;">Thank you Ruben. We are expecting _@csanders_ back anytime now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:26 UTC</span>

<span style="font-size: 90%;">We can then return to [#1600](https://github.com/coreruleset/coreruleset/issues/#1600).</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:47:26 UTC</span>

<span style="font-size: 90%;">And third step is automation. So block if a threshold is reached.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:47:31 UTC</span>

<span style="font-size: 90%;">This is really, really good</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:47:54 UTC</span>

<span style="font-size: 90%;">Great. I'm available for questions after this session.</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:03 UTC</span>

<span style="font-size: 90%;">:ok_hand:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:48:08 UTC</span>

<span style="font-size: 90%;">very nice work _@Ruben van Vreeland_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:12 UTC</span>

<span style="font-size: 90%;">There are many design decisions involved, which I like. But I would like to see them in :writing_hand:</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:48:31 UTC</span>

<span style="font-size: 90%;">Yup, exactly, working on that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:35 UTC</span>

<span style="font-size: 90%;">Let me know how can I help</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:48:43 UTC</span>

<span style="font-size: 90%;">Exactly that :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:59 UTC</span>

<span style="font-size: 90%;">One of the things we talked in Ams</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:09 UTC</span>

<span style="font-size: 90%;">Was about the rule generation for the false positives</span>

**fgs** <span style="color: grey; font-size: 90%;">20:49:26 UTC</span>

<span style="font-size: 90%;">Is this managed, self-hosted, or both?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:49:28 UTC</span>

<span style="font-size: 90%;"></span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:49:35 UTC</span>

<span style="font-size: 90%;">Rule generation is there.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:49:50 UTC</span>

<span style="font-size: 90%;">It has a bug, that one is fixed btw</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:52 UTC</span>

<span style="font-size: 90%;">Cool!</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:50:14 UTC</span>

<span style="font-size: 90%;">Both self managed and SaaS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:21 UTC</span>

<span style="font-size: 90%;">Excellent. Yeah, I would normally use ruleRemoveTargetById</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:51:17 UTC</span>

<span style="font-size: 90%;">OSS is just docker-compose up. And then with a "licence" SaaS / download containers.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:20 UTC</span>

<span style="font-size: 90%;">If _@csanders_ is not coming back, I think we should move on.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:51:31 UTC</span>

<span style="font-size: 90%;">Def looks very interesting. I will explore it a bit more when I have some time.
Would the demo account work for a bit?</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:56 UTC</span>

<span style="font-size: 90%;">how do you go from a detection to the exclusion generation?</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:51:57 UTC</span>

<span style="font-size: 90%;">I can create an account for only you, and you can push your own logs to it as well.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:52:26 UTC</span>

<span style="font-size: 90%;">Click on the rule in an audit log record.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:52:36 UTC</span>

<span style="font-size: 90%;">Thanks. I want to show this to someone so I might contact you via DM later.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:52:38 UTC</span>

<span style="font-size: 90%;">And then the builder is opened with sane defaults.</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:41 UTC</span>

<span style="font-size: 90%;">ahhhh found it</span>

**fgs** <span style="color: grey; font-size: 90%;">20:53:11 UTC</span>

<span style="font-size: 90%;">_@dune73_ should we go back briefly to the topic or skip it for now?</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:13 UTC</span>

<span style="font-size: 90%;">really cool!</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:53:25 UTC</span>

<span style="font-size: 90%;">You push them to hackme directly</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:53:31 UTC</span>

<span style="font-size: 90%;">So use with caution hehe</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:48 UTC</span>

<span style="font-size: 90%;">So can we take a look at [#1599](https://github.com/coreruleset/coreruleset/issues/#1599).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:01 UTC</span>

<span style="font-size: 90%;">_@fgs_: Let's move back</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:21 UTC</span>

<span style="font-size: 90%;">I tought we would take Ruben until _@csanders_ returns. but then he did not, so let's look at [#1599](https://github.com/coreruleset/coreruleset/issues/#1599).</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">20:54:31 UTC</span>

<span style="font-size: 90%;">I'll be available later indeed :thumbsup:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:39 UTC</span>

<span style="font-size: 90%;">Thank you Ruben.</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:51 UTC</span>

<span style="font-size: 90%;">thanks for the cool demo _@Ruben van Vreeland_!</span>

**fgs** <span style="color: grey; font-size: 90%;">20:54:53 UTC</span>

<span style="font-size: 90%;">Yup, very cool</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:00 UTC</span>

<span style="font-size: 90%;">_@airween_ has described an issue / new plans with Travis here. But I think he needs more people discussing this with him.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:56:01 UTC</span>

<span style="font-size: 90%;">Re # 1599, yes, yes and yes. Not sure what’s there to discuss :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:24 UTC</span>

<span style="font-size: 90%;">It's probably too much to discuss here. But can we assign to somebody to solve the open questions with him and herd it towards a PR?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:41 UTC</span>

<span style="font-size: 90%;">You volunteer _@fgs_?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:57:05 UTC</span>

<span style="font-size: 90%;">Yup, I will add my name. I think this is something we can all chime in</span>

**fgs** <span style="color: grey; font-size: 90%;">20:57:13 UTC</span>

<span style="font-size: 90%;">And can grow as we see new things to add</span>

**fgs** <span style="color: grey; font-size: 90%;">20:57:25 UTC</span>

<span style="font-size: 90%;">So I’d suggest to just have a replacement for what we have first</span>

**fgs** <span style="color: grey; font-size: 90%;">20:57:35 UTC</span>

<span style="font-size: 90%;">And then add more features incrementally so _@airween_ is not blocked</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:49 UTC</span>

<span style="font-size: 90%;">That sounds only fair.</span>

**airween** <span style="color: grey; font-size: 90%;">20:57:51 UTC</span>

<span style="font-size: 90%;">I'ld ask you what could be the the "new things to add" :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:53 UTC</span>

<span style="font-size: 90%;">_@airween_?</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:13 UTC</span>

<span style="font-size: 90%;">oh definitely, there are so many things to think about, although I’d recommend creating a MVP first</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:18 UTC</span>

<span style="font-size: 90%;">now the tool does two checks</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:20 UTC</span>

<span style="font-size: 90%;">would work on this be blocked by the docker changes?</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:39 UTC</span>

<span style="font-size: 90%;">or can it run in parallel without conflicts</span>

**csanders** <span style="color: grey; font-size: 90%;">20:59:19 UTC</span>

<span style="font-size: 90%;">hey friends i'm back</span>

**fgs** <span style="color: grey; font-size: 90%;">20:59:30 UTC</span>

<span style="font-size: 90%;">_@airween_ I think we can add things later. Let’s just get something working that ensures that the rules are OK first (and anything else that is ready now).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:51 UTC</span>

<span style="font-size: 90%;">Welcome _@csanders_. We are finishing [#1599](https://github.com/coreruleset/coreruleset/issues/#1599) and will then return to [#1600](https://github.com/coreruleset/coreruleset/issues/#1600) with your support.</span>

**airween** <span style="color: grey; font-size: 90%;">20:59:53 UTC</span>

<span style="font-size: 90%;">I think it can run in parallel, this tool "only" checks the rules and some consistency check</span>

**csanders** <span style="color: grey; font-size: 90%;">21:00:07 UTC</span>

<span style="font-size: 90%;">thank you :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">21:00:16 UTC</span>

<span style="font-size: 90%;">If it covers what we already have I think that’s good to ship it :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">21:00:17 UTC</span>

<span style="font-size: 90%;">but we can extend this last list</span>

**fgs** <span style="color: grey; font-size: 90%;">21:00:38 UTC</span>

<span style="font-size: 90%;">As _@walter_ said, let’s get a MVP first</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:53 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:04 UTC</span>

<span style="font-size: 90%;">[#1599](https://github.com/coreruleset/coreruleset/issues/#1599) is settled and we move back to [#1600](https://github.com/coreruleset/coreruleset/issues/#1600)?</span>

**fgs** <span style="color: grey; font-size: 90%;">21:01:31 UTC</span>

<span style="font-size: 90%;">_@airween_ Let’s take this to DM</span>

**csanders** <span style="color: grey; font-size: 90%;">21:01:31 UTC</span>

<span style="font-size: 90%;">awesome</span>

**airween** <span style="color: grey; font-size: 90%;">21:01:38 UTC</span>

<span style="font-size: 90%;">right</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:42 UTC</span>

<span style="font-size: 90%;">thank you guys.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:13 UTC</span>

<span style="font-size: 90%;">So [#1600](https://github.com/coreruleset/coreruleset/issues/#1600): @bufrasch and I could not bring the right arguments to convince _@fgs_ why the folder versioning is a good idea for our docker.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:22 UTC</span>

<span style="font-size: 90%;">_@csanders_: do you see additional ones?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:32 UTC</span>

<span style="font-size: 90%;">so we're just talking about the CRS side of foldering?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:56 UTC</span>

<span style="font-size: 90%;">No, the CRS side is off the table. It's about the foldering of the docker stuff. (2) in the issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:11 UTC</span>

<span style="font-size: 90%;">(1) is removed from the proposal.</span>

**fgs** <span style="color: grey; font-size: 90%;">21:03:23 UTC</span>

<span style="font-size: 90%;">As for 1. we’re also excluding renaming some of the directories?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:38 UTC</span>

<span style="font-size: 90%;">These will be separate issues and separate PRs.</span>

**fgs** <span style="color: grey; font-size: 90%;">21:03:46 UTC</span>

<span style="font-size: 90%;">Ok</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:50 UTC</span>

<span style="font-size: 90%;">We said we are generally open if there is a painpoint.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:12 UTC</span>

<span style="font-size: 90%;">But they should not try to change the branch / folder structure of our repo. We would object strongly.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:26 UTC</span>

<span style="font-size: 90%;">And somehow it took a big hammer to drive home that point.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:04:26 UTC</span>

<span style="font-size: 90%;">we have a LOT of images that we . will maintain</span>

**fgs** <span style="color: grey; font-size: 90%;">21:04:33 UTC</span>

<span style="font-size: 90%;">So the docker stuff, are we planning to support multiple distributions?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:04:43 UTC</span>

<span style="font-size: 90%;">multiple distros?</span>

**fgs** <span style="color: grey; font-size: 90%;">21:04:45 UTC</span>

<span style="font-size: 90%;">Right, that’s another of my questions: who is going to maintain this</span>

**csanders** <span style="color: grey; font-size: 90%;">21:04:46 UTC</span>

<span style="font-size: 90%;">as in OSs</span>

**fgs** <span style="color: grey; font-size: 90%;">21:04:50 UTC</span>

<span style="font-size: 90%;">Yup</span>

**csanders** <span style="color: grey; font-size: 90%;">21:05:07 UTC</span>

<span style="font-size: 90%;">per my memory we are planning to maintain docker:apache and docker:nginx</span>

**csanders** <span style="color: grey; font-size: 90%;">21:05:18 UTC</span>

<span style="font-size: 90%;">with plan for further docker:iis</span>

**fgs** <span style="color: grey; font-size: 90%;">21:05:21 UTC</span>

<span style="font-size: 90%;">Are we going to build images daily?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:05:23 UTC</span>

<span style="font-size: 90%;">thosse are both based on debian if i recall</span>

**csanders** <span style="color: grey; font-size: 90%;">21:05:34 UTC</span>

<span style="font-size: 90%;">it will be either daily or on change</span>

**fgs** <span style="color: grey; font-size: 90%;">21:06:02 UTC</span>

<span style="font-size: 90%;">A change in 3.3 will also rebuild 3.1?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:06:30 UTC</span>

<span style="font-size: 90%;">no, travis will kick off the build and should be smart enough to build 3.3 only</span>

**csanders** <span style="color: grey; font-size: 90%;">21:06:53 UTC</span>

<span style="font-size: 90%;">we essentially tie the branch name in CRS to the docker path in modsecurity-crs-docker</span>

**csanders** <span style="color: grey; font-size: 90%;">21:07:47 UTC</span>

<span style="font-size: 90%;">this is mostly meant to allow for a single script that CAN build all of them as needed</span>

**fgs** <span style="color: grey; font-size: 90%;">21:08:05 UTC</span>

<span style="font-size: 90%;">Something that a script cannot do already? :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:14 UTC</span>

<span style="font-size: 90%;">not sharing components</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:33 UTC</span>

<span style="font-size: 90%;">so we may say these are ALWAYS the prereqs on Nginx</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:39 UTC</span>

<span style="font-size: 90%;">no matter what the version</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:54 UTC</span>

<span style="font-size: 90%;">we'll use those to 'build' the docker images</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:58 UTC</span>

<span style="font-size: 90%;">instead of manually writing them</span>

**csanders** <span style="color: grey; font-size: 90%;">21:09:20 UTC</span>

<span style="font-size: 90%;">that is the biggest argument</span>

**fgs** <span style="color: grey; font-size: 90%;">21:10:25 UTC</span>

<span style="font-size: 90%;">Unfortunately it is me now that needs to step out</span>

**csanders** <span style="color: grey; font-size: 90%;">21:10:33 UTC</span>

<span style="font-size: 90%;">oh derar</span>

**csanders** <span style="color: grey; font-size: 90%;">21:10:37 UTC</span>

<span style="font-size: 90%;">how about we follow up in PM</span>

**csanders** <span style="color: grey; font-size: 90%;">21:10:42 UTC</span>

<span style="font-size: 90%;">since it seems you have valid concerns</span>

**csanders** <span style="color: grey; font-size: 90%;">21:10:49 UTC</span>

<span style="font-size: 90%;">and we live on nearby timezones</span>

**fgs** <span style="color: grey; font-size: 90%;">21:10:50 UTC</span>

<span style="font-size: 90%;">If you all agree then it’s ok</span>

**fgs** <span style="color: grey; font-size: 90%;">21:11:04 UTC</span>

<span style="font-size: 90%;">I don’t want to stop progress on this</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:07 UTC</span>

<span style="font-size: 90%;">OK.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:11:16 UTC</span>

<span style="font-size: 90%;">haha -- we can talk later today and get back via the ticket</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:20 UTC</span>

<span style="font-size: 90%;">But let me suggest you guys follow up in issue 1600.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:29 UTC</span>

<span style="font-size: 90%;">I'd like to make this transparent to the original reporters.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:31 UTC</span>

<span style="font-size: 90%;">Agreed?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:11:34 UTC</span>

<span style="font-size: 90%;">agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:14 UTC</span>

<span style="font-size: 90%;">Phew. So that's done for the time being too. But I get the funny feeling docker is like a boomerang.</span>

**walter** <span style="color: grey; font-size: 90%;">21:12:16 UTC</span>

<span style="font-size: 90%;">great</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:52 UTC</span>

<span style="font-size: 90%;">Which brings us to [#650](https://github.com/coreruleset/coreruleset/issues/#650).An ancient issue that was lately revived by #airween and now _@anna_ says she would be interested to give this a go.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:04 UTC</span>

<span style="font-size: 90%;">So do we have an opinion or plan for the ver action?</span>

**walter** <span style="color: grey; font-size: 90%;">21:14:35 UTC</span>

<span style="font-size: 90%;">it seems like an issue that could be automated using _@airween_ python tooling, right?</span>

**airween** <span style="color: grey; font-size: 90%;">21:15:07 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:34 UTC</span>

<span style="font-size: 90%;">Yes, I guess so. I would make it dependent on the presence of a paranoia level tag, or maybe scoring. Plus a few rules like 949110 that will get it anyways.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:44 UTC</span>

<span style="font-size: 90%;">Or all the rules that log?</span>

**airween** <span style="color: grey; font-size: 90%;">21:16:38 UTC</span>

<span style="font-size: 90%;">the PL tags affected at [#610](https://github.com/coreruleset/coreruleset/issues/#610) - or not?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:45 UTC</span>

<span style="font-size: 90%;">_@airween_: You self-assigned. Now _@anna_ says she would like to have a go and it's a good beginner issue - and a good intro to your parser script. Can you have her do it and support if she needs it? (She's probably back to work...)</span>

**airween** <span style="color: grey; font-size: 90%;">21:16:52 UTC</span>

<span style="font-size: 90%;">the [#650](https://github.com/coreruleset/coreruleset/issues/#650) is the `ver` tag</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:02 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:14 UTC</span>

<span style="font-size: 90%;">I think not all rules should have a ver tag. Or am I wrong?</span>

**airween** <span style="color: grey; font-size: 90%;">21:17:37 UTC</span>

<span style="font-size: 90%;">yes, we usually discuss about these tasks</span>

**airween** <span style="color: grey; font-size: 90%;">21:17:48 UTC</span>

<span style="font-size: 90%;">no, you're right</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:06 UTC</span>

<span style="font-size: 90%;">Good. So the two of you will handle this issue. Thanks.</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:08 UTC</span>

<span style="font-size: 90%;">I've created a table</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:14 UTC</span>

<span style="font-size: 90%;">a spreadsheet</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:41 UTC</span>

<span style="font-size: 90%;">[https://docs.google.com/spreadsheets/d/1x6tg8RyAELw0h4y1uoMEi3rPiLfrNFpK598kyXLtogs/edit?usp=drive_web&ouid=110786040352774819872](https://docs.google.com/spreadsheets/d/1x6tg8RyAELw0h4y1uoMEi3rPiLfrNFpK598kyXLtogs/edit?usp=drive_web&ouid=110786040352774819872)</span>

**airween** <span style="color: grey; font-size: 90%;">21:19:14 UTC</span>

<span style="font-size: 90%;">you can turn on the filter in the headers, and you can see where the ver action missing</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:39 UTC</span>

<span style="font-size: 90%;">That's a good base. Thanks.</span>

**walter** <span style="color: grey; font-size: 90%;">21:19:57 UTC</span>

<span style="font-size: 90%;">I liked your heuristic to only apply it to logging rules, _@dune73_</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:05 UTC</span>

<span style="font-size: 90%;">So 650 is settled and I take it we have the same resolution for 610. Don't we?</span>

**walter** <span style="color: grey; font-size: 90%;">21:20:07 UTC</span>

<span style="font-size: 90%;">that should also be straightforward to do in python</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:11 UTC</span>

<span style="font-size: 90%;">Thanks _@walter_.</span>

**airween** <span style="color: grey; font-size: 90%;">21:20:58 UTC</span>

<span style="font-size: 90%;">650 and 610 are similar, but 610 is a bit more sophisticated</span>

**airween** <span style="color: grey; font-size: 90%;">21:21:18 UTC</span>

<span style="font-size: 90%;">at last week we discussed with _@fgs_ and I made a new spreadsheet</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:21 UTC</span>

<span style="font-size: 90%;">I got as much as that.</span>

**airween** <span style="color: grey; font-size: 90%;">21:21:54 UTC</span>

<span style="font-size: 90%;">there is an another table too:
[https://docs.google.com/spreadsheets/d/1B2VCMauDQ-eubNwOmz8IbqQ4xeljnrbTY9N-bs2W3bA/edit#gid=1564920677](https://docs.google.com/spreadsheets/d/1B2VCMauDQ-eubNwOmz8IbqQ4xeljnrbTY9N-bs2W3bA/edit#gid=1564920677)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:48 UTC</span>

<span style="font-size: 90%;">So can we leave this in your hands and you coordinate with Anna and _@fgs_ when there is a need?</span>

**airween** <span style="color: grey; font-size: 90%;">21:22:57 UTC</span>

<span style="font-size: 90%;">but the solution is more clear for me in case of 610: where the column J or column K has the value "X", then we have to align the rule</span>

**airween** <span style="color: grey; font-size: 90%;">21:23:07 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:52 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:59 UTC</span>

<span style="font-size: 90%;">So that's the issues for tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:08 UTC</span>

<span style="font-size: 90%;">Time is very much advanced.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:27 UTC</span>

<span style="font-size: 90%;">But I'd like to share some infos about a call with Trustwave last week.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:51 UTC</span>

<span style="font-size: 90%;">_@csanders_, @Walter and I were on a callwith the new ModSec coordinator at TW and with Felipe, the lead ModSec developer.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:05 UTC</span>

<span style="font-size: 90%;">_@walter_: Could you summarize this please?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:12 UTC</span>

<span style="font-size: 90%;">Drum roll.....</span>

**walter** <span style="color: grey; font-size: 90%;">21:25:53 UTC</span>

<span style="font-size: 90%;">yes, Anat Davidi is now managing the project and we had a very nice chat with her and Felipe</span>

**walter** <span style="color: grey; font-size: 90%;">21:26:20 UTC</span>

<span style="font-size: 90%;">to summarize, Trustwave is continuing development on ModSecurity 3, focusing on performance and feature additions, and they hope to do a release at the end of the year</span>

**walter** <span style="color: grey; font-size: 90%;">21:26:34 UTC</span>

<span style="font-size: 90%;">the ModSec3 Apache connector, which is now not yet finished, is also on the roadmap</span>

**walter** <span style="color: grey; font-size: 90%;">21:28:17 UTC</span>

<span style="font-size: 90%;">we had some discussions about PRs that were on the ModSec github but not accepted, Felipe said there were coding style issues but he would like to address them, however it is hard to work simultaneously on many PRs so we should pick one PR at a time</span>

**walter** <span style="color: grey; font-size: 90%;">21:29:29 UTC</span>

<span style="font-size: 90%;">so we can discuss amongst ourselves which PRs we find are most urgent and then use github to communicate about this</span>

**walter** <span style="color: grey; font-size: 90%;">21:30:08 UTC</span>

<span style="font-size: 90%;">furthermore we had some productive discussions about the format of TW / CRS cooperation and we ended the call hopeful that we will have better communication and collaboration going forward :)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:30:56 UTC</span>

<span style="font-size: 90%;">They were quite insisting that github should be used actively and I think we should no longer be shy about expressing our need to make progress on lingering PRs.</span>

**walter** <span style="color: grey; font-size: 90%;">21:32:41 UTC</span>

<span style="font-size: 90%;">in the past communication from TW was not always very forthcoming, but I could also see their point where Felipe might have been overwhelmed by many PRs, I’ve had this sort of fatigue where a well intentioned outside collaborator opens a lot of PRs which have some issues that sometimes require intensive review, I can see where it is easier on Felipe to do it one PR by one</span>

**walter** <span style="color: grey; font-size: 90%;">21:32:56 UTC</span>

<span style="font-size: 90%;">so I guess we should pick our favorite issue :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">21:33:12 UTC</span>

<span style="font-size: 90%;">and then drive it with good information and reasoning</span>

**walter** <span style="color: grey; font-size: 90%;">21:33:32 UTC</span>

<span style="font-size: 90%;">now I am not running ModSec 3 yet but maybe we should look at missing features first</span>

**dune73** <span style="color: grey; font-size: 90%;">21:33:44 UTC</span>

<span style="font-size: 90%;">_@airween_: Is there one or two where you think our project should put our weight behind?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:34:13 UTC</span>

<span style="font-size: 90%;">v3 compatibility!</span>

**airween** <span style="color: grey; font-size: 90%;">21:34:28 UTC</span>

<span style="font-size: 90%;">as you know, my goal was that make ModSec3 fully compatible with v2 with Apache at least</span>

**airween** <span style="color: grey; font-size: 90%;">21:34:43 UTC</span>

<span style="font-size: 90%;">I've used the ftw to check this</span>

**airween** <span style="color: grey; font-size: 90%;">21:34:55 UTC</span>

<span style="font-size: 90%;">and what I found then, tried to fix</span>

**airween** <span style="color: grey; font-size: 90%;">21:35:31 UTC</span>

<span style="font-size: 90%;">walked on this way, I've sent about 15 patch - and few more without a direct commit</span>

**airween** <span style="color: grey; font-size: 90%;">21:36:08 UTC</span>

<span style="font-size: 90%;">but there are 3, which brakes the full compability (viewed only the ftw results)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:36:52 UTC</span>

<span style="font-size: 90%;">That would be ModSecv3 the engine to make modSec v3 on NGINX compatible with v2?</span>

**airween** <span style="color: grey; font-size: 90%;">21:38:04 UTC</span>

<span style="font-size: 90%;"></span>

**airween** <span style="color: grey; font-size: 90%;">21:38:39 UTC</span>

<span style="font-size: 90%;">no, I used Apache to comparing the v3 with v2</span>

**airween** <span style="color: grey; font-size: 90%;">21:38:54 UTC</span>

<span style="font-size: 90%;">the Apache connector was in that state, that I could use it</span>

**airween** <span style="color: grey; font-size: 90%;">21:39:27 UTC</span>

<span style="font-size: 90%;">(I also worked on that, but it's also contains several bugs - and may be some generic design error)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:39:36 UTC</span>

<span style="font-size: 90%;">So you patched the connector and then it would work and then you could work on ModSec3? So the PRs above will also improve for ModSec for NGINX?</span>

**airween** <span style="color: grey; font-size: 90%;">21:40:13 UTC</span>

<span style="font-size: 90%;">yes, there was an another spreadsheet - maybe you remember - where all ftw tests were PASSED</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:25 UTC</span>

<span style="font-size: 90%;">And what order for these PRs do you prefer? (TW asked us to go with one, maybe two, PRs at a time.)</span>

**airween** <span style="color: grey; font-size: 90%;">21:40:27 UTC</span>

<span style="font-size: 90%;">then was about 1550 tests</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:33 UTC</span>

<span style="font-size: 90%;">I clearly remember that spreadsheet.</span>

**airween** <span style="color: grey; font-size: 90%;">21:40:56 UTC</span>

<span style="font-size: 90%;">pfff... I can't decide what is the most important :stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">21:41:12 UTC</span>

<span style="font-size: 90%;">then choose the one with the easiest fix :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">21:41:17 UTC</span>

<span style="font-size: 90%;">So the PRs above will also improve for ModSec for NGINX? - yes, but not for all cases</span>

**airween** <span style="color: grey; font-size: 90%;">21:41:47 UTC</span>

<span style="font-size: 90%;">the [#2023](https://github.com/coreruleset/coreruleset/issues/#2023) and [#2107](https://github.com/coreruleset/coreruleset/issues/#2107) is trivial, easy to understand, and ready to merge...</span>

**airween** <span style="color: grey; font-size: 90%;">21:42:01 UTC</span>

<span style="font-size: 90%;">the [#2045](https://github.com/coreruleset/coreruleset/issues/#2045) is a bigger problem</span>

**airween** <span style="color: grey; font-size: 90%;">21:42:51 UTC</span>

<span style="font-size: 90%;">Mirko also reported this bug: [https://github.com/SpiderLabs/ModSecurity/issues/2146](https://github.com/SpiderLabs/ModSecurity/issues/2146)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:43:05 UTC</span>

<span style="font-size: 90%;">One of them has a request open by Felipe. One of them has a bit of conversation. And one has been without comment from Felipe. I think it's best to work on the one where he requested a change. Then the one where he reacted and then the one that has been ignored from his side (probably because he wants the other ones fixed first).</span>

**dune73** <span style="color: grey; font-size: 90%;">21:43:43 UTC</span>

<span style="font-size: 90%;">So that would be [#2023](https://github.com/coreruleset/coreruleset/issues/#2023) first from my point of view.</span>

**walter** <span style="color: grey; font-size: 90%;">21:44:00 UTC</span>

<span style="font-size: 90%;">that makes sense!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:44:14 UTC</span>

<span style="font-size: 90%;">Then [#2107](https://github.com/coreruleset/coreruleset/issues/#2107), finally [#2045](https://github.com/coreruleset/coreruleset/issues/#2045).</span>

**airween** <span style="color: grey; font-size: 90%;">21:44:59 UTC</span>

<span style="font-size: 90%;">[#2023](https://github.com/coreruleset/coreruleset/issues/#2023) could be a bit "dangerous" bug, because with the actually used parsing method could bypassed (I mean the WAF)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:45:10 UTC</span>

<span style="font-size: 90%;">_@airween_: Is there anything blocking you from making the change he requested for [#2023](https://github.com/coreruleset/coreruleset/issues/#2023).If you perform that change, we can then push for a merge or ask that roadblocks are still stopping him.</span>

**airween** <span style="color: grey; font-size: 90%;">21:45:20 UTC</span>

<span style="font-size: 90%;">_@fgs_, _@theMiddle_ if you want to see that... :slightly_smiling_face:</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:46:25 UTC</span>

<span style="font-size: 90%;">sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:45:51 UTC</span>

<span style="font-size: 90%;">I do not understand. Your fix has a bug, or the original code has a bypass bug and you are fixing it, or not?</span>

**airween** <span style="color: grey; font-size: 90%;">21:46:20 UTC</span>

<span style="font-size: 90%;">_@dune73_ I'm done with that he asked me...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:46:25 UTC</span>

<span style="font-size: 90%;">sure!</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:46:25 UTC</span>

<span style="font-size: 90%;">sure!</span>

**airween** <span style="color: grey; font-size: 90%;">21:47:01 UTC</span>

<span style="font-size: 90%;">I made a small tool to compare the current and modified work:
[https://gist.github.com/airween/efb8a737193910b5ae893d93e0325902](https://gist.github.com/airween/efb8a737193910b5ae893d93e0325902)</span>

**airween** <span style="color: grey; font-size: 90%;">21:47:30 UTC</span>

<span style="font-size: 90%;">IMHO this gist describes perfectly what's wrong the used method, and how did I fix...</span>

**csanders** <span style="color: grey; font-size: 90%;">21:48:05 UTC</span>

<span style="font-size: 90%;">wow</span>

**airween** <span style="color: grey; font-size: 90%;">21:48:22 UTC</span>

<span style="font-size: 90%;">the problem is if you placed some spaces or extra = signs in the cookie, the parser split them at wrong positions...</span>

**airween** <span style="color: grey; font-size: 90%;">21:48:53 UTC</span>

<span style="font-size: 90%;">so I don't know what can I do any more here... :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:49:45 UTC</span>

<span style="font-size: 90%;">So this is a security relevant bug and your PR fixes it. What is then the change that he requests. Can you apply that? Because he thinks the ball is in your side of the field and he does not move until you have changed your PR.</span>

**airween** <span style="color: grey; font-size: 90%;">21:50:25 UTC</span>

<span style="font-size: 90%;">I can't confirm that's a security bug - that's why I asked _@theMiddle_ - I know he likes these topics :stuck_out_tongue:</span>

**airween** <span style="color: grey; font-size: 90%;">21:51:54 UTC</span>

<span style="font-size: 90%;">and finally, there are the parser related issues</span>

**airween** <span style="color: grey; font-size: 90%;">21:52:09 UTC</span>

<span style="font-size: 90%;">where I didn't sent any fix, just reports</span>

**dune73** <span style="color: grey; font-size: 90%;">21:52:37 UTC</span>

<span style="font-size: 90%;">OK.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:52:49 UTC</span>

<span style="font-size: 90%;">if I can trick the parser to parse the wrong key, maybe it could be used to bypass some specific rule. _@airween_ have you tested the parser with cookie flags and prefix too?</span>

**airween** <span style="color: grey; font-size: 90%;">21:53:10 UTC</span>

<span style="font-size: 90%;">[https://github.com/SpiderLabs/ModSecurity/issues/2145](https://github.com/SpiderLabs/ModSecurity/issues/2145)
[https://github.com/SpiderLabs/ModSecurity/issues/2148](https://github.com/SpiderLabs/ModSecurity/issues/2148)
[https://github.com/SpiderLabs/ModSecurity/issues/2157](https://github.com/SpiderLabs/ModSecurity/issues/2157)</span>

**airween** <span style="color: grey; font-size: 90%;">21:53:41 UTC</span>

<span style="font-size: 90%;">and one more, but now I don't find it</span>

**airween** <span style="color: grey; font-size: 90%;">21:54:30 UTC</span>

<span style="font-size: 90%;">the issue is that if you put an extra space between two keywords in config file, then the engine crashed :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:54:34 UTC</span>

<span style="font-size: 90%;">I'd like to move on, but you have not responded to my question _@airween_: Felipe has requested you to change your PR. I understand back in spring. And it seems you have not done that. Can you carry out his request, or is there a reason not to?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:54:47 UTC</span>

<span style="font-size: 90%;">I am pretty sure he won't be moving unless you sort this out.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:55:10 UTC</span>

<span style="font-size: 90%;">And he told us quite frankly, all your other PRs are blocked until the first one is cleared up.</span>

**airween** <span style="color: grey; font-size: 90%;">21:55:12 UTC</span>

<span style="font-size: 90%;">sorry, what request are you thinking?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:55:46 UTC</span>

<span style="font-size: 90%;">Near the end of 2023, there is a github notice, that the reviewer felipe requested a change.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:56:45 UTC</span>

<span style="font-size: 90%;">His last comment in March was "Hi _@airween_, I remember that we were discussing this issue over hangout a few days ago. Are the changes ready?" To what you responded that you did not, but you provided a script.</span>

**airween** <span style="color: grey; font-size: 90%;">21:57:11 UTC</span>

<span style="font-size: 90%;">yes, and there are my answers...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:58:10 UTC</span>

<span style="font-size: 90%;">Is that your June 1 response? (I'm not deep enough into the code to really understand what is going on. But I want to make sure the ball is not in your garden but with TW instead.)</span>

**airween** <span style="color: grey; font-size: 90%;">21:59:37 UTC</span>

<span style="font-size: 90%;">sure, but I'ld like to discuss her request. I do not find it justified her request, that's why I make the tool to demonstrate it.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:00:27 UTC</span>

<span style="font-size: 90%;">I see. Unfortunately, that is not clear from the conversation on github. You do not say that you think the request is wrong. So I see a misunderstanding happening.</span>

**airween** <span style="color: grey; font-size: 90%;">22:01:08 UTC</span>

<span style="font-size: 90%;">I'm sorry - I'll review the conversations on Github, and will ask Felipe directly</span>

**dune73** <span style="color: grey; font-size: 90%;">22:01:15 UTC</span>

<span style="font-size: 90%;">So let's leave it at this. I will join this issue on github and help you clear out the misunderstanding and then we can hopefully move on, eventually getting to 2107 and then 2045.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:01:54 UTC</span>

<span style="font-size: 90%;">With that, and if somebody is still awake, a brief update on the CRS meetup in Bern.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:01:58 UTC</span>

<span style="font-size: 90%;">@vuf</span>

**dune73** <span style="color: grey; font-size: 90%;">22:02:01 UTC</span>

<span style="font-size: 90%;">@bufrasch</span>

**dune73** <span style="color: grey; font-size: 90%;">22:02:18 UTC</span>

<span style="font-size: 90%;">@bufrasch and I started with a meetup there in June as we thought the potential was large neough in Bern.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:02:52 UTC</span>

<span style="font-size: 90%;">We did 3 meetings so far and had like 14, 8 and 13 people on site. Puzzle, the employer of @bufrasch has sponsored this and the food so far.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:03:20 UTC</span>

<span style="font-size: 90%;">After the last meeting we talked about the future of the meetup and decided to continue together into 2020.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:03:35 UTC</span>

<span style="font-size: 90%;">We're going to do 5 meetups in 2020, each with a presentation and a workshop.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:03:52 UTC</span>

<span style="font-size: 90%;">3 additional companies volunteered to host at least one of these meetups.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:04:16 UTC</span>

<span style="font-size: 90%;">And the participants stated quite clearly they would beinterested to do workshops where we guide them through solving open CRS issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:04:29 UTC</span>

<span style="font-size: 90%;">So this sounds very positive, I think.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:05:11 UTC</span>

<span style="font-size: 90%;">And I saw a preparation for AllDayDevOps too right?</span>

**dune73** <span style="color: grey; font-size: 90%;">22:05:12 UTC</span>

<span style="font-size: 90%;">We also decided we think streaming is too much of a hassle. Recording might be an option if we find a volunteer.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:05:31 UTC</span>

<span style="font-size: 90%;">Yes, that's going to be _@franbuehler_ and _@csanders_.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:05:41 UTC</span>

<span style="font-size: 90%;">Great!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:05:44 UTC</span>

<span style="font-size: 90%;">They did that presentation for us at the last meetup.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:05:57 UTC</span>

<span style="font-size: 90%;">_@csanders_ via remote, apparently.</span>

**walter** <span style="color: grey; font-size: 90%;">22:06:10 UTC</span>

<span style="font-size: 90%;">cool</span>

**csanders** <span style="color: grey; font-size: 90%;">22:06:20 UTC</span>

<span style="font-size: 90%;">we only have 30 minutes</span>

**csanders** <span style="color: grey; font-size: 90%;">22:06:23 UTC</span>

<span style="font-size: 90%;">so its nothing ground breaking</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:06:35 UTC</span>

<span style="font-size: 90%;">Do you track engagement in some way?</span>

**dune73** <span style="color: grey; font-size: 90%;">22:06:38 UTC</span>

<span style="font-size: 90%;">But it's a nice talk.</span>

**csanders** <span style="color: grey; font-size: 90%;">22:07:04 UTC</span>

<span style="font-size: 90%;">just talks at high level about how CRS uses travis/docker and how CRS can be deployed as part of a devops pipeline</span>

**dune73** <span style="color: grey; font-size: 90%;">22:07:07 UTC</span>

<span style="font-size: 90%;">It's meetup, so we can track participants. And we now have 45 people following the meetup online. And I think about 20 of them participated in at least one of them.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:07:31 UTC</span>

<span style="font-size: 90%;">Nothing more to add about the meetup I guess.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:07:53 UTC</span>

<span style="font-size: 90%;">The next topic was "Propose to formally use semantic versioning (MAJOR.MINOR.PATCH)". That was a topic _@fgs_ wanted to talk about, IIRC, so we might have to postpone that.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:08:03 UTC</span>

<span style="font-size: 90%;">Pretty good. Interesting to see adoption closer to developers.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:08:20 UTC</span>

<span style="font-size: 90%;">Which brings us close to the end and [#1590](https://github.com/coreruleset/coreruleset/issues/#1590), the security.md.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:08:37 UTC</span>

<span style="font-size: 90%;">What do we have to discuss there? _@fzipitria_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:08:56 UTC</span>

<span style="font-size: 90%;">Well, tough one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:09:08 UTC</span>

<span style="font-size: 90%;">What do we consider a security bug in CRS</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:09:11 UTC</span>

<span style="font-size: 90%;">Basically</span>

**dune73** <span style="color: grey; font-size: 90%;">22:09:34 UTC</span>

<span style="font-size: 90%;">Tough.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:09:35 UTC</span>

<span style="font-size: 90%;">My thoughts are "anything that can break the WAF from working"?</span>

**csanders** <span style="color: grey; font-size: 90%;">22:09:35 UTC</span>

<span style="font-size: 90%;">a FN in PL4</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:09:48 UTC</span>

<span style="font-size: 90%;">Like the ReDOS stuff</span>

**csanders** <span style="color: grey; font-size: 90%;">22:09:50 UTC</span>

<span style="font-size: 90%;">yeah a DOS caused by CRS</span>

**walter** <span style="color: grey; font-size: 90%;">22:10:09 UTC</span>

<span style="font-size: 90%;"> redos is a good example</span>

**dune73** <span style="color: grey; font-size: 90%;">22:10:12 UTC</span>

<span style="font-size: 90%;">Yes, I think ReDoS qualifies, at least the one that was real.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:10:16 UTC</span>

<span style="font-size: 90%;">But that was not PL1.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:10:28 UTC</span>

<span style="font-size: 90%;">Other than that, I think FN at PL1 is too broad.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:10:34 UTC</span>

<span style="font-size: 90%;">Well, but it will break your WAF because of CRS</span>

**csanders** <span style="color: grey; font-size: 90%;">22:10:35 UTC</span>

<span style="font-size: 90%;">changed it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:10:52 UTC</span>

<span style="font-size: 90%;">FN at PL4 could make sense also</span>

**dune73** <span style="color: grey; font-size: 90%;">22:10:53 UTC</span>

<span style="font-size: 90%;">Consequently, anything that anybody publishes is a 0-day for us, even if we block it at PL2 and above...</span>

**csanders** <span style="color: grey; font-size: 90%;">22:10:54 UTC</span>

<span style="font-size: 90%;">FN with PL 4</span>

**dune73** <span style="color: grey; font-size: 90%;">22:11:14 UTC</span>

<span style="font-size: 90%;">OK, PL4.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:11:33 UTC</span>

<span style="font-size: 90%;">FN with PL4 is certainly more narrow.</span>

**csanders** <span style="color: grey; font-size: 90%;">22:11:35 UTC</span>

<span style="font-size: 90%;">Anything that causes unexpected behavior of the engine via manipulation of existing CRS provided rules</span>

**csanders** <span style="color: grey; font-size: 90%;">22:11:46 UTC</span>

<span style="font-size: 90%;">(DOS, RCE, etc)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:11:50 UTC</span>

<span style="font-size: 90%;">Yeah, that's a little bit open</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:12:19 UTC</span>

<span style="font-size: 90%;">I mean: we don't want emails received for things that will be forwarded and treated as issues in github</span>

**csanders** <span style="color: grey; font-size: 90%;">22:12:32 UTC</span>

<span style="font-size: 90%;">i agree but i don't wanna miss an RCE because someone read it only said DOS</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:12:33 UTC</span>

<span style="font-size: 90%;">We want issues for that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:12:48 UTC</span>

<span style="font-size: 90%;">I agree</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:12:54 UTC</span>

<span style="font-size: 90%;">Just trying to draw a line</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:13:11 UTC</span>

<span style="font-size: 90%;">But it needs to be a reasonable clear line</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:13:22 UTC</span>

<span style="font-size: 90%;">It seems like people that found bypasses to rules might look for the security.md file. Is there an explicit answer for that case too?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:14:17 UTC</span>

<span style="font-size: 90%;">Test it with PL4</span>

**dune73** <span style="color: grey; font-size: 90%;">22:14:42 UTC</span>

<span style="font-size: 90%;">I think we just need to say that a bypass is not a security issue for us per se, but if it's a bypass at PL4, then we would like to have an info via mail before ti is being published as CRS bypass.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:14:50 UTC</span>

<span style="font-size: 90%;">Plus all the unexpected behaviours.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:14:59 UTC</span>

<span style="font-size: 90%;">Is that a clearpolicy?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:15:15 UTC</span>

<span style="font-size: 90%;">:thinking_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:15:25 UTC</span>

<span style="font-size: 90%;">For us, maybe yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:15:31 UTC</span>

<span style="font-size: 90%;">For general public.....</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:15:57 UTC</span>

<span style="font-size: 90%;">But we should have something, and then see how many we receive, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:16:34 UTC</span>

<span style="font-size: 90%;">So I think rephrasing to have that, and see how it goes in the future</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:17:01 UTC</span>

<span style="font-size: 90%;">If we begin receiving emails that we decide they don't belong, then we correct</span>

**dune73** <span style="color: grey; font-size: 90%;">22:17:02 UTC</span>

<span style="font-size: 90%;">It will be easier once we have the demo site up and running and that is not too far away anymore, I hear...</span>

**walter** <span style="color: grey; font-size: 90%;">22:17:11 UTC</span>

<span style="font-size: 90%;">I could also see where people would not want to post a FN publicly on github, in that case i wouldn’t mind receiving an email either</span>

**walter** <span style="color: grey; font-size: 90%;">22:17:24 UTC</span>

<span style="font-size: 90%;">i don’t expect too many mails anyway...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:17:33 UTC</span>

<span style="font-size: 90%;">Me too</span>

**dune73** <span style="color: grey; font-size: 90%;">22:18:17 UTC</span>

<span style="font-size: 90%;">Me neither.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:18:52 UTC</span>

<span style="font-size: 90%;">Yup. Good to be explicit about the PL level.</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:19:13 UTC</span>

<span style="font-size: 90%;">Also give a bit of room to yourselves, if there's a guy tweeting about bypasses.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:19:28 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: That is settled then?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:19:51 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:19:56 UTC</span>

<span style="font-size: 90%;">thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">22:19:58 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">22:20:16 UTC</span>

<span style="font-size: 90%;">I realize I was a bit too fast about the versioning above. In fact it was not _@fgs_, but you who wanted to discuss this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:20:49 UTC</span>

<span style="font-size: 90%;">Yeah, I'm in the middle of working day, I guess I skipped that part?</span>

**dune73** <span style="color: grey; font-size: 90%;">22:20:59 UTC</span>

<span style="font-size: 90%;">Are we still in a state to discuss this as a project, or would that be a discussion that affects everybody and we better postpone?
After all, the next release is months away...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:21:00 UTC</span>

<span style="font-size: 90%;">Couldn't read it in the history</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:21:08 UTC</span>

<span style="font-size: 90%;">We postpone</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:21:20 UTC</span>

<span style="font-size: 90%;">It's late for many of you</span>

**franbuehler** <span style="color: grey; font-size: 90%;">22:21:26 UTC</span>

<span style="font-size: 90%;">Yeeees</span>

**dune73** <span style="color: grey; font-size: 90%;">22:21:27 UTC</span>

<span style="font-size: 90%;">Thank you for your understanding.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:21:30 UTC</span>

<span style="font-size: 90%;">And we need to process all of the things that happened here</span>

**dune73** <span style="color: grey; font-size: 90%;">22:21:53 UTC</span>

<span style="font-size: 90%;">Very good. So are kind of done and we can get to sleep.</span>

**walter** <span style="color: grey; font-size: 90%;">22:22:11 UTC</span>

<span style="font-size: 90%;">yes!!!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:22:15 UTC</span>

<span style="font-size: 90%;">I kind of hope we would be done by 9pm and I could still go out and meet _@emphazer_...</span>

**walter** <span style="color: grey; font-size: 90%;">22:22:42 UTC</span>

<span style="font-size: 90%;">this must have been the longest monthly chat!</span>

**walter** <span style="color: grey; font-size: 90%;">22:22:48 UTC</span>

<span style="font-size: 90%;">but we covered a lot of topics</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:22:58 UTC</span>

<span style="font-size: 90%;">Have a good one all of you!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:23:03 UTC</span>

<span style="font-size: 90%;">Yes and some controversial ones on top!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:23:07 UTC</span>

<span style="font-size: 90%;">Thanks everybody</span>

**walter** <span style="color: grey; font-size: 90%;">22:23:14 UTC</span>

<span style="font-size: 90%;">Thank you all!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:23:14 UTC</span>

<span style="font-size: 90%;">:fireworks:</span>

**airween** <span style="color: grey; font-size: 90%;">22:23:17 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**walter** <span style="color: grey; font-size: 90%;">22:23:21 UTC</span>

<span style="font-size: 90%;">:owasp: </span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:23:25 UTC</span>

<span style="font-size: 90%;">bye all!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">22:23:26 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">22:27:45 UTC</span>

<span style="font-size: 90%;">:wave: bye (only joined half way through :sweat_smile: )</span>

**Ruben van Vreeland** <span style="color: grey; font-size: 90%;">22:27:50 UTC</span>

<span style="font-size: 90%;">Bye!</span>

