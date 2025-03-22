### Mon, Feb 3rd, 2025

**maxleske** <span style="color: grey; font-size: 90%;">19:30:35 UTC</span>

<span style="font-size: 90%;">Hi all, welcome to the monthly chat.</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">hi guys, sorry, I'll be late a bit</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:48 UTC</span>

<span style="font-size: 90%;">5 mins...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:09 UTC</span>

<span style="font-size: 90%;">Ok, let's wait 5 minutes then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:40 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:39 UTC</span>

<span style="font-size: 90%;">Hi there, I'm a few min late. Still reading bedtime stories ...</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">Evening</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:11 UTC</span>

<span style="font-size: 90%;">(The CRS calendar still says we have a meeting on the 2nd Monday of this month btw. It's a small thing, but we should make sure we're publishing accurate information.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:31 UTC</span>

<span style="font-size: 90%;">Thanks. We'll fix it</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:23 UTC</span>

<span style="font-size: 90%;">hi everyone!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:58 UTC</span>

<span style="font-size: 90%;">Right, let's get started.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:48 UTC</span>

<span style="font-size: 90%;">Do you have any questions w.r.t. to the community call?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:26 UTC</span>

<span style="font-size: 90%;">Doesn't appear so.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:32 UTC</span>

<span style="font-size: 90%;">Next: [https://github.com/coreruleset/coreruleset/issues/3989](https://github.com/coreruleset/coreruleset/issues/3989)</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:38:55 UTC</span>

<span style="font-size: 90%;">Hello everyone :wave: just got up now</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:58 UTC</span>

<span style="font-size: 90%;">_@airween_ do you want to say something about that issue?</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:34 UTC</span>

<span style="font-size: 90%;">I see the reason of this rule (920130), but I think we must investigate the circumstances more, and fix that</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:54 UTC</span>

<span style="font-size: 90%;">I've already started to study that rule and the engines' behavior</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">so I'll take this issue with a fix</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:15 UTC</span>

<span style="font-size: 90%;">I assigned that to myself</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:42 UTC</span>

<span style="font-size: 90%;">the main problem is that we should check the existing of `:` character in the MP header</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:43 UTC</span>

<span style="font-size: 90%;">BUT</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:00 UTC</span>

<span style="font-size: 90%;">if that's a part of a field value and it's quoted, then we must allow</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">the good news is that we don't need to care about these scenarios:
Content-Disposition: form-data; name=form:buttonbecause engines allows only quoted values</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:04 UTC</span>

<span style="font-size: 90%;">this MP header triggers the rule 200002</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:27 UTC</span>

<span style="font-size: 90%;">but we have to check other places, eg:
Content-Disposition: form-data; na:me="form:button"</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:53 UTC</span>

<span style="font-size: 90%;">so this is the goal to implement this solution</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">What is an "MP" header? I'm not familiar with the term.</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:02 UTC</span>

<span style="font-size: 90%;">Multipart</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:05 UTC</span>

<span style="font-size: 90%;">sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:05 UTC</span>

<span style="font-size: 90%;">Ah, tahnks</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:44 UTC</span>

<span style="font-size: 90%;">I've made few other new tests already</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:53 UTC</span>

<span style="font-size: 90%;">for rule 920130</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:04 UTC</span>

<span style="font-size: 90%;">I'll send the PR if I'm done</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:14 UTC</span>

<span style="font-size: 90%;">Thanks _@airween_.</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:26 UTC</span>

<span style="font-size: 90%;">if anyone has an idea around this, please let me know</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:22 UTC</span>

<span style="font-size: 90%;">How do you want to implement it? Detecting colons, but only outside quotes is hard.</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:47 UTC</span>

<span style="font-size: 90%;">actually I have a chained rule at the moment, but I want to investigate the behavior more</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:49 UTC</span>

<span style="font-size: 90%;">Definitely without backreferences</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:13 UTC</span>

<span style="font-size: 90%;">yes, as _@fzipitria_ wrote, I don't want to use any look-ahead/behind solution</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:29 UTC</span>

<span style="font-size: 90%;">but I'm afraid we can't solve that without a chained rule</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">That's an approach. But how about the situation where you have a quoted colon and a non-quoted one delivering the attack payload. I think that situation is always very hard, even with chains.</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:48 UTC</span>

<span style="font-size: 90%;">yes, I know - this is why I need some time</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">I just started to work on it today and unfortunately I had very limited time for that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:00 UTC</span>

<span style="font-size: 90%;">I might be able to take a look.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:14 UTC</span>

<span style="font-size: 90%;">Let's move to the next topic.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:30 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/wordpress-rule-exclusions-plugin/pull/6](https://github.com/coreruleset/wordpress-rule-exclusions-plugin/pull/6)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">I stumbled across this PR from Andrea that was meant to improve testing of plugins.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:06 UTC</span>

<span style="font-size: 90%;">It probably needs a bit of work but the idea is good. So if anyone has some free time on their hands, this one would be nice to have.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:51:37 UTC</span>

<span style="font-size: 90%;">what does this do that the existing tests in the plugins don't do?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:52:31 UTC</span>

<span style="font-size: 90%;">TBH, I haven't looked at it in detail. I think it adds a bit of linting and verification that's currently missing. But it's possible that it could just be closed.</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:36 UTC</span>

<span style="font-size: 90%;">We use WP plugin for several servers, I can try to help with this</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:06 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:29 UTC</span>

<span style="font-size: 90%;">That's it already for the items on the agenda. Is there anything else you would like to discuss?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:51 UTC</span>

<span style="font-size: 90%;">Well</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:02 UTC</span>

<span style="font-size: 90%;">I can also add the first part :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:10 UTC</span>

<span style="font-size: 90%;">Please do</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:39 UTC</span>

<span style="font-size: 90%;">Basically most of you should have received the reimbursements and payments from Dev-on-duty</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:51 UTC</span>

<span style="font-size: 90%;">Let me know if not</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:19 UTC</span>

<span style="font-size: 90%;">I'm still trying to get a room for the CRS user day in Barcelona :man-facepalming:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:51 UTC</span>

<span style="font-size: 90%;">After the community call publishing, that one is next</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:25 UTC</span>

<span style="font-size: 90%;">If someone plans to attend there, please book your hotels asap.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:45 UTC</span>

<span style="font-size: 90%;">Looks like there is a race of some kind and things are getting 3x :man-facepalming:</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:41 UTC</span>

<span style="font-size: 90%;">28th of May will be the CRS user day, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:48 UTC</span>

<span style="font-size: 90%;">And lastly: I still need to get a balance from OWASP HQ so we know our budget for 2025.</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:51 UTC</span>

<span style="font-size: 90%;">It's a Wednesday</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:56 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:11 UTC</span>

<span style="font-size: 90%;">thanks - is there any announcement?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:15 UTC</span>

<span style="font-size: 90%;">That's another thing we are discussing.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:27 UTC</span>

<span style="font-size: 90%;">There is no announcement yet, because there is no place yet. :disappointed:</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:26 UTC</span>

<span style="font-size: 90%;">probably for to communicate the date, a "save-the-date" would be find - wouldn't be?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:35 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:52 UTC</span>

<span style="font-size: 90%;">We were giving more priority for the community call right now :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:10 UTC</span>

<span style="font-size: 90%;">That's it!</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:32 UTC</span>

<span style="font-size: 90%;">a side note from me: Felipe suggested us in Woburn that we should look possibilities on local universities for presentations about CRS and ModSecurity. I talked to a few universities here in Hungary, and now I have two dates (finalized) and two promises from another two universities :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:51 UTC</span>

<span style="font-size: 90%;">Wow! That's great!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:45 UTC</span>

<span style="font-size: 90%;">And on that great note I think we can end the meeting. Thanks for being here. Have a good night or a great day. bb</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:55 UTC</span>

<span style="font-size: 90%;">Thanks for hosting.</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:02 UTC</span>

<span style="font-size: 90%;">thanks</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:05:05 UTC</span>

<span style="font-size: 90%;">Good night and bye</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:10 UTC</span>

<span style="font-size: 90%;">good night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:05:34 UTC</span>

<span style="font-size: 90%;">good night everyone</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;">Night</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:13 UTC</span>

<span style="font-size: 90%;">Good night everyone!</span>

