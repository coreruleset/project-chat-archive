### Mon, Jul 6th, 2020

**dune73** <span style="color: grey; font-size: 90%;">18:30:57 UTC</span>

<span style="font-size: 90%;">Hello _@Emile_, nice to have you here. Who else is attending?</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:05 UTC</span>

<span style="font-size: 90%;">I’m here!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:31:10 UTC</span>

<span style="font-size: 90%;">i’m also here</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:14 UTC</span>

<span style="font-size: 90%;">hi</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:18 UTC</span>

<span style="font-size: 90%;">hello everybody</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:25 UTC</span>

<span style="font-size: 90%;">somebody has to take the ass whooping for bugs in the release :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:59 UTC</span>

<span style="font-size: 90%;">Hello, hello. So nice to see old faces again. :wink:
Welcome _@csanders_!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:32:10 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:32:22 UTC</span>

<span style="font-size: 90%;">thank you, i’m very happy that i’m being welcomed back at all :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:00 UTC</span>

<span style="font-size: 90%;">Out monthly agenda is at [https://github.com/coreruleset/coreruleset/issues/1836](https://github.com/coreruleset/coreruleset/issues/1836)
Thank you _@fzipitria_ for creating the issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:30 UTC</span>

<span style="font-size: 90%;">If you look over it, you can see that it's quite full and it also looks like we are getting quite a few issues now with new ones almost on a daily rhythm.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:48 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:03 UTC</span>

<span style="font-size: 90%;">So let's kick it right off.</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:20 UTC</span>

<span style="font-size: 90%;">alright!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:30 UTC</span>

<span style="font-size: 90%;">So what do you make of 1781?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:49 UTC</span>

<span style="font-size: 90%;">Is this somethign we want? AFAIK it's not an official webdav method, or is it?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:19 UTC</span>

<span style="font-size: 90%;">But then it's a rule exclusion aimed at Nextcloud and if it uses that, we should exclude the alert.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:24 UTC</span>

<span style="font-size: 90%;">Merge?</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:56 UTC</span>

<span style="font-size: 90%;">interesting, I’ve never seen this construct but it’s looking good!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:57 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:11 UTC</span>

<span style="font-size: 90%;">it adds to the tx.allowed_methods but seemingly in a good way</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:34 UTC</span>

<span style="font-size: 90%;">OK. Let's merge then.</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:40 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:38:46 UTC</span>

<span style="font-size: 90%;">Merge, yes.</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:53 UTC</span>

<span style="font-size: 90%;">this is on v3.3 branch though</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:56 UTC</span>

<span style="font-size: 90%;">can we move it to v3.4?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:08 UTC</span>

<span style="font-size: 90%;">Glad you spotted. Could you take care of that?</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:31 UTC</span>

<span style="font-size: 90%;">I’ll ask the submitter to do it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:53 UTC</span>

<span style="font-size: 90%;">1786 is another edit on the CT header check. It could do with a test, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:35 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ could you have the contributer write one or do one yourself, then I guess we should simply merge it.
Or is there anything around that # character that tells us not to merge?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:51 UTC</span>

<span style="font-size: 90%;">I think it makes sense</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:02 UTC</span>

<span style="font-size: 90%;">Having that char</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:41:23 UTC</span>

<span style="font-size: 90%;">And also point the PR against v3.4</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:26 UTC</span>

<span style="font-size: 90%;">Plus the v3.3 problem</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:30 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:35 UTC</span>

<span style="font-size: 90%;">I'll ask for rebasing</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:40 UTC</span>

<span style="font-size: 90%;">great!</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:18 UTC</span>

<span style="font-size: 90%;">azurit is submitting a lot of nice PRs lately</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:19 UTC</span>

<span style="font-size: 90%;">1793 is a new rule sqli contributed by _@theMiddle_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:12 UTC</span>

<span style="font-size: 90%;">Yes, he is. I need to talk to him. He should add himself to the CONTRIBUTOR file under developer, I think. And start to join our chats, but that demand better waits until he has updated it.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:48 UTC</span>

<span style="font-size: 90%;">Anybody know where _@theMiddle_ is?</span>

**Emile** <span style="color: grey; font-size: 90%;">18:44:31 UTC</span>

<span style="font-size: 90%;">1793 look quite sensitive, if we want it to go to PL1, I would like to run it a bit to get an idea of the false positives to expect</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">18:45:50 UTC</span>

<span style="font-size: 90%;">:= should keep things under control but overwise, it’s a bit concerning</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:21 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:31 UTC</span>

<span style="font-size: 90%;">I think so too and it takes a bit more explanations from my point of view.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:41 UTC</span>

<span style="font-size: 90%;">Also, I do not see where the set variable comes in.</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:43 UTC</span>

<span style="font-size: 90%;">yes, we have a bit of a situation with FP detection… normally my rule was to put the rule in production for 2 weeks… but I find that my production sites use lots of exclusions (for APIs that receive json etc), so I’m probably seeing much fewer FPs than the “set-and-forget” CRS user</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:02 UTC</span>

<span style="font-size: 90%;">this seems to find a pattern like @foo = 3</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:04 UTC</span>

<span style="font-size: 90%;">The good thing: We are very early in the 3.4 cycle, so there is still time.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:33 UTC</span>

<span style="font-size: 90%;">Where is that pattern in the test, _@walter_?</span>

**Emile** <span style="color: grey; font-size: 90%;">18:46:59 UTC</span>

<span style="font-size: 90%;">I can run them on a very wide set of application, so it should get interesting data</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:22 UTC</span>

<span style="font-size: 90%;">_@dune73_ how do you mean? yeah it’s not in the test, good rules should have a lot of tests, also negative tests!</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:36 UTC</span>

<span style="font-size: 90%;">I think if we would be more strict on that, we’d have less “oopses”</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:56 UTC</span>

<span style="font-size: 90%;">_@Emile_: We have set our hopes on several companies doing exactly that in readonly mode and reporting back to us. So far no luck with somebody actually doing that outside of @Walter and _@theMiddle_ to a certain extent.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">18:49:07 UTC</span>

<span style="font-size: 90%;">If we can find a way to get a good feedback loop, that’d be a win-win from my/our point of view :slightly_smiling_face:</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">18:50:34 UTC</span>

<span style="font-size: 90%;">Formalizing this feedback and have people use this process would be a huge win for the project - and those admins thinking of the future release where it will be on by default.</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:58 UTC</span>

<span style="font-size: 90%;">it also shows a bit of the mind of the rule-writer</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:40 UTC</span>

<span style="font-size: 90%;">OK: So we want better documentation, better / more tests and the rule stays in PL2 kindergarden until it is proven to have only very few FPs. It can still be in PL1 for 3.4, but per default it goes to PL2.
OK?</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:58 UTC</span>

<span style="font-size: 90%;">really sounds like a good way to introduce a potentially scary rule</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:50:02 UTC</span>

<span style="font-size: 90%;">Sounds good!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:00 UTC</span>

<span style="font-size: 90%;">More opinions?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:30 UTC</span>

<span style="font-size: 90%;">Yeah, I like the approach</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:38 UTC</span>

<span style="font-size: 90%;">I would like to have tests also</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:16 UTC</span>

<span style="font-size: 90%;">Anticipating a later agenda item: The HTTP Working Group is asking us to consider the effect of new rules / updates on the HTTP protocol.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:49 UTC</span>

<span style="font-size: 90%;">Like: What will happen if 50 or 90% of the web uses this rule. How will browsers implement new features.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:31 UTC</span>

<span style="font-size: 90%;">The problem for browsers is twofold</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:35 UTC</span>

<span style="font-size: 90%;">I think this rule does not have any effect, but rules working with a positive security approach, namely on headers / request line are affecting that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:51 UTC</span>

<span style="font-size: 90%;">In the sense that they need to deal with these new rules</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:04 UTC</span>

<span style="font-size: 90%;">But also, many people has older versions of the CRS in prod</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:16 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:01 UTC</span>

<span style="font-size: 90%;">(which also should make us think in how do we get people updated sooner)</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:27 UTC</span>

<span style="font-size: 90%;">the best way would be to add amazing features often!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:30 UTC</span>

<span style="font-size: 90%;">That's another request of said group.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:45 UTC</span>

<span style="font-size: 90%;">But let's move on. It's scheduled later in the agenda.</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:53 UTC</span>

<span style="font-size: 90%;">I expect the big providers to be always slow though</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:58 UTC</span>

<span style="font-size: 90%;">but we could put up a page on our site</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">1806 deals with FPs.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">18:57:35 UTC</span>

<span style="font-size: 90%;">You wanted to test this rule or let it test by Verizon??</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:10 UTC</span>

<span style="font-size: 90%;">and have checkmarks and red crosses for uptodateness</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">18:56:54 UTC</span>

<span style="font-size: 90%;">would be a problem for forks that lower the sensitivity: they would be out of date but is that a bad thing?)</span>

↳ **walter** <span style="color: grey; font-size: 90%;">18:57:28 UTC</span>

<span style="font-size: 90%;">yeah you’re right it’s always more complex… but still the latest base version would be something I’d like to know before choosing a cloud WAF!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:46 UTC</span>

<span style="font-size: 90%;">(like [https://github.com/coreruleset/coreruleset/security/policy](https://github.com/coreruleset/coreruleset/security/policy)) ?</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:53 UTC</span>

<span style="font-size: 90%;">the only reason I am on a emergency project to upgrade all boxes to php 7.3, is that the wordpress panel has started to show a banner saying your php is insecure :rolling_on_the_floor_laughing:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:57:35 UTC</span>

<span style="font-size: 90%;">You wanted to test this rule or let it test by Verizon??</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">18:57:35 UTC</span>

<span style="font-size: 90%;">You wanted to test this rule or let it test by Verizon??</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:09 UTC</span>

<span style="font-size: 90%;">No response from Verizon. For several months. My 2 contacts don't respond.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:03 UTC</span>

<span style="font-size: 90%;">Maybe _@Emile_ and sqreen will do a better job. Ideally we would have a standartized process for this.</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:11 UTC</span>

<span style="font-size: 90%;">[#1806](https://github.com/coreruleset/coreruleset/issues/#1806) seems pretty good on the eye. had lots of HAVING fps in my time</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:35 UTC</span>

<span style="font-size: 90%;">I’m only not sure if SELECT is needed to exploit it…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:48 UTC</span>

<span style="font-size: 90%;">Am I reading the regex correctly, that you want to see SELECT before HAVING? (Sorry if this has been explained to me before)</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:00:42 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:54 UTC</span>

<span style="font-size: 90%;">if you have a partial query that you can inject to, maybe you can add HAVING id=1 in order to enumerate…</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:19 UTC</span>

<span style="font-size: 90%;">yes I think that is the main gist _@dune73_ if I’m correct</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:32 UTC</span>

<span style="font-size: 90%;">_@franbuehler_?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:20 UTC</span>

<span style="font-size: 90%;">I mean the message with the PR makes it pretty clear that SELECT is a necessary keyword going with HAVING. But I think Walter has a point.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:01:25 UTC</span>

<span style="font-size: 90%;">Mhh, I found out that having only makes sense with a select in front of it. But I'm not an sqli pro.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:37 UTC</span>

<span style="font-size: 90%;">On the plus side: A ton of welcome tests.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:34 UTC</span>

<span style="font-size: 90%;">I don't think we need tests here. It's a PR to avoid FP.
If we want to have it tested, we should ask an SQLi pro...??</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:49 UTC</span>

<span style="font-size: 90%;">like Andrea??</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:22 UTC</span>

<span style="font-size: 90%;">assign it to him for review and come back to it next month?</span>

**Emile** <span style="color: grey; font-size: 90%;">19:04:53 UTC</span>

<span style="font-size: 90%;">I’ll also run it a bit, but it appears to be solving the FPs we had :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:16 UTC</span>

<span style="font-size: 90%;">that’s one good thing!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:05:33 UTC</span>

<span style="font-size: 90%;">And the PR solves 2 issues :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:40 UTC</span>

<span style="font-size: 90%;">I looked up the rule on regex101. Clearer now for me. I'd be OK with merging. It think the sub-query argument of @Walter is too specfic here. One could say the same thing about other rules or the other OR groups of this one.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:06:00 UTC</span>

<span style="font-size: 90%;">Yeeeess, merge it :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:19 UTC</span>

<span style="font-size: 90%;">that is definitely true, and we have pretty good coverage of these issues already due to libinjection</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:40 UTC</span>

<span style="font-size: 90%;">So we merge it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:41 UTC</span>

<span style="font-size: 90%;">alright, let’s merge!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:28 UTC</span>

<span style="font-size: 90%;">1817 is brought to us by _@Emile_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:35 UTC</span>

<span style="font-size: 90%;">Another FP fix.</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:10 UTC</span>

<span style="font-size: 90%;">oh yeah this one</span>

**Emile** <span style="color: grey; font-size: 90%;">19:08:20 UTC</span>

<span style="font-size: 90%;">I tuned it down a lot which helped tremendously with the FP rate we experienced</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:23 UTC</span>

<span style="font-size: 90%;">I looked at it but put it aside a bit, because I’m a bit scared of lossing SQL syntax coverage</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:36 UTC</span>

<span style="font-size: 90%;">This is quite the change. Could you explain it a bit?</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:52 UTC</span>

<span style="font-size: 90%;">for instance, one might do truncate `tablename` , would that be covered still?</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:41 UTC</span>

<span style="font-size: 90%;">the pattern was ^[\W\d]+\s*?truncate\b but is now ^[\W\d]+\s*?truncate\s+\w+</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:54 UTC</span>

<span style="font-size: 90%;">I think this problem might only appear with truncate but would have to look at SQL documentation for a bit :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:27 UTC</span>

<span style="font-size: 90%;">we could just leave the truncate at the old pattern of course, but I’m willing to do a deeper check on this PR if wanted!</span>

**Emile** <span style="color: grey; font-size: 90%;">19:11:22 UTC</span>

<span style="font-size: 90%;">hum, the pattern for
[\d\W]\s+as\b\s*[\"'\`\w]+\s*\bfromused
[\"'\`\w]</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:51 UTC</span>

<span style="font-size: 90%;">Looking over it, I'm OK with 90% of the change, but there are some items where my regex foo is too weak on the quick and I'd like to know more.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:01 UTC</span>

<span style="font-size: 90%;">Probably too much to talk it through tonight.</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:14 UTC</span>

<span style="font-size: 90%;">exactly my feelings, shall we take it upon ourselves to totally flesh it out over the next month?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:25 UTC</span>

<span style="font-size: 90%;">Picking up @Walter volunteering: Can we assign it to you and you sort it out with _@Emile_?</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:36 UTC</span>

<span style="font-size: 90%;">yes sir!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:00 UTC</span>

<span style="font-size: 90%;">Thank you very much. And thanks for the welcome contribution and the many tests, Emile-Hugo.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:42 UTC</span>

<span style="font-size: 90%;">Which brings us to some  old friends in the PR department.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:07 UTC</span>

<span style="font-size: 90%;">I rad _@fgs_ agreed to work on the 758 revert again. Any news from the other two?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:58 UTC</span>

<span style="font-size: 90%;">I've asked allanrbo, but no news yet</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:20 UTC</span>

<span style="font-size: 90%;">He has left our planet and I do not think he will be back.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:26 UTC</span>

<span style="font-size: 90%;">Ouch</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:30 UTC</span>

<span style="font-size: 90%;">This PR needs a new foster parent.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:40 UTC</span>

<span style="font-size: 90%;">I think that 1663 should be a good addition</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:57 UTC</span>

<span style="font-size: 90%;">Oh definitely.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:11 UTC</span>

<span style="font-size: 90%;">I could make a new PR based on his work.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:25 UTC</span>

<span style="font-size: 90%;">Thanks _@franbuehler_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:08 UTC</span>

<span style="font-size: 90%;">That would be awesome. It's one hell of a PR. And was not it the one where we were also expecting performance issues? (Or was that another one from Allan?)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">I don't know!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">It would be in the comments.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:41 UTC</span>

<span style="font-size: 90%;">I remember the discussion, but have not read up on it tonight</span>

**Emile** <span style="color: grey; font-size: 90%;">19:17:54 UTC</span>

<span style="font-size: 90%;">Uh, that’s interesting… We’re using 920120 internally and our engine is RE2 o0</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:18:29 UTC</span>

<span style="font-size: 90%;">Ah, nvm, unsupported target, our tolling ignored it :sweat_smile:</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:18:50 UTC</span>

<span style="font-size: 90%;">I'm not surprised. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:25 UTC</span>

<span style="font-size: 90%;">1602 is _@theMiddle_ again. Let's say we give him another month...</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:00 UTC</span>

<span style="font-size: 90%;">I think this is the original issue that was superseded by his PR [#1783](https://github.com/coreruleset/coreruleset/issues/#1783)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:09 UTC</span>

<span style="font-size: 90%;">Ah, ok. So I delete my name again.</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:09 UTC</span>

<span style="font-size: 90%;">since we merged that, [#1602](https://github.com/coreruleset/coreruleset/issues/#1602) can be closed i think</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:30 UTC</span>

<span style="font-size: 90%;">the [#1783](https://github.com/coreruleset/coreruleset/issues/#1783) might still be a bit picky, so I’m hoping on not too many FP reports about it…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:40 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: @Walter was talking of a different PR.</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:48 UTC</span>

<span style="font-size: 90%;">oops sorry</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:20:39 UTC</span>

<span style="font-size: 90%;">I assign myself again and I'll see :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:18 UTC</span>

<span style="font-size: 90%;">haha good</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:19 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:25 UTC</span>

<span style="font-size: 90%;">don’t forget to set the milestone to 3.4.0!</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:36 UTC</span>

<span style="font-size: 90%;">if it doesn’t have a milestone 3.4.0, I won’t look at it for the release</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:50 UTC</span>

<span style="font-size: 90%;">assuming I have the humble role of release doofus again :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:55 UTC</span>

<span style="font-size: 90%;">And 1602 can be closed? I suggest we add a notice to 1602 and ask _@theMiddle_ to close</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:02 UTC</span>

<span style="font-size: 90%;">I think so yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:08 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:26 UTC</span>

<span style="font-size: 90%;">done</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:27 UTC</span>

<span style="font-size: 90%;">So we're done with the PRs, I guess. Which brings us to the "Other items".</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:37 UTC</span>

<span style="font-size: 90%;">yes, low number of PRs after a release always :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:56 UTC</span>

<span style="font-size: 90%;">It's a reasonable number I think.</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:58 UTC</span>

<span style="font-size: 90%;">relatively, that is. we’re still doing good with getting people to report problems!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:06 UTC</span>

<span style="font-size: 90%;">No need to add more than one new rule per month. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:14 UTC</span>

<span style="font-size: 90%;">at least we seem to.. we don’t know the base rate :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:25 UTC</span>

<span style="font-size: 90%;">Haha</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:05 UTC</span>

<span style="font-size: 90%;">So I reckon everybody understands how pleased that Walter and I am with _@csanders_ making a comeback in our monthly chat. It's been a while.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:24:15 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:24:27 UTC</span>

<span style="font-size: 90%;">i’m glad to be back</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:13 UTC</span>

<span style="font-size: 90%;">Walter and I have been feeling uneasy, but it took other members to get the ball rolling again and we are very happy Chaim heard the call. What have  you been up to since last Autumn?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:26:42 UTC</span>

<span style="font-size: 90%;">So since last Autumn i’ve both moved jobs, got married, and remained teaching</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:04 UTC</span>

<span style="font-size: 90%;">so i’ve had a VERY full load, additionally, I was running into some anti-compete stuff, which has since been sorted out</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:05 UTC</span>

<span style="font-size: 90%;">waov', impressive list :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:36 UTC</span>

<span style="font-size: 90%;">I’m going to be moving into more of a developer role on the project leaving _@dune73_ and _@walter_ in the co-lead positions</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:27:47 UTC</span>

<span style="font-size: 90%;">Write a book, plant a tree, kids. You tried all at once?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:14 UTC</span>

<span style="font-size: 90%;">My first goal is to bring the demo site to fruition - and II want to write some more capable rules around SSO</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:28:24 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:29 UTC</span>

<span style="font-size: 90%;">Very nice.</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:34 UTC</span>

<span style="font-size: 90%;">awesome</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:45 UTC</span>

<span style="font-size: 90%;">So you live in Seattle now and who do you work for?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:47 UTC</span>

<span style="font-size: 90%;">i’m super happy that all of you have been so patient, and also for _@dune73_ and _@walter_ for stepping up</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:57 UTC</span>

<span style="font-size: 90%;">I work for Okta (hence some SSO rules)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:29:15 UTC</span>

<span style="font-size: 90%;">I would say, it is real good to hear from you</span>

**csanders** <span style="color: grey; font-size: 90%;">19:29:17 UTC</span>

<span style="font-size: 90%;">and I still teach at RIT</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:01 UTC</span>

<span style="font-size: 90%;">Cool. Man.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:05 UTC</span>

<span style="font-size: 90%;">i was also contracting for some companies doing some WAF type stuff, but that is about as much as I can say about that area :confused:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:19 UTC</span>

<span style="font-size: 90%;">SOO rules, would that be stuff to protect session tickets, openid connect and such?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:34 UTC</span>

<span style="font-size: 90%;">s/SOO/SSO/</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:48 UTC</span>

<span style="font-size: 90%;">yes, II would love to add rules that check for signatures on SAML requests</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:30:48 UTC</span>

<span style="font-size: 90%;">we are talking about single sign on right?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:02 UTC</span>

<span style="font-size: 90%;">ensure that we don’t have XML signature wraapping or XXE</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:15 UTC</span>

<span style="font-size: 90%;">and then there are also a whole bunch of JSON OIDC validations that can be done</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:44 UTC</span>

<span style="font-size: 90%;">but those are some examples</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:47 UTC</span>

<span style="font-size: 90%;">That would be awesome indeed.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:12 UTC</span>

<span style="font-size: 90%;">but, my main goal is to be much more involved</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:34:19 UTC</span>

<span style="font-size: 90%;">Hi guys, Ive been long time offline but keep reading you from time to time, congrats for the latest release :)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:52 UTC</span>

<span style="font-size: 90%;">Just got a private DM from _@theMiddle_. He apologizes for not attending the meeting. He's very exhausted after a horrible day.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:35:02 UTC</span>

<span style="font-size: 90%;">heyho _@SpartanTri_</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:05 UTC</span>

<span style="font-size: 90%;">:heart: hope tomorrow is better</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:07 UTC</span>

<span style="font-size: 90%;">Is this like reunion night or what? Welcome _@SpartanTri_!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:35:25 UTC</span>

<span style="font-size: 90%;">looks like that</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">:D</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:36 UTC</span>

<span style="font-size: 90%;">:conga_party_parrot:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:36:09 UTC</span>

<span style="font-size: 90%;">I’m full trying to finish my master degree and getting up to speed on my new role</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:20 UTC</span>

<span style="font-size: 90%;">Is this a new party parrot _@fzipitria_ (asking for a friend)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:38 UTC</span>

<span style="font-size: 90%;">What is your exact job at AWS, _@SpartanTri_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:44 UTC</span>

<span style="font-size: 90%;">:conga_party_parrot:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:00 UTC</span>

<span style="font-size: 90%;">I’m Cloud infrastructure architect </span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:07 UTC</span>

<span style="font-size: 90%;">But you can search anything in [https://slackmojis.com/](https://slackmojis.com/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:08 UTC</span>

<span style="font-size: 90%;">Sounds impressive.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:15 UTC</span>

<span style="font-size: 90%;">How close is that to the WAF people?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:16 UTC</span>

<span style="font-size: 90%;">Professional services for public sector </span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:51 UTC</span>

<span style="font-size: 90%;">Not much yet but I plan to work with them on some ideas</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:00 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:30 UTC</span>

<span style="font-size: 90%;">I guess we better get going again. But it's definitely a special night to see two lost sons again. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">We are in bit of a situation with Trustwave again. _@airween_: Do you want to explain it, or should I make a brief summary?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:39:13 UTC</span>

<span style="font-size: 90%;">I’m just a bout to finish my master so hopefully will start coding again </span>

**walter** <span style="color: grey; font-size: 90%;">19:39:36 UTC</span>

<span style="font-size: 90%;">awesome!</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:46 UTC</span>

<span style="font-size: 90%;">yes, please make it shorter (than me :slightly_smiling_face:)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:01 UTC</span>

<span style="font-size: 90%;">Haha</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:45 UTC</span>

<span style="font-size: 90%;">OK. So _@airween_ and _@theMiddle_ have found another undocumented difference between ModSec2 and ModSec3.
It's a dead simple DoS thanks to one of our rules.</span>

**Slackbot** <span style="color: grey; font-size: 90%;">19:40:46 UTC</span>

<span style="font-size: 90%;">Bring out your dead! Bring out your dead!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:12 UTC</span>

<span style="font-size: 90%;">TW says it is not a security issues, but the expected behaviour or a regex engine.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:43 UTC</span>

<span style="font-size: 90%;">But they still merged a PR that fixes the behaviour, but naturally refuse to do a security release.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:12 UTC</span>

<span style="font-size: 90%;">The CVSS score is 7.5, HIGH, remote DoS with no victim interaction.</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:25 UTC</span>

<span style="font-size: 90%;">I think now I can share the video which demonstrates the behavior, but doesn't show the PoC</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:42:35 UTC</span>

<span style="font-size: 90%;">Which versions are affected?</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:37 UTC</span>

<span style="font-size: 90%;">_@dune73_ em I right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:41 UTC</span>

<span style="font-size: 90%;">Please send the link.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:43 UTC</span>

<span style="font-size: 90%;">This is for 3.x, right?</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:51 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ all v3 except which have the latest commit</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:52 UTC</span>

<span style="font-size: 90%;">All libmodsec3 versions are affected.</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:54 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">ModSec2 is not affected.</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">[https://www.dropbox.com/s/6qilx9f21lz7jy2/capture_932100.mp4](https://www.dropbox.com/s/6qilx9f21lz7jy2/capture_932100.mp4)</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:13 UTC</span>

<span style="font-size: 90%;">and the fix is out</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:36 UTC</span>

<span style="font-size: 90%;">and merged to master:
[https://github.com/SpiderLabs/ModSecurity/pull/2348](https://github.com/SpiderLabs/ModSecurity/pull/2348)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:45 UTC</span>

<span style="font-size: 90%;">Airween and the theMiddle think they would rather have the project handle this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:27 UTC</span>

<span style="font-size: 90%;">WOW</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:08 UTC</span>

<span style="font-size: 90%;">So what do we do? Do we make an announcement? Where? Do we inform the distributions? NGINX? Are we getting a CVE?
Are we ready  to go to war with TW over this (this is not necessarily a declaration of war, but it could be a step in that direction and we better assume it might before we take such a decision lightly)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:40 UTC</span>

<span style="font-size: 90%;">Well</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:14 UTC</span>

<span style="font-size: 90%;">they fixed it in master, but that doesn’t say they are doing a release.. for some reason that is very hard to get from them</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:32 UTC</span>

<span style="font-size: 90%;">I don’t have a problem publishing it</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:40 UTC</span>

<span style="font-size: 90%;">we could make a compatibility matrix for modsec versions</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:46 UTC</span>

<span style="font-size: 90%;">Final detail: Airween made it quite clear he really thinks this is a security thing and the arguments brought forward by TW are not convincing. If we give in (again), this will feel as they are always getting their way - which is certainly not fair to Airween and theMiddle who are going way out of their way to help them.</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:58 UTC</span>

<span style="font-size: 90%;">with a small description of the issues based on which we discourage some versions</span>

**Emile** <span style="color: grey; font-size: 90%;">19:47:25 UTC</span>

<span style="font-size: 90%;">Unless they’re planning to go public with it, we can go with a 90 days time for diplomatic purposes then put out a non-specific announcement</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:47:56 UTC</span>

<span style="font-size: 90%;">“Significant vulnerability in a feature CRS uses, we strongly recommend update, remote DoS”</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:28 UTC</span>

<span style="font-size: 90%;">The problem resides in that there is no version</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:53 UTC</span>

<span style="font-size: 90%;">TW first answer was this:
In terms of this behavior being used to cause DoS, this heavily depends on the machine's hardware, but our investigations show that you would need a very large number of requests that are also very large in size (depending on the rule you are attempting to attack) in order to stress the engine enough to produce a DoS. (emphasis by myself)</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:48:36 UTC</span>

<span style="font-size: 90%;">wtf</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">yeah :smile:</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">19:49:41 UTC</span>

<span style="font-size: 90%;">this seems to only be a mitigation not actually saying its not a security issue</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:53:43 UTC</span>

<span style="font-size: 90%;">_@csanders_: yes, we think it too</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:56 UTC</span>

<span style="font-size: 90%;">yes we would then discommend(?) the latest modsec 3.0.4 and basically only leave 2.9.3 as recommended :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:15 UTC</span>

<span style="font-size: 90%;">The problem with the 90 days is for them it's not even a security issue.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:49:18 UTC</span>

<span style="font-size: 90%;">That’s why I’m saying for diplomatic purposes, if you want to make sure we don’t go to war</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:50:03 UTC</span>

<span style="font-size: 90%;">If everybody is aligned with “we disagree on our assessment”, then we can go public without risk</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">is that true though do you need so many requests?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:49:44 UTC</span>

<span style="font-size: 90%;">what does it mean "so many"?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:49:53 UTC</span>

<span style="font-size: 90%;">I tried with 10 paralell request</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:50:32 UTC</span>

<span style="font-size: 90%;">thanks. that’s not much!</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">yeah</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:28 UTC</span>

<span style="font-size: 90%;">Walter: We're getting to that shortly in the agenda.</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:33 UTC</span>

<span style="font-size: 90%;">oops</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:44 UTC</span>

<span style="font-size: 90%;">what does it mean "so many"?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:49:44 UTC</span>

<span style="font-size: 90%;">what does it mean "so many"?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:49:53 UTC</span>

<span style="font-size: 90%;">I tried with 10 paralell request</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:50:32 UTC</span>

<span style="font-size: 90%;">thanks. that’s not much!</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">yeah</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:01 UTC</span>

<span style="font-size: 90%;">well, TW is saying that you would need a very large number of requests that are also very large in size</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:50:09 UTC</span>

<span style="font-size: 90%;">[Https://cveform.mitre.org/](Https://cveform.mitre.org/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:11 UTC</span>

<span style="font-size: 90%;">It takes very little to hose a server. This is a DoS not a DDoS.</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:17 UTC</span>

<span style="font-size: 90%;">ack</span>

**airween** <span style="color: grey; font-size: 90%;">19:51:09 UTC</span>

<span style="font-size: 90%;">one more very important fact: on the video, all components installed with default config: nginx, libmodsecurity, and CRS is on PL1</span>

**Emile** <span style="color: grey; font-size: 90%;">19:51:09 UTC</span>

<span style="font-size: 90%;">I think this need to be public, and they won’t do it. The rest is mostly a matter of semantic and politics :neutral_face:</span>

**Emile** <span style="color: grey; font-size: 90%;">19:52:01 UTC</span>

<span style="font-size: 90%;">I’m not clear on what impact can TW have on CRS. Isn’t it widely more used than modsecurity itself?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:04 UTC</span>

<span style="font-size: 90%;">I read that you guys would definitely want to publish this.</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:23 UTC</span>

<span style="font-size: 90%;">I think TW should be so happy with people reporting these!</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:25 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_: _@dune73_ helped me to create the report, here is that:
[https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H&version=3.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H&version=3.1)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:09 UTC</span>

<span style="font-size: 90%;">So we can basically go out now / soon. Or we wait the full 90 days to make sure they can not complain. We can do it in a minimal way, or we can go full out to make sure users really hear the call.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:14 UTC</span>

<span style="font-size: 90%;">What are your feelings?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:34 UTC</span>

<span style="font-size: 90%;">(I think we're like 20 days into the process.)</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:43 UTC</span>

<span style="font-size: 90%;">_@csanders_: yes, we think it too</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:48:36 UTC</span>

<span style="font-size: 90%;">wtf</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">yeah :smile:</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">19:49:41 UTC</span>

<span style="font-size: 90%;">this seems to only be a mitigation not actually saying its not a security issue</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:53:43 UTC</span>

<span style="font-size: 90%;">_@csanders_: yes, we think it too</span>

**Emile** <span style="color: grey; font-size: 90%;">19:53:44 UTC</span>

<span style="font-size: 90%;">I’d say ignoring the delay, start getting in touch with prominent users</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:00 UTC</span>

<span style="font-size: 90%;">i’d always say wait the 90 days to preserve the relationship</span>

**Emile** <span style="color: grey; font-size: 90%;">19:54:02 UTC</span>

<span style="font-size: 90%;">Once they updated, go public</span>

**airween** <span style="color: grey; font-size: 90%;">19:54:30 UTC</span>

<span style="font-size: 90%;">_@Emile_ - same here</span>

**Emile** <span style="color: grey; font-size: 90%;">19:54:44 UTC</span>

<span style="font-size: 90%;">There is a decent chance getting large users to update actually get us to 90 days :bowtie:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:54:47 UTC</span>

<span style="font-size: 90%;">Keep a communication timeline, and send friendly reminders </span>

**airween** <span style="color: grey; font-size: 90%;">19:55:21 UTC</span>

<span style="font-size: 90%;">today TW replied me again, and confirmed they don't want to handle this as security issue</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:45 UTC</span>

<span style="font-size: 90%;">Once more, we do not consider this a security issue, as for the implemented behaviour change- the PR can be found here [https://github.com/SpiderLabs/ModSecurity/pull/2348/commits/b9620c26a0ceaa23d2d7876718586f969f01168f](https://github.com/SpiderLabs/ModSecurity/pull/2348/commits/b9620c26a0ceaa23d2d7876718586f969f01168f) and you're both welcome and encouraged to test it against CRS and make sure the changes don't negatively affect any of the rules.</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:48 UTC</span>

<span style="font-size: 90%;">ouch, well then we should just put out a (somewhat generous) timeline and publish it!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:55 UTC</span>

<span style="font-size: 90%;">I read the PR again. I think it is relatively discreet and does not give a way the problem to potential attackers unless the reader really pays attention.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:10 UTC</span>

<span style="font-size: 90%;">So that speaks against a rush as well.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:57:51 UTC</span>

<span style="font-size: 90%;">there are 120 people on this channel though :grimacing:</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:58:33 UTC</span>

<span style="font-size: 90%;">That is correct. But we decided to discuss it hear with the community, because it really affects the community.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:59:49 UTC</span>

<span style="font-size: 90%;">I agree, but my point is that I don’t believe a lot in the argument of “nobody will notice so we can take our time” once it’s out on a fairly public forum</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:25 UTC</span>

<span style="font-size: 90%;">at last Autumn, there was an another DoS issue, what I found, and _@theMiddle_ made a PoC for that. Then TW asked us, they need 90 days to fix the bug and publish it</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:56:31 UTC</span>

<span style="font-size: 90%;">Do you have some details on what this relationship is? I’m fairly new to the projet</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:57:25 UTC</span>

<span style="font-size: 90%;">at last Autumn, there was an another DoS issue, what I found, and _@theMiddle_ made a PoC for that. Then TW asked us, they need 90 days to fix the bug and publish it</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">19:58:01 UTC</span>

<span style="font-size: 90%;">the relationship has always been a strained one between TW who is an important contributor to ModSec and CRS who are the primary ussers</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:45 UTC</span>

<span style="font-size: 90%;">Not so nice from TW: Airween and theMiddle have not received any credit in the Changelog (so far).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:09 UTC</span>

<span style="font-size: 90%;">If we do a timeline and they think it's not an issue worthy of a security release, it would be very pressuring to ask them to publish in less than 90 days, would not it?
Also: We're getting into the same "We're only doing a 3.1, not a 3.0.x release" I am sure.</span>

**Emile** <span style="color: grey; font-size: 90%;">20:00:47 UTC</span>

<span style="font-size: 90%;">distros are used to pulling commits though, no?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:02:42 UTC</span>

<span style="font-size: 90%;">No. I'm Debian Maintainer (eg. libmodsecurity3), but we can't fix it without CVE...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:09 UTC</span>

<span style="font-size: 90%;">_@Emile_ They are not overly active with regards to ModSec.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:20 UTC</span>

<span style="font-size: 90%;">And most have a security-release only policy.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">So the decision by TW is really grave and if they combine it with a 3.1 only release, then most people are just f***ed.</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">so, I was not sure this is a security issue and thought may be it's not important to notice the users. But now as I see your comments this is it.

TW said we can continue it as public, and released the fix - should we wait for anything?</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:42 UTC</span>

<span style="font-size: 90%;">No. I'm Debian Maintainer (eg. libmodsecurity3), but we can't fix it without CVE...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:02:42 UTC</span>

<span style="font-size: 90%;">No. I'm Debian Maintainer (eg. libmodsecurity3), but we can't fix it without CVE...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:49 UTC</span>

<span style="font-size: 90%;">TW did not say, we can publish. Or did they?
They just said they will not.
This implies they would prefer if we would keep quiet too.</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:34 UTC</span>

<span style="font-size: 90%;">With that, further discussions about implementation can go back to the usual public channels where they belong.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:38 UTC</span>

<span style="font-size: 90%;">I would assume they want us to keep it quiet but as airween mentioned, if this needs a CVE to be fixed, then we should go forward with 90 days disclosure via CVE - IMHO</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:32 UTC</span>

<span style="font-size: 90%;">Yes, the more I think about it, let's wait out the standard time-frame, but make it big.
And also reserve the right to go out faster if exploits start to appear in the wild.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:49 UTC</span>

<span style="font-size: 90%;">if exploits start appearing, all bets are off</span>

**Emile** <span style="color: grey; font-size: 90%;">20:05:27 UTC</span>

<span style="font-size: 90%;">Once exploits start appearing, it’s too late :neutral_face:</span>

**Emile** <span style="color: grey; font-size: 90%;">20:06:22 UTC</span>

<span style="font-size: 90%;">I’m not a fan of giving 90 days if there is not a social contract between both parties</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:24 UTC</span>

<span style="font-size: 90%;">yeah, and I'm a bit afraid if somebody checks the fix, then it's easy to make any exploit</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:33 UTC</span>

<span style="font-size: 90%;">That is the problem with the 90 days. But honestly, if you want to run a DoS against ModSec, this is just one of many options. It's a simple one, but there are alternative.</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:23 UTC</span>

<span style="font-size: 90%;">I think I have to go, I’m feeling very sleepy and my effective output is nosediving…</span>

**Emile** <span style="color: grey; font-size: 90%;">20:09:24 UTC</span>

<span style="font-size: 90%;">So basically: we can’t do anything until there is a version to update to, and TW doesn’t want to release before 3.1. Is there a timeline on this?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:38 UTC</span>

<span style="font-size: 90%;">_@airween_ and _@Emile_: it goes without saying that I would prefer to be faster. But we are doing a dance here with a somewhat unwilling partner. This influences the timeline / development. In an ideal situation, it would be a partnership with mutual agreement. TW behaves in a way that makes it non-ideal. We can force it our way, but I do not think it is in our best interest and that of our users in the long run.
Or in other words: I'd rather avoid to go to war.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:11:19 UTC</span>

<span style="font-size: 90%;">There is a difference between putting pressure and going to war, no? They’re an influential library to run CRS but without CRS, they’re useless</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:11:59 UTC</span>

<span style="font-size: 90%;">not really, TW has own ruleset</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:20:34 UTC</span>

<span style="font-size: 90%;">so from this point of view we are competitors :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:45 UTC</span>

<span style="font-size: 90%;">Bye Walter and thank you for attending.</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:46 UTC</span>

<span style="font-size: 90%;">I don’t think TW can put out a credible timeline already</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:56 UTC</span>

<span style="font-size: 90%;">It has to be our timeline.</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:15 UTC</span>

<span style="font-size: 90%;">_@dune73_ true!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:16 UTC</span>

<span style="font-size: 90%;">Bye Walter, good night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:35 UTC</span>

<span style="font-size: 90%;">bye everyone and feel free to assign some issue to me for the month, not the hardest one please ;)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:41 UTC</span>

<span style="font-size: 90%;">Good night Walter!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:10:58 UTC</span>

<span style="font-size: 90%;">good night</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:22 UTC</span>

<span style="font-size: 90%;">Hmm. We do not have agreement on the timeline it seems.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:10 UTC</span>

<span style="font-size: 90%;">_@airween_: Can you live with 90 days or do you insist to be faster? (Hint :wink: : You said it was the project's job to deal with it)</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:51 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**airween** <span style="color: grey; font-size: 90%;">20:13:39 UTC</span>

<span style="font-size: 90%;">I can live with 90 days or more, but I don't see the reason why we have to wait.</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:25 UTC</span>

<span style="font-size: 90%;">I don't use libmodsec3 anywhere, so I'm not affected :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:28 UTC</span>

<span style="font-size: 90%;">My reason is: I do not want to give TW any excuse to be mad with us. Not waiting 90 days allows them to cry foul.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:43 UTC</span>

<span style="font-size: 90%;">If you agree to wait out the full grace period (unless exploits in the wild), I'll send the timeline to TW on Wednesday and we can then reserve the CVE and start to draft a plan for the publication and how we warn distros in time.</span>

**airween** <span style="color: grey; font-size: 90%;">20:16:18 UTC</span>

<span style="font-size: 90%;">right, thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:52 UTC</span>

<span style="font-size: 90%;">Thank you man. And sorry for being so reluctant. It takes an awful lot of time, but the last two times, we had it our way in the end.</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:14 UTC</span>

<span style="font-size: 90%;">just one more question: when started/starts the 90 days? I reported this issue 15th of June, so 3 weeks ago</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:27 UTC</span>

<span style="font-size: 90%;">That's when the timeline started.</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:32 UTC</span>

<span style="font-size: 90%;">okay</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:52 UTC</span>

<span style="font-size: 90%;">So we are looking at September 13, are not we?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:06 UTC</span>

<span style="font-size: 90%;">That would be a Monday.</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:32 UTC</span>

<span style="font-size: 90%;">right</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:47 UTC</span>

<span style="font-size: 90%;">yes!</span>

**Emile** <span style="color: grey; font-size: 90%;">20:18:49 UTC</span>

<span style="font-size: 90%;">I mean, it’s going to depend on distros & users ultimately, no?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:50 UTC</span>

<span style="font-size: 90%;">Wow. Time flies. Shall we move to the next issue?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:18:57 UTC</span>

<span style="font-size: 90%;">yeah :stuck_out_tongue:</span>

**airween** <span style="color: grey; font-size: 90%;">20:19:09 UTC</span>

<span style="font-size: 90%;">thanks guys!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:25 UTC</span>

<span style="font-size: 90%;">_@fzipitria_:  Can you cover the migration of the other projects?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:31 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:35 UTC</span>

<span style="font-size: 90%;">"Cover" in the sense of presenting it here?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:50 UTC</span>

<span style="font-size: 90%;">Ok</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:56 UTC</span>

<span style="font-size: 90%;">Give me 10 :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:22 UTC</span>

<span style="font-size: 90%;">10 min?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:27 UTC</span>

<span style="font-size: 90%;">5'</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:45 UTC</span>

<span style="font-size: 90%;">Then let's move to next of Airweens initiatives and we return afterwards.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:51 UTC</span>

<span style="font-size: 90%;">Yes , thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:27 UTC</span>

<span style="font-size: 90%;">There is a new wiki page with a collection of issues of ModSec3 that prevents ModSec3 from passing our unit tests.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">The link, Airweens wiki page is not public</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:01 UTC</span>

<span style="font-size: 90%;">Brief summary:
</span>

**airween** <span style="color: grey; font-size: 90%;">20:22:02 UTC</span>

<span style="font-size: 90%;">(note, that page isn't public yet - if anybody wants to see that, let me know, and I'll give acces for that)</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:22:55 UTC</span>

<span style="font-size: 90%;">Yes, please :slightly_smiling_face:</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:25:39 UTC</span>

<span style="font-size: 90%;">Also interested please :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:22:07 UTC</span>

<span style="font-size: 90%;">He asked me for help, but I never responded, sorry for that, Airween :disappointed:</span>

**airween** <span style="color: grey; font-size: 90%;">20:22:17 UTC</span>

<span style="font-size: 90%;">no problem :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:22 UTC</span>

<span style="font-size: 90%;">PFB-4 expands to half a dozen sub-items.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:50 UTC</span>

<span style="font-size: 90%;">The list is very thorough with a lot of infos like a list of all the rules/tests that fail because of it.</span>

**airween** <span style="color: grey; font-size: 90%;">20:22:53 UTC</span>

<span style="font-size: 90%;">yes, there are several parser issues under one item, it needs to split into more items</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:33 UTC</span>

<span style="font-size: 90%;">Under the line the wiki page is very painful for TW and it will serve as base to declare at ModSec3 is not fit for production use (30 months after TW declared it ready for production use).</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:53 UTC</span>

<span style="font-size: 90%;">Ohh, another TW issue :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:09 UTC</span>

<span style="font-size: 90%;">A PR or an issue is linked where that exists.</span>

**airween** <span style="color: grey; font-size: 90%;">20:24:38 UTC</span>

<span style="font-size: 90%;">and meanwhile I found new issue: there are few unimplemented actions... :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:50 UTC</span>

<span style="font-size: 90%;">And we think this information should be published. And I'd rather not wait out the full 90 days.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:02 UTC</span>

<span style="font-size: 90%;">Important actions? Or the bitshifting stuff?</span>

**airween** <span style="color: grey; font-size: 90%;">20:25:20 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ invitation had been sent</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:26:11 UTC</span>

<span style="font-size: 90%;">Thank you, got it!</span>

**airween** <span style="color: grey; font-size: 90%;">20:25:36 UTC</span>

<span style="font-size: 90%;">expirevar , and 2 ctl actions</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:15 UTC</span>

<span style="font-size: 90%;">At least we are not directly affected.</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:19 UTC</span>

<span style="font-size: 90%;">_@Emile_ - sent</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:37 UTC</span>

<span style="font-size: 90%;">CRS contains all of them</span>

**airween** <span style="color: grey; font-size: 90%;">20:27:19 UTC</span>

<span style="font-size: 90%;">have to investigate what their absence results from</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:22 UTC</span>

<span style="font-size: 90%;">So this is just for your info what we are coming up with.
As long as we lived under the TW repo, we really kept our calm, but it's now time to come out and stop the madness with TW.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:15 UTC</span>

<span style="font-size: 90%;">They are not putting security and their users first and we have to make this transparent, I think.</span>

**airween** <span style="color: grey; font-size: 90%;">20:28:51 UTC</span>

<span style="font-size: 90%;">ctl:auditEngine and ctl:forceRequestBodyVariable are missing</span>

**csanders** <span style="color: grey; font-size: 90%;">20:29:14 UTC</span>

<span style="font-size: 90%;">urgh the CTL ones are used in a lot of custom stuff too</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:29:51 UTC</span>

<span style="font-size: 90%;">yes, they looks like not-an-important-actions, but they are</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:30:28 UTC</span>

<span style="font-size: 90%;">for us they are very important</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:30:52 UTC</span>

<span style="font-size: 90%;">yeah, I can see...</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">20:31:35 UTC</span>

<span style="font-size: 90%;">I use ctl:auditEngine on a bunch of honeypots</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:32:22 UTC</span>

<span style="font-size: 90%;">the problem is that libmodsec3 engine eats the config, but the code points to an empty function. It does nothing... silently...</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:32:47 UTC</span>

<span style="font-size: 90%;">we use it for geoip stuff to switch between detectiononly and on...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:35 UTC</span>

<span style="font-size: 90%;">Is the 2nd one really needed with  the way ModSec3 behaves?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:30:19 UTC</span>

<span style="font-size: 90%;">don't know - have to investigate</span>

**airween** <span style="color: grey; font-size: 90%;">20:29:51 UTC</span>

<span style="font-size: 90%;">yes, they looks like not-an-important-actions, but they are</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:29:51 UTC</span>

<span style="font-size: 90%;">yes, they looks like not-an-important-actions, but they are</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:30:28 UTC</span>

<span style="font-size: 90%;">for us they are very important</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:30:52 UTC</span>

<span style="font-size: 90%;">yeah, I can see...</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">20:31:35 UTC</span>

<span style="font-size: 90%;">I use ctl:auditEngine on a bunch of honeypots</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:32:22 UTC</span>

<span style="font-size: 90%;">the problem is that libmodsec3 engine eats the config, but the code points to an empty function. It does nothing... silently...</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:32:47 UTC</span>

<span style="font-size: 90%;">we use it for geoip stuff to switch between detectiononly and on...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:04 UTC</span>

<span style="font-size: 90%;">So I guess we have you in the boat to publish this page and continue to maintain it under our project.</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:28 UTC</span>

<span style="font-size: 90%;">right - I need few days, and I'll finish it. Any help are welcome :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">I'll gladly look over it when you are done _@airween_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:45 UTC</span>

<span style="font-size: 90%;">@fzip: You ready?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:50 UTC</span>

<span style="font-size: 90%;">2'</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:52 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:58 UTC</span>

<span style="font-size: 90%;">Haha.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:33:07 UTC</span>

<span style="font-size: 90%;">Call with my boss</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:33:12 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:20 UTC</span>

<span style="font-size: 90%;">_@Emile_ Can you jump in with your plans?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:33:23 UTC</span>

<span style="font-size: 90%;">Yep</span>

**Emile** <span style="color: grey; font-size: 90%;">20:34:27 UTC</span>

<span style="font-size: 90%;">So, the role the WAF play in our product is a little different from usual. We have other layers more focused toward protections and thus our approach to what WAF patterns are acceptable and which are not is quite biased against false positives</span>

**Emile** <span style="color: grey; font-size: 90%;">20:35:27 UTC</span>

<span style="font-size: 90%;">One problem we had working with CRS was that PL1 is designed to be quite a bit more agressive than what we’re comfortable with. We requalified the PL1 level on our trafic and ended up providing our users a safer, smaller subset</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:36:12 UTC</span>

<span style="font-size: 90%;">Ok, done</span>

**Emile** <span style="color: grey; font-size: 90%;">20:36:12 UTC</span>

<span style="font-size: 90%;">the problem is that this subset is hard to maintain and generally hard to modify whle staying in sync with CRS</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:36:51 UTC</span>

<span style="font-size: 90%;">have you tried with the msc_pyparser? :smile:</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:38:50 UTC</span>

<span style="font-size: 90%;">A colleague wrote the import script so maybe :stuck_out_tongue: The problem really are the forks</span>

**Emile** <span style="color: grey; font-size: 90%;">20:36:40 UTC</span>

<span style="font-size: 90%;">the idea is that this safer ruleset is actually likely interesting to other users of CRS</span>

**Emile** <span style="color: grey; font-size: 90%;">20:36:44 UTC</span>

<span style="font-size: 90%;">(a PL0 level)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:44 UTC</span>

<span style="font-size: 90%;">ISPs have reported similar problems (not surprisingly), so I think this could be interesting in general.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:59 UTC</span>

<span style="font-size: 90%;">EIther as an ISP Exclusions pack - or as a PL0.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:38:00 UTC</span>

<span style="font-size: 90%;">Sounds interesting!</span>

**Emile** <span style="color: grey; font-size: 90%;">20:38:04 UTC</span>

<span style="font-size: 90%;">This level would basically inherit from PL1, but be smaller and sometimes tweak the regex (for instance [https://github.com/coreruleset/coreruleset/pull/1817](https://github.com/coreruleset/coreruleset/pull/1817))</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:22 UTC</span>

<span style="font-size: 90%;">Since we are the beginning of a new cycle, it's a very good moment to get going with such an endeavour, I think.</span>

**Emile** <span style="color: grey; font-size: 90%;">20:40:19 UTC</span>

<span style="font-size: 90%;">I’d say the big problem would be figuring out how to tune down some good rules from PL1 to PL0 while keeping them maintainable (improvements to PL1 propagate to PL)</span>

**Emile** <span style="color: grey; font-size: 90%;">20:41:30 UTC</span>

<span style="font-size: 90%;">the alternative from our PoV is a complete fork, but that’s a loose-loose situation :disappointed:</span>

**Emile** <span style="color: grey; font-size: 90%;">20:42:34 UTC</span>

<span style="font-size: 90%;">so yeah, curious about what you thought about the idea, if you had any suggestion, etc… :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:08 UTC</span>

<span style="font-size: 90%;">Please don't fork. It's much better to try and address these problems within the project. I also think these are needs that are perfectly in line with the general policies of the project. It really depends on the security appetite of a service and if you are a hoster, I understand that you fear FPs like the devil fears holy water (not sure you can say this in English, you I guess you get the idea).</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:43:52 UTC</span>

<span style="font-size: 90%;">yeah :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:43 UTC</span>

<span style="font-size: 90%;">We're definitely need to sort out some policy questions.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:10 UTC</span>

<span style="font-size: 90%;">Like the maintenance you mentioned, rule IDs, strict siblings etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:11 UTC</span>

<span style="font-size: 90%;">Any ideas / opinions or are you all already exhaused?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:17 UTC</span>

<span style="font-size: 90%;">exhausted</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:34 UTC</span>

<span style="font-size: 90%;">This is a good one.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:41 UTC</span>

<span style="font-size: 90%;">I would say the same: don't fork</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:57 UTC</span>

<span style="font-size: 90%;">Let's try to figure it out what can be done for that PL0</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:46:08 UTC</span>

<span style="font-size: 90%;">I'm pretty sure technically it could be solved</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:12 UTC</span>

<span style="font-size: 90%;">I like the idea of a PL0.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:32 UTC</span>

<span style="font-size: 90%;">Or of having no false positives...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:00 UTC</span>

<span style="font-size: 90%;">Yes, the idea has been around, but there was never somebody who really wanted to actually do the heavy lifting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:25 UTC</span>

<span style="font-size: 90%;">I see a lot of interest for this (-> cpanel!)</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:47:32 UTC</span>

<span style="font-size: 90%;">there will be always FPs</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:47:50 UTC</span>

<span style="font-size: 90%;">yep, but we can drive them down a lot</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:47:57 UTC</span>

<span style="font-size: 90%;">and I have the data to back this up</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:50:32 UTC</span>

<span style="font-size: 90%;">but then you definetly need to turn off forceRequestBodyVariable 901340</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:53:10 UTC</span>

<span style="font-size: 90%;">we run in a different context, inside the application. The body being parsed is table stake for us :sweat_smile:</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:53:28 UTC</span>

<span style="font-size: 90%;">but not too many rules are actually sensitive to free text</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:55:23 UTC</span>

<span style="font-size: 90%;">well, we are a hoster too and noticed that a PUT method doesn't like that rule at all...</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:55:29 UTC</span>

<span style="font-size: 90%;">but sounds good</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:56:28 UTC</span>

<span style="font-size: 90%;">we’re not a hoster actually</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:57:06 UTC</span>

<span style="font-size: 90%;">We’re a SaaS company providing a micro-agent running inside our users applications and protecting them from the inside</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:57:07 UTC</span>

<span style="font-size: 90%;">[https://www.sqreen.com](https://www.sqreen.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:05 UTC</span>

<span style="font-size: 90%;">Don't spoil the good vibes, here, _@emphazer_. :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:48 UTC</span>

<span style="font-size: 90%;">I reckon it's a 80:20,or rather 98:2 thing. Like when we introduced the PL2-4 with v3.0.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:27 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:42 UTC</span>

<span style="font-size: 90%;">Moving over to _@fzipitria_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:19 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:31 UTC</span>

<span style="font-size: 90%;">So, now that we already migrated the main repo, we should be consolidating projects hosted in CRS-support to the coreruleset umbrella:

* ftw
* modsecurity-docker
* modsecurity-crs-docker
* secrules_parsing
* modsecurity-ansible-role
* owasp-crs-documentation

We should migrate those directly to the new organization, maybe _@csanders_ can be part of this one :)

This may imply some changes in the published things we have on dockerhub and/or pypi</span>

**csanders** <span style="color: grey; font-size: 90%;">20:51:51 UTC</span>

<span style="font-size: 90%;">yeah that sounds good</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:02 UTC</span>

<span style="font-size: 90%;">i can mmigrate those in the next few hours</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:09 UTC</span>

<span style="font-size: 90%;">Cool</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:15 UTC</span>

<span style="font-size: 90%;">i’ll start now</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:20 UTC</span>

<span style="font-size: 90%;">We should to the proper migration</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:25 UTC</span>

<span style="font-size: 90%;">(the one from github)</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:31 UTC</span>

<span style="font-size: 90%;">yup :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:35 UTC</span>

<span style="font-size: 90%;">That would redirect users there</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:42 UTC</span>

<span style="font-size: 90%;">it may break things temporarily but it really shouldn’t break too much</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:48 UTC</span>

<span style="font-size: 90%;">Also, I've created subgroups in the main organization</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:50 UTC</span>

<span style="font-size: 90%;">and if we do the proper one, things still work 99% of the time</span>

**csanders** <span style="color: grey; font-size: 90%;">20:52:55 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ i’ll PM you</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:56 UTC</span>

<span style="font-size: 90%;">So we can deal with permissions</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:53:03 UTC</span>

<span style="font-size: 90%;">Cool!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:53:37 UTC</span>

<span style="font-size: 90%;">Now your feedback from the HTTP WG _@dune73_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:55 UTC</span>

<span style="font-size: 90%;">OK.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:24 UTC</span>

<span style="font-size: 90%;">So following our merge of a rule adding some whitelisting to the cache request header, the HTTP Working Group approached us and asked us to refrain from this.
It seems we hit a sore spot with them. Because: If we whitelist headers, they can no longer add a new keyword to an existing header without risking that browsers are being blocked by (outdated) CRS installations.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:53 UTC</span>

<span style="font-size: 90%;">And browsers are surprisingly sensitive for these blockings (reported by users using nightly builds).</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:57:06 UTC</span>

<span style="font-size: 90%;">Guten Abend.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:15 UTC</span>

<span style="font-size: 90%;">They are starting to discuss a new RFC that brings means to prevent this so called protocol ossification, because if they are not preventing it, browsers will simply invent a new header where we are not yet whitelisting the format.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:18 UTC</span>

<span style="font-size: 90%;">Hi Christian.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:58 UTC</span>

<span style="font-size: 90%;">But they also think it is probably more effective to simply talk to the WAF developers, so I have been invited into their slack.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:30 UTC</span>

<span style="font-size: 90%;">And that's quite interesting. WAFs are surprisingly problematic for the evolution of the WWW.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:28 UTC</span>

<span style="font-size: 90%;">Well, I wonder who was problematic first :thinking_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:45 UTC</span>

<span style="font-size: 90%;">(Not the evolution)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:50 UTC</span>

<span style="font-size: 90%;">But the browsers</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:01:24 UTC</span>

<span style="font-size: 90%;">and even ore the "home-made-HTTP-clients"</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:30 UTC</span>

<span style="font-size: 90%;">They see QUIC as a way around the TCP ossification introduced by traffic shapers and other bad routers that blocks TCP evolution and they want to avoid HTTP dying the same way.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:35 UTC</span>

<span style="font-size: 90%;">Yes, so that's about ti from that front. If you are interested, I have 2-3 papers to share.</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">21:02:43 UTC</span>

<span style="font-size: 90%;">Wow that is deep topic at this hour.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:48 UTC</span>

<span style="font-size: 90%;">that would be really interesting to read</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:52 UTC</span>

<span style="font-size: 90%;">definitely</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">21:03:03 UTC</span>

<span style="font-size: 90%;">Would like to read that too. Please share</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:07 UTC</span>

<span style="font-size: 90%;">I'll send them to you _@csanders_ abd _@fzipitria_ .</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:07 UTC</span>

<span style="font-size: 90%;">I always liked more the vegas tcp</span>

**csanders** <span style="color: grey; font-size: 90%;">21:03:56 UTC</span>

<span style="font-size: 90%;">Repos are moving over now ([https://github.com/coreruleset/modsecurity-ansible-role](https://github.com/coreruleset/modsecurity-ansible-role)) iis the first</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:07:37 UTC</span>

<span style="font-size: 90%;">could you put an example to README, how can I make an exception to CRS config, or exclusion? I'm not an Ansible expert, but I need for that :slightly_smiling_face:</span>

↳ **csanders** <span style="color: grey; font-size: 90%;">21:27:34 UTC</span>

<span style="font-size: 90%;">we’ll def hahve to go back through that ansible role, its been three years since it was updated :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:13 UTC</span>

<span style="font-size: 90%;">Yes, it0s getting very late. Are we moving to the issues, or are we calling it a night?
The problem is, there are quite a lot of new ones.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:04:34 UTC</span>

<span style="font-size: 90%;">Calling it a night!! I will leave now and go to bed.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:04:47 UTC</span>

<span style="font-size: 90%;">night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:04:50 UTC</span>

<span style="font-size: 90%;">Can you send me the paper too, _@dune73_?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:56 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:05:03 UTC</span>

<span style="font-size: 90%;">good night franzi</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">21:07:00 UTC</span>

<span style="font-size: 90%;">Good night :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:07 UTC</span>

<span style="font-size: 90%;">We might want to do a small task for issues next Monday</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:08 UTC</span>

<span style="font-size: 90%;">Would it be an option to do an issue caht next Monday?</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">21:05:13 UTC</span>

<span style="font-size: 90%;">I'm calling it a night too. But I'll have a look at the open issues in the comming days to see if I could help with one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:15 UTC</span>

<span style="font-size: 90%;">Yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:05:15 UTC</span>

<span style="font-size: 90%;">Thank you.
Good night everybody or have a good day...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:17 UTC</span>

<span style="font-size: 90%;">Exatly my thinking. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:52 UTC</span>

<span style="font-size: 90%;">Let continue with the issues next monday</span>

**airween** <span style="color: grey; font-size: 90%;">21:06:03 UTC</span>

<span style="font-size: 90%;">_@dune73_ I'ld read that papers too</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:06:13 UTC</span>

<span style="font-size: 90%;">I will be in summer vacation. But I will take two issues/topics. See list.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:47 UTC</span>

<span style="font-size: 90%;">Cool. So it's next Monday for those who have time and no politics before we turn to the issues!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:57 UTC</span>

<span style="font-size: 90%;">Thank you everybody for participating!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:01 UTC</span>

<span style="font-size: 90%;">We still need to talk about documentation</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:09 UTC</span>

<span style="font-size: 90%;">:rolling_on_the_floor_laughing:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:14 UTC</span>

<span style="font-size: 90%;">Nah, see you next time!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:51 UTC</span>

<span style="font-size: 90%;">I'll move the documentation topic for next month chat</span>

**Emile** <span style="color: grey; font-size: 90%;">21:08:56 UTC</span>

<span style="font-size: 90%;">See you next week o/</span>

**airween** <span style="color: grey; font-size: 90%;">21:10:27 UTC</span>

<span style="font-size: 90%;">good night to all!</span>

**csanders** <span style="color: grey; font-size: 90%;">21:10:31 UTC</span>

<span style="font-size: 90%;">night</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">21:10:58 UTC</span>

<span style="font-size: 90%;">good night !</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:11:00 UTC</span>

<span style="font-size: 90%;">good night all</span>

**csanders** <span style="color: grey; font-size: 90%;">21:26:37 UTC</span>

<span style="font-size: 90%;">[https://github.com/crs-support](https://github.com/crs-support) is empty all repos have been moved over — I guess we’ll see in the next few days if this causes any issues due to the redirects :slightly_smiling_face:</span>

