### Mon, Jan 16th, 2023

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:30:23 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:27 UTC</span>

<span style="font-size: 90%;">Hello, hello, time for the CRS chat!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:42 UTC</span>

<span style="font-size: 90%;">Hello _@Paul Beckett_! How is it going and how is the dog?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:31:33 UTC</span>

<span style="font-size: 90%;">Amber (the dog) is still sick. Been referred to get her an ultrasound next week, to see if she's eaten something she shouldn't of that might have gotten stuck</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:31:52 UTC</span>

<span style="font-size: 90%;">hello everybody!!!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:19 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:23 UTC</span>

<span style="font-size: 90%;">hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:30 UTC</span>

<span style="font-size: 90%;">Hey _@emphazer_ and all. Good to see you.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:34 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ Sorry to hear about the dog! Hope she gets better soon.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:46 UTC</span>

<span style="font-size: 90%;">That's a long time sick for a young dog. I agree, it's time for the ultra.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:55 UTC</span>

<span style="font-size: 90%;">Hello</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:00 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:12 UTC</span>

<span style="font-size: 90%;">Hey _@franbuehler_! Is your portrait already online?</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">I don't think so... Have to check, wait...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">No...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:28 UTC</span>

<span style="font-size: 90%;">Hey, hey _@fzipitria_!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:33:33 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">Fortunately she's no longer being sick every day, but really been to get it sorted soon</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:53 UTC</span>

<span style="font-size: 90%;">Wow, even _@Matteo Pace_ is here. Good to see you around.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:42 UTC</span>

<span style="font-size: 90%;">Please find our agenda at [https://github.com/coreruleset/coreruleset/issues/3037](https://github.com/coreruleset/coreruleset/issues/3037)
You need to scroll down to "Separate 2nd meeting".</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:13 UTC</span>

<span style="font-size: 90%;">I think _@maxleske_ is not here yet, so let's start with something easy. Issue [#3079](https://github.com/coreruleset/coreruleset/issues/#3079).</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">I don't think so... Have to check, wait...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">I don't think so... Have to check, wait...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">No...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">No...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">I don't think so... Have to check, wait...</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">No...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:55 UTC</span>

<span style="font-size: 90%;">This is about an edge case with IP collection in CRS 3.x.

Given CRS4 no longer works with collections, this is on the way out.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:19 UTC</span>

<span style="font-size: 90%;">Looking forward to see it published, though. I got a peek preview from Alessandro ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:03 UTC</span>

<span style="font-size: 90%;">But anyways, is this bug in 3079 really a problem that we need to solve and backport, or do we mark it as won't fixed?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:09 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:22 UTC</span>

<span style="font-size: 90%;">I triaged it, and I'd say 'Won't fix'. But it's an interesting case to be aware of.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:30 UTC</span>

<span style="font-size: 90%;">Also: We have another question around IP collection afterwards. I am not entirely sure they are fully independent.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:49 UTC</span>

<span style="font-size: 90%;">Hello _@maxleske_, thanks for joining.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">IMHO, this should be moved to the corresponding plugin, if needed.</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:35 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:42 UTC</span>

<span style="font-size: 90%;">Hello, hello!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:06 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ I don't think there is a plugin.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:15 UTC</span>

<span style="font-size: 90%;">Is anyone writing one? I haven't seen one materialise.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:00 UTC</span>

<span style="font-size: 90%;">The question is if we want  to initialize collections in CRS despite not using them in CRS anymore. Or do we tell to plugins to initialize themselves, or do we provide a collection initialization plugin?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:22 UTC</span>

<span style="font-size: 90%;">What happens if you have two plugins and they both try to initcol the same collection?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:33 UTC</span>

<span style="font-size: 90%;">I haven't played with collections in a while, I don't remember...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:47 UTC</span>

<span style="font-size: 90%;">This very much depends on the entire initialization discussion we had on plugins...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:09 UTC</span>

<span style="font-size: 90%;">That's the disadvantage of having the plugins handle it. If we do it that way, plugins ought to check for prior initialization ...</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:41:57 UTC</span>

<span style="font-size: 90%;">The first one to initcol wins</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:42:03 UTC</span>

<span style="font-size: 90%;">I ran into that with my plugin</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:04 UTC</span>

<span style="font-size: 90%;">If we provide a collection initialization plugin, we need to find a way to make sure it runs before the plugins that need it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:30 UTC</span>

<span style="font-size: 90%;">And - besides - we defined that plugins should try to live independently, this not interfering with one another.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">With that being said, I personally lean somewhat in the direction of CRS doing the initialization, if an optional variable is set (off by default).</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:43:16 UTC</span>

<span style="font-size: 90%;">Off by default is good.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:21 UTC</span>

<span style="font-size: 90%;">That sounds like a good compromise.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:22 UTC</span>

<span style="font-size: 90%;">Absolutely.</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:25 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:54 UTC</span>

<span style="font-size: 90%;">Is 3079 affected by this (I did not think this through in this light)?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:28 UTC</span>

<span style="font-size: 90%;">I think it uses collections, so yes. But no plugin version exists for it, so also no :sweat_smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:34 UTC</span>

<span style="font-size: 90%;">3079 is specifically about a weird situation with a higher executing PL than blocking PL, where a PL 2 rule sets a blocking flag that gets actioned at PL 1…</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:01 UTC</span>

<span style="font-size: 90%;">Unless anyone is keen to fix that, I would suggest we mark as 'Wont Fix' and we flag it in the future if someone writes a plugin for IP reputation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:18 UTC</span>

<span style="font-size: 90%;">A future design consideration, if the plugin ever materialises.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:25 UTC</span>

<span style="font-size: 90%;">I think this is the right course of action. And if we overhaul the scanner detection, I no longer think this matters.
So won't fix here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:51 UTC</span>

<span style="font-size: 90%;">And CRS collection initialization via config item.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:13 UTC</span>

<span style="font-size: 90%;">Could somebody create the issue for that tasks? Milestone CRS4.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:50:16 UTC</span>

<span style="font-size: 90%;">for collection init? or are there two tasks?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:10 UTC</span>

<span style="font-size: 90%;">Bug Bounty and 932150 next, or do we turn to special ideas around ARGS / ARGS_NAMES of the Coraza community?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:46 UTC</span>

<span style="font-size: 90%;">Let's let the discussion in the Coraza thread play out first.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:26 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:29 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:02 UTC</span>

<span style="font-size: 90%;">So Envoy is a bit special in the sense that it forwards HTTP Headers before Coraza gets to execute phase 2 rules.</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:29 UTC</span>

<span style="font-size: 90%;">ugh</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:49 UTC</span>

<span style="font-size: 90%;">Given there are CRS rules inspecting HTTP Headers in phase 2 (due to rules working on ARGS and Headers in the same rule), the headers CRS is inspecting have sometimes hit the backend already.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:30 UTC</span>

<span style="font-size: 90%;">Problems with fast forwarding of headers aside, one problem is that CRS runs the header tests too late.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:36 UTC</span>

<span style="font-size: 90%;">A solution would be to split rules into targets that are available in phase 1 and a twin rule for targets only available in phase 2. This could mean to replace ARGS with ARGS_GET and ARGS_POST and move the ARGS_GET into a phase 1 twin rule.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:56:47 UTC</span>

<span style="font-size: 90%;">This could break some of our rules. Eg 920390

[https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872)</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:17 UTC</span>

<span style="font-size: 90%;">That sounds like a performance and maintenance nightmare</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:32 UTC</span>

<span style="font-size: 90%;">An alternative we discussed would be to keep them in phase 2 and Coraza on Envoy gets a functionality, that more or less ignores the phase action, but runs the rules immediately when variables become available.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:48 UTC</span>

<span style="font-size: 90%;">That saves us from the duplication of rules.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:06 UTC</span>

<span style="font-size: 90%;">Well, hopefully in the future we will be “transpiling’ the ruleset, so this might be automatically generated</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:23 UTC</span>

<span style="font-size: 90%;">(but not applicable for now)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:26 UTC</span>

<span style="font-size: 90%;">Now Coraza could dynamically replace ARGS with it's counterparts. But that would become messier and messier. So if we would simply replace ARGS with ARGS_GET and ARGS_POST (+ ARGS_NAMES of course), then that would maybe not change much for CRS, but would make life for Coraza on Envoy easier.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:14 UTC</span>

<span style="font-size: 90%;">_@xanadu_ was right to do the math and pretty much rule out the copying of rules into multiple phases in mainline CRS, but maybe the latter would not hurt us too much.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:18 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:17 UTC</span>

<span style="font-size: 90%;">Do we expect ARGS and ARGS_GET|ARGS_POST to have identical performance?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:58:23 UTC</span>

<span style="font-size: 90%;">I think everything is documented very well in the GitHub issue and comments should go there.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:28 UTC</span>

<span style="font-size: 90%;">No weird Apache initialisation overhead at play?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:37 UTC</span>

<span style="font-size: 90%;">Would be good to double-check.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:07 UTC</span>

<span style="font-size: 90%;">Really not sure about the performance impact. I would expect a minimal overhead, but what are expectations when it comes to performance ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:49 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Yes of course. But we are here to discuss it together and ideally come to a resolution - or at least a plan how to get to a resolution.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:30 UTC</span>

<span style="font-size: 90%;">It is about the same, IMHO</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:00 UTC</span>

<span style="font-size: 90%;">Is it, indeed, the same</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:15 UTC</span>

<span style="font-size: 90%;">Literally, the same function</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:19 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ and _@Matteo Pace_ Just how important is this really for Coraza and especially for Coraza on Envoy?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:31 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: You are looking the code?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:37 UTC</span>

<span style="font-size: 90%;">Yes</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:02:37 UTC</span>

<span style="font-size: 90%;">I would say definitely important, because we are talking about waf bypasses</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:03:01 UTC</span>

<span style="font-size: 90%;">But, just thinking from the CRS standpoint, wouldn’t be useful trying to make the early blocking feature as effective as possible?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:03:40 UTC</span>

<span style="font-size: 90%;">Then, I see the trade-off with the maintenance nightmare (when it comes to splitting rules into twins)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:03:54 UTC</span>

<span style="font-size: 90%;">❯ diff args.c args_get.c
1c1
<  /* ARGS */
---
>  /* ARGS_GET */
3c3
<  static int var_args_generate(modsec_rec *msr, msre_var *var, msre_rule *rule,
---
>  static int var_args_get_generate(modsec_rec *msr, msre_var *var, msre_rule *rule,
16a17,19
>          /* Only QUERY_STRING arguments */
>          if (strcmp("QUERY_STRING", arg->origin) != 0) continue;
>
36c39
<              rvar->name = apr_psprintf(mptmp, "ARGS:%s", log_escape_nq_ex(mptmp, arg->name, arg->name_len));
---
>              rvar->name = apr_psprintf(mptmp, "ARGS_GET:%s", log_escape_nq_ex(mptmp, arg->name, arg->name_len));</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:04:44 UTC</span>

<span style="font-size: 90%;">Cool to see :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:19 UTC</span>

<span style="font-size: 90%;">I would say both are the same, technically. ¯\\\_(ツ)\_/¯</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:58 UTC</span>

<span style="font-size: 90%;">Wait: there is an envoy variable to prevent forwarding headers.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:05 UTC</span>

<span style="font-size: 90%;">From a CRS standpoint it really does not matter too much. Early Blocking has 2 effects on a standard ModSec setup:
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:08 UTC</span>

<span style="font-size: 90%;">So this is about speed, not security.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:16 UTC</span>

<span style="font-size: 90%;">Ah.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:23 UTC</span>

<span style="font-size: 90%;">You found the variable?</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:24 UTC</span>

<span style="font-size: 90%;">That changes everything, IMHO</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:35 UTC</span>

<span style="font-size: 90%;">Yes, let me get it</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;">Putting a WAF in the path = expect latency.</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:47 UTC</span>

<span style="font-size: 90%;">If Envoy can just prevent this problem by setting a variable, and it saves us possibly weeks of work…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:35 UTC</span>

<span style="font-size: 90%;">When following the Coraza discussion I think the point was that they do not want to stop this problem. It's an envoy feature, but a bug.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:28 UTC</span>

<span style="font-size: 90%;">_@walter_ We do separate ARGS into ARGS_GET and ARGS_POST, then I do not think it's week of work. But our rules get slightly more complicated. I think it would be acceptable if nobody sees any downsides.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:07:58 UTC</span>

<span style="font-size: 90%;">I still think the engine can and should take care of that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:00 UTC</span>

<span style="font-size: 90%;">If we duplicate the rules of course, then a ton of work, and duplication / separation of tests and what not. I do not see us doing that.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:08:44 UTC</span>

<span style="font-size: 90%;">and maintain them later...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:32 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Coraza should split ARGS itself and shift ARGS_GET to phase 1 itself if it absolutely feels like it?</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:44 UTC</span>

<span style="font-size: 90%;">and maintain them later...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:08:44 UTC</span>

<span style="font-size: 90%;">and maintain them later...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:25 UTC</span>

<span style="font-size: 90%;">_@Matteo Pace_ Do you see why more early blocking at such a big cost is not interesting for CRS?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:11:21 UTC</span>

<span style="font-size: 90%;">Yep, I see, thanks. That feature is definitely more useful with Envoy or potentially other proxies apart from Apache/nginx. I tought that skipping phase 2 would still have been a nice cpu/ram save</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:27 UTC</span>

<span style="font-size: 90%;">Yes. Unless I'm missing something, that sounds like the best solution to me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:12 UTC</span>

<span style="font-size: 90%;">I’m trying to find the setting. Don’t remember where I’ve pasted that one</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:13:05 UTC</span>

<span style="font-size: 90%;">To the best of my knowledge, Envoy side there is an (old) discussione about it, the main point is to enable buffering the header and controlling that lifecycle from the Wasm</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:33 UTC</span>

<span style="font-size: 90%;">But you do not see much negative impact from splitting in CRS? Or is there a serious downside to it?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:38 UTC</span>

<span style="font-size: 90%;">What do we want to do with some special rules, eg 920390, where we check the length or (summarized) arguments?

[https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:13:33 UTC</span>

<span style="font-size: 90%;">Good point! You should add that to the GitHub issue</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:07 UTC</span>

<span style="font-size: 90%;">Can’t Coraza do the same when parsing the rules?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:11:21 UTC</span>

<span style="font-size: 90%;">Yep, I see, thanks. That feature is definitely more useful with Envoy or potentially other proxies apart from Apache/nginx. I tought that skipping phase 2 would still have been a nice cpu/ram save</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:11:21 UTC</span>

<span style="font-size: 90%;">Yep, I see, thanks. That feature is definitely more useful with Envoy or potentially other proxies apart from Apache/nginx. I tought that skipping phase 2 would still have been a nice cpu/ram save</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:11:23 UTC</span>

<span style="font-size: 90%;">We wouldn't need to do anything to CRS, that's the point</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:46 UTC</span>

<span style="font-size: 90%;">Coraza and others can add additional stuff on top</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:12:08 UTC</span>

<span style="font-size: 90%;">But one thing we are not doing is just keep phases “independent”</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:38 UTC</span>

<span style="font-size: 90%;">What do we want to do with some special rules, eg 920390, where we check the length or (summarized) arguments?

[https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:38 UTC</span>

<span style="font-size: 90%;">What do we want to do with some special rules, eg 920390, where we check the length or (summarized) arguments?

[https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:13:33 UTC</span>

<span style="font-size: 90%;">Good point! You should add that to the GitHub issue</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:04 UTC</span>

<span style="font-size: 90%;">_@Matteo Pace_ Unfortunately not. >95% of the requests are benign and they will have to run through all rules in all the phases and all we do is responding faster to attackers.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:33 UTC</span>

<span style="font-size: 90%;">Good point! You should add that to the GitHub issue</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:38 UTC</span>

<span style="font-size: 90%;">What do we want to do with some special rules, eg 920390, where we check the length or (summarized) arguments?

[https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872](https://github.com/coreruleset/coreruleset/blob/v4.0/dev/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L853-L872)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:13:33 UTC</span>

<span style="font-size: 90%;">Good point! You should add that to the GitHub issue</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:36 UTC</span>

<span style="font-size: 90%;">Thanks _@airween_. That tilts the balance in direction of we do not want to do anything. It's getting hairy and I personally think the whole early forwarding is very hairy in reality (especially for the backend application that expects a body and it's being blocked after it read the headers...)</span>

**airween** <span style="color: grey; font-size: 90%;">20:16:26 UTC</span>

<span style="font-size: 90%;">it's not the advertisement, but you should check the CRSDOC page:

[https://crsdoc.digitalwave.hu/?v=v4.0-dev](https://crsdoc.digitalwave.hu/?v=v4.0-dev)

click on the targets, and you can see a good summary of used targets. (I've updated the rules db an hour ago)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:52 UTC</span>

<span style="font-size: 90%;">Anybody still in favor of taking action here?</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:13 UTC</span>

<span style="font-size: 90%;">for eg. we can see there are 174 rules where we use ARGS:
[https://crsdoc.digitalwave.hu/?v=v4.0-dev&f=1&_trg=35](https://crsdoc.digitalwave.hu/?v=v4.0-dev&f=1&_trg=35)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:41 UTC</span>

<span style="font-size: 90%;">That's about the count that _@xanadu_ did. Definitely not smart to create twin rules (for standard ModSec).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:43 UTC</span>

<span style="font-size: 90%;">Anyway, thank you for a fruitful discussion. I think this is settled.
Is somebody adding our reasoning to the Coraza issue in question?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:45 UTC</span>

<span style="font-size: 90%;">I'm a bit fuzzy on the details, to be honest, so I don't think this should be me.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:23:34 UTC</span>

<span style="font-size: 90%;">Thanks for the discussion, would have been cool to find a way to keep each phase as much as possible independent. I think it would make easier to adopt the CRS outside apache/nginx, but I somehow see that it is not painless CRS side</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:45 UTC</span>

<span style="font-size: 90%;">Thanks for your understanding. _@fzipitria_ mentioned during the discussion that future version of CRS may generate the ruleset. If we implement that, it will be easy to do a Coraza/Envoy ruleset that separates stuff completely without affecting other installations.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:24:51 UTC</span>

<span style="font-size: 90%;">I will dive better on the details learning from your summary :sweat_smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:25:39 UTC</span>

<span style="font-size: 90%;">Exactly. We generate CRS for Apache or for Envoy. And with that is easier to maintain.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:26:18 UTC</span>

<span style="font-size: 90%;">In the meanwhile we will do the best just relying on what we can do Engine side</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:26:46 UTC</span>

<span style="font-size: 90%;">I am happy to reply to both of those open GitHub threads with a summary of the discussion this evening, i.e. the point of view of the CRS team.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:27:07 UTC</span>

<span style="font-size: 90%;">(Unless someone else wants to, I'll do it.)</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:28:20 UTC</span>

<span style="font-size: 90%;">(Oh, I just caught up with the main chat, _@dune73_ is happy to summarise :sweat_smile:)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:03 UTC</span>

<span style="font-size: 90%;">So let's see how the BB come along. _@franbuehler_ and _@maxleske_ you picked up the work on the refactoring of 932150 and friends. For those not familiar with the problem: We think this very rule is responsible for most of the remaining open BB findings and _@maxleske_ volunteered to implement a new version.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:45 UTC</span>

<span style="font-size: 90%;">I'm a bit fuzzy on the details, to be honest, so I don't think this should be me.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:21:45 UTC</span>

<span style="font-size: 90%;">I'm a bit fuzzy on the details, to be honest, so I don't think this should be me.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:23:34 UTC</span>

<span style="font-size: 90%;">Thanks for the discussion, would have been cool to find a way to keep each phase as much as possible independent. I think it would make easier to adopt the CRS outside apache/nginx, but I somehow see that it is not painless CRS side</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:24:45 UTC</span>

<span style="font-size: 90%;">Thanks for your understanding. _@fzipitria_ mentioned during the discussion that future version of CRS may generate the ruleset. If we implement that, it will be easy to do a Coraza/Envoy ruleset that separates stuff completely without affecting other installations.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:24:51 UTC</span>

<span style="font-size: 90%;">I will dive better on the details learning from your summary :sweat_smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:25:39 UTC</span>

<span style="font-size: 90%;">Exactly. We generate CRS for Apache or for Envoy. And with that is easier to maintain.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:26:18 UTC</span>

<span style="font-size: 90%;">In the meanwhile we will do the best just relying on what we can do Engine side</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:26:46 UTC</span>

<span style="font-size: 90%;">I am happy to reply to both of those open GitHub threads with a summary of the discussion this evening, i.e. the point of view of the CRS team.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:27:07 UTC</span>

<span style="font-size: 90%;">(Unless someone else wants to, I'll do it.)</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:28:20 UTC</span>

<span style="font-size: 90%;">(Oh, I just caught up with the main chat, _@dune73_ is happy to summarise :sweat_smile:)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:53 UTC</span>

<span style="font-size: 90%;">A PR by _@franbuehler_ was standing in the way, but that is now resolved (for the time being) and Max told me the toolchain needed to get a new feature.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:22 UTC</span>

<span style="font-size: 90%;">If _@fzipitria_ and _@Matteo Pace_ do not have the time, I'd be happy to summarize.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:38 UTC</span>

<span style="font-size: 90%;">There was also some wishful thinking from my side around 932150 in the previous meeting. But I am not losing hope ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:23:44 UTC</span>

<span style="font-size: 90%;">I'm moving the cmdline patterns out of the toolchain and into a configuration file in CRS. Those should not be in the toolchain and are part of the current issue (rules are getting too long).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:45 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ is working on adding twin rules at PL2 that check User-Agent and Referer headers.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:07 UTC</span>

<span style="font-size: 90%;">So the new config file would then be used via pmFromFile and you combine that with evasion techniques?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:49 UTC</span>

<span style="font-size: 90%;">No, probably not. It will be configuration file for the toolchain.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">Now it makes more sense</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:15 UTC</span>

<span style="font-size: 90%;">The outcome will be pretty much the same though</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:40 UTC</span>

<span style="font-size: 90%;">Got you. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:13 UTC</span>

<span style="font-size: 90%;">I thought I had understood that before. So it's a config file to be used during rule generation and it will still help with rule size.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:44 UTC</span>

<span style="font-size: 90%;">Not with rule size per se, but when we need to change the patterns we don't need to update the toolchain</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:50 UTC</span>

<span style="font-size: 90%;">And it will be more visible</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:26 UTC</span>

<span style="font-size: 90%;">Cool. And the rule size is dealt with by separating the small command (Sorry if I mix things up ... )?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:21 UTC</span>

<span style="font-size: 90%;">Rule size is handled by the change to 932150. Same as 932100 and friends</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:47 UTC</span>

<span style="font-size: 90%;">one generalized rule + one special rule for short words</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:04 UTC</span>

<span style="font-size: 90%;">Cool. Glad my memory is not failing me entirely.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:17 UTC</span>

<span style="font-size: 90%;">So this is on good tracks, but it just takes time, I guess?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:50 UTC</span>

<span style="font-size: 90%;">Yes. And I'm not quite as involved at the moment as I was before christmas.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:41 UTC</span>

<span style="font-size: 90%;">You told us it would be two days all in all. Is this still the estimate and is there work you can offload?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:48 UTC</span>

<span style="font-size: 90%;">The problem is we're kind of waiting for this break-through and the project is somewhat stalled over it. Not necessarily because it's such a complicated PR or rule, but because we stand in front of the remaining BB issues like the mouse in front of the snake.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:53 UTC</span>

<span style="font-size: 90%;">Shouldn't be much more, I think. I've only spent a few hours on it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:36:34 UTC</span>

<span style="font-size: 90%;">I know. I think _@franbuehler_'s help is already most of what makes sense to offload</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:28 UTC</span>

<span style="font-size: 90%;">And do you have time for the rest?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:54 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:26 UTC</span>

<span style="font-size: 90%;">Good, then let's see how this goes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:26 UTC</span>

<span style="font-size: 90%;">Remaining points on the agenda: Community Summit in Dublin Feb 14 and our plans for Coraza on NGINX.</span>

↳ **José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:05:58 UTC</span>

<span style="font-size: 90%;">Is there any active issue tracking this?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:02 UTC</span>

<span style="font-size: 90%;">_@airween_ already volunteered to present his new CRS - how do you call it - cockpit? Dashboard?</span>

**airween** <span style="color: grey; font-size: 90%;">20:41:18 UTC</span>

<span style="font-size: 90%;">uhm... I do not know yet :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:25 UTC</span>

<span style="font-size: 90%;">Not much infos from sponsors so far, I hope to see some of them though.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:48 UTC</span>

<span style="font-size: 90%;">And then a few people from the community stating they look fwd to attend.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:43 UTC</span>

<span style="font-size: 90%;">I guess things will change when we open the registration formally. I plan to do this via eventbrite or rather pretix this time. For free, but proper registration.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:19 UTC</span>

<span style="font-size: 90%;">As you have seen, we have finished our accounts for 2022. I think it's safe for the project to pay all travel expenses.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:31 UTC</span>

<span style="font-size: 90%;">And then we should look into conference attendance.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:48 UTC</span>

<span style="font-size: 90%;">I will certainly stay for the conference and hope some of you will stay too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:14 UTC</span>

<span style="font-size: 90%;">Yeah, I’m presenting there with Juan Pablo… so I guess I’ll need to be there :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:24 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ and _@walter_ we did not talk about conference tickets, but is this something the project could / should pay to those devs who would want to attend? Or at least partially?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:16 UTC</span>

<span style="font-size: 90%;">If we know the numbers of devs attending (and staying) we could rent an AirBnB together, which would be substantially cheaper than a dozen of hotel rooms.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:46 UTC</span>

<span style="font-size: 90%;">Conference tickets are rather $$$</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:11 UTC</span>

<span style="font-size: 90%;">I’m afraid I won’t be able to make it. :cry: My health is still bad, I can only work a little bit every day and there are some projects at work with deadlines that only I can do, plus family matters that take up all my energy until at least the start of March.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:46:13 UTC</span>

<span style="font-size: 90%;">Or those are the trainings?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:24 UTC</span>

<span style="font-size: 90%;">Yes, they are. But it's a worthwhile investment for the project I think and it also supports OWASP.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:47:03 UTC</span>

<span style="font-size: 90%;">Ok, sounds good</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:47:45 UTC</span>

<span style="font-size: 90%;">Conference tickets are €525.00+€5.95 Fee (OWASP members)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:48:01 UTC</span>

<span style="font-size: 90%;">Count me in for the airbnb</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:02 UTC</span>

<span style="font-size: 90%;">[https://www.eventbrite.com/e/owasp-global-appsec-dublin-2023-tickets-428685398567](https://www.eventbrite.com/e/owasp-global-appsec-dublin-2023-tickets-428685398567)
We're talking 600 EUR with 1 year OWASP complementary membership. Leaders only 100 EUR though. hehe.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:16 UTC</span>

<span style="font-size: 90%;">So who plans to attend?
And I suggest _@fzipitria_ and _@walter_ and I sort out the conf tickets among ourselves and let you know what we will do.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:16 UTC</span>

<span style="font-size: 90%;">If you have not attended a bit OWASP conference: They are really quite nice, some 500 people or so, very wide range of talks, decent quality and a lot of good networking, also with other OWASP projects.</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:15 UTC</span>

<span style="font-size: 90%;">Agreed. Lots of nice talks and gives good inspiration.</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:15 UTC</span>

<span style="font-size: 90%;">Looks like I'm going to Dublin but only to meet with you guys (14th of February). I'm going to go with the family for a trip.</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:33 UTC</span>

<span style="font-size: 90%;">(So I won't attend on the conference)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:53:05 UTC</span>

<span style="font-size: 90%;">I'm not sure yet, probably not...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:58 UTC</span>

<span style="font-size: 90%;">OWASP just confirmed we have a room for the day at the Dublin Convention Center.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:54:25 UTC</span>

<span style="font-size: 90%;">I'm 50/50. I was thinking of just going for the CRS meetup day with my integrator hat on. I could probably stay for the conference, but my employer wouldn't have paid for it :laughing:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:54:48 UTC</span>

<span style="font-size: 90%;">Also Southampton has a direct flight to Dublin, so it's very easy to get there.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:54 UTC</span>

<span style="font-size: 90%;">But if we pay, you stay?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:55:16 UTC</span>

<span style="font-size: 90%;">I would, but I certainly wasn't expecting CRS to suggest CRS would pay for it! :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:24 UTC</span>

<span style="font-size: 90%;">_@maxleske_ do you have plans to attend? _@Paul Beckett_, _@emphazer_ ?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:55:33 UTC</span>

<span style="font-size: 90%;">Nope</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:03 UTC</span>

<span style="font-size: 90%;">Also _@Matteo Pace_: You are young, you need to get to conferences to get input!</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:59:40 UTC</span>

<span style="font-size: 90%;">As of today, no plans so far :white_frowning_face:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:56:13 UTC</span>

<span style="font-size: 90%;">Not sure. Clashes with school holidays, and travel from Norwich isn't that easy</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:56:30 UTC</span>

<span style="font-size: 90%;">not yet</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:01 UTC</span>

<span style="font-size: 90%;">Tell me all about it, but at least there are direct flights from Zurich.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:58:20 UTC</span>

<span style="font-size: 90%;">No direct flights from Norwich :(</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:04 UTC</span>

<span style="font-size: 90%;">Well anyways, let's not prolong the meeting too much.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:04 UTC</span>

<span style="font-size: 90%;">In Varese we agreed, that we would like to support Coraza by helping to stabilize the NGINX port in 2023. They year has started, so I think it's time to come up with a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:58 UTC</span>

<span style="font-size: 90%;">There is a strong suspicion there are memory leaks hidden in the code and it probably takes more than test-driving this to identify and solve them.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:01:33 UTC</span>

<span style="font-size: 90%;">Good night everyone. I have to go :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:36 UTC</span>

<span style="font-size: 90%;">Also, we came to the conclusion that we can provide the systematic approach, while Coraza is probably focused on other topics.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:03:14 UTC</span>

<span style="font-size: 90%;">Do we have a volunteer?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:08 UTC</span>

<span style="font-size: 90%;">A volunteer could help. Or we agree it's something we want to make an investment into without necessarily eating too much of our own resources, so we could finance a developer for some limited amount of time.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:57 UTC</span>

<span style="font-size: 90%;">Or a mixed approach with a dedicated C / GoLang developer and a group of volunteers to run the code in production for a few months and report their bugs.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:23 UTC</span>

<span style="font-size: 90%;">I do not know, this is more an initial discussion and we need to start somewhere...</span>

**airween** <span style="color: grey; font-size: 90%;">21:06:15 UTC</span>

<span style="font-size: 90%;">There is the tool [ftwrunner](https://github.com/digitalwave/ftwrunner/tree/v1.0/dev), which supports Coraza too, but I think Coraza's logger is still not complete...</span>

**airween** <span style="color: grey; font-size: 90%;">21:06:34 UTC</span>

<span style="font-size: 90%;">this is why I still can't release the new version</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:07:14 UTC</span>

<span style="font-size: 90%;">I guess ftwrunner relays on libcoraza?</span>

**airween** <span style="color: grey; font-size: 90%;">21:07:27 UTC</span>

<span style="font-size: 90%;">yes</span>

↳ **José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:08:58 UTC</span>

<span style="font-size: 90%;">So current situation for libcoraza is that it does not have an owner and it is more like a pet project.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:09:20 UTC</span>

<span style="font-size: 90%;">oh, I see</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:09:51 UTC</span>

<span style="font-size: 90%;">I can help you - but I'm not a Go programmer :slightly_smiling_face:, rather a C coder</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:46 UTC</span>

<span style="font-size: 90%;">Hello _@José Carlos Chávez_!
_@airween_ you told me you would basically be interested, but you would need to check resources with your boss? Still the case?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:08:27 UTC</span>

<span style="font-size: 90%;">I assume yes, it is</span>

**airween** <span style="color: grey; font-size: 90%;">21:08:27 UTC</span>

<span style="font-size: 90%;">I assume yes, it is</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:08:27 UTC</span>

<span style="font-size: 90%;">I assume yes, it is</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:08:58 UTC</span>

<span style="font-size: 90%;">So current situation for libcoraza is that it does not have an owner and it is more like a pet project.</span>

↳ **José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:08:58 UTC</span>

<span style="font-size: 90%;">So current situation for libcoraza is that it does not have an owner and it is more like a pet project.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:09:20 UTC</span>

<span style="font-size: 90%;">oh, I see</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:09:51 UTC</span>

<span style="font-size: 90%;">I can help you - but I'm not a Go programmer :slightly_smiling_face:, rather a C coder</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:13 UTC</span>

<span style="font-size: 90%;">libcoraza is the NGINX port of Coraza, correct?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:09:38 UTC</span>

<span style="font-size: 90%;">No.</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:09:54 UTC</span>

<span style="font-size: 90%;">libcoraza is the drop in replacement for libmodsecurity</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:09:58 UTC</span>

<span style="font-size: 90%;">Is more like the connection to C from coraza</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:19 UTC</span>

<span style="font-size: 90%;">It is not a 100% drop in replacement</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:33 UTC</span>

<span style="font-size: 90%;">But you have everything you need.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:10:59 UTC</span>

<span style="font-size: 90%;">The problem is that we depend on something that is still not implemented in coraza</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:11:32 UTC</span>

<span style="font-size: 90%;">ah, yes, this is what JuanPablo told me...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:20 UTC</span>

<span style="font-size: 90%;">Oh, I see. That's news. Something big?</span>

**airween** <span style="color: grey; font-size: 90%;">21:11:32 UTC</span>

<span style="font-size: 90%;">ah, yes, this is what JuanPablo told me...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">21:11:32 UTC</span>

<span style="font-size: 90%;">ah, yes, this is what JuanPablo told me...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:05 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/500](https://github.com/corazawaf/coraza/issues/500)</span>

↳ **José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:14:38 UTC</span>

<span style="font-size: 90%;">Interesting turn out. We definitively need an issue in libcoraza linking to this.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:56 UTC</span>

<span style="font-size: 90%;">Hmm. But that is not needed if you run everything in server context?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:57 UTC</span>

<span style="font-size: 90%;">Without that, we can't do anything</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:36 UTC</span>

<span style="font-size: 90%;">(Because I thought JP told us, it can be used as is with some beta quality.)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:10 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:14:48 UTC</span>

<span style="font-size: 90%;">I see.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:27 UTC</span>

<span style="font-size: 90%;">Anyways, this thing needs some love and if we are not getting serious about it, there is a chance it starves a lonely death.</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:15:53 UTC</span>

<span style="font-size: 90%;">Yup.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:07 UTC</span>

<span style="font-size: 90%;">Does anybody see a solution where we find a dedicated sponsor company for this work? Or somebody in the NGINX community perhaps?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:47 UTC</span>

<span style="font-size: 90%;">That could obviously save us a lot of resources and depending on the approach also money. But it would also mean a lot of talking with potential partners (looking at my schedule ... :))</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:17:58 UTC</span>

<span style="font-size: 90%;">One thing I noticed, specially in coraza connectors is that if there is no user around it, it is unlikely to get production ready state. E.g. proxy-wasm has Tetrate as main user and that is why we have E2E smoke tests, FTW tests, load tests and etc. Whereas others like coraza-spoa, coraza-caddy or libcoraza depends on spare time from coraza contributors to progress to a PoC point but given the nature of the library and its position in the critical path, production readiness is unlikely to happen.</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:18:23 UTC</span>

<span style="font-size: 90%;">So if CRS wants to take libcoraza seriously it would be a huge win for all of us.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:31 UTC</span>

<span style="font-size: 90%;">That was exactly our discussion in Varese. And given ModSec EOL, it's something we have a genuine interest in doing. But we need to have the right approach.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:14 UTC</span>

<span style="font-size: 90%;">If anybody has a good idea during the week or so, please share. Maybe somebody is waiting for us to contact them with a proposal.</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:21:16 UTC</span>

<span style="font-size: 90%;">Let me create an issue for “Looking for a maintainer” in libcoraza so you guys can chime in?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:38 UTC</span>

<span style="font-size: 90%;">Sure, it's a start.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:24:27 UTC</span>

<span style="font-size: 90%;">Good, so let's call it a night then. Thank you all for participation and we'll keep you posted about the summit (travel expenses) and Coraza plans.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:24:41 UTC</span>

<span style="font-size: 90%;">Thanks, bb</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:24:46 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:12 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**walter** <span style="color: grey; font-size: 90%;">21:25:14 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**José Carlos Chávez** <span style="color: grey; font-size: 90%;">21:25:17 UTC</span>

<span style="font-size: 90%;">nn</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:25:53 UTC</span>

<span style="font-size: 90%;">Good night</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:25:56 UTC</span>

<span style="font-size: 90%;">good night!</span>

**airween** <span style="color: grey; font-size: 90%;">21:27:30 UTC</span>

<span style="font-size: 90%;">good night!</span>

