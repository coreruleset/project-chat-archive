### Mon, Dec 19th, 2022

**dune73** <span style="color: grey; font-size: 90%;">19:30:24 UTC</span>

<span style="font-size: 90%;">Results for bug bounty tests with new exclusion list:
PL1  368  77.97% (76.67% last week)
PL2  444  94.07% (92.50%)
PL3  446  94.49% (92.92%)
PL4  467  98.94% (97.92%)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:38 UTC</span>

<span style="font-size: 90%;">Welcome to the chat!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:10 UTC</span>

<span style="font-size: 90%;">hi guys!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:32 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:31:39 UTC</span>

<span style="font-size: 90%;">hellooooo!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:59 UTC</span>

<span style="font-size: 90%;">For the record, it's 26 findings we do not detect at PL3 after the new exclusions.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:08 UTC</span>

<span style="font-size: 90%;">Hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:18 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:35 UTC</span>

<span style="font-size: 90%;">So nice to see you all. Thank you all for joining.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:07 UTC</span>

<span style="font-size: 90%;">Our agenda is at [https://github.com/coreruleset/coreruleset/issues/3036](https://github.com/coreruleset/coreruleset/issues/3036)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:49 UTC</span>

<span style="font-size: 90%;">These are 6 open questions for us to discuss.
But there is no way around the bug bounty topic and the question of the status there. 26 findings we are still not blocking / detecting and that's after new exlusions for issues we came to the conclusion we won't fix lately.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:13 UTC</span>

<span style="font-size: 90%;">How do you want to start? BB first, 6 issues first or 3 issues and then BB and then the rest?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:56 UTC</span>

<span style="font-size: 90%;">BB first I guess</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:49 UTC</span>

<span style="font-size: 90%;">Other votes? We could also do with some uplifting discussions first, I guess. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:21 UTC</span>

<span style="font-size: 90%;">Yay, Azure :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">As long as we get to the urgent discussions before everybody’s tired :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:25 UTC</span>

<span style="font-size: 90%;">Max, you mentioned you saw a clear way forward with the BB findings. Could you share that please. Namely with rules IDs, PRs, BB finding names if possible.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:09 UTC</span>

<span style="font-size: 90%;">So, BB status:
</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:42 UTC</span>

<span style="font-size: 90%;">I am very optimistic that we can get the curl call failures done with ~ 3 PR's</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:41:57 UTC</span>

<span style="font-size: 90%;">I agree 100% here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:13 UTC</span>

<span style="font-size: 90%;">"curl call failures" == BB findings we are not yet detecting?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:15 UTC</span>

<span style="font-size: 90%;">Some of them will keep failing because they are due to ModSecurity issues or are accepted as PL3 only.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:20 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:24 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:06 UTC</span>

<span style="font-size: 90%;">What's more, I'm on vacation now, so I can work on that stuff</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:11 UTC</span>

<span style="font-size: 90%;">So the big issue is [#2419](https://github.com/coreruleset/coreruleset/issues/#2419) plus then 2 additional ones and we're mostly done.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:39 UTC</span>

<span style="font-size: 90%;">Thank you for the confirmation _@fzipitria_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:36 UTC</span>

<span style="font-size: 90%;">Which are the other issues? (I know one is technically mine, but I'd like to have it in the chat archive)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:15 UTC</span>

<span style="font-size: 90%;">[#2978](https://github.com/coreruleset/coreruleset/issues/#2978) needs re-examining. The Powershell cmdlet thing.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:55 UTC</span>

<span style="font-size: 90%;">Then we can fix or ignore YAHOO-VYYFBP5V.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:51 UTC</span>

<span style="font-size: 90%;">I can probably also tackle that one, once I've don the others. I have a Windows env where I can do some checks. I'm no expert of course but at least we can test the most basic stuff</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:56 UTC</span>

<span style="font-size: 90%;">We can get a cloud host if needed for that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">[#3059](https://github.com/coreruleset/coreruleset/issues/#3059) is a great step to clean up Windows / Unix commands</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:47:29 UTC</span>

<span style="font-size: 90%;">That was my thinking</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:24 UTC</span>

<span style="font-size: 90%;">It's a no-brainer IMO</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:24 UTC</span>

<span style="font-size: 90%;">So the 3 issues / PRs to rule them all are
Please confirm or correct!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:14 UTC</span>

<span style="font-size: 90%;">Sorry, what do you mean by "to rule them all"?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:23 UTC</span>

<span style="font-size: 90%;">To fix all failing curl calls?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:43 UTC</span>

<span style="font-size: 90%;">I don’t think [#3059](https://github.com/coreruleset/coreruleset/issues/#3059) will fix anything</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:38 UTC</span>

<span style="font-size: 90%;">Yes, that's what I meant. You guys talk of 3 issues and I would like to know them for sure or it's all fluid and we do not really know we're talking of the same topic.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:59 UTC</span>

<span style="font-size: 90%;">Ok, sorry for the misunderstanding. No, those PR's don't all exist yet. I have one open, one in draft, one I'm working on and then there's _@franbuehler_'s PR, which is also relevant. Then there's at least one more PR I need to open for the toolchain (additional evasions). So 4 at least.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:52:17 UTC</span>

<span style="font-size: 90%;">(I know, I wrote "~3" above)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:48 UTC</span>

<span style="font-size: 90%;">No worries, but let's name or at least define it so it's crystal clear for everyone.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:24 UTC</span>

<span style="font-size: 90%;">Before I can give you a definitive list, we have to discuss _@franbuehler_'s PR and my draft PR</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:35 UTC</span>

<span style="font-size: 90%;">And [#2419](https://github.com/coreruleset/coreruleset/issues/#2419), for that matter</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:14 UTC</span>

<span style="font-size: 90%;">Good. So I suggest we move to the open question - as we are still fresh. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:48 UTC</span>

<span style="font-size: 90%;">932150 is at the heart of the issue here. _@walter_ wrote that this rule "isn't so important". If that is the case, we might have some options here.

As we discussed in _@franbuehler_'s PR, we need to detect RCE in User-Agent and Referer headers, which is why we decided to add a rule at PL2 for them (please correct me _@franbuehler_ if that's not correct).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:44 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:52 UTC</span>

<span style="font-size: 90%;">It's more than one rule, but yes, it's correct.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:57:08 UTC</span>

<span style="font-size: 90%;">I found that multiple of the failing curl calls are due to the fact that the payload is being sent in those two headers. I was able to fix them easily by simply checking those two headers in (almost) every rule of 932.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:58:15 UTC</span>

<span style="font-size: 90%;">I've opened a draft PR for that. However, I'm a bit uncomfortable with that change. For one thing, we consciously decided to add the new rule at PL2.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:06 UTC</span>

<span style="font-size: 90%;">So you mean, we downgrade 932150 slighly by removing time and ping and then we extend coverage of UA and Referer to 932150 and most of the 932xxx gang?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:59:11 UTC</span>

<span style="font-size: 90%;">This is point 1. Do we want / need to check those headers in all rules? If so, do we need to add new twins at PL2 for all of them?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:59:48 UTC</span>

<span style="font-size: 90%;">time and ping are a separate issue (point 2). I'll discuss that afterwards.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:24 UTC</span>

<span style="font-size: 90%;">I'm waiting for comments :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:44 UTC</span>

<span style="font-size: 90%;">Then I do not understand your statement about 932150 not being so important. How does that play into this.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:01:21 UTC</span>

<span style="font-size: 90%;">Sorry, that was misleading. That's more relevant to point 2.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:44 UTC</span>

<span style="font-size: 90%;">I think it's risky to extend coverage so much for UA + Referer in terms of 932xxx. But 932 is vital as we are seeing again and again and log4j would have been a no-brainer for us if it was not for lack of coverage for UA + Referer on 932130. And here it's a remaining hard core of the BB findings. So I am inclined to make the jump. If we can do anything to land softer then I'm open to that of course.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:26 UTC</span>

<span style="font-size: 90%;">Ok. What about the twin rules idea? It would be in line with the work that _@franbuehler_ is doing.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:35 UTC</span>

<span style="font-size: 90%;">(read: test a few thousand user agents for FPs...; construct a few thousand of Referers and FP test them)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:05 UTC</span>

<span style="font-size: 90%;">I do not get the twin rules idea. That's copying PL1 rules to PL2 in order to cover UA + Referer at PL2 and not at PL1?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:12 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:32 UTC</span>

<span style="font-size: 90%;">Can we use _@theMiddle_'s idea here? If UA or Referer only contains A-Z0-9 then we don't need to scan it for weird RCE patterns etc. and turn off all of the twin rules?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:39 UTC</span>

<span style="font-size: 90%;">We do not have the toolchain functionality to do this without copying the *.ra file, don't we?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:52 UTC</span>

<span style="font-size: 90%;">Yes, we do</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:59 UTC</span>

<span style="font-size: 90%;">We can use includes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:03 UTC</span>

<span style="font-size: 90%;">UAs + Referers never contain only A-Z0-9.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:08 UTC</span>

<span style="font-size: 90%;">+1 on the includes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:50 UTC</span>

<span style="font-size: 90%;">Under the line we're talking of 14 PL1 rules for 932. Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:08 UTC</span>

<span style="font-size: 90%;">I would have to check, but that sounds about right</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:48 UTC</span>

<span style="font-size: 90%;">932230
932110
932115
932120
932125
932130
932140
932150
932330
932160
932170
932171
932175
932180</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:06:49 UTC</span>

<span style="font-size: 90%;">14 at PL 1, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:47 UTC</span>

<span style="font-size: 90%;">3 of these seem to be replicas of another rule ID since the regex would be too big otherwise.</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:20 UTC</span>

<span style="font-size: 90%;">I would rather not include 932150 for UA/Referer checking: an app that directly executes those header values in a shell will probably not exist.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:09 UTC</span>

<span style="font-size: 90%;">That's what I said last time and then you or _@theMiddle_ said that yes, those apps do exist :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:38 UTC</span>

<span style="font-size: 90%;">_@dune73_ I think we would also need to add those two headers to the existing PL2 rules in that file.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:52 UTC</span>

<span style="font-size: 90%;">What about log viewers that tried to execute '${jndi…' in logged UAs?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:59 UTC</span>

<span style="font-size: 90%;">I do not see a problem at PL2, but I understand the PL1 concerns.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:59 UTC</span>

<span style="font-size: 90%;">May be an exception, though, and unusual...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:17 UTC</span>

<span style="font-size: 90%;">But an important rule class.</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:54 UTC</span>

<span style="font-size: 90%;">Yes, log viewers might be a concern (although I think probably more for XSS)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:11:48 UTC</span>

<span style="font-size: 90%;">There might be also code execution at this level</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:12:23 UTC</span>

<span style="font-size: 90%;">I saw one using ansi escape codes recently</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:11:04 UTC</span>

<span style="font-size: 90%;">Ok. I get the feeling that we sort of agree on the general direction. I will work with _@franbuehler_ on a proposal.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:11 UTC</span>

<span style="font-size: 90%;">Hold on.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:52 UTC</span>

<span style="font-size: 90%;">Walter says 932150 should rather not be included, but I understood Max thinks 932150 has to be included in order to catch several BB findings. Or am I puzzled now?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:12:37 UTC</span>

<span style="font-size: 90%;">932150 must be included</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:39 UTC</span>

<span style="font-size: 90%;">Well, it would be "932150 at PL2"</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:40 UTC</span>

<span style="font-size: 90%;">932150 also has to be included to cover a big part of Shivam's 2nd bypass list.</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:04 UTC</span>

<span style="font-size: 90%;">Ack</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:12 UTC</span>

<span style="font-size: 90%;">But it will be only the rule without evasions</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:43 UTC</span>

<span style="font-size: 90%;">That’s why we are failing to catch some of the stuff</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:45 UTC</span>

<span style="font-size: 90%;">Thank you. And sorry for being such a bore, but I really think we need to be very clear what we want.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:08 UTC</span>

<span style="font-size: 90%;">The path is not that difficult. We just need $time</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:14 UTC</span>

<span style="font-size: 90%;">So you are aiming for copying PL1 rules to PL2 then _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:29 UTC</span>

<span style="font-size: 90%;">Yes, ATM.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:34 UTC</span>

<span style="font-size: 90%;">ACK</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:42 UTC</span>

<span style="font-size: 90%;">In my PR I copied 932150 to 932152 at PL2 already. But only some of the rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:01 UTC</span>

<span style="font-size: 90%;">Given the list is rather small, I think that's doable and worth the $whatever.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:15:04 UTC</span>

<span style="font-size: 90%;">We have to decide if we want to clone all of the 932xxx rules.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:15:25 UTC</span>

<span style="font-size: 90%;">But I can work on this with Max.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:34 UTC</span>

<span style="font-size: 90%;">I'm fine with you and Max sort this out among you and present a proposal for rules where you think it makes sense.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:15:54 UTC</span>

<span style="font-size: 90%;">Great. Let's move on to the second issue with 932150</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:22 UTC</span>

<span style="font-size: 90%;">The rule has become to big for Apache to handle and is also outdated.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:42 UTC</span>

<span style="font-size: 90%;">That's the sad truth.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:17:05 UTC</span>

<span style="font-size: 90%;">We can fix both of those issues by doing the following (there's a caveat that I will get to later):</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:41 UTC</span>

<span style="font-size: 90%;"></span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:23 UTC</span>

<span style="font-size: 90%;">Now the caveat: things like time and ping may bi in that word list of words of length > 3.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">For the record, why would we not want to keep the _full_ list, _with_ anti-evasion patterns, and simply split it into multiple rules?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:20:08 UTC</span>

<span style="font-size: 90%;">This is also where _@walter_’s comment comes in: if the rule "isn't that important", then maybe those FP are acceptable....</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:27 UTC</span>

<span style="font-size: 90%;">Why is it a problem if they are in said word list?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:48 UTC</span>

<span style="font-size: 90%;">Because [#2419](https://github.com/coreruleset/coreruleset/issues/#2419) is about removing ping and time</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:11 UTC</span>

<span style="font-size: 90%;">Because we will need to keep adding more rules in the future. Generic detection is much better and simple word lists can be matched with pmFromFile.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:11 UTC</span>

<span style="font-size: 90%;">Because we will need to keep adding more rules in the future. Generic detection is much better and simple word lists can be matched with pmFromFile.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:48 UTC</span>

<span style="font-size: 90%;">Because [#2419](https://github.com/coreruleset/coreruleset/issues/#2419) is about removing ping and time</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:48 UTC</span>

<span style="font-size: 90%;">Because [#2419](https://github.com/coreruleset/coreruleset/issues/#2419) is about removing ping and time</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:35 UTC</span>

<span style="font-size: 90%;">Ah, I see. So the FP at PL1 for ping and time would persist</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:23:04 UTC</span>

<span style="font-size: 90%;">Yes. And potentially get worse over time, as we would no longer remove words from the "common" word list</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:14 UTC</span>

<span style="font-size: 90%;">Not sure this is viable, since that is a persisting default installation FP and it kind of forces people to remove that rule in the long run.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:35 UTC</span>

<span style="font-size: 90%;">Maybe, if we detected words of length > 2 at PL2 only (for 932150), that would be an option?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:56 UTC</span>

<span style="font-size: 90%;">The list of commands of length <= 3 is pretty stable</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:12 UTC</span>

<span style="font-size: 90%;">What do we do with the <=3 ones again?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:25:56 UTC</span>

<span style="font-size: 90%;">That is also a common list but checked against evasion patterns and suffix etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:28 UTC</span>

<span style="font-size: 90%;">So not only word detection but some context as well</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:29 UTC</span>

<span style="font-size: 90%;">Can't we add ping and time here as special cases?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">Yes but that doesn't help... they would be in the other list of words > 3</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:43 UTC</span>

<span style="font-size: 90%;">No, my idea is to remove them from said wordlist and give them the < 3 treatment.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:33 UTC</span>

<span style="font-size: 90%;">No. The lists must be common, usable by more than one rule. There's no room for special cases, or we'll end up in the same situation again.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:29:27 UTC</span>

<span style="font-size: 90%;">(it's possible that we would excluded time and ping from that list anyway, but I'm talking about such a move in principle too)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:35 UTC</span>

<span style="font-size: 90%;">I think there are special cases. And time and ping qualify since they are common English words. grep does not qualify, because it's a different kind of word.

I'd really like to avoid a FP in the default installation, since it will simply lead to the big cloud providers axing the rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:30 UTC</span>

<span style="font-size: 90%;">But if you state they definitely have no room here, then maybe they need their own cosy little rule for 932.</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:41 UTC</span>

<span style="font-size: 90%;">That sounds appealing to me…</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">But time was already mostly resolved by adding it to the command prefixes, was it not?</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:31 UTC</span>

<span style="font-size: 90%;">So we would need only a rule for ping</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:32 UTC</span>

<span style="font-size: 90%;">Yes, that is true</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:39 UTC</span>

<span style="font-size: 90%;">And if we get more FPs with the >3 wordlist, we shift them over to the special case rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:57 UTC</span>

<span style="font-size: 90%;">I do not remember the history. But very good if it's only ping.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:35 UTC</span>

<span style="font-size: 90%;">I don't fully understand your idea of the special case rule. Wouldn't the FP still exist since the word is in the common list?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:25 UTC</span>

<span style="font-size: 90%;">I'd remove it from there and give it special treatment that adds context, evasions. Unless you tell me that's not doable. But it seems to be doable for <=3...</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:43 UTC</span>

<span style="font-size: 90%;">I see. IMO, words can only be removed from a list if that benefits each using rule. <= 3 is just that: <= 3. There's no special treatment of that list, except for wrapping it with ##!> cmdline unix.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:16 UTC</span>

<span style="font-size: 90%;">But I kind of do see the need to alter the list for a specific rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:49 UTC</span>

<span style="font-size: 90%;">I have a vague idea of a crs-toolchain thing that would allow one to specify exclusions.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:57 UTC</span>

<span style="font-size: 90%;">Not sure how I would implement that yet though.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:41:39 UTC</span>

<span style="font-size: 90%;">I think that could work. I need to think about it a bit more, but I think I will be able to come up with a proposal for changing 932150.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:20 UTC</span>

<span style="font-size: 90%;">Re: "I see. IMO, ..." You mean the word list where ping is listed should keep ping, since it's used in more than one location.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:42:47 UTC</span>

<span style="font-size: 90%;">precisely</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:42:26 UTC</span>

<span style="font-size: 90%;">Imagine:
##!> include-except <some-file>
ping
time
...
##!<</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:06 UTC</span>

<span style="font-size: 90%;">OK, so no cosy little rule. Thanks for the explanation.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:43:13 UTC</span>

<span style="font-size: 90%;">That would also give us a way to clearly document why we exclude some word</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:43:41 UTC</span>

<span style="font-size: 90%;">I think I understand your reasoning to keep these word lists 'pure' and not have lots of exceptions… but how many rules do you imagine using this list? The existing rule plus a higher PL twin? Or dozens and dozens of rules?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:44:45 UTC</span>

<span style="font-size: 90%;">If we have the option to exclude things, then the number doesn't matter, I think. Without that, I would be careful to have too many rules using a single list.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:42 UTC</span>

<span style="font-size: 90%;">But a tentative option to shift ping into the <=3 class by adding an exclusion option there.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:44:45 UTC</span>

<span style="font-size: 90%;">If we have the option to exclude things, then the number doesn't matter, I think. Without that, I would be careful to have too many rules using a single list.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:44:45 UTC</span>

<span style="font-size: 90%;">If we have the option to exclude things, then the number doesn't matter, I think. Without that, I would be careful to have too many rules using a single list.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:45:42 UTC</span>

<span style="font-size: 90%;">Almost. I would create a second rule for words >3 and add the exclusion there.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:45:50 UTC</span>

<span style="font-size: 90%;">As in the example above</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:59 UTC</span>

<span style="font-size: 90%;">Good. I think I understand this now and I think we have a way forward. Any other remarks on this?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:24 UTC</span>

<span style="font-size: 90%;">I suggest we move to "[Add tests to plugins #3051](https://github.com/coreruleset/coreruleset/issues/3051)" then</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:34 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ are you free to explain this?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:05 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:08 UTC</span>

<span style="font-size: 90%;">Kindof</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:22 UTC</span>

<span style="font-size: 90%;">This one is easy</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:53 UTC</span>

<span style="font-size: 90%;">There is a setup that allows you just to copy the files in the template plugin for running a pipeline testing plugins</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:10 UTC</span>

<span style="font-size: 90%;">You just need to write the test itself.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:31 UTC</span>

<span style="font-size: 90%;">There might be some additional work on those plugins that make modifications to the CRS docker image</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:41 UTC</span>

<span style="font-size: 90%;">Right, and the test would be a typical FP payload that has mostly no_log_contains, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:43 UTC</span>

<span style="font-size: 90%;">So we can leave those for the end</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:51 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:52 UTC</span>

<span style="font-size: 90%;">(for the exclusions plugins)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:13 UTC</span>

<span style="font-size: 90%;">What we need to tests is that we are excluding stuff properly</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:23 UTC</span>

<span style="font-size: 90%;">Could you quickly link the template here, please?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:29 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:37 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/template-plugin/blob/main/tests/regression/template-plugin/9500100.yaml](https://github.com/coreruleset/template-plugin/blob/main/tests/regression/template-plugin/9500100.yaml)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:03 UTC</span>

<span style="font-size: 90%;">That's the example test for the template plugin</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:04 UTC</span>

<span style="font-size: 90%;">Thank you for this. That's ver yuseful and a standard way. Thus something that comes in very handy.</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:40 UTC</span>

<span style="font-size: 90%;">It’s not difficult work but it is a lot of work to get complete coverage…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:53:55 UTC</span>

<span style="font-size: 90%;">Some plugins will need extra work, like adding extra lua stuff</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:05 UTC</span>

<span style="font-size: 90%;">But then let's move that to a second phase</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:19 UTC</span>

<span style="font-size: 90%;">We should have tests at least for all the ones we moved from the core</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:36 UTC</span>

<span style="font-size: 90%;">Agreed on the 2nd phase.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:17 UTC</span>

<span style="font-size: 90%;">I think complete test coverage would be useful, but we did not have test coverage for RE packages in 3.3 and I would not hold back 4.0 over this question.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:44 UTC</span>

<span style="font-size: 90%;">Unless you want to have proof that things are working</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:00 UTC</span>

<span style="font-size: 90%;">At least your apache should work</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:25 UTC</span>

<span style="font-size: 90%;">Before that test was implied</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:40 UTC</span>

<span style="font-size: 90%;">At least apache should work, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:10 UTC</span>

<span style="font-size: 90%;">But I would rather have 4.0 out the door than being 100% sure that each one of the $RE-Package rule exclusions are working.</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:57 UTC</span>

<span style="font-size: 90%;">I know, but we’re still in crisis mode for 4.0. Maybe we could at least start with minimal tests so that there are no syntax errors, not go for complete coverage. Having good coverage would require probably to run the app without the plugin and re-discover triggering payloads again, it would be doable for small plugins but for Xenforo for instance I don’t think I can do that quickly - these FPs and exclusions were found over periods of more than a year running it. And still I add some on a monthly basis.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:03 UTC</span>

<span style="font-size: 90%;">I agree on that 100%.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:05 UTC</span>

<span style="font-size: 90%;">I thing we are waiting on BB for an RC2</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:43 UTC</span>

<span style="font-size: 90%;">But once BB is done and word lists covered, I do not want to wait any longer over plugin tests. It's plugins for a reason.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:54 UTC</span>

<span style="font-size: 90%;">Yes, agreed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:15 UTC</span>

<span style="font-size: 90%;">Not much progress on the lists yet....</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:27 UTC</span>

<span style="font-size: 90%;">Som progress, but not enough, I agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:49 UTC</span>

<span style="font-size: 90%;">Let's move to PR [#3059](https://github.com/coreruleset/coreruleset/issues/#3059).</span>

**walter** <span style="color: grey; font-size: 90%;">21:00:51 UTC</span>

<span style="font-size: 90%;">I planned my lists work for my only 2 free days in 2022…</span>

**walter** <span style="color: grey; font-size: 90%;">21:01:33 UTC</span>

<span style="font-size: 90%;">I could also try to make a basic test for Wordpress plugin.</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:11 UTC</span>

<span style="font-size: 90%;">And maybe a XenForo one with just a few basic ones.</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:19 UTC</span>

<span style="font-size: 90%;">This would be around 29-30 dec</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:27 UTC</span>

<span style="font-size: 90%;">If you have time I'd prefer the lists. But if it's simple, then do it by all means.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:17 UTC</span>

<span style="font-size: 90%;">What is the character of those 2 rules 932110 / 932115 now _@fzipitria_ ? You want to split them by source now, if I got you correctly.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:29 UTC</span>

<span style="font-size: 90%;">Windows commands</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:36 UTC</span>

<span style="font-size: 90%;">You got it right</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:53 UTC</span>

<span style="font-size: 90%;">It was a split in two files because of size (alphabetic)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:23 UTC</span>

<span style="font-size: 90%;">But now I want to use 110 for windows so we can use the lolbas there</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:32 UTC</span>

<span style="font-size: 90%;">And the other for general commands</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:37 UTC</span>

<span style="font-size: 90%;">What is lolbas exactly?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:50 UTC</span>

<span style="font-size: 90%;">It is a repo of windows commands</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:00 UTC</span>

<span style="font-size: 90%;">Ah, ok.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:07 UTC</span>

<span style="font-size: 90%;">[https://lolbas-project.github.io/#](https://lolbas-project.github.io/#)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:54 UTC</span>

<span style="font-size: 90%;">Devil's advocate: Why can't we combined the two sources and then continue to split by alphabet?
What happens when lolbas picks up an item that previously resided on the general commands list? New FP?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:11 UTC</span>

<span style="font-size: 90%;">Why is lolbas and general commands complementary? Is not there an overlap?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:19 UTC</span>

<span style="font-size: 90%;">It's clearer if we have them separated</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:43 UTC</span>

<span style="font-size: 90%;">There should be no overlap between windows commands and application commands</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:54 UTC</span>

<span style="font-size: 90%;">E.g. applications are mysqladmin</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:18 UTC</span>

<span style="font-size: 90%;">So generic application commands are going to overlap with unix maybe</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:25 UTC</span>

<span style="font-size: 90%;">But not with windows commands</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:02 UTC</span>

<span style="font-size: 90%;">Ah, so lolbas is windows application commands? The rest is generic windows stuff. You could also say Microsoft vs 3rd party?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:08:57 UTC</span>

<span style="font-size: 90%;">Maybe, if they are from microsoft, but I cannot guarantee that</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:55 UTC</span>

<span style="font-size: 90%;">I think this split makes sense. It's just very annoying for our users of course. Also there is a chance that existing REs continue to remain active despite the original payload would now target the other rule.

Final question: The new resulting rules will fit size-wise with some margin of safety?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:42 UTC</span>

<span style="font-size: 90%;">Good question: don't know 100% now. I've done this today, it just sounded good.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:54 UTC</span>

<span style="font-size: 90%;">But I think we are safe</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:00 UTC</span>

<span style="font-size: 90%;">Hmm. I think we should shift to two new rule IDs. If the 2 rules are different source now, there is no point keeping one of them at 932xx5 anymore. It should be a 932xx0 rule in my opinion. It would also make sure users start with new REs anew.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:08 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:15:45 UTC</span>

<span style="font-size: 90%;">Well, if we must</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:28 UTC</span>

<span style="font-size: 90%;">There is plenty of ID space and it won't be the same rule anymore. So I do not see much advantage of keeping the same location.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:23 UTC</span>

<span style="font-size: 90%;">But anyways, I think the only remaining issue before going to sleep is [#2978](https://github.com/coreruleset/coreruleset/issues/#2978), is not it?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:10 UTC</span>

<span style="font-size: 90%;">_@xanadu_ what is your take here? Which variant do you prefer?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:18:38 UTC</span>

<span style="font-size: 90%;">I really don't know. My Powershell (and general Windows) knowledge is almost 0, so I'm not sure on this case.</span>

**walter** <span style="color: grey; font-size: 90%;">21:18:54 UTC</span>

<span style="font-size: 90%;">Same here..</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:59 UTC</span>

<span style="font-size: 90%;">This is the same problem from 932150, just for windows</span>

**walter** <span style="color: grey; font-size: 90%;">21:19:05 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:19:08 UTC</span>

<span style="font-size: 90%;">?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:19:21 UTC</span>

<span style="font-size: 90%;">I have to go. Sorry. Good night!</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:19:29 UTC</span>

<span style="font-size: 90%;">Then let's tackle 932150 first.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:19:38 UTC</span>

<span style="font-size: 90%;">How are they related?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:19:43 UTC</span>

<span style="font-size: 90%;">They seem totally different to me.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:50 UTC</span>

<span style="font-size: 90%;">Looks like we only match the evasion attempt instead of the plain word?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:00 UTC</span>

<span style="font-size: 90%;">This</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:08 UTC</span>

<span style="font-size: 90%;">Goo dnight _@franbuehler_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:26 UTC</span>

<span style="font-size: 90%;">You said it</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:21:03 UTC</span>

<span style="font-size: 90%;">Yes. That's the crux of it. We have a test looking for one thing, while we have a rule doing another thing.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:21:18 UTC</span>

<span style="font-size: 90%;">So either the test is no good or the rule is no good. I'm not sure which it is.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:21:29 UTC</span>

<span style="font-size: 90%;">Either we rework the test or we rework the rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:21:32 UTC</span>

<span style="font-size: 90%;">The rule and the test</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:21:44 UTC</span>

<span style="font-size: 90%;">We need a new rule, and move that test to the new rule</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:06 UTC</span>

<span style="font-size: 90%;">OK. But what is the difference of the new rule?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:22:17 UTC</span>

<span style="font-size: 90%;">??</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:17 UTC</span>

<span style="font-size: 90%;">Outside of the lack of prefix?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:22:25 UTC</span>

<span style="font-size: 90%;">New rule? Why does this require a new rule now?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:22:27 UTC</span>

<span style="font-size: 90%;">932150 is that rule for unix. We need the same for Windows</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:22:50 UTC</span>

<span style="font-size: 90%;">We're talking about the test.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:22:56 UTC</span>

<span style="font-size: 90%;">To check it off of the bug bounty list.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:10 UTC</span>

<span style="font-size: 90%;">Just remove it then, if you like</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:23:16 UTC</span>

<span style="font-size: 90%;">oh, sorry</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:23:42 UTC</span>

<span style="font-size: 90%;">That is one of the options</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:23:54 UTC</span>

<span style="font-size: 90%;">If it's the test at fault then we can just ignore/delete it</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:24:21 UTC</span>

<span style="font-size: 90%;">But is the pattern in question a valid attack pattern? That's the question.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:24:34 UTC</span>

<span style="font-size: 90%;">If the test is valid then we need to change the rule, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:38 UTC</span>

<span style="font-size: 90%;">There was a discussion where somebody stated this test and several others were at fault, because these things never work without the prefix.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:24:40 UTC</span>

<span style="font-size: 90%;">But I can't answer that.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:25:31 UTC</span>

<span style="font-size: 90%;">And if that's the case, and a prefix is always required, then we can throw away this test and that's one less BB thing to worry about.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:33 UTC</span>

<span style="font-size: 90%;">Do we have the prefix to avoid FPs? If yes, then removing the prefix / making it optional will bring more FPs, I guess.</span>

**walter** <span style="color: grey; font-size: 90%;">21:25:42 UTC</span>

<span style="font-size: 90%;">Yes, we don’t have a ‘direct RCE’ rule for Windows even, I think, unless somebody added that in the meantime. I didn’t make that rule for two reasons: (1) it didn’t scratch my personal itch because I don’t use Windows, (2) Windows shell commands are more English words and tend to be more FP prone (copy, move, etc instead of cp/mv) so I tried to steer clear from it. So if we don’t detect Windows ‘direct RCE’ we don’t have to do it for iwmi either.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:27:50 UTC</span>

<span style="font-size: 90%;">I can live with that :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:25:56 UTC</span>

<span style="font-size: 90%;">Um... I still think this is the same issue as with 932150. There we have this extra rule for matching without prefix, so IMO, the test is OK, as long as we have a rule to match it</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:26:43 UTC</span>

<span style="font-size: 90%;">Hmm, ok. I think I don't understand the 932150 discussion at all :sweat_smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:27:50 UTC</span>

<span style="font-size: 90%;">I can live with that :smile:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:27:50 UTC</span>

<span style="font-size: 90%;">I can live with that :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:25 UTC</span>

<span style="font-size: 90%;">I think the difference between copy/move and iwmi is that in the case of the latter, we can have a rule that does "direct RCE" without too much risk of FPs. So we could create a new rule with all the base commands of the existing rules that are not English words and create a new "direct RCE" rule for those.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:38 UTC</span>

<span style="font-size: 90%;">Maybe a stricter sibling for the other key words at higher PL.</span>

**walter** <span style="color: grey; font-size: 90%;">21:30:30 UTC</span>

<span style="font-size: 90%;">If iwmi -class Win32_process -name Create -ArgumentList cmd is just a fancy way of doing cmd and we don’t even detect cmd…</span>

**walter** <span style="color: grey; font-size: 90%;">21:31:25 UTC</span>

<span style="font-size: 90%;">Then I would say don’t bother and do require the command separator.</span>

**walter** <span style="color: grey; font-size: 90%;">21:33:01 UTC</span>

<span style="font-size: 90%;">we could detect Win32_process also</span>

**walter** <span style="color: grey; font-size: 90%;">21:33:15 UTC</span>

<span style="font-size: 90%;">and -ArgumentList</span>

**dune73** <span style="color: grey; font-size: 90%;">21:33:25 UTC</span>

<span style="font-size: 90%;">I see your point, but just because we are bad at detecting cmd does not mean we have to be bad at detecting the fancy stuff. On top, we do not know if the backend is protecting itself from the common cmd but forgot about the exotic stuff.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:33:49 UTC</span>

<span style="font-size: 90%;">+1 on the Win32 and ArgumentList. If that's a quick solution, then great and we skip this discussion.</span>

**walter** <span style="color: grey; font-size: 90%;">21:34:13 UTC</span>

<span style="font-size: 90%;">Not sure if those are absolutely required though due to lack of Win knowledge.</span>

**walter** <span style="color: grey; font-size: 90%;">21:34:40 UTC</span>

<span style="font-size: 90%;">But we could close the finding like a checklist item.</span>

**walter** <span style="color: grey; font-size: 90%;">21:35:22 UTC</span>

<span style="font-size: 90%;">So if we would just add iwmi to 932110 I don’t see problems</span>

**walter** <span style="color: grey; font-size: 90%;">21:35:39 UTC</span>

<span style="font-size: 90%;">And Windows immediate RCE could be a 4.1 feature</span>

**dune73** <span style="color: grey; font-size: 90%;">21:36:04 UTC</span>

<span style="font-size: 90%;">_@xanadu_ would iwmi in 931110 solve this issue?</span>

**walter** <span style="color: grey; font-size: 90%;">21:36:53 UTC</span>

<span style="font-size: 90%;">I think the fact that nobody ever came up with a Windows false negative in the issues also speaks volumes that the user demand for this is probably low…</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:37:19 UTC</span>

<span style="font-size: 90%;">I don't know. Sorry, I'm totally lost with where this discussion went.</span>

**walter** <span style="color: grey; font-size: 90%;">21:38:12 UTC</span>

<span style="font-size: 90%;">932110 is just a list of Windows commands, but it requires a token to start the command, e.g. abcd.jpg|iwmi …</span>

**walter** <span style="color: grey; font-size: 90%;">21:38:26 UTC</span>

<span style="font-size: 90%;">so it would close the hole for the case of shell injection attacks</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:38:48 UTC</span>

<span style="font-size: 90%;">Then no, that wouldn't resolve this particular test/issue.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:38:51 UTC</span>

<span style="font-size: 90%;">Are you sure it's rule 931110?</span>

**walter** <span style="color: grey; font-size: 90%;">21:38:53 UTC</span>

<span style="font-size: 90%;">but it would not catch foo=iwmi , which is consistent with our other behavior for Windows commands</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:38:56 UTC</span>

<span style="font-size: 90%;">That looks like PHP stuff...</span>

**walter** <span style="color: grey; font-size: 90%;">21:39:15 UTC</span>

<span style="font-size: 90%;">932110, did I say 931? sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:14 UTC</span>

<span style="font-size: 90%;">I think the test would still fail. The test is
code=iwmi -class ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:40:41 UTC</span>

<span style="font-size: 90%;">Yes, the test would fail but according to _@walter_ we would accept that as long as the modified test with prefix doesn't fail</span>

**walter** <span style="color: grey; font-size: 90%;">21:40:54 UTC</span>

<span style="font-size: 90%;">Yes, we don’t catch any Windows commands without a command starter (including iwmi) like that in 3.3 and 4.0.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:41:36 UTC</span>

<span style="font-size: 90%;">So code=;iwmi -class ... would need to be detected</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:41:38 UTC</span>

<span style="font-size: 90%;">Then in that case, if that's how we do it and we're happy with that, let's flag this test as an unrealistic test case and add it to the ignore list.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:41:40 UTC</span>

<span style="font-size: 90%;">Case closed.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:42:17 UTC</span>

<span style="font-size: 90%;">We still need to add iwmi and add a test case though, right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:42:28 UTC</span>

<span style="font-size: 90%;">Or do we already detect that?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:42:46 UTC</span>

<span style="font-size: 90%;">It already is a test, and it's failing.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:42:57 UTC</span>

<span style="font-size: 90%;">_@maxleske_ means the naked command</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:43:04 UTC</span>

<span style="font-size: 90%;">We only match ;iwmi</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:43:09 UTC</span>

<span style="font-size: 90%;">Or other prefixes</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:43:13 UTC</span>

<span style="font-size: 90%;">Yes, ok. That's good then</span>

**walter** <span style="color: grey; font-size: 90%;">21:43:33 UTC</span>

<span style="font-size: 90%;">It’s the way it is, I don’t think we can address this for 4.0</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:43:34 UTC</span>

<span style="font-size: 90%;">So no action required</span>

**dune73** <span style="color: grey; font-size: 90%;">21:43:45 UTC</span>

<span style="font-size: 90%;">OK, let's add it to the ignore list for the bug bounty findings, then. No further action required, I guess.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:44:23 UTC</span>

<span style="font-size: 90%;">Phew! :sweat_smile: Thanks for the discussion everyone. We're getting there</span>

**dune73** <span style="color: grey; font-size: 90%;">21:45:03 UTC</span>

<span style="font-size: 90%;">Thank you all. Unless there is something we missed, I'm ready for bed!</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:45:14 UTC</span>

<span style="font-size: 90%;">Me too! Good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:45:20 UTC</span>

<span style="font-size: 90%;">Ooohhh…. bed….</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:45:51 UTC</span>

<span style="font-size: 90%;">good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:46:04 UTC</span>

<span style="font-size: 90%;">good night and thanks everyone!!!</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:46:16 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:46:18 UTC</span>

<span style="font-size: 90%;">good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:46:25 UTC</span>

<span style="font-size: 90%;">Good night</span>

**airween** <span style="color: grey; font-size: 90%;">21:49:01 UTC</span>

<span style="font-size: 90%;">good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">22:45:43 UTC</span>

<span style="font-size: 90%;">Ah-hah! In case anybody else was extremely confused by this evening's discussions about anti-evasions and breaking up lists into commands only 3 letters long, read this first and it will make sense :sweat_smile:
[https://github.com/coreruleset/coreruleset/issues/2632](https://github.com/coreruleset/coreruleset/issues/2632)
That's enough GitHub for one night… :zzz:</span>

