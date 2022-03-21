### Mon, Feb 1st, 2021

**dune73** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">So cool to see you _@nerrehmit_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:22 UTC</span>

<span style="font-size: 90%;">Welcome</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:35 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:38 UTC</span>

<span style="font-size: 90%;">I hope it's not only the 2 of us.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:50 UTC</span>

<span style="font-size: 90%;">Hey _@franbuehler_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:16 UTC</span>

<span style="font-size: 90%;">boo!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">Hey, hey!</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">I haven’t slept through this one, that’s a good sign :wink:</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">heyhoo everybody</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:02 UTC</span>

<span style="font-size: 90%;">hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:10 UTC</span>

<span style="font-size: 90%;">Hello _@emphazer_ and _@airween_ !</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:35 UTC</span>

<span style="font-size: 90%;">I presented at the Usenix Enigma conference today. Unfortunately only virtually. But still my favorite conf. Presenting there has been a big goal of mine for several years. Here is the live tweet thread in case you are interested: [https://twitter.com/LeaKissner/status/1356275426184740872](https://twitter.com/LeaKissner/status/1356275426184740872)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:07 UTC</span>

<span style="font-size: 90%;">I see _@azurIt_ is around too and I saw _@fzipitria_ earlier today. I reckon he'll be around too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:22 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:29 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:58 UTC</span>

<span style="font-size: 90%;">We have a stuffed agenda and that was after a merging frenzy. So we better get going.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:09 UTC</span>

<span style="font-size: 90%;">Here is the agenda: [https://github.com/coreruleset/coreruleset/issues/1992](https://github.com/coreruleset/coreruleset/issues/1992)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">Before we dive in: Our new sponsor NGINX/F5 have paid the invoice, but they are a bit unresponsive with regards to a joint announcement. So this is still our private little secret. :slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:38:36 UTC</span>

<span style="font-size: 90%;">Not anymore :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:03 UTC</span>

<span style="font-size: 90%;">You have probably seen the new developer links in the wiki and wallarm released a doc with several WAF bypasses.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">Also targetting our rule set.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:26 UTC</span>

<span style="font-size: 90%;">So if somebody wants to close more holes, this could be a starting point.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">We merged 19 PRs, so the speed is quite impressive - even if some PRs can take long to be reviewed; the sheer number is impressive.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:08 UTC</span>

<span style="font-size: 90%;">I suggest we move to the open PRs. 10 of them. 1-2 will lead to bigger questions, also anticipating discussions that are scheduled under "other items".</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:41 UTC</span>

<span style="font-size: 90%;">PR 1868 is a contributed PR that does away with a PCRE dependency.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:08 UTC</span>

<span style="font-size: 90%;">It comes with a severe performance problem, but that problem only affects file uploads.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:47 UTC</span>

<span style="font-size: 90%;">The blog post at [https://coreruleset.org/20210106/introducing-msc_retest/](https://coreruleset.org/20210106/introducing-msc_retest/) looks at the old and the new regex in detail (example use case).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:09 UTC</span>

<span style="font-size: 90%;">And the question is now if we accept the performance decrease, or do we skip this PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:13 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:34 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:47 UTC</span>

<span style="font-size: 90%;">Hey, hey _@theMiddle_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:19 UTC</span>

<span style="font-size: 90%;">It’s hard to gauge this performance impact on a real live site. I find myself agreeing with the people who prefer keeping the PCRE-extension, but putting the new compatible regexp in a comment. I think integrators who use non-PCRE engines generally have an inhouse fork anyway and it would be only a very small effort for them to switch the patterns around.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:37 UTC</span>

<span style="font-size: 90%;">is this the performance decrease?
                                OLD REGEX    NEW REGEX
   modsec2-nojit-pattern.txt :   1.014460   630.129000
 modsec2-withjit-pattern.txt :   0.937687    38.511100
 modsec3-withjit-pattern.txt :   5.979850    56.225600</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">Yes, this is it.</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:01 UTC</span>

<span style="font-size: 90%;">:open_mouth:</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:22 UTC</span>

<span style="font-size: 90%;">630x is a lot…</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:23 UTC</span>

<span style="font-size: 90%;">then I choose that "we skip this PR" answer :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:34 UTC</span>

<span style="font-size: 90%;">but it might be 630 x a very small base number…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:56 UTC</span>

<span style="font-size: 90%;">That could be the case. And file uploads often take several seconds on the backend too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:07 UTC</span>

<span style="font-size: 90%;">But I started to value JIT when I wrote this blog post.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:09 UTC</span>

<span style="font-size: 90%;">I'd really love to get rid of PCRE, but I agree that we are not losing anything for the time being if we put the alternative rule into comments. Important: If we update the rule, we also have to update the pcre-free implementation.</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:48 UTC</span>

<span style="font-size: 90%;">could you make an estimate of how a single run would be on a typical FILES request, _@dune73_?</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:17 UTC</span>

<span style="font-size: 90%;">or would it open us up to an easy DoS by supplying a file with a large name (maybe we could have a rule before it that limits the length of a file name!)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:57 UTC</span>

<span style="font-size: 90%;">The numbers above are median over typical requests with typical file names. 1 file upload per request.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:06 UTC</span>

<span style="font-size: 90%;">The time is in seconds, cummulated across 100K requests if I remember correctly. So it's still fast.</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:57 UTC</span>

<span style="font-size: 90%;">thank you, so we’re talking about a mean of 630 sec / 100K requests = 0.0063 seconds per request?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:27 UTC</span>

<span style="font-size: 90%;">Yes. Only for file uploads. GET requests do not execute the rule.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:33 UTC</span>

<span style="font-size: 90%;">that sounds acceptable to me!</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:59 UTC</span>

<span style="font-size: 90%;">though we might be sensitive to DoS if people submit 1M long file names?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:45 UTC</span>

<span style="font-size: 90%;">Kind of. But _@fgs_ is pointing out, that we do not know how this affects various installations. If you run a separate file upload server with a substantial amount of traffic, you are probably toast.</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:03 UTC</span>

<span style="font-size: 90%;">I agree 6ms is still a long time on that timescale, but for my use case, it would be a rare request and I’d be willing to take it</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:09 UTC</span>

<span style="font-size: 90%;">how does counting FILES_NAMES? I mean there is a SecRequestBodyNoFilesLimit directive...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:20 UTC</span>

<span style="font-size: 90%;">I have not thought / investigated the DOS question. So no idea.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:36 UTC</span>

<span style="font-size: 90%;">So what do we do? Other opinions. I'm torn and would let the question up to you.</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:13 UTC</span>

<span style="font-size: 90%;">I would postpone the merge of this PR...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:50 UTC</span>

<span style="font-size: 90%;">And put it in comments, _@airween_?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:09 UTC</span>

<span style="font-size: 90%;">I am also torn. I like the idea of putting the new regular expression in a comment. It seems that no non-PCRE regexes are currently required.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">We could put it into the incubator, but measuring performance is hard and it could kill the incubator users (if any :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:39 UTC</span>

<span style="font-size: 90%;">putting it to incubator is a good idea</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:23 UTC</span>

<span style="font-size: 90%;">I do not like that idea but it is risky. We can guarantee it's not blocking in incubator. But we can not guarantee it's killing a production server. The performance costs are too high for incubator in my eyes. Besides, that is a new and delicate project. So rather be conservative about what we use there.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:58 UTC</span>

<span style="font-size: 90%;">@Walter: Can you live with the comment solution or do you really thing we ought to merge?</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;">I can live with that :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:08 UTC</span>

<span style="font-size: 90%;">Thanks. Let's do that then an d we continue with the next PR.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:10 UTC</span>

<span style="font-size: 90%;">So I'll change the PR and move the regex to the comment?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:20 UTC</span>

<span style="font-size: 90%;">Yes, please.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:31 UTC</span>

<span style="font-size: 90%;">And also add a comment??</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:35 UTC</span>

<span style="font-size: 90%;">Of course</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:52 UTC</span>

<span style="font-size: 90%;">1996: _@airween_ thinks this is ready to be merged. I have a feeling this might introduce new bypasses.</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:58 UTC</span>

<span style="font-size: 90%;">yeah, may be - then we have to investigate this possibility. nb: we discussed this issue here: [https://owasp.slack.com/archives/CBKGH8A5P/p1611003798117600](https://owasp.slack.com/archives/CBKGH8A5P/p1611003798117600)</span>

**airween** <span style="color: grey; font-size: 90%;">20:09:28 UTC</span>

<span style="font-size: 90%;">have to ask _@fgs_ and _@theMiddle_</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:32 UTC</span>

<span style="font-size: 90%;">if I read it correctly it was approved in that discussion?</span>

**airween** <span style="color: grey; font-size: 90%;">20:09:58 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:10 UTC</span>

<span style="font-size: 90%;">I guess it might reintroduce bypasses that use comments if we get rid of the /</span>

**airween** <span style="color: grey; font-size: 90%;">20:10:15 UTC</span>

<span style="font-size: 90%;">but we focused on cookies</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:22 UTC</span>

<span style="font-size: 90%;">Ah, my bad. So we covered this already (my memory is more like a stack)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:10:29 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:30 UTC</span>

<span style="font-size: 90%;">yes I think these would be quite rare in cookies</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:57 UTC</span>

<span style="font-size: 90%;">So do we have to split if we want to keep covering the comments?</span>

**airween** <span style="color: grey; font-size: 90%;">20:10:57 UTC</span>

<span style="font-size: 90%;">then we should split this rule...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:28 UTC</span>

<span style="font-size: 90%;">I mean this is about PHP stuff and Cookies it not my 1st choice when sending a PHP exploit...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:38 UTC</span>

<span style="font-size: 90%;">I see this splitting more and more. It's useful, but it makes the rule set more complicated and it decreases performance. But that's more a fundamental discussion beyond this PR.</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:15 UTC</span>

<span style="font-size: 90%;">I have never seen a cookie like this, it could be argued that it’s a very rare case and not warrant action on our part. But I wouldn’t mind a split.</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:15 UTC</span>

<span style="font-size: 90%;">we have to ask _@theMiddle_ what does he think about ARGS against this attacks</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:51 UTC</span>

<span style="font-size: 90%;">and can we left the / from the regex</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:16:24 UTC</span>

<span style="font-size: 90%;">IIRC I’ve a PoC that I used to create that rule… I can test this PR with it and try to understand if a bypass is possible or not</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:52 UTC</span>

<span style="font-size: 90%;">anyway t:replaceComments in that rule should do his work and replace all comment syntax (including /*) with a whitespace</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:07 UTC</span>

<span style="font-size: 90%;">That would be very helpful. So we postpone the decision and you test it and then _@airween_ can adopt.</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:14 UTC</span>

<span style="font-size: 90%;">right</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:40 UTC</span>

<span style="font-size: 90%;">_@airween_ maybe I can make it reachable for you too, if you agree we can work on it this week?</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:50 UTC</span>

<span style="font-size: 90%;">sure!</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:53 UTC</span>

<span style="font-size: 90%;">thanks!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:53 UTC</span>

<span style="font-size: 90%;">cool</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:01 UTC</span>

<span style="font-size: 90%;">that would be very welcome. maybe the general pattern can be improved somewhat. I take it the / is only relevant as part of a comment /* so maybe it can be worked around in the normal regexp</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:29 UTC</span>

<span style="font-size: 90%;">+1</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:22 UTC</span>

<span style="font-size: 90%;">Good. So that's settled for the time being.
The PR is actually two PRs. And we can not really discuss it without talking about a new idea that affects these two PRs. So I suggest we take that first.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:19 UTC</span>

<span style="font-size: 90%;">_@azurIt_ has submitted 2-3 PRs that depend on Lua. These are cool PRs, but we do not yet formally depend on Lua and several alternative re-implementations of ModSec that run CRS have not implemented the Lua connector.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:32 UTC</span>

<span style="font-size: 90%;">One way to address is would be to drop these PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:57 UTC</span>

<span style="font-size: 90%;">Another way would be to merge and welcome Lua dependency (and tie us closer to ModSec)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:40 UTC</span>

<span style="font-size: 90%;">Or we come up with a more general solution that would allow to integrate other rule sets into CRS. That way these rules would be released as a separate project under our CRS github. Or by a 3rd party.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:05 UTC</span>

<span style="font-size: 90%;">The advantage is that CRS remains slim and simple. Yet we are open for more sophisticated rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:26 UTC</span>

<span style="font-size: 90%;">So this would be like a standard structure / API for additional rule sets.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:45 UTC</span>

<span style="font-size: 90%;">We could put these response body decompressing rules in such a plugin structure.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:53 UTC</span>

<span style="font-size: 90%;">you mean a separate project under coreruleset github with all Lua extensions but keeping the CRS base (updated)?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:55 UTC</span>

<span style="font-size: 90%;">The incubator would be made to fit.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:14 UTC</span>

<span style="font-size: 90%;">And the DoS rules that we decided will leave the standard CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:37 UTC</span>

<span style="font-size: 90%;">So there are already 3-4 candidates for additional rule sets that could be used as plugin.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:04 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: 1 plugin per new rule set. So 1 for Incubator, 1 for body decompression, 1 for DoS rules ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:28 UTC</span>

<span style="font-size: 90%;">This is quite a big new feature for CRS so we need to think this through.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:40 UTC</span>

<span style="font-size: 90%;">But it would definitely enhance interoperability.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:25:42 UTC</span>

<span style="font-size: 90%;">I would consider to rewrite also exclusion packages as plugins.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:55 UTC</span>

<span style="font-size: 90%;">Interesting thought, _@azurIt_!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:52 UTC</span>

<span style="font-size: 90%;">An advantage is, that the "special" rulesets that we have integrated are tied to our slow release cycle. One of the reasons I wanted to separate the incubator. But I did not think of making it generic. Azurits PRs made me think about this and I get the feeling it could be a solution that opens us for the future.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:17 UTC</span>

<span style="font-size: 90%;">The details (include structure!) to be solved of course.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:33 UTC</span>

<span style="font-size: 90%;">What do you all think of this idea?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:30:06 UTC</span>

<span style="font-size: 90%;">I like this modular approach. However, the "plugins" should also be maintained...</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:10 UTC</span>

<span style="font-size: 90%;">I think it is a fantastic idea and could open up a world of new rulesets that use features like lua, where our policies are too restrictive.</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:16 UTC</span>

<span style="font-size: 90%;">We would have to think very clearly about how to weave those modular rulesets into the CRS, since they would use our scoring mechanism (presumably). We also can’t change the interaction mechanism too much, it would basically be a public API that we can’t easily change.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:33 UTC</span>

<span style="font-size: 90%;">This.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:22 UTC</span>

<span style="font-size: 90%;">I suggest _@azurIt_ and I think this through and we come back in a couple of weeks. I think this ought to go into 3.4, but as we will discuss later, we are probably delaying there too...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:37 UTC</span>

<span style="font-size: 90%;">... come back with a proposal.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:56 UTC</span>

<span style="font-size: 90%;">Azurit has already provided a PR which can serve as a draft, but I need to think about this some more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:07 UTC</span>

<span style="font-size: 90%;">And this kind of covers these 2 PRs, since I reckon (based on the feedback above) there is little support for merging 1968 and introduce a Lua dependency right now.</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:35 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:35:47 UTC</span>

<span style="font-size: 90%;">So i suggest to close it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:55 UTC</span>

<span style="font-size: 90%;">1968, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:20 UTC</span>

<span style="font-size: 90%;">And we keep 1993 open.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:34 UTC</span>

<span style="font-size: 90%;">Which brings us to 1990.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:04 UTC</span>

<span style="font-size: 90%;">This is the last big and potentially controversial PR for tonight. It's been something I have been planning / promising to do for a very long time.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:37:09 UTC</span>

<span style="font-size: 90%;">a big one!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:37:11 UTC</span>

<span style="font-size: 90%;">the problem with 1993 is how to makes it compatible with nginx…</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:37:41 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ isn't it?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:38:32 UTC</span>

<span style="font-size: 90%;">I mean this: [https://github.com/coreruleset/coreruleset/pull/1993/files#diff-b83b327f0b62e8168163c61f15fb0ac2c14169729e4f4184678337a15cd04decL95-L103](https://github.com/coreruleset/coreruleset/pull/1993/files#diff-b83b327f0b62e8168163c61f15fb0ac2c14169729e4f4184678337a15cd04decL95-L103)</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:38:55 UTC</span>

<span style="font-size: 90%;">It should be compatible.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:39:29 UTC</span>

<span style="font-size: 90%;">see [https://github.com/coreruleset/coreruleset/pull/1988#issuecomment-771118134](https://github.com/coreruleset/coreruleset/pull/1988#issuecomment-771118134)</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:40:11 UTC</span>

<span style="font-size: 90%;">ooh ok</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:40:13 UTC</span>

<span style="font-size: 90%;">tnx</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:12 UTC</span>

<span style="font-size: 90%;">It allows you to enable decoding and ModSec/CRS will then run through all sorts of decodings trying to make sense of a payload. Only at PL3 and PL4, but it is able to detect double encoded exploits like this (Base64 + Hex encoding) in a generic way.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:17 UTC</span>

<span style="font-size: 90%;">It takes 3 steps to enable this:
</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:08 UTC</span>

<span style="font-size: 90%;">The latter is crucial as we need this to add the TX variables with the decoded ARGS to all the rules that handle ARGS. If we add them by default, we lose 5-10% of performance on the default installation.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:38 UTC</span>

<span style="font-size: 90%;">The nice thing about PR 1990 is, that it surprisingly works with ModSec2 and ModSec3 alike.</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:48 UTC</span>

<span style="font-size: 90%;">would the performance hit also be present if the feature is disabled in crs-setup.conf?</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:59 UTC</span>

<span style="font-size: 90%;">ohh, wait, we do store some things in TX: by default of course</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:08 UTC</span>

<span style="font-size: 90%;">they’d have to be iterated</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:17 UTC</span>

<span style="font-size: 90%;">Yes, it would as the SecRules would do an additional regex match to identify potential targets.</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:24 UTC</span>

<span style="font-size: 90%;">yes, I see now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:29 UTC</span>

<span style="font-size: 90%;">Exactly. An additional iteration.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:49 UTC</span>

<span style="font-size: 90%;">The magic is in REQUEST-904-GENERIC-TRANSFORMATIONS.conf btw.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:04 UTC</span>

<span style="font-size: 90%;"># Transformation: base64DecodeExt
SecRule ARGS "!@streq %{ARGS}" \
    "id:904100,\
    phase:2,\
    pass,\
    t:base64DecodeExt,\
    nolog,\
    setvar:'tx.tf_1_base64DecodeExt_%{MATCHED_VAR_NAME}=%{MATCHED_VAR}'"</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:09 UTC</span>

<span style="font-size: 90%;">would this feature be doable as a plugin instead of having it as part of CRS proper?</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:23 UTC</span>

<span style="font-size: 90%;">I kind of like it but would not prefer to run PL3.</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:03 UTC</span>

<span style="font-size: 90%;">but if it was a plugin, people could use it regardless of PL</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:05 UTC</span>

<span style="font-size: 90%;">I am not sure. I have thought about this, but I am not yet sure.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:43:10 UTC</span>

<span style="font-size: 90%;">I would not tie it with PL level.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:23 UTC</span>

<span style="font-size: 90%;">Regardless of PL would be an advantage indeed.</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:38 UTC</span>

<span style="font-size: 90%;">it seems comparable to the LUA response decoding effort, it seems a good candidate for a plugin…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:02 UTC</span>

<span style="font-size: 90%;">I see some merits at PL2. But running this at PL1 would be odd, I think. There are bigger holes in PL1 than encoded parameters.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:00 UTC</span>

<span style="font-size: 90%;">Bye bye, I'm going to bed now. Good night.
I'll update the meeting decisions this week.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:30 UTC</span>

<span style="font-size: 90%;">Bye _@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:34 UTC</span>

<span style="font-size: 90%;">Thank you for joining</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:45:43 UTC</span>

<span style="font-size: 90%;">_@dune73_ i would either make it as a plugin or not tie it with PL - if someone wants to use it in PL1, why not allow it?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:42 UTC</span>

<span style="font-size: 90%;">OK. So you all agree I should at least try and make this a plugin and ideally independent of PL?</span>

**walter** <span style="color: grey; font-size: 90%;">20:47:21 UTC</span>

<span style="font-size: 90%;">that would be super awesome and a welcome nudge to have people try plugins</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:01 UTC</span>

<span style="font-size: 90%;">OK. I'll do that then and come back with a new version.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:40 UTC</span>

<span style="font-size: 90%;">1988: This is about the question if ModSec3 is ready for "include *.conf" or if we still need to advocate the inclusion of individual files.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:56 UTC</span>

<span style="font-size: 90%;">Latest update to the PR say we can drop the individual includes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:06 UTC</span>

<span style="font-size: 90%;">So this is ready to be merged?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:50:36 UTC</span>

<span style="font-size: 90%;">I was checking only sources of 2.9.3 version.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:51:34 UTC</span>

<span style="font-size: 90%;">2.9.3 supports wildcard in Include and IncludeOptional .</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:03 UTC</span>

<span style="font-size: 90%;">ok, so we have to verify this on modsec3</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:21 UTC</span>

<span style="font-size: 90%;">Modsec3 doesn't support IncludeOptional, only Include</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:52:29 UTC</span>

<span style="font-size: 90%;">Really? Hm :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:46 UTC</span>

<span style="font-size: 90%;">argh</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:48 UTC</span>

<span style="font-size: 90%;">That's cruel!</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:56 UTC</span>

<span style="font-size: 90%;">let me check again - but as I remember I ran into this few days ago...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:31 UTC</span>

<span style="font-size: 90%;">Time is progressing. _@airween_: Can you look into this and get back to _@azurIt_ and you see if it can be merged as is?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:53:54 UTC</span>

<span style="font-size: 90%;">azurit@azurit:~/public_html/modsecurity/modsec_src/modsecurity-v3.0.4$ grep -R -i IncludeOptional * 
azurit@azurit:~/public_html/modsecurity/modsec_src/modsecurity-v3.0.4$</span>

**airween** <span style="color: grey; font-size: 90%;">20:54:11 UTC</span>

<span style="font-size: 90%;">yep - now I checked, the parser doesn't contain this token</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:54:23 UTC</span>

<span style="font-size: 90%;">Ok, what about wildcards?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:54:36 UTC</span>

<span style="font-size: 90%;">I remember I had to ask for include originally</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:54:39 UTC</span>

<span style="font-size: 90%;">IncludeOptional can be bypassed by providing empty *.conf file</span>

**airween** <span style="color: grey; font-size: 90%;">20:55:14 UTC</span>

<span style="font-size: 90%;">yep</span>

**airween** <span style="color: grey; font-size: 90%;">20:55:19 UTC</span>

<span style="font-size: 90%;">2021/02/01 20:54:55 [emerg] 672483[#672483](https://github.com/coreruleset/coreruleset/issues/#672483): "modsecurity_rules_file" directive Rules error. File: /usr/share/modsecurity-crs/owasp-crs.load. Line: 6. Column: 81. Invalid input:  IncludeOptional /etc/modsecurity/crs/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf in /etc/nginx/sites-enabled/default:52</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:25 UTC</span>

<span style="font-size: 90%;">IncludeOptional comes from Apache</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:30 UTC</span>

<span style="font-size: 90%;">Can you take this offline, please?
It's a bit rude from me, but the agenda is really long...</span>

**airween** <span style="color: grey; font-size: 90%;">20:56:34 UTC</span>

<span style="font-size: 90%;">_@azurIt_ you mean Include /path/to/*.conf? it works</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:56:58 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ this is different includeoptional</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:57:18 UTC</span>

<span style="font-size: 90%;">_@airween_ yes, cool! so it can be merged as this PR is not using IncludeOptional</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:19 UTC</span>

<span style="font-size: 90%;">(no worries, I second _@dune73_ proposal)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:40 UTC</span>

<span style="font-size: 90%;">Let's chat it later/afterwards</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:54 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:19 UTC</span>

<span style="font-size: 90%;">1986 is super cool and a very nice implementation. And obviously another plugin candidate.</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:29 UTC</span>

<span style="font-size: 90%;">_@azurIt_ I'm using this one:
Include /usr/share/modsecurity-crs/rules/*.conf</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:58:48 UTC</span>

<span style="font-size: 90%;">Cool! Thank you.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">21:00:44 UTC</span>

<span style="font-size: 90%;">So do you think it can be merged?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:59:03 UTC</span>

<span style="font-size: 90%;">_@dune73_ I agree with plugin idea.</span>

**walter** <span style="color: grey; font-size: 90%;">20:59:06 UTC</span>

<span style="font-size: 90%;">this is very cool and indeed could be a good plugin!</span>

**walter** <span style="color: grey; font-size: 90%;">20:59:36 UTC</span>

<span style="font-size: 90%;">clamd could run sandboxed and accept inputs over socket, it would be much easier to secure than the old stuff we had</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:57 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:54 UTC</span>

<span style="font-size: 90%;">1978 is problematic. It solves FPs with the help of Lua. I do not think we can make it a plugin and I do not see how we could integrate it into CRS...</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:01:32 UTC</span>

<span style="font-size: 90%;">Yes, unfortunately. I suggest to close it. But it would resolve lot's of FPs. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:05 UTC</span>

<span style="font-size: 90%;">couldn’t it work as a plugin? it could secruleremoveid 930120 to get rid of the old rule, and replace it by another</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:02:21 UTC</span>

<span style="font-size: 90%;">It, probably, could be rewritten as plugin but i don't know if it's enough to create plugin from this.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:11 UTC</span>

<span style="font-size: 90%;">Conceptually yes, but would anybody install a plugin because of an FP when you can do SecRuleRemoveById without the plugin to solve the FP too?</span>

**walter** <span style="color: grey; font-size: 90%;">21:03:37 UTC</span>

<span style="font-size: 90%;">true, but it’s a very nice rule :slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:03:47 UTC</span>

<span style="font-size: 90%;">Thanks! :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">21:04:37 UTC</span>

<span style="font-size: 90%;">I haven’t seen too much FP on 930120 though so in my opinion it’s not a big problem, but could depend on environment…</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:38 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**walter** <span style="color: grey; font-size: 90%;">21:05:07 UTC</span>

<span style="font-size: 90%;">but since it does lua, it would have to be a plugin</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:05:23 UTC</span>

<span style="font-size: 90%;">maybe a part of bigger plugin which solves also other things</span>

**walter** <span style="color: grey; font-size: 90%;">21:05:38 UTC</span>

<span style="font-size: 90%;">oh I would be in favor of having smaller plugins doing one clear thing well</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:28 UTC</span>

<span style="font-size: 90%;">You could develop a "popular lua scripts to avoid certain FPs"-plugin.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:06:37 UTC</span>

<span style="font-size: 90%;">That way you could suck up several FPs.</span>

**walter** <span style="color: grey; font-size: 90%;">21:06:53 UTC</span>

<span style="font-size: 90%;">that’s true!</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:51 UTC</span>

<span style="font-size: 90%;">as long as it focuses just on this purpose</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:00 UTC</span>

<span style="font-size: 90%;">But I guess 1978 as off the table in this form.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:08 UTC</span>

<span style="font-size: 90%;">Sorry. It is good work.</span>

**walter** <span style="color: grey; font-size: 90%;">21:09:36 UTC</span>

<span style="font-size: 90%;">:bulb: a tip for plugins: they should each have a SecComponentSignature "myplugin/0.1". all these are separately given in the output and could help debugging people’s audit logs</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:10:09 UTC</span>

<span style="font-size: 90%;">_@dune73_ no worry! I'm closing it.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:53 UTC</span>

<span style="font-size: 90%;">Thank you for your understanding. You do so much work right now and I feel sorry that we are reluctant to merge a good share of it.
Coming to an end with the PRs here: 1958.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:12:10 UTC</span>

<span style="font-size: 90%;">Ok, here i still don't understand that one last thing.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:16 UTC</span>

<span style="font-size: 90%;">This is almost ready, but I think it is a candidate to be split as well. It's a complicated construct to get rid of FPs with widspread Google OAuth2. I do not see any other way to pull this off, but Cookies need to be covered too.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:31 UTC</span>

<span style="font-size: 90%;">Ah, OK. What is it that you do not understand.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:12:44 UTC</span>

<span style="font-size: 90%;">Using:
SecRule ARGS_NAMES "@rx ^(code|scope|state)$"is not the same as my solution.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:13:06 UTC</span>

<span style="font-size: 90%;">(Btw, I wasn't able to make it work but that's probably my fault)</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:13:24 UTC</span>

<span style="font-size: 90%;">what about sending two 'code' args?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:13:58 UTC</span>

<span style="font-size: 90%;">Will it bypass the checks?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:14:53 UTC</span>

<span style="font-size: 90%;">I know that, if it will, you probably cannot to use this to abuse something but you will force CRS to detect bogus Google OAuth2 callback.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:02 UTC</span>

<span style="font-size: 90%;">But you have an arg counter in your rule, don't you? That solves the unique parameter problem, or you mean one could trade one of the 3 parameters for an exploit? Cunning ...</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:16:09 UTC</span>

<span style="font-size: 90%;">I mean, sending, for example, code=&code=&state=</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:16:25 UTC</span>

<span style="font-size: 90%;">*fixed the typo above</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:17:12 UTC</span>

<span style="font-size: 90%;">This definitely isn't Google OAuth2 callback so it shoudl not be detected as one.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:17:37 UTC</span>

<span style="font-size: 90%;">There are 3 ARGS and all are passing the ^(code|scope|state)$  regexp.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:52 UTC</span>

<span style="font-size: 90%;">You are right. Your rule is better.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:07 UTC</span>

<span style="font-size: 90%;">Then it's only the split question.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:12 UTC</span>

<span style="font-size: 90%;">What do you and the others think?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:19:01 UTC</span>

<span style="font-size: 90%;">What are the benefits of splitting also XML?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:20 UTC</span>

<span style="font-size: 90%;">Not much. The complicated rule would be a bit simpler without the XML target. Less thinking when you read the rule.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:21:12 UTC</span>

<span style="font-size: 90%;">It will also simplifies checking for GOAuth2 a little.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:22:11 UTC</span>

<span style="font-size: 90%;">But i don't know if there can be XML if REQUEST_METHOD is GET.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:35 UTC</span>

<span style="font-size: 90%;">Probably not. Definitely not with the body processor.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:22:40 UTC</span>

<span style="font-size: 90%;">(GOAuth2 callback is always GET)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:52 UTC</span>

<span style="font-size: 90%;">Let's take this offline (-> github) and talk about this during the week.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:23:05 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:44 UTC</span>

<span style="font-size: 90%;">Final PR 1975: The contributor brings an alternative URI structure to our attention. I wonder if we can get rid of the one we use. Can we run then side by side?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:50 UTC</span>

<span style="font-size: 90%;">-> rx vs contains</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:24:04 UTC</span>

<span style="font-size: 90%;">For the last one, i think that whole Nextcloud ex. package needs to be rewritten.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:25:06 UTC</span>

<span style="font-size: 90%;">I was also having some complains about it before ( [https://github.com/coreruleset/coreruleset/issues/1947](https://github.com/coreruleset/coreruleset/issues/1947) ) and these new URI structure is even worse.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:25:16 UTC</span>

<span style="font-size: 90%;">most of the rules are not matching it</span>

**walter** <span style="color: grey; font-size: 90%;">21:25:37 UTC</span>

<span style="font-size: 90%;">ouch</span>

**walter** <span style="color: grey; font-size: 90%;">21:25:41 UTC</span>

<span style="font-size: 90%;">that’s a pity</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:26:14 UTC</span>

<span style="font-size: 90%;">So i would suggest to create a whole new exclusion package which, as _@dune73_ suggested, can be run side-by-side with current one until is good enough</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:26:30 UTC</span>

<span style="font-size: 90%;">Then it can replace the old one.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:36 UTC</span>

<span style="font-size: 90%;">You mean 2 exlcusion packages in CRS for the time being?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:44 UTC</span>

<span style="font-size: 90%;">Time being == 3.4 release?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:26:56 UTC</span>

<span style="font-size: 90%;">Ou, probably not in 3.4.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:22 UTC</span>

<span style="font-size: 90%;">So we would replace the package before 3.4?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:32 UTC</span>

<span style="font-size: 90%;">This work has to happen in the next few weeks to be sure then.</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:29:13 UTC</span>

<span style="font-size: 90%;">I would review and merge (if possible) this PR and start work on new exclusion package after 3.4.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:30:11 UTC</span>

<span style="font-size: 90%;">Can you do the review?</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:30:17 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**walter** <span style="color: grey; font-size: 90%;">21:30:24 UTC</span>

<span style="font-size: 90%;">awesome!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:31:08 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:31:33 UTC</span>

<span style="font-size: 90%;">That means we're done with the PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:31:38 UTC</span>

<span style="font-size: 90%;">Feeling relieved.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:32:06 UTC</span>

<span style="font-size: 90%;">Python 2.7 is being deprecated and I do not understand what our status is here.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:32:18 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ could you explain this to us?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:32:18 UTC</span>

<span style="font-size: 90%;">Our status is not good</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:32:22 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:32:42 UTC</span>

<span style="font-size: 90%;">So, we use python for our tests. Basically, for ftw</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:32:59 UTC</span>

<span style="font-size: 90%;">Our pipeline gets the proper python modules, on each run</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:33:33 UTC</span>

<span style="font-size: 90%;">The pip command, which is used for getting python modules, has dropped support for python 2</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:33:52 UTC</span>

<span style="font-size: 90%;">I mean, will refuse to install anything py2 related</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:34:12 UTC</span>

<span style="font-size: 90%;">Which makes sense, otherwise you cannot deprecate things</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:34:25 UTC</span>

<span style="font-size: 90%;">But we are in the situation we still kind of depend of py2</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:34:27 UTC</span>

<span style="font-size: 90%;">are python 2 modules via pip not avaible anymore?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:34:33 UTC</span>

<span style="font-size: 90%;">They are</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:34:45 UTC</span>

<span style="font-size: 90%;">With an older pip version, we can still get those</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:34:56 UTC</span>

<span style="font-size: 90%;">ok</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:35:00 UTC</span>

<span style="font-size: 90%;">But it is going to be more and more difficult, for a good reason</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:35:09 UTC</span>

<span style="font-size: 90%;">We should drop support for py2</span>

**dune73** <span style="color: grey; font-size: 90%;">21:35:25 UTC</span>

<span style="font-size: 90%;">So we are in kind of a grace period and ftw needs to be ported?</span>

**walter** <span style="color: grey; font-size: 90%;">21:35:47 UTC</span>

<span style="font-size: 90%;">will it break hard?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:35:48 UTC</span>

<span style="font-size: 90%;">Last time we interacted with _@fgs_, I had a solution working</span>

**csanders** <span style="color: grey; font-size: 90%;">21:35:51 UTC</span>

<span style="font-size: 90%;">It shouldn’t be too too hard to port but i saw there was ftw-go</span>

**airween** <span style="color: grey; font-size: 90%;">21:35:53 UTC</span>

<span style="font-size: 90%;">_@emphazer_ :
[https://pypi.org/project/pip/](https://pypi.org/project/pip/)

Note: pip 21.0, in January 2021, removed Python 2 support, per pip's Python 2 support policy. Please migrate to Python 3.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:04 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:06 UTC</span>

<span style="font-size: 90%;">Both</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:22 UTC</span>

<span style="font-size: 90%;">So, for the py3 module, which we did look into a lot past months</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:31 UTC</span>

<span style="font-size: 90%;">Federico was worried about compatibility</span>

**csanders** <span style="color: grey; font-size: 90%;">21:36:41 UTC</span>

<span style="font-size: 90%;">its 99% sockets</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:45 UTC</span>

<span style="font-size: 90%;">Maybe it has some use in Fastly, or others</span>

**csanders** <span style="color: grey; font-size: 90%;">21:36:46 UTC</span>

<span style="font-size: 90%;">not much has changed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:36:49 UTC</span>

<span style="font-size: 90%;">Don't really know</span>

**csanders** <span style="color: grey; font-size: 90%;">21:37:04 UTC</span>

<span style="font-size: 90%;">in python3 they expect byte buffers</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:37:05 UTC</span>

<span style="font-size: 90%;">Other than that, I've already ported it to Go</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:37:25 UTC</span>

<span style="font-size: 90%;">[https://github.com/fzipi/go-ftw](https://github.com/fzipi/go-ftw)</span>

**csanders** <span style="color: grey; font-size: 90%;">21:37:31 UTC</span>

<span style="font-size: 90%;">but I think pretty much anyone should be able to add .encode()/.decode() aas needed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:37:43 UTC</span>

<span style="font-size: 90%;">It was tricky</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:37:49 UTC</span>

<span style="font-size: 90%;">And some things need to change</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:38:03 UTC</span>

<span style="font-size: 90%;">For example, in my go port, we need to do small changes to the test files</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:38:11 UTC</span>

<span style="font-size: 90%;">So it simplifies things</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:38:33 UTC</span>

<span style="font-size: 90%;">I would say it works, but I'm still writing tests</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:38:50 UTC</span>

<span style="font-size: 90%;">The good thing is that is it extremely fast, compared to the python version</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:39:22 UTC</span>

<span style="font-size: 90%;">Anyway</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:39:38 UTC</span>

<span style="font-size: 90%;">I will monitor this next couple of days the pipelines, and act accordingly</span>

**dune73** <span style="color: grey; font-size: 90%;">21:39:43 UTC</span>

<span style="font-size: 90%;">The speed gain would be very welcome.</span>

**walter** <span style="color: grey; font-size: 90%;">21:39:50 UTC</span>

<span style="font-size: 90%;">yes this sounds very awesome</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:39:56 UTC</span>

<span style="font-size: 90%;">Yes, but I don't want to force the project with anything</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:01 UTC</span>

<span style="font-size: 90%;">You mean you run the tests in parallel to our pipeline?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:12 UTC</span>

<span style="font-size: 90%;">I might do that, for testing</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:21 UTC</span>

<span style="font-size: 90%;">Sounds cool.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:28 UTC</span>

<span style="font-size: 90%;">Until we have some confidence on it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:47 UTC</span>

<span style="font-size: 90%;">But, I might have to change the tests</span>

**dune73** <span style="color: grey; font-size: 90%;">21:40:47 UTC</span>

<span style="font-size: 90%;">Can you do the tweaks to the tests on your end, or do we need to change the test files before making the shift?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:40:59 UTC</span>

<span style="font-size: 90%;">That is something I need to review</span>

**dune73** <span style="color: grey; font-size: 90%;">21:41:04 UTC</span>

<span style="font-size: 90%;">I see.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:41:18 UTC</span>

<span style="font-size: 90%;">This is very important work. Thank you very much.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:41:24 UTC</span>

<span style="font-size: 90%;">This is what needs to be patched, [https://gist.github.com/fzipi/b9e22b3834a5fa32970878c72775d41e](https://gist.github.com/fzipi/b9e22b3834a5fa32970878c72775d41e)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:41:47 UTC</span>

<span style="font-size: 90%;">What I did was unify types</span>

**dune73** <span style="color: grey; font-size: 90%;">21:42:15 UTC</span>

<span style="font-size: 90%;">I see.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:42:20 UTC</span>

<span style="font-size: 90%;">Instead of allowing a list of status codes, or an individual, just use always list</span>

**dune73** <span style="color: grey; font-size: 90%;">21:42:27 UTC</span>

<span style="font-size: 90%;">It's easy enough for the status, but more work for the data.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:42:52 UTC</span>

<span style="font-size: 90%;">Well, the data is a list of strings, but there is a proper yaml construct to do that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:43:00 UTC</span>

<span style="font-size: 90%;">Just use | and indent</span>

**walter** <span style="color: grey; font-size: 90%;">21:43:24 UTC</span>

<span style="font-size: 90%;">the new format is definitely more pretty</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:43:31 UTC</span>

<span style="font-size: 90%;">And more yaml compliant</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:01 UTC</span>

<span style="font-size: 90%;">The only "real" change</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:08 UTC</span>

<span style="font-size: 90%;">Is that, as some of you saw</span>

**dune73** <span style="color: grey; font-size: 90%;">21:44:20 UTC</span>

<span style="font-size: 90%;">So I guess we'll hear more from this throughout the month?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:20 UTC</span>

<span style="font-size: 90%;">There was a change in the testing docker we merged</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:27 UTC</span>

<span style="font-size: 90%;">Yes, definitely</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:40 UTC</span>

<span style="font-size: 90%;">We are not using [example.com](http://example.com) as test anymore</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:55 UTC</span>

<span style="font-size: 90%;">And we don't send queries outside our dockers now</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:45:08 UTC</span>

<span style="font-size: 90%;">As we use [httpbin.org](http://httpbin.org) as backend</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:45:44 UTC</span>

<span style="font-size: 90%;">You need to do POST to the /post url if you want a 200 status</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:46:04 UTC</span>

<span style="font-size: 90%;">So that's the only "semantic" change</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:46:27 UTC</span>

<span style="font-size: 90%;">Sorry friends, i have to go! Good night.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:46:34 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:46:49 UTC</span>

<span style="font-size: 90%;">I'm taking the lead on this</span>

**walter** <span style="color: grey; font-size: 90%;">21:47:09 UTC</span>

<span style="font-size: 90%;">awesome!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:47:24 UTC</span>

<span style="font-size: 90%;">Good night _@azurIt_.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:47:36 UTC</span>

<span style="font-size: 90%;">Yes, we need to come to an end here as well.</span>

**walter** <span style="color: grey; font-size: 90%;">21:48:35 UTC</span>

<span style="font-size: 90%;">agreed :yawning_face:</span>

**walter** <span style="color: grey; font-size: 90%;">21:48:41 UTC</span>

<span style="font-size: 90%;">so much development!!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:48:42 UTC</span>

<span style="font-size: 90%;">We scheduled 3.4 for Feb / March but after the last meeting more problems with the early blocking on ModSec3 popped up. So it's like our workaround lead to the discovery of more bugs and we can neither release our workaround this way, nor can we release 3.4 with early blocking since it does not work on MdoSec3.</span>

**walter** <span style="color: grey; font-size: 90%;">21:49:30 UTC</span>

<span style="font-size: 90%;">yeah, it’s a no-no to release something that doesn’t work on modsec3</span>

**walter** <span style="color: grey; font-size: 90%;">21:49:44 UTC</span>

<span style="font-size: 90%;">I think too many people are running that by now</span>

**dune73** <span style="color: grey; font-size: 90%;">21:49:47 UTC</span>

<span style="font-size: 90%;">We have somebody from Nginx investigate the bad behaviour on ModSec3 (TW could not care less) and until he comes back with a report (or we investigate it ourselves), we are blocked.</span>

**walter** <span style="color: grey; font-size: 90%;">21:50:02 UTC</span>

<span style="font-size: 90%;">I think you mentioned to wait on that for a few weeks, right?</span>

**walter** <span style="color: grey; font-size: 90%;">21:50:27 UTC</span>

<span style="font-size: 90%;">what would your opinion be about backing out the early blocking feature if that would allow us to release 3.4? and leave it for a later release?</span>

**airween** <span style="color: grey; font-size: 90%;">21:50:35 UTC</span>

<span style="font-size: 90%;">note: ModSec3 wrong behavior comes only in special cases</span>

**dune73** <span style="color: grey; font-size: 90%;">21:51:33 UTC</span>

<span style="font-size: 90%;">The reason for 3.4 was the early blocking and the workaround that it brings. The planned schedule was to release later in the year. Spring or Summer. Or am I wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:52:14 UTC</span>

<span style="font-size: 90%;">And without early blocking, we leave users that have BodyAccess off on ModSec3 exposed to a complete WAF bypass.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:52:24 UTC</span>

<span style="font-size: 90%;">So I think we need to do something sooner or later.</span>

**walter** <span style="color: grey; font-size: 90%;">21:52:26 UTC</span>

<span style="font-size: 90%;">that is true, buyt there are a lot of new developmenst going on right now. with the plugin architecture, we might as well be justified in calling it CRS 4.0, imo</span>

**dune73** <span style="color: grey; font-size: 90%;">21:52:55 UTC</span>

<span style="font-size: 90%;">Here is the issue in question with the thread that covers this: [https://github.com/SpiderLabs/ModSecurity/issues/2465#issuecomment-763588208](https://github.com/SpiderLabs/ModSecurity/issues/2465#issuecomment-763588208)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:53:27 UTC</span>

<span style="font-size: 90%;">Agreed for a 4.0 with plugins.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:53:37 UTC</span>

<span style="font-size: 90%;">If we release a few plugins along with it.</span>

**airween** <span style="color: grey; font-size: 90%;">21:55:46 UTC</span>

<span style="font-size: 90%;">but _@theMiddle_ and me found a workaround:
[https://github.com/SpiderLabs/ModSecurity/issues/2465#issuecomment-764458019](https://github.com/SpiderLabs/ModSecurity/issues/2465#issuecomment-764458019)</span>

**airween** <span style="color: grey; font-size: 90%;">21:56:21 UTC</span>

<span style="font-size: 90%;">the error_page directive fixes that behavior</span>

**dune73** <span style="color: grey; font-size: 90%;">21:56:43 UTC</span>

<span style="font-size: 90%;">ModSec3 is such a mess!</span>

**airween** <span style="color: grey; font-size: 90%;">21:58:07 UTC</span>

<span style="font-size: 90%;">btw Defan works on it:
[https://github.com/SpiderLabs/ModSecurity-nginx/issues/238#issuecomment-766851671](https://github.com/SpiderLabs/ModSecurity-nginx/issues/238#issuecomment-766851671)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:58:57 UTC</span>

<span style="font-size: 90%;">So either way, we need to wait a few weeks and then make a call, potentially rolling back the early blocking because of ModSec3. And I'd hate to do that.</span>

**walter** <span style="color: grey; font-size: 90%;">21:59:31 UTC</span>

<span style="font-size: 90%;">agreed :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">22:00:33 UTC</span>

<span style="font-size: 90%;">Is there anything else we need to talk about?</span>

**dune73** <span style="color: grey; font-size: 90%;">22:00:43 UTC</span>

<span style="font-size: 90%;">We're done with the agenda, I guess...</span>

**dune73** <span style="color: grey; font-size: 90%;">22:00:50 UTC</span>

<span style="font-size: 90%;">And we covered so many PRs!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:02:17 UTC</span>

<span style="font-size: 90%;">I see we're all quite exhausted. So thank you all for joining and helping talk things through!</span>

**dune73** <span style="color: grey; font-size: 90%;">22:02:22 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**airween** <span style="color: grey; font-size: 90%;">22:02:26 UTC</span>

<span style="font-size: 90%;">gn!</span>

**walter** <span style="color: grey; font-size: 90%;">22:02:27 UTC</span>

<span style="font-size: 90%;">thank you for leading!</span>

**walter** <span style="color: grey; font-size: 90%;">22:02:33 UTC</span>

<span style="font-size: 90%;">good night! :sleeping:</span>

**emphazer** <span style="color: grey; font-size: 90%;">22:02:37 UTC</span>

<span style="font-size: 90%;">good night everybody</span>

**csanders** <span style="color: grey; font-size: 90%;">22:02:42 UTC</span>

<span style="font-size: 90%;">night</span>

**emphazer** <span style="color: grey; font-size: 90%;">22:02:54 UTC</span>

<span style="font-size: 90%;">:sleeping:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">22:03:21 UTC</span>

<span style="font-size: 90%;">Good night!</span>

