### Mon, Jun 3rd, 2019

**dune73** <span style="color: grey; font-size: 90%;">18:31:02 UTC</span>

<span style="font-size: 90%;">Hello everybody. Hi _@0xInfection_, good to have you in our channel!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:16 UTC</span>

<span style="font-size: 90%;">So who's around (on the phone or via a real keyboard)?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">:wave::skin-tone-2:</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:37 UTC</span>

<span style="font-size: 90%;">hello everybody :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:54 UTC</span>

<span style="font-size: 90%;">Hi _@theMiddle_! Hello _@emphazer_! Is @fgsch around?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:32:58 UTC</span>

<span style="font-size: 90%;">i'm here :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:00 UTC</span>

<span style="font-size: 90%;">(I’ll be mostly read only because I’m extremely tired)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:05 UTC</span>

<span style="font-size: 90%;">_@fgs_ I meant.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;">Hello _@walter_!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:33:33 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:17 UTC</span>

<span style="font-size: 90%;">So we have our agenda at <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1443></span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:32 UTC</span>

<span style="font-size: 90%;">Feel free to add stuff.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:44 UTC</span>

<span style="font-size: 90%;">But let's start with our manifest ReDoS problem.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:45 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:13 UTC</span>

<span style="font-size: 90%;">We have a solution for the published CVE, but it has a side effect, we could not get rid of so far.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:31 UTC</span>

<span style="font-size: 90%;">See <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1417></span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:21 UTC</span>

<span style="font-size: 90%;">So the question is, what do we do? Do we postpone a release even further, or do we push through? We've been sitting on the CVE for almost two months now, so I favor a speedy resolution now.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:36:52 UTC</span>

<span style="font-size: 90%;">The regexp are not regenerated in realtime. We could simply ship the regexp</span>

**fgs** <span style="color: grey; font-size: 90%;">18:37:00 UTC</span>

<span style="font-size: 90%;">And fix the script later.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:37:07 UTC</span>

<span style="font-size: 90%;">Sounds good</span>

**csanders** <span style="color: grey; font-size: 90%;">18:37:11 UTC</span>

<span style="font-size: 90%;">that seems like the right solution to me</span>

**fgs** <span style="color: grey; font-size: 90%;">18:37:23 UTC</span>

<span style="font-size: 90%;">Perhaps add a comment to the rule. It’s not ideal, I know..</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:38 UTC</span>

<span style="font-size: 90%;">Yes, seems like a viable action also</span>

**csanders** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">but its best to get it fixed</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:49 UTC</span>

<span style="font-size: 90%;">_@csanders_ agreed to this in a separate chat already. So the plan would be to merge the fix to the regex, but not the updated regex-assembly.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:38:09 UTC</span>

<span style="font-size: 90%;">Ok, I will update the PR to remove the changes to the script.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:15 UTC</span>

<span style="font-size: 90%;">Instead, I'd like to ship a seperate regex-assembly, that is only aimed at 942260. That would be temporary.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:38:15 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:38:18 UTC</span>

<span style="font-size: 90%;">And open a separate PR to handle that.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:48 UTC</span>

<span style="font-size: 90%;">You ok with a separate regex-assembly? Like the PR version?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:39:11 UTC</span>

<span style="font-size: 90%;">Myself? Yup.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:16 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:24 UTC</span>

<span style="font-size: 90%;">So we have a way forward. Much appreciated.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:41 UTC</span>

<span style="font-size: 90%;">We can then do a 3.1.1 release. Does the release plan in the wiki still apply?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:55 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/wiki/Release-Procedure></span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:40:55 UTC</span>

<span style="font-size: 90%;">Sorry, I did not see the mention in the PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:17 UTC</span>

<span style="font-size: 90%;">Nevermind _@franbuehler_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:45 UTC</span>

<span style="font-size: 90%;">And do we release a RC, or do we go straight at the release. I mean we need to backport first, but afterwards ...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:55 UTC</span>

<span style="font-size: 90%;">If nobody has an opinion, I think we will do the release directly. It's a point release and if there is a problem (think 3.0.1), we can immediately</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:02 UTC</span>

<span style="font-size: 90%;">do a fix afterwards.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:43:32 UTC</span>

<span style="font-size: 90%;">Yep, I like it</span>

**csanders** <span style="color: grey; font-size: 90%;">18:44:05 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:05 UTC</span>

<span style="font-size: 90%;">Thanks _@theMiddle_. It seems _@csanders_ is still hooked in another meeting, then let's move to the PRs until we return to travis and docker afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:13 UTC</span>

<span style="font-size: 90%;">Ah, here he smiles again.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:25 UTC</span>

<span style="font-size: 90%;">_@csanders_: ready to talk about docker?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:44:36 UTC</span>

<span style="font-size: 90%;">can you give me 15?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:44:37 UTC</span>

<span style="font-size: 90%;">or 10</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:13 UTC</span>

<span style="font-size: 90%;">Sure. Then let's move to the PRs. My impression is, that most PRs are on hold / need action before they can be merged. So we are a bit stuck there.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:34 UTC</span>

<span style="font-size: 90%;">It's a bit of an unhealthy situation, I think as there are really a lot of PRs...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:12 UTC</span>

<span style="font-size: 90%;">I know, I think some of my PRs need action too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:51 UTC</span>

<span style="font-size: 90%;">There are the 3 PRs by our ReDoS researcher and a epic discussion on the git history on docker... But really nothing we could resolve tonight, or is there anything we should be discussing?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:47:35 UTC</span>

<span style="font-size: 90%;">No, I think, nothing we can resolve tonight, you're right.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:04 UTC</span>

<span style="font-size: 90%;">I have to work on my 3 PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:08 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:26 UTC</span>

<span style="font-size: 90%;">I did not have enough time/energy to work on them.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:34 UTC</span>

<span style="font-size: 90%;">But I'll try.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:39 UTC</span>

<span style="font-size: 90%;">So nothing to do with the PRs. That brings us to a brand new issue that is most unfortunate. <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1444></span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:51 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Could you explain the matter, please?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:48:57 UTC</span>

<span style="font-size: 90%;">I’m in a bad situation with v3</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:49:13 UTC</span>

<span style="font-size: 90%;">Thanks god _@airween_ helps me a lot</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:16 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:28 UTC</span>

<span style="font-size: 90%;">I found the bug, but don't know yet how can I solve</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:54 UTC</span>

<span style="font-size: 90%;">1444 basically says, rule exclusion packages do not work with ModSec3 and it's not our fault. But why?</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:36 UTC</span>

<span style="font-size: 90%;">sorry, what do you think about the "why"?</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:49 UTC</span>

<span style="font-size: 90%;">because v3 contains several bugs :stuck_out_tongue:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:56 UTC</span>

<span style="font-size: 90%;">ruleRemoveRargetByTag works only on exact match</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:59 UTC</span>

<span style="font-size: 90%;">On v3</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:03 UTC</span>

<span style="font-size: 90%;">I’m often using `removeTargetByTag=CRS` in exclusions, because `CRS` is then regexp matched to the tags and all our rules have `OWASP_CRS/FOO/BAR`, so the exclusion affects all our rules, it’s great for exclusions. but it seems that modsec v3 no longer does a regexp match on tags</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:06 UTC</span>

<span style="font-size: 90%;">Exact match?</span>

**airween** <span style="color: grey; font-size: 90%;">18:51:33 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">18:51:36 UTC</span>

<span style="font-size: 90%;">here:
<https://github.com/SpiderLabs/ModSecurity/blob/1cc22966db8c3e7574738ddac358cf51ab013f22/src/rule.cc#L865-L872></span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:52:07 UTC</span>

<span style="font-size: 90%;">Yep, as _@walter_ saying, in v3 is not possible to exclude a target on a rule using a substring of a tag</span>

**airween** <span style="color: grey; font-size: 90%;">18:52:20 UTC</span>

<span style="font-size: 90%;">_@walter_, yes, but the similar bug was fixed few days ago</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:28 UTC</span>

<span style="font-size: 90%;">oh that’s great!</span>

**airween** <span style="color: grey; font-size: 90%;">18:52:31 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/commit/5472362313ae1c69fad756ba149478d5650c2049></span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:38 UTC</span>

<span style="font-size: 90%;">Oh, I see. But that also means we used an undocumented feature of ModSec2, did not we?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:46 UTC</span>

<span style="font-size: 90%;">And now it's gone ...</span>

**airween** <span style="color: grey; font-size: 90%;">18:52:59 UTC</span>

<span style="font-size: 90%;">hmmm... that's a good question</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:02 UTC</span>

<span style="font-size: 90%;">ohhh, was it undocumented?</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:21 UTC</span>

<span style="font-size: 90%;">it was so useful! I am also often using `.*` in similar situations :disappointed:</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:24 UTC</span>

<span style="font-size: 90%;">I also didn't found any documentation about this, I had to review the source</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:30 UTC</span>

<span style="font-size: 90%;">in v2</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:02 UTC</span>

<span style="font-size: 90%;">Not sure if it is really undocumented, but I do not think I every saw regexes in this context (and I hardly ever remove by tag).</span>

**fgs** <span style="color: grey; font-size: 90%;">18:54:04 UTC</span>

<span style="font-size: 90%;">It is documented in v2</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:30 UTC</span>

<span style="font-size: 90%;">yeah it’s documented</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:35 UTC</span>

<span style="font-size: 90%;">So it is documented. How come, I am the one who knows so little about the documentation .... :disappointed:</span>

**fgs** <span style="color: grey; font-size: 90%;">18:54:56 UTC</span>

<span style="font-size: 90%;">Wait, I think I’m confusing it with SecRuleRemoveByTag.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:58 UTC</span>

<span style="font-size: 90%;">So it is not our fault but another shortcoming of the feature-complete ModSec3.</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:07 UTC</span>

<span style="font-size: 90%;">hmm well it’s actually NOT documented at all</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:15 UTC</span>

<span style="font-size: 90%;">_@fgs_, yes, but not the ruleRemoveTargetByTag</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:23 UTC</span>

<span style="font-size: 90%;">the format of these ctls is not speced in the reference manual</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:41 UTC</span>

<span style="font-size: 90%;">but it would stand to reason that ctl:ruleRemoveByTag works the same as the SecRuleRemoveByTag, which IS documented as: `Syntax: SecRuleRemoveByTag REGEX`</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:41 UTC</span>

<span style="font-size: 90%;">_@walter_ is right</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:48 UTC</span>

<span style="font-size: 90%;">The ref manual is completely bogus on the ctl. I tried to do a better job in the handbook.</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:04 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/blob/ca8e2db5a70de9b059ffb58eb468224d3d55b7e8/apache2/re_actions.c#L923-L933></span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:06 UTC</span>

<span style="font-size: 90%;">But it's still incomplete.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:56:07 UTC</span>

<span style="font-size: 90%;">_@walter_ yeah, that’s how I read it.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:56:26 UTC</span>

<span style="font-size: 90%;">In any case, it’s a change in behaviour from v2 to v3.</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:39 UTC</span>

<span style="font-size: 90%;">`if (!msc_pregcomp(mp, parm, 0, NULL, NULL))`
here compiles the regex from the parm</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:49 UTC</span>

<span style="font-size: 90%;">Do we have any chance of TW fixing this (with the support of our dear _@airween_)? Or do we need to think of an update to our rules?</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:31 UTC</span>

<span style="font-size: 90%;">I'm working on it, I hope I can fix it - but that will not a trivial as the last PR</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:57:41 UTC</span>

<span style="font-size: 90%;">A tag on all rule could be useful in situation like this one</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:50 UTC</span>

<span style="font-size: 90%;">If we remove by tag CRS, we can remove by ID 900000-999999 (unless that is not supported of course).</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:58:12 UTC</span>

<span style="font-size: 90%;">Oh, yes this sounds good too</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:58:28 UTC</span>

<span style="font-size: 90%;">And it means less work to do</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:42 UTC</span>

<span style="font-size: 90%;">I think it's supported</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:51 UTC</span>

<span style="font-size: 90%;">and works as well</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:01 UTC</span>

<span style="font-size: 90%;">_@walter_: what do you think?</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:16 UTC</span>

<span style="font-size: 90%;">I wonder what carries more downsides: adding an additional tag `CRS` to all our rules, or removing on 900000-999999 (which also catches crs-setup.conf, and our initialization rules, might this be less performant? or cause weird side effects?)</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:30 UTC</span>

<span style="font-size: 90%;">the latter would be a lot less work, IF it works :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:34 UTC</span>

<span style="font-size: 90%;">We have 103 mentions of byTag CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:53 UTC</span>

<span style="font-size: 90%;">A perf test is quickly done, I suppose.</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:10 UTC</span>

<span style="font-size: 90%;">I don’t recall much about how actually the algorithms work behind this ctl</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:20 UTC</span>

<span style="font-size: 90%;">a look at the debuglog at 9 would probably reveal much</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:47 UTC</span>

<span style="font-size: 90%;">it's less useful for v3 I think...</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:15 UTC</span>

<span style="font-size: 90%;">if we can get by with 900000-999999 that would surely be the better option for us in terms of maintenance load. touching every rule is horrible because likely other PRs will start conflicting because of it</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:42 UTC</span>

<span style="font-size: 90%;">and that’s such a drag on development speed and joy</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:02:45 UTC</span>

<span style="font-size: 90%;">Yep </span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:01 UTC</span>

<span style="font-size: 90%;">Yes, I think so too. If we want to be a bit more carefule, we could remove 910000-999999.</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:29 UTC</span>

<span style="font-size: 90%;">we also have rules in the 9M range but those don’t seem to matter for this purpose</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:36 UTC</span>

<span style="font-size: 90%;">_@theMiddle_, would you mind doing a PR for this?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:42 UTC</span>

<span style="font-size: 90%;">_@walter_: agreed.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:03:56 UTC</span>

<span style="font-size: 90%;">Yes! Of course </span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:06 UTC</span>

<span style="font-size: 90%;">Thank you for volunteering.</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:10 UTC</span>

<span style="font-size: 90%;">so I think 910000-999999 would be nice. maybe it’s even a lot faster: integer comparisons instead of regexp matches</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:19 UTC</span>

<span style="font-size: 90%;">True.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:34 UTC</span>

<span style="font-size: 90%;">This fix should go into 3.1.1. Correct?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:04:57 UTC</span>

<span style="font-size: 90%;">It would be nice</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:57 UTC</span>

<span style="font-size: 90%;">I wouldn’t mind</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:10 UTC</span>

<span style="font-size: 90%;">My production thanks for it :joy:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:45 UTC</span>

<span style="font-size: 90%;">Good, so if you are quick, it goes into 3.1.1, otherwise it will have to wait for a 3.1.2 or 3.2.0.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:53 UTC</span>

<span style="font-size: 90%;">Thank for the constructive resolution.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:13 UTC</span>

<span style="font-size: 90%;">_@csanders_: Ready?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:06:16 UTC</span>

<span style="font-size: 90%;">I can send it not before tomorrow, is it ok?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:06:22 UTC</span>

<span style="font-size: 90%;">readyish</span>

**csanders** <span style="color: grey; font-size: 90%;">19:06:23 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:32 UTC</span>

<span style="font-size: 90%;">Sure, _@theMiddle_. Even Wednesday. :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:06:40 UTC</span>

<span style="font-size: 90%;">so the general gist is simple</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:48 UTC</span>

<span style="font-size: 90%;">Please elaborate ....</span>

**csanders** <span style="color: grey; font-size: 90%;">19:07:06 UTC</span>

<span style="font-size: 90%;">we now have 3 docker images</span>

**csanders** <span style="color: grey; font-size: 90%;">19:08:06 UTC</span>

<span style="font-size: 90%;">all on v3.2 for NGINX-libmodsec, APACHE-libmodsec, and Apache-2.9.3</span>

**csanders** <span style="color: grey; font-size: 90%;">19:08:45 UTC</span>

<span style="font-size: 90%;">all of those run of all scans</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:55 UTC</span>

<span style="font-size: 90%;">We means 3.2.0 will carry these, or we means our Travis?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:02 UTC</span>

<span style="font-size: 90%;">oonly fails on the apache 2.9.3 failures</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:20 UTC</span>

<span style="font-size: 90%;">3.2.0 will carry all of these</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:28 UTC</span>

<span style="font-size: 90%;">and our travis is doing the scans with these</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:59 UTC</span>

<span style="font-size: 90%;">Nice. So that long story is actually over and docker is done?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:22 UTC</span>

<span style="font-size: 90%;">good question, there are some suggestions that we would like to take on from bittner</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:41 UTC</span>

<span style="font-size: 90%;">It's nice to see bittner so active and supporting.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:06 UTC</span>

<span style="font-size: 90%;">Where can I see the results of Apache-libmodsecurity Travis for a new PR?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:35 UTC</span>

<span style="font-size: 90%;"><https://travis-ci.org/SpiderLabs/owasp-modsecurity-crs></span>

**csanders** <span style="color: grey; font-size: 90%;">19:11:41 UTC</span>

<span style="font-size: 90%;">and on every PR :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:36 UTC</span>

<span style="font-size: 90%;">So we have the allowed failures below the mandatory pass. And when libmodsecurity is finally updated with the necessary fixes, we can make them conditional as well?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:48 UTC</span>

<span style="font-size: 90%;">exactly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:09 UTC</span>

<span style="font-size: 90%;">Brillant.
Does this run in parallel, or serial?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:14 UTC</span>

<span style="font-size: 90%;">parallel</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:14 UTC</span>

<span style="font-size: 90%;">that is really cool!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:32 UTC</span>

<span style="font-size: 90%;">oh and i fixed all the old version (3.0, 3.1, and 3.2) to work with modsec 2.9.3</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:43 UTC</span>

<span style="font-size: 90%;">Nice, nice.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:08 UTC</span>

<span style="font-size: 90%;">so now i'll be working to chmop down the size of the repos</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:15 UTC</span>

<span style="font-size: 90%;">and we're still waiting on OWASP for dockerhub to work</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">Technically, we can no add additional ModSec implementations like waflz?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:21 UTC</span>

<span style="font-size: 90%;">for auto builds but i'll be building more often</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:28 UTC</span>

<span style="font-size: 90%;">oh good question</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:29 UTC</span>

<span style="font-size: 90%;">yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:36 UTC</span>

<span style="font-size: 90%;">i have a working waflez build</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:47 UTC</span>

<span style="font-size: 90%;">And does it load CRS3?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:52 UTC</span>

<span style="font-size: 90%;">it does load it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:59 UTC</span>

<span style="font-size: 90%;">And ....</span>

**csanders** <span style="color: grey; font-size: 90%;">19:15:00 UTC</span>

<span style="font-size: 90%;">however our changes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:15:23 UTC</span>

<span style="font-size: 90%;">where we removed tx.msg</span>

**csanders** <span style="color: grey; font-size: 90%;">19:15:28 UTC</span>

<span style="font-size: 90%;">broke how they were processing rulese</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:38 UTC</span>

<span style="font-size: 90%;">Oh, oh...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:14 UTC</span>

<span style="font-size: 90%;">(For the record waflz is an alternative implementation of the ModSec rule language. It is opensource, but hardly used outside Verizon so far)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:34 UTC</span>

<span style="font-size: 90%;">so we'll see :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:16:45 UTC</span>

<span style="font-size: 90%;">they are aware of the issue -- i haven't been able to look at it much yet</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:53 UTC</span>

<span style="font-size: 90%;">Well, very good. Thank you for the good work here, _@csanders_ and whoever was involved here as well.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:03 UTC</span>

<span style="font-size: 90%;">bunch of the verizon team guys</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:29 UTC</span>

<span style="font-size: 90%;">Where I am not sure: Are the suggestions / developments of _@franbuehler_'s docker container (env variables) in our official container as well now? Or is that pending?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:18:20 UTC</span>

<span style="font-size: 90%;">I think this is still pending. We can start with this work, when the CRS image is ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:49 UTC</span>

<span style="font-size: 90%;">So that's about now?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:38 UTC</span>

<span style="font-size: 90%;">Yes, it seems so!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:19:56 UTC</span>

<span style="font-size: 90%;">yeah _@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:59 UTC</span>

<span style="font-size: 90%;">Great. I'm really looking forward to your features as well.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:20:08 UTC</span>

<span style="font-size: 90%;">we should figure out the best way to get the features of modsec down to the CRS image</span>

**csanders** <span style="color: grey; font-size: 90%;">19:20:23 UTC</span>

<span style="font-size: 90%;">not sure i designed it well given that requirement -- but we'll make it through :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:37 UTC</span>

<span style="font-size: 90%;">features of modes down? Not sure I follow you....</span>

**csanders** <span style="color: grey; font-size: 90%;">19:20:41 UTC</span>

<span style="font-size: 90%;">sorry -- just finished my meeting :honey_pot:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:20:58 UTC</span>

<span style="font-size: 90%;">like proxy/ssl/etc</span>

**csanders** <span style="color: grey; font-size: 90%;">19:21:20 UTC</span>

<span style="font-size: 90%;">they are supported in the upstream modsec images -- but with env variables -- not sure the best way to activate those downstream (might be possible)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:21:29 UTC</span>

<span style="font-size: 90%;">have to look at the docs :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:58 UTC</span>

<span style="font-size: 90%;">OK, ok. Kind of get it. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:07 UTC</span>

<span style="font-size: 90%;">So we move on to the next issue?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:23:13 UTC</span>

<span style="font-size: 90%;">please :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:28 UTC</span>

<span style="font-size: 90%;">That would be <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1320>, I guess</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:24:01 UTC</span>

<span style="font-size: 90%;">Yes, the last comment</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:15 UTC</span>

<span style="font-size: 90%;">Also a rather unfortunate turn of events. Can you summarize quickly, please.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:12 UTC</span>

<span style="font-size: 90%;">on v2 (and not v3 just for a bug that _@airween_ is going to fix) it’s possible to bypass all rules that inspect REQUEST_BODY just by setting the CT triggering the XML or JSON body processor</span>

**csanders** <span style="color: grey; font-size: 90%;">19:26:42 UTC</span>

<span style="font-size: 90%;">why is that the case?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:26:46 UTC</span>

<span style="font-size: 90%;">is REQUEST_BODY not filled?</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:50 UTC</span>

<span style="font-size: 90%;">no</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:01 UTC</span>

<span style="font-size: 90%;">And if the backend ignores the CT and reads it anyways, then the backend if doomed?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:27:39 UTC</span>

<span style="font-size: 90%;">That’s the point</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:03 UTC</span>

<span style="font-size: 90%;">in v3, the REQUEST_BODY filled</span>

**csanders** <span style="color: grey; font-size: 90%;">19:27:09 UTC</span>

<span style="font-size: 90%;">thats kinda strange</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:10 UTC</span>

<span style="font-size: 90%;">that's why it worked</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:30 UTC</span>

<span style="font-size: 90%;">So at last v3 does something better than v2.</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:37 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:27:39 UTC</span>

<span style="font-size: 90%;">That’s the point</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:27:39 UTC</span>

<span style="font-size: 90%;">That’s the point</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:57 UTC</span>

<span style="font-size: 90%;">In phase 2 the REQUEST_BODY is gone if CT was one of the special processors.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:28:06 UTC</span>

<span style="font-size: 90%;">Yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:09 UTC</span>

<span style="font-size: 90%;">i guess that makes some sense as the body may be huge</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:16 UTC</span>

<span style="font-size: 90%;">And we do not really have the means to test if CT and body corresponds, or do we?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:28:18 UTC</span>

<span style="font-size: 90%;">but not that much</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:25 UTC</span>

<span style="font-size: 90%;">I think in v2 the REQUEST_BODY isn't filled, if the CT was spec</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:36 UTC</span>

<span style="font-size: 90%;">in v3, it does</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:42 UTC</span>

<span style="font-size: 90%;">now (in the current v3/master branch) there is a bug: it does not matter, what is the CT, always check the RWQUEST_BODY, if the rule use it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:43 UTC</span>

<span style="font-size: 90%;">Why is no the body processor failing if the payload is not matching the CT? This is the piece I do not get.</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:05 UTC</span>

<span style="font-size: 90%;">that's the bug</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">But it constantly fails and is being caught by recommended rule 200002, or what do I not get?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:35 UTC</span>

<span style="font-size: 90%;">SecRule REQBODY_ERROR "!@eq 0" \
"id:'200002', phase:2,t:none,log,deny,status:400,msg:'Failed to parse request body.',logdata:'%{reqbody_error_msg}',severity:2"</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:15 UTC</span>

<span style="font-size: 90%;">this fails in v2 only, or not?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:49 UTC</span>

<span style="font-size: 90%;">Have not tested this in v3, but you guys stated the bypass only works in v2.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:35:03 UTC</span>

<span style="font-size: 90%;">Maybe 200002 blocks it, didn’t test because of the XML rule-set. In this case, 200002 it’s irrilevant</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:51 UTC</span>

<span style="font-size: 90%;">I don't understand. XML rule-set? And why is it irrelevant?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:27 UTC</span>

<span style="font-size: 90%;">Because the body respect what the CT says</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:16 UTC</span>

<span style="font-size: 90%;">But, in that case, we have no other option than reading from REQUEST BODY </span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:57 UTC</span>

<span style="font-size: 90%;">But our documentation says, we assume rule 200002 (= recommended rules) is in place. If that is not granted, we run in an environment which does not follow our standard.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:38:49 UTC</span>

<span style="font-size: 90%;">No I mean that the body is a valid XML syntax</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:39:33 UTC</span>

<span style="font-size: 90%;">The problem is that the body processor makes unavailable the request body variable </span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">Oh, now I get it. You can make the body correct XML, but the parsed argument do not see the attack payload, it would take REQUEST_BODY to see it?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:30 UTC</span>

<span style="font-size: 90%;">Does that only work with xee, or are there generally parts of XML that are hidden (= don't resolve to parameters)?
For the record: XXE makes security a mess for ModSecurity. The effects are horrible and there is very little you can do.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:15 UTC</span>

<span style="font-size: 90%;">idk if this happens with JSON syntax too but I don’t think so...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:17 UTC</span>

<span style="font-size: 90%;">As the case stands, I do not see much beyond making REQUEST_BODY available to CRS in v2 - or whitelisting CT for URIs...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:36 UTC</span>

<span style="font-size: 90%;">Anyways, there is little we can do and it's really annoying.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:43:52 UTC</span>

<span style="font-size: 90%;">_@airween_ is currently doing his magic things in order to solve this problem in v3</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:15 UTC</span>

<span style="font-size: 90%;">but that will not solve in v2 :disappointed:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:24 UTC</span>

<span style="font-size: 90%;">I mean makes the request body variable always available </span>

**airween** <span style="color: grey; font-size: 90%;">19:44:33 UTC</span>

<span style="font-size: 90%;">yep</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:36 UTC</span>

<span style="font-size: 90%;">:disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:59 UTC</span>

<span style="font-size: 90%;">Looking at the agenda, I think we skipped the new ReDoS checker by _@airween_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:14 UTC</span>

<span style="font-size: 90%;">Sorry about that. Let's return to this new invention, _@airween_.</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:16 UTC</span>

<span style="font-size: 90%;">v2 doc said:
```
Holds the raw request body. This variable is available only if the URLENCODED request body processor was used, which will occur by default when the application/x-www-form-urlencoded content type is detected, or if the use of the URLENCODED request body parser was forced. ```</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:26 UTC</span>

<span style="font-size: 90%;">okay</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:29 UTC</span>

<span style="font-size: 90%;">Mighty welcome development.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:28 UTC</span>

<span style="font-size: 90%;">then we are done?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">i guess so :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:44 UTC</span>

<span style="font-size: 90%;">Yes, then we're done.</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:52 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:17 UTC</span>

<span style="font-size: 90%;">What exactly can we expect from your new checker. Will it catch like 80% of the problems, or all of them? Or only point where to look by hand?</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:50 UTC</span>

<span style="font-size: 90%;">just point to the potentially dangerous regex's</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:27 UTC</span>

<span style="font-size: 90%;">and only when the more repeat symbol followed each others</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:03 UTC</span>

<span style="font-size: 90%;">it similar to the regex, what you showed at last monthly agenda, by _@franbuehler_</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:11 UTC</span>

<span style="font-size: 90%;">with `grep`</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:30 UTC</span>

<span style="font-size: 90%;">but this one is a little bit more sophisticated</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:09 UTC</span>

<span style="font-size: 90%;">When you run it across all our rules, how many alerts do you get?</span>

**airween** <span style="color: grey; font-size: 90%;">19:50:13 UTC</span>

<span style="font-size: 90%;">here is the reporter summary:
<https://github.com/SpiderLabs/ModSecurity/issues/2072#issuecomment-483925456></span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:32 UTC</span>

<span style="font-size: 90%;">nice</span>

**airween** <span style="color: grey; font-size: 90%;">19:51:31 UTC</span>

<span style="font-size: 90%;">the alternative handling isn't showed with my tool</span>

**airween** <span style="color: grey; font-size: 90%;">19:51:48 UTC</span>

<span style="font-size: 90%;">here is the output:
```
933160: may be vulnerable, need to check
933180: may be vulnerable, need to check
933161: may be vulnerable, need to check
942130: Regex compile error
942310: may be vulnerable, need to check
942330: may be vulnerable, need to check
942450: may be vulnerable, need to check
932100: may be vulnerable, need to check
932105: may be vulnerable, need to check
932140: may be vulnerable, need to check
932150: may be vulnerable, need to check
932106: may be vulnerable, need to check
941210: may be vulnerable, need to check
941220: may be vulnerable, need to check
920460: Regex compile error
```</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:12 UTC</span>

<span style="font-size: 90%;">_@csanders_: Do you see us adding this to Travis? So we would get an alarm when we _create_ new ReDoS problems? I mean we might need to start with a whitelist of rules, where we are OK with the alert for the time being...</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:19 UTC</span>

<span style="font-size: 90%;">of course</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:23 UTC</span>

<span style="font-size: 90%;">we can add it VERRY quickly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:13 UTC</span>

<span style="font-size: 90%;">All we need is a wrapper with the the whitelist of the rule above (thanks _@airween_), or is there more?</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:19 UTC</span>

<span style="font-size: 90%;">we can add any white list to this tool, if you mean about that...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:58 UTC</span>

<span style="font-size: 90%;">As you wish.</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:26 UTC</span>

<span style="font-size: 90%;">if _@csanders_ will tell me, what do I place and how (eg: external file, ...), I can add it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:53 UTC</span>

<span style="font-size: 90%;">Cool. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:08 UTC</span>

<span style="font-size: 90%;">And if there is nothing else, then I suggest we close this meeting...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:22 UTC</span>

<span style="font-size: 90%;">I'll close my original PR, ok?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:24 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1371></span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:48 UTC</span>

<span style="font-size: 90%;">I guess it is superseeded with the new checker, yes.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:42 UTC</span>

<span style="font-size: 90%;">so i can walk you through that airween -- we can either pull from an external repo (like the parser) or include it locally (like the regression tests)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:07 UTC</span>

<span style="font-size: 90%;">OK, I think I'll retire. Thanks everybody for joining. We made some good progress tonight, even if most of the topics were rather depressive.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:18 UTC</span>

<span style="font-size: 90%;">thanks _@dune73_</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:21 UTC</span>

<span style="font-size: 90%;">keep up the good work all</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:23 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:34 UTC</span>

<span style="font-size: 90%;">Thank you, _@dune73_</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:03:51 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:04:04 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:06 UTC</span>

<span style="font-size: 90%;">good night :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:04:15 UTC</span>

<span style="font-size: 90%;">Good night, and bye everyone!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:17 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:04:19 UTC</span>

<span style="font-size: 90%;">good night :wave:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:21 UTC</span>

<span style="font-size: 90%;">nite nite!</span>

