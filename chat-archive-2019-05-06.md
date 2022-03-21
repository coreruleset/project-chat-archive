### Mon, May 6th, 2019

**dune73** <span style="color: grey; font-size: 90%;">18:30:58 UTC</span>

<span style="font-size: 90%;">Hello everyone. So who's around for our monthly chat?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:16 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:24 UTC</span>

<span style="font-size: 90%;">heyho</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:26 UTC</span>

<span style="font-size: 90%;">hallo</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:31:37 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:06 UTC</span>

<span style="font-size: 90%;">Good to see you all. It's busy times and I get the feeling we're making big progress. Under pressure and not where we expected it, but it's important problems we are saving.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:22 UTC</span>

<span style="font-size: 90%;">I have opened an agenda item at <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1402></span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:47 UTC</span>

<span style="font-size: 90%;">It's a bit late, so it's still mostly empty. Please add items as you see fit or add them as comment if the issue is locked by somebody else.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:36 UTC</span>

<span style="font-size: 90%;">I would like to put ReDoS in the center, but it does not make much sense without _@fgs_, so I guess we'll postpone that until he shows up. His little daughter is keeping busy at evening hours...</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:34:54 UTC</span>

<span style="font-size: 90%;">isn't it 20:30 CEST and not CET?</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:20 UTC</span>

<span style="font-size: 90%;">is the baby’s clock set to UTC?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:35:35 UTC</span>

<span style="font-size: 90%;">Hi. Sorry, give me 5 and I will be here.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:41 UTC</span>

<span style="font-size: 90%;">+1</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:37 UTC</span>

<span style="font-size: 90%;">#emphazer: Not sure, but does not CEST replace CET during Summer, or is CET still active, but not in use? (philosophical question...)</span>

**airween** <span style="color: grey; font-size: 90%;">18:36:55 UTC</span>

<span style="font-size: 90%;">hi all :wave:</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:37:03 UTC</span>

<span style="font-size: 90%;">heheh, nothing important</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">Hello _@airween_!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:43 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:50 UTC</span>

<span style="font-size: 90%;">Hello _@fzipitria_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:57 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:57 UTC</span>

<span style="font-size: 90%;">Wow, it's full house tonight!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:38:43 UTC</span>

<span style="font-size: 90%;">hey all!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:38:45 UTC</span>

<span style="font-size: 90%;">My times are all messed up but I’m here now.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:38:59 UTC</span>

<span style="font-size: 90%;">i love how many PRs there are!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:03 UTC</span>

<span style="font-size: 90%;">Hi guys, this feels like we're complete!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:39:05 UTC</span>

<span style="font-size: 90%;">(it also scares me)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:35 UTC</span>

<span style="font-size: 90%;">Yes, we're a bit buried in PRs. Which is nice and intimidating at the same time.
Let's tackle ReDoS and 3.1.1 first. Shall we?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:39:43 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:40:10 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:30 UTC</span>

<span style="font-size: 90%;">_@fgs_: Can you give us a status of your work and how far we are from fixing the one CVE that really bugs us (and the rest of the ReDoS problem as we know it so far).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:56 UTC</span>

<span style="font-size: 90%;">For the record: We decided to kill the CVE first, release 3.1.1 and then fix the rest. Ideally, we stick to that plan.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:42:17 UTC</span>

<span style="font-size: 90%;">Still working on it. Haven’t had much time on it (and needed a break from regexp).
So unfortunately not done yet.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:42:43 UTC</span>

<span style="font-size: 90%;">how can we help if at all?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:42:46 UTC</span>

<span style="font-size: 90%;">I will say a few more days but I haven’t had much sleep the last couple of days.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:43:32 UTC</span>

<span style="font-size: 90%;">for the record we are talking about
<https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1355>
<https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1361>
<https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1362></span>

**fgs** <span style="color: grey; font-size: 90%;">18:43:40 UTC</span>

<span style="font-size: 90%;">_@csanders_ good question. I guess we can all work together to try to fix the patterns.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">(With the core being <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1359>)</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:45:05 UTC</span>

<span style="font-size: 90%;">what about [#1379](https://github.com/coreruleset/coreruleset/issues/#1379) ?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:54 UTC</span>

<span style="font-size: 90%;">For me [#1379](https://github.com/coreruleset/coreruleset/issues/#1379) is part of the solution for [#1359](https://github.com/coreruleset/coreruleset/issues/#1359).</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:46:05 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:06 UTC</span>

<span style="font-size: 90%;">Correct?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:46:38 UTC</span>

<span style="font-size: 90%;">yeah, it covers one of the patterns</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:11 UTC</span>

<span style="font-size: 90%;">Personally, I'd just like to see the whole thing together with the solution for 942260 and then we try it against the CVE.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:47:50 UTC</span>

<span style="font-size: 90%;">yes correct</span>

**fgs** <span style="color: grey; font-size: 90%;">18:48:04 UTC</span>

<span style="font-size: 90%;">btw, I think we still want to fix the other problems he pointed out</span>

**fgs** <span style="color: grey; font-size: 90%;">18:48:12 UTC</span>

<span style="font-size: 90%;">Specially for the ones that are easy to fix</span>

**csanders** <span style="color: grey; font-size: 90%;">18:48:26 UTC</span>

<span style="font-size: 90%;">yes, i agree</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:29 UTC</span>

<span style="font-size: 90%;">I'd really like to fix those, but it need not be done before 3.1.1.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:48:44 UTC</span>

<span style="font-size: 90%;">less we end up getting another CVE for things that are easily fixed</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:50 UTC</span>

<span style="font-size: 90%;">If it's ready before [#1359](https://github.com/coreruleset/coreruleset/issues/#1359) is fixed and backported, then why not.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:27 UTC</span>

<span style="font-size: 90%;">oh right, 3.1.1, sorry.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:37 UTC</span>

<span style="font-size: 90%;">And we can always release a 3.1.2 when we have the next batch done. But given it's been several weeks now, we should not linger and longer if we have something that improves the situation.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:45 UTC</span>

<span style="font-size: 90%;">agreed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:17 UTC</span>

<span style="font-size: 90%;">agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:23 UTC</span>

<span style="font-size: 90%;">So we're giving _@fgs_ some more days and we try and test and support whereever we can.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:15 UTC</span>

<span style="font-size: 90%;">Honestly, I do not know where we would be without your regexp skills _@fgs_. We have others with a similar skillset, but you are the one that took the time to sit down and get working.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:54 UTC</span>

<span style="font-size: 90%;">One positive effect of this whole business is, that it prompted me to dig up old logs and generate new tests. This triggered _@emphazer_ and we are now looking at more and more tests based on real world attack traffic.
For me this is very welcome, namely where it helps to close gaps. We need some policy though on how many tests we really want (for a given rule) and how close the patterns can / should be to one another.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:23 UTC</span>

<span style="font-size: 90%;">yes, i've been seeing that influx and trying to keep up with testing them</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:28 UTC</span>

<span style="font-size: 90%;">most are VERY useful tests</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:41 UTC</span>

<span style="font-size: 90%;">[#1400](https://github.com/coreruleset/coreruleset/issues/#1400) includes 118 tests, to give you an idea...</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">18:54:21 UTC</span>

<span style="font-size: 90%;">hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:53 UTC</span>

<span style="font-size: 90%;">Hi _@SpartanTri_!
_@fgs_: You opted to make sure the tests are really distinct.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:03 UTC</span>

<span style="font-size: 90%;">So what do you all think?</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:55:25 UTC</span>

<span style="font-size: 90%;">it was necessary here to use that many tests. they are all different. sometimes with small/big letter</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:00 UTC</span>

<span style="font-size: 90%;">I would say more tests is almost always good!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:29 UTC</span>

<span style="font-size: 90%;">It's a big step forward for the CRS.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:57:00 UTC</span>

<span style="font-size: 90%;">Unfortunately under pressure because of the CVEs. But it's good!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:23 UTC</span>

<span style="font-size: 90%;">OK, so let me play the devil's advocate: This is going to cost us a lot of cycles down the road</span>

**fgs** <span style="color: grey; font-size: 90%;">18:57:27 UTC</span>

<span style="font-size: 90%;">Since my bandwidth is limited my opinion atm is get them all in, clean them up later.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:36 UTC</span>

<span style="font-size: 90%;">A test in the test suite is hardly ever going to be an option</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:59 UTC</span>

<span style="font-size: 90%;">And would not _1_ test with capital / camelcase letters be enough to test if a rule is case sensitive?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:58:02 UTC</span>

<span style="font-size: 90%;">(I haven’t looked at them in detail outside my initial comment about some of them)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:23 UTC</span>

<span style="font-size: 90%;">-> Throwing out a a test in the test suite is hardly ever going to be an option</span>

**fgs** <span style="color: grey; font-size: 90%;">18:59:16 UTC</span>

<span style="font-size: 90%;">Tests are good, I’m just wary that having too many tests will make spotting what tests are missing hard, specially if there is a lot of redundancy.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:59:22 UTC</span>

<span style="font-size: 90%;">But maybe I’m overthinking it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:39 UTC</span>

<span style="font-size: 90%;">That's an interesting argument: So a lot of tests could blur the view and make us believe that a rule is nicely covered, when in fact all the tests are only testing a part of a rule.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:00:56 UTC</span>

<span style="font-size: 90%;">true</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:55 UTC</span>

<span style="font-size: 90%;">But I guess there is nothing we can do about this than a review of every rule and the tests that go without. Maybe grouping them into red/orange/green as far as tests ar concerned. One day when we think we have hte basics covered.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:02:32 UTC</span>

<span style="font-size: 90%;">Yeah. I think we should start enforcing that new rules and changes should always go together with tests.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:02:51 UTC</span>

<span style="font-size: 90%;">i agree</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:09 UTC</span>

<span style="font-size: 90%;">I think we are on good tracks with that. If we have new contributors, we can easily open an accompanying issue to add tests.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:29 UTC</span>

<span style="font-size: 90%;">Yes, I think we are.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:50 UTC</span>

<span style="font-size: 90%;">But let me sum this up: For the moment, we welcome huge sets of tests!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:57 UTC</span>

<span style="font-size: 90%;">Thank you all.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:17 UTC</span>

<span style="font-size: 90%;">_@emphazer_: How many additional rules can you cover like this?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:05:08 UTC</span>

<span style="font-size: 90%;">hmmm... its just guessing. but i think 90%</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:36 UTC</span>

<span style="font-size: 90%;">So you have attack traffic triggering like 90% of the rules and you - at least ideally - can turn this all into unit tests?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:05:53 UTC</span>

<span style="font-size: 90%;">yes</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:06:14 UTC</span>

<span style="font-size: 90%;">spend friday and today round about 10hours with it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:55 UTC</span>

<span style="font-size: 90%;">Please continue! (by all means)</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:06:59 UTC</span>

<span style="font-size: 90%;">its nothing auto generated in the end... every payload is personally reviewed by me</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:07:33 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:06 UTC</span>

<span style="font-size: 90%;">super cool</span>

**airween** <span style="color: grey; font-size: 90%;">19:08:08 UTC</span>

<span style="font-size: 90%;">sorry for the interrupt - may be you know I've worked with ftw so much times, till I aligned libmodsec3. My opinion is that the ftw in this form is not a pure solution for the good tests, because it just looks a minimal pattern. For eg (and reflect back to ReDos) if you wrote a test for a rule, and the test listens a pattern, you don't know which context occures it.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:08:16 UTC</span>

<span style="font-size: 90%;">its very time intensive but i will do what i can..</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:32 UTC</span>

<span style="font-size: 90%;">Can you do this at work and is it OK for your boss?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:09:01 UTC</span>

<span style="font-size: 90%;">_@airween_ exactly!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:09:39 UTC</span>

<span style="font-size: 90%;">thats why i did a grep -Po at the end... just the real complete match is in the payload</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:10:35 UTC</span>

<span style="font-size: 90%;">_@dune73_ i must do this at work and my boss knows we got a CVE and he also knows its important for us.</span>

**airween** <span style="color: grey; font-size: 90%;">19:10:56 UTC</span>

<span style="font-size: 90%;">in first step, we have to extend the ftw, or review all test, and extend the expected result</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:11:00 UTC</span>

<span style="font-size: 90%;">but i wont be able to spend too much time on it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">We'll end with this topic shortly. We do not have time to look into all the PRs. But there is the label "meeting agenda" that we set up lately. Please tag PRs with this if you want them covered tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:13 UTC</span>

<span style="font-size: 90%;">It's Olaf, is not it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:54 UTC</span>

<span style="font-size: 90%;">I can give a shot to extend ftw</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:12:03 UTC</span>

<span style="font-size: 90%;">yeah, him and my referent</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:43 UTC</span>

<span style="font-size: 90%;">FTW: FTW has its limits but it also does a lot of things right. A problem is that ModSec gives very little support to identify ReDoS rules. But if we can have FTW extended, then I'm sure _@csanders_ welcomes that.</span>

**airween** <span style="color: grey; font-size: 90%;">19:12:50 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ I will gladly help</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:08 UTC</span>

<span style="font-size: 90%;">If there is anything I / we can do to help you at work, let me know. I'll happily draft a letter in the name of the project.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:54 UTC</span>

<span style="font-size: 90%;">OK, so have a little team that will try to close gaps in FTW features. Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:43 UTC</span>

<span style="font-size: 90%;">For the record: _@csanders_ is our contact to the lead developer Zack Allen. What's his nick on slack?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:20 UTC</span>

<span style="font-size: 90%;">techy</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:22 UTC</span>

<span style="font-size: 90%;">but hes not on</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:48 UTC</span>

<span style="font-size: 90%;">let me hit himup</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:59 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:59 UTC</span>

<span style="font-size: 90%;">we have def extend it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:02 UTC</span>

<span style="font-size: 90%;">i saw a couple PRs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:13 UTC</span>

<span style="font-size: 90%;">Good. The next PR with the "meeting agenda" label is <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1392></span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:49 UTC</span>

<span style="font-size: 90%;">Are you basically OK with this PR that brings a very specific rule at PL3 for a rare bypass. I made it in a way it will be skipped unless a certain header is present.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:18:59 UTC</span>

<span style="font-size: 90%;">i have no problem for that</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:31 UTC</span>

<span style="font-size: 90%;">pretty funny bypass and nice rule!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:49 UTC</span>

<span style="font-size: 90%;">Thank you _@dune73_ for covering this!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:12 UTC</span>

<span style="font-size: 90%;">Fun fact: \@rx is really faster than \@beginsWith for short rules rules and simple patterns. I tested this extensively. _@fgs_ was right.</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:27 UTC</span>

<span style="font-size: 90%;">is that also true for endswith?</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:51 UTC</span>

<span style="font-size: 90%;">so unintuitive!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:21:01 UTC</span>

<span style="font-size: 90%;">that is crazy</span>

**fgs** <span style="color: grey; font-size: 90%;">19:21:10 UTC</span>

<span style="font-size: 90%;">The problem is the lowercase transformation really</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:17 UTC</span>

<span style="font-size: 90%;">Good. And thanks. I really like it how the researcher approached us _before_ publishing because we were like the only ones reacting to his charset bypasses. He informed imperva like two years ago. His talk at OWASP last Summer was heartbreaking.</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:20 UTC</span>

<span style="font-size: 90%;">oh, yeah that makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:10 UTC</span>

<span style="font-size: 90%;">Lowercase is really troubling. But even without lowercase, \@rx had the edge. But things change for longer input strings, like a User-Agent and such. But lowercase kills it all, which was a relevation for me.</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:35 UTC</span>

<span style="font-size: 90%;">note, that as I know in case of using `@rx`, then all variable matching will case insensitive - so the t:lowercase has any effect?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:38 UTC</span>

<span style="font-size: 90%;">My rule is wrong as of this writing. I changed to \@rx, but left the lowercase intact. My bad.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:45 UTC</span>

<span style="font-size: 90%;">Will fix before merging.</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:58 UTC</span>

<span style="font-size: 90%;">no, just asking independently :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:02 UTC</span>

<span style="font-size: 90%;">OK. Next PR. What do we do with [#1364](https://github.com/coreruleset/coreruleset/issues/#1364)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:17 UTC</span>

<span style="font-size: 90%;">Fix indentation and python version in crs2-renumbering script</span>

**fgs** <span style="color: grey; font-size: 90%;">19:27:00 UTC</span>

<span style="font-size: 90%;">I think _@csanders_ just updated it</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:05 UTC</span>

<span style="font-size: 90%;">yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:06 UTC</span>

<span style="font-size: 90%;">sorry</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:07 UTC</span>

<span style="font-size: 90%;">i did</span>

**fgs** <span style="color: grey; font-size: 90%;">19:27:13 UTC</span>

<span style="font-size: 90%;">The comment at the very top is wrong though</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:20 UTC</span>

<span style="font-size: 90%;">it looks pretty good, i left it at pythonv2</span>

**fgs** <span style="color: grey; font-size: 90%;">19:27:30 UTC</span>

<span style="font-size: 90%;">It should be after the #!…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:38 UTC</span>

<span style="font-size: 90%;">And Travis failing.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:40 UTC</span>

<span style="font-size: 90%;">did i do that?</span>

↳ **fgs** <span style="color: grey; font-size: 90%;">19:28:16 UTC</span>

<span style="font-size: 90%;">you did :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:49 UTC</span>

<span style="font-size: 90%;">_@csanders_: Could you please fix and merge?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:37 UTC</span>

<span style="font-size: 90%;">fuck, i did</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:38 UTC</span>

<span style="font-size: 90%;">thanks</span>

**csanders** <span style="color: grey; font-size: 90%;">19:29:34 UTC</span>

<span style="font-size: 90%;">oh, you know what -- it was the conflict resolution</span>

**csanders** <span style="color: grey; font-size: 90%;">19:29:36 UTC</span>

<span style="font-size: 90%;">that's annoying</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:54 UTC</span>

<span style="font-size: 90%;">Still conflicting it seems ... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:37 UTC</span>

<span style="font-size: 90%;">_@csanders_: Could you please fix and merge?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:54 UTC</span>

<span style="font-size: 90%;">working on it :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:36 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:31 UTC</span>

<span style="font-size: 90%;">Next one: [#1327](https://github.com/coreruleset/coreruleset/issues/#1327): <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1327>
I want to be really sure: We are going to remove all that cruft and the expense of no longer getting full information in the 980ties rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:39 UTC</span>

<span style="font-size: 90%;">_@fgs_ did a huge PR to remove this all.</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:31 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:40 UTC</span>

<span style="font-size: 90%;">well full information… it was always a bit incomplete anyway</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:06 UTC</span>

<span style="font-size: 90%;">Yes, that's why I never liked it. And it makes all rules much more complicated only because of this stuff.</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:11 UTC</span>

<span style="font-size: 90%;">yes!</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:14 UTC</span>

<span style="font-size: 90%;">will be so happy when it’s gone</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:54 UTC</span>

<span style="font-size: 90%;">I *think* i fixed [#1364](https://github.com/coreruleset/coreruleset/issues/#1364), so when its done someone can feel free to review and merge (since it's python -- not a big deal)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:34 UTC</span>

<span style="font-size: 90%;">while i have the floor for a couple seconds</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">thanks to _@fgs_ for modifying the CRS docker image to use the new updated modsecurity docker naming scheme</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:59 UTC</span>

<span style="font-size: 90%;">_@csanders_ I’ll review and merge this</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:08 UTC</span>

<span style="font-size: 90%;">there are a couple changes we'll be making to ensure checks run on v2/v3 in the coming days</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:24 UTC</span>

<span style="font-size: 90%;">but after that we *should* be able to have all our testing running against v3</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:36 UTC</span>

<span style="font-size: 90%;">which -- is pretty neat :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:53 UTC</span>

<span style="font-size: 90%;">Next one: Time to look into ReDoS prevention with [#1371](https://github.com/coreruleset/coreruleset/issues/#1371) and similar ideas. Do we want this and is 1371 a good start.
Important: We are unlikely to be able to detect all ReDoS issues automatically in the future. But we can avoid the biggest pitfalls.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:40:14 UTC</span>

<span style="font-size: 90%;">_@csanders_ are we going to keep testing against both?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:28 UTC</span>

<span style="font-size: 90%;">at least for the time being, i know most major shops still use v2</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:38 UTC</span>

<span style="font-size: 90%;">i also want to bring waffelz into the check path (if possible)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:41:06 UTC</span>

<span style="font-size: 90%;">ok, we can always have 2 test stages, one doing v2 and the other v3</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:14 UTC</span>

<span style="font-size: 90%;">yup, thats the plan</span>

**fgs** <span style="color: grey; font-size: 90%;">19:41:18 UTC</span>

<span style="font-size: 90%;">(or integration, or whatever)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:41:25 UTC</span>

<span style="font-size: 90%;">cool</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:02 UTC</span>

<span style="font-size: 90%;">Can we do this in series or how are we testing with multiple dockers?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:09 UTC</span>

<span style="font-size: 90%;">multiple dockers</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:22 UTC</span>

<span style="font-size: 90%;">i think travis will let us run them in parallel but i am still testing.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:42:24 UTC</span>

<span style="font-size: 90%;">_@dune73_ we can do in parallel with travis ci using stages</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:56 UTC</span>

<span style="font-size: 90%;">then we can add more and more as needed :slightly_smiling_face: (aka v3.0.3 and v3.0.4, etc()</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:12 UTC</span>

<span style="font-size: 90%;">I have contact with a new Swiss startup that proposes to give us room on their infrastructure to launch as many containers as we want for free.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:32 UTC</span>

<span style="font-size: 90%;">travis should already do that, but lets see</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:37 UTC</span>

<span style="font-size: 90%;">Their business case is renting out unneeded resources to be used for containers.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:01 UTC</span>

<span style="font-size: 90%;">neat</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:11 UTC</span>

<span style="font-size: 90%;">I suggest we get it up and running on travis and then we could look into that alternative to see if this would speed things up.</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:17 UTC</span>

<span style="font-size: 90%;">this may be a stupid question but would we in the future need to avoid backtracking completely if we want to be more regex engine-independent? I think RE2 has stronger DoS safety than PCRE for instance, but if I recall correctly it does not (fully?) support backtracking</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">Given we are getting more and more tests ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:06 UTC</span>

<span style="font-size: 90%;">Can we avoid backtracking and does it make sense?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:47:16 UTC</span>

<span style="font-size: 90%;">I don’t think people write regexp having backtracking in mind</span>

**fgs** <span style="color: grey; font-size: 90%;">19:47:38 UTC</span>

<span style="font-size: 90%;">To me it’s more about ensuring that it works with most of all the possible engines</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:26 UTC</span>

<span style="font-size: 90%;">_@fgs_: that's what the PCRE developer told me too :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:48:39 UTC</span>

<span style="font-size: 90%;">And try to avoid using engine specific syntax</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:43 UTC</span>

<span style="font-size: 90%;">I don’t know enough about re2 to say anything about it, but if our future is more restrictive in what we can do in rx, we will likely have to forbid more operators or patterns, in that case starting with [#1371](https://github.com/coreruleset/coreruleset/issues/#1371) as a pilot seems good and we can get more restrictive later</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:48 UTC</span>

<span style="font-size: 90%;">i like the idea even though this first grep will probably not have such good coverage</span>

**fgs** <span style="color: grey; font-size: 90%;">19:49:51 UTC</span>

<span style="font-size: 90%;">I think the idea behind 1371 is good. I feel we will hit a limitation with grep sooner or later so personally I’d like to see this as a py.test</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:19 UTC</span>

<span style="font-size: 90%;">_@fgs_: I can do that, if all agree :+1:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:50:34 UTC</span>

<span style="font-size: 90%;">But either way, we can’t make it hard fail until we fix all the patterns</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:42 UTC</span>

<span style="font-size: 90%;">Yes, sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:47 UTC</span>

<span style="font-size: 90%;">I think we do. If you can me it a base that we can expand later one, then that's a plus.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:15 UTC</span>

<span style="font-size: 90%;">Ok. We let the ticket "On hold" but we do not close it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:36 UTC</span>

<span style="font-size: 90%;">Thought: Can 1371 be hard fail and come with a list of rules where we accept 1371 to fail and then we shorten the list?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">Step by step?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:52:00 UTC</span>

<span style="font-size: 90%;">We can do that too</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:52:04 UTC</span>

<span style="font-size: 90%;">Cool idea!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:52:26 UTC</span>

<span style="font-size: 90%;">I can try that</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:56 UTC</span>

<span style="font-size: 90%;">I didn't want to write about that yet, but a few days ago I've started to work on a small tool, which parses the regex's, and try to catch the ReDoS-able pattern. It uses sre_parse modul, build the AST of regex, and tries to walk it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:42 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ You started with RXXR, did not you? Can we combine this all in the base laid by 1371?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:56:05 UTC</span>

<span style="font-size: 90%;">_@airween_ that sounds pretty cool!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:14 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ no longer around it seems. But _@airween_, if we can have your stuff within [#1371](https://github.com/coreruleset/coreruleset/issues/#1371), that's certainly cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:27 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: can you coordinate with the others?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:33 UTC</span>

<span style="font-size: 90%;">yes, sure!</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">yes, of course - I'll try to work on hardly. It's pure Python, I think it's more independent than RXXR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:16 UTC</span>

<span style="font-size: 90%;">Great. Thanks.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:38 UTC</span>

<span style="font-size: 90%;">Do you ping me, when you have results, _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:44 UTC</span>

<span style="font-size: 90%;">sure! :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:56 UTC</span>

<span style="font-size: 90%;">That's all PRs that we need to handle here, I think. More stuff or we move to issues quickly?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:59:18 UTC</span>

<span style="font-size: 90%;">Quickly, yes...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:56 UTC</span>

<span style="font-size: 90%;">Issues: Our effort in March / April to cut down on issues was fruitful, but then it stalled and now they are piling up again. Can we get rid of the new ones?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:04 UTC</span>

<span style="font-size: 90%;">CVEs aside for the moment.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:39 UTC</span>

<span style="font-size: 90%;">I can work on 1398.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:00 UTC</span>

<span style="font-size: 90%;">I am not a sqli pro, but worked a bit with these sqli regexes in the past...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:33 UTC</span>

<span style="font-size: 90%;">thank you _@franbuehler_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:02:49 UTC</span>

<span style="font-size: 90%;">Back.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:02:59 UTC</span>

<span style="font-size: 90%;">Was having a class</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:17 UTC</span>

<span style="font-size: 90%;">And 1374, or does _@SpartanTri_ would like to work on it?</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:17 UTC</span>

<span style="font-size: 90%;">I think 1389 is a more commonly seen issue. It’s because we don’t scan `REQUEST_FILENAME` for sql so heavily. That might be because of FP. If we add that, we might get some FPs. For instance a blog post with `-having-` in the slug is likely to trigger libinjection. So maybe we should do it but in PL2.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:04:43 UTC</span>

<span style="font-size: 90%;">sure I will finish 1374</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:05:11 UTC</span>

<span style="font-size: 90%;">Thank you _@walter_. You already did the work :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:13 UTC</span>

<span style="font-size: 90%;">_@walter_: makes sense. Would that lead to a lot of stricter siblings?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:29 UTC</span>

<span style="font-size: 90%;">?? [#1389](https://github.com/coreruleset/coreruleset/issues/#1389) is a closed PR about tests. What is the correct number?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:39 UTC</span>

<span style="font-size: 90%;">1398?</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:47 UTC</span>

<span style="font-size: 90%;">might be a case-by-case thing depending on FP… if I recall correctly, I did try once to let libinjection scan many things, but I ended up with the opinion that the former CRS maintainers probably knew what they did in skipping some targets :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:56 UTC</span>

<span style="font-size: 90%;">oops sorry [#1398](https://github.com/coreruleset/coreruleset/issues/#1398)</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:44 UTC</span>

<span style="font-size: 90%;">I think a sibling for 942100 on REQUEST_FILENAME would likely be of most value</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:56 UTC</span>

<span style="font-size: 90%;">Seems like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:45 UTC</span>

<span style="font-size: 90%;">Anybody interested to volunteer for  [#1346](https://github.com/coreruleset/coreruleset/issues/#1346)?</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:21 UTC</span>

<span style="font-size: 90%;">I wouldn’t mind this, but I think it would involve changes to our Docker pipeline too, so it’s not really a 1 minute thing</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:31 UTC</span>

<span style="font-size: 90%;">And do we want to do this at all?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:40 UTC</span>

<span style="font-size: 90%;">not major</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:40 UTC</span>

<span style="font-size: 90%;">No. I don't think so!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:42 UTC</span>

<span style="font-size: 90%;">yeah</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:45 UTC</span>

<span style="font-size: 90%;">i can take this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:48 UTC</span>

<span style="font-size: 90%;">I mean he has a point, but still ...</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:56 UTC</span>

<span style="font-size: 90%;">I would say we have no resources right now to do it</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:00 UTC</span>

<span style="font-size: 90%;">its not a major change of things</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:07 UTC</span>

<span style="font-size: 90%;">just renmaing and changing the dockerhub repo</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:11:13 UTC</span>

<span style="font-size: 90%;">But it's not important.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:18 UTC</span>

<span style="font-size: 90%;">yeah, exactly</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:29 UTC</span>

<span style="font-size: 90%;">Are we endorsing people using that docker image for running things off?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:41 UTC</span>

<span style="font-size: 90%;">yes, it is listed on docker-hub</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:43 UTC</span>

<span style="font-size: 90%;">Eventually yes, _@fgs_.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:01 UTC</span>

<span style="font-size: 90%;"><https://hub.docker.com/r/owasp/modsecurity-crs/></span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:03 UTC</span>

<span style="font-size: 90%;">That's why I think he has a point. Conventions are good.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:19 UTC</span>

<span style="font-size: 90%;">if you guys don't mind, i'll take that ticket</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:24 UTC</span>

<span style="font-size: 90%;">also my in house scripts and probably other people’s depend on the current location of tests, so it also will cause some inconvenience downstream</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:27 UTC</span>

<span style="font-size: 90%;">Ok, good to know. I was under the impression it was mostly (only?) for testing</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:41 UTC</span>

<span style="font-size: 90%;">But placing it under /util makes it clear it is an optional part of the project. With /dockerfile not so much.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:59 UTC</span>

<span style="font-size: 90%;">People are using this container in production.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:01 UTC</span>

<span style="font-size: 90%;">_@walter_ make a symlink?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:07 UTC</span>

<span style="font-size: 90%;">that was what i was gonna say</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:10 UTC</span>

<span style="font-size: 90%;">is that possible in git?</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:21 UTC</span>

<span style="font-size: 90%;">_@fgs_ of course, no problem, just a minor thing</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:24 UTC</span>

<span style="font-size: 90%;">I mean we can make it in the repo, not you</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:34 UTC</span>

<span style="font-size: 90%;">also, yeah if we update the dockerhub repo</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:36 UTC</span>

<span style="font-size: 90%;">and people are using that</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:40 UTC</span>

<span style="font-size: 90%;">the location of the dockerfile in the repo</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:41 UTC</span>

<span style="font-size: 90%;">yeah, you can make symlinks in git</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:42 UTC</span>

<span style="font-size: 90%;">oh yeah that’s a nice idea _@fgs_</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:42 UTC</span>

<span style="font-size: 90%;">is of no importance</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:56 UTC</span>

<span style="font-size: 90%;">its only if they are pulling the dockerfile down via a script</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:58 UTC</span>

<span style="font-size: 90%;">but the regression tests</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:00 UTC</span>

<span style="font-size: 90%;">that's a problem</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:07 UTC</span>

<span style="font-size: 90%;">although a symlink solves it nicely</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:12 UTC</span>

<span style="font-size: 90%;">and i don't think the docs are a big problem</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:26 UTC</span>

<span style="font-size: 90%;">although as some others know -- we're gonna be working with Verizon to CDN <http://coreruleset.org|coreruleset.org></span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:30 UTC</span>

<span style="font-size: 90%;">and i'll be hosting the docs on there</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:32 UTC</span>

<span style="font-size: 90%;">compiled daily</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:41 UTC</span>

<span style="font-size: 90%;">one of my backend initatives</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:43 UTC</span>

<span style="font-size: 90%;">along with a demo</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:16 UTC</span>

<span style="font-size: 90%;">So we are adding symlinks and be done with it for the time being?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:35 UTC</span>

<span style="font-size: 90%;">i think that is the plan</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:11 UTC</span>

<span style="font-size: 90%;">_@csanders_: What's the state with the work on our containers?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:25 UTC</span>

<span style="font-size: 90%;">I lost the overview...</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:27 UTC</span>

<span style="font-size: 90%;">i have to make changes to the ubuntu images</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:36 UTC</span>

<span style="font-size: 90%;">to put files into the right location</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:40 UTC</span>

<span style="font-size: 90%;">after that update the CRS image</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:42 UTC</span>

<span style="font-size: 90%;">and then we're done</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">oh and change the travis tests to use v2/v3 in parallel for testing</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:17:28 UTC</span>

<span style="font-size: 90%;">The CRS image is 6 months old. It would be cool to update it soon.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:44 UTC</span>

<span style="font-size: 90%;">yup, i'll be doing that very soon -- i have it all done with a new readme ready to go</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:46 UTC</span>

<span style="font-size: 90%;">just doing some testing</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:47 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:52 UTC</span>

<span style="font-size: 90%;">and the new images use latest</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:02 UTC</span>

<span style="font-size: 90%;">apache:latest or nginx:latest</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:11 UTC</span>

<span style="font-size: 90%;">and ubuntu:latest (will be)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:12 UTC</span>

<span style="font-size: 90%;">and add automatic updates...</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:25 UTC</span>

<span style="font-size: 90%;">yup, lets talk offline</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:30 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:47 UTC</span>

<span style="font-size: 90%;">_@csanders_: Can you give us a date when the new container will be merged?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:04 UTC</span>

<span style="font-size: 90%;">the new containers for modsec are already up</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:15 UTC</span>

<span style="font-size: 90%;">the crs one, i can commit to be the end of the week</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:23 UTC</span>

<span style="font-size: 90%;">its really just a couple line changes</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:28 UTC</span>

<span style="font-size: 90%;">shouldn't be more than hour of testing left</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:42 UTC</span>

<span style="font-size: 90%;">Sounds good. Thanks.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:43 UTC</span>

<span style="font-size: 90%;">That would be cool!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:54 UTC</span>

<span style="font-size: 90%;">Then we could also close: <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1290></span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:58 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: That would be all that is open in this domain?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:58 UTC</span>

<span style="font-size: 90%;">what is cool, is that the CRS image should work with any of the upstream iamges</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:00 UTC</span>

<span style="font-size: 90%;">*images</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:12 UTC</span>

<span style="font-size: 90%;">That's a big plus _@csanders_.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:27 UTC</span>

<span style="font-size: 90%;">after this is done i'm gonna try and bring on verizon wafelz</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:28 UTC</span>

<span style="font-size: 90%;">_@dune73_: yes, I think so.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:31 UTC</span>

<span style="font-size: 90%;">but that's not till i'm done</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:46 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ has been super helpful with all this</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:49 UTC</span>

<span style="font-size: 90%;">and _@fgs_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:52 UTC</span>

<span style="font-size: 90%;">Waflz for the win!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:01 UTC</span>

<span style="font-size: 90%;">i also have a number of open tickets with owasp</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:05 UTC</span>

<span style="font-size: 90%;">to fix the github->dockerhub sync</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:09 UTC</span>

<span style="font-size: 90%;">but for now its not a big issue\</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:17 UTC</span>

<span style="font-size: 90%;">DanE90 is also part of game, is not he?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:23 UTC</span>

<span style="font-size: 90%;">yes yes</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:28 UTC</span>

<span style="font-size: 90%;">there are a lot of people here</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:28 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">they have al helped testing</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:37 UTC</span>

<span style="font-size: 90%;">Very good.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:39 UTC</span>

<span style="font-size: 90%;">everyone in #crscontainer (which is private, msg me if you want an invite)</span>

**csanders** <span style="color: grey; font-size: 90%;">20:21:42 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:00 UTC</span>

<span style="font-size: 90%;">OK. Other issues that we should cover - or that we should force-assign to somebody?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:00 UTC</span>

<span style="font-size: 90%;">:thinking_face: don't think so right now</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:29 UTC</span>

<span style="font-size: 90%;">I would like to go to bed :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:33 UTC</span>

<span style="font-size: 90%;">we have also updated the images on the owasp swag....</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:40 UTC</span>

<span style="font-size: 90%;">They finally merged that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:09 UTC</span>

<span style="font-size: 90%;"><https://github.com/OWASP/owasp-swag/tree/master/projects/coreruleset></span>

**csanders** <span style="color: grey; font-size: 90%;">20:24:34 UTC</span>

<span style="font-size: 90%;">wow, helpful!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:34 UTC</span>

<span style="font-size: 90%;">I was going to finish with swag. _@fzipitria_ did cool work there, next step is with me (paypal account for our project) and then we can finally start to print stickers!</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:42 UTC</span>

<span style="font-size: 90%;">woot!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:01 UTC</span>

<span style="font-size: 90%;">Before we close this: _@airween_ can you give us a quick status of the open issues with ModSec3 so our test suit runs there?</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:27 UTC</span>

<span style="font-size: 90%;">yes, I can give you a very quick status: nothing happens :stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:26:38 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:52 UTC</span>

<span style="font-size: 90%;">So it's all with Trustwave and you have to wait on them to merge your stuff?</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:59 UTC</span>

<span style="font-size: 90%;">as you can see in the PR's, there are lot  of requests</span>

**airween** <span style="color: grey; font-size: 90%;">20:27:12 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">20:27:53 UTC</span>

<span style="font-size: 90%;">and there is still more one fix remain, I'm working on it too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:00 UTC</span>

<span style="font-size: 90%;">Yes, it's a lot of stuff. But you are solving real issues that lead to false negatives. They are not detecting attacks because of not immediately merging your fixes.</span>

**airween** <span style="color: grey; font-size: 90%;">20:28:20 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**airween** <span style="color: grey; font-size: 90%;">20:28:27 UTC</span>

<span style="font-size: 90%;">I'm so sorry... :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:29 UTC</span>

<span style="font-size: 90%;">We'd immediately write to trustwave, but as we have come to see in the past it does not help much.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:33 UTC</span>

<span style="font-size: 90%;">Not your fault.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:12 UTC</span>

<span style="font-size: 90%;">What we could theoretically do is a blog post that shows how to apply all your fixes and then compile v3 to get a halfway decent ModSec that covers our test suite.</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:04 UTC</span>

<span style="font-size: 90%;">or sell it as Nginx++</span>

**airween** <span style="color: grey; font-size: 90%;">20:30:09 UTC</span>

<span style="font-size: 90%;">there are one or two PR's, which not in fixed state, we should discuss about them</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:45 UTC</span>

<span style="font-size: 90%;">Are they talking to you, or are your questions / offers ignored?</span>

**airween** <span style="color: grey; font-size: 90%;">20:30:54 UTC</span>

<span style="font-size: 90%;">I miss it very much the discusses, like here the monthly meetups...</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:00 UTC</span>

<span style="font-size: 90%;">Some PR's are ready, and I just waiting for to merge them, or ask somebody me, like 'hey, wha't this?'</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:07 UTC</span>

<span style="font-size: 90%;">but nothing...</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:22 UTC</span>

<span style="font-size: 90%;">okay, in last few weeks I was very busy</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:38 UTC</span>

<span style="font-size: 90%;">I thought I'll review all of them again</span>

**airween** <span style="color: grey; font-size: 90%;">20:33:04 UTC</span>

<span style="font-size: 90%;">and send a ping to developers... let's move on</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:29 UTC</span>

<span style="font-size: 90%;">Too bad. If there is anything you think we can do, please let us know.

It's been a 2 hours meeting. I think we'll close it now. Thanks everybody for joining. Hope you catch some sleep _@fgs_. Giovanna woke me up 5 times last night.</span>

**airween** <span style="color: grey; font-size: 90%;">20:33:42 UTC</span>

<span style="font-size: 90%;">sure, thanks!</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:34:21 UTC</span>

<span style="font-size: 90%;">good night, talk you later</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:34:35 UTC</span>

<span style="font-size: 90%;">Good night! And bye</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:34:47 UTC</span>

<span style="font-size: 90%;">Sleep well</span>

**airween** <span style="color: grey; font-size: 90%;">20:34:49 UTC</span>

<span style="font-size: 90%;">bye! :wave:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:02 UTC</span>

<span style="font-size: 90%;">night all!</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:27 UTC</span>

<span style="font-size: 90%;">bye bye!!</span>

**fgs** <span style="color: grey; font-size: 90%;">20:35:33 UTC</span>

<span style="font-size: 90%;">_@dune73_ thanks. I had 4 hours sleep last night in installments :laughing:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:42 UTC</span>

<span style="font-size: 90%;">haha, to bed!</span>

**fgs** <span style="color: grey; font-size: 90%;">20:35:45 UTC</span>

<span style="font-size: 90%;">My partner is having it harder though</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:51 UTC</span>

<span style="font-size: 90%;">:disappointed:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:36:22 UTC</span>

<span style="font-size: 90%;">But she’s such a cutie is all forgiven</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:36:22 UTC</span>

<span style="font-size: 90%;">Good night all!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:44 UTC</span>

<span style="font-size: 90%;">Good night everybody!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:39:32 UTC</span>

<span style="font-size: 90%;">night all</span>

**techy** <span style="color: grey; font-size: 90%;">20:42:18 UTC</span>

<span style="font-size: 90%;">_@techy_ has joined the channel</span>

**techy** <span style="color: grey; font-size: 90%;">20:43:43 UTC</span>

<span style="font-size: 90%;">:wave: hello! _@csanders_ invited me. We both created FTW</span>

**fgs** <span style="color: grey; font-size: 90%;">20:45:19 UTC</span>

<span style="font-size: 90%;">Hello _@techy_</span>

**fgs** <span style="color: grey; font-size: 90%;">20:46:08 UTC</span>

<span style="font-size: 90%;">I’ve opened <https://github.com/CRS-support/ftw/issues/22> and also commented on <https://github.com/CRS-support/ftw/issues/19>.
If you can take a look I’d appreciate it.</span>

**techy** <span style="color: grey; font-size: 90%;">20:47:59 UTC</span>

<span style="font-size: 90%;">:+1: cool will take a look</span>

**csanders** <span style="color: grey; font-size: 90%;">20:54:55 UTC</span>

<span style="font-size: 90%;">hey _@techy_, glad you're here</span>

**techy** <span style="color: grey; font-size: 90%;">20:56:07 UTC</span>

<span style="font-size: 90%;">^^ IRT releasing on pypi - _@csanders_, whats your pypi username</span>

**techy** <span style="color: grey; font-size: 90%;">20:56:13 UTC</span>

<span style="font-size: 90%;">wouldnt want to block people if im not available</span>

**csanders** <span style="color: grey; font-size: 90%;">20:58:11 UTC</span>

<span style="font-size: 90%;">don't think i have one</span>

**techy** <span style="color: grey; font-size: 90%;">20:58:59 UTC</span>

<span style="font-size: 90%;">Wanna make one?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:59:10 UTC</span>

<span style="font-size: 90%;">of course, but it'll bea  few</span>

**csanders** <span style="color: grey; font-size: 90%;">20:59:14 UTC</span>

<span style="font-size: 90%;">just got my new monitor :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">21:21:52 UTC</span>

<span style="font-size: 90%;">_@csanders_ don’t forget to update <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1364></span>

**csanders** <span style="color: grey; font-size: 90%;">21:24:39 UTC</span>

<span style="font-size: 90%;">wtf? i already did?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:24:48 UTC</span>

<span style="font-size: 90%;">oh nvm its there</span>

**csanders** <span style="color: grey; font-size: 90%;">21:24:48 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">21:25:03 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/0609a9380461917c55b757daf4aee8d2367ad89e/util/crs2-renumbering/update.py></span>

**csanders** <span style="color: grey; font-size: 90%;">21:25:08 UTC</span>

<span style="font-size: 90%;">the latest commit is down at the bottom</span>

**csanders** <span style="color: grey; font-size: 90%;">21:26:43 UTC</span>

<span style="font-size: 90%;">i think i'll have to pull from upstream to pass tests :confused:</span>

**csanders** <span style="color: grey; font-size: 90%;">21:26:47 UTC</span>

<span style="font-size: 90%;">give me a few on that</span>

**csanders** <span style="color: grey; font-size: 90%;">21:29:35 UTC</span>

<span style="font-size: 90%;">alright, its running again -- lets see if it passes</span>

**csanders** <span style="color: grey; font-size: 90%;">21:29:38 UTC</span>

<span style="font-size: 90%;">then i'll squash all those pulls</span>

**fgs** <span style="color: grey; font-size: 90%;">21:38:06 UTC</span>

<span style="font-size: 90%;">now it looks like the history is fubar</span>

**fgs** <span style="color: grey; font-size: 90%;">21:38:09 UTC</span>

<span style="font-size: 90%;">did you rebase?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:38:15 UTC</span>

<span style="font-size: 90%;">not yet</span>

**csanders** <span style="color: grey; font-size: 90%;">21:38:21 UTC</span>

<span style="font-size: 90%;">i will rebase if it builds fine</span>

**fgs** <span style="color: grey; font-size: 90%;">21:38:28 UTC</span>

<span style="font-size: 90%;">cool</span>

**csanders** <span style="color: grey; font-size: 90%;">21:38:31 UTC</span>

<span style="font-size: 90%;">i just pulled in the changes</span>

**csanders** <span style="color: grey; font-size: 90%;">21:38:34 UTC</span>

<span style="font-size: 90%;">from v3.2/dev</span>

**fgs** <span style="color: grey; font-size: 90%;">21:38:36 UTC</span>

<span style="font-size: 90%;">Can you move the comment after the bang though?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:38:47 UTC</span>

<span style="font-size: 90%;">yeah i should be able to do that</span>

**Somdev Sangwan** <span style="color: grey; font-size: 90%;">21:42:23 UTC</span>

<span style="font-size: 90%;">_@Somdev Sangwan_ has joined the channel</span>

**csanders** <span style="color: grey; font-size: 90%;">21:47:51 UTC</span>

<span style="font-size: 90%;">_@fgs_</span>

**csanders** <span style="color: grey; font-size: 90%;">21:47:56 UTC</span>

<span style="font-size: 90%;">i may have foobared that</span>

**csanders** <span style="color: grey; font-size: 90%;">21:47:56 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">21:48:10 UTC</span>

<span style="font-size: 90%;">i thought if i rolled back to that previous committ and then merged it would work fine</span>

**csanders** <span style="color: grey; font-size: 90%;">21:48:15 UTC</span>

<span style="font-size: 90%;">but it still left all that garbage</span>

**csanders** <span style="color: grey; font-size: 90%;">21:48:47 UTC</span>

<span style="font-size: 90%;">i guess i could still rebase and manually squash all that</span>

**csanders** <span style="color: grey; font-size: 90%;">21:48:48 UTC</span>

<span style="font-size: 90%;">yuck</span>

