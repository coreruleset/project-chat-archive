### Mon, Nov 3rd, 2025

**maxleske** <span style="color: grey; font-size: 90%;">19:30:27 UTC</span>

<span style="font-size: 90%;">Hi all, welcome to the monthly chat</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:13 UTC</span>

<span style="font-size: 90%;">hi, good evening!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:17 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:45 UTC</span>

<span style="font-size: 90%;">Please take a couple of minutes to read the meeting agenda: [https://github.com/coreruleset/coreruleset/issues/4317](https://github.com/coreruleset/coreruleset/issues/4317)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:31:48 UTC</span>

<span style="font-size: 90%;">Hello :wave:</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:32:32 UTC</span>

<span style="font-size: 90%;">Hello :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:21 UTC</span>

<span style="font-size: 90%;">Hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:25 UTC</span>

<span style="font-size: 90%;">Let's get started.</span>

**Conor Rynne** <span style="color: grey; font-size: 90%;">19:36:56 UTC</span>

<span style="font-size: 90%;">Hiii</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:14 UTC</span>

<span style="font-size: 90%;">Good news: OWASP has greenlit the payment of the hotel, so you all will have somewhere to sleep when you get to Bern :wink:</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:38 UTC</span>

<span style="font-size: 90%;">ah, yes, that's definitely a very good news :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:02 UTC</span>

<span style="font-size: 90%;">We have three issues to discuss tonight. The first one: [https://github.com/coreruleset/coreruleset/pull/4291](https://github.com/coreruleset/coreruleset/pull/4291)</span>

↳ **Vincent - TW** <span style="color: grey; font-size: 90%;">19:42:08 UTC</span>

<span style="font-size: 90%;">This rule now has fewer false positives than most PL1 XSS rules, thanks to the new regex observed on your infrastructure - mostly PHP e-commerce CMSs.

Since it catches critical flaws, it would be wise to downgrade it to PL1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:50 UTC</span>

<span style="font-size: 90%;">For reference, the last change to the regular expression of that rule is from 5 months ago, when we removed the exclusion of the `_utm` cookie prefifx</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:00 UTC</span>

<span style="font-size: 90%;">Is there a link to the change so we can see?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:09 UTC</span>

<span style="font-size: 90%;">_@Vincent - TW_ I'm not sure which change to the regex you are referring too.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:42:39 UTC</span>

<span style="font-size: 90%;">This one : [https://github.com/coreruleset/coreruleset/blob/main/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf#L837](https://github.com/coreruleset/coreruleset/blob/main/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf#L837)</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:43:51 UTC</span>

<span style="font-size: 90%;">This isn't a change though</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:15 UTC</span>

<span style="font-size: 90%;">You mention a "change to the regex". Which one was that?</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:43:17 UTC</span>

<span style="font-size: 90%;">This rule now has fewer false positives than most PL1 XSS rules, thanks to the new regex observed on your infrastructure - mostly PHP e-commerce CMS.

Since it catches critical flaws, imo, it would be wise to downgrade it to PL1.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:44:08 UTC</span>

<span style="font-size: 90%;">The previous one was a nightmare - it caught all Base64 sequences.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:46 UTC</span>

<span style="font-size: 90%;">Which was the previous one? I can't find it.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:44:53 UTC</span>

<span style="font-size: 90%;">`(?i)[\s\"'`;\/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]+[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=` I think</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:00 UTC</span>

<span style="font-size: 90%;">Can you share the PR _@Vincent - TW_?</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:45:21 UTC</span>

<span style="font-size: 90%;">I don't known when you updated the regex - but the new is perfect.</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:40 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/commit/ff153384730e77c875973dcb769d6148a98a8a33#diff-49c831b25b258f29245a1f[…]ab352750ce88056e2bfR81-R836](https://github.com/coreruleset/coreruleset/commit/ff153384730e77c875973dcb769d6148a98a8a33#diff-49c831b25b258f29245a1fa974e05ccdffd3a16e2294bab352750ce88056e2bfR81-R836)</span>

↳ **Vincent - TW** <span style="color: grey; font-size: 90%;">19:46:45 UTC</span>

<span style="font-size: 90%;">it's not this one, it's older i guess</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:30 UTC</span>

<span style="font-size: 90%;">That commit only removed an _exclusion_. It didn't change the regex.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:47 UTC</span>

<span style="font-size: 90%;">ah, sorry</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:52 UTC</span>

<span style="font-size: 90%;">you're right</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:10 UTC</span>

<span style="font-size: 90%;">As far as I can tell, the regex hasn't changed in over 4 years. _@Vincent - TW_, please clarify this in the PR. We need to know what you mean exactly.</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:51 UTC</span>

<span style="font-size: 90%;">it was changed in 2024:
[https://github.com/coreruleset/coreruleset/commit/e1806e08de40cf489e2cd5950d23601eda6a6883#diff-49c831b25b258f29245a1f[…]294bab352750ce88056e2bfR807](https://github.com/coreruleset/coreruleset/commit/e1806e08de40cf489e2cd5950d23601eda6a6883#diff-49c831b25b258f29245a1fa974e05ccdffd3a16e2294bab352750ce88056e2bfR807)
but I'm not sure that's a significant change</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:51:06 UTC</span>

<span style="font-size: 90%;">I don't think so. If anything, that change would have increased the chances for FPs</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:51 UTC</span>

<span style="font-size: 90%;">Let's move on to the second topic, maybe _@Vincent - TW_ will have an update by the end of the chat.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:31 UTC</span>

<span style="font-size: 90%;">Next one: [https://github.com/coreruleset/coreruleset/pull/3813](https://github.com/coreruleset/coreruleset/pull/3813)</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:51:55 UTC</span>

<span style="font-size: 90%;">I don’t understand why it’s so important to know when it was edited.

I’m simply saying that this regex now has fewer false positives than most PL1 XSS rules, that it still catches dangerous payloads, and that we should reconsider making it PL1 to encourage third parties to enable it.

I check on 4.0.0 ([https://github.com/coreruleset/coreruleset/archive/refs/tags/v4.0.0.zip](https://github.com/coreruleset/coreruleset/archive/refs/tags/v4.0.0.zip)), the regex was :

(?i)[\s\"'`;/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]{3,25}[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=[^=]</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:52:53 UTC</span>

<span style="font-size: 90%;">Sorry, I need to go to my son. I'll update the decisions afterwards.</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:20 UTC</span>

<span style="font-size: 90%;">why it’s so important to know when it was editedthe question is not _when_, but _what_ was edited.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:53:29 UTC</span>

<span style="font-size: 90%;">On [https://github.com/coreruleset/coreruleset/releases/tag/v3.3.5](https://github.com/coreruleset/coreruleset/releases/tag/v3.3.5) this was the previous regex : (?i)[\s\"'`;\/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]+[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:33 UTC</span>

<span style="font-size: 90%;">I see, thanks. Can you please update your PR with that reference?</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">19:54:41 UTC</span>

<span style="font-size: 90%;"><= 3.3.5 :

(?i)[\s\"'`;\/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]+[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=

>= 4.0.0

(?i)[\s\"'`;/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]{3,25}[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=[^=]

(?i)[\s\"'`;\/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]+[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?= => This one was PL1 - it triggers a lot of false positive - base64 like.
(?i)[\s\"'`;/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]{3,25}[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?=[^=] => This new one that you deploy on 4.0.0 could be PL1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:47 UTC</span>

<span style="font-size: 90%;">We'll have to review that. 4 years ago, we decided to move the rule _with the current regex_ from PL1 to PL2. :slightly_smiling_face:</span>

↳ **Vincent - TW** <span style="color: grey; font-size: 90%;">19:56:15 UTC</span>

<span style="font-size: 90%;">You are right</span>

↳ **Vincent - TW** <span style="color: grey; font-size: 90%;">19:56:47 UTC</span>

<span style="font-size: 90%;">The previous regex should have been in PL2 because of its false positives.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:57:02 UTC</span>

<span style="font-size: 90%;">Yes, probably</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:56:35 UTC</span>

<span style="font-size: 90%;">Some numbers would help to argue for a PL move. I.e. run the full quantitative testing against the old pattern and the new one, see & prove if the false positive rate is much lower on the new regex?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:57:38 UTC</span>

<span style="font-size: 90%;">Yes, some numbers would be nice. Let's continue the discussion in the PR though.</span>

**michela** <span style="color: grey; font-size: 90%;">19:58:28 UTC</span>

<span style="font-size: 90%;">So that I may learn, are there standardised quantitative tests that we could run to determine the rate of false positives?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:58:45 UTC</span>

<span style="font-size: 90%;">As for topic number 2, you can ignore that for now, I'm in the process of writing a response and I'm unsure whether the rule makes sense at all.</span>

**michela** <span style="color: grey; font-size: 90%;">19:59:07 UTC</span>

<span style="font-size: 90%;">I seem to remember a new project recently released or near release to run reports on false positives, but I could be imagining that.  :smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:23 UTC</span>

<span style="font-size: 90%;">It's built into "toolchain" now, I think</span>

**michela** <span style="color: grey; font-size: 90%;">20:00:45 UTC</span>

<span style="font-size: 90%;">Thanks! I also see [this](https://github.com/coreruleset/false-positive-report-plugin). So, is that what you would run to determine the number of false positives then, _@xanadu_? Is that what you were referring to in your last comment?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:01:05 UTC</span>

<span style="font-size: 90%;">No, that's a new plugin from _@azurit_ :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:02 UTC</span>

<span style="font-size: 90%;">We run quantitive tests as part of the CI pipeline. We've built this into the go-ftw, which allows us to run requests with language corpus data against CRS.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">20:02:21 UTC</span>

<span style="font-size: 90%;">PR edited : [https://github.com/coreruleset/coreruleset/pull/4291](https://github.com/coreruleset/coreruleset/pull/4291)</span>

**michela** <span style="color: grey; font-size: 90%;">20:02:23 UTC</span>

<span style="font-size: 90%;">Right. Okay. Thank you! :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:45 UTC</span>

<span style="font-size: 90%;">We use standardised corpi with natural language, like newspaper headlines to determine the number of FPs against natural language.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:05 UTC</span>

<span style="font-size: 90%;">It's not perfect but at least it's an approximation that let's us get some numbers without actual traffic.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:19 UTC</span>

<span style="font-size: 90%;">_@xanadu_ built it at the dev retreat 2(?) years ago.</span>

**michela** <span style="color: grey; font-size: 90%;">20:03:45 UTC</span>

<span style="font-size: 90%;">Nice. I will try to tinker with that, and the new plug-in, when I have a chance, hopefully soon!</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:05:11 UTC</span>

<span style="font-size: 90%;">More on quantitive testing also in go-ftw readme: [https://github.com/coreruleset/go-ftw?tab=readme-ov-file#experimental-quantitative-testing](https://github.com/coreruleset/go-ftw?tab=readme-ov-file#experimental-quantitative-testing)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:18 UTC</span>

<span style="font-size: 90%;">_@azurit_, can you take topic 3, the mailing list issue you linked to?</span>

**azurit** <span style="color: grey; font-size: 90%;">20:07:09 UTC</span>

<span style="font-size: 90%;">Hi, sure. I was trying what user suggested as a benchmark and the numbers were the same - according to it, CRS really slows down the web server.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:07:35 UTC</span>

<span style="font-size: 90%;">I was testing it on apache, modsec2 and crs3.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:08:15 UTC</span>

<span style="font-size: 90%;">But the user claimed to do testing also with crs4.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:09:33 UTC</span>

<span style="font-size: 90%;">The interesting is that i never noticed so high performance drop on my real-world servers.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">20:10:53 UTC</span>

<span style="font-size: 90%;">In the tests, did he try with and without the RESPONSE rule sets - 950 to 954?</span>

**michela** <span style="color: grey; font-size: 90%;">20:10:54 UTC</span>

<span style="font-size: 90%;">Indeed hat is interesting. I do not notice any significant impact on the servers and services I run with CRS. Some of them are incredibly fast.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:11:12 UTC</span>

<span style="font-size: 90%;">Without knowing the exact setup, anything could be the issue. We don't know whether there are custom rules in there (unless I missed that when skimming the message).</span>

**michela** <span style="color: grey; font-size: 90%;">20:11:34 UTC</span>

<span style="font-size: 90%;">Perhaps they could be even faster without it, but the difference would probably be negligible, it seems.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:11:43 UTC</span>

<span style="font-size: 90%;">He was trying the whole ruleset but i did some tests, i was not related to one or few rules.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:02 UTC</span>

<span style="font-size: 90%;">It also depends on the ModSecurity configuration</span>

**azurit** <span style="color: grey; font-size: 90%;">20:12:17 UTC</span>

<span style="font-size: 90%;">Butbi tested it on my own.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:27 UTC</span>

<span style="font-size: 90%;">You could not replicate their results, could you _@azurit_?</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:32 UTC</span>

<span style="font-size: 90%;">last year's retreat I made a comparison between CRS3 and CRS4, and CRS4 is slower, definitely - but the reason is simple: there are more rules in CRS4.</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">20:12:44 UTC</span>

<span style="font-size: 90%;">We’ve also observed severe performance drops on some Magento back offices - but only when the 950 to 954 rule sets are enabled.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:13:08 UTC</span>

<span style="font-size: 90%;">Yes, i was able to replicate that numbers.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:22 UTC</span>

<span style="font-size: 90%;">Oh, ok.</span>

**michela** <span style="color: grey; font-size: 90%;">20:14:12 UTC</span>

<span style="font-size: 90%;">I have to take my dog to a doctor's appointment. I will check the chat later. Please feel free to assign tasks to me if needed. I am happy to help in further performance testing as well.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:23 UTC</span>

<span style="font-size: 90%;">Have you got audit log performance "Stopwatch" metrics? Do they suggest where the time is being spent?</span>

**azurit** <span style="color: grey; font-size: 90%;">20:14:33 UTC</span>

<span style="font-size: 90%;">(using the same benchmark tool)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:15:33 UTC</span>

<span style="font-size: 90%;">I guess this would be something interesting to work on at the retreat as well. Standardised performance metrics. I'm sure we've discussed this before.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:16:31 UTC</span>

<span style="font-size: 90%;">I was not doing any deep research atound it. I tried crs3 on on of my servers, played a bit with removing (disabling) various CRS files to see how results are changing..</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:17:01 UTC</span>

<span style="font-size: 90%;">I've added the topic to the dev retreat topics list</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:17:30 UTC</span>

<span style="font-size: 90%;">There's nothing we can do about it immediately, until we understand the bottlenecks better.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:17:32 UTC</span>

<span style="font-size: 90%;">As i said, my results were similar to his and it was not related to one or few rules.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:17:50 UTC</span>

<span style="font-size: 90%;">Ok</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:32 UTC</span>

<span style="font-size: 90%;">(_@franbuehler_ decision here)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:24 UTC</span>

<span style="font-size: 90%;">As already written, _@azurit_ has released a new plugin, which we will host as an official CRS plugin. It can be used to send e-mails when CRS rules trigger. The plugin hasn't been officially released yet (it's not in the registry yet), because we want to make sure that users are aware of the risks (e.g., flooding their mail boxes) and that we cannot support them with their setup.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:22:53 UTC</span>

<span style="font-size: 90%;">The dev retreat will start in 19 days :party-crs: Can't wait to see you all! I think we have a great retreat planned.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:52 UTC</span>

<span style="font-size: 90%;">What we need from you are topics. Please take just 10 minutes maybe, look at the list of current topics ([https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2025-Topics](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2025-Topics)) and add anything you think might be interesting or relevant. We won't have time for everything, but this is YOUR project. It shouldn't be just Felipe and me who propose stuff to work on.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:11 UTC</span>

<span style="font-size: 90%;">(no hype for that message... :sweat_smile:)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:42 UTC</span>

<span style="font-size: 90%;">Is there anything else you would like to discuss before we close?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:54 UTC</span>

<span style="font-size: 90%;">First meal - dinner Sat 22nd, last meal - breakfast Sat 29th?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:02 UTC</span>

<span style="font-size: 90%;">(That helps with planning)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:31 UTC</span>

<span style="font-size: 90%;">Yes, correct</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:30:06 UTC</span>

<span style="font-size: 90%;">Ok then. Let's close for tonight. See you soon!</span>

**Vincent - TW** <span style="color: grey; font-size: 90%;">20:30:15 UTC</span>

<span style="font-size: 90%;">Good night :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:30:52 UTC</span>

<span style="font-size: 90%;">Thank you for leading the meeting. Good night and see you all soon!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:30:58 UTC</span>

<span style="font-size: 90%;">Night night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:31:05 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4317#issuecomment-3482264532](https://github.com/coreruleset/coreruleset/issues/4317#issuecomment-3482264532)</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:13 UTC</span>

<span style="font-size: 90%;">good night!</span>

