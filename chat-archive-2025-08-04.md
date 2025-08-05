### Mon, Aug 4th, 2025

**maxleske** <span style="color: grey; font-size: 90%;">18:31:08 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly CRS chat. Please take a few minutes to read through the agenda.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:33:07 UTC</span>

<span style="font-size: 90%;">Greetings</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:07 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:26 UTC</span>

<span style="font-size: 90%;">Hi there, we are having guests tonight, and I am sorry I can not follow the chat. Looking through the agenda, I quite like the idea of referencing friendly projects.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:34:46 UTC</span>

<span style="font-size: 90%;">Thanks. Enjoy the company.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:06 UTC</span>

<span style="font-size: 90%;">I want to give a shout out to _@Esad Cetiner_, who took care to update all of the plugins to use the new test format. Thanks a lot!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:59 UTC</span>

<span style="font-size: 90%;">For the first item on the agenda I feel like we need at least _@azurit_. Are you here?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:38:15 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:49 UTC</span>

<span style="font-size: 90%;">Great. So the question, which we've discussed before, I believe, is, whether we want to support third party WP plugins.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:39:08 UTC</span>

<span style="font-size: 90%;">I don't think it's possible.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:40:10 UTC</span>

<span style="font-size: 90%;">`$ grep "# WordPress" REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf | wc -l`
`424`</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:13 UTC</span>

<span style="font-size: 90%;">I agree and _@Esad Cetiner_ seems to share that view as well.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:40:45 UTC</span>

<span style="font-size: 90%;">This is the number of exclusion rules which i'm using for WP for my commercial services.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:41:02 UTC</span>

<span style="font-size: 90%;">And it's growing every day.</span>

**michela** <span style="color: grey; font-size: 90%;">18:41:14 UTC</span>

<span style="font-size: 90%;">Wow. That's a lot.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:31 UTC</span>

<span style="font-size: 90%;">Can we find a common root?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:47 UTC</span>

<span style="font-size: 90%;">Basically, someone would need to support a third party plugin for that.</span>

**michela** <span style="color: grey; font-size: 90%;">18:44:24 UTC</span>

<span style="font-size: 90%;">Alternate option: we could write a guide on using WordPress with CRS. I have a lot of experience supporting WordPress in CRS environments (as does _@azurit_, clearly :slightly_smiling_face: ), and I would be happy to contribute to this, or to lead it.

For example, perhaps making an exclusion for those using the WP Forms plug-in and running into the problem cited in issue #80, based on the query string parameter, `?page=wpforms-builder&view=fields&form_id` would help them. The developers of that plug-in could reference the CRS deployment guide in their documentation.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:44 UTC</span>

<span style="font-size: 90%;">That's not a bad idea.</span>

**michela** <span style="color: grey; font-size: 90%;">18:46:15 UTC</span>

<span style="font-size: 90%;">It would probably be useful to have something like this for WordPress, if not official plug-ins or similar, since it is incredibly popular.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ Probably yes if a level or security is lowered. I'm trying to create a one rule per WP plugin i.e. not mixing multiple plugins into one rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:54 UTC</span>

<span style="font-size: 90%;">From a cursory read of the issue it appears like OP only needs one extra rule. Is that really the case or would we be facing a flood of new rules? If we can support this plugin with a single rule on a best effort basis, then maybe we could make an exception.</span>

**michela** <span style="color: grey; font-size: 90%;">18:47:56 UTC</span>

<span style="font-size: 90%;">I see so many posts online advising people to disable ModSecurity due to false positives, and of course that's not wise at all. So, maybe there are things like this we can do to make it less likely for people to do that sort of thing. I think this is especially worth consideration because a lot of people visit these WordPress sites, and they deserve to have a safe experience -- enabled by CRS, of course!  :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:23 UTC</span>

<span style="font-size: 90%;">The policy could be: if it's 3 rules or less for a plugin then we can talk about supporting it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:52 UTC</span>

<span style="font-size: 90%;">I think it would be a great idea to have a section in the docs for popular frameworks that tells people what **not** to do and how to proceed. That would hopefully counteract some of that stuff you found _@michela_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:12 UTC</span>

<span style="font-size: 90%;">_@azurit_ what do you think about a "soft" / "best effort" policy for "low maintenance" plugins? (if there is even such a thing)</span>

**azurit** <span style="color: grey; font-size: 90%;">18:52:49 UTC</span>

<span style="font-size: 90%;">Most of the rules are targeted to URL `/wp-admin/admin-ajax.php` or `/wp-admin/admin.php` .</span>

**azurit** <span style="color: grey; font-size: 90%;">18:53:23 UTC</span>

<span style="font-size: 90%;">Maybe we can just dislabe FW for these two.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:53:37 UTC</span>

<span style="font-size: 90%;">But, maybe it's the same as disabling FW for WordPress at all.</span>

**michela** <span style="color: grey; font-size: 90%;">18:55:57 UTC</span>

<span style="font-size: 90%;">I’ve also found a lot of false positives in Wordpress are related to making POST requests to those URIs. </span>

**michela** <span style="color: grey; font-size: 90%;">18:56:15 UTC</span>

<span style="font-size: 90%;">Sorry, what is ‘FW’?  :slightly_smiling_face: </span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:56:42 UTC</span>

<span style="font-size: 90%;">**F**ire**W**all? :slightly_smiling_face:</span>

**azurit** <span style="color: grey; font-size: 90%;">18:56:49 UTC</span>

<span style="font-size: 90%;">Firewall</span>

**michela** <span style="color: grey; font-size: 90%;">18:57:49 UTC</span>

<span style="font-size: 90%;">Wordpress crams a tonne of JSON in the database for a lot of things (menus, posts and pages, I believe, and other content types). That can trigger WAF rules, because it can look suspicious. </span>

**azurit** <span style="color: grey; font-size: 90%;">18:58:34 UTC</span>

<span style="font-size: 90%;">The one big problem with WordPress is that lots of the plugins are sending JSON data not as JSON (with proper Content-Type) but simple POST form data.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:20 UTC</span>

<span style="font-size: 90%;">Ok. I understand that both of you think that we would be rather facing a "flood" scenario, meaning, either we have to be very generic, which is bad, or very specific, which would make support untenable.</span>

**michela** <span style="color: grey; font-size: 90%;">19:00:59 UTC</span>

<span style="font-size: 90%;">Ah. Thanks. Yah. I think we should not recommend people disable based on those URI patterns. As you suggested, it would mostly make the WAF ignore lots of potentially malicious requests to Wordpress. Wordpress should not allow such requests from unauthenticated uses, but one never knows what other possibilities might be present for attackers — they may be able to circumvent that in some cases. </span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:05 UTC</span>

<span style="font-size: 90%;">I propose we remain with our decision to not support WP plugins (in general). _@michela_, if I didn't misunderstand you would volunteer to spearhead the writing of a new docs section for WP, is that right?</span>

**michela** <span style="color: grey; font-size: 90%;">19:01:43 UTC</span>

<span style="font-size: 90%;">Yes. That’s right.  :blush: </span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:11 UTC</span>

<span style="font-size: 90%;">That's great, thank you!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:24 UTC</span>

<span style="font-size: 90%;">(Decision here _@franbuehler_)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:09 UTC</span>

<span style="font-size: 90%;">Let's move on. The next item is about a new rule for detecting LaTex injections.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:02 UTC</span>

<span style="font-size: 90%;">While this is indeed an attack vector, the number of users that would potentially benefit from this rule might be very small. Still we would need to maintain the rule. What should we do?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:57 UTC</span>

<span style="font-size: 90%;">In this case, the rule is fairly simple of course, but we all know that the devil is in the detail and the rule will likely have to be tuned in the future.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:05:08 UTC</span>

<span style="font-size: 90%;">I think it have a sense. I would support it BUT not as general as current implementation.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:49 UTC</span>

<span style="font-size: 90%;">Let's assume the rule has the fixes that _@jit_ wanted to make.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:06:22 UTC</span>

<span style="font-size: 90%;">If I am running a web-based LaTeX compiler then I **definitely **want this rule on, all the time, i.e. PL 1. But 99.9% of users are never going to do that, so probably a plugin makes most sense?</span>

**airween** <span style="color: grey; font-size: 90%;">19:06:42 UTC</span>

<span style="font-size: 90%;">I also prefer this as a plugin...</span>

**azurit** <span style="color: grey; font-size: 90%;">19:07:35 UTC</span>

<span style="font-size: 90%;">Or two rules: One, PL1, which will block specific latex 'commands' and second, PL2, which may be more general (similar as current rule).</span>

**michela** <span style="color: grey; font-size: 90%;">19:08:05 UTC</span>

<span style="font-size: 90%;">Would it make sense to consider moving rules to PL 2 or a plugin based on expected rate of FPs, rather than affected installations?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:21 UTC</span>

<span style="font-size: 90%;">Yes, from one point of view. My view is more on reducing maintenance work where we can and in that context the number of users makes more sense to me as a metric.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:00 UTC</span>

<span style="font-size: 90%;">When we can 'compile' CRS this problem goes away: simply enable or disable "Compile LaTeX rules" and it's solved.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:29 UTC</span>

<span style="font-size: 90%;">But for now, I do question if we want to have this 1 (or maybe 2) rules executing for everyone. That's a lot of unnecessary CPU cycles.</span>

**michela** <span style="color: grey; font-size: 90%;">19:10:57 UTC</span>

<span style="font-size: 90%;">Ah, fair enough.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:02 UTC</span>

<span style="font-size: 90%;">Yes :slightly_smiling_face:. I also feel like this should be a plugin. What I'm not sure about is whether we event want to add this as a plugin. Again: _we_ have will have to maintain it.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:11:39 UTC</span>

<span style="font-size: 90%;">Plugin.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:39 UTC</span>

<span style="font-size: 90%;">And I don't think any of us are running LaTex compilers on the web :smile:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:12:14 UTC</span>

<span style="font-size: 90%;">I guess we're just not cool enough :sweat_smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:12:17 UTC</span>

<span style="font-size: 90%;">_Hold my beer_ :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:12:39 UTC</span>

<span style="font-size: 90%;">If I were still at university... :wink:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:12:56 UTC</span>

<span style="font-size: 90%;">Oh, good old times... :slightly_smiling_face:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:13:07 UTC</span>

<span style="font-size: 90%;">overleaf probably</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:37 UTC</span>

<span style="font-size: 90%;">Alright. How about this: we'll add the rule(s) as a plugin _if_ _@jit_ agrees to maintain it.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:02 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:11 UTC</span>

<span style="font-size: 90%;">_@jit_?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:35 UTC</span>

<span style="font-size: 90%;">Are you currently with us?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:15:02 UTC</span>

<span style="font-size: 90%;">Anyway, i would prefer if it's not so general as current rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:04 UTC</span>

<span style="font-size: 90%;">It's probably too late for him now</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:42 UTC</span>

<span style="font-size: 90%;">Hopefully he'll respond tomorrow.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:51 UTC</span>

<span style="font-size: 90%;">(Decision here _@franbuehler_)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:36 UTC</span>

<span style="font-size: 90%;">Let's come back to the third item later and continue with the last item, since it concerns the same rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:22 UTC</span>

<span style="font-size: 90%;">In it's current form, the new LaTex rule is too generic. _@fzipitria_ and I think we should roll back, cut a patch release, and then roll out the rule again when it's ready.
Given the discussion above, I believe this has become a no-brainer, as we said we're not going to include the rule in the core anyway.
Any objections?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:00 UTC</span>

<span style="font-size: 90%;">Or rather: +1 if you agree :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:19:55 UTC</span>

<span style="font-size: 90%;">Does it require a new release?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:20:00 UTC</span>

<span style="font-size: 90%;">That's a non-zero amount of work to do‥</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:27 UTC</span>

<span style="font-size: 90%;">Yes. But I think it's worth it. And it's quick enough, I believe.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:20:56 UTC</span>

<span style="font-size: 90%;">We can do it with standard new release.</span>

**S0obi** <span style="color: grey; font-size: 90%;">19:21:12 UTC</span>

<span style="font-size: 90%;">On our side, we decided to skip 4.17.0 because of the FP risks for our specific context</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">What was causing the FP risks, out of interest? The LaTeX rule or something else?</span>

↳ **S0obi** <span style="color: grey; font-size: 90%;">19:23:53 UTC</span>

<span style="font-size: 90%;">The risk we identified is actually only on the new 934190 rule (LateX injection)</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:24:29 UTC</span>

<span style="font-size: 90%;">Interesting. That's useful context, thanks.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:53 UTC</span>

<span style="font-size: 90%;">We could. But I don't want people to start using the new release and then having to realise that they have to wait 5 weeks for the next one. If we issue a patch release now, they can take that straight away.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:56 UTC</span>

<span style="font-size: 90%;">If _@fzipitria_ is fine with doing the work then I think we can agree, right? :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:20 UTC</span>

<span style="font-size: 90%;">(Decision here _@franbuehler_)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:44 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:00 UTC</span>

<span style="font-size: 90%;">I'll cut the release today/tomorrow</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:32 UTC</span>

<span style="font-size: 90%;">Moving on to the last topic: we now have a couple of important and interesting projects in our "universe". Some, like Coraza, are something like "partners in spirit", others are just good to know about when you're a CRS user, e.g. _@airween_'s rule UI.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:25 UTC</span>

<span style="font-size: 90%;">I thought it might be nice to have a section somewhere, where we could highlight these projects. Disclaimer: I also want this because I always forget the URLs to these kinds of things (or even that they exist).</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:26:46 UTC</span>

<span style="font-size: 90%;">We do already have:
**Useful Tools**
[https://coreruleset.org/docs/6-development/6-6-useful_tools/](https://coreruleset.org/docs/6-development/6-6-useful_tools/)
"…many first and third party tools that help with ModSecurity and CRS development"</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:05 UTC</span>

<span style="font-size: 90%;">So it would be good to avoid duplication, e.g. generic projects vs specific tools</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:39 UTC</span>

<span style="font-size: 90%;">Yes, you're right. The other thing I was wondering: do we want to add those links to the README on GitHub as well? Personally, I often find those kinds of links helpful in other projects.</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:37 UTC</span>

<span style="font-size: 90%;">I think this is a good idea - at least a link to the URL what _@xanadu_ shared above</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:47 UTC</span>

<span style="font-size: 90%;">Yes, that might be better to avoid duplication.
I'll propose a PR, then you can all look over hit.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:55 UTC</span>

<span style="font-size: 90%;">(Decision here _@franbuehler_)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:46 UTC</span>

<span style="font-size: 90%;">FYI, I've been procrastinating and we had to move the community call back. Next proposed date is September 22.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:40 UTC</span>

<span style="font-size: 90%;">**Radical idea:** live in-person community call from the Dev Retreat? :open_mouth:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:55 UTC</span>

<span style="font-size: 90%;">The CRS Podcast? :rolling_on_the_floor_laughing:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:05 UTC</span>

<span style="font-size: 90%;">May be too radical.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:22 UTC</span>

<span style="font-size: 90%;">Put it in the wiki and we'll see :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:37 UTC</span>

<span style="font-size: 90%;">(Or we just livestream a project naming discussion)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:34:06 UTC</span>

<span style="font-size: 90%;">Pssst. People might leave the project :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:34:38 UTC</span>

<span style="font-size: 90%;">That would be more boring than any political discussion in the EU parliament :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:35:26 UTC</span>

<span style="font-size: 90%;">Oh come on! La7er FTW!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:34:55 UTC</span>

<span style="font-size: 90%;">Also, we've been talking about potential destinations and dates for the dev retreat this year. But we've already been here for an hour, so we will write you something to read and maybe start a poll to get your wishes into consideration.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:36:20 UTC</span>

<span style="font-size: 90%;">I vote for Switzerland.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:36 UTC</span>

<span style="font-size: 90%;">Thank you all for you input today. Have a great rest of the day / evening and see you soon!</span>

**azurit** <span style="color: grey; font-size: 90%;">19:37:33 UTC</span>

<span style="font-size: 90%;">I would like to ask one thing.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:28 UTC</span>

<span style="font-size: 90%;">Go ahead!</span>

**azurit** <span style="color: grey; font-size: 90%;">19:38:32 UTC</span>

<span style="font-size: 90%;">I'm having big positive response on this my plugin: [https://github.com/azurit/modsecurity-false-positive-report-plugin](https://github.com/azurit/modsecurity-false-positive-report-plugin)</span>

**azurit** <span style="color: grey; font-size: 90%;">19:39:14 UTC</span>

<span style="font-size: 90%;">Would like to make it official but not sure if it's suitable for CRS plugin.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:06 UTC</span>

<span style="font-size: 90%;">Why not? You've written it to fit into the plugin system, right?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:40:16 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">Why do you think it might not be suitable?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">Let's review it and decide.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:54:41 UTC</span>

<span style="font-size: 90%;">That's all from me. :slightly_smiling_face:</span>

