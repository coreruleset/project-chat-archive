### Mon, Jun 19th, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:31:20 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's CRS meeting time. Welcome to the chat.</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:33 UTC</span>

<span style="font-size: 90%;">hi there</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:33 UTC</span>

<span style="font-size: 90%;">Please find our agenda here: [https://github.com/coreruleset/coreruleset/issues/3221](https://github.com/coreruleset/coreruleset/issues/3221)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:42 UTC</span>

<span style="font-size: 90%;">Evening</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:45 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:54 UTC</span>

<span style="font-size: 90%;">Hey, hey. Good to see you guys!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:33:02 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:12 UTC</span>

<span style="font-size: 90%;">Hello _@Matteo Pace_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:19 UTC</span>

<span style="font-size: 90%;">It seems it's a nice Summer evening and there are alternatives to a CRS chat. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:47 UTC</span>

<span style="font-size: 90%;">_@Juan Pablo Tosso_ mentioned he would be around, though. And I think it would be good if _@fzipitria_ could join us too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:33 UTC</span>

<span style="font-size: 90%;">Do we want to get going?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:49 UTC</span>

<span style="font-size: 90%;">First item would be the group of PHP function list rules.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:01 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:03 UTC</span>

<span style="font-size: 90%;">JP made an initial PR at [https://github.com/coreruleset/coreruleset/pull/3228](https://github.com/coreruleset/coreruleset/pull/3228)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:52 UTC</span>

<span style="font-size: 90%;">There are other issues for the remainder of the 93315x and 93316x rule group. _@Matteo Pace_ selfassigned one, I volunteered for two other ones.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:21 UTC</span>

<span style="font-size: 90%;">Apparently it's all interconnected. Maybe you have seen my graph at [https://github.com/coreruleset/coreruleset/pull/3228#issuecomment-1594813466](https://github.com/coreruleset/coreruleset/pull/3228#issuecomment-1594813466)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:59 UTC</span>

<span style="font-size: 90%;">The point is, there is new mechanism and what used to be a manual decision are now 2 scriptable decisions.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:39:03 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:10 UTC</span>

<span style="font-size: 90%;">Before we would gauge whether something was dangerous, now I propose to work with a minimal and manual list of dangerous function names (that also are English words) and we pick up JP's idea to use the frequency of use based on GH numbers.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:39:28 UTC</span>

<span style="font-size: 90%;">It looks like a clever solution. Kudos to everyone involved :clap:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:31 UTC</span>

<span style="font-size: 90%;">When you look at the graph, I think the decision on the left can actually be skipped.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:09 UTC</span>

<span style="font-size: 90%;">The manual list would go directly into 933160. The rest remains the same, 933161 would thus indeed be "yes+no" (this was a question).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:33 UTC</span>

<span style="font-size: 90%;">Thank you _@xanadu_, glad you like it. What do you all think? Is this a way to get this implemented?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:23 UTC</span>

<span style="font-size: 90%;">One thing that just occurred to me: the frequency on GitHub may change, so that words may not only be added but also be removed. It's probably not an issue, just wanted to bring it up.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:50 UTC</span>

<span style="font-size: 90%;">I think it’s an interesting approach!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:50 UTC</span>

<span style="font-size: 90%;">Ah, good thinking. That did not occur to me. I think so far JP proposes to pick up functions that are features in 100+ projects. I reckon GH is ever expanding, but we might have to tune that criteria somewhat on the long run.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:32 UTC</span>

<span style="font-size: 90%;">You did the original rules _@walter_. Would you be comfortable with this replacement?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:25 UTC</span>

<span style="font-size: 90%;">It's apparently still not 100% automated, but I see very few changes to 933160. The rest would be nice and automatic. But we also lose the flexibility of the manual classification we did before.</span>

**jit** <span style="color: grey; font-size: 90%;">18:44:29 UTC</span>

<span style="font-size: 90%;">Hi guys. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:33 UTC</span>

<span style="font-size: 90%;">Hey _@jit_, nice to see you around.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:49 UTC</span>

<span style="font-size: 90%;">We're talking about PR 3228.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:24 UTC</span>

<span style="font-size: 90%;">Hey</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:42 UTC</span>

<span style="font-size: 90%;">I think this replacement could be good, especially if we keep the high risk list :+1:</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:20 UTC</span>

<span style="font-size: 90%;">In the comments I see a few mentions of print_replacement or medieval but these should be tackled by word boundaries.</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:35 UTC</span>

<span style="font-size: 90%;">And we will still be matching for ( after the word right?</span>

**JC** <span style="color: grey; font-size: 90%;">18:46:38 UTC</span>

<span style="font-size: 90%;">Aloha</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:15 UTC</span>

<span style="font-size: 90%;">Then I think the FP possibility is probably addressed well.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:29 UTC</span>

<span style="font-size: 90%;">I guess that would be the case. We're flexible how to use them and FP would be kept in check one way or the other.</span>

**jit** <span style="color: grey; font-size: 90%;">18:47:40 UTC</span>

<span style="font-size: 90%;">I already submitted a PR updating PHP fn to latest version. It was merged a few weeks ago.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:45 UTC</span>

<span style="font-size: 90%;">One other thing: the scripting relies heavily on the new spell script that _@theMiddle_ wrote. Unfortunately, spell is fairly old, inflexible and not readily available on all systems (e.g. mine). I'd like to have a script that works for all of us.</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:09 UTC</span>

<span style="font-size: 90%;">Although I think we should review the output of the script manually before merging.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:31 UTC</span>

<span style="font-size: 90%;">At least for the first few iterations. And add plenty of tests. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:50 UTC</span>

<span style="font-size: 90%;">_@maxleske_ You updated the script lately. What part of it is missing for you?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:07 UTC</span>

<span style="font-size: 90%;">You do not have the package on Mac or what is the problem exactly?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:17 UTC</span>

<span style="font-size: 90%;">_@jit_, which one was that?</span>

**jit** <span style="color: grey; font-size: 90%;">18:49:50 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3213](https://github.com/coreruleset/coreruleset/pull/3213)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:22 UTC</span>

<span style="font-size: 90%;">Yes, I don't have the package for Mac (there's probably a way but it's not "easy" :tm: ). Secondly, there are multiple (more modern) alternatives to the original spell that address some shortcomings.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:57 UTC</span>

<span style="font-size: 90%;">How much of a roadblock is this for CRSv4?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:40 UTC</span>

<span style="font-size: 90%;">It's not a major issue but if we exchange spell for something else the list will probably change a bit.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:55 UTC</span>

<span style="font-size: 90%;">the list of english words that is</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:00 UTC</span>

<span style="font-size: 90%;">_@jit_, AFAICT the new way of addressing the creation of these rules would cover your additions as well - plus all the future stuff.</span>

**jit** <span style="color: grey; font-size: 90%;">18:52:21 UTC</span>

<span style="font-size: 90%;">I think 3228 is a great addition.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:11 UTC</span>

<span style="font-size: 90%;">PHP function names would move from 933161 to 933150 / 933151 when changing the spell implementation / the dictionary. Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:59 UTC</span>

<span style="font-size: 90%;">Precisely</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:23 UTC</span>

<span style="font-size: 90%;">What I personally do not like about PR 3228 is the 3 scripts in use. They are - sorry for being so blunt - cobbled together with little sense of style / usability. Bash and Python used, without clear criteria why. I think they need to be updated / replaced and also renamed.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:28 UTC</span>

<span style="font-size: 90%;">I could probably update the script within one or two hours. Unless _@theMiddle_ or someone else has a particular reason for sticking to spell.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:49 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ you also used it lately, did not you?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:58 UTC</span>

<span style="font-size: 90%;">These things will have to be moved into the toolchain, but for now I think the scripts are fine</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:20 UTC</span>

<span style="font-size: 90%;">I agree, we can go with a selection of scripts for 4.0 and then we consolidate into the toolchain for 4.1.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:51 UTC</span>

<span style="font-size: 90%;">_@maxleske_ what would you update around our spell script exactly?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">I used spell.sh, yes. But just used it. We don't have to use spell, in my opinion.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:48 UTC</span>

<span style="font-size: 90%;">I would replace spell with an equivalent, more modern utility (e.g. aspell or ispell)</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:13 UTC</span>

<span style="font-size: 90%;">Huh, I have aspell installed by default. Never knew that.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:26 UTC</span>

<span style="font-size: 90%;">But not spell</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:34 UTC</span>

<span style="font-size: 90%;">They don't have the same interfaces as spell, so you can't interchange them</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:10 UTC</span>

<span style="font-size: 90%;">Ah, we're talking about "these" alternatives. Used aspell for the last 20 years.
Why do we use the naked "spell"?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:29 UTC</span>

<span style="font-size: 90%;">Because spell sucks :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:37 UTC</span>

<span style="font-size: 90%;">And it's not readily available on Mac</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:56 UTC</span>

<span style="font-size: 90%;">Oh, sorry, the opposite: ask _@theMiddle_ :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:17 UTC</span>

<span style="font-size: 90%;">Ok, so it should be replaced by aspell which provides same functionality, but needs script changes?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:43 UTC</span>

<span style="font-size: 90%;">Yes. Let me just create a PR with the change and then you can all judge for youselves.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:55 UTC</span>

<span style="font-size: 90%;">That sounds like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:11 UTC</span>

<span style="font-size: 90%;">But does it affect your other future PRs we need for the next CRSv4 RC?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:32 UTC</span>

<span style="font-size: 90%;">Not really. That one will be quick</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:47 UTC</span>

<span style="font-size: 90%;">Word!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:25 UTC</span>

<span style="font-size: 90%;">_@Matteo Pace_ Do you want to work with me to put everything into a new PR? Probably based on _@Juan Pablo Tosso_'s work, but new implementation?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:02:46 UTC</span>

<span style="font-size: 90%;">Sure :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:07 UTC</span>

<span style="font-size: 90%;">OK. I guess this is mostly settled then and we'll implement it in a way we can switch to the new spell.sh by Max quickly.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:15 UTC</span>

<span style="font-size: 90%;">Anything else on this topic?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:41 UTC</span>

<span style="font-size: 90%;">I don't see anybody typing. So let's move to the next topic.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:05:46 UTC</span>

<span style="font-size: 90%;">Just to recap, so all these scripts will be a “quick and dirty” implementation that will be followed by a Go implementation inside the toolchain for 4.1?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:58 UTC</span>

<span style="font-size: 90%;">Pretty much</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:18 UTC</span>

<span style="font-size: 90%;">Unless you want to do it right now :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:20 UTC</span>

<span style="font-size: 90%;">No, what we have is quick and diry and what we want is a more or less professional implementation that will carry us until the integration.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:35 UTC</span>

<span style="font-size: 90%;">I mean the PR has the quick and dirty scripts.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:50 UTC</span>

<span style="font-size: 90%;">And we'll beautify these.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:07:14 UTC</span>

<span style="font-size: 90%;">Yep, got you, thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:19 UTC</span>

<span style="font-size: 90%;">We have a very welcome 3rd party contribution of a rule exclusion plugin for the iRedMail / Roundcube application. The problem at hand is the different instances of this software and whether they can all be addressed via the same plugin or if we need to do multiple plugins as well (and if the Aussie contributor has any interest to work on something that complicates his work).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:28 UTC</span>

<span style="font-size: 90%;">See [https://github.com/coreruleset/plugin-registry/pull/13](https://github.com/coreruleset/plugin-registry/pull/13)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:54 UTC</span>

<span style="font-size: 90%;">_@airween_ and _@maxleske_ you looked into this a bit deeper. What do you guys think how we should proceed?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:10:36 UTC</span>

<span style="font-size: 90%;">and if the Aussie contributor has any interest to work on something that complicates his workit shouldn't complicate the plugin much by splitting it into 3</span>

**airween** <span style="color: grey; font-size: 90%;">19:10:53 UTC</span>

<span style="font-size: 90%;">if we keep this plugin as is I would live with that - I mean splitting into 3 part is not necessary. But setting the RC path is important.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:07 UTC</span>

<span style="font-size: 90%;">3 plugins gives users more flexibility but at the cost of complexity, I guess</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:12:23 UTC</span>

<span style="font-size: 90%;"> I mean splitting into 3 part is not necessaryit would allow non iredmail users to use some of the exclusions for a non iredmail server</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:12:45 UTC</span>

<span style="font-size: 90%;">imo, if you want non iredmail users to use the plugin, this would be the better way of doing it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:11 UTC</span>

<span style="font-size: 90%;">E.g. RoundCube users could profit</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:35 UTC</span>

<span style="font-size: 90%;">Thank you for joining us at this horrible hour, _@Esad Cetiner_.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:14:37 UTC</span>

<span style="font-size: 90%;">may be he hasn't gone to bed yet... :smile:</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:14:51 UTC</span>

<span style="font-size: 90%;">I do have insomnia so...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:22 UTC</span>

<span style="font-size: 90%;">I am not sure I get this 100%. Namely not how "it would allow non iredmail users to use some of the exclusions for a non iredmail server". Would that be if split, or if kept together?</span>

**airween** <span style="color: grey; font-size: 90%;">19:14:37 UTC</span>

<span style="font-size: 90%;">may be he hasn't gone to bed yet... :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:14:37 UTC</span>

<span style="font-size: 90%;">may be he hasn't gone to bed yet... :smile:</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:14:51 UTC</span>

<span style="font-size: 90%;">I do have insomnia so...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:57 UTC</span>

<span style="font-size: 90%;">And how does setting the RC path play into this? We would only have to set when it's a single plugin. Correct?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:15:45 UTC</span>

<span style="font-size: 90%;"> Would that be if splitif we were to split it, a sogo user could use the sogo exclusions plugin and a roundcube user could use the roundcube exclusions.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:16:24 UTC</span>

<span style="font-size: 90%;"> We would only have to set when it's a single pluginyes, but I do feel it would be out of scope</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:41 UTC</span>

<span style="font-size: 90%;">And how does setting the RC path play into this? - as I know (now) iredmail installed to a specific path, which is (fix me if I'm wrong) always the same. But if someone install an RC instance, then it depends what does she/he chooses. Eg. I always choose /, but I have few old servers, where the previous admin installed under the /webmail</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:32 UTC</span>

<span style="font-size: 90%;">Got you. Thanks. It's mostly like I understood.</span>

**airween** <span style="color: grey; font-size: 90%;">19:18:04 UTC</span>

<span style="font-size: 90%;">and the plugin has built on the path of the webmail (the exclusion rules)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:06 UTC</span>

<span style="font-size: 90%;">What do you mean by "yes, but I do feel it would be out of scope" _@Esad Cetiner_. Out of scope for you, or what exactly?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:18:51 UTC</span>

<span style="font-size: 90%;"> Out of scope for you, or what exactlyout of scope for the plugin, since it's meant to specifically be used for an iredmail email server, not any installation of roundcube.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:05 UTC</span>

<span style="font-size: 90%;">Got you.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:20:48 UTC</span>

<span style="font-size: 90%;">it was just the first and simple choice IMO. spell doesn't requires anything and it has a built in dictionary. But we just need something that identify English words, it could be anything...</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:20:48 UTC</span>

<span style="font-size: 90%;">it was just the first and simple choice IMO. spell doesn't requires anything and it has a built in dictionary. But we just need something that identify English words, it could be anything...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:12 UTC</span>

<span style="font-size: 90%;">(hello everyone)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:13 UTC</span>

<span style="font-size: 90%;">Here is an idea: Can this plugin be designed in a generic way, like a template, and then there is a script that generates the rules-files for one of the multiple variants? By default this leads to a iredmail plugin, but you can run it, answer the right questions and you get a roundcube RE plugin?
Advantages: There is only a single plugin and we only use a single rule range, while still addressing multiple use cases of very similar software.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:33 UTC</span>

<span style="font-size: 90%;">Sounds nice but has the downside that we need to add more explanations to how plugins work: "oh, by the way, some plugins are special and have a script that you can run..." etc.</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:34 UTC</span>

<span style="font-size: 90%;">ohhh... template and generating rules from that? Yumm! I can help him in this! :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:57 UTC</span>

<span style="font-size: 90%;">Or we run that script to generate the variants?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:37 UTC</span>

<span style="font-size: 90%;">Then we'd still need 3 ID ranges, no?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:23:13 UTC</span>

<span style="font-size: 90%;"> Here is an idea: Can this plugin be designed in a generic way, like a template, and then there is a script that generates the rules-files for one of the multiple variants? By default this leads to a iredmail plugin, but you can run it, answer the right questions and you get a roundcube RE plugin?
Advantages: There is only a single plugin and we only use a single rule range, while still addressing multiple use cases of very similar software.I think a script is overkill, but I did have a similar idea around rebranding the plugin into a collection of rule exclusions for email related web software.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:13 UTC</span>

<span style="font-size: 90%;">It's a 3rd party plugin. _@Esad Cetiner_ is free to do anything ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:17 UTC</span>

<span style="font-size: 90%;">I think it’s a bit difficult for a user to do this</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:37 UTC</span>

<span style="font-size: 90%;">Then we'd still need 3 ID ranges, no?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:37 UTC</span>

<span style="font-size: 90%;">Then we'd still need 3 ID ranges, no?</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:55 UTC</span>

<span style="font-size: 90%;">Yes, but is that a problem?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:06 UTC</span>

<span style="font-size: 90%;">ID ranges: not necessarily. It would be the same rules with different URI prefix.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:27 UTC</span>

<span style="font-size: 90%;">Or different iredmail implementations get different tanges within the 1K block.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:02 UTC</span>

<span style="font-size: 90%;">No, I think _@walter_ is talking about running the script to generate the plugins, you are talking about a single plugin where the user runs the script</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:25:14 UTC</span>

<span style="font-size: 90%;"> Or different iredmail implementations get different tanges within the 1K block.all iredmail servers are setup the same, you just have a choice in what you want installed i.e roundcube vs sogo or iredadmin or no iredadmin.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:58 UTC</span>

<span style="font-size: 90%;">My point is: We have somebody taking the time to do something that a lot of people can profit from. I'd like to find a way to maximize the profit without adding a burden to our team and without annoying _@Esad Cetiner_ by asking to maintain stuff he does not need.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:32 UTC</span>

<span style="font-size: 90%;">_@maxleske_: Yes, if we distribute 3 plugins, then I think it ought to be 3 ranges.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:26:51 UTC</span>

<span style="font-size: 90%;">I don't have an issue with maintaining 3 plugins (or 2 if airween wants to do roundcube), I don't think the workload will be that much more anyways.</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:25 UTC</span>

<span style="font-size: 90%;">if airween wants to do roundcube - no, airween does not want to do that. He told me.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:23 UTC</span>

<span style="font-size: 90%;">_@airween_ has a history of being super lazy. He always takes the easy route <running away to hide in a bunker now></span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:29:52 UTC</span>

<span style="font-size: 90%;">I can be pretty lazy too if I want to</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:31:10 UTC</span>

<span style="font-size: 90%;">I just do not have enough time for it, unfortunately :disappointed:. So maximum respect and thanks for dealing with this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:00 UTC</span>

<span style="font-size: 90%;">_@Esad Cetiner_ That's quite the offer. From my perspective that would be like the best solution from a CRS perspective.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">but it's fun for me</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:23 UTC</span>

<span style="font-size: 90%;">Are you sure you can keep the 3 plugins in sync and keep the quality?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:30:59 UTC</span>

<span style="font-size: 90%;"> Are you sure you can keep the 3 plugins in sync and keep the quality?I already use both roundcube and iredadmin so I can be confident that those plugins will be high quality</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:31:08 UTC</span>

<span style="font-size: 90%;">I don't use sogo so that will be a bit harder for me</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:36 UTC</span>

<span style="font-size: 90%;">Thank you very much. This is most helpful.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:31:39 UTC</span>

<span style="font-size: 90%;"> From my perspective that would be like the best solution from a CRS perspectiveI agree, the only reason I made the plugin was to help other users.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">In fact we had hope CRS would sooner or later attract communities providing rule exclusion packages, it just did not happen. Creating the plugin system is the next step for us, since it makes contributions easier. Thank you for taking up this task.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:54 UTC</span>

<span style="font-size: 90%;">Anything else here?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:33:18 UTC</span>

<span style="font-size: 90%;"> Creating the plugin system is the next step for us, since it makes contributions easierthat is one of my favorite feature of CRS 4 for that reason</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:02 UTC</span>

<span style="font-size: 90%;">Same here. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">OK, the next and probably final item for tonight / early aussie morning is the idea to extend git conflicts to the agenda by placing a working copy of the agenda in the wiki and then we edit the agenda via git. On the plus side we would stop overwriting each other's agenda items. And given how frequently this happened lately, I have a preference for git conflicts here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:22 UTC</span>

<span style="font-size: 90%;">Alternative: Google docs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:25 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:36:30 UTC</span>

<span style="font-size: 90%;">Let's try it.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:36:44 UTC</span>

<span style="font-size: 90%;">Preferable to stay in one place (GitHub) rather than spreading out into Google Docs, if possible.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:58 UTC</span>

<span style="font-size: 90%;">That is a PRO, indeed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:23 UTC</span>

<span style="font-size: 90%;">Also: world visible while Google docs in our google drive is not.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:31 UTC</span>

<span style="font-size: 90%;">Very true.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:56 UTC</span>

<span style="font-size: 90%;">July's agenda is up, so shall we try for August?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:02 UTC</span>

<span style="font-size: 90%;">Or put July into the wiki?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:15 UTC</span>

<span style="font-size: 90%;">I'm very open to try this for the July agenda. Very easy to move and replace with a link to the wiki in the current agenda issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:28 UTC</span>

<span style="font-size: 90%;">And then move back once we're done.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:13 UTC</span>

<span style="font-size: 90%;">We could also try to use an iframe in the issue, if you still want to keep the issue.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:44 UTC</span>

<span style="font-size: 90%;">(not sure that will work)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:45 UTC</span>

<span style="font-size: 90%;">That would save copy-pasting things around. (If it works)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:40:19 UTC</span>

<span style="font-size: 90%;">But I guess not a problem if not.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:07 UTC</span>

<span style="font-size: 90%;">Let's just try and if iframe works then cool and if not, then we copy it back right before the meeting starts and close the wiki page.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:21 UTC</span>

<span style="font-size: 90%;">And if this does not work, we use something else for August.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:23 UTC</span>

<span style="font-size: 90%;">OK?</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:27 UTC</span>

<span style="font-size: 90%;">OK!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:32 UTC</span>

<span style="font-size: 90%;">Cool. Looks like we're done for tonight. Anything else to bring to the table? Any issues worth discussing?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:28 UTC</span>

<span style="font-size: 90%;">Well, good night / good morning then :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:47 UTC</span>

<span style="font-size: 90%;">Good night everyone :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:45:50 UTC</span>

<span style="font-size: 90%;">Thanks! See you around</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:55 UTC</span>

<span style="font-size: 90%;">Night!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:00 UTC</span>

<span style="font-size: 90%;">bye!</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:20 UTC</span>

<span style="font-size: 90%;">good night!</span>

**jit** <span style="color: grey; font-size: 90%;">19:46:29 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:41 UTC</span>

<span style="font-size: 90%;">btye!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:42 UTC</span>

<span style="font-size: 90%;">Good night everybody. And thank you for joining _@Esad Cetiner_</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:48:13 UTC</span>

<span style="font-size: 90%;">no worries!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">20:02:28 UTC</span>

<span style="font-size: 90%;">Sorry I couldn’t join :( I had something to do :face_holding_back_tears: </span>

