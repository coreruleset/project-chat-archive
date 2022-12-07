### Mon, Dec 5th, 2022

**dune73** <span style="color: grey; font-size: 90%;">19:30:19 UTC</span>

<span style="font-size: 90%;">Dear all, it's CRS meeting time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:26 UTC</span>

<span style="font-size: 90%;">Please find the agenda here: [https://github.com/coreruleset/coreruleset/issues/3036](https://github.com/coreruleset/coreruleset/issues/3036)</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:30:33 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:54 UTC</span>

<span style="font-size: 90%;">Wrap-Up of the sub-project status:

</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:45 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:45 UTC</span>

<span style="font-size: 90%;">Hello _@Paul Beckett_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">Hey _@xanadu_, nice to see you.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:31 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:35 UTC</span>

<span style="font-size: 90%;">I'm please to see that the idea with the subproject status seems to work nicely.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:40 UTC</span>

<span style="font-size: 90%;">Hello  _@maxleske_</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:24 UTC</span>

<span style="font-size: 90%;">hi there</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:39 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:45 UTC</span>

<span style="font-size: 90%;">Hello _@airween_, welcome. And hi _@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">For those who did not spot it, _@fzipitria_ was approached to formally take over libinjection maintenance by the intermediary maintainers. He accepted.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:47:14 UTC</span>

<span style="font-size: 90%;">Just for the record: acceptance was based on this being the last in my line of projects now. ¯\\\_(ツ)\_/¯</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:03 UTC</span>

<span style="font-size: 90%;">Hello and thank you for the summary _@dune73_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:15 UTC</span>

<span style="font-size: 90%;">AFAICT, this does not change anything as far as our interest in taking over libinjection as a project is concerned. But it's closer to us now.</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:20 UTC</span>

<span style="font-size: 90%;">Meeting closed? :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:16 UTC</span>

<span style="font-size: 90%;">The status items sound interesting enough. Does anybody know where _@theMiddle_ published the new challenges, or are they not published yet?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:40:07 UTC</span>

<span style="font-size: 90%;">:wave:
I'm going to publish all the new challenges under /challenges like this one: [https://sandbox.coreruleset.org/challenges/php-rce-01](https://sandbox.coreruleset.org/challenges/php-rce-01)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:30 UTC</span>

<span style="font-size: 90%;">:wave: all</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:41 UTC</span>

<span style="font-size: 90%;">Hello _@fzipitria_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:07 UTC</span>

<span style="font-size: 90%;">With the bug bounty findings, there is an open ReDoS question. Which finding / issue is this?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:30 UTC</span>

<span style="font-size: 90%;">LHETJGAX</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:57 UTC</span>

<span style="font-size: 90%;">But there are actually multiple ReDOS issues in that report</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:13 UTC</span>

<span style="font-size: 90%;">Multiple rules are affected</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:26 UTC</span>

<span style="font-size: 90%;">TBH, I don't think we should address those.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:35 UTC</span>

<span style="font-size: 90%;">At least not at the moment</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:00 UTC</span>

<span style="font-size: 90%;">LHETJGAX-2  is a JSON with 70K payload?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:15 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:28 UTC</span>

<span style="font-size: 90%;">The length is important. It could be any content.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:51 UTC</span>

<span style="font-size: 90%;">Except for the beginning, which needs to match the regex</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:07 UTC</span>

<span style="font-size: 90%;">:wave:
I'm going to publish all the new challenges under /challenges like this one: [https://sandbox.coreruleset.org/challenges/php-rce-01](https://sandbox.coreruleset.org/challenges/php-rce-01)</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:40:07 UTC</span>

<span style="font-size: 90%;">:wave:
I'm going to publish all the new challenges under /challenges like this one: [https://sandbox.coreruleset.org/challenges/php-rce-01](https://sandbox.coreruleset.org/challenges/php-rce-01)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:09 UTC</span>

<span style="font-size: 90%;">Can you explain how it works, briefly? (-> "Where is the challenge, what is a bounty hunter supposed to do?")</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:41:48 UTC</span>

<span style="font-size: 90%;">the format querystring parameter is vulnerable to remote command execution</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:54 UTC</span>

<span style="font-size: 90%;">LHETJGAX-2  : I do not think we should care. If you submit a specially crafted 70K payload, you can bring down anybody.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:05 UTC</span>

<span style="font-size: 90%;">so the hunter need to find a way to exploit it bypassing the CRS</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:42:27 UTC</span>

<span style="font-size: 90%;">hello everybody!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:45 UTC</span>

<span style="font-size: 90%;">Ooh:
[https://sandbox.coreruleset.org/challenges/php-rce-01?format=/bin/bash](https://sandbox.coreruleset.org/challenges/php-rce-01?format=/bin/bash)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:55 UTC</span>

<span style="font-size: 90%;">Nice little HTML response :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:19 UTC</span>

<span style="font-size: 90%;">Awesome _@theMiddle_!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:43:19 UTC</span>

<span style="font-size: 90%;">That's very cool _@theMiddle_</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:43:32 UTC</span>

<span style="font-size: 90%;">:pray: tnx!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:51 UTC</span>

<span style="font-size: 90%;">Got you. Thanks.
I think it would pay to add a single sentence summary btw title and the 3 options.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:13 UTC</span>

<span style="font-size: 90%;">yep</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:42 UTC</span>

<span style="font-size: 90%;">How many of these do you have planned to do?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:31 UTC</span>

<span style="font-size: 90%;">at least one per CRS rule set file, but it should be one per attack category techniques</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:46 UTC</span>

<span style="font-size: 90%;">Impressive. But agreed, that's what it takes to get ideal coverage. Starting with the rule set files would be very cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:18 UTC</span>

<span style="font-size: 90%;">Thank you for picking up writing down the decisions of this meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:25 UTC</span>

<span style="font-size: 90%;">_@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:06 UTC</span>

<span style="font-size: 90%;">Anybody has a different stance on LHETJGAX-2 ?</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:14 UTC</span>

<span style="font-size: 90%;">Not me!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:26 UTC</span>

<span style="font-size: 90%;">Good, so this is settled. OK _@maxleske_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:40 UTC</span>

<span style="font-size: 90%;">I think this is all we need to discuss with the status items.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:47 UTC</span>

<span style="font-size: 90%;">Great, thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:49 UTC</span>

<span style="font-size: 90%;">Thank you all for your support.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:17 UTC</span>

<span style="font-size: 90%;">Which brings us to project discussions. Let's start with the easy stuff.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:46 UTC</span>

<span style="font-size: 90%;">Before the pandemic we did 2 CRS community summits. That was a 1 day technical conference next to the OWASP AppSec EU conference.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:16 UTC</span>

<span style="font-size: 90%;">For 2023, this points to Tue Feb 14, 2023 at the Dublin Convention Center.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">We touched on this in Varese and I think we agreed to do this. I'm waiting for HQ to confirm we can have a room (or we rent one ourselves).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:49 UTC</span>

<span style="font-size: 90%;">If this works out, we can soon start with registration and program. We're probably looking at 10 sessions of 30min or something along those lines. Sponsors are invited / guaranteed a presentation slot btw.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:04 UTC</span>

<span style="font-size: 90%;">And then a night out in Dublin together.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:53:19 UTC</span>

<span style="font-size: 90%;">14 Feb? Valentine's Day</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:53:26 UTC</span>

<span style="font-size: 90%;">“Fall in love with your WAF: Install CRS today!"</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:45 UTC</span>

<span style="font-size: 90%;">A match made in the clouds!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:42 UTC</span>

<span style="font-size: 90%;">Before the pandemic we had about 25 people and met _@airween_ (and everybody else) for the first time face2face.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:27 UTC</span>

<span style="font-size: 90%;">How do you all see participation? (Ideally together with the OWASP conference)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:35 UTC</span>

<span style="font-size: 90%;">I’m in.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:55:59 UTC</span>

<span style="font-size: 90%;">Very interested, with sponsors, integrators etc. attending.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:56:09 UTC</span>

<span style="font-size: 90%;">Should be a good event.</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:56 UTC</span>

<span style="font-size: 90%;">I’m interested and hope my health allows…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:10 UTC</span>

<span style="font-size: 90%;">Let's talk about ftw and go-ftw. So the plan was to retire ftw after the release of 4.0. There is now a proposal to leave ftw behind at the start of the new year.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:37 UTC</span>

<span style="font-size: 90%;">I do not have a clear opinion on this. It seems we got use to go-ftw and it's being maintained very actively.</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:53 UTC</span>

<span style="font-size: 90%;">Yes, I’d say rather sooner than later</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:55 UTC</span>

<span style="font-size: 90%;">Are there arguments to keep ftw going for a few additional weeks / months.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:32 UTC</span>

<span style="font-size: 90%;">But I take it there are arguments for the sooner rather than later position?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:26 UTC</span>

<span style="font-size: 90%;">I don't think there are any arguments to keep ftw from the developer side. There might be from other users.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:58 UTC</span>

<span style="font-size: 90%;">But you do not know of any? I mean migration is relatively clear, is not it?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:11 UTC</span>

<span style="font-size: 90%;">Can we continue to maintain 3.3 with go-ftw alone?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:48 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ Did you recently re-work the 3.x tests so that they work with go-ftw? So we can do 3.3 using go-ftw?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:04 UTC</span>

<span style="font-size: 90%;">Yes, we merged those @ Varese</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:16 UTC</span>

<span style="font-size: 90%;">Awesome. So the hard work has already been done.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:58 UTC</span>

<span style="font-size: 90%;">There are no real needs now to keep ftw</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;">Thought so. So let's retire it at the end of the year. CRS v4 is close (I hope) and it's time to move on.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:09 UTC</span>

<span style="font-size: 90%;">[#2926](https://github.com/coreruleset/coreruleset/pull/2926): _@franbuehler_ can you lay down the question here, please?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:08:08 UTC</span>

<span style="font-size: 90%;">Yes, in Shivam Bathla's 2nd bypass list he found out that we don't test for sqli and rce in request headers.
Christian, Andrea and I discussed this in Varese and I think we are not sure if we need to test for sqli and rce in request headers.
I made this proposal PR where I copy some of the sqli and rce rules into higher PLs and test for REQUEST_HEADERS instead of ARGS.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:10 UTC</span>

<span style="font-size: 90%;">Now I'm not sure if I should pursue this idea and work on these rules or if anybody says: no sqli and rce in request headers is not common...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:55 UTC</span>

<span style="font-size: 90%;">Are there any opinions and should I continue to work on this?</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:32 UTC</span>

<span style="font-size: 90%;">I think this is a good idea. What paranoia level would be appropriate? PL2?</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:18 UTC</span>

<span style="font-size: 90%;">I think at least for SQLi this is interesting. I think applications suffering from RCE in headers is probably more rare…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:30 UTC</span>

<span style="font-size: 90%;">So you duplicate rules into higher PLs with different targets. How many rules is that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:11:35 UTC</span>

<span style="font-size: 90%;">I can only think of customer specific applications that would interpret the contents of a request header. Of course, web servers will use values from proxy headers but I very much doubt that it is possible to do SQLi or RCE that way. Maybe buffer overflows etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:50 UTC</span>

<span style="font-size: 90%;">I can see UA + Referer at PL2 and other headers at PL3, but I wonder if it's worth the performance.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:40 UTC</span>

<span style="font-size: 90%;">_@walter_ Do you have an example of a scenario where a header could lead to SQLi?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:13:17 UTC</span>

<span style="font-size: 90%;">I don't know yet how many rules. It's not complete yet. I think I will cover his findings. I don't think we can copy all of the rules?
Maybe 5 to 10 rules?</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:35 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Not really when asked….. Maybe some logging functionality or something like that…</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:14 UTC</span>

<span style="font-size: 90%;">I see Christian's and Max' point and to be honest, I don't know if applications do interprete this.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:19 UTC</span>

<span style="font-size: 90%;">Oh ok. That would then actually be more RCE like, I guess. Like Log4Shell</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:36 UTC</span>

<span style="font-size: 90%;">And would you do all headers or the ones typically logged (like UA + Referer)?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:14:37 UTC</span>

<span style="font-size: 90%;">sqli in req headers is common on ua, cookies and referer AFAIK</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:54 UTC</span>

<span style="font-size: 90%;">In the PR I do all REQUEST_HEADERS</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:56 UTC</span>

<span style="font-size: 90%;">Yes, Cookies of course too.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:59 UTC</span>

<span style="font-size: 90%;">But I can change that of course.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:00 UTC</span>

<span style="font-size: 90%;">I think all REQUEST_HEADERS is really heavy.
Imagine a GET request where you execute a single RegEx on the URI and then you add every header and CPU usage grows tenfold!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:28 UTC</span>

<span style="font-size: 90%;">I think UA + Referer would be reasonable.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:45 UTC</span>

<span style="font-size: 90%;">Ok, so we check for UA, Referer at PL2? And Cookies?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:57 UTC</span>

<span style="font-size: 90%;">And cookies, definitely.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:57 UTC</span>

<span style="font-size: 90%;">the problem with SQLi and Cookies is that there're a LOT of FPs. In my production I have removed request header cookie from CRS and I created a sepcific Lua module to avoid FPs</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:12 UTC</span>

<span style="font-size: 90%;">Adding these to 5-10 rules / stricter siblings in PL2 would be acceptable, I think.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:12 UTC</span>

<span style="font-size: 90%;">Oh!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:38 UTC</span>

<span style="font-size: 90%;">there are ton of app that use foo|bar  or quotes or comment syntaxes in cookie values :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:47 UTC</span>

<span style="font-size: 90%;">yep, or JSON…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:48 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ has a point there. But it's really cookie-sqli-specific is not it? Never seen an RCE / XSS problem in cookies.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:04 UTC</span>

<span style="font-size: 90%;">But then it's only PL2...</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:20:00 UTC</span>

<span style="font-size: 90%;">How about pushing the cookie checks to PL3?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:58 UTC</span>

<span style="font-size: 90%;">It's more and more rules to keep in sync. But I see the point.
<hint>Can crs-toolchain support us with that soon?</hint></span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:47 UTC</span>

<span style="font-size: 90%;">Possibly :slightly_smiling_face: Do you have a bit more for me to go on?</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:26 UTC</span>

<span style="font-size: 90%;">We have this 1 rule 1 data file connection which is really helpful. But here not so much.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:41 UTC</span>

<span style="font-size: 90%;">Here it would be better to allow n rules 1 data file.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:25:58 UTC</span>

<span style="font-size: 90%;">You can do it right now using includes</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:26:29 UTC</span>

<span style="font-size: 90%;">You just need an “empty” .ra file that includes the base one</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:28:13 UTC</span>

<span style="font-size: 90%;">Yes that's the best way for now. If we start to see more of those, we can think about a better approach.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:41:15 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:58 UTC</span>

<span style="font-size: 90%;">Really tough call</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:47 UTC</span>

<span style="font-size: 90%;">I think the toolchain might be able to</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:49 UTC</span>

<span style="font-size: 90%;">I'll continue to work on this PR and propose them at PL2.
Then we'll see of which rules we are talking.
Maybe the rules I use to cover Shivam's bypasses are not so prone to FP and are really clear sqli keywords. Not only 6 special characters or so...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:26 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:35 UTC</span>

<span style="font-size: 90%;">Idea: Instead of duplicating rules, we could in the future also add all the targets to PL1 rules. If we are in PL2, it's OK. But if we are in PL1, we remove the targets like UA dynamically. (-> Less rules in the ruleset).</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:24 UTC</span>

<span style="font-size: 90%;">That is a smart idea. It makes the rules a bit more complex to interpret, but is better than complete rule duplication.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:24:25 UTC</span>

<span style="font-size: 90%;">Would love to test the performance of that. Dynamic ctl actions vs extra rules.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:25:20 UTC</span>

<span style="font-size: 90%;">Didn't you say that the regex would still be evaluated for the excluded rules _@dune73_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:29 UTC</span>

<span style="font-size: 90%;">Every since _@theMiddle_ brought up such an idea in Varese, my head is spinning in overdrive on this concept.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:53 UTC</span>

<span style="font-size: 90%;">working on it :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:39 UTC</span>

<span style="font-size: 90%;">Unfortunately yes, _@maxleske_. But it's got to be tested.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:54 UTC</span>

<span style="font-size: 90%;">oh, ok</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:01 UTC</span>

<span style="font-size: 90%;">I guess this brings us to the painful discussions and some sad truths.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:05 UTC</span>

<span style="font-size: 90%;">So here is the thing: We covered all the bug bounty findings, but when running the tests, there are a few findings, a two digit number, that are still not detected in PL2 nor in PL3. And it seems there is very little movement. We are not getting anywhere here anymore.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:40 UTC</span>

<span style="font-size: 90%;">Similar situation with the keyword lists. We know we need a systematic approach, but we are failing to come up with the right sources for the keyword lists.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:51 UTC</span>

<span style="font-size: 90%;">Under the line, this results in false negatives.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:29:55 UTC</span>

<span style="font-size: 90%;">I'm still working on them. No need to test them yet :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:30:06 UTC</span>

<span style="font-size: 90%;">I do not think anyone make a real effort on the lists</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:14 UTC</span>

<span style="font-size: 90%;">Bug bounty findings _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:30:17 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:31 UTC</span>

<span style="font-size: 90%;">How many?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:04 UTC</span>

<span style="font-size: 90%;">Why are there dupes on the list still?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:04 UTC</span>

<span style="font-size: 90%;">All of the open ones, including the ones assigned to _@fzipitria_.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:17 UTC</span>

<span style="font-size: 90%;">We filtered those out months and months ago. How did they come back?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:40 UTC</span>

<span style="font-size: 90%;">~12</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:41 UTC</span>

<span style="font-size: 90%;">Which list _@xanadu_?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:49 UTC</span>

<span style="font-size: 90%;">Sorry, I meant the Bug Bounty spreadsheet</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:13 UTC</span>

<span style="font-size: 90%;">"Filtered out" as in issue solved / PR merged?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:17 UTC</span>

<span style="font-size: 90%;">Because _@azurIt_ created tests for the dupes too and they fail</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:18 UTC</span>

<span style="font-size: 90%;">It's all the tests in the private bug-bounty-tests repo. See the results folder or the dev chat last week.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:07 UTC</span>

<span style="font-size: 90%;">So you think you have a solution for about 12 of the failing tests, _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:35 UTC</span>

<span style="font-size: 90%;">Well, I need to look through all of them. But what I've noticed is that we made one mistake when thinking about the refactoring: we now fail to recognise non-evaded keywords</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:50 UTC</span>

<span style="font-size: 90%;">I think that will account for some of the issues</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:10 UTC</span>

<span style="font-size: 90%;">I see what you mean. This summarizes a thought I had to when looking at some of the remaining findings.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:30 UTC</span>

<span style="font-size: 90%;">Do you have a time-frame, _@maxleske_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:15 UTC</span>

<span style="font-size: 90%;">Not exactly. I wanted to finish that other finding first, then look through these. I hope I can say more next week</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:09 UTC</span>

<span style="font-size: 90%;">Thank you. "Other finding" as in ReDoS?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:40:26 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:30 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:40:36 UTC</span>

<span style="font-size: 90%;">But I think that's solved now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:18 UTC</span>

<span style="font-size: 90%;">So there is some perspective here, but it's nowhere near solving everything. The question is if we want to grind away or call it a day.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:30 UTC</span>

<span style="font-size: 90%;">Personally, I think we are holding back on all the great new CRSv4 detection rules over the edge cases where we fail. And I also think the unpleasant situation is hurting our project more than some false negatives however unpleasant they may be.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:55 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:43:28 UTC</span>

<span style="font-size: 90%;">I think that it is not 100% accurate.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:43:47 UTC</span>

<span style="font-size: 90%;">I get what you say about the new rules and features</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:02 UTC</span>

<span style="font-size: 90%;">But then most of them will not apply at lower paranoia levels</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:21 UTC</span>

<span style="font-size: 90%;">So a big chunk of out users base will be left out of the new stuff.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:43 UTC</span>

<span style="font-size: 90%;">Most lists target, precisely, users at PL1</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:53 UTC</span>

<span style="font-size: 90%;">But we are neglecting that user base somehow :confused:</span>

**walter** <span style="color: grey; font-size: 90%;">20:45:41 UTC</span>

<span style="font-size: 90%;">I will admit that I did not look at the java classes list as promised :disappointed: that should really be improved for 4.0</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:50 UTC</span>

<span style="font-size: 90%;">We really do with the lists, we really do. But I do not see us doing the necessary work in a useful timeframe.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:46:56 UTC</span>

<span style="font-size: 90%;">Is YAHOO-1OVO6EJE truly still in the state "1 - open"? We've never addressed it at all?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:46:59 UTC</span>

<span style="font-size: 90%;">How did that happen?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:47:33 UTC</span>

<span style="font-size: 90%;">I wasn't able to find a PR</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:47:35 UTC</span>

<span style="font-size: 90%;">Yahoo paid out, so it seems to be valid.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:47:53 UTC</span>

<span style="font-size: 90%;">I sincerely hope we can use threads in the future for topics</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:04 UTC</span>

<span style="font-size: 90%;">Now the list discussion is buried</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:48:15 UTC</span>

<span style="font-size: 90%;">Threads are so hard to follow on Slack…</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:48:22 UTC</span>

<span style="font-size: 90%;">Things get lost so easily.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:25 UTC</span>

<span style="font-size: 90%;">Let's call it "spread", not buried.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:31 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:49:10 UTC</span>

<span style="font-size: 90%;">I always think about our meeting on IRC when I'm upset with slack</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:32 UTC</span>

<span style="font-size: 90%;">I use threads all the time and they work</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:42 UTC</span>

<span style="font-size: 90%;">At least we did not have to talk about threading in IRC. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:50 UTC</span>

<span style="font-size: 90%;">We had two topics that wanted to discuss, but now we are discussing threads</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:49:54 UTC</span>

<span style="font-size: 90%;">My personal opinion: get the BB stuff done for 4.0, no matter what. If we don't it will leave a bitter feeling and it might come back to haunt us. Once we have those I can help with the lists. I would reevaluate in 2 weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:21 UTC</span>

<span style="font-size: 90%;">I don't think we will have it in two weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:36 UTC</span>

<span style="font-size: 90%;">Let me repost the stats in the dev channel.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:51:53 UTC</span>

<span style="font-size: 90%;">For the remaining issues, do we know if they are caused by bad PRs and good tests, or good PRs and bad tests?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:56 UTC</span>

<span style="font-size: 90%;">I see the bitter feeling creeping in. But I see growing bitterness all around, honestly.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:51:59 UTC</span>

<span style="font-size: 90%;">Do we know where the problem is?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:35 UTC</span>

<span style="font-size: 90%;">Some bad tests, but most of it is incomplete PRs / overly complex bug reports.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:20 UTC</span>

<span style="font-size: 90%;">I just re-posted the overview over the payloads we are not detecting. Each one of them in a single dump.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:08 UTC</span>

<span style="font-size: 90%;">Giving you an example: ...?code=cat /path/file.gz</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:25 UTC</span>

<span style="font-size: 90%;">That is what Max just mentioned</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:54:33 UTC</span>

<span style="font-size: 90%;">I see your point. But I can't give you an honest opinion about a time frame without having looked at the issues. In two weeks I can tell you yes or no.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:53 UTC</span>

<span style="font-size: 90%;">I am not trying to pressure you.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:55:05 UTC</span>

<span style="font-size: 90%;">I know :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:24 UTC</span>

<span style="font-size: 90%;">I just try to to support a honest look into the future.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:56 UTC</span>

<span style="font-size: 90%;">Before we all starve (and your stamina is way higher than other team members).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:56:35 UTC</span>

<span style="font-size: 90%;">I appreciate that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:54 UTC</span>

<span style="font-size: 90%;">Lists.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:10 UTC</span>

<span style="font-size: 90%;">Lists.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:23 UTC</span>

<span style="font-size: 90%;">Will anything change if we give it 2-4 more weeks.</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:31 UTC</span>

<span style="font-size: 90%;">BB = prevent past exploits, lists = prevent future exploits</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:41 UTC</span>

<span style="font-size: 90%;">Will more join the party, and do lists?</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:45 UTC</span>

<span style="font-size: 90%;">hard to say which needs to prioritize.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:53 UTC</span>

<span style="font-size: 90%;">I am happy to wait. But we need a perspective.</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:31 UTC</span>

<span style="font-size: 90%;">I would like to work on lists, but I’m not so good on scripting them and am not totally up to date, although of course I would support automating their updates as much as possible.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:58:40 UTC</span>

<span style="font-size: 90%;">Do not script them</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:58:54 UTC</span>

<span style="font-size: 90%;">Write the rationale of what you are doing</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:59 UTC</span>

<span style="font-size: 90%;">Check</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:02 UTC</span>

<span style="font-size: 90%;">This!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:59:11 UTC</span>

<span style="font-size: 90%;">With lists do we want to try and alter the existing rules, or start again from scratch for those rules based off lists like lolbas</span>

**walter** <span style="color: grey; font-size: 90%;">20:59:25 UTC</span>

<span style="font-size: 90%;">So, a bit of historiography why an entry is in the list, and use that as inspiration to find more entries?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:33 UTC</span>

<span style="font-size: 90%;">Inspiration</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:33 UTC</span>

<span style="font-size: 90%;">It's the lack of sources for the lists, that I see as problem. The scripting is easy, I think.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:54 UTC</span>

<span style="font-size: 90%;">I don’t care about the list if it is not out there</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:13 UTC</span>

<span style="font-size: 90%;">Can you elaborate _@fzipitria_? I do not get this</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:29 UTC</span>

<span style="font-size: 90%;">The list is a picture in time</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:00:32 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ IMO we also need a rework for some list rules, not from scratch</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:01:04 UTC</span>

<span style="font-size: 90%;">ops, this answer shoul de done in a thread :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:44 UTC</span>

<span style="font-size: 90%;">We don’t know where they come, how they were created.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:09 UTC</span>

<span style="font-size: 90%;">If we get a list that we actually know where it is coming from (as Paul said, lolbas for example), then I always prefer that list</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:32 UTC</span>

<span style="font-size: 90%;">Oh sure. I agree.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:36 UTC</span>

<span style="font-size: 90%;">Having a list that has functions from PHP 4 won’t be useful in 2022</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:02:06 UTC</span>

<span style="font-size: 90%;">virtual patching!</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">21:02:45 UTC</span>

<span style="font-size: 90%;">If you have PHP4 you need to :pray: , not virtual patch</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:03:04 UTC</span>

<span style="font-size: 90%;">lol, but PHP5 maybe... some legacy env</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:01 UTC</span>

<span style="font-size: 90%;">So some lists must be created from scratch, and we should not care about the content</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:06 UTC</span>

<span style="font-size: 90%;">It is just a reference</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:51 UTC</span>

<span style="font-size: 90%;">What do you mean by "not care abou the content"? Existing content in our rules? Or content of the list we found online?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:57 UTC</span>

<span style="font-size: 90%;">In the list</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:03 UTC</span>

<span style="font-size: 90%;">The rule is fine</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:03:37 UTC</span>

<span style="font-size: 90%;">For the lists: these are those issues labeled with 'list-update'. This list of lists is already complete, right? [https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+list+label%3A%22%3Azap%3A+list+update%22](https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+list+label%3A%22%3Azap%3A+list+update%22)
So my next task after Shivam Bathla's bypasses is to work on these lists. That's prio nr. 1?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">21:04:16 UTC</span>

<span style="font-size: 90%;">That would be awesome</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:58 UTC</span>

<span style="font-size: 90%;">This one has the overall: [https://github.com/coreruleset/coreruleset/issues/2621](https://github.com/coreruleset/coreruleset/issues/2621)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:00 UTC</span>

<span style="font-size: 90%;">That would be highly welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:41 UTC</span>

<span style="font-size: 90%;">So it's like we lack 20 lists?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">21:04:50 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:41 UTC</span>

<span style="font-size: 90%;">Nobody will be creating lists alone. We do it as a team.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:29 UTC</span>

<span style="font-size: 90%;">See this example: [https://github.com/coreruleset/coreruleset/pull/2791](https://github.com/coreruleset/coreruleset/pull/2791)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:49 UTC</span>

<span style="font-size: 90%;">You just throw an idea, and we discuss.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:05 UTC</span>

<span style="font-size: 90%;">Iterate, and get a better output. That’s it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:27 UTC</span>

<span style="font-size: 90%;">Better imperfect, but updated, than perfectly deprecated list.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:34 UTC</span>

<span style="font-size: 90%;">Good. _@xanadu_, _@emphazer_, _@airween_, _@Paul Beckett_ are you in the boat with grinding on for some more weeks, namely on findings good sources to base these lists on?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:07:03 UTC</span>

<span style="font-size: 90%;">I would prefer to look at non-list related things, personally.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:25 UTC</span>

<span style="font-size: 90%;">If you like, you can help out with the BB issues</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:27 UTC</span>

<span style="font-size: 90%;">Like bug bounty re-tests.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:29 UTC</span>

<span style="font-size: 90%;">?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:07:31 UTC</span>

<span style="font-size: 90%;">Sure</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:09:43 UTC</span>

<span style="font-size: 90%;">I will start looking at the issues assigned to Felipe, Andrea has some open ones. So if you could start with dune's list and work from that angle, that would be great.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">21:10:19 UTC</span>

<span style="font-size: 90%;">That sounds good.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:07:34 UTC</span>

<span style="font-size: 90%;">I can help with that.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:42 UTC</span>

<span style="font-size: 90%;">That would be much appreciated.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:09:18 UTC</span>

<span style="font-size: 90%;">I'm swamped until Christmas (got to study and re-qualify / re-certify for my GSEC), but happy to look at lists after that. Think I already proposed a couple of lists for Linux and windows commands</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:47 UTC</span>

<span style="font-size: 90%;">Yes, you did. Thanks.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:10:30 UTC</span>

<span style="font-size: 90%;">sure, I can try to help</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:35 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:46 UTC</span>

<span style="font-size: 90%;">Can you also try to dive _@dune73_?</span>

**walter** <span style="color: grey; font-size: 90%;">21:11:40 UTC</span>

<span style="font-size: 90%;">I’ll still keep the java list on my task list, but my health and work duties made it hard. But the week after Xmas I should have time to get it in good shape.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:45 UTC</span>

<span style="font-size: 90%;">_@emphazer_ looking at open lists would be most helpful.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:11:59 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:18 UTC</span>

<span style="font-size: 90%;">If I find the scarce time, I'm most interested in the entire crawler, UA lists business. It's a bit of a mess and vastly incomplete.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:27 UTC</span>

<span style="font-size: 90%;">So let me summarize: We are aware of pending shortcomings with BB findings and keyword lists, but we are not yet ready to give up on this as a team and we will continue the struggle for a few more weeks (do we feel like giving the team a Christmas gift?)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:50 UTC</span>

<span style="font-size: 90%;">Anybody in touch with _@Karel_? I get the feeling we could use him here.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:16:10 UTC</span>

<span style="font-size: 90%;">He's not very active on GH at the moment.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:16:44 UTC</span>

<span style="font-size: 90%;">We should also think on starting with the RC process maybe</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:16:59 UTC</span>

<span style="font-size: 90%;">That will be more focused on the release process itself</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:17:13 UTC</span>

<span style="font-size: 90%;">RC2 in January?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:17:21 UTC</span>

<span style="font-size: 90%;">You mean the automation, or the planning?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:46 UTC</span>

<span style="font-size: 90%;">The planning. I’m slowly progressing on the automation there</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:18:51 UTC</span>

<span style="font-size: 90%;">I need to go to bed. I'll complete the decisions tomorrow.
Bye and good night...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:04 UTC</span>

<span style="font-size: 90%;">RC planning is a good idea, but maybe not tonight. But no real need to do this as a team, I think. We could start with a draft documetn somewhere and then share for review.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:36 UTC</span>

<span style="font-size: 90%;">Anything else, or we call it a night?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:22:06 UTC</span>

<span style="font-size: 90%;">One more CRS meeting until Christmas… :smile: :snowflake:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">21:22:42 UTC</span>

<span style="font-size: 90%;">:smile: :hot_face: here</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:22:52 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:59 UTC</span>

<span style="font-size: 90%;">Have a good one!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:23:05 UTC</span>

<span style="font-size: 90%;">Good night</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:23:10 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:23:11 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:23:52 UTC</span>

<span style="font-size: 90%;">good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:25 UTC</span>

<span style="font-size: 90%;">Good night everybody. And thank you all for joining. It's heartwarming how you keep up!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:24:34 UTC</span>

<span style="font-size: 90%;">good .*</span>

**airween** <span style="color: grey; font-size: 90%;">21:26:21 UTC</span>

<span style="font-size: 90%;">sorry guys, I was very busy... good night!</span>

