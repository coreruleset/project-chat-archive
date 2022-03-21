### Mon, Nov 2nd, 2020

**dune73** <span style="color: grey; font-size: 90%;">19:30:31 UTC</span>

<span style="font-size: 90%;">Hello, hello. It's meeting time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:50 UTC</span>

<span style="font-size: 90%;">Our agenda is at [https://github.com/coreruleset/coreruleset/issues/1916](https://github.com/coreruleset/coreruleset/issues/1916)
And I just finished filling it out.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:28 UTC</span>

<span style="font-size: 90%;">I see 4 waving hands. So we're at least the 5 of us. Who else is here?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:21 UTC</span>

<span style="font-size: 90%;">I have added a new section in the agenda. It's about merged or dropped PRs since the last month. Given I am not writing a monthly news thing these days, this could serve as a simple replacement. And it's nice to see the work that we are actually doing.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:50 UTC</span>

<span style="font-size: 90%;">Howdy all</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">Hey _@csanders_, nice to see you!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:33 UTC</span>

<span style="font-size: 90%;">Shall we start?</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">let’s go!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:50 UTC</span>

<span style="font-size: 90%;">So 1915 is about a new feature that allows you to ignore certain monitoring agents from localhost if they match the UA. With the default UA list being empty.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:26 UTC</span>

<span style="font-size: 90%;">The PR does not pass the tests, but otherwise it seems to be really well through through (there was a lot of prior discussion). I did not check the unit tests, though ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:32 UTC</span>

<span style="font-size: 90%;">Or the failures...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:29 UTC</span>

<span style="font-size: 90%;">I reckon: fix the PR and we'll merge. Is there any opposition for that verdict?</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:51 UTC</span>

<span style="font-size: 90%;">agree!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:43 UTC</span>

<span style="font-size: 90%;">OK. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">1913 was a typo with a rule id in a comment. I just merged that one.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:40:09 UTC</span>

<span style="font-size: 90%;">I would add more examples into trusted_ua.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:40:16 UTC</span>

<span style="font-size: 90%;">for example for Zabbix</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:15 UTC</span>

<span style="font-size: 90%;">Sounds like a plan. I'll not it for the minutes (as _@theMiddle_ does not seem to be around)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">1911 is a possible fix for an FP in 921110. _@airween_, do you think it's ready or are you looking for a review?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:08 UTC</span>

<span style="font-size: 90%;">-> I'll note it for the minutes ...</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:28 UTC</span>

<span style="font-size: 90%;">I think it would be good that somebody review that - eg. see the issue comments from ssigwart:
[https://github.com/coreruleset/coreruleset/issues/1883#issuecomment-713135942](https://github.com/coreruleset/coreruleset/issues/1883#issuecomment-713135942)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:20 UTC</span>

<span style="font-size: 90%;">_@fgs_ has been involved with the discussion in the issue. We can ask him to review. Other volunteers?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:30 UTC</span>

<span style="font-size: 90%;">OK. I'll ask _@fgs_.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:34 UTC</span>

<span style="font-size: 90%;">thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:31 UTC</span>

<span style="font-size: 90%;">With 1910, we have failing tests and _@theMiddle_ thinks it's about transformations. Does anybody see why they should suddenly fail, or am I seeing this wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:18 UTC</span>

<span style="font-size: 90%;">Could anybody please check this out quickly?</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:58 UTC</span>

<span style="font-size: 90%;">hmmm</span>

**airween** <span style="color: grey; font-size: 90%;">19:50:05 UTC</span>

<span style="font-size: 90%;">I started to re-run the job</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:31 UTC</span>

<span style="font-size: 90%;">OK, then let's move on and we return to it afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:20 UTC</span>

<span style="font-size: 90%;">1906 is docker optimization. Any opinions here?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:43 UTC</span>

<span style="font-size: 90%;">hi all! sorry can't attend :pensive: I try to connect later</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:59 UTC</span>

<span style="font-size: 90%;">Hey man, good to see you. So we'll be in touch later.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:15 UTC</span>

<span style="font-size: 90%;">We're looking for reviewers for your PRs. :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:31 UTC</span>

<span style="font-size: 90%;">oh well!</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:11 UTC</span>

<span style="font-size: 90%;">about [#1906](https://github.com/coreruleset/coreruleset/issues/#1906), the .gitignore seems uncontroversial, the TZ change makes sense, but I don’t know about the nginx.conf file as I’m not knowledgeable with Nginx</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:07 UTC</span>

<span style="font-size: 90%;">_@airween_: Do you have an opinion on that?</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:09 UTC</span>

<span style="font-size: 90%;">no, sorry - I don't have idea for that</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:14 UTC</span>

<span style="font-size: 90%;">but</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:45 UTC</span>

<span style="font-size: 90%;">is that an Nginx issue? Or is that a Docker issue?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:51 UTC</span>

<span style="font-size: 90%;">The way I read the description of the PR this tries to cover for the fact, that a naked NGINX does not accept POST requests and returns a 405. But I am not heavy into NGINX and also not into docker. So I reckon we need at least somebody well versed with docker who can launch this with an NGINX...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:45 UTC</span>

<span style="font-size: 90%;">I reckon he mounts the NGINX config via a volume and then replaces it in order to bring in his little workaround for the 405 where he tells the server to return a 200 instead of a 405.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:30 UTC</span>

<span style="font-size: 90%;">Or what do you guys make of this?</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:48 UTC</span>

<span style="font-size: 90%;">that seems to be what it could do, but I don’t know the @ notation at all</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:34 UTC</span>

<span style="font-size: 90%;">but if it does what it says it does, then it might resolve some nginx test failures</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:10 UTC</span>

<span style="font-size: 90%;">What do you think _@airween_. Are you running docker at all?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:50 UTC</span>

<span style="font-size: 90%;">The problem is that Franziska who is running docker is not into NGINX at all and neither are the VSHN guys, AFAIK.</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:52 UTC</span>

<span style="font-size: 90%;">I have Docker on some VM's. I'll try to investigate it, but not now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:08 UTC</span>

<span style="font-size: 90%;">Fair enough. Can we assign you as reviewer?</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:12 UTC</span>

<span style="font-size: 90%;">just assign me</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:16 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:27 UTC</span>

<span style="font-size: 90%;">Thank you very much.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:46 UTC</span>

<span style="font-size: 90%;">1902: Fixing this and it seems this is ready to be merged. _@azurIt_, you reviewed it, did not you. Ready to be merged?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:05:24 UTC</span>

<span style="font-size: 90%;">Let me have a one quick look.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:02 UTC</span>

<span style="font-size: 90%;">There is also a comment by user [mackov83](https://github.com/mackov83) that I do not understand.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:36 UTC</span>

<span style="font-size: 90%;">Maybe he commented on the wrong PR?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:34 UTC</span>

<span style="font-size: 90%;">Ah, the PR linked an issue and that issue was by said user. Got it now.</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:04 UTC</span>

<span style="font-size: 90%;">ah, yes, he seems to ask how he can try this new rule out on his system?</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:08 UTC</span>

<span style="font-size: 90%;">it doesn’t seem to comment on the issue</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:53 UTC</span>

<span style="font-size: 90%;">_@azurIt_, could you explain how to apply this new PR or latest version after the merge?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:05 UTC</span>

<span style="font-size: 90%;">To mackov in the PR...</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:11 UTC</span>

<span style="font-size: 90%;">the PR looks good to me, although I wonder why the rule id’s are all changed?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:09:23 UTC</span>

<span style="font-size: 90%;">If you all consider something like this ok SecRule REQUEST_METHOD "@pm PROPFIND PUT"  (i mean @pm vs @rx) then it's ready for merge.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:09:39 UTC</span>

<span style="font-size: 90%;">_@dune73_ i will</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:52 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:32 UTC</span>

<span style="font-size: 90%;">We could insist on t:lowercase to cover for the case insensitive nature of pm.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:54 UTC</span>

<span style="font-size: 90%;">I actually like pm, because it's so nice to read.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:11:13 UTC</span>

<span style="font-size: 90%;">yeah but it matches the substring :disappointed:</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:11:42 UTC</span>

<span style="font-size: 90%;">@walter hm, i'm looking into the reason of that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:27 UTC</span>

<span style="font-size: 90%;">The substring is a problem, yes. But does it matter in this situation on the method?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:12:36 UTC</span>

<span style="font-size: 90%;">i think no</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:42 UTC</span>

<span style="font-size: 90%;">just a side note for [#1910](https://github.com/coreruleset/coreruleset/pull/1910/): I can confirm the failed test with REQUEST-942-APPLICATION-ATTACK-SQLI/942190.yaml - here are same failed tests in locally</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:56 UTC</span>

<span style="font-size: 90%;">Too bad about 1910. :disappointed:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:14:47 UTC</span>

<span style="font-size: 90%;">yeah, the t:removeCommentsChar triggers this error</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:15:15 UTC</span>

<span style="font-size: 90%;">I just removed it and all test passed</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:16:46 UTC</span>

<span style="font-size: 90%;">thats strange</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">I'll investigate this</span>

↳ **emphazer** <span style="color: grey; font-size: 90%;">20:17:31 UTC</span>

<span style="font-size: 90%;">but good you found it ;-)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:21:14 UTC</span>

<span style="font-size: 90%;">sh*t, _@theMiddle_ wrote the comment:

[https://github.com/coreruleset/coreruleset/pull/1910/#issuecomment-711948704](https://github.com/coreruleset/coreruleset/pull/1910/#issuecomment-711948704)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:58 UTC</span>

<span style="font-size: 90%;">1902: I suggest the following: _@azurIt_ works with the contributor to sort at least the IDs out and maybe also the somewhat unsettling use of pm. If that is covered, feel free to merge, _@azurIt_.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:14:39 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:38 UTC</span>

<span style="font-size: 90%;">1901 by _@azurIt_ looks good to me, but I guess it could do with a small review. Volunteers?</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:56 UTC</span>

<span style="font-size: 90%;">looks good, I think it’s ready to merge</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:08 UTC</span>

<span style="font-size: 90%;">Cool. Then please go ahead.</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:26 UTC</span>

<span style="font-size: 90%;">done!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:45 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:46 UTC</span>

<span style="font-size: 90%;">nice how we are slowly adding edge cases to that useful rule</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:11 UTC</span>

<span style="font-size: 90%;">CT is so super complicated and I get the feeling we are slowly covering it all.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:48 UTC</span>

<span style="font-size: 90%;">1899 by the same very active author is ready to me merged, unless we think xss should not be disabled here (but sqli already is).</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:35 UTC</span>

<span style="font-size: 90%;">I was initially hesitant to add it, as I once found a WordPress theme where the post’s title was not properly encoded… but that’s an error in the theme and generally this should be 99% OK</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:56 UTC</span>

<span style="font-size: 90%;">How often is this argument being used?</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:56 UTC</span>

<span style="font-size: 90%;">and also, I don’t find many post titles having to contain <script> tags, but I think on sec related blogs it might be :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:15 UTC</span>

<span style="font-size: 90%;">that was my assessment at the time</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:38 UTC</span>

<span style="font-size: 90%;">I see.</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:45 UTC</span>

<span style="font-size: 90%;">but it could go both ways</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:58 UTC</span>

<span style="font-size: 90%;">The arg is very limited and it's all in the hearbeat ajax request.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:06 UTC</span>

<span style="font-size: 90%;">So I guess we can allow that.</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:08 UTC</span>

<span style="font-size: 90%;">have you run into FP with this rule, _@azurIt_? do you remember an example?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:23:17 UTC</span>

<span style="font-size: 90%;">Yes i have, let me check if i find more info.</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:21 UTC</span>

<span style="font-size: 90%;">[https://developer.wordpress.org/reference/functions/the_title/](https://developer.wordpress.org/reference/functions/the_title/) Like [the_content()](https://developer.wordpress.org/reference/functions/the_content/) , the output of [the_title()](https://developer.wordpress.org/reference/functions/the_title/) is unescaped. This is considered a feature and not a bug, see [the FAQ “Why are some users allowed to post unfiltered HTML?”](https://make.wordpress.org/core/handbook/testing/reporting-security-vulnerabilities/#why-are-some-users-allowed-to-post-unfiltered-html) . If the post title is <script>alert(“test”);</script>, then that JavaScript code will be run wherever [the_title()](https://developer.wordpress.org/reference/functions/the_title/) is used. For this reason, do not write code that allows untrusted users to create post titles.</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:36 UTC</span>

<span style="font-size: 90%;">so I guess it’s a “feature” …</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:10 UTC</span>

<span style="font-size: 90%;">but I do notice in recent WP versions, that non-admin users are not allowed to use <script> any more in content</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:25:16 UTC</span>

<span style="font-size: 90%;">I don't have an exact example but i can see this in my personal exclusion rules:
ctl:ruleRemoveTargetById=941100;ARGS:data[wp_autosave][post_title],\
ctl:ruleRemoveTargetById=941270;ARGS:data[wp_autosave][post_title],\
ctl:ruleRemoveTargetById=932110;ARGS:data[wp_autosave][post_title],\</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:25:52 UTC</span>

<span style="font-size: 90%;">sorry, the last one is not related</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:18 UTC</span>

<span style="font-size: 90%;">So it's a case where WP says it's no security problem and we either follow that example of let the users bump into a FP.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:45 UTC</span>

<span style="font-size: 90%;">But when you write <script> in a title of a post, when you probably have a faint idea, which this could lead to a 403. Or am I wrong?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:26:55 UTC</span>

<span style="font-size: 90%;">I think we should not disable any features in any software.</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:42 UTC</span>

<span style="font-size: 90%;">right, WP have probably got this question many times as they made a FAQ about it, so we could say it’s not our problem, and we could edge on the side of preventing FP</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:21 UTC</span>

<span style="font-size: 90%;">so I can (somewhat grudgingly) agree with this PR</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:26 UTC</span>

<span style="font-size: 90%;">Can we at least add a comment that we follow WP here? I mean this really feels bad, but if admins want to do this, who are we to stop them...</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:28 UTC</span>

<span style="font-size: 90%;">a problem with WP is that it (and plugins) uses so many inline scripts, which change on every release, that a tight CSP is pretty much impossible, which makes me fear XSS more</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:29:46 UTC</span>

<span style="font-size: 90%;">Looking into 941270 indicate that someone was trying to put a link inside a post title (which can be one example of FP)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:05 UTC</span>

<span style="font-size: 90%;">I see.</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:11 UTC</span>

<span style="font-size: 90%;">yeah but putting links in titles sounds crazy to me, how will you click through to the post when inside the title is another link?</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:51 UTC</span>

<span style="font-size: 90%;">but a good example of FP might convince me…</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:23 UTC</span>

<span style="font-size: 90%;">I haven’t seen one yet in my environment and we have some crazy customers…</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:31:41 UTC</span>

<span style="font-size: 90%;">yeah, that sounds a little strange</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:32:03 UTC</span>

<span style="font-size: 90%;">But i'm not sure how WP will handle it.</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:24 UTC</span>

<span style="font-size: 90%;">maybe we should allow links (941280), but keep the libinjection XSS checker?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:32:27 UTC</span>

<span style="font-size: 90%;">Will it 'execute' HTML/JS also outside of the article/page?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:54 UTC</span>

<span style="font-size: 90%;">That would be a good compromise in my eyes _@walter_.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:33:35 UTC</span>

<span style="font-size: 90%;">941280 or 941270?</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:42 UTC</span>

<span style="font-size: 90%;">941270 sorry</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:33:52 UTC</span>

<span style="font-size: 90%;">ok</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:33:54 UTC</span>

<span style="font-size: 90%;">i agree</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:15 UTC</span>

<span style="font-size: 90%;">alright then let’s do it this way for now, and keep an eye on FP’s for a possible future enhancement</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:34:35 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:12 UTC</span>

<span style="font-size: 90%;">Thank you guys</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:26 UTC</span>

<span style="font-size: 90%;">_@azurIt_ I see you changed a line, maybe you forgot (or maybe you are still busy) changing it also in ctl:ruleRemoveTargetByTag=attack-xss;ARGS:new_title,\</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:38:29 UTC</span>

<span style="font-size: 90%;">Sorry, i really missed it!</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:38:50 UTC</span>

<span style="font-size: 90%;">For that arg, i see also this in my exclusion rules:
ctl:ruleRemoveTargetById=941110;ARGS:new_title</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:39:16 UTC</span>

<span style="font-size: 90%;">it's really a usage of <script> tag.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:39:49 UTC</span>

<span style="font-size: 90%;">But i suggest to keep the original deal - get with the 941270 and keep an eye on FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:04 UTC</span>

<span style="font-size: 90%;">1887 is nice, but unfortunately in includes a look-behind that we really try to avoid. And here we would reintroduce it. So what can we do?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:06 UTC</span>

<span style="font-size: 90%;">1887 is nice, but unfortunately in includes a look-behind that we really try to avoid. And here we would reintroduce it. So what can we do?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:10 UTC</span>

<span style="font-size: 90%;">It's a welcome contribution, but I'm a bit at a loss here. Also regexp-wise...</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:30 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ made a comment there, I think we can wait the answer</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:55 UTC</span>

<span style="font-size: 90%;">I just doubt the contributor is up for the task to find another way to express this logic. Or do you see one?</span>

**airween** <span style="color: grey; font-size: 90%;">20:45:13 UTC</span>

<span style="font-size: 90%;">we can ping him again...</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:10 UTC</span>

<span style="font-size: 90%;">I unfortunately don’t know how to resolve that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:14 UTC</span>

<span style="font-size: 90%;">It's really a pity. On some other news, I learnt that HAProxy has forked ModSec3 with RE2 support.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:44 UTC</span>

<span style="font-size: 90%;">Let's ping him. And maybe Franziska has an idea. She's also an official regex wizard after all.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:00 UTC</span>

<span style="font-size: 90%;">1793 is a new rule by theMiddle.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:36 UTC</span>

<span style="font-size: 90%;">This can be merged, I guess. Since it's been covered before. Agreed?</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:49 UTC</span>

<span style="font-size: 90%;">agreed</span>

**airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

**airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

**csanders** <span style="color: grey; font-size: 90%;">20:51:08 UTC</span>

<span style="font-size: 90%;">to be fair, this is fairly common based on the kitchen sink approach to ModSecv3</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:28 UTC</span>

<span style="font-size: 90%;">Yes, they really liked our work there. I am planning to get in touch. The author of the blog is their product lead.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:47 UTC</span>

<span style="font-size: 90%;">I see it the same way, _@csanders_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:16 UTC</span>

<span style="font-size: 90%;">OK, so we merge this one and we're done with the PRs outside of 1910.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:38 UTC</span>

<span style="font-size: 90%;">Any opinions there? TheMiddle thinks it's about the transformations and that we could remove them.</span>

**airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:42 UTC</span>

<span style="font-size: 90%;">hmmmm</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:46 UTC</span>

<span style="font-size: 90%;">t:removeCommentsChar may be harmful here</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:52 UTC</span>

<span style="font-size: 90%;">the tests are correct IMHO</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:02 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ You worked on the unit tests on github. What do you think could cause this.</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:14 UTC</span>

<span style="font-size: 90%;">if i do in mysql, select * from/**/foo it is interpreted as select * from foo</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:25 UTC</span>

<span style="font-size: 90%;">Hwo would they be harmful. So far, I do not get it.</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:41 UTC</span>

<span style="font-size: 90%;">but if we remove comment chars on that payload, then we inspect select * fromfoo  and that would not trigger the rule (and open up a possible bypass)</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:08 UTC</span>

<span style="font-size: 90%;">so the comment char removal may string two separate tokens together into a single one…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:58:20 UTC</span>

<span style="font-size: 90%;">Hey</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:22 UTC</span>

<span style="font-size: 90%;">That is of course a problem.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:58:29 UTC</span>

<span style="font-size: 90%;">Got out two minutes early from a meeting</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:03 UTC</span>

<span style="font-size: 90%;">Perfect timing. We have a problem on the unit tests of 1910. And besides, we are not so sure about the rule in question.</span>

**airween** <span style="color: grey; font-size: 90%;">20:59:04 UTC</span>

<span style="font-size: 90%;">I don't have any MSSQL account, but I thought it would be check how evaluates the engine a query above</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:04 UTC</span>

<span style="font-size: 90%;">What happen with the gh tests?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:41 UTC</span>

<span style="font-size: 90%;">Do you have some failed run?</span>

**airween** <span style="color: grey; font-size: 90%;">21:00:12 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ yes, see 1910</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:21 UTC</span>

<span style="font-size: 90%;">Oh, thanks</span>

**airween** <span style="color: grey; font-size: 90%;">21:00:33 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1910/](https://github.com/coreruleset/coreruleset/pull/1910/)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:33 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**airween** <span style="color: grey; font-size: 90%;">21:02:02 UTC</span>

<span style="font-size: 90%;">finally: I think ModSecv3 next release will contains RE2 support

[https://github.com/SpiderLabs/ModSecurity/pull/2012](https://github.com/SpiderLabs/ModSecurity/pull/2012)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">hmm....

[https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/](https://www.haproxy.com/blog/cve-2020-15598-haproxy-enterprise-unaffected-due-to-modsecurity-hardening-measures/)

:)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:50:38 UTC</span>

<span style="font-size: 90%;">CRS team was mentioned there</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">In other vulnerable software that we tested, this payload would hang the process for over 60 minutes.

vs.

We don’t consider this a DoS vulnerability (as the engine is doing exactly the amount of work it was asked to do).</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:02:02 UTC</span>

<span style="font-size: 90%;">finally: I think ModSecv3 next release will contains RE2 support

[https://github.com/SpiderLabs/ModSecurity/pull/2012](https://github.com/SpiderLabs/ModSecurity/pull/2012)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:23 UTC</span>

<span style="font-size: 90%;">looks like 19, 31 and 32 are failing</span>

**airween** <span style="color: grey; font-size: 90%;">21:02:48 UTC</span>

<span style="font-size: 90%;">I think there are more failed test</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:03 UTC</span>

<span style="font-size: 90%;">One more, 9</span>

**airween** <span style="color: grey; font-size: 90%;">21:04:05 UTC</span>

<span style="font-size: 90%;">eg 9</span>

**airween** <span style="color: grey; font-size: 90%;">21:04:08 UTC</span>

<span style="font-size: 90%;">yep :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:19 UTC</span>

<span style="font-size: 90%;">942190-9</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:33 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ Could you look into this during the week and come to a conclusion how to fix this, so we can merge it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:51 UTC</span>

<span style="font-size: 90%;">Sure</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:53 UTC</span>

<span style="font-size: 90%;">Thank you man.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:37 UTC</span>

<span style="font-size: 90%;">In the mixed news section, OWASP board member Vandana asked me to present CRS in her webcast series on spotlight OWASP projects. See the link in the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:32 UTC</span>

<span style="font-size: 90%;">It's only got 200 views on youtube, but she has like 80 likes on Linkedin, so I wonder if there are alternative channels for this. And if not, it's still nice.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:17 UTC</span>

<span style="font-size: 90%;">The incubator project has been created, but I still need to document how to enable the rules. And actually, I am not sure which rules, I want to add for the start. :wink:</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:09:32 UTC</span>

<span style="font-size: 90%;">I'm looking/listening to it right now.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:38 UTC</span>

<span style="font-size: 90%;">The new 942520 would be an option I think. What other candidates do we have?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:36 UTC</span>

<span style="font-size: 90%;">There was a rule that did not make it for PL1 for the 3.3 release. Anybody remember the id? It think it was a new rule by theMiddle.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:27 UTC</span>

<span style="font-size: 90%;">OK, nevermind. I guess I'll find it when I browse the archive.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:22 UTC</span>

<span style="font-size: 90%;">Final item on the agenda: Federico asked to shift this meeting to an earlier time. _@airween_ and _@fzipitria_ agreed to that idea.</span>

**airween** <span style="color: grey; font-size: 90%;">21:17:53 UTC</span>

<span style="font-size: 90%;">_@airween_ agreed? :open_mouth:</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:17:58 UTC</span>

<span style="font-size: 90%;">it was me</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:14 UTC</span>

<span style="font-size: 90%;">Oops. Sorry. I remembered that wrong.</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:19 UTC</span>

<span style="font-size: 90%;">np :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:22 UTC</span>

<span style="font-size: 90%;">Yes, it was _@azurIt_.</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:50 UTC</span>

<span style="font-size: 90%;">what does it mean "earlier"?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:56 UTC</span>

<span style="font-size: 90%;">For me, the meeting starts when the kids are in bed. If we do it earlier, the meeting is likely when my kids are eating super - which is actually fgs problem that we mean to solve.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:25 UTC</span>

<span style="font-size: 90%;">I do not know what earlier means. But 1-4 hours earlier means my kids are around.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:35 UTC</span>

<span style="font-size: 90%;">And I have 3 of them.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:53 UTC</span>

<span style="font-size: 90%;">Well, later would be better</span>

**walter** <span style="color: grey; font-size: 90%;">21:19:55 UTC</span>

<span style="font-size: 90%;">that seems a dealbreaker</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:03 UTC</span>

<span style="font-size: 90%;">But we cannot live with timezones</span>

**walter** <span style="color: grey; font-size: 90%;">21:20:04 UTC</span>

<span style="font-size: 90%;">oh no, not any later :rolling_on_the_floor_laughing:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:09 UTC</span>

<span style="font-size: 90%;">Yeah, I know</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:17 UTC</span>

<span style="font-size: 90%;">If we do it 5-8 hours earlier, then it's like really early for _@csanders_. But we might become more attractive to India and Pakistan.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:33 UTC</span>

<span style="font-size: 90%;">While for most of you in EU it is a proper time</span>

**walter** <span style="color: grey; font-size: 90%;">21:20:41 UTC</span>

<span style="font-size: 90%;">yes, that would absolutely work for me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:43 UTC</span>

<span style="font-size: 90%;">Normally I've get caught in the middle of working day</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:21:17 UTC</span>

<span style="font-size: 90%;">But I guess we cannot solve everything</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:58 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is there any time that would be more convenient for you and not the middle of the night for us?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:27 UTC</span>

<span style="font-size: 90%;">Well, not much, sincerely. shifting couple hours would hurt you a lot</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:43 UTC</span>

<span style="font-size: 90%;">It is more a wish, so I can contribute better</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:56 UTC</span>

<span style="font-size: 90%;">That is the problem that I see.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:06 UTC</span>

<span style="font-size: 90%;">But in the end, I could have made an effort on the weekend</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:08 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:16 UTC</span>

<span style="font-size: 90%;">I think Federico could do with a shift of 1-2 hours, but that would really hurt the other Europeans. Right now it's in the middle of the working days in the Americas but the Europeans are more or less with the exception of Federico and Azurit who would like to retire earlier.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:07 UTC</span>

<span style="font-size: 90%;">One way to deal with this would be to emphasize the meeting less by talking directly with people about issues. The way it is now is that I abandon most PRs and then wake up in a rush before the meeting ...</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:25:09 UTC</span>

<span style="font-size: 90%;">Usually, i need to leave at about 21:30.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:43 UTC</span>

<span style="font-size: 90%;">We can do meetings twice a month</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:47 UTC</span>

<span style="font-size: 90%;">But half the time</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:54 UTC</span>

<span style="font-size: 90%;">This is not really good for the project, so 1:1 discussions during the month and then less at the meeting would be better.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:13 UTC</span>

<span style="font-size: 90%;">We already do meetings twice the month at 2/3 of the time. Please not a 3rd meeting. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:20 UTC</span>

<span style="font-size: 90%;">:rolling_on_the_floor_laughing:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:37 UTC</span>

<span style="font-size: 90%;">Yeah, in the end, the meeting should be executive about resolutions</span>

**dune73** <span style="color: grey; font-size: 90%;">21:27:16 UTC</span>

<span style="font-size: 90%;">It's just a lot of PRs. Of course they could be reduced if somebody cleans them out before the meeting, so we have less to talk about.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:27:52 UTC</span>

<span style="font-size: 90%;">But it does not change the fact that it's eating / bathing time in Federico's family - and it's too late for Azurit, since I doubt we can get it done in 1 hour.</span>

**walter** <span style="color: grey; font-size: 90%;">21:27:53 UTC</span>

<span style="font-size: 90%;">yes, I try to merge before the meeting, but there are so many cases when there’s just that tiny last bit that you’re unsure about</span>

**walter** <span style="color: grey; font-size: 90%;">21:28:28 UTC</span>

<span style="font-size: 90%;">I’m afraid we won’t get a better compromise</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:32 UTC</span>

<span style="font-size: 90%;">Yes, with a lot of the PRs we just need to discuss it in the group. And we're really a project that profits from these group discussions, I think.</span>

**walter** <span style="color: grey; font-size: 90%;">21:28:48 UTC</span>

<span style="font-size: 90%;">yes, a lot of these PRs would keep hanging around for a long time otherwise…</span>

**dune73** <span style="color: grey; font-size: 90%;">21:29:38 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ For you it's just in the middle of the day and we collide with day job meetings that you have to attend?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:29:51 UTC</span>

<span style="font-size: 90%;">Same for _@csanders_, I guess.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:31:27 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:31:36 UTC</span>

<span style="font-size: 90%;">I'm basically in calls all my afternoon</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:31:42 UTC</span>

<span style="font-size: 90%;">When California wakes up</span>

**dune73** <span style="color: grey; font-size: 90%;">21:32:10 UTC</span>

<span style="font-size: 90%;">I see.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:35:02 UTC</span>

<span style="font-size: 90%;">Well I guess, the conclusion is once more that the timing at 2030 CET is not ideal for some of us, but other Europeans with kids (at least Franziska, Airween and me) would have a hard time shifting it 1-3 hours earlier and shifting it more would kill it for other participants (and would be in the middle of the workday for the Europeans).
But we try to acomodate for this a bit more by talking 1:1 with those affected like Federico, so we can still have them contribute. It just takes anticipation where they could make a contribution.</span>

**airween** <span style="color: grey; font-size: 90%;">21:38:04 UTC</span>

<span style="font-size: 90%;">IMHO we can say that the two monthly meeting are works. What if we shift only one of them?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:38:20 UTC</span>

<span style="font-size: 90%;">Sorry guys, i really have to go, my wife is already angry to me :smile: My reason is also my kid who refuses to go to sleep without me so, usually, i'm going to sleep at about 21:30. But i understand everyones reasons too. I will simply have to go about 21:30, but i think it's not a big deal. :slightly_smiling_face: Thank you and good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:38:46 UTC</span>

<span style="font-size: 90%;">that sounds actually fine, we’ll just deal with your PRs first :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:38:50 UTC</span>

<span style="font-size: 90%;">Thanks _@azurIt_.</span>

**walter** <span style="color: grey; font-size: 90%;">21:39:01 UTC</span>

<span style="font-size: 90%;">thank you for attending and of course the very nice phpBB support, people will love it!</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:39:38 UTC</span>

<span style="font-size: 90%;">thanks, it was all fun as usual :slightly_smiling_face: bye!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:24 UTC</span>

<span style="font-size: 90%;">Yeah, let's keep talking</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:26 UTC</span>

<span style="font-size: 90%;">_@airween_: I think it's not really a solution. Right now we have one person who can not attend. If we shift one of the meetings we have more people with serious problems.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:43 UTC</span>

<span style="font-size: 90%;">But I see this time hard to move for many</span>

**dune73** <span style="color: grey; font-size: 90%;">21:42:53 UTC</span>

<span style="font-size: 90%;">Yes, I guess that's the conclusion. And I need to think some more.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:43:00 UTC</span>

<span style="font-size: 90%;">Shall we close it for today?</span>

**airween** <span style="color: grey; font-size: 90%;">21:43:25 UTC</span>

<span style="font-size: 90%;">yep'</span>

**walter** <span style="color: grey; font-size: 90%;">21:45:53 UTC</span>

<span style="font-size: 90%;">yay!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:47:25 UTC</span>

<span style="font-size: 90%;">:fireworks:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:47:29 UTC</span>

<span style="font-size: 90%;">Always a pleasure</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:48:05 UTC</span>

<span style="font-size: 90%;">good night</span>

**airween** <span style="color: grey; font-size: 90%;">21:49:17 UTC</span>

<span style="font-size: 90%;">good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:50:34 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

