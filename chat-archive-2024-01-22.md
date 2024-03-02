### Mon, Jan 22nd, 2024

**dune73** <span style="color: grey; font-size: 90%;">19:31:09 UTC</span>

<span style="font-size: 90%;">Hello, hello, time for the monthly issue chat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:18 UTC</span>

<span style="font-size: 90%;">Please find the agenda at [https://github.com/coreruleset/coreruleset/issues/3466](https://github.com/coreruleset/coreruleset/issues/3466)</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:21 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:31:57 UTC</span>

<span style="font-size: 90%;">Hello :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:00 UTC</span>

<span style="font-size: 90%;">I have split the v4 label into "v4" and "v4-doc". This way only 5 (!) issues remain with the rules (and 4 doc issues).</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:23 UTC</span>

<span style="font-size: 90%;">Evening</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">Good evening </span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">Hello</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:33:13 UTC</span>

<span style="font-size: 90%;">Hi :wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:16 UTC</span>

<span style="font-size: 90%;">Hola!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:45 UTC</span>

<span style="font-size: 90%;">Thank you all for attending. _@fzipitria_ is maybe still on holidays, but I guess we'll make it work without him.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:00 UTC</span>

<span style="font-size: 90%;">It's going to be very interesting, since we're really close to v4 now. At last.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:21 UTC</span>

<span style="font-size: 90%;">I just updated the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:28 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3466](https://github.com/coreruleset/coreruleset/issues/3466)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:33 UTC</span>

<span style="font-size: 90%;">Trustwave scheduled a release covering our V3E security meeting for today.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:47 UTC</span>

<span style="font-size: 90%;">_@airween_ tested the patch for us, but we have been a bit late with our response.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:59 UTC</span>

<span style="font-size: 90%;">Have you heard from TW Ervin?</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:22 UTC</span>

<span style="font-size: 90%;">not yet</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:46 UTC</span>

<span style="font-size: 90%;">OK. Please keep us posted on this.</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:05 UTC</span>

<span style="font-size: 90%;">I've re-added everyone's address to e-mail, hope they will continue the mailing with those addresses</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:37 UTC</span>

<span style="font-size: 90%;">Next item (we need to get this off the table): There is a CRS issue / PR that is affected by V3E and the fix: [https://github.com/coreruleset/coreruleset/pull/3410](https://github.com/coreruleset/coreruleset/pull/3410)
The PR has been approved, but actually, we do not really agree on the matter. So it carries the do-not-merge label.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:41 UTC</span>

<span style="font-size: 90%;">Please have a look everybody.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:56 UTC</span>

<span style="font-size: 90%;">The final comment by _@maxleske_ is probably the way to solve this. But that would mean a new PR.
(Sorry I let this slide too long. We should have a mergeable PR by now.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:38 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Do you still think this is how we should do it?
I am not entirely sure foo%1G.txt should be a valid file name. But I really fail to see the attack vector and that means the rule is probably bogus at PL1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:05 UTC</span>

<span style="font-size: 90%;">This could be a valid file name: Taxes20%done.txt . Yes, I still think so.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:00 UTC</span>

<span style="font-size: 90%;">Do you have the time to work on the PR? If not, I can take it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:12 UTC</span>

<span style="font-size: 90%;">Yes, that's a very good example. This should be ok, indeed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:22 UTC</span>

<span style="font-size: 90%;">If you could take it, I would really appreciate.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:54 UTC</span>

<span style="font-size: 90%;">Anybody has anything else to add to this problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:16 UTC</span>

<span style="font-size: 90%;">I'll add the v4 label to it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:30 UTC</span>

<span style="font-size: 90%;">That is reasonable. Thank you very much.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:53 UTC</span>

<span style="font-size: 90%;">So let's move on to the next item on the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:05 UTC</span>

<span style="font-size: 90%;">My idea is to go through the open v4 issues and check their status.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:16 UTC</span>

<span style="font-size: 90%;">Here is the link: [https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+label%3Av4](https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+label%3Av4)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:40 UTC</span>

<span style="font-size: 90%;">First one: FP issue [#3397](https://github.com/coreruleset/coreruleset/issues/#3397).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:47 UTC</span>

<span style="font-size: 90%;">_@xanadu_ what is the status here?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:52:13 UTC</span>

<span style="font-size: 90%;">I'm not sure. I'm not working on it atm.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:52:34 UTC</span>

<span style="font-size: 90%;">I've opened a PR to address the issue but haven't received any feedback yet</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:45 UTC</span>

<span style="font-size: 90%;">Which one is that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:05 UTC</span>

<span style="font-size: 90%;">It's a difficult issue as we have to weaken detection to decrease FPs. The idea is to use more precise detection for known issues instead of generic expressions.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:14 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3494](https://github.com/coreruleset/coreruleset/pull/3494)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:19 UTC</span>

<span style="font-size: 90%;">Got you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:43 UTC</span>

<span style="font-size: 90%;">That means even at PL2, we need the precision or these FPs can't be fought?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:33 UTC</span>

<span style="font-size: 90%;">Well, the rule is pretty bad for some cases.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:54 UTC</span>

<span style="font-size: 90%;">With an FP rate of 8% on the quantitative testing, this rule is way beyond the acceptable level.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:27 UTC</span>

<span style="font-size: 90%;">(We have not really defined anything, but a rate above 1% is hard to justify, even at PL2.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:56:55 UTC</span>

<span style="font-size: 90%;">The fix should make a big difference, at some detection expense of course</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:35 UTC</span>

<span style="font-size: 90%;">_@xanadu_ could us test the PR for the new FP rate?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:16 UTC</span>

<span style="font-size: 90%;">Sure. I'll add the results to the issue/PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:57 UTC</span>

<span style="font-size: 90%;">_@maxleske_ is there any sense in re-creating the existing rule as stricter sibling of your PR at PL3?
(Like shifting the rule to PL3 and reintroduce a tuned down version - your PR - at PL2?)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:07 UTC</span>

<span style="font-size: 90%;">I don't think so. The rule triggers for trivial things like "I'm in love", because of the single quote.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:30 UTC</span>

<span style="font-size: 90%;">That's a bit steep.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:00:36 UTC</span>

<span style="font-size: 90%;">in my experience, the rule pretty much triggers anything with a
'or
"</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:10 UTC</span>

<span style="font-size: 90%;">_@maxleske_ your PR passes all the tests (-> bug bounty tests)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:51 UTC</span>

<span style="font-size: 90%;">Looks like it :slightly_smiling_face: But it's really just a first step. I'm sure there are other patterns we will need to detect but I lack the experience. If _@xanadu_ finds more, we can add those, and maybe someone else has some ideas.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:06 UTC</span>

<span style="font-size: 90%;">Hmm. So if _@xanadu_ finds there are still too many FPs, we might need a few extra cycles here.
Is this something we should hold v4 over?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:55 UTC</span>

<span style="font-size: 90%;">It's a lot of FPs, but also it's not worse than 3.3.5 :shrug:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:06:32 UTC</span>

<span style="font-size: 90%;">Hang on, that's not true, this is a new rule, so it is a regression.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:40 UTC</span>

<span style="font-size: 90%;">My thinking, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:32 UTC</span>

<span style="font-size: 90%;">Maybe we move to the next issue and then decide on both of them together.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:42 UTC</span>

<span style="font-size: 90%;">So next one is [#3396](https://github.com/coreruleset/coreruleset/issues/#3396).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:55 UTC</span>

<span style="font-size: 90%;">This is even worse: Even more FPs for PL2 and even harder to fix.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:18 UTC</span>

<span style="font-size: 90%;">We're talking about 942110.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:46 UTC</span>

<span style="font-size: 90%;">The only good thing here is that the rule has been like this in 3.3.x and I am confident everybody has disabled it already.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:58 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:10:38 UTC</span>

<span style="font-size: 90%;">Move to PL3?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:10:51 UTC</span>

<span style="font-size: 90%;">Or accept that strings starting or ending with quote marks are forbidden</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:10 UTC</span>

<span style="font-size: 90%;">The rule is about "'`; .</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:11:26 UTC</span>

<span style="font-size: 90%;">How valid is the rule in reality?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:11:46 UTC</span>

<span style="font-size: 90%;">(I haven't checked the test payloads. Is this a useful rule?)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:54 UTC</span>

<span style="font-size: 90%;">While payloads have a tendency to start and end with quotes. But I do not see the same for backticks and semicolons.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:07 UTC</span>

<span style="font-size: 90%;">The tests do not look overly dangerous.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:40 UTC</span>

<span style="font-size: 90%;">I could dig into my repo of 4M security scanner tests to see what it detects as well.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:41 UTC</span>

<span style="font-size: 90%;">Do we want to remove this rule? It's waaay too strict.
It looks for a " at the start or end of a string.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:10 UTC</span>

<span style="font-size: 90%;">I think this rule should only be applied together with other SQLI tests</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:30 UTC</span>

<span style="font-size: 90%;">The detection of the quotes themselves has no significance</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:13:45 UTC</span>

<span style="font-size: 90%;">Can we split the rule? What kills us is the "'</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:51 UTC</span>

<span style="font-size: 90%;">I see multiple options:
</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:13:54 UTC</span>

<span style="font-size: 90%;">Detect backticks and semicolons at PL2?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:00 UTC</span>

<span style="font-size: 90%;">Ah :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:08 UTC</span>

<span style="font-size: 90%;">That's what I thought. But maybe not worth the hassle.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:20 UTC</span>

<span style="font-size: 90%;">It would also be good to remove rules once in a while.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:42 UTC</span>

<span style="font-size: 90%;">For the record: The rule first like crazy on burp according to my log archive.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:53 UTC</span>

<span style="font-size: 90%;">The only thing that makes remotely sense to me is the detection of the semi-colon. Everything else could easily be part of a markdown document, for example</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:39 UTC</span>

<span style="font-size: 90%;">And honestly, there are other rules that check for special chars like ; and quotes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:09 UTC</span>

<span style="font-size: 90%;">Kick it?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:19 UTC</span>

<span style="font-size: 90%;">I do not see any different proposals. So let's remove the rule. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:41 UTC</span>

<span style="font-size: 90%;">Which brings us to the quantitative testing issue [#3392](https://github.com/coreruleset/coreruleset/issues/#3392).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:31 UTC</span>

<span style="font-size: 90%;">If I get this correctly, we still need to cover 932236 PL2, 920240 PL1 and 932380 PL1.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:00 UTC</span>

<span style="font-size: 90%;">I do not have the overview here. Are we working on these or not right now?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:09 UTC</span>

<span style="font-size: 90%;">It needs re-testing. I've just noticed that [#3394](https://github.com/coreruleset/coreruleset/issues/#3394) has been merged, so maybe 932236 is fixed, not sure.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:27 UTC</span>

<span style="font-size: 90%;">I don't think the others have been looked at.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:44 UTC</span>

<span style="font-size: 90%;">Can you re-run the test during the meeting so we learn about 932236?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:23:14 UTC</span>

<span style="font-size: 90%;">Ok. I'll disappear for a moment to another machine…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:31 UTC</span>

<span style="font-size: 90%;">For the other two rules, we lack the payloads, since there is no issue so far.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:25:04 UTC</span>

<span style="font-size: 90%;">Also [https://github.com/coreruleset/coreruleset/pull/3487](https://github.com/coreruleset/coreruleset/pull/3487) addressed 932236.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:25:28 UTC</span>

<span style="font-size: 90%;">There were a few more as well</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:51 UTC</span>

<span style="font-size: 90%;">More rules that ought to be addressed over the quantitative testing FPs?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:31 UTC</span>

<span style="font-size: 90%;">Yes, there are more, but we discussed at an earlier meeting that the 5 listed in the issue below the graphical table above are the ones we want to cover for v4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:35 UTC</span>

<span style="font-size: 90%;">The rest afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:44 UTC</span>

<span style="font-size: 90%;">Also via defining proper limits per PL.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:09 UTC</span>

<span style="font-size: 90%;">While Xanadu is away, we can look into the security issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:21 UTC</span>

<span style="font-size: 90%;">_@Esad Cetiner_ you do not have access to these.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:04 UTC</span>

<span style="font-size: 90%;">I think there are three issues - all reported by project members - that have to be checked for v4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:16 UTC</span>

<span style="font-size: 90%;">Some of them contain additional sub-issues / different payloads.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:32 UTC</span>

<span style="font-size: 90%;">_@jit_ has reported 2 of these 3 issues. Both contain 3 individual bypasses.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:46 UTC</span>

<span style="font-size: 90%;">I think there are PRs for most of them, but I lack the overview and _@jit_ is not here.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:09 UTC</span>

<span style="font-size: 90%;">I need feedback from you on one.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:16 UTC</span>

<span style="font-size: 90%;">Another one I've already merged</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:38 UTC</span>

<span style="font-size: 90%;">(I'm sorry I am so behind with the status. I had freed the afternoon to prepare this meeting, but then I had to attend an emergency meeting in school. Not so pleasant and of course this kills every plan.)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:56 UTC</span>

<span style="font-size: 90%;">Which one is that, _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:37 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/security-tracker-private/issues/14#issuecomment-1894441703](https://github.com/coreruleset/security-tracker-private/issues/14#issuecomment-1894441703)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:02 UTC</span>

<span style="font-size: 90%;">And then Jit promised another PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:34 UTC</span>

<span style="font-size: 90%;">So 1 open question, 1 PR coming. What about the other 4 payloads in his two security issues?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:36:04 UTC</span>

<span style="font-size: 90%;">Sorry, that was the wrong link</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:20 UTC</span>

<span style="font-size: 90%;">(thought so. but I was not sure.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:36:26 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3503#issuecomment-1904429141](https://github.com/coreruleset/coreruleset/pull/3503#issuecomment-1904429141)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:49 UTC</span>

<span style="font-size: 90%;">Ah, yes, I saw this tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:20 UTC</span>

<span style="font-size: 90%;">If I got this right, this problem is only for v3.3? So **no** need to do anything for v4?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:18 UTC</span>

<span style="font-size: 90%;">I'll have to check</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:39:07 UTC</span>

<span style="font-size: 90%;">(I have numbers to return to discussing 932236 when we're ready.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:08 UTC</span>

<span style="font-size: 90%;">From a cursory glance they should be good on v4</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:32 UTC</span>

<span style="font-size: 90%;">We're usually not adding better detection to old releases outside of super-critical stuff like rule set bypasses (over a fear of new FPs in an existing release line).
So I would rather explain to _@jit_ that this is kind of accepted.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:18 UTC</span>

<span style="font-size: 90%;">I suggest, I will test Jit's 6 payloads again vs v4 and the individual status and report on the dev channel tomorrow.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:42:01 UTC</span>

<span style="font-size: 90%;">Thanks. Are you going to address that in the issue or should I?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:18 UTC</span>

<span style="font-size: 90%;">Please take it into your hands.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:21 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:34 UTC</span>

<span style="font-size: 90%;">This leaves issue [https://github.com/coreruleset/security-tracker-private/issues/15](https://github.com/coreruleset/security-tracker-private/issues/15) / KK4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:55 UTC</span>

<span style="font-size: 90%;">This was reported by _@theMiddle_, but he's unfortunately not here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:40 UTC</span>

<span style="font-size: 90%;">I proposed in the issue to postpone until after v4 is out (since this could mean an SQL rules redesign).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:01 UTC</span>

<span style="font-size: 90%;">But there has not been any feedback on my proposal - nor on TheMiddle's idea / report.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:59 UTC</span>

<span style="font-size: 90%;">His idea could also play into the discussion around 942110 where we said it better be combined with another SQLi rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:06 UTC</span>

<span style="font-size: 90%;">Anybody has an opinion on all of this?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:47:38 UTC</span>

<span style="font-size: 90%;">I think it's a great idea. I don't see the necessity for the change to go into v4, however. Even if we redesign SQLl in the future, that might be v5.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:48:37 UTC</span>

<span style="font-size: 90%;">Unless we wanted to address the high FP rate that _@xanadu_ reported</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:44 UTC</span>

<span style="font-size: 90%;">Thanks for the confirmation. I really hope theMiddle is not overly pissed with my / our conservative approach here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:53 UTC</span>

<span style="font-size: 90%;">But let's leave this and return to the FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:10 UTC</span>

<span style="font-size: 90%;">So _@xanadu_ has new numbers: [https://github.com/coreruleset/coreruleset/issues/3392#issuecomment-1904758232](https://github.com/coreruleset/coreruleset/issues/3392#issuecomment-1904758232)</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:49:22 UTC</span>

<span style="font-size: 90%;">[Fresh stats.](https://github.com/coreruleset/coreruleset/issues/3392#issuecomment-1904758232)

932236 went from 275 FPs down to 254 FPs. An improvement, but probably needs further investigation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:50:23 UTC</span>

<span style="font-size: 90%;">I can open a new issue tomorrow and include payload examples.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:43 UTC</span>

<span style="font-size: 90%;">Please do. I think it's worth it for 932236.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:51:17 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:34 UTC</span>

<span style="font-size: 90%;">920240 PL1 is an interesting case.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:02 UTC</span>

<span style="font-size: 90%;">No change between v3.3 and v4. Yet 1.3% of payloads trigger this rule in the quantitiative testing.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:11 UTC</span>

<span style="font-size: 90%;">SecRule REQUEST_HEADERS:Content-Type "@rx ^(?i)application/x-www-form-urlencoded" \
    "id:920240,\
    phase:2,\
    block,\
    t:none,\
    msg:'URL Encoding Abuse Attack Attempt',\
    logdata:'%{MATCHED_VAR}',\
    tag:'application-multi',\
    tag:'language-multi',\
    tag:'platform-multi',\
    tag:'attack-protocol',\
    tag:'paranoia-level/1',\
    tag:'OWASP_CRS',\
    tag:'capec/1000/255/153/267/72',\
    ver:'OWASP_CRS/4.0.0-rc2',\
    severity:'WARNING',\
    chain"
    SecRule REQUEST_BODY "@rx \x25" \
        "chain"
        SecRule REQUEST_BODY "@validateUrlEncoding" \
            "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.warning_anomaly_score}'"</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:52:38 UTC</span>

<span style="font-size: 90%;">I think I made a note about this in Budapest…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:16 UTC</span>

<span style="font-size: 90%;">It's by far the most offensive PL1 rule now. A factor of 8 above 932380.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:53:20 UTC</span>

<span style="font-size: 90%;">Oh yeah, that's right: the presence of a %</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:53:28 UTC</span>

<span style="font-size: 90%;">So "Stocks are up by 5%" causes problems</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:34 UTC</span>

<span style="font-size: 90%;">Apparently very similar to what we talked about before.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:54:27 UTC</span>

<span style="font-size: 90%;">I'll open an issue for that too. I hoped to do that already, but haven't yet.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:45 UTC</span>

<span style="font-size: 90%;">I think we can better with the chained rule, the \x25 ?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:53 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:55:08 UTC</span>

<span style="font-size: 90%;">Isn't that the same rule that we have another issue open for?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:55:22 UTC</span>

<span style="font-size: 90%;">Because of the URL validation / double decoding</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:50 UTC</span>

<span style="font-size: 90%;">I do not think it's the same rule.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:56:38 UTC</span>

<span style="font-size: 90%;">Are they siblings?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:38 UTC</span>

<span style="font-size: 90%;">No, nothing open according to my searching.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:43 UTC</span>

<span style="font-size: 90%;">But similar problem.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:54 UTC</span>

<span style="font-size: 90%;">920240 does not have siblings.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:57:16 UTC</span>

<span style="font-size: 90%;">You're right, it's 920220</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:57:40 UTC</span>

<span style="font-size: 90%;">It's similar</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:45 UTC</span>

<span style="font-size: 90%;">What about chaining the x25 with other hex stuff?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:58:17 UTC</span>

<span style="font-size: 90%;">Ah, yes: they've both "URL Encoding Abuse" rules. One checks REQUEST_URI, ther other checks REQUEST_BODY</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:21 UTC</span>

<span style="font-size: 90%;">% followed by whitespace or special chars should not be a problem and thus solve the "stocks are up 5%!" FP.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:58:23 UTC</span>

<span style="font-size: 90%;">The comment you wrote in the PR:
# There are two different chained rules, 920220 and 920240.
# We need to separate them as we are inspecting two
# different variables - REQUEST_URI_RAW and REQUEST_BODY - that
# need different treatment.
# For REQUEST_URI_RAW we want to inspect every request in phase 1.
# For REQUEST_BODY, we only want to inspect if the content-type
# is application/x-www-form-urlencoding and only in phase 2.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:54 UTC</span>

<span style="font-size: 90%;">What PR was that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:59:05 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3410](https://github.com/coreruleset/coreruleset/pull/3410)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:15 UTC</span>

<span style="font-size: 90%;">Ah, that one.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:22 UTC</span>

<span style="font-size: 90%;">Here we meet again, old friend.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:46 UTC</span>

<span style="font-size: 90%;">Worth noting, these are both "WARNING" level rules.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:56 UTC</span>

<span style="font-size: 90%;">Still causing FPs, but at warning level only.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:09 UTC</span>

<span style="font-size: 90%;">Oh, only anomaly score 4. Overlooked that.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:12 UTC</span>

<span style="font-size: 90%;">Most interesting.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:01:19 UTC</span>

<span style="font-size: 90%;">So... since they are both only warnings... skip them for v4?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:38 UTC</span>

<span style="font-size: 90%;">Good thinking, but let's talk a bit more about this.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:57 UTC</span>

<span style="font-size: 90%;">Am I right that we are not sure what the validateUrlEncoding really prevents here - again?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:03:01 UTC</span>

<span style="font-size: 90%;">It's the same case as in the other rule I believe. However, here it's clear: you don't normally use URL encoding in form-data requests, unless you're maybe trying to evade detection.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:03:57 UTC</span>

<span style="font-size: 90%;">No, that doesn't make sense...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:05 UTC</span>

<span style="font-size: 90%;">So why do we have that many FPs then?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:04:30 UTC</span>

<span style="font-size: 90%;">The rule validates that if there's a percent sign, then it must be valid URL encoding.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:31 UTC</span>

<span style="font-size: 90%;">Or is the script encoding the percent symbol, when a browser would not?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:04:51 UTC</span>

<span style="font-size: 90%;">This only makes sense to me if you're trying to prevent attacks against a decoder library.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:57 UTC</span>

<span style="font-size: 90%;">Now I am puzzled too.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:59 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:21 UTC</span>

<span style="font-size: 90%;">What do you think about the combination of the x25 as pointed out above: "% followed by whitespace or special chars should not be a problem and thus solve the "stocks are up 5%!" FP"</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:51 UTC</span>

<span style="font-size: 90%;">%0A should be detected though.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:08:06 UTC</span>

<span style="font-size: 90%;">But %0A would never be detected. It's a valid sequence</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:08:33 UTC</span>

<span style="font-size: 90%;">The rule only triggers on invalid sequences, which you would pretty much be excluding with your idea. So the rule becomes pointless</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:08:44 UTC</span>

<span style="font-size: 90%;">(it was pointless anyway, IMO)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:47 UTC</span>

<span style="font-size: 90%;">You have a point there.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:40 UTC</span>

<span style="font-size: 90%;">Which brings us back to the idea of kicking this rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:09:44 UTC</span>

<span style="font-size: 90%;">Honestly, I think both rules (as they are now), try to detect an application level evasion / attack. I don't think CRS should / can block that</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:50 UTC</span>

<span style="font-size: 90%;">Or at least make it PL2 and be done with it for v4.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:10:21 UTC</span>

<span style="font-size: 90%;">Does it matter what we do, if they only warn?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:47 UTC</span>

<span style="font-size: 90%;">Well, I run threshold 2 in production.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:08 UTC</span>

<span style="font-size: 90%;">And it fills your dashboard for FPs. So from a hygiene standpoint, I think it matters.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:11:16 UTC</span>

<span style="font-size: 90%;">That's true.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:34 UTC</span>

<span style="font-size: 90%;">But that need not be the policy of CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:54 UTC</span>

<span style="font-size: 90%;">But I would suggest to move it to PL2 in that case so at least PL1 is clean from its FPs.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:12:16 UTC</span>

<span style="font-size: 90%;">And open an issue to revisit dropping the rule?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:26 UTC</span>

<span style="font-size: 90%;">Yes, why not.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:09 UTC</span>

<span style="font-size: 90%;">(I see my burg log archive has a few hits on the rule. I'm currently grepping through 12GB of logs to find the exact payload.)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:45 UTC</span>

<span style="font-size: 90%;">Any volunteers?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:14:27 UTC</span>

<span style="font-size: 90%;">To open an issue or move it to PL2?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:38 UTC</span>

<span style="font-size: 90%;">Both. :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:14:40 UTC</span>

<span style="font-size: 90%;">Or drop the rule?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:14:54 UTC</span>

<span style="font-size: 90%;">I will open the issue anyway, if I have time I'll open a PR to move PL to 2</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:08 UTC</span>

<span style="font-size: 90%;">Move it to PL2 and then revisit when v4 is out and we still think it's a good idea.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:15:19 UTC</span>

<span style="font-size: 90%;">Or at least add to the issue "next step: we agree move to PL 2 and rethink in the future"</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:54 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:15 UTC</span>

<span style="font-size: 90%;">Summarizing the v4 issue situation, I think we are unsure about 932240 / issue [#3397](https://github.com/coreruleset/coreruleset/issues/#3397), but we see the light with most of the other stuff. 1-2 additional new FPs issues to be made and we need to get an overview of the remaining bypasses in the security tracker.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:17:16 UTC</span>

<span style="font-size: 90%;">I have a PR for moving the rule</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:31 UTC</span>

<span style="font-size: 90%;">Did I get the above right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:18:38 UTC</span>

<span style="font-size: 90%;">Sounds about right</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:12 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:33 UTC</span>

<span style="font-size: 90%;">So if there are no unpleasant surprises, we have a road to the release.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:00 UTC</span>

<span style="font-size: 90%;">This won't be between here and the 1st February meeting, but I think we can come up with tentative release planning.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:21 UTC</span>

<span style="font-size: 90%;">How about Wednesday, Feb 14th? There is still ample time, also for the admin / doc stuff. But good to have a date now.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:48 UTC</span>

<span style="font-size: 90%;">Anybody else? Everybody fell asleep in the meantime. :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:23:03 UTC</span>

<span style="font-size: 90%;">14 Feb for a release? Valentines Day?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:23:20 UTC</span>

<span style="font-size: 90%;">"Spend your Valentines with CRS v4.0 :kissing_closed_eyes:"</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:23:43 UTC</span>

<span style="font-size: 90%;">New poster!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:10 UTC</span>

<span style="font-size: 90%;">That was not my thinking when I looked at the calendar, but now that you bring it up ... :rose:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:43 UTC</span>

<span style="font-size: 90%;">That poster guy better get down to business now. He is postponing constantly. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:27:22 UTC</span>

<span style="font-size: 90%;">It's getting a bit late now. I do not think we need to pick a release manager tonight. Please speak up if you want to volunteer or if you think we should do that ahead of the Feb meeting (-> Monday Feb 5, 9 days before the release).</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:43 UTC</span>

<span style="font-size: 90%;">Apparently little interest in the job tonight. Then let's close the meeting. Thank you all for attending, this was a blast.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:28:58 UTC</span>

<span style="font-size: 90%;">Thanks. bb!</span>

**airween** <span style="color: grey; font-size: 90%;">21:29:13 UTC</span>

<span style="font-size: 90%;">good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:29:14 UTC</span>

<span style="font-size: 90%;">Night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">21:29:21 UTC</span>

<span style="font-size: 90%;">bye :wave:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:29:24 UTC</span>

<span style="font-size: 90%;">Night night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:30:00 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:30:10 UTC</span>

<span style="font-size: 90%;">Good night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:30:12 UTC</span>

<span style="font-size: 90%;">I tried to write down the decisions. I hope everything is correct, we jumped a bit between the topics... Please correct if I got something wrong:

[https://github.com/coreruleset/coreruleset/issues/3466#issuecomment-1904742398](https://github.com/coreruleset/coreruleset/issues/3466#issuecomment-1904742398)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:31:38 UTC</span>

<span style="font-size: 90%;">Thank you _@franbuehler_.</span>

