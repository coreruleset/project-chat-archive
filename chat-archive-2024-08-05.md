### Mon, Aug 5th, 2024

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:34 UTC</span>

<span style="font-size: 90%;">Welcome to out monthly meeting chat! :wave:</span>

**airween** <span style="color: grey; font-size: 90%;">18:30:49 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**jit** <span style="color: grey; font-size: 90%;">18:31:54 UTC</span>

<span style="font-size: 90%;">Hi</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:54 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:04 UTC</span>

<span style="font-size: 90%;">We have some interesting topics for tonight</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:07 UTC</span>

<span style="font-size: 90%;">Evening.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:08 UTC</span>

<span style="font-size: 90%;">Hello, hello.</span>

**jit** <span style="color: grey; font-size: 90%;">18:33:19 UTC</span>

<span style="font-size: 90%;">Can we do the [#3780](https://github.com/coreruleset/coreruleset/issues/#3780) PR first :slightly_smiling_face:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:34:20 UTC</span>

<span style="font-size: 90%;">We can I guess</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:34:41 UTC</span>

<span style="font-size: 90%;">You could have put that into the issue :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:17 UTC</span>

<span style="font-size: 90%;">Makes sense given _@jit_'s local time.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:34:36 UTC</span>

<span style="font-size: 90%;">Hi</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:59 UTC</span>

<span style="font-size: 90%;">So * feat: added rule to detect Bash Brace Expansion [#3780](https://github.com/coreruleset/coreruleset/issues/#3780): new rule or add to existing rule? → performance overhead vs. rule complexity (and ReDos)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:23 UTC</span>

<span style="font-size: 90%;">Who can explain what is needed?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:48 UTC</span>

<span style="font-size: 90%;">I think we can postpone / skip this discussion.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:25 UTC</span>

<span style="font-size: 90%;">Since I put it on the list, I discovered that we might better put the change into existing infrastructure. I'd like to explore that properly first.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:39 UTC</span>

<span style="font-size: 90%;">Ok, that makes sense then.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:36:47 UTC</span>

<span style="font-size: 90%;">Discuss at the next issues meeting?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:37:26 UTC</span>

<span style="font-size: 90%;">No, I'll put it back on the agenda if it's necessary.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:36:57 UTC</span>

<span style="font-size: 90%;">(It could go straight back on the agenda)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:04 UTC</span>

<span style="font-size: 90%;">In general, I think we need to discuss how we want to proceed in the future with new detections.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:37:32 UTC</span>

<span style="font-size: 90%;">This is the discussion we want to have?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:09 UTC</span>

<span style="font-size: 90%;">So we would integrate this? So the preliminary decision is to use an existing rule?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:26 UTC</span>

<span style="font-size: 90%;">No, I'll put it back on the agenda if it's necessary.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:37:26 UTC</span>

<span style="font-size: 90%;">No, I'll put it back on the agenda if it's necessary.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:33 UTC</span>

<span style="font-size: 90%;">_@maxleske_ you think the case by case decision does not work in the future?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:53 UTC</span>

<span style="font-size: 90%;">I think the case by case decision will work in the future, but we currently try to avoid new rules at all costs. The "cost" comes with complexity, maintenance overhead and an increased potential for ReDos and rule bypasses. That's my opinion.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:39:00 UTC</span>

<span style="font-size: 90%;">Could be a topic for the retreat.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:21 UTC</span>

<span style="font-size: 90%;">That's exactly what I thought</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:24 UTC</span>

<span style="font-size: 90%;">These are strong arguments. I agree, we should consider the priorities.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:33 UTC</span>

<span style="font-size: 90%;">Should I put the topic in the wiki?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:39 UTC</span>

<span style="font-size: 90%;">Ok, then we settle this that Max will follow up for this case, and we discuss the general case at the retreat</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:20 UTC</span>

<span style="font-size: 90%;">Do we have a place where to put topics yet?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:41:39 UTC</span>

<span style="font-size: 90%;">I think we don't have yet</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Empty, but there is a page for the topics</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:42:14 UTC</span>

<span style="font-size: 90%;">Found it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:23 UTC</span>

<span style="font-size: 90%;">OK with you _@jit_?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:43:41 UTC</span>

<span style="font-size: 90%;">I was thinking it'd be an existing rule, but this is bit of a surprise. Anyways, its decided.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">18:44:02 UTC</span>

<span style="font-size: 90%;">Cool</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:39 UTC</span>

<span style="font-size: 90%;">I think we don't have yet</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:41:39 UTC</span>

<span style="font-size: 90%;">I think we don't have yet</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Empty, but there is a page for the topics</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:42:14 UTC</span>

<span style="font-size: 90%;">Found it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:18 UTC</span>

<span style="font-size: 90%;">I guess jit can follow up in the thread</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:47 UTC</span>

<span style="font-size: 90%;">Next topic: LTS release</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:54 UTC</span>

<span style="font-size: 90%;">So, what do we think we need for v4 LTS? Some of the topics that come to mind are: fixing possible redos (this might change rules/ids, etc), we need to finish updating reponse rules updates, quantitative analysis measures, etc.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:18 UTC</span>

<span style="font-size: 90%;">How stable/mature do people think v4 currently is?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:27 UTC</span>

<span style="font-size: 90%;">Given it's been around a little while and a few versions in, now</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:29 UTC</span>

<span style="font-size: 90%;">We need to address the FPs in the Unix RCE rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:49 UTC</span>

<span style="font-size: 90%;">I am confident there are no real showstoppers. Gradual problems like FPs, but I do not think this is necessarily a killer for an LTS. But taking 1-2 months to fix a few priority issues and then LTS would be a smart move.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:24 UTC</span>

<span style="font-size: 90%;">What I am not sure is: I got the feeling around 4.0 that half of the team did not want to do / support and LTS at all and put it all on the users.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:44 UTC</span>

<span style="font-size: 90%;">Was that impression wrong? Or has there been a gradual shift in opinion?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:44 UTC</span>

<span style="font-size: 90%;">There are: we need to do redos analysis</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:20 UTC</span>

<span style="font-size: 90%;">And quantitative analysis</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:34 UTC</span>

<span style="font-size: 90%;">And updating the response rules ofc</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:48 UTC</span>

<span style="font-size: 90%;">We always had ReDoS. If we can solve it, then cool. If not, then that's the cost of doing business. But that's only my personal opinion.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:48:52 UTC</span>

<span style="font-size: 90%;">Are those showstoppers? Those weren't showstoppers for v4.0 or with v3.3.x, or are these new issues that have been recently introduced?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:14 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:23 UTC</span>

<span style="font-size: 90%;">At least for me, there are.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:57 UTC</span>

<span style="font-size: 90%;">We have redos for those who use modsecurity</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:09 UTC</span>

<span style="font-size: 90%;">Or at least, pcre</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:50:41 UTC</span>

<span style="font-size: 90%;">In new v4 rules or is this an "it was always there" problem?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:22 UTC</span>

<span style="font-size: 90%;">I think it is new, but please correct me. We introduced new rules, we didn't tested then for redos probably</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:51:23 UTC</span>

<span style="font-size: 90%;">If it's new rules then yes, that should be fixed, surely</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:25 UTC</span>

<span style="font-size: 90%;">Wait, "redos analysis" != "fix all redos"</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:51:26 UTC</span>

<span style="font-size: 90%;">Ok</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:45 UTC</span>

<span style="font-size: 90%;">Agreed we don't need to fix everything</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:58 UTC</span>

<span style="font-size: 90%;">But doing LTS implies no changes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:04 UTC</span>

<span style="font-size: 90%;">No new anything</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:17 UTC</span>

<span style="font-size: 90%;">Would we use existing methodology, or try and develop additional tooling to discover more ReDoS?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:52:49 UTC</span>

<span style="font-size: 90%;">And probably try to address new ReDos that cropped up with 4.0</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:17 UTC</span>

<span style="font-size: 90%;">So, if we fix a redos by splitting rules</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:49 UTC</span>

<span style="font-size: 90%;">And probably try to address new ReDos that cropped up with 4.0</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:52:49 UTC</span>

<span style="font-size: 90%;">And probably try to address new ReDos that cropped up with 4.0</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:01 UTC</span>

<span style="font-size: 90%;">I have some tooling that might help, but no time to process/finish with the results</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:05 UTC</span>

<span style="font-size: 90%;">LTS simply means that we promise to backport "important" fixes, right?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:17 UTC</span>

<span style="font-size: 90%;">That was my understanding, too</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:22 UTC</span>

<span style="font-size: 90%;">It doesn't prevent us from doing whatever we want in newer releases.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:25 UTC</span>

<span style="font-size: 90%;">Not 100% static</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:56 UTC</span>

<span style="font-size: 90%;">No changes in rules, if I understood correctly lts</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:10 UTC</span>

<span style="font-size: 90%;">I think fixing existing rules would be in line with LTS, but _@fzipitria_ is correct that fixing a ReDoS could mean to split a rule and that's when it gets hairy in terms of LTS.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:13 UTC</span>

<span style="font-size: 90%;">The idea of the "no rule change in LTS" policy was to be a guideline, never a rule to follow by the letter. We broke the rule before anyways. For good reasons.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:15 UTC</span>

<span style="font-size: 90%;">So, we make a list of what we believe are "showstoppers" for a v4 LTS and then we can discuss further?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:20 UTC</span>

<span style="font-size: 90%;">A list always helps</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:29 UTC</span>

<span style="font-size: 90%;">But as we didn't do a full analysis, we might face the need for splitting more than one rule</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:44 UTC</span>

<span style="font-size: 90%;">I would rather define LTS in the case of CRS as no new rule, no rule deletion - but by definition a rule can be modified</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:55 UTC</span>

<span style="font-size: 90%;">That was my idea, create a list</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:12 UTC</span>

<span style="font-size: 90%;">Happy with that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:37 UTC</span>

<span style="font-size: 90%;">I would say creating tickets/issues and and the V4 lts tag would be the best</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:19 UTC</span>

<span style="font-size: 90%;">Excellent</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:30 UTC</span>

<span style="font-size: 90%;">We can add more discussion on each ticket</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:38 UTC</span>

<span style="font-size: 90%;">I think it is worthwhile</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:19 UTC</span>

<span style="font-size: 90%;">Ok, next topic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:46 UTC</span>

<span style="font-size: 90%;">There was a survey internally about what leaders think about a Contributor License Agreement (CLA)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:09 UTC</span>

<span style="font-size: 90%;">Internally to OWASP?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:48 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:08 UTC</span>

<span style="font-size: 90%;">The links are full of legalese… is there a TL;DR summary of the problem/issue/debate?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:22 UTC</span>

<span style="font-size: 90%;">What would this provide that simply publishing under the Apache 2.0 licence does not already provide?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:01 UTC</span>

<span style="font-size: 90%;">The last link, the one from Yahoo, explains it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:20 UTC</span>

<span style="font-size: 90%;">There are two cases, individual, and company</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:41 UTC</span>

<span style="font-size: 90%;">I guess for owasp the more problematic could be about companies</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:30 UTC</span>

<span style="font-size: 90%;">I don't think it is our case, but as it might arise as a broader discussion, we thought about making it more public</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:16 UTC</span>

<span style="font-size: 90%;">Personally, I don't mind about such agreements, as long as it doesn't create additional friction in our flows</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:06:50 UTC</span>

<span style="font-size: 90%;">So every single contributor would first need to sign an agreement, if we implemented this across all of OWASP?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:00 UTC</span>

<span style="font-size: 90%;">No</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:30 UTC</span>

<span style="font-size: 90%;">This is something that was solved for other projects, so no.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:54 UTC</span>

<span style="font-size: 90%;">You just add a checkbox, or say "yes" in a pr</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:08:07 UTC</span>

<span style="font-size: 90%;">Ah</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:19 UTC</span>

<span style="font-size: 90%;">But that is just if we actually do something about that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:42 UTC</span>

<span style="font-size: 90%;">I don't think there was a push for moving in that direction</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:00 UTC</span>

<span style="font-size: 90%;">Just a survey on "what people thinks" about it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:32 UTC</span>

<span style="font-size: 90%;">The idea of bringing it here was to let everyone know first</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:39 UTC</span>

<span style="font-size: 90%;">As I see it, nobody knows what this mean</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:05 UTC</span>

<span style="font-size: 90%;">It's all a bit legalese like _@xanadu_ said and it's not quite clear where this is leading.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:17 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:46 UTC</span>

<span style="font-size: 90%;">Let's move on then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:16 UTC</span>

<span style="font-size: 90%;">941160 reacts to img [#3770](https://github.com/coreruleset/coreruleset/issues/#3770): how much HTML do we want to detect? - _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">19:13:59 UTC</span>

<span style="font-size: 90%;">Uhm, I have no idea. As I remember _@maxleske_ wrote then he can take a review</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:42 UTC</span>

<span style="font-size: 90%;">I guess it could help when we write topics in the agenda, also who wrote it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:16:29 UTC</span>

<span style="font-size: 90%;">You mean who put the issue into the agenda, the he would put the author/responsible?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:24:40 UTC</span>

<span style="font-size: 90%;">That would have been me :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:25:25 UTC</span>

<span style="font-size: 90%;">Okay, but who is responsible to put it into the agenda?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:26:16 UTC</span>

<span style="font-size: 90%;">? I put it into the agenda, so I should have put my name there.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:27:14 UTC</span>

<span style="font-size: 90%;">thanks - I didn't know who put that and who's responsible for that. That wasn't clear.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:56:34 UTC</span>

<span style="font-size: 90%;">I did add the name, thought it was you. Sorry.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:11:30 UTC</span>

<span style="font-size: 90%;">np</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:35 UTC</span>

<span style="font-size: 90%;">Sry, give me a sec</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:37 UTC</span>

<span style="font-size: 90%;">Sure</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:48 UTC</span>

<span style="font-size: 90%;">Yes, I looked at that one.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:03 UTC</span>

<span style="font-size: 90%;">We have an ancient (meaning "before the great Git reckoning") rule that was pretty much copied from the NoScript Chrome extension.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:00 UTC</span>

<span style="font-size: 90%;">The plugged regular expression tries to find some "dangerous" HTML tags and our rule does exactly the same. It doesn't care what the tag contains, just if it's there.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:00 UTC</span>

<span style="font-size: 90%;">So `<img ` would produce a match. Now, this isn't wrong, per se, and we can say that we just want to detect any HTML, which is what the rule comment states anyway.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:37 UTC</span>

<span style="font-size: 90%;">The issue is about the fact that `<img />` is actually valid HTML and also isn't dangerous.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:57 UTC</span>

<span style="font-size: 90%;">Thanks for the explanation.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">So the question becomes, more or less, do we simply want to block _any_ HTML, or do we want to be more specific? The former is easier of course, but also more prone to FPs.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:21:47 UTC</span>

<span style="font-size: 90%;">Does general HTML input still make CRS (v4) go bananas?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:21:50 UTC</span>

<span style="font-size: 90%;">It was suggested in the past that we (CRS) could test which rules struggle with HTML input and then publish a list of rules that require attention, in order to help users who need to submit HTML payloads in ARGS etc.

Would that idea be more helpful? Rather than trying to rework each rule to allow HTML input through.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:48 UTC</span>

<span style="font-size: 90%;">Reading the issue description, guidance might be all that is needed. I don't think we need to be great at detecting valid and dangerous HTML / JS.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:22 UTC</span>

<span style="font-size: 90%;">Ok. I'll respond with that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:25:58 UTC</span>

<span style="font-size: 90%;">Next topic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:34 UTC</span>

<span style="font-size: 90%;">* Linter should check that all rules have the correct CRS tag and version [#3573](https://github.com/coreruleset/coreruleset/issues/#3573) - @airween</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:27 UTC</span>

<span style="font-size: 90%;">yepp</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:47 UTC</span>

<span style="font-size: 90%;">meanwhile _@maxleske_ responded there, so more or less everything is clear</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:57 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3573](https://github.com/coreruleset/coreruleset/issues/3573)</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:43 UTC</span>

<span style="font-size: 90%;">I suggest to introduce a new (mandatory) cli argument: `--version` and user must pass it for each run</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:29:09 UTC</span>

<span style="font-size: 90%;">Sounds good then</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:31 UTC</span>

<span style="font-size: 90%;">in GH workflow I can get that with some magic shell script</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:29:39 UTC</span>

<span style="font-size: 90%;">:blush:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:02 UTC</span>

<span style="font-size: 90%;">Any other topic to cover today?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:59 UTC</span>

<span style="font-size: 90%;">Our friend Davide Ariu is launching a new WAF project.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:10 UTC</span>

<span style="font-size: 90%;">OWASP has asked me to review it before approval.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:22 UTC</span>

<span style="font-size: 90%;">It's a rules management project.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:00 UTC</span>

<span style="font-size: 90%;">I did not really look into it so far, but I think it means to use his research and apply it to rules, probably CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:13 UTC</span>

<span style="font-size: 90%;">My preliminary impression is, this is very good and very welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:01 UTC</span>

<span style="font-size: 90%;">I like it how OWASP now draws more WAF projects. If you want to do open source WAF, then OWASP is the obvious place.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">I'll let you know once I have done the review.</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:23 UTC</span>

<span style="font-size: 90%;">he is the researcher who took a presentation about rise and fall of ModSecurity and CRS?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:13 UTC</span>

<span style="font-size: 90%;">That's the one.</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:56 UTC</span>

<span style="font-size: 90%;">_WAF project_ / _It's a rules management project._ - now I'm confused :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:43 UTC</span>

<span style="font-size: 90%;">Rules management is a subcategory of WAF, is not it?</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:09 UTC</span>

<span style="font-size: 90%;">wait, what stands "rules management"?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:35 UTC</span>

<span style="font-size: 90%;">We'll see when I really read it.</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:11 UTC</span>

<span style="font-size: 90%;">okay</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:21 UTC</span>

<span style="font-size: 90%;">if no other topic, then good night guys</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:25 UTC</span>

<span style="font-size: 90%;">Good night then :smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:37 UTC</span>

<span style="font-size: 90%;">Night</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">Good night everybody</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:14 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**azurit** <span style="color: grey; font-size: 90%;">20:00:50 UTC</span>

<span style="font-size: 90%;">Good night.</span>

