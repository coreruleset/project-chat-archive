### Mon, Apr 7th, 2025

**airween** <span style="color: grey; font-size: 90%;">18:31:12 UTC</span>

<span style="font-size: 90%;">Evening'</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:35 UTC</span>

<span style="font-size: 90%;">Hello all!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:31:43 UTC</span>

<span style="font-size: 90%;">Hello :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:52 UTC</span>

<span style="font-size: 90%;">Hello</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:30 UTC</span>

<span style="font-size: 90%;">Hi everyone :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:34 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly chat</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:53 UTC</span>

<span style="font-size: 90%;">I hope you're all doing well :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:40 UTC</span>

<span style="font-size: 90%;">First item on the agenda: open WAF day in Barcelona.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:45 UTC</span>

<span style="font-size: 90%;">:bender:</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:34:54 UTC</span>

<span style="font-size: 90%;">:bender:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:34:06 UTC</span>

<span style="font-size: 90%;">It looks like it's going to happen, thanks to lots of initiative from _@fzipitria_.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:31 UTC</span>

<span style="font-size: 90%;">Team effort!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:12 UTC</span>

<span style="font-size: 90%;">We are planning nice talks, and the agenda is being filled as soon as this week</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:33 UTC</span>

<span style="font-size: 90%;">Later we are doing the formal invitation for people to register and share</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:58 UTC</span>

<span style="font-size: 90%;">The idea was to gather formally between the three OWASP projects: CRS, ModSecurity and Coraza, and make it special for all those users and integrators to have a place where we can share ideas and showcase the usage.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:34 UTC</span>

<span style="font-size: 90%;">I like this concept. Do you have an idea who is coming?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:37 UTC</span>

<span style="font-size: 90%;">Hope to see everyone that is going to attend the main OWASP conference and interest in WAFs there.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:11 UTC</span>

<span style="font-size: 90%;">We have some proposed speakers, but will have more data by EOW</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:38 UTC</span>

<span style="font-size: 90%;">Of course we are inviting sponsors, integrators, and everyone in general who wants to attend.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:27 UTC</span>

<span style="font-size: 90%;">We are securing sponsors also specific for the OWASP WAF Day, that will be great if we can keep for any of the projects :tada:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:39:46 UTC</span>

<span style="font-size: 90%;">Thanks _@fzipitria_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:12 UTC</span>

<span style="font-size: 90%;">Oh, interesting. We had cpanel pay 1.5K USD for a dinner once. But it was a one shot thing.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:19 UTC</span>

<span style="font-size: 90%;">Someone filled the closed PRs in the agenda, thanks for that :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:02 UTC</span>

<span style="font-size: 90%;">Next up: discussions.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:55 UTC</span>

<span style="font-size: 90%;">_@jit_, do you want to say something about the first one?</span>

**jit** <span style="color: grey; font-size: 90%;">18:43:03 UTC</span>

<span style="font-size: 90%;">Well, I think the issue is obvious, do we start supporting Ruby since it's the second most used server side programming language?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:40 UTC</span>

<span style="font-size: 90%;">As somebody who write ruby, I'm in favor. :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:21 UTC</span>

<span style="font-size: 90%;">I see merit in this, especially if we have a script/scriptlet to automatically pull the Ruby function names down and generate the regexes</span>

**jit** <span style="color: grey; font-size: 90%;">18:44:22 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4074](https://github.com/coreruleset/coreruleset/issues/4074)</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:44:33 UTC</span>

<span style="font-size: 90%;">I don't see any reason not to add support, but maybe some of those keywords should be put at PL-2 for example `Interrupt`</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:48 UTC</span>

<span style="font-size: 90%;">I believe we should have _some_ rational for which languages we check.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:14 UTC</span>

<span style="font-size: 90%;">We could use the TIOBE index, for example, although even the top 10 change from time to time.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:46:33 UTC</span>

<span style="font-size: 90%;">Common sense?
Ruby, yes
Eiffel, no</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:33 UTC</span>

<span style="font-size: 90%;">Opportunistic reasons? Because somebody was willing to do the work?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:02 UTC</span>

<span style="font-size: 90%;">Yes, but we can create followup work based on tiobe</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:09 UTC</span>

<span style="font-size: 90%;">If we do the work for one language, adding minimal support for a couple of others shouldn't be that much more effort, I think.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:18 UTC</span>

<span style="font-size: 90%;">Or follow-ups, yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:31 UTC</span>

<span style="font-size: 90%;">At least that is a common ground.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:46 UTC</span>

<span style="font-size: 90%;">_@jit_ would you be willing to take the lead since you've already invested a bit of time?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:49 UTC</span>

<span style="font-size: 90%;">Then we can have the time or not, but at least there is a clear idea on where to go</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:29 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:30 UTC</span>

<span style="font-size: 90%;">You also brought up the second item, _@jit_, although that PR has already been merged.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:37 UTC</span>

<span style="font-size: 90%;">Do you still want to discuss it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:43 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/4076](https://github.com/coreruleset/coreruleset/pull/4076)</span>

**jit** <span style="color: grey; font-size: 90%;">18:50:23 UTC</span>

<span style="font-size: 90%;">Nah, this is okay. I merged it today. :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:25 UTC</span>

<span style="font-size: 90%;">Well then. That's the agenda covered. Does anybody have something else they would like to discuss?</span>

**Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:52:36 UTC</span>

<span style="font-size: 90%;">Hey _@airween_, i wanted to discuss [https://github.com/coreruleset/coreruleset/issues/4017](https://github.com/coreruleset/coreruleset/issues/4017) a bit further as promised</span>

↳ **Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">Essentially, the root question i have is the following: should json decoding occur before or after transformation functions? With both we are seeing a bunch of regressions (currently we have it running both pre and post transformation functions with no regressions)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:07 UTC</span>

<span style="font-size: 90%;">4087 is the agenda...</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:14 UTC</span>

<span style="font-size: 90%;">That might be the wrong link _@Talha Abdul Ghafoor_?</span>

**Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:53:37 UTC</span>

<span style="font-size: 90%;">ah apologies fixed</span>

**Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">Essentially, the root question i have is the following: should json decoding occur before or after transformation functions? With both we are seeing a bunch of regressions (currently we have it running both pre and post transformation functions with no regressions)</span>

↳ **Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">Essentially, the root question i have is the following: should json decoding occur before or after transformation functions? With both we are seeing a bunch of regressions (currently we have it running both pre and post transformation functions with no regressions)</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:34 UTC</span>

<span style="font-size: 90%;">JSON decoding happens **BEFORE** any transformations, even **BEFORE** any rule evaluation</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">Transformations are part of a rule. They happen during the rule execution, for every rule execution.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:57:40 UTC</span>

<span style="font-size: 90%;">sorry, I meant that way</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:24 UTC</span>

<span style="font-size: 90%;">JSON decoding? Do you mean JSON parsing and creating ARGS out of the JSON payload?</span>

↳ **Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:57:31 UTC</span>

<span style="font-size: 90%;">yes</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:58:29 UTC</span>

<span style="font-size: 90%;">this is what I wrote above: this happens **BEFORE** any rule evaluation</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:40 UTC</span>

<span style="font-size: 90%;">sorry, I meant that way</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:57:40 UTC</span>

<span style="font-size: 90%;">sorry, I meant that way</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:18 UTC</span>

<span style="font-size: 90%;">Obviously that has to happen before you can to transformations, since you need to know the variables you want to inspect with a rule. So JSON body parsing happens before the request body phase rules start running.</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:29 UTC</span>

<span style="font-size: 90%;">this is what I wrote above: this happens **BEFORE** any rule evaluation</span>

↳ **Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">18:57:31 UTC</span>

<span style="font-size: 90%;">yes</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:58:29 UTC</span>

<span style="font-size: 90%;">this is what I wrote above: this happens **BEFORE** any rule evaluation</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:09 UTC</span>

<span style="font-size: 90%;">I'm not sure that performing JSON decoding a second time makes a lot of sense. Would you replace the ARGS? When exactly would you do it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:45 UTC</span>

<span style="font-size: 90%;">IMO, there's also difference between Unicode escape decoding and "JSON decoding"</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:12 UTC</span>

<span style="font-size: 90%;">The former we can achieve with `t:jsDecode`, I believe.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:40 UTC</span>

<span style="font-size: 90%;">I think _@Talha Abdul Ghafoor_ refers to JSON body parsing when he says decoding. See above.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:04 UTC</span>

<span style="font-size: 90%;">Hence my question...</span>

**Talha Abdul Ghafoor** <span style="color: grey; font-size: 90%;">19:06:13 UTC</span>

<span style="font-size: 90%;">so the issue is that we are getting some regressions when not running json decode for a second time (and also regressions when also running it post transformation functions). ill get some examples up in a minute where i can show the exact logic flow and why (based on the logic in the rule) the tests are failing</span>

**airween** <span style="color: grey; font-size: 90%;">19:07:30 UTC</span>

<span style="font-size: 90%;">_@Talha Abdul Ghafoor_ regarding to the issue 4017 - have you seen my last comment?

[https://github.com/coreruleset/coreruleset/issues/4017#issuecomment-2715454581](https://github.com/coreruleset/coreruleset/issues/4017#issuecomment-2715454581)

your perception was correct, the `\u00NNNN` decoding is by YAJL, the JSON parser</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:06 UTC</span>

<span style="font-size: 90%;">This is taking a long time. I feel it would be better to continue the discussion in the issue. _@Talha Abdul Ghafoor_ would that be ok with you?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:31 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:41 UTC</span>

<span style="font-size: 90%;">Anything else for tonight?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:52 UTC</span>

<span style="font-size: 90%;">Ok then. Please keep an eye on [https://github.com/coreruleset/coreruleset/issues/4017](https://github.com/coreruleset/coreruleset/issues/4017).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:20 UTC</span>

<span style="font-size: 90%;">Did you guys get in touch with Etienne who did this AI rule documentation thing?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:14:00 UTC</span>

<span style="font-size: 90%;">No, not yet. Thanks for reminding me.</span>

**airween** <span style="color: grey; font-size: 90%;">19:13:25 UTC</span>

<span style="font-size: 90%;">I tried that with `yyjson`: [https://github.com/coreruleset/coreruleset/issues/4017#issuecomment-2784326221](https://github.com/coreruleset/coreruleset/issues/4017#issuecomment-2784326221)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:00 UTC</span>

<span style="font-size: 90%;">And anybody, namely leaders, still in touch with Michela who showed up after the community call?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:32 UTC</span>

<span style="font-size: 90%;">Nope, but keeping an eye. She wanted to work on a blog post.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:18 UTC</span>

<span style="font-size: 90%;">Let's close for tonight. Thanks for showing up.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:15:35 UTC</span>

<span style="font-size: 90%;">Thanks for leading the meeting.
Good night :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:05 UTC</span>

<span style="font-size: 90%;">Good night</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:11 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:16:17 UTC</span>

<span style="font-size: 90%;">Bye</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:27 UTC</span>

<span style="font-size: 90%;">GN!</span>

