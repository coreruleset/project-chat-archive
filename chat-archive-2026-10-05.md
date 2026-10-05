### Mon, Oct 5th, 2026

**jit** <span style="color: grey; font-size: 90%;">18:31:07 UTC</span>

<span style="font-size: 90%;">Hi everyone!! :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:42 UTC</span>

<span style="font-size: 90%;">Hello everybbody!</span>

**jit** <span style="color: grey; font-size: 90%;">18:31:43 UTC</span>

<span style="font-size: 90%;">I will leave early today.</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:45 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:44 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly chat. There are only two items on the agenda tonight, but they're both a bit involved, so please take 10 minutes to read through the two GitHub issues referenced in the agenda.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:35:32 UTC</span>

<span style="font-size: 90%;">:wave::wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:31 UTC</span>

<span style="font-size: 90%;">I see more than two items. Can you tell us which ones we should read?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:37:32 UTC</span>

<span style="font-size: 90%;">Just wanted to ask if those 2 things are only my shit or something else. :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:43 UTC</span>

<span style="font-size: 90%;">> [https://github.com/coreruleset/coreruleset/issues/4840](https://github.com/coreruleset/coreruleset/issues/4840)
> [https://github.com/coreruleset/coreruleset/issues/4817](https://github.com/coreruleset/coreruleset/issues/4817)
</span>

↳ **azurit** <span style="color: grey; font-size: 90%;">18:46:13 UTC</span>

<span style="font-size: 90%;">So my shit get ignored. :grin: I put it into agenda to make sure it's not going to be ignored. :shrug:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">Which one is it?</span>

**jit** <span style="color: grey; font-size: 90%;">18:42:00 UTC</span>

<span style="font-size: 90%;">Let's start with 4817.</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:07 UTC</span>

<span style="font-size: 90%;">but 4817 belongs to _@fzipitria_, isn't it? :smile: (_Hi, fzipi, i hope you doing well and good_)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:13 UTC</span>

<span style="font-size: 90%;">For 4817, what do you think of a new rule for `member of` specifically?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:45:00 UTC</span>

<span style="font-size: 90%;">We will have to do that for every function: [https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com](https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:16 UTC</span>

<span style="font-size: 90%;">I would not want touch such a hard issues that is meant to be for fzipi. :slightly_smiling_face:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:45:07 UTC</span>

<span style="font-size: 90%;">Please do :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:56 UTC</span>

<span style="font-size: 90%;">I do not yet get, why "member of" would need a separate rule.</span>

**jit** <span style="color: grey; font-size: 90%;">18:45:00 UTC</span>

<span style="font-size: 90%;">We will have to do that for every function: [https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com](https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com)</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:45:00 UTC</span>

<span style="font-size: 90%;">We will have to do that for every function: [https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com](https://dev.mysql.com/doc/refman/8.4/en/json-search-functions.html?utm_source=chatgpt.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:28 UTC</span>

<span style="font-size: 90%;">Why can't we add it to one of the keyword lists? Is it the `/*` ?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:14 UTC</span>

<span style="font-size: 90%;">We could. Maybe that's enough. If there are more functions then we'll have to do something like that anyway.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:43 UTC</span>

<span style="font-size: 90%;">There are so many SQLi rules already. Something must be fitting, I think.</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:54 UTC</span>

<span style="font-size: 90%;">do we want to check `member of` with libinjection? (I haven't checked yet)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:07 UTC</span>

<span style="font-size: 90%;">The PL3 bypasses are really annoying. The one he pulls of with so few special chars. Argh.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:43 UTC</span>

<span style="font-size: 90%;">Like with ever so many SQLI keywords, `member of` is standard English of course.</span>

**airween** <span style="color: grey; font-size: 90%;">18:48:06 UTC</span>

<span style="font-size: 90%;">ah, no, we already have rules with libinjection, and I assume that should have catch it</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:07 UTC</span>

<span style="font-size: 90%;">Well, in any case, I think if it's many keywords we'll want to use a separate rule specific to MySQL (if we don't have that yet).</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">but `member of` will cause tons of FP's</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">So to keep sql dialects separate?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:27 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:34 UTC</span>

<span style="font-size: 90%;">Just my preference</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:37 UTC</span>

<span style="font-size: 90%;">Makes sense.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:41 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:00 UTC</span>

<span style="font-size: 90%;">Agreed. We are getting to the point that splitting would make more sense</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:21 UTC</span>

<span style="font-size: 90%;">Ok.
Decision: we need to detect those keywords and we probably want to split rules by dialect</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:24 UTC</span>

<span style="font-size: 90%;">Agreed?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:42 UTC</span>

<span style="font-size: 90%;">I'm not 100% percent convinced by the dialect split. From an operational view, I doubt this is necessary. But we can start that way.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:14 UTC</span>

<span style="font-size: 90%;">Agreed. It's a suggestion that we can look into.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:38 UTC</span>

<span style="font-size: 90%;">Let's move on to [https://github.com/coreruleset/coreruleset/issues/4840](https://github.com/coreruleset/coreruleset/issues/4840)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:01 UTC</span>

<span style="font-size: 90%;">I have a simple proposal for a fix: we add `chef-` to the PL1 FP list.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:11 UTC</span>

<span style="font-size: 90%;">It already contains `chef`.</span>

**jit** <span style="color: grey; font-size: 90%;">18:54:15 UTC</span>

<span style="font-size: 90%;">Good night everyone!! :night_with_stars:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:22 UTC</span>

<span style="font-size: 90%;">bb</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">That's a decent approach. Yet it's a bit arbitrary. Many of these keywords could come in the combination with a dash.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:13 UTC</span>

<span style="font-size: 90%;">How likely are we creating bypass options this way?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:42 UTC</span>

<span style="font-size: 90%;">No, it affects only those that are in the list. `chef-` is in the list, without enumerating all options intentionally.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:34 UTC</span>

<span style="font-size: 90%;">I think the problem is not on `chef-`, but on the added scope.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:44 UTC</span>

<span style="font-size: 90%;">Yes, but I am meaning to say, if we do `chef-`, we could equally do `ab-` and `at-` and `chancel-` etc. etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:18 UTC</span>

<span style="font-size: 90%;">Yes. But _@fzipitria_ is right, of course. It's a blunt solution</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:37 UTC</span>

<span style="font-size: 90%;">Yes, when adding REQUEST_FILENAME, we jumped into a new class of problem I think</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:54 UTC</span>

<span style="font-size: 90%;">That is likely.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:21 UTC</span>

<span style="font-size: 90%;">I think [https://github.com/coreruleset/go-ftw/issues/673](https://github.com/coreruleset/go-ftw/issues/673) will give us more input for decisions</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:54 UTC</span>

<span style="font-size: 90%;">Yes. The question remains though, do we remove the target from one rule now? It reopens the hole a little bit. We'll have to plug it again later.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:07 UTC</span>

<span style="font-size: 90%;">We need to do a pass on the list, as things like `/recipes/chef-salad, /blog/docker-tips, /en/dpkg-guide, /wiki/ansible-best-practices, /docs/netstat-explained` will match</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:22 UTC</span>

<span style="font-size: 90%;">This!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:57 UTC</span>

<span style="font-size: 90%;">We want most commands to receive some type of argument, provided there is a space somewhere</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:12 UTC</span>

<span style="font-size: 90%;">E.g. `chef --salad` is not `chef-salad`</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:58 UTC</span>

<span style="font-size: 90%;">That sounds like a more general reworking of the RCE rules (which I support). We would split rules into "argument accepting" and "non-argument accepting" commands? That would cause us to have much more knowledge about each command (and there are lots).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:49 UTC</span>

<span style="font-size: 90%;">That could be a step forward.
But what are "non-argument accepting" commands? Do we have anything in this category in Unix?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:05 UTC</span>

<span style="font-size: 90%;">`whoami`</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:23 UTC</span>

<span style="font-size: 90%;">The problem starts there already, many accept both</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:34 UTC</span>

<span style="font-size: 90%;">That's what I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:51 UTC</span>

<span style="font-size: 90%;">`whoami --version`</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:31 UTC</span>

<span style="font-size: 90%;">I don't know if we can make a decision today, sadly.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:51 UTC</span>

<span style="font-size: 90%;">No, I don't think we can. But we need a fast way forward to fix the FPs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:00 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:05 UTC</span>

<span style="font-size: 90%;">I propose to drop the target for the rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:11 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:19 UTC</span>

<span style="font-size: 90%;">Yes for now.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:00 UTC</span>

<span style="font-size: 90%;">Decsion: drop the `REQUEST_FILENAME` target again for rule 932260, open follow-up issue to discuss longterm fix / strategy</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:16 UTC</span>

<span style="font-size: 90%;">OK, let's do that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:18 UTC</span>

<span style="font-size: 90%;">_@azurit_ what was it you wanted to discuss?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:11:12 UTC</span>

<span style="font-size: 90%;">Just few things which are preventing me to close some issues. I linked them in 'plugins' section. Thanks.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:57 UTC</span>

<span style="font-size: 90%;">Ok, one issue with secrule_parsing and (I assume) your issue with Albedo. I'll check the Albedo issue.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:31 UTC</span>

<span style="font-size: 90%;">I'll also quickly check the other issue and maybe ask _@airween_ for help.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:08 UTC</span>

<span style="font-size: 90%;">I'll handle the secrules_parsing stuff.</span>

**airween** <span style="color: grey; font-size: 90%;">19:14:31 UTC</span>

<span style="font-size: 90%;">haha, I also started to fix one (secrules_parsing issue)</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:38 UTC</span>

<span style="font-size: 90%;">Sounds cool, thank you very much!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:58 UTC</span>

<span style="font-size: 90%;">Alright. Anything else to discuss?</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:21 UTC</span>

<span style="font-size: 90%;">(I started to finish issue 143 - it's already opened in my terminal, but could't progress since a few days...)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:03 UTC</span>

<span style="font-size: 90%;">One thing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:26 UTC</span>

<span style="font-size: 90%;">Shall we skip next month's Chat? We usually do while at the retreat.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:39 UTC</span>

<span style="font-size: 90%;">Yes</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:44 UTC</span>

<span style="font-size: 90%;">okay</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:21 UTC</span>

<span style="font-size: 90%;">Sweet. Then let's end for tonight. Thanks everyone. See you soon!</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:28 UTC</span>

<span style="font-size: 90%;">good night!</span>

**azurit** <span style="color: grey; font-size: 90%;">19:17:40 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:14 UTC</span>

<span style="font-size: 90%;">Good night</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:24 UTC</span>

<span style="font-size: 90%;">:wave:</span>

