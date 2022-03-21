### Mon, Aug 3rd, 2020

**dune73** <span style="color: grey; font-size: 90%;">18:30:45 UTC</span>

<span style="font-size: 90%;">Hello everyone. Time for our monthly chat. So who is around?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:31:00 UTC</span>

<span style="font-size: 90%;">howdy</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:31:17 UTC</span>

<span style="font-size: 90%;">hi all</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:12 UTC</span>

<span style="font-size: 90%;">hello!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:35 UTC</span>

<span style="font-size: 90%;">Hey ho!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:40 UTC</span>

<span style="font-size: 90%;">huhu</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;">Wow cool, that's a good number of people, despite being Summer holidays. Welcome!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:52 UTC</span>

<span style="font-size: 90%;">I have finished a heavy government project last week and today, I finally sat down and caught up on CRS. I updated the previous chat protocol and also PRs and issues. For some it might have been short notice, though, namely those people who did not attend the last meeting or the last special issue meeting the week afterwards.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">18:35:51 UTC</span>

<span style="font-size: 90%;">Thank you for your work!</span>

↳ **walter** <span style="color: grey; font-size: 90%;">18:37:01 UTC</span>

<span style="font-size: 90%;">You should get your own series in the Marvel universe!</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:58 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:08 UTC</span>

<span style="font-size: 90%;">Hello _@airween_!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:50 UTC</span>

<span style="font-size: 90%;">Our agenda is at: [https://github.com/coreruleset/coreruleset/issues/1853](https://github.com/coreruleset/coreruleset/issues/1853)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:35:51 UTC</span>

<span style="font-size: 90%;">Thank you for your work!</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">18:35:51 UTC</span>

<span style="font-size: 90%;">Thank you for your work!</span>

↳ **walter** <span style="color: grey; font-size: 90%;">18:37:01 UTC</span>

<span style="font-size: 90%;">You should get your own series in the Marvel universe!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:33 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: You did this work those last few months and today I realized again just how much work it is to go through the whole chat and write down decisions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:43 UTC</span>

<span style="font-size: 90%;">So thank you for the April, May and June.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:20 UTC</span>

<span style="font-size: 90%;">Speaking off: Does anybody have a good script to backup a slack channel?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:46 UTC</span>

<span style="font-size: 90%;">It seems we can not use the official export, since we are sitting on a free service. And scrolling is hard.</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:06 UTC</span>

<span style="font-size: 90%;">never tried doing that, sorry</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:38:24 UTC</span>

<span style="font-size: 90%;">No, I have not.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:15 UTC</span>

<span style="font-size: 90%;">I'd really like to dump the conversation and archive it.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:26 UTC</span>

<span style="font-size: 90%;">But whatever, that's not something for tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:30 UTC</span>

<span style="font-size: 90%;">Shall we start?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:39:33 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:50 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:47 UTC</span>

<span style="font-size: 90%;">So PR 1848 seems innocent enough. Opinions?</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:01 UTC</span>

<span style="font-size: 90%;">looks great!</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:30 UTC</span>

<span style="font-size: 90%;">insta-merge?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:41:37 UTC</span>

<span style="font-size: 90%;">Looks good, merge it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:42 UTC</span>

<span style="font-size: 90%;">We could do with a test, though, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:37 UTC</span>

<span style="font-size: 90%;">The description actually brings an example and I think we could ask for the example being made into a test before we merge. What do you think?</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:57 UTC</span>

<span style="font-size: 90%;">agreed, I’ll ask the submitter for a test</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:21 UTC</span>

<span style="font-size: 90%;">Yeah, tests are always good</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:43:29 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:40 UTC</span>

<span style="font-size: 90%;">So we assign to you _@walter_ and you'll merge when ready.</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:50 UTC</span>

<span style="font-size: 90%;">yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:05 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:44:21 UTC</span>

<span style="font-size: 90%;">thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:23 UTC</span>

<span style="font-size: 90%;">[#1847](https://github.com/coreruleset/coreruleset/issues/#1847): NextCloud FP handling of 200002.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:44 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:04 UTC</span>

<span style="font-size: 90%;">I think we decided we do rule exclusions for recommended rules even if they are not ours. So it would make sense to merge this as well.
But there is the rule id issue the contributors are discussing.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:10 UTC</span>

<span style="font-size: 90%;">Anybody wants to guide them?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:38 UTC</span>

<span style="font-size: 90%;">I can help them</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:46:35 UTC</span>

<span style="font-size: 90%;">the rule id has nothing to do with CRS</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:37 UTC</span>

<span style="font-size: 90%;">there is precedent for excluding 200002, our WordPress and Nextcloud exclusions are already doing it</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">oh okay</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:35 UTC</span>

<span style="font-size: 90%;">Should we also prefer matching REQUEST_FILENAME first and then by method?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:47 UTC</span>

<span style="font-size: 90%;">_@emphazer_: Yes, it is a bit odd, but then this is a service to our users and I guess they do not care and ModSecurity apparently does not offer rule exclusion packages.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:00 UTC</span>

<span style="font-size: 90%;">That would be a plus _@fzipitria_, I think.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:48:04 UTC</span>

<span style="font-size: 90%;">okay i understand</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:43 UTC</span>

<span style="font-size: 90%;">Do you think then we merge and change afterwards? Or we should talk about that in the issue?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:15 UTC</span>

<span style="font-size: 90%;">Your choice if you guide them. Just make sure it's not forgotten.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:01 UTC</span>

<span style="font-size: 90%;">Thanks for volunteering _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:19 UTC</span>

<span style="font-size: 90%;">[#1846](https://github.com/coreruleset/coreruleset/issues/#1846) is on hold while errors are being fixed.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:04 UTC</span>

<span style="font-size: 90%;">And [#1845](https://github.com/coreruleset/coreruleset/issues/#1845) is a long standing issue, a fixed PR we had in the old repo for a very long time. I'm glad _@fgs_ found the time to get this done.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:13 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:19 UTC</span>

<span style="font-size: 90%;">it looks scary to me but I’ve never quite put much work into learning these decodes…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:38 UTC</span>

<span style="font-size: 90%;">As long as we have tests</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:39 UTC</span>

<span style="font-size: 90%;">would we not miss encoded attacks? or are they not relevant in these rules?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:55 UTC</span>

<span style="font-size: 90%;">And looks like they were updated</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:00 UTC</span>

<span style="font-size: 90%;">It's a reversion of a change we made earlier (and released in 3.3)</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:39 UTC</span>

<span style="font-size: 90%;">hot from the press: it looks like libinjection maintainership might be given to TrustWave [https://github.com/client9/libinjection/issues/150#issuecomment-668179739](https://github.com/client9/libinjection/issues/150#issuecomment-668179739)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:54:03 UTC</span>

<span style="font-size: 90%;">No please....</span>

↳ **walter** <span style="color: grey; font-size: 90%;">18:54:31 UTC</span>

<span style="font-size: 90%;">I wish I could code in C but I really don’t dare to do that…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:39 UTC</span>

<span style="font-size: 90%;">I think the point of _@fgs_ was that the double encoding is done in vain, but I never really looked into this here.</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:40 UTC</span>

<span style="font-size: 90%;">alright, that’s a very smart dude so I tend to trust him on these issues, but similarly I have never looked in detail</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:00 UTC</span>

<span style="font-size: 90%;">Oops. It's up for grabs.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:06 UTC</span>

<span style="font-size: 90%;">I could say yes, but I still have open issues from last month because I didn't do anything :see_no_evil:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:18 UTC</span>

<span style="font-size: 90%;">Well... summer</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:29 UTC</span>

<span style="font-size: 90%;">Yes... And vacation...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:59:05 UTC</span>

<span style="font-size: 90%;">If nobody wants to take it, I'll take it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:13 UTC</span>

<span style="font-size: 90%;">I guess we can push it a little later to see if fgs returns</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:59:16 UTC</span>

<span style="font-size: 90%;">But I do not promise to finish it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:02 UTC</span>

<span style="font-size: 90%;">I think we can assign to _@franbuehler_ for the time being, if _@fgs_ returns tonight, we can bring it back to the table, otherwise it would be good if _@franbuehler_ could review and eventually merge.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:00:21 UTC</span>

<span style="font-size: 90%;">Ok</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:00:52 UTC</span>

<span style="font-size: 90%;">I self assigned it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:40 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:53 UTC</span>

<span style="font-size: 90%;">What about [#1843](https://github.com/coreruleset/coreruleset/issues/#1843)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:14 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: You are covering this one too?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:31 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:36 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:38 UTC</span>

<span style="font-size: 90%;">Both netxcloud</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:30 UTC</span>

<span style="font-size: 90%;">[#1842](https://github.com/coreruleset/coreruleset/issues/#1842) is a welcome rule cleanup by _@fgs_. Any objections to merging?</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:28 UTC</span>

<span style="font-size: 90%;">ah, this looks very nice</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:04:51 UTC</span>

<span style="font-size: 90%;">looks good</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:55 UTC</span>

<span style="font-size: 90%;">So we merge?</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:25 UTC</span>

<span style="font-size: 90%;">I’m for it!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:05:36 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:06 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:43 UTC</span>

<span style="font-size: 90%;">[#1839](https://github.com/coreruleset/coreruleset/issues/#1839): Seems welcome, but lint fails. I do not see why exactly, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:59 UTC</span>

<span style="font-size: 90%;">There are three empty lines before the rule in question. Could that be the issue?</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:54 UTC</span>

<span style="font-size: 90%;">tests/regression/tests/REQUEST-942-APPLICATION-ATTACK-SQLI/942230.yaml
[12](https://github.com/coreruleset/coreruleset/pull/1839/checks?check_run_id=844943445#step:5:12)
  168:1     error    too many blank lines (1 > 0)  (empty-lines)</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:14 UTC</span>

<span style="font-size: 90%;">strangely, that file doesn’t seem changed in this PR?</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:35 UTC</span>

<span style="font-size: 90%;">so it must be the state of master where he branched from…</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:03 UTC</span>

<span style="font-size: 90%;">I think in cases like this, we can merge…</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:10 UTC</span>

<span style="font-size: 90%;">or we can ask for a test!</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:27 UTC</span>

<span style="font-size: 90%;">and hopefully the regression test will work out itself</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:08 UTC</span>

<span style="font-size: 90%;">shall I self-assign and ask for the test?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:14 UTC</span>

<span style="font-size: 90%;">Yes, true, test missing here too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:19 UTC</span>

<span style="font-size: 90%;">That is most welcome. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:00 UTC</span>

<span style="font-size: 90%;">[#1817](https://github.com/coreruleset/coreruleset/issues/#1817) has a long thread of discussions.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:21 UTC</span>

<span style="font-size: 90%;">We talked about it last month, but I think this is not over.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:23 UTC</span>

<span style="font-size: 90%;">Correct?</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:58 UTC</span>

<span style="font-size: 90%;">you are correct. sadly I did not have time to look at this issue in the last month :pensive:</span>

**Emile** <span style="color: grey; font-size: 90%;">19:14:11 UTC</span>

<span style="font-size: 90%;">(:wave:)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:15 UTC</span>

<span style="font-size: 90%;">I set the "needs action" label. Let's give it another month.</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:19 UTC</span>

<span style="font-size: 90%;">hi _@Emile_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:21 UTC</span>

<span style="font-size: 90%;">Hi _@Emile_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:22 UTC</span>

<span style="font-size: 90%;">yes, I’ll plan it in my calendar!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:17 UTC</span>

<span style="font-size: 90%;">Let's move to [#1794](https://github.com/coreruleset/coreruleset/issues/#1794) then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:39 UTC</span>

<span style="font-size: 90%;">Which is a work in progres.</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:07 UTC</span>

<span style="font-size: 90%;">wasn’t t:removeCommentsChar going to be deprecated in v3?</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:10 UTC</span>

<span style="font-size: 90%;">maybe I remember this wrong</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:00 UTC</span>

<span style="font-size: 90%;">I must be wrong, it’s in there, sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:11 UTC</span>

<span style="font-size: 90%;">Confirmed.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:17:19 UTC</span>

<span style="font-size: 90%;">nope, removeComments “could be deprecated soon in a future release”</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:33 UTC</span>

<span style="font-size: 90%;">i think we discussed it because removal always led to new security issues</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:17:55 UTC</span>

<span style="font-size: 90%;">I can work on it this week and fix GA errors</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:08 UTC</span>

<span style="font-size: 90%;">Cool _@theMiddle_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:02 UTC</span>

<span style="font-size: 90%;">So [#1793](https://github.com/coreruleset/coreruleset/issues/#1793), which looks very intriguing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:52 UTC</span>

<span style="font-size: 90%;">That's a new rule for an injection technique we did not cover hitherto. Correct _@theMiddle_?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:19 UTC</span>

<span style="font-size: 90%;">yes, the problem is that 942520 (like 932200) are really a mess. In the specific rule, 942520 just cover the PoC sent us by a user here [https://github.com/coreruleset/coreruleset/issues/1727](https://github.com/coreruleset/coreruleset/issues/1727)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:22:16 UTC</span>

<span style="font-size: 90%;">as you can see, it’s prone to some false positive especially on free text and password input</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:23:31 UTC</span>

<span style="font-size: 90%;">a stricter version should be FPs free, but could be more easy to bypass</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:00 UTC</span>

<span style="font-size: 90%;">Last month, we decided to give it a go in PL2. Do you want to merge as is (in PL2) or do you prefer to work on it some more?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:25:22 UTC</span>

<span style="font-size: 90%;">let me do a refresh on it, and I’ll do some other test this week</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:21 UTC</span>

<span style="font-size: 90%;">PL2 is a good idea IMO. Anyway let me see if I can make it more stricter</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:28 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:57 UTC</span>

<span style="font-size: 90%;">np, sorry for my lateness</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:17 UTC</span>

<span style="font-size: 90%;">No worries, man.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:28 UTC</span>

<span style="font-size: 90%;">So I think we're done with the PRs, I guess.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:43 UTC</span>

<span style="font-size: 90%;">Other issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:11 UTC</span>

<span style="font-size: 90%;">No on the agenda: I wrote to TW about the new DoS like we agreed to and I did not get a response.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:23 UTC</span>

<span style="font-size: 90%;">Did anybody else hear anything?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:36 UTC</span>

<span style="font-size: 90%;">:disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:41 UTC</span>

<span style="font-size: 90%;">nope</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:43 UTC</span>

<span style="font-size: 90%;">Or - in case - do we know of exploits abusing this in the wild?</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:25 UTC</span>

<span style="font-size: 90%;">no, still no answer</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:29:42 UTC</span>

<span style="font-size: 90%;">that’s really frightening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:54 UTC</span>

<span style="font-size: 90%;">I'll probably send another message.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">Other than that, I think it is time to contact the packagers / distributors, point them to the fix in the code and start a conversation how they want to handle this. Maybe alert of the timeline and that we will be releasing in September.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:11 UTC</span>

<span style="font-size: 90%;">TW knows that we would like to make it public?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:42 UTC</span>

<span style="font-size: 90%;">Yes, we informed them in early July. No response.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:51 UTC</span>

<span style="font-size: 90%;">oky tnx</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:05 UTC</span>

<span style="font-size: 90%;">they know the CVE number...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:12 UTC</span>

<span style="font-size: 90%;">ah</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">The lack of response also tells me, that publishing _@airween_'s list of v3 shortcomings is maybe a bit early... :wink:</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:55 UTC</span>

<span style="font-size: 90%;">ah, yes! could you review that?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:35:01 UTC</span>

<span style="font-size: 90%;">It's a sad situation!</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:19 UTC</span>

<span style="font-size: 90%;">what's the plan, when can we publish it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:49 UTC</span>

<span style="font-size: 90%;">I postponed reviewing it. Sorry _@airween_. I looked over it briefly. The content is great, but I'd like to reword certain things.
Which I will do eventually.
But given the situation with the DoS with TW, I think publishing it now could be like adding oil to the fire.</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">ah, right - but I don't see the reasons, that's just a "collection", there isn't any secret :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:56 UTC</span>

<span style="font-size: 90%;">It's usually the messenger who is shot first.</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:11 UTC</span>

<span style="font-size: 90%;">right, that's in a good place now - if anybody wants to check, just let me know</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:24 UTC</span>

<span style="font-size: 90%;">yes thanks!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">but I think I’ve already read it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:48 UTC</span>

<span style="font-size: 90%;">I think once we have a response from TW we can me a better guess if we want to publish before the CVE comes out, or rather afterwards, after the dust settled again a bit.</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:42 UTC</span>

<span style="font-size: 90%;">sure, you're right</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">btw a CRS related question: at last month we've discussed about security releases, but I don't remember what we agreed on... I mean the backports</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:23 UTC</span>

<span style="font-size: 90%;">Did we agree on this?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:38 UTC</span>

<span style="font-size: 90%;">Was it about backporting the stuff Amit Semper reported?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:47 UTC</span>

<span style="font-size: 90%;">Btw: His talk is up any day now, is not it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:57 UTC</span>

<span style="font-size: 90%;">I created an issue to track this, but haven’t made releases: [https://github.com/coreruleset/coreruleset/issues/1833](https://github.com/coreruleset/coreruleset/issues/1833)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:03 UTC</span>

<span style="font-size: 90%;">Anybody has the link to the conference schedule just in case?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:44:09 UTC</span>

<span style="font-size: 90%;">Amit: Yes, start of August.</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:13 UTC</span>

<span style="font-size: 90%;">ah, yes! thanks _@walter_!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:44:22 UTC</span>

<span style="font-size: 90%;">Did he receive the gift??</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:35 UTC</span>

<span style="font-size: 90%;">I have not heard from him on the gift.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:47 UTC</span>

<span style="font-size: 90%;">Maybe melted in the sun (-> Swiss Chocolate)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:02 UTC</span>

<span style="font-size: 90%;">But I'm sure the stickers made it. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:04 UTC</span>

<span style="font-size: 90%;">Thank you _@walter_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:18 UTC</span>

<span style="font-size: 90%;">So what do you think about contacting the CRS / ModSecurity packagers about the upcoming CVE?</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:05 UTC</span>

<span style="font-size: 90%;">a Debian/Ubuntu packager is here... :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:47:32 UTC</span>

<span style="font-size: 90%;">I found it:
[https://www.blackhat.com/us-20/briefings/schedule/#http-request-smuggling-in-2020--new-variants-new-defenses-and-new-challenges-20019](https://www.blackhat.com/us-20/briefings/schedule/#http-request-smuggling-in-2020--new-variants-new-defenses-and-new-challenges-20019)</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:47:32 UTC</span>

<span style="font-size: 90%;">I found it:
[https://www.blackhat.com/us-20/briefings/schedule/#http-request-smuggling-in-2020--new-variants-new-defenses-and-new-challenges-20019](https://www.blackhat.com/us-20/briefings/schedule/#http-request-smuggling-in-2020--new-variants-new-defenses-and-new-challenges-20019)</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:54 UTC</span>

<span style="font-size: 90%;">anyway, I think we must to inform them</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:19 UTC</span>

<span style="font-size: 90%;">I think it makes perfect sense to alert packagers, at least they’re aware. if they like, they can pull a patch into their packaging process… I think most would prefer to wait for an official release. but this is a good way to raise interest and I think there’s a good chance it will help Felipe raise priority, get budget for the work, etc…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:44 UTC</span>

<span style="font-size: 90%;">Amit: "I demonstrate a circumvention of an existing HTTP Request Smuggling protection for a free, open source application security solution."</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:49:33 UTC</span>

<span style="font-size: 90%;">It's fixed now! (Hopefully :wink: )</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:50:01 UTC</span>

<span style="font-size: 90%;">is it ever been vulnerable? who knows! ;)</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:07:55 UTC</span>

<span style="font-size: 90%;">Haha :rolling_on_the_floor_laughing:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:49:05 UTC</span>

<span style="font-size: 90%;">without a working PoC :slightly_smiling_face: (ok, stop it)</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">it’s such a shame, so much work was put into modsec3 only to deal with so many bugs and problems… it’s a good reminder how complete rewrites (as inviting as they may seem) can ruin your project…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:26 UTC</span>

<span style="font-size: 90%;">I have 2-3 other communication tasks this month, so I would not mind if somebody else would get in touch with the packagers.</span>

**Emile** <span style="color: grey; font-size: 90%;">19:52:34 UTC</span>

<span style="font-size: 90%;">I have been writing a WAF compatible with ModSecurity’s capability... the format is a mess</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:54:46 UTC</span>

<span style="font-size: 90%;">Ok, not so much the format as the matrix of capability, and partially thought through operators and transformers :(</span>

**Emile** <span style="color: grey; font-size: 90%;">19:52:59 UTC</span>

<span style="font-size: 90%;">The amount of cruft is insane. This rewrite can’t have been a fun project :grimacing: </span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:54 UTC</span>

<span style="font-size: 90%;">OK. I'm taking this on. _@airween_: I would be happy if you could help me with contacts, if you have any.</span>

**airween** <span style="color: grey; font-size: 90%;">19:54:06 UTC</span>

<span style="font-size: 90%;">compatible with ModSecurity’s capability. - compatible with ModSecurity or with CRS?</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:55:07 UTC</span>

<span style="font-size: 90%;">The goal for this push is being able to import most of CRS</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:55:28 UTC</span>

<span style="font-size: 90%;">and are you working on it currently?</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:55:39 UTC</span>

<span style="font-size: 90%;">Yep</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:55:55 UTC</span>

<span style="font-size: 90%;">(exceptions for very networky rules which we don’t care as much about)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:56:15 UTC</span>

<span style="font-size: 90%;">oh, sounds good - and which language do you use?</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">C++, we ship the binary with our agents as libSqreen. We may open source it at some point</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:00:15 UTC</span>

<span style="font-size: 90%;">Actually, the header is published here [https://github.com/sqreen/go-libsqreen/tree/master/waf/internal/bindings](https://github.com/sqreen/go-libsqreen/tree/master/waf/internal/bindings) not very useful though :sweat_smile: </span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:07:22 UTC</span>

<span style="font-size: 90%;">and do you use CRS and/or Seclang syntax?</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:09:58 UTC</span>

<span style="font-size: 90%;">Nope, we import it internally and replace it by our own syntax. We don’t have to expose it so I can rely on the representation being very human-unfriendly but helpful for the WAF</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:10:23 UTC</span>

<span style="font-size: 90%;">(we also have a different rule flow model)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:10:28 UTC</span>

<span style="font-size: 90%;">right, thanks</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:11:28 UTC</span>

<span style="font-size: 90%;">We still need to be more or less at feature parity, so some of the cruft hit us right in the face :sweat_smile: </span>

**airween** <span style="color: grey; font-size: 90%;">19:54:47 UTC</span>

<span style="font-size: 90%;">_@dune73_, right, I'll try to collect the addresses - not just the packagers, the other distributors</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:56:18 UTC</span>

<span style="font-size: 90%;">I think that 90% of libmodsec users are using it with nginx… should Nginx be included?</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:23 UTC</span>

<span style="font-size: 90%;">thank you _@dune73_. wish I could help but my time is really limited due to what we call Mantelzorg (taking care for sick relatives)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:30 UTC</span>

<span style="font-size: 90%;">Thank you very much. I can then do the message itself.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:05 UTC</span>

<span style="font-size: 90%;">Dutch has a few very cosy words. Mantelzorg is beautiful (if it was not so sad).</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:15 UTC</span>

<span style="font-size: 90%;">_@airween_ don’t forget FreeBSD - [marius.halden@modirum.com](mailto:marius.halden@modirum.com) is the maintainer there of mod_security3</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:56:18 UTC</span>

<span style="font-size: 90%;">I think that 90% of libmodsec users are using it with nginx… should Nginx be included?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:56:18 UTC</span>

<span style="font-size: 90%;">I think that 90% of libmodsec users are using it with nginx… should Nginx be included?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:31 UTC</span>

<span style="font-size: 90%;">Absolutely. I have that contact.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:02 UTC</span>

<span style="font-size: 90%;">Basically all the ModSec integrators we know. And we know quite a few.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:10 UTC</span>

<span style="font-size: 90%;">ModSec3 integrators that is.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:37 UTC</span>

<span style="font-size: 90%;">Let's move back to the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:07 UTC</span>

<span style="font-size: 90%;">Our meetings tend to be super long and once we hit the open issues, most people are very exhausted.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:21 UTC</span>

<span style="font-size: 90%;">So there is the idea, to split off the issue topic into a separate meeting.</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:31 UTC</span>

<span style="font-size: 90%;">I love that idea!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:49 UTC</span>

<span style="font-size: 90%;">We tried this out in July. It felt good, but only a few people showed up.</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:41 UTC</span>

<span style="font-size: 90%;">well, if we are with few, we could still tackle some issues, and any controversial ones we could take to the next monthly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:47 UTC</span>

<span style="font-size: 90%;">So what do you think? Is this something we should institutionalize? Would we have enough people showing up? Would it bring a better rhythm to the project?
Or would this be too much CRS for you?</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:00 UTC</span>

<span style="font-size: 90%;">it would mean a chat every ~ two weeks, instead of monthly</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:27 UTC</span>

<span style="font-size: 90%;">I fear people might stay away from said meeting to make sure they are not being volunteered ...</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:45 UTC</span>

<span style="font-size: 90%;">I think maybe people just think it’s too much time</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:49 UTC</span>

<span style="font-size: 90%;">but let’s hear it from the crowd!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:09 UTC</span>

<span style="font-size: 90%;">I am up for it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:01:14 UTC</span>

<span style="font-size: 90%;">not too much for me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:19 UTC</span>

<span style="font-size: 90%;">The problem is that it is in the middle of my work day</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:01:51 UTC</span>

<span style="font-size: 90%;">20:30 CET is not always awesome for me, but no problem</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:32 UTC</span>

<span style="font-size: 90%;">would another time work better? I’m flexible, in fact I’d love earlier… later would be a problem :sweat_smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:53 UTC</span>

<span style="font-size: 90%;">but earlier would be incompatible with US people..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:29 UTC</span>

<span style="font-size: 90%;">20:30 CET is a sweet spot for me, but it stands very much in the way for other people. Namely _@fgs_, but I guess _@fzipitria_ and _@csanders_ have a hard time making it work.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:05:27 UTC</span>

<span style="font-size: 90%;">no problem here. You mean 1st monday => PR 2nd monday => issues ?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:48 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: The advantage of the 2nd meeting would be that it's not eating up half a workday anymore, but two times 1-2 hours. Or is this no real advantage?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:06:09 UTC</span>

<span style="font-size: 90%;">Do we want to test it for the next 2 months?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:10 UTC</span>

<span style="font-size: 90%;">I like it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:12 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Maybe rather 1st Monday and 3rd Monday.</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:33 UTC</span>

<span style="font-size: 90%;">Or is this no real advantage? - in July, this was very good</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:07 UTC</span>

<span style="font-size: 90%;">_@emphazer_ and _@Emile_: What do you guys think?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:08:14 UTC</span>

<span style="font-size: 90%;">I’m up for trying to split. Not much difference for me, no kid at home :)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:55 UTC</span>

<span style="font-size: 90%;">_@csanders_: Have we heard from you about this idea?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:09 UTC</span>

<span style="font-size: 90%;">i don’t think so</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:10:34 UTC</span>

<span style="font-size: 90%;">hmmm</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:34 UTC</span>

<span style="font-size: 90%;">What do you think? It's right in the middle of your work day or even morning, is not it?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:37 UTC</span>

<span style="font-size: 90%;">it can work for me :slightly_smiling_face:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:10:57 UTC</span>

<span style="font-size: 90%;">i think it could be possible.</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:11:10 UTC</span>

<span style="font-size: 90%;">so 2 mondays per month right?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:32 UTC</span>

<span style="font-size: 90%;">2 mondays per month, but get to bed earlier in return.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:40 UTC</span>

<span style="font-size: 90%;">(without having to leave earlier)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:22 UTC</span>

<span style="font-size: 90%;">OK. Let's give it a go then and we'll meet in two weeks again. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:39 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:51 UTC</span>

<span style="font-size: 90%;">_@franbuehler_proposed to try it out for two months. I think that is a good plan and we can then re-assess the situation in the October meeting.</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:18 UTC</span>

<span style="font-size: 90%;">great!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:31 UTC</span>

<span style="font-size: 90%;">I do not want to make this too long tonight, but there is something where I / we need your support.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:46 UTC</span>

<span style="font-size: 90%;">OWASP is currently reviewing over a dozens of its formal policies.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">I ignored this email...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:58 UTC</span>

<span style="font-size: 90%;">One that is affecting us is the "donations" policy.</span>

**airween** <span style="color: grey; font-size: 90%;">20:15:18 UTC</span>

<span style="font-size: 90%;">a last question (not related to the agenda): I started to write a full SecLang parser in C, not just the SecRule and few keywords, but all of the documented tokens.

It works as very well with CRS. Now I tested it on Comodo rules, and found an interesting variable:

SecRule HTTP_User-Agent "WinHttp\.WinHttpRequest\.5" \
    "id:221031,chain,msg...
What's the HTTP_User-Agent?</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:17:00 UTC</span>

<span style="font-size: 90%;">Looks like a bug and they meant REQUEST_HEADERS:User-Agent …</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:18:00 UTC</span>

<span style="font-size: 90%;">hmm... but this comes from the Comodo rule set.... I'm sure that the downloadable files are tested...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:19:19 UTC</span>

<span style="font-size: 90%;">Apache2 allowed it! :open_mouth:</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:19:57 UTC</span>

<span style="font-size: 90%;">but did the rule work? :stuck_out_tongue:</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">I guess not</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:20:28 UTC</span>

<span style="font-size: 90%;">okay, you're true - now I just looking the parser :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:20:41 UTC</span>

<span style="font-size: 90%;">nginx was failed</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:24:59 UTC</span>

<span style="font-size: 90%;">haha, there is a separated version for Nginx+modsec3. That rule is removed from there...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:08 UTC</span>

<span style="font-size: 90%;">The way the new policy is written, makes life very hard for us (to gain separate sponsors).</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">I ignored this email...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">I ignored this email...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:36 UTC</span>

<span style="font-size: 90%;">I have reviewed the proposal carefully and will provide extensive feedback. The feedback must be submitted by August 12.
I talked to @Walter and _@fzipitria_ chimed in as well. Our idea is now to publish our feedback and invite other people to co-sign our feedback.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:21 UTC</span>

<span style="font-size: 90%;">This is where you come in. I would like you to read the feedback carefully, provide feedback on the feedback if you want to, and then help to spread the word and co-sign as well.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:19:29 UTC</span>

<span style="font-size: 90%;">Of course!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:39 UTC</span>

<span style="font-size: 90%;">Thank you, Christian. What would we do without you!!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:42 UTC</span>

<span style="font-size: 90%;">I am not sure if they explicitly limit the feedback to paying OWASP members.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:09 UTC</span>

<span style="font-size: 90%;">Are you in touch with other OWASP people / chapters / projects you could invite personally to co-sign?
I'd really like to make this big. The more signatures the better.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:42 UTC</span>

<span style="font-size: 90%;">There won't be a discussion about the policy. Just the call for feedback, then they prepare the final policy and then the board agrees to adopt it (or not).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:09 UTC</span>

<span style="font-size: 90%;">So if we want our feedback to make an impact it has to carry enough weight so they can not pass over it.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:22:29 UTC</span>

<span style="font-size: 90%;">I could forward the feedback to OWASP DevSlop, Nancy etc.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:06 UTC</span>

<span style="font-size: 90%;">I do not have a lot of personal contacts.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:10 UTC</span>

<span style="font-size: 90%;">Please do.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:31 UTC</span>

<span style="font-size: 90%;">Anybody else with additional contacts? (-> Local chapters?)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:24:13 UTC</span>

<span style="font-size: 90%;">Did you ask the CH chapter?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:23 UTC</span>

<span style="font-size: 90%;">I plan to. And 2-3 other chapters I know. But that's about it with my OWASP contacts outside of board members or former board members ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:30 UTC</span>

<span style="font-size: 90%;">Good, I guess that's it on that topic. Expect the blog post on Wednesday or so.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:38 UTC</span>

<span style="font-size: 90%;">Anything else we need to discuss tonight?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:27:04 UTC</span>

<span style="font-size: 90%;">I have most of the Demo stie done, should be able to share with a few folks for testing later today</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:44 UTC</span>

<span style="font-size: 90%;">Super cool. I'd love to see that!</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:53 UTC</span>

<span style="font-size: 90%;">awesome!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:40 UTC</span>

<span style="font-size: 90%;">I guess we can close the meeting with these good news.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:03 UTC</span>

<span style="font-size: 90%;">Thank you all for attending. It has been nice to see you all again and I look forward to a productive issue meeting in two weeks.</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:11 UTC</span>

<span style="font-size: 90%;">see you in two!</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:17 UTC</span>

<span style="font-size: 90%;">thanks everyone</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:38 UTC</span>

<span style="font-size: 90%;">thanks! bye</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:30:45 UTC</span>

<span style="font-size: 90%;">cya in 2 weeks</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:30:48 UTC</span>

<span style="font-size: 90%;">bye bye!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:30:52 UTC</span>

<span style="font-size: 90%;">good night/day</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:46 UTC</span>

<span style="font-size: 90%;">good night!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:32:53 UTC</span>

<span style="font-size: 90%;">night</span>

