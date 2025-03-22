### Mon, Mar 3rd, 2025

**maxleske** <span style="color: grey; font-size: 90%;">19:30:17 UTC</span>

<span style="font-size: 90%;">Hello everyone, welcome to the monthly chat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:04 UTC</span>

<span style="font-size: 90%;">Hello _@maxleske_!</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:50 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:05 UTC</span>

<span style="font-size: 90%;">Hey! :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:32 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">Hi.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:32:50 UTC</span>

<span style="font-size: 90%;">Hello Hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:34:08 UTC</span>

<span style="font-size: 90%;">Not much on the agenda this week. The most important item (which isn't even on the agenda) is the fix for the CVE discovered in ModSecurity. I trust you've read the notice.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:35:42 UTC</span>

<span style="font-size: 90%;">I think Agenda-Next has not been copy-pasted across as there are items in there</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:36:51 UTC</span>

<span style="font-size: 90%;">Oh. Could you update the agenda with the missing items? I'll go ahead and talk about the next topic.</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:37:02 UTC</span>

<span style="font-size: 90%;">On it now.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">Unfortunately, that issue went undetected since September.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:24 UTC</span>

<span style="font-size: 90%;">We know there is a lack of testing in ModSecurity. But I am pleased to see that _@airween_ and Marc are slowly moving in the right direction there.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:57 UTC</span>

<span style="font-size: 90%;">Definitely! _@airween_ has been amazing!</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:28 UTC</span>

<span style="font-size: 90%;">yes, there is a student on UCLeuven who started to help me a lot in MRTS. He well make his master thesis from MRTS in June :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:57 UTC</span>

<span style="font-size: 90%;">Note that Marc invited him into that project</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:00 UTC</span>

<span style="font-size: 90%;">For those reading the notes here, MRTS == ?</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:14 UTC</span>

<span style="font-size: 90%;">Doh... [https://github.com/owasp-modsecurity/MRTS](https://github.com/owasp-modsecurity/MRTS)</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:28 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:42 UTC</span>

<span style="font-size: 90%;">_"ModSecurity Regression Test set_"</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:00 UTC</span>

<span style="font-size: 90%;">I believe we had already discussed [https://github.com/coreruleset/wordpress-rule-exclusions-plugin/pull/6](https://github.com/coreruleset/wordpress-rule-exclusions-plugin/pull/6) last time. I will take care of it, if it still needs work (we weren't sure if it's even relevant still).</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:46 UTC</span>

<span style="font-size: 90%;">yes, and I promised I'll take a look at that, and really sorry but I didn't have enough time to take care with that :disappointed:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:55 UTC</span>

<span style="font-size: 90%;">No worries :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:00 UTC</span>

<span style="font-size: 90%;">(I haven't forget it)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:34 UTC</span>

<span style="font-size: 90%;">Thanks _@xanadu_ for adding the lost agenda topics.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3991](https://github.com/coreruleset/coreruleset/issues/3991)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ could you give us a resumé?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:21 UTC</span>

<span style="font-size: 90%;">I'll give it a try then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:00 UTC</span>

<span style="font-size: 90%;">The proposal is to add specific tags to "each file", for easier rule removing.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:28 UTC</span>

<span style="font-size: 90%;">I see some value on this, but have some doubts.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:53 UTC</span>

<span style="font-size: 90%;">First: we are probably moving away from this file organization we have today.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:06 UTC</span>

<span style="font-size: 90%;">Of course, not tomorrow.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:31 UTC</span>

<span style="font-size: 90%;">But I see the value of having something that can be used to remove features as a whole.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:49 UTC</span>

<span style="font-size: 90%;">So the question is: is there any other organization than _tags_ for this?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:16 UTC</span>

<span style="font-size: 90%;">Then... adding tags is the best we have.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:25 UTC</span>

<span style="font-size: 90%;">I agree</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:44 UTC</span>

<span style="font-size: 90%;">So the question is: which tags we will be adding? Per-file? Per-feature?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:07 UTC</span>

<span style="font-size: 90%;">And of course: we need to keep things _sane_ afterwards.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:25 UTC</span>

<span style="font-size: 90%;">Did we ever measure the time penalty for adding tags? E.g. if we double the number of tags we add, how does that affect the time taken for a "RuleRemoveByTag" regex?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:37 UTC</span>

<span style="font-size: 90%;">Hopefully it is not too bad, but we ought to test</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:22 UTC</span>

<span style="font-size: 90%;">I don't believe we did. Would be good to know indeed.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:49 UTC</span>

<span style="font-size: 90%;">I don't think we'll be able to solve this tonight. But please comment on the issue if you have any thoughts.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:51 UTC</span>

<span style="font-size: 90%;">That was planned for the performance testing framework. But it never really became usable and without, proper performance metrics are hard.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:38 UTC</span>

<span style="font-size: 90%;">I'll apreciate your comments there, and followup tickets if needed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:43 UTC</span>

<span style="font-size: 90%;">It's also likely that RuleRemoveByTag could be performance optimized (together with its friends). But somebody would have to do the work.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:28 UTC</span>

<span style="font-size: 90%;">In the meantime... I don't think we need to solve that _now_, not _this team_ :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:53 UTC</span>

<span style="font-size: 90%;">But please add your comments in the ticket</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:16 UTC</span>

<span style="font-size: 90%;">Next topic:
Re-visiting this discussion: How does CRS want to approach `modsecurity.conf-recommended` in the future? The situation is clearly different, now, in 2025.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:48 UTC</span>

<span style="font-size: 90%;">I'll let the text from the agenda speak for itself:

> In the past, there was friction with the engine's previous owner (e.g. CRS advocated for enabling rule 200006 (allow JSON subtypes) by default, but we were told 'no'.)
> We previously discussed the idea that one day CRS could handle everything from `modsecurity.conf-recommended` directly within CRS, so that all config would be in one place and CRS could control which "default" rules to enable/disable.
> There is also now the potential to work with team ModSecurity to come up with a solution (e.g. keep `modsecurity.conf-recommended` but change the defaults to be more sensible/CRS-friendly).
> Why re-open this discussion now? It follows on from issue 9EA-241022. We removed several default allowed content types (including some "+json" subtypes). The open question remaining was: do we want to enable 'recommended' rule 200006 by default and retire rule 200001? And, more broadly, how do we want to work with/around `modsecurity.conf-recommended` going forwards?
</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:32 UTC</span>

<span style="font-size: 90%;">I'd leave this with ModSec, but make sure ModSec really cleans it up.

One major problem I see is the order of error handling.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:50:48 UTC</span>

<span style="font-size: 90%;">Oh jeez, I forgot about the error handling.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:51:00 UTC</span>

<span style="font-size: 90%;">Not even documented anywhere IIRC</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:52:33 UTC</span>

<span style="font-size: 90%;">[https://github.com/owasp-modsecurity/ModSecurity/wiki/Reference-Manual-(v2.x)#tx](https://github.com/owasp-modsecurity/ModSecurity/wiki/Reference-Manual-(v2.x)#tx)

?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:54:03 UTC</span>

<span style="font-size: 90%;">Yes, but nowhere does it say that you need to split the recommended rules around CRS (or another rule set). Someone asked Trustwave in the past and the response was "you simply have to know how to split the rules up that way" :no_mouth:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:55:19 UTC</span>

<span style="font-size: 90%;">ye, I see - and I can say that "documentation" is very poor (regarding the mentioned variables)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:33 UTC</span>

<span style="font-size: 90%;">Rule 200005 is typically executed before CRS, but CRS triggers errors (-> PCRE match limits) that would be detected by 200005.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:23 UTC</span>

<span style="font-size: 90%;">The rest can probably be solved with better defaults and better coordination with CRS. But how to do the error handling if there is only a single recommended rule file?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:41 UTC</span>

<span style="font-size: 90%;">This somewhat ties into the previous item about tagging / rule files. The current mechanism isn't very flexible. It would be great if we had some other mechanism to tell ModSecurity when to load which rules. That would also make it possible for ModSecurity to define "pre" and "post" rules.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:56:07 UTC</span>

<span style="font-size: 90%;">The same goes for CRS of course. The plugin mechanism would also become simpler.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:56:17 UTC</span>

<span style="font-size: 90%;">But of course, I haven't invented that system yet :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:34 UTC</span>

<span style="font-size: 90%;">Microphases / Subphases?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:58:42 UTC</span>

<span style="font-size: 90%;">Maybe. But I was thinking more along the lines of loading rules by something like ID block, instead of by inclusion order.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">20:00:12 UTC</span>

<span style="font-size: 90%;">Hmm, did not think about this before. Rule block, ....</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:57:38 UTC</span>

<span style="font-size: 90%;">It seems to me that the issue could be split into "default rules" and "error handling". The former appears to be easier to solve than the latter.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:46 UTC</span>

<span style="font-size: 90%;">With clear documentation, that could work as an immediate solution</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:00 UTC</span>

<span style="font-size: 90%;">"Error handling **must** come **after** rule set execution" etc</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:22 UTC</span>

<span style="font-size: 90%;">Would you be willing to work on that _@xanadu_? The first step would be rather simple: open two issues in the ModSecurity repo.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:00:33 UTC</span>

<span style="font-size: 90%;">Sure.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:04:53 UTC</span>

<span style="font-size: 90%;">Would you mind tagging me on the issues you are going to open? I would like to see how it has to be translated into fixes also to the Coraza config file :pray:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:05:20 UTC</span>

<span style="font-size: 90%;">Yep, will do</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">20:05:28 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:19 UTC</span>

<span style="font-size: 90%;">That's it for the main agenda. Does anyone have something else to add or talk about?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:02:57 UTC</span>

<span style="font-size: 90%;">Community call reminder?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:07 UTC</span>

<span style="font-size: 90%;">Yes, thanks. Good point.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:38 UTC</span>

<span style="font-size: 90%;">[https://coreruleset.org/20250203/first-crs-community-call/](https://coreruleset.org/20250203/first-crs-community-call/)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:01 UTC</span>

<span style="font-size: 90%;">The date is March 17.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:03 UTC</span>

<span style="font-size: 90%;">Don't miss this!</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:40 UTC</span>

<span style="font-size: 90%;">(it's already in the CRS calendar!)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:40 UTC</span>

<span style="font-size: 90%;">I think it's time to launch a social media campaign with as many personal / individual posts as possible.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:25 UTC</span>

<span style="font-size: 90%;">Thanks for your attendance. I wish more of us could be present for this once appointment per month. We might think about adjusting the schedule, if that would help (we would of course check with all of you first).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:48 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:13 UTC</span>

<span style="font-size: 90%;">Good night and bye</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:20 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**airween** <span style="color: grey; font-size: 90%;">20:07:24 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:07:43 UTC</span>

<span style="font-size: 90%;">Night.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:09 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:35 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4033#issuecomment-2695397663](https://github.com/coreruleset/coreruleset/issues/4033#issuecomment-2695397663)</span>

