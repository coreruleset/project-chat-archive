### Mon, Mar 4th, 2024

**dune73** <span style="color: grey; font-size: 90%;">19:30:46 UTC</span>

<span style="font-size: 90%;">Hello, time for our monthly chat!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:55 UTC</span>

<span style="font-size: 90%;">Hey</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:31:05 UTC</span>

<span style="font-size: 90%;">Hello</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:31:18 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:33 UTC</span>

<span style="font-size: 90%;">Hello</span>

**jit** <span style="color: grey; font-size: 90%;">19:31:34 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:34 UTC</span>

<span style="font-size: 90%;">Hi there, good to see you all</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:58 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is in a call but might be listening on one ear.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:09 UTC</span>

<span style="font-size: 90%;">hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:09 UTC</span>

<span style="font-size: 90%;">He should join us fully in half an hour.</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">hi everyone!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:11 UTC</span>

<span style="font-size: 90%;">Special welcome to _@Esad Cetiner_, first meeting as "real" developer!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:27 UTC</span>

<span style="font-size: 90%;">(Very sorry this happens in the middle of the night for you.)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:34:47 UTC</span>

<span style="font-size: 90%;">the new times are actually a bit better (6:30AM) so it's not as bad as 4:00AM</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:35:39 UTC</span>

<span style="font-size: 90%;">ah, you are already awake since 4:00 but more fresh? :slightly_smiling_face:</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:36:06 UTC</span>

<span style="font-size: 90%;">depends on the day</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:12 UTC</span>

<span style="font-size: 90%;">The times are the same with GMT, it's maybe your Summer time ...</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:35:23 UTC</span>

<span style="font-size: 90%;">maybe</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:39 UTC</span>

<span style="font-size: 90%;">ah, you are already awake since 4:00 but more fresh? :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:35:39 UTC</span>

<span style="font-size: 90%;">ah, you are already awake since 4:00 but more fresh? :slightly_smiling_face:</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:36:06 UTC</span>

<span style="font-size: 90%;">depends on the day</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:41 UTC</span>

<span style="font-size: 90%;">Ah, no, not the same GMT, the same CET/CEST</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:04 UTC</span>

<span style="font-size: 90%;">And if we do 1 hour in one direction and you go 1 hour in the other direction, we jump 2 hours.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:56 UTC</span>

<span style="font-size: 90%;">You have seen the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:06 UTC</span>

<span style="font-size: 90%;">The new changes-pending makes the rule stuff in the agenda much easier.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">And I think this actually helps our audience with the chat-archive, since you see new changes at a single glance every month now. In a new standardized format (PR names are not as readable).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:45 UTC</span>

<span style="font-size: 90%;">If we look over the various news items, there is this surge in nextcloud activity that I do not really understand. What's happening there? It has to do with testing, but also with moving to PL4? Can somebody explain?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">Yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:05 UTC</span>

<span style="font-size: 90%;">Firstly, _@Esad Cetiner_ has done a ton of work on the Nextcloud plugin. Two weeks ago, another large chunk was added, Nextcloud Office support, IIRC.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:40:46 UTC</span>

<span style="font-size: 90%;">Yes, mainly Nextcloud Office</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:52 UTC</span>

<span style="font-size: 90%;">With the release of the v4 images, the plugin tests now use those and so we saw that many tests suddenly started to fail.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:48 UTC</span>

<span style="font-size: 90%;">It turned out that a slight misconfiguration in the docker-compose file used for running the test suite meant that, previously, all tests were run at PL1, not PL4 as was assumed to be configured.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:47 UTC</span>

<span style="font-size: 90%;">So me, _@azurIt_ and _@Esad Cetiner_ spent some time to clean that up. Tests for other plugins (probably Wordpress), may start to fail with new PRs and we'll have to deal with the issue then</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">What is the effect of running tests at PL1 vs PL4? You do not get the PL2 FPs, or what's the matter. I do not yet get this.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:22 UTC</span>

<span style="font-size: 90%;">You don't see effects of rules > PL1</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:59 UTC</span>

<span style="font-size: 90%;">Rembember, these are tests for exclusions, and you know how it is with negative tests... :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:06 UTC</span>

<span style="font-size: 90%;">Absolutely.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:38 UTC</span>

<span style="font-size: 90%;">So you want to test for the absence of further FPs at say PL2, so you have to make sure the tests run at >= PL2. Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:46 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:26 UTC</span>

<span style="font-size: 90%;">In CRS, we run at PL 4, but since the tests are usually positive test, we wouldn't run into the same issue, unless we tested for PL2 stuff</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:13 UTC</span>

<span style="font-size: 90%;">I see this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:41 UTC</span>

<span style="font-size: 90%;">And now with switching to PL4, there were many new PL2 FPs, or what's the deal exactly.
And how does this affect other plugins?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:04 UTC</span>

<span style="font-size: 90%;">(Just trying to get a clearer picture here, since I did not follow this, and I reckon I'm not the only one.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">Yes, new FPs. In some instances, additional targets because we hadn't really tested the rule and only gone off the log entries.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:39 UTC</span>

<span style="font-size: 90%;">The same could be true for other plugins</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:56 UTC</span>

<span style="font-size: 90%;">Because all plugin tests are now at PL4 if I read this correctly and we better look through all RE plugins anew.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:59 UTC</span>

<span style="font-size: 90%;">Yes. However, Nextcloud is surely affected the most because of all the new rules. Most of the other plugins don't have tests anyway.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:35 UTC</span>

<span style="font-size: 90%;">And it does not really change anythign for our users, it's just a question of visibility of the FPs.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:42 UTC</span>

<span style="font-size: 90%;">Correct.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:07 UTC</span>

<span style="font-size: 90%;">Good. Thank you for explaining this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:25 UTC</span>

<span style="font-size: 90%;">Anything else in the news section?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:03 UTC</span>

<span style="font-size: 90%;">We had discussed the toolchain release two weeks ago already, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:35 UTC</span>

<span style="font-size: 90%;">Yes, probably, but I thought it worthwhile to add it here under news and I could not remember properly.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:08 UTC</span>

<span style="font-size: 90%;">It was only a discussion and not an easy to find summary after all.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:24 UTC</span>

<span style="font-size: 90%;">Ok. Summary: crs-toolchain 2.0.0 was released with improvements to regular expression generation. In general, expressions will now be slightly shorter. We had to regenerate all expressions because of that but the changes were only syntactical.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:54 UTC</span>

<span style="font-size: 90%;">Thanks. Can somebody please update the agenda?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:56:07 UTC</span>

<span style="font-size: 90%;">Will do</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:17 UTC</span>

<span style="font-size: 90%;">Next: There is a tiny issue with the changelog PRs. If we update one of these changelog-PRs then somebody else has to approve and merge. With multiple changelog PRs per day this starts to take some coordination bc of the merge conflicts.
Is there a way around this for changelog-PRs?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:37 UTC</span>

<span style="font-size: 90%;">Sorry, I thought they were no decisions so far :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:47 UTC</span>

<span style="font-size: 90%;">This was not a decision.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:59 UTC</span>

<span style="font-size: 90%;">It was an addendum to the news section (there was a FIXME under tools).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:41 UTC</span>

<span style="font-size: 90%;">One solution I see is making 1 changelog-PR per day instead 1 changelog-PR per day per merging dev.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:00 UTC</span>

<span style="font-size: 90%;">Multipls changelog-PRs per day are easier to assign to various merging devs, obviously.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:30 UTC</span>

<span style="font-size: 90%;">Is there any GitHub magic that can help here with the merge conflicts?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:00:13 UTC</span>

<span style="font-size: 90%;">Yes, merge queue maybe. We'd have to try that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:59:51 UTC</span>

<span style="font-size: 90%;">We could also introduce sections. That would be one section per dev. Or one file per dev.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:36 UTC</span>

<span style="font-size: 90%;">Merge queue might actually be a good idea _@xanadu_</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:55 UTC</span>

<span style="font-size: 90%;">It would help in other cases too. I'll look into that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:00 UTC</span>

<span style="font-size: 90%;">I take it it is not possible to introduce exceptions for "different approver from latest committer on a PR"?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:01:37 UTC</span>

<span style="font-size: 90%;">It should be...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:38 UTC</span>

<span style="font-size: 90%;">I mean it's a very useful rule, but with the changelog-PRs is unnecessary admin overhead.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:11 UTC</span>

<span style="font-size: 90%;">How would merge queing work?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:12 UTC</span>

<span style="font-size: 90%;">Very abstract: PRs are decoupled in time, which is why we get merge conflicts. If you put them in a queue then they are coupled in time and you know in which order to resolve them. I'm not an expert on this though.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:58 UTC</span>

<span style="font-size: 90%;">Interesting concept. You would create said queue when creating the PRs automatically and they can then only be merged in that order?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:15 UTC</span>

<span style="font-size: 90%;">That would actually help a lot with changelog-PRs.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:18 UTC</span>

<span style="font-size: 90%;">It's a feature on GitHub</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:33 UTC</span>

<span style="font-size: 90%;">Pretty much, yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:51 UTC</span>

<span style="font-size: 90%;">If somebody has the time to try this out, that would be sweet.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:06 UTC</span>

<span style="font-size: 90%;">It's no big deal, but it can become one when we merge in a frenzy.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:32 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:42 UTC</span>

<span style="font-size: 90%;">Next up is our first release where we really feel our new release policy. What do we do with 4.1?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:06 UTC</span>

<span style="font-size: 90%;">4.1.0 to be precise.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:10 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:35 UTC</span>

<span style="font-size: 90%;">I think the release date would be good to be after the second chat of the month, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:46 UTC</span>

<span style="font-size: 90%;">So once we round that, I'll schedule the release</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:48 UTC</span>

<span style="font-size: 90%;">That's a good plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:58 UTC</span>

<span style="font-size: 90%;">Freeze time +/- at the 2nd meeting?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:08:51 UTC</span>

<span style="font-size: 90%;">Not sure if this possible yet (so much to do), but in the future we should try to not have to freeze.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:20 UTC</span>

<span style="font-size: 90%;">So new fixes can go in right up to the last minute?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:37 UTC</span>

<span style="font-size: 90%;">If that's the idea/benefit?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:41 UTC</span>

<span style="font-size: 90%;">That's the idea yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:53 UTC</span>

<span style="font-size: 90%;">I did not mean a technical freeze.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:58 UTC</span>

<span style="font-size: 90%;">I realize that, right now, it would be hard because of updating version numbers etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:00 UTC</span>

<span style="font-size: 90%;">I meant more like a cut-off time.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:16 UTC</span>

<span style="font-size: 90%;">Cut off for 4.1.0, but if we need a 4.1.1 fixing something the next day, we can</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:46 UTC</span>

<span style="font-size: 90%;">Would we do a branch and then update version numbers, tags etc in that branch, then release?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:02 UTC</span>

<span style="font-size: 90%;">Basically a PR</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:29 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:12:54 UTC</span>

<span style="font-size: 90%;">Yes. We need to automate releasing, and we are done</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:41 UTC</span>

<span style="font-size: 90%;">All for that. We'll get practice and automate this a bit better every cycle.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:13 UTC</span>

<span style="font-size: 90%;">Does anybody see a need for a 4.0.1 before a we do 4.1.0 or together with 4.1.0?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:30 UTC</span>

<span style="font-size: 90%;">(Personally, I do not see a need.)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:36 UTC</span>

<span style="font-size: 90%;">No need</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:38 UTC</span>

<span style="font-size: 90%;">If 4.0 is not an LTS release then we don't need to do x.x.1 releases, right?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:47 UTC</span>

<span style="font-size: 90%;">(If I understand the plan correctly)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:53 UTC</span>

<span style="font-size: 90%;">If there is a security release for the 4.0 release line before we would probably bring out 4.1.0, we might do a 4.0.1 security release without it being an LTS. But it's rather hypothetical.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:03 UTC</span>

<span style="font-size: 90%;">We could also speed up 4.1.0 in such a situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:46 UTC</span>

<span style="font-size: 90%;">What do we want to tackle next, some technical question for a change or more project policy?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:24 UTC</span>

<span style="font-size: 90%;">Then let's do the plugin changelogs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:29 UTC</span>

<span style="font-size: 90%;">What is your take on that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:23:55 UTC</span>

<span style="font-size: 90%;">I understand why we'd want a changelog file for CRS core. But as you know, the overhead required to build it in the way we want is quite big. I don't think it makes any sense to devote the same amount of energy on plugin changelogs.
</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:26 UTC</span>

<span style="font-size: 90%;">My suggestion: remove the changelog files from plugin repositories and simply do regular GH releases.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:58 UTC</span>

<span style="font-size: 90%;">I think that makes sense for individual PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:13 UTC</span>

<span style="font-size: 90%;">But what about big changes, important feature changes?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:27 UTC</span>

<span style="font-size: 90%;">Regular releases based on PRs title should be the case</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:34 UTC</span>

<span style="font-size: 90%;">Like the things we listed on top of the CRS4 changelog.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:47 UTC</span>

<span style="font-size: 90%;">Those would be hidden with all the automated rest.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:49 UTC</span>

<span style="font-size: 90%;">That might be a blogpost</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:11 UTC</span>

<span style="font-size: 90%;">It could, or said manual touch up.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:12 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:45 UTC</span>

<span style="font-size: 90%;">Yes, let's do this. Definitely better than the admin overhead for FP PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:34 UTC</span>

<span style="font-size: 90%;">Good, so that's settled too. We're much faster than I thought tonight...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:45 UTC</span>

<span style="font-size: 90%;">Decoding.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:46 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3450](https://github.com/coreruleset/coreruleset/pull/3450)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:05 UTC</span>

<span style="font-size: 90%;">I think this is a policy decision that will affect several rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:16 UTC</span>

<span style="font-size: 90%;">Are we ready for a clear policy?</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:28:30 UTC</span>

<span style="font-size: 90%;">Good evening, I’m very sorry but wasn’t able to come earlier.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:31 UTC</span>

<span style="font-size: 90%;">Hello _@emphazer_, thanks for joining.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:42 UTC</span>

<span style="font-size: 90%;">No worries.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:22 UTC</span>

<span style="font-size: 90%;">I'm a little worried about this one. It's similar to the JSON / Unicode issue we had, where we played around with double decoding. Who says that the new way is the correct way to decode? If I want to evade, I can simply encode Unicode with URL encoding.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:42 UTC</span>

<span style="font-size: 90%;">Me too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:53 UTC</span>

<span style="font-size: 90%;">And I do not think we have really thought about this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:05 UTC</span>

<span style="font-size: 90%;">enough, I mean.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:15 UTC</span>

<span style="font-size: 90%;">Obviously, the evasion argument is true for the current state of the rule as well</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:30 UTC</span>

<span style="font-size: 90%;">There was even a GSoC idea for 2-3 years to come up with a concept about order of tranformations.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:50 UTC</span>

<span style="font-size: 90%;">I think we need to think about evasions and what typical backends do in terms of decoding.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:22 UTC</span>

<span style="font-size: 90%;">If we can force an attacker to triple encode or do crazy stuff so the backend ignores it, we win.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:26 UTC</span>

<span style="font-size: 90%;">Or at least that's my thinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:30 UTC</span>

<span style="font-size: 90%;">But we need to know more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:35 UTC</span>

<span style="font-size: 90%;">Also the final ModSec / Coraza URI decoding behavior of REQUEST_URI is not sorted out yet. Will easy be another month to be honest (And that will be only the decision, not the code and the distros and the installations updated).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:44 UTC</span>

<span style="font-size: 90%;">So what do we do here?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:37:49 UTC</span>

<span style="font-size: 90%;">This should be a document</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:37:59 UTC</span>

<span style="font-size: 90%;">And we receive comments</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:27 UTC</span>

<span style="font-size: 90%;">The solution / policy would be a document / part of CONTRIBUTING.md.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:31 UTC</span>

<span style="font-size: 90%;">Or do I get you wrong?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:43 UTC</span>

<span style="font-size: 90%;">I think that the proposed change messes with the semantics. I would be ok with the following change:
- t:none,t:utf8toUnicode,t:urlDecodeUni,t:htmlEntityDecode,t:jsDecode,t:cssDecode,t:removeNulls,\
+ t:none,t:utf8toUnicode,t:urlDecodeUni,t:utf8toUnicode,t:htmlEntityDecode,t:jsDecode,t:cssDecode,t:removeNulls,\</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:40:05 UTC</span>

<span style="font-size: 90%;">With multi match?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:41:23 UTC</span>

<span style="font-size: 90%;">Maybe... Not necessarily though. I mean, it would be good, but the performance overhead...</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:40:44 UTC</span>

<span style="font-size: 90%;">We did something very similar (double decoding like that) with the 941xxx rules a few months ago, and then it was all removed a few weeks later.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:42:08 UTC</span>

<span style="font-size: 90%;">Really? Why?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:42:49 UTC</span>

<span style="font-size: 90%;">I think it was "deemed not to be a valid evasion/attack vector". Although a user wrote in with it as a false negative, so :shrug:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:43:03 UTC</span>

<span style="font-size: 90%;">oh</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:43:34 UTC</span>

<span style="font-size: 90%;">Ah yes, I recall. I think we decided that it was application dependent.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:44:06 UTC</span>

<span style="font-size: 90%;">The payload was something like base64 encoded in a JSON in a cookie, or something like that</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:44:31 UTC</span>

<span style="font-size: 90%;">I should also get the auto-decode plugin back in shape ...</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:41:03 UTC</span>

<span style="font-size: 90%;">Might be best to be certain we want to do that before putting the effort in to make those changes, write the tests, etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:08 UTC</span>

<span style="font-size: 90%;">My thinking too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:36 UTC</span>

<span style="font-size: 90%;">But somehow nobody really wants to explore this topic deep enough so we can really come up with a policy.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:44:30 UTC</span>

<span style="font-size: 90%;">Because it's hard, not fun :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:56 UTC</span>

<span style="font-size: 90%;">I'd rather clean my house with a toothbrush.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:45:40 UTC</span>

<span style="font-size: 90%;">Hi</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:46:41 UTC</span>

<span style="font-size: 90%;">We need to nail a few people down to tackle this, otherwise it will be buried in the backlog</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:59 UTC</span>

<span style="font-size: 90%;">We could pull straws ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:47:04 UTC</span>

<span style="font-size: 90%;">I'll help but I can't take the lead</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:22 UTC</span>

<span style="font-size: 90%;">Or make it a dev-retreat topic (and then nobody shows up).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:49:48 UTC</span>

<span style="font-size: 90%;">Merge queue won't help with the merge conflicts on changelog PRs. We should still enable it though, it will make our lives easier.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:49:48 UTC</span>

<span style="font-size: 90%;">Merge queue won't help with the merge conflicts on changelog PRs. We should still enable it though, it will make our lives easier.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:12 UTC</span>

<span style="font-size: 90%;">OK, I guess we do not have a volunteer just yet. But I really think we need to keep this on the table.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:26 UTC</span>

<span style="font-size: 90%;">Let's move on for the meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:18 UTC</span>

<span style="font-size: 90%;">So there is this virtual env maintenance question I brought up in the dev channel today; namely with regards to sandbox maintenance and potential future status page envs maintenance.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:33 UTC</span>

<span style="font-size: 90%;">Is this going to be a real problem at all or is it something, I am making up?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:52:34 UTC</span>

<span style="font-size: 90%;">It seems uncontroversial to allocate x% of the project budget to maintain our systems. I guess the question is what percentage should x be :stuck_out_tongue:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:52:49 UTC</span>

<span style="font-size: 90%;">And who will be y</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:55 UTC</span>

<span style="font-size: 90%;">I do not think we can easily assign the right x, but we can make an assumption and state that we will give it a shot and then maybe adjust in subsequent years. Apparently also a question of having ready money.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:08 UTC</span>

<span style="font-size: 90%;">But as it's time to finish our budget for the year, we should kind of decide now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:38 UTC</span>

<span style="font-size: 90%;">(Or next week, but not in September unless we have good reasons)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:44 UTC</span>

<span style="font-size: 90%;">We can also allocate and then not use it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:51 UTC</span>

<span style="font-size: 90%;">We've done that before several times.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:55:07 UTC</span>

<span style="font-size: 90%;">A generous over-budget, and then adjust down next year</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:55:41 UTC</span>

<span style="font-size: 90%;">We can use the overhead to take _@dune73_ to a fancy historical restaurant.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:55:28 UTC</span>

<span style="font-size: 90%;">I guess someone needs to make a realistic forecast before that, though.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:55:41 UTC</span>

<span style="font-size: 90%;">We can use the overhead to take _@dune73_ to a fancy historical restaurant.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:55:41 UTC</span>

<span style="font-size: 90%;">We can use the overhead to take _@dune73_ to a fancy historical restaurant.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:25 UTC</span>

<span style="font-size: 90%;">If there is a single fancy historical restaurant, it's "The Olde Hansa" in Talinn. I'm all for using any overhead to invite the team to Estonia.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:43 UTC</span>

<span style="font-size: 90%;">Beautiful historical cities, nice and incomprehensible people.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:46 UTC</span>

<span style="font-size: 90%;">And great food.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:39 UTC</span>

<span style="font-size: 90%;">(For the record: [https://www.oldehansa.ee/](https://www.oldehansa.ee/))</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:57:57 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is probably best equipped to give an estimate of the amount of maintenance work.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:39 UTC</span>

<span style="font-size: 90%;">One big question is if we can bring Status Page of the ground. Then if it's going to be 2 envs at the end of the year or 12.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:32 UTC</span>

<span style="font-size: 90%;">Next question is if there is anybody interested in the team to deliver this with a reasonable SLA, or if we look on the market.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:00:38 UTC</span>

<span style="font-size: 90%;">Let's try to get an estimate from _@fzipitria_ for sandbox + status page for Azure until the end of the year. Then go from there.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:56 UTC</span>

<span style="font-size: 90%;">Oops</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:58 UTC</span>

<span style="font-size: 90%;">Ok</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:08 UTC</span>

<span style="font-size: 90%;">(sorry at my class)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:15 UTC</span>

<span style="font-size: 90%;">OK. So you are mostly open to the idea generally and it's more a question of how much and whom?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:53 UTC</span>

<span style="font-size: 90%;">(I'm fine with that. I just wanted to be sure you are OK with spending money here. I do not want to spoil the fun of somebody who enjoys maintenance as a hobby.)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:25 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:31 UTC</span>

<span style="font-size: 90%;">One last thing (from me).</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:22 UTC</span>

<span style="font-size: 90%;">This may be stupid, but if we do / _@fzipitria_ does the new website on [github.io](http://github.io). It will still be available on [coreruleset.org](http://coreruleset.org). Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:05:01 UTC</span>

<span style="font-size: 90%;">You can link a public domain to a GitHub page, yes</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:05:39 UTC</span>

<span style="font-size: 90%;">Will github host also DNS?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:06:12 UTC</span>

<span style="font-size: 90%;">Pretty sure, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:33 UTC</span>

<span style="font-size: 90%;">Thanks for the clarification.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:06:59 UTC</span>

<span style="font-size: 90%;">Actually, no.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:06 UTC</span>

<span style="font-size: 90%;">Sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:11 UTC</span>

<span style="font-size: 90%;">Felipe has done a lot of progress with this. So this is pretty close, with all former blog posts still available at old URI.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:23 UTC</span>

<span style="font-size: 90%;">[https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages#using-an-[…]pages-site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages#using-an-apex-domain-for-your-github-pages-site)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:29 UTC</span>

<span style="font-size: 90%;">So we need to host DNS ourselves / at cloudflare?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:46 UTC</span>

<span style="font-size: 90%;">Yes, we'll have to have a DNS provider.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:13 UTC</span>

<span style="font-size: 90%;">That will then point to our static page running on [github.io](http://github.io).</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:08:26 UTC</span>

<span style="font-size: 90%;">yes</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:08:53 UTC</span>

<span style="font-size: 90%;">So we need DNS provider and domain registrar.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:09:32 UTC</span>

<span style="font-size: 90%;">What about email? Are we using it on [coreruleset.org](http://coreruleset.org)?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:04 UTC</span>

<span style="font-size: 90%;">We have a security@...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:07 UTC</span>

<span style="font-size: 90%;">So yes.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:10:33 UTC</span>

<span style="font-size: 90%;">So we need also email provider.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:45 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:02 UTC</span>

<span style="font-size: 90%;">We can stay with what we have, we just need a simple change</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:15 UTC</span>

<span style="font-size: 90%;">No worries, I can do the change for the website</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:36 UTC</span>

<span style="font-size: 90%;">Folks just need to review things</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:11:41 UTC</span>

<span style="font-size: 90%;">And what is what we have?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:11 UTC</span>

<span style="font-size: 90%;">[coreruleset.github.io/website](http://coreruleset.github.io/website)</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">21:13:08 UTC</span>

<span style="font-size: 90%;">you misspelled github
[coreruleset.github.io/website](http://coreruleset.github.io/website)</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:12:26 UTC</span>

<span style="font-size: 90%;">I think he means DNS, e-mail, etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:21 UTC</span>

<span style="font-size: 90%;">We're with Walter's company [slik.nl](http://slik.nl).</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:42 UTC</span>

<span style="font-size: 90%;">His partner told us we can stay forever if we want. But probably time to move on.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:09 UTC</span>

<span style="font-size: 90%;">I mean it's no big deal. This could be any service. But apparently _@azurIt_ offers it too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:15 UTC</span>

<span style="font-size: 90%;">DNS is in cloudflare</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:39 UTC</span>

<span style="font-size: 90%;">We can take this offline</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:15:01 UTC</span>

<span style="font-size: 90%;">My idea was that expose the website itself, not the internals</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:09 UTC</span>

<span style="font-size: 90%;">?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:13 UTC</span>

<span style="font-size: 90%;">What do you mean?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:15:40 UTC</span>

<span style="font-size: 90%;">I mean DNS, hosting, email, that's not that relevant now</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:32 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:16:55 UTC</span>

<span style="font-size: 90%;">So let's review the "new" website content</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:02 UTC</span>

<span style="font-size: 90%;">And we can migrate</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:21 UTC</span>

<span style="font-size: 90%;">Sounds like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:46 UTC</span>

<span style="font-size: 90%;">If I got you write, we need to test for broken links across the whole repo. Correct?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:38 UTC</span>

<span style="font-size: 90%;">And weird showing content</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:41 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:00 UTC</span>

<span style="font-size: 90%;">And look at the readme, see if everything works locally for you</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:03 UTC</span>

<span style="font-size: 90%;">Etc</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:55 UTC</span>

<span style="font-size: 90%;">Is it ready for review now? Or still work to be done from you?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:02 UTC</span>

<span style="font-size: 90%;">We'll I guess that's it for tonight then. You've seen the URI for the website. Please take a peek and then we'll do a systematic review.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:23 UTC</span>

<span style="font-size: 90%;">Thank you all for joining. Looking fwd to 4.1.0.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:23:53 UTC</span>

<span style="font-size: 90%;">bb :blob-wave:</span>

**jit** <span style="color: grey; font-size: 90%;">21:23:55 UTC</span>

<span style="font-size: 90%;">Goodnight everyone</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">21:24:02 UTC</span>

<span style="font-size: 90%;">bye</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:24:09 UTC</span>

<span style="font-size: 90%;">good night :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:24:14 UTC</span>

<span style="font-size: 90%;">Night.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:24:16 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:24:26 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

**airween** <span style="color: grey; font-size: 90%;">21:25:05 UTC</span>

<span style="font-size: 90%;">bye!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:25:25 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3530#issuecomment-1977383432](https://github.com/coreruleset/coreruleset/issues/3530#issuecomment-1977383432)</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:25:26 UTC</span>

<span style="font-size: 90%;">Good night</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:26:47 UTC</span>

<span style="font-size: 90%;">Bye</span>

