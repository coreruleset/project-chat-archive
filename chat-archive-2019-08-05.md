### Mon, Aug 5th, 2019

**dune73** <span style="color: grey; font-size: 90%;">18:30:24 UTC</span>

<span style="font-size: 90%;">Hello everybody. Welcome to the monthly chat.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:30:31 UTC</span>

<span style="font-size: 90%;">heyhooo</span>

**walter** <span style="color: grey; font-size: 90%;">18:30:35 UTC</span>

<span style="font-size: 90%;">hellø !</span>

**airween** <span style="color: grey; font-size: 90%;">18:30:56 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:12 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**csanders** <span style="color: grey; font-size: 90%;">18:31:20 UTC</span>

<span style="font-size: 90%;">good morning</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:33 UTC</span>

<span style="font-size: 90%;">Good morning _@csanders_ :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:56 UTC</span>

<span style="font-size: 90%;">Cool to see you call.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:01 UTC</span>

<span style="font-size: 90%;">Shall we kick it off?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:27 UTC</span>

<span style="font-size: 90%;">The agenda is at <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1496>. Feel free to add more items.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:52 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ will be late. And I guess _@fgs_ is having dinner with his little family.</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:08 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:01 UTC</span>

<span style="font-size: 90%;">So we have declogged the PR pipeline successfully and so the meeting is much leaner on that front, thus a bit more time to talk about other project topics.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:24 UTC</span>

<span style="font-size: 90%;">We have a new contribution at 1490. Has anybody looked at it? No comment so far...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:53 UTC</span>

<span style="font-size: 90%;">It seems simple enough...</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:18 UTC</span>

<span style="font-size: 90%;">it looks uncontroversial to me! it’s true that you also have PUBLIC, but i’m not so aware of how they work…</span>

**fgs** <span style="color: grey; font-size: 90%;">18:35:21 UTC</span>

<span style="font-size: 90%;">I’m here</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:28 UTC</span>

<span style="font-size: 90%;">Hi _@fgs_!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:35:31 UTC</span>

<span style="font-size: 90%;">Not sure for how long though :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:36 UTC</span>

<span style="font-size: 90%;">haha</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:49 UTC</span>

<span style="font-size: 90%;"><https://xmlwriter.net/xml_guide/entity_declaration.shtml> says, “Private external entities are identified by the keyword SYSTEM, and are intended for use by a single author or group of authors. Public external entities are identified by the keyword PUBLIC and are intended for broad use.

<!ENTITY name SYSTEM “URI”>
<!ENTITY name PUBLIC “public_ID” “URI”>”</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:58 UTC</span>

<span style="font-size: 90%;">There is a merge conflict now, but other than that it think it's merge-worthy.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:05 UTC</span>

<span style="font-size: 90%;">If nobody objects, I'm going to self-assign and see it being merged.</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:16 UTC</span>

<span style="font-size: 90%;">nice offer, thanks :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">18:37:32 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:56 UTC</span>

<span style="font-size: 90%;">Next one: [#1487](https://github.com/coreruleset/coreruleset/issues/#1487) by _@walter_</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:22 UTC</span>

<span style="font-size: 90%;">yes. I’m still a bit conflicted on creating a new file versus adding the single rule to RCE…</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:13 UTC</span>

<span style="font-size: 90%;">and gotwf made some salient comments about us not having many rules against newish targets</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:25 UTC</span>

<span style="font-size: 90%;">Yes, that's really a question. What do you guys think about a "various applications / languages" group</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:45 UTC</span>

<span style="font-size: 90%;">He's right though, but we can only merge what we get as PRs.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:33 UTC</span>

<span style="font-size: 90%;">that’s true, but I could see myself becoming a bit more proactive and write some rules</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:29 UTC</span>

<span style="font-size: 90%;">so I went on youtube and watched some talks about node.js security, but people seemed most concerned with NPM related issues rather than specific attacks</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:34 UTC</span>

<span style="font-size: 90%;">but I still have a dream…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:46 UTC</span>

<span style="font-size: 90%;">Haha ...</span>

**fgs** <span style="color: grey; font-size: 90%;">18:41:55 UTC</span>

<span style="font-size: 90%;">a world without node.js? :troll:</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:07 UTC</span>

<span style="font-size: 90%;">nevertheless, yes, it’s safe to assume that we won’t get too many PRs and we might get a bit more rule files with just one or a few rules… I wouldn’t mind that too much myself</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:23 UTC</span>

<span style="font-size: 90%;">well a world without PHP would probably be safer :smile: we have many PHP rules but you actually need them!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:07 UTC</span>

<span style="font-size: 90%;">I think as there are many more languages and we grow our project, a various section might actually help.</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:30 UTC</span>

<span style="font-size: 90%;">but a rule can’t really exit out of a various section, as we number our rules</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:49 UTC</span>

<span style="font-size: 90%;">so I could see where it could get a bit messy after some time</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:05 UTC</span>

<span style="font-size: 90%;">Yes, that is an issue. But then the exit is unlikely to be pressing and with a major release like CRS4 we could do a various cleanup.</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:29 UTC</span>

<span style="font-size: 90%;">the RCE file is also a bit of a various bag right now with some windows shell stuff, bash, etc…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:31 UTC</span>

<span style="font-size: 90%;">If we're not doing that way we run the risk blocking a rule block with only two rules ...</span>

**csanders** <span style="color: grey; font-size: 90%;">18:44:38 UTC</span>

<span style="font-size: 90%;">I dunno it is hard to say</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:46 UTC</span>

<span style="font-size: 90%;">True for RCE, but do we need to make it works.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:54 UTC</span>

<span style="font-size: 90%;">make it worse?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:46:04 UTC</span>

<span style="font-size: 90%;">I'm kinda hoping we can throw  some template injection, some parameter pollution</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:04 UTC</span>

<span style="font-size: 90%;">Any other opinions on the question of separate node.js rule group or integration or new various group?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:46:22 UTC</span>

<span style="font-size: 90%;">the problem is template injection is more general than Node</span>

**csanders** <span style="color: grey; font-size: 90%;">18:46:29 UTC</span>

<span style="font-size: 90%;">but not RCE always</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:59 UTC</span>

<span style="font-size: 90%;">Which makes "various" all the more attractive...</span>

**fgs** <span style="color: grey; font-size: 90%;">18:47:39 UTC</span>

<span style="font-size: 90%;">_@dune73_ to summarise, is the question whether we should have separate categories or fold them into RCE?</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:51 UTC</span>

<span style="font-size: 90%;">I hate creating “misc” / “utilities” in software projects though, it doesn’t force the author enough to decide what is what</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:07 UTC</span>

<span style="font-size: 90%;">A nodejs category, a various category or integrate into RCE, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:26 UTC</span>

<span style="font-size: 90%;">You have a point there.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:48:46 UTC</span>

<span style="font-size: 90%;">We do have PHP</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">Do we have enough rules to warrant a nodejs category though?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:20 UTC</span>

<span style="font-size: 90%;">Not yet enough ...</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:28 UTC</span>

<span style="font-size: 90%;">We can always split them later</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:32 UTC</span>

<span style="font-size: 90%;">But we need to make the decision with the first rule that we release...</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:32 UTC</span>

<span style="font-size: 90%;">at this point, it would be 1 rule, and this rule is mostly against older versions of serialization libraries, so it’s a bit thin…</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:45 UTC</span>

<span style="font-size: 90%;">but I’m definitely willing to add lots more rules and also do the rule writing for it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:17 UTC</span>

<span style="font-size: 90%;">If you can guarantee 10 rules, we're game.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:50:19 UTC</span>

<span style="font-size: 90%;">> But we need to make the decision with the first rule that we release...
because of the rule ids?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:50:24 UTC</span>

<span style="font-size: 90%;">bingo</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:31 UTC</span>

<span style="font-size: 90%;">Yes, exactly, because of the rule ids.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:50:39 UTC</span>

<span style="font-size: 90%;">my personal take is as long as it’s not in a release</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:40 UTC</span>

<span style="font-size: 90%;">yes, the ruleids are hard to revise, and currently we are in the great position that our numbering is pretty sane</span>

**fgs** <span style="color: grey; font-size: 90%;">18:50:49 UTC</span>

<span style="font-size: 90%;">the numbers in master can change</span>

**fgs** <span style="color: grey; font-size: 90%;">18:51:03 UTC</span>

<span style="font-size: 90%;">once it’s in a release, it’s a different story</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:12 UTC</span>

<span style="font-size: 90%;">I agree on that.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:51:16 UTC</span>

<span style="font-size: 90%;">but not sure if that’s the official posture</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:09 UTC</span>

<span style="font-size: 90%;">I’m not sure if people run our stuff straight from git, I have done so sometimes when I didn’t want to wait on a release, but true, we shouldn’t guarantee too much</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:27 UTC</span>

<span style="font-size: 90%;">but we do want to cut a release around AppSec Amsterdam which is short of 2 months from now</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:48 UTC</span>

<span style="font-size: 90%;">I don’t think there is an ideal solution, but I think it’s still a slight bit cleaner to have language specific files even if they are a bit thin</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:11 UTC</span>

<span style="font-size: 90%;">maybe a NOSQL file for all kinds of NoSQL databases</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:20 UTC</span>

<span style="font-size: 90%;">I can live with that decision.</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:45 UTC</span>

<span style="font-size: 90%;">Nodejs is probably [going to be] big enough that we will have more and more rules for it</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">I have some cipher injection work i'm doing</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:49 UTC</span>

<span style="font-size: 90%;">the main problem is modsec's  stunning lack ofJSON parsing support</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:03 UTC</span>

<span style="font-size: 90%;">well -- refined JSON parsing support</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:10 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:15 UTC</span>

<span style="font-size: 90%;">sounds interesting!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:34 UTC</span>

<span style="font-size: 90%;">So we make it a separate nodejs, walter finishes the PR and we move on with the discussion?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:41 UTC</span>

<span style="font-size: 90%;">sounds good</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:48 UTC</span>

<span style="font-size: 90%;">yes I think a nodejs file will probably be filled eventually :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:02 UTC</span>

<span style="font-size: 90%;">alright, I’ll just fix up this PR</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:24 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:31 UTC</span>

<span style="font-size: 90%;">what do you think about gotwf’s comments? I would be happy to take on some work writing rules, but we do need informations about possible attacks</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:46 UTC</span>

<span style="font-size: 90%;">I wonder if we could gather some people … maybe after your talk _@dune73_? :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">18:56:49 UTC</span>

<span style="font-size: 90%;">I agree,i'd be interested in helping a biit</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:50 UTC</span>

<span style="font-size: 90%;">Hi</span>

**csanders** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">hey _@franbuehler_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:03 UTC</span>

<span style="font-size: 90%;">Hey _@franbuehler_, welcome.</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:04 UTC</span>

<span style="font-size: 90%;">hi _@franbuehler_ :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:22 UTC</span>

<span style="font-size: 90%;">After my talk in Amsterdam?</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:26 UTC</span>

<span style="font-size: 90%;">broader, how can we motivate people to send us interesting attacks?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:57:46 UTC</span>

<span style="font-size: 90%;">one idea is to make a rule submission page</span>

**csanders** <span style="color: grey; font-size: 90%;">18:57:53 UTC</span>

<span style="font-size: 90%;">where 0day rules can be submitted</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:03 UTC</span>

<span style="font-size: 90%;">I would still like to grow our project to 15 committers this year...</span>

**csanders** <span style="color: grey; font-size: 90%;">18:58:03 UTC</span>

<span style="font-size: 90%;">liike a less bad SL rules</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:46 UTC</span>

<span style="font-size: 90%;">I do see enough garden variety PHP attacks and general filesystem based stuff towards <http://coreruleset.org|coreruleset.org> (at least the stuff that we detect :bulb: )</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:08 UTC</span>

<span style="font-size: 90%;">but this is the age of node.js and the reverse proxy so I really want to do more there</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:17 UTC</span>

<span style="font-size: 90%;">at least we are still in the picture…</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">18:59:22 UTC</span>

<span style="font-size: 90%;">good evening!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:26 UTC</span>

<span style="font-size: 90%;">Yes, that is certainly the case. We want more in that regard.</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:31 UTC</span>

<span style="font-size: 90%;">hi _@Christian Treutler_ :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:37 UTC</span>

<span style="font-size: 90%;">Hello _@Christian Treutler_, good to see you around.</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">18:59:48 UTC</span>

<span style="font-size: 90%;">Kids are finally asleep :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:01 UTC</span>

<span style="font-size: 90%;">We're talking about the problem of getting better coverage of modern attacks against modern app servers like node</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:59 UTC</span>

<span style="font-size: 90%;">So let's keep this in mind as a general direction that we would like to take and make be can recruit experts in this field.</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:39 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:52 UTC</span>

<span style="font-size: 90%;">[#1484](https://github.com/coreruleset/coreruleset/issues/#1484) is ready to be merged.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:58 UTC</span>

<span style="font-size: 90%;">Objections?</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:06 UTC</span>

<span style="font-size: 90%;">looks good to me!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:27 UTC</span>

<span style="font-size: 90%;">Could you merge, please. We can then continue with [#1467](https://github.com/coreruleset/coreruleset/issues/#1467).</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:36 UTC</span>

<span style="font-size: 90%;">great! i’ll do it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:49 UTC</span>

<span style="font-size: 90%;">_@csanders_: You are still covering that contribution by _@Allan Boll_, are not you?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:05:48 UTC</span>

<span style="font-size: 90%;">I know I am a bit late, but I think, it would be good to cover the "new" MEAN stack, MongoDB, Express (I don't know it), Angular and Node.js.
Yes, I think that is a good plan...</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:05:58 UTC</span>

<span style="font-size: 90%;">I see there's a comment in there about integrating it with the owasp crs image</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:05:59 UTC</span>

<span style="font-size: 90%;">Sorry, for the interruption...  go ahead</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:06:17 UTC</span>

<span style="font-size: 90%;">that kind of defeats the point of this PR. The point is to test against stock ubuntu modsec binaries, as that's what many users will.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:06 UTC</span>

<span style="font-size: 90%;">_@csanders_?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:07:12 UTC</span>

<span style="font-size: 90%;">_@Allan Boll_ Is the idea of this to replace the jobs in travis?</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:07:21 UTC</span>

<span style="font-size: 90%;">nope</span>

**csanders** <span style="color: grey; font-size: 90%;">19:07:24 UTC</span>

<span style="font-size: 90%;">sorry about that --  was  gone for a sec</span>

**fgs** <span style="color: grey; font-size: 90%;">19:07:24 UTC</span>

<span style="font-size: 90%;">or to be able to quickly and simply run the tests without all the typing?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:07:56 UTC</span>

<span style="font-size: 90%;">he wanted to replace the travis tests</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:07:57 UTC</span>

<span style="font-size: 90%;">just needed a quick way to run the CRS tests locally while making changes to CRS, in a way that realisticly reflects what most users will be running</span>

**csanders** <span style="color: grey; font-size: 90%;">19:08:14 UTC</span>

<span style="font-size: 90%;">so the thing we were gonna  do was just add a flag for FTW on the upstream</span>

**csanders** <span style="color: grey; font-size: 90%;">19:08:24 UTC</span>

<span style="font-size: 90%;">which will run the tests</span>

**fgs** <span style="color: grey; font-size: 90%;">19:09:19 UTC</span>

<span style="font-size: 90%;">As someone who runs the tests manually many times, having an easier way to run the tests makes sense</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:38 UTC</span>

<span style="font-size: 90%;">the thought is that we'll add a -FTW</span>

**fgs** <span style="color: grey; font-size: 90%;">19:09:40 UTC</span>

<span style="font-size: 90%;">I’m not sure, however, if we should (or want) to support other configurations</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:41 UTC</span>

<span style="font-size: 90%;">or the like</span>

**csanders** <span style="color: grey; font-size: 90%;">19:09:47 UTC</span>

<span style="font-size: 90%;">and it will run the tests</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:03 UTC</span>

<span style="font-size: 90%;">and you can overriide the endpoint and just get the testing env</span>

**fgs** <span style="color: grey; font-size: 90%;">19:10:05 UTC</span>

<span style="font-size: 90%;">Because the options will be endless</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:23 UTC</span>

<span style="font-size: 90%;">_@Allan Boll_ does that support your use case?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:10:55 UTC</span>

<span style="font-size: 90%;">it will also simplify travis a tidbit, not much</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:11:22 UTC</span>

<span style="font-size: 90%;">think of someone jumping in to contribute a simple CRS change (my coworkers here for example): they just need a simple discoverable way of running the tests. They won't be looking around in other repos for this.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:12 UTC</span>

<span style="font-size: 90%;">that makes sense to me -- i think this with a minor readme change will make it easier</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:12:34 UTC</span>

<span style="font-size: 90%;">yea maybe something prominent in the readme is the key</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:48 UTC</span>

<span style="font-size: 90%;">essentially saying - run docker  run -ftw ... to run all the tests</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:57 UTC</span>

<span style="font-size: 90%;">here is how to run it against your custom banch ....</span>

**csanders** <span style="color: grey; font-size: 90%;">19:12:59 UTC</span>

<span style="font-size: 90%;">etc</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:07 UTC</span>

<span style="font-size: 90%;">I would not mind reading a blog post that takes it from my practical FTW blog post to the docker world.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:25 UTC</span>

<span style="font-size: 90%;">This, _@csanders_!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:27 UTC</span>

<span style="font-size: 90%;">i should be allocating an hour every day now</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:34 UTC</span>

<span style="font-size: 90%;">to CRS</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:35 UTC</span>

<span style="font-size: 90%;">so</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:36 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:13:41 UTC</span>

<span style="font-size: 90%;">well ideally it wouldn't require going online to search for a blogpost. Ideally it's just a one-liner in the readme :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:42 UTC</span>

<span style="font-size: 90%;">shouldn't be an issue</span>

**csanders** <span style="color: grey; font-size: 90%;">19:13:50 UTC</span>

<span style="font-size: 90%;">it'll be in the readme :slightly_smiling_face:</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:13:55 UTC</span>

<span style="font-size: 90%;">(y)</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:14:06 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:22 UTC</span>

<span style="font-size: 90%;">Yes, it should definitely go into the readme. And then the blog post for the extended explanations.</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:22 UTC</span>

<span style="font-size: 90%;">oh yeah I would love this, I created a little bit of tooling for it and I’m sure many people had to do that</span>

**csanders** <span style="color: grey; font-size: 90%;">19:14:38 UTC</span>

<span style="font-size: 90%;">_@franbuehler_, sounds like some easy feedback for our perso :-P\</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:46 UTC</span>

<span style="font-size: 90%;">Any takers for such a blog post (ideally people who can spell dokker)?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:14:56 UTC</span>

<span style="font-size: 90%;">:joy:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:15:06 UTC</span>

<span style="font-size: 90%;">Allan, would you like to work with me on that</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:15:11 UTC</span>

<span style="font-size: 90%;">sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:18 UTC</span>

<span style="font-size: 90%;">Cool. Thank you guys!</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:22 UTC</span>

<span style="font-size: 90%;">awesome</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:15:25 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:29 UTC</span>

<span style="font-size: 90%;">And what do we do with the PR?</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:15:56 UTC</span>

<span style="font-size: 90%;">I'll press close on it for now</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:44 UTC</span>

<span style="font-size: 90%;">So that's settled. Great</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:19 UTC</span>

<span style="font-size: 90%;">Which leaves us with [#1445](https://github.com/coreruleset/coreruleset/issues/#1445), that is unfortunately on hold due to ModSec development. Has there been any update on that front?</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:29 UTC</span>

<span style="font-size: 90%;">no :neutral_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:17:39 UTC</span>

<span style="font-size: 90%;">:cry:</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:04 UTC</span>

<span style="font-size: 90%;">might be an unpopular opinion, but I think we should retain modsec 3 compatibility and mitigate for it by adding CRS to all our rules</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:23 UTC</span>

<span style="font-size: 90%;">if I’m correct, that will solve all the problems, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">Add a tga CRS?</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:30 UTC</span>

<span style="font-size: 90%;">yes add tag `CRS` to every of our rules</span>

**airween** <span style="color: grey; font-size: 90%;">19:18:38 UTC</span>

<span style="font-size: 90%;">(just see the PR's... there are so much request, and the latest one is almost a month old)</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:02 UTC</span>

<span style="font-size: 90%;">we really need *some* mechanism to remove our rules, for making exclusions</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:07 UTC</span>

<span style="font-size: 90%;">Sounds like the idea to overhaul all our tagging for 3.2. I kind of volunteered, but I am not getting anywhere.</span>

**airween** <span style="color: grey; font-size: 90%;">19:19:33 UTC</span>

<span style="font-size: 90%;">_we really need *some* mechanism to remove our rules, for making exclusions_ - I have an idea....</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:38 UTC</span>

<span style="font-size: 90%;">well I rather would have a small project :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:18 UTC</span>

<span style="font-size: 90%;">It's a relatively simple sed to add a CRS tag before the "ver" line.</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:01 UTC</span>

<span style="font-size: 90%;">I've made a parser, which parses CRS rules - I'm done with it. Now I will export the rules to YAML/JSON, and the next step will that I will load to an RDBMS. After that, we can export the rules by several aspects...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:22 UTC</span>

<span style="font-size: 90%;">Hear, hear ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:23 UTC</span>

<span style="font-size: 90%;">I wonder how many inconsistencies in our rules you will find :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:37 UTC</span>

<span style="font-size: 90%;">Not that many thanks to _@fgs_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:43 UTC</span>

<span style="font-size: 90%;">We have made huge progress.</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:46 UTC</span>

<span style="font-size: 90%;">that’s tru!</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:54 UTC</span>

<span style="font-size: 90%;">but, for example, we can normalize the TAGS, what the [#1445](https://github.com/coreruleset/coreruleset/issues/#1445) describes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:02 UTC</span>

<span style="font-size: 90%;">What do you mean by several aspects?</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:20 UTC</span>

<span style="font-size: 90%;">what do you mean the "inconsistencies"?</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:33 UTC</span>

<span style="font-size: 90%;">oh I mean just little things like forgotten tags etc</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:38 UTC</span>

<span style="font-size: 90%;">ah</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:39 UTC</span>

<span style="font-size: 90%;">Missing tags, actions in the wrong order, etc.</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:41 UTC</span>

<span style="font-size: 90%;">if you go round-trip you will see the diff :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">but that sounds like an awesome project</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">_@airween_: can we see the parser in action somewhere?</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:08 UTC</span>

<span style="font-size: 90%;">I think that this will not be revealed</span>

**airween** <span style="color: grey; font-size: 90%;">19:23:34 UTC</span>

<span style="font-size: 90%;">_@dune73_: not yet</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:49 UTC</span>

<span style="font-size: 90%;">I'm very eager to see it :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:57 UTC</span>

<span style="font-size: 90%;">Little presentation in Amsterdam?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:24:18 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:25:02 UTC</span>

<span style="font-size: 90%;">_What do you mean by several aspects?_ - eg: there are several differences between v2 and v3. For eg: the v3 adds an extra "\" char to every "\" char, but v2 strips it</span>

**airween** <span style="color: grey; font-size: 90%;">19:25:26 UTC</span>

<span style="font-size: 90%;">there are many rules which contains `@rx` op with some regex, which has no effect</span>

**airween** <span style="color: grey; font-size: 90%;">19:25:49 UTC</span>

<span style="font-size: 90%;">in the export step, you can choose, which export "style" you want</span>

**csanders** <span style="color: grey; font-size: 90%;">19:25:52 UTC</span>

<span style="font-size: 90%;">interesting</span>

**airween** <span style="color: grey; font-size: 90%;">19:25:53 UTC</span>

<span style="font-size: 90%;">v2 or v3...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:06 UTC</span>

<span style="font-size: 90%;">I see. An interesting additional option. _@Christian Treutler_ did you see that?</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:25 UTC</span>

<span style="font-size: 90%;">we can decrease the differences and incompabilities between two versions</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:54 UTC</span>

<span style="font-size: 90%;">Good, but to come back to our question, it seems we will need to add a CRS tag unless a miracle happens with the modsec development.</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:55 UTC</span>

<span style="font-size: 90%;">_Little presentation in Amsterdam?_ - you mean at the CRS meetup?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:03 UTC</span>

<span style="font-size: 90%;">Yes, _@airween_</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:10 UTC</span>

<span style="font-size: 90%;">may be</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:40 UTC</span>

<span style="font-size: 90%;">I'll continue to pester you. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:46 UTC</span>

<span style="font-size: 90%;">sorry, I don't see the reason of the new tag - what can it help to us?</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:46 UTC</span>

<span style="font-size: 90%;">would be very interesting!</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:11 UTC</span>

<span style="font-size: 90%;">well in modsec v2 there are two styles of ways to make exclusions (selectively deactivate our CRS rules)…. one that I like is `ctl:ruleRemoveTargetByTag=CRS` (this worked on modsec v2 as it did a regexp on the tags so it would catch any rule with a tag like ‘OWASP_CRS/WEB_ATTACK/NODEJS_INJECTION’). another option is  `ctl:ruleRemoveTargetById=900000;999999` to exclude our well-known range (but this is broken in modsec v3 as well)</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:25 UTC</span>

<span style="font-size: 90%;">with my tool, we can "refactorise" the tags for v3 (and v2 too)</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:08 UTC</span>

<span style="font-size: 90%;">_@walter_, the first example works in v3</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:28 UTC</span>

<span style="font-size: 90%;">oh, no, sorry :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:37 UTC</span>

<span style="font-size: 90%;">_@airween_ but in modsec v3, it’s an exact string match (maybe case in/sensitive, not sure)</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:44 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:51 UTC</span>

<span style="font-size: 90%;">so that is why we are considering just add the little `CRS` tag everywhere and the idiom works again</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:04 UTC</span>

<span style="font-size: 90%;">at least on the attack rules I mean</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:12 UTC</span>

<span style="font-size: 90%;">but we can "connect" the used tags with the remove actions - or not?</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">how do you mean?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">Refactorising is an interesting future option, but no immediate solution to a pressing problem that has to be solved before 3.2.</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:30 UTC</span>

<span style="font-size: 90%;">ok</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:47 UTC</span>

<span style="font-size: 90%;">I like _@walter_’s idea.</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:49 UTC</span>

<span style="font-size: 90%;">_@walter_ - we can discuss later :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:58 UTC</span>

<span style="font-size: 90%;">So who adds all that tags?</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:06 UTC</span>

<span style="font-size: 90%;">shall I do it?</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:20 UTC</span>

<span style="font-size: 90%;">how important is this?</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:37 UTC</span>

<span style="font-size: 90%;">I mean it would be a good test for my ugly tool above... :stuck_out_tongue:</span>

**fgs** <span style="color: grey; font-size: 90%;">19:32:54 UTC</span>

<span style="font-size: 90%;">Can we use `OWASP_CRS` instead of simply `CRS`?</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:56 UTC</span>

<span style="font-size: 90%;">it’s important for anyone who uses our (wordpress, drupal, ..) exclusion sets, because the exclusions are not applied, and you basically cannot run CRS on WordPress and other CMSes with modsec 3 :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:18 UTC</span>

<span style="font-size: 90%;">well that’s the next question :stuck_out_tongue: if we add tags, which one we choose</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:43 UTC</span>

<span style="font-size: 90%;">I agree with _@fgs_ on OWASP_CRS and I think _@airween_ is right, that it would be an interesting test case for his tool.</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:50 UTC</span>

<span style="font-size: 90%;">yes I agree</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:05 UTC</span>

<span style="font-size: 90%;">OWASP_CRS would do the job!</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">I can finish it at the end of August - is that enough?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:31 UTC</span>

<span style="font-size: 90%;">Your tool, or this PR with the new tag?</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:36 UTC</span>

<span style="font-size: 90%;">both</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:40 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:50 UTC</span>

<span style="font-size: 90%;">And we'll promote you to committer at the September community chat.</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:14 UTC</span>

<span style="font-size: 90%;">okay, the tool will be just beta version :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:41 UTC</span>

<span style="font-size: 90%;">Unfortunately, we can't do beta promotions. So it will have to be definite. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:59 UTC</span>

<span style="font-size: 90%;">the PR will done</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:07 UTC</span>

<span style="font-size: 90%;">Wonderful.</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:13 UTC</span>

<span style="font-size: 90%;">cool!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:17 UTC</span>

<span style="font-size: 90%;">So we are done with PRs and move on to the other stuff?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">Can we do a 3.2 release until September 25?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:56 UTC</span>

<span style="font-size: 90%;">That would mean an RC1 near the end of the month.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:38:22 UTC</span>

<span style="font-size: 90%;">I think we have enough stuff at this point</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:34 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">I’m up for it!</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:07 UTC</span>

<span style="font-size: 90%;">I’ll reserve some time for testing in production</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:23 UTC</span>

<span style="font-size: 90%;">Thanks. But I do not see much enthusiasm from the other people in the chat. Does that mean that it is welcome, but people prefer not having to work on it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:44 UTC</span>

<span style="font-size: 90%;">and I did offer to try to make the release by myself, as I think you and Chaim have done this, but I don’t yet fully know how to do it</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">so I’m offering to be the ‘release manager’ for this release</span>

**fgs** <span style="color: grey; font-size: 90%;">19:41:59 UTC</span>

<span style="font-size: 90%;">September 25th sounds good to me</span>

**fgs** <span style="color: grey; font-size: 90%;">19:42:18 UTC</span>

<span style="font-size: 90%;">(can’t remember when the last one was but hopefully that means ~6 months)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:42:48 UTC</span>

<span style="font-size: 90%;">or whatever was agreed last time :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:42:54 UTC</span>

<span style="font-size: 90%;">I think it's good to have a date and to work towards this date.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:54 UTC</span>

<span style="font-size: 90%;">We promised the next release for AppSecEU in 2019 and we're lucky it is late in the year.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:17 UTC</span>

<span style="font-size: 90%;">_@csanders_ did the 3.1 release, but I dare say it took a few months longer than we had planned for.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:35 UTC</span>

<span style="font-size: 90%;">that is very true</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:39 UTC</span>

<span style="font-size: 90%;">we ran into some bugs</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:47 UTC</span>

<span style="font-size: 90%;">if i recall</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:48 UTC</span>

<span style="font-size: 90%;">I'm very happy with @walter volunteering</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:00 UTC</span>

<span style="font-size: 90%;">that sounds like a plan</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:14 UTC</span>

<span style="font-size: 90%;">the docs are also really good on packing at this point</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:28 UTC</span>

<span style="font-size: 90%;">thanks to dune for that i belive</span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:32 UTC</span>

<span style="font-size: 90%;">from 3.0 time</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:47 UTC</span>

<span style="font-size: 90%;">True that. The release guide in the wiki should work.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:39 UTC</span>

<span style="font-size: 90%;">Will docker be in a releaseable state for 3.2-RC1 at the end of the month? I think this is very much a moving target AFAICS.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:57 UTC</span>

<span style="font-size: 90%;">It should be releasable now -- but we'll have the FTW change</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:02 UTC</span>

<span style="font-size: 90%;">and more to the point</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:06 UTC</span>

<span style="font-size: 90%;">the readme update</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:50 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:56 UTC</span>

<span style="font-size: 90%;">I did not work on this docker stuff anymore.
I think it's sad we don't support proxy and TLS in the default image...? But that is my personal opinion.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:10 UTC</span>

<span style="font-size: 90%;">that is something i intend to change</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:17 UTC</span>

<span style="font-size: 90%;">since its just a param update</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:18 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:20 UTC</span>

<span style="font-size: 90%;">But that's more of a nice to have, I think, is not it?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:47:34 UTC</span>

<span style="font-size: 90%;">cool!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:47 UTC</span>

<span style="font-size: 90%;">it should just be a matter of time ... it takes time to get those testing right, but shouldn't affect travis</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:52 UTC</span>

<span style="font-size: 90%;">so its not bad news:)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:17 UTC</span>

<span style="font-size: 90%;">the FTW change will change our travis deploy slightly but i don't think it should be bad -- i'llt ry and roll it all in at the same time</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:41 UTC</span>

<span style="font-size: 90%;">Cool, thanks _@csanders_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:10 UTC</span>

<span style="font-size: 90%;">_@walter_ is an RC1 on August 26, 3 weeks from now, viable? That would leave some time for RC2 and fixes...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:11 UTC</span>

<span style="font-size: 90%;">Thank you! I can help you, of course!</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:27 UTC</span>

<span style="font-size: 90%;">_@dune73_ I agree with you and I think we shouldn’t aim too much later</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:39 UTC</span>

<span style="font-size: 90%;">we should try to freeze around Aug 26 and then we have a month to do the needful</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">sounds like a plan!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:37 UTC</span>

<span style="font-size: 90%;">If you freeze on Aug 26, you'll need some time until RC1, don't you? So more like at the next community chat?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:53 UTC</span>

<span style="font-size: 90%;">and we'll be able to talk about it devops days _@franbuehler_</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:54 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:16 UTC</span>

<span style="font-size: 90%;">yes, _@csanders_:-)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:26 UTC</span>

<span style="font-size: 90%;">_@walter_: I'd like to fix an RC1 date, so we can really schedule it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:32 UTC</span>

<span style="font-size: 90%;">what about 26 aug RC1 — 8 sept RC2 — 24 sep release?</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:57 UTC</span>

<span style="font-size: 90%;">I’ve taken off the day of 24 anyway</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:04 UTC</span>

<span style="font-size: 90%;">That would be perfect. But can you freeze on the day as RC1?</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:07 UTC</span>

<span style="font-size: 90%;">I’ve taken the day off I mean :airplane_departure:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:12 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:56 UTC</span>

<span style="font-size: 90%;">how do you mean can you freeze?</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:32 UTC</span>

<span style="font-size: 90%;">or do you think we need some chat for open PRs</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:48 UTC</span>

<span style="font-size: 90%;">that might be smart right</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:53 UTC</span>

<span style="font-size: 90%;">If call a freeze on a given day, can you integrate the last merges into the changelog, documentation, RC1 release message etc. all on the same day. Or do you need a few days between the merge freeze and the RC1?</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:57 UTC</span>

<span style="font-size: 90%;">or, we decide now that we won’t accept any new PRs into 3.2 from this point</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:18 UTC</span>

<span style="font-size: 90%;">except those which are in progress (and we can always make an exception for urgent things)</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:43 UTC</span>

<span style="font-size: 90%;">oh like that… yeah let’s freeze one day early then :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:47 UTC</span>

<span style="font-size: 90%;">I think allowing merges until Aug 19 would be a smart thing and could speed up development. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:07 UTC</span>

<span style="font-size: 90%;">It would be cool to close some of the open issues with a PR...</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:47 UTC</span>

<span style="font-size: 90%;">thing is I don’t want to overwork _@airween_ too much if he is going to programmatically alter the rules, I think it’s quite ambitious, and maybe it will be ready only at the end of August</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:17 UTC</span>

<span style="font-size: 90%;">I’ve dabbed a bit in compiler construction and you can only really see some failures when you’re completely done</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:30 UTC</span>

<span style="font-size: 90%;">but… we can always use ssd :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:33 UTC</span>

<span style="font-size: 90%;">s e d</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:38 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:05 UTC</span>

<span style="font-size: 90%;">but alright you are right _@dune73_ let’s set a cut off date at Aug 19 for new contributions</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:11 UTC</span>

<span style="font-size: 90%;">if I can't do it with the tool, I'll do it with sed/awk/...</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:30 UTC</span>

<span style="font-size: 90%;">great, yes it’s good to  have that fallback option :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:41 UTC</span>

<span style="font-size: 90%;">OK. We agree on the release plan then. Thank you very much. I'm very happy we can work on this together for Amsterdam. :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:09 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:13 UTC</span>

<span style="font-size: 90%;">yeah we should have some good new stuff for people there :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:35 UTC</span>

<span style="font-size: 90%;">by the way, I’m still only running modsec 2 so if some of you could do some modsec 3 based testing that would be very valuable…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:48 UTC</span>

<span style="font-size: 90%;">Next one. Info:
The CapitalOne breach is said to be due to a misconfigured ModSecurity / CRS installation according to Brian Krebs. No additional infos so far, though.
And we can not really see how this could be possible.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:25 UTC</span>

<span style="font-size: 90%;">You did not receive an answer?</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:32 UTC</span>

<span style="font-size: 90%;">yeah I was puzzled about that! I saw your tweet</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:59 UTC</span>

<span style="font-size: 90%;">it’s sort of like blaming the doctor for your disease!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:04 UTC</span>

<span style="font-size: 90%;">No response. The same question was also in a comment on his blog.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:23 UTC</span>

<span style="font-size: 90%;">I think he has left out some information. Maybe ModSec running on an application server...</span>

**csanders** <span style="color: grey; font-size: 90%;">20:02:40 UTC</span>

<span style="font-size: 90%;">^^</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:44 UTC</span>

<span style="font-size: 90%;">But he sould reply...</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:20 UTC</span>

<span style="font-size: 90%;">maybe it was in `DetectionOnly` mode and the attack was trivial, i don’t know</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:20 UTC</span>

<span style="font-size: 90%;">*mutters under his breath about the state of security journalism*</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:29 UTC</span>

<span style="font-size: 90%;">Brian is a busy person ...</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:40 UTC</span>

<span style="font-size: 90%;">II do think we should add the metadata urls to our list</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:59 UTC</span>

<span style="font-size: 90%;">there is no legit use case for accessing them through a WAF that i can think of</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:12 UTC</span>

<span style="font-size: 90%;">in the same way we blacklist ../ -- we can add that badboy</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:14 UTC</span>

<span style="font-size: 90%;">Yes, that is an option.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:36 UTC</span>

<span style="font-size: 90%;">i will make the PR</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:40 UTC</span>

<span style="font-size: 90%;">find a good place for it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:54 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:35 UTC</span>

<span style="font-size: 90%;">The next topic was brought up by _@airween_. It's about JSON FPs...</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:45 UTC</span>

<span style="font-size: 90%;">yeah</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:55 UTC</span>

<span style="font-size: 90%;">I think this is a very bad news...</span>

**airween** <span style="color: grey; font-size: 90%;">20:07:31 UTC</span>

<span style="font-size: 90%;">and I just tough we can discuss about it here, may be somebody has some idea...</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:39 UTC</span>

<span style="font-size: 90%;">as I wrote the comment, all operators what works looking a string matches, doesn't work correctly on JSON arguments</span>

**airween** <span style="color: grey; font-size: 90%;">20:09:10 UTC</span>

<span style="font-size: 90%;">the question is: can we solve this on CRS side?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:53 UTC</span>

<span style="font-size: 90%;">Thats' really bad news, but complements that black JSON painting we talked about above.</span>

**airween** <span style="color: grey; font-size: 90%;">20:11:08 UTC</span>

<span style="font-size: 90%;">I thought _@csanders_ talked about this :stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:25 UTC</span>

<span style="font-size: 90%;">what exactly?</span>

**airween** <span style="color: grey; font-size: 90%;">20:11:32 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/issues/2136></span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:06 UTC</span>

<span style="font-size: 90%;">hmmm, i hadn't seen that ticket sppecfically</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:20 UTC</span>

<span style="font-size: 90%;">enough to read only this comment:
<https://github.com/SpiderLabs/ModSecurity/issues/2136#issuecomment-516384575></span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:39 UTC</span>

<span style="font-size: 90%;">urgh</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:44 UTC</span>

<span style="font-size: 90%;">yep</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:09 UTC</span>

<span style="font-size: 90%;">Yes. That bad.</span>

**airween** <span style="color: grey; font-size: 90%;">20:13:11 UTC</span>

<span style="font-size: 90%;">_refined JSON parsing support_ :stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:27 UTC</span>

<span style="font-size: 90%;">the JSON parsing support is kinda a mess</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:35 UTC</span>

<span style="font-size: 90%;">because it also relies on all elements being JSON</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:42 UTC</span>

<span style="font-size: 90%;">there is no way to run a single parameter though</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:21 UTC</span>

<span style="font-size: 90%;">This!</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:11 UTC</span>

<span style="font-size: 90%;">yeah :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:43 UTC</span>

<span style="font-size: 90%;">I do not think anybody has a quick solution in the back of his head.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:59 UTC</span>

<span style="font-size: 90%;">it would require massive rule additions</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:03 UTC</span>

<span style="font-size: 90%;">on the CRS side</span>

**airween** <span style="color: grey; font-size: 90%;">20:16:12 UTC</span>

<span style="font-size: 90%;">yeah, I think too... just good to know</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:15 UTC</span>

<span style="font-size: 90%;">Sometimes, I feel like we're constantly trying to work around ModSec shortcomings instead of adding great new rules.</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:24 UTC</span>

<span style="font-size: 90%;">it does take us a lot of time yeah</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:33 UTC</span>

<span style="font-size: 90%;">I wish that modsec would have some way to opportinistically parse what looks like json</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:40 UTC</span>

<span style="font-size: 90%;">that would also solve soooo many false positives</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:01 UTC</span>

<span style="font-size: 90%;">a large part of false positive alerts are JSON in parameters or cookies</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:12 UTC</span>

<span style="font-size: 90%;">oh man, that sounds like a security issue though</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:22 UTC</span>

<span style="font-size: 90%;">any time i hear opprotunistic parsing :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:23 UTC</span>

<span style="font-size: 90%;">why?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:32 UTC</span>

<span style="font-size: 90%;">although i guess it could go through and as soon as an error appears</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:34 UTC</span>

<span style="font-size: 90%;">haha yeah you are right, it could create a mechanism to hide payloads</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:36 UTC</span>

<span style="font-size: 90%;">it drops back</span>

**csanders** <span style="color: grey; font-size: 90%;">20:17:53 UTC</span>

<span style="font-size: 90%;">there are ways i think</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:17 UTC</span>

<span style="font-size: 90%;">but it is possible it would introduce a security issue where someone breaks up an XSS inside a JSON bit that wasn't supposed to be json</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:21 UTC</span>

<span style="font-size: 90%;">somehting strange like that</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:25 UTC</span>

<span style="font-size: 90%;">yes I can see that happening, exactly</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:49 UTC</span>

<span style="font-size: 90%;">It would be an interesting bypass path, yes.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:10 UTC</span>

<span style="font-size: 90%;">I don’t have an example off the top of my head but yes agreed</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:22 UTC</span>

<span style="font-size: 90%;">anyway it’s dreaming anyway</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:46 UTC</span>

<span style="font-size: 90%;">Yes, it is and I can't see how we can solve this ModSec issue in a reasonable manner.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:06 UTC</span>

<span style="font-size: 90%;">It's a bit depressing, but I think we need to move on.</span>

**airween** <span style="color: grey; font-size: 90%;">20:21:14 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:01 UTC</span>

<span style="font-size: 90%;">On the bright side, we have our swag show now and we already sold a sticker:  <https://www.redbubble.com/people/fzipi/collections/1148737-owasp-core-rule-set></span>

**walter** <span style="color: grey; font-size: 90%;">20:23:28 UTC</span>

<span style="font-size: 90%;">oh I love stickers</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:32 UTC</span>

<span style="font-size: 90%;">The problem, this is a huge collection of stuff people could order, but we need to add some sense and reason by adding some key items to our website.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:11 UTC</span>

<span style="font-size: 90%;">That sounds good</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:15 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ has organised the whole setup, btw. Very please with his evaluation of vendors. Redbubble is really very broad with their offering.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:24:35 UTC</span>

<span style="font-size: 90%;">Thank you, _@fzipitria_! cool stuff</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:38 UTC</span>

<span style="font-size: 90%;">Thanks. _@dune73_!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:54 UTC</span>

<span style="font-size: 90%;">And _@franbuehler_</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:54 UTC</span>

<span style="font-size: 90%;">lol the Acrylic Block</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:05 UTC</span>

<span style="font-size: 90%;">i’m actually loling out loud about that, maybe I’ll get it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:20 UTC</span>

<span style="font-size: 90%;">The round image is good for many things</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:51 UTC</span>

<span style="font-size: 90%;">I think we should distribute some stickers at AppSec too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:56 UTC</span>

<span style="font-size: 90%;">Who could work on this for our website?</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:10 UTC</span>

<span style="font-size: 90%;">is it really €2.51 per single sticker though???</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:19 UTC</span>

<span style="font-size: 90%;">I have like 200 stickers ordered on Stickermule. I'll certainly bring them to share.</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:35 UTC</span>

<span style="font-size: 90%;">you mean a little blog post advertising the shop? can try to do that</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:40 UTC</span>

<span style="font-size: 90%;">and add the shop to the menu? :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:43 UTC</span>

<span style="font-size: 90%;">Mine were more like 0.40 per sticker. Bulk order.</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">I did order stickers once, it was like €70 for 1000. (but don’t buy 1000 stickers, you’ll be left with 900 stickers after 5 years)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:05 UTC</span>

<span style="font-size: 90%;">Yes, adding the shop to the menu with a few prominent items. Ideally a blog.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:36 UTC</span>

<span style="font-size: 90%;">Problem: It is not really a dedicated shop on redbubble. More a selection of too many things...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:56 UTC</span>

<span style="font-size: 90%;">What we could also do is a bulk order for the team and have it delivered to the Netherlands. That would save a lot of P&P for everybody.</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:10 UTC</span>

<span style="font-size: 90%;">that makes sense!</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:21 UTC</span>

<span style="font-size: 90%;">we could gather them and I could bring it to the venue</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:29:33 UTC</span>

<span style="font-size: 90%;">Yes, _@dune73_!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:29:37 UTC</span>

<span style="font-size: 90%;">Good idea</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:29:56 UTC</span>

<span style="font-size: 90%;">I definitely want to buy some things :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:57 UTC</span>

<span style="font-size: 90%;">That would be very nice, _@walter_. Shall I set up a doodle, where people can enter the things that they want with the URL?</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:22 UTC</span>

<span style="font-size: 90%;">yes, please!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:30:38 UTC</span>

<span style="font-size: 90%;">yes, please</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:43 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: Is there an option to make our CRS 3 release poster printable via redbubble?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:50 UTC</span>

<span style="font-size: 90%;">OK. Noted.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:17 UTC</span>

<span style="font-size: 90%;">Good question. Will push for that.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:56 UTC</span>

<span style="font-size: 90%;">The only thing that gets me nervous is quality</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:57 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:32:07 UTC</span>

<span style="font-size: 90%;">sorry have to go. i must get up very early. cya</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:08 UTC</span>

<span style="font-size: 90%;">We'd need a test order.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:10 UTC</span>

<span style="font-size: 90%;">But for what I've heard it is good so far</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">So will ask for that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:26 UTC</span>

<span style="font-size: 90%;">Bye _@emphazer_, thanks for joining. Will you be in Amsterdam?</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:32:47 UTC</span>

<span style="font-size: 90%;">i will try to</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:32:55 UTC</span>

<span style="font-size: 90%;">bye bye</span>

**csanders** <span style="color: grey; font-size: 90%;">20:32:55 UTC</span>

<span style="font-size: 90%;">I unfortunatly cannot :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:09 UTC</span>

<span style="font-size: 90%;">we have some experience with print, if we’re going to order them to NL i can also have them printed here at a familiar print shop</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:11 UTC</span>

<span style="font-size: 90%;">Uh, oh. We'll miss you dearly, _@csanders_.</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:17 UTC</span>

<span style="font-size: 90%;">_@csanders_ noooo! that’s too bad</span>

**csanders** <span style="color: grey; font-size: 90%;">20:33:29 UTC</span>

<span style="font-size: 90%;">oh</span>

**csanders** <span style="color: grey; font-size: 90%;">20:33:42 UTC</span>

<span style="font-size: 90%;">not 100%</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:54 UTC</span>

<span style="font-size: 90%;">_@walter_: Printing is genereally not a problem. But I'd like to see an option where anybody can get a post easily via our website.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:39 UTC</span>

<span style="font-size: 90%;">So who will be in Amsterdam for the summit (in order to convince _@csanders_ to make it possible to join)?</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:00 UTC</span>

<span style="font-size: 90%;">meee</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:07 UTC</span>

<span style="font-size: 90%;">_@dune73_ agreed, would be nice</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:35:17 UTC</span>

<span style="font-size: 90%;">I think I will be there. But maybe only for our summit...</span>

**csanders** <span style="color: grey; font-size: 90%;">20:35:29 UTC</span>

<span style="font-size: 90%;">haha</span>

**csanders** <span style="color: grey; font-size: 90%;">20:36:03 UTC</span>

<span style="font-size: 90%;">i'm gonna see if i can swing it--ihave to be at Ekopart</span>

**csanders** <span style="color: grey; font-size: 90%;">20:36:06 UTC</span>

<span style="font-size: 90%;">for work</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:18 UTC</span>

<span style="font-size: 90%;">:disappointed:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:36:27 UTC</span>

<span style="font-size: 90%;">so amsterdam for a day and then argentina is a bit of a trip :confused:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:36:34 UTC</span>

<span style="font-size: 90%;">i'd prbably only be able to stay for like 5 hours</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:52 UTC</span>

<span style="font-size: 90%;">Amsterdam in 5 hours would be a bit of a record.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:37:08 UTC</span>

<span style="font-size: 90%;">haha, we'll see what i can do -- i already asaked my boss</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:15 UTC</span>

<span style="font-size: 90%;">We could move the summit to the airport, of course. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:37:23 UTC</span>

<span style="font-size: 90%;">Oh are going to ekoparty?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:37:24 UTC</span>

<span style="font-size: 90%;">haha</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:37:37 UTC</span>

<span style="font-size: 90%;">Didn't know _@csanders_</span>

**csanders** <span style="color: grey; font-size: 90%;">20:37:49 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">20:37:52 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ yup</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:02 UTC</span>

<span style="font-size: 90%;">I would have attended then</span>

**csanders** <span style="color: grey; font-size: 90%;">20:38:06 UTC</span>

<span style="font-size: 90%;">just found out a couple weeks ago</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:12 UTC</span>

<span style="font-size: 90%;">I've have so many friends there</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:14 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ and _@airween_ said they would be there. _@theMiddle_, you coming? How about you _@Christian Treutler_?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:38:40 UTC</span>

<span style="font-size: 90%;">well i'll hit you up before hand _@fzipitria_ and I can get an intro to the best 3 ;l)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:43 UTC</span>

<span style="font-size: 90%;">_@fgs_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:52 UTC</span>

<span style="font-size: 90%;">I can join you if you want to go from Amsterdam</span>

**csanders** <span style="color: grey; font-size: 90%;">20:39:06 UTC</span>

<span style="font-size: 90%;">i'll keep you updated</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:12 UTC</span>

<span style="font-size: 90%;">Sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:15 UTC</span>

<span style="font-size: 90%;">_@airween_ had this idea to rent an appartment for the team. We could probably safe money individually that way. But of course only if we fill it for the full duration (of the conference). otherwise it's too much of a hazzle.</span>

**airween** <span style="color: grey; font-size: 90%;">20:41:18 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:41:31 UTC</span>

<span style="font-size: 90%;">oof, that sounds amazing _@dune73_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:46 UTC</span>

<span style="font-size: 90%;">One more reason to really talk to your boss.</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:46 UTC</span>

<span style="font-size: 90%;">would not be a bad idea, hotel prices and availability in Amsterdam is horrible during high season</span>

**airween** <span style="color: grey; font-size: 90%;">20:41:48 UTC</span>

<span style="font-size: 90%;">I thought you reserve the rooms in same motel :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:41:54 UTC</span>

<span style="font-size: 90%;">haha</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:55 UTC</span>

<span style="font-size: 90%;">And think of the parties...</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:06 UTC</span>

<span style="font-size: 90%;">but it's better, well :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:24 UTC</span>

<span style="font-size: 90%;">_@airween_: Your message brought me to this idea. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:42:55 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:58 UTC</span>

<span style="font-size: 90%;">so, then it would be to know, who comes to the conf, and how many days for...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:26 UTC</span>

<span style="font-size: 90%;">I see options for 6 beds for Wed - Sat starting from 450 Euros...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:11 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: Have you booked a room already?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:17 UTC</span>

<span style="font-size: 90%;">If everyone is in, count me</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:21 UTC</span>

<span style="font-size: 90%;">If I can join you for 1 or 2 nights.... But if that is too complicated...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:23 UTC</span>

<span style="font-size: 90%;">Nope, don't have</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:44 UTC</span>

<span style="font-size: 90%;">When do you fly to Amsterdam, _@dune73_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:45 UTC</span>

<span style="font-size: 90%;">_@airween_: Are you interested to join?</span>

**airween** <span style="color: grey; font-size: 90%;">20:45:59 UTC</span>

<span style="font-size: 90%;">also for 1 or 2 days</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:18 UTC</span>

<span style="font-size: 90%;">Not sure, _@franbuehler_. Probably not flying. Rather night train if possible. Or car if it has to be.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:29 UTC</span>

<span style="font-size: 90%;">Ok...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:41 UTC</span>

<span style="font-size: 90%;">_@airween_: You are not staying for the full conference?</span>

**airween** <span style="color: grey; font-size: 90%;">20:46:50 UTC</span>

<span style="font-size: 90%;">I think I can't</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:47:10 UTC</span>

<span style="font-size: 90%;">Ok, I already had a look at night trains. But it's a bit complicated...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:47:20 UTC</span>

<span style="font-size: 90%;">Tell me, if you have a solution</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:49 UTC</span>

<span style="font-size: 90%;">OK. I'll check for the AirBnB option during the week. My experience is that it's cheaper to rent an appartment and to leave it half-empty than to book hotel rooms.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:11 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:47 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: Share a car? If we swap driving we could get it done, I guess. (I do not like to fly on the continent if it can be avoided)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:47 UTC</span>

<span style="font-size: 90%;">But whatever: Final piece of info before we close this session: I talked to Mitre about the CVEs, but their service is a bit disappointing. The guy stopped responding and I need to ping again.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:51:00 UTC</span>

<span style="font-size: 90%;">I will think about it...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:51:55 UTC</span>

<span style="font-size: 90%;">Thank you, _@dune73_ for talking to them...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:53:11 UTC</span>

<span style="font-size: 90%;">Bye bye, I am tired and have to go to bed now...</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:50 UTC</span>

<span style="font-size: 90%;">I also am almost asleep, thanks everyone :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:51 UTC</span>

<span style="font-size: 90%;">So let's call it a night. Thank you all for joining! And I'm really looking forward to the RC1!</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:02 UTC</span>

<span style="font-size: 90%;">it will be the best release eeeevaar!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:54:05 UTC</span>

<span style="font-size: 90%;">lol</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:54:11 UTC</span>

<span style="font-size: 90%;">Good night to everyone</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:14 UTC</span>

<span style="font-size: 90%;">good night!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:54:18 UTC</span>

<span style="font-size: 90%;">night all</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:54:22 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**airween** <span style="color: grey; font-size: 90%;">20:54:35 UTC</span>

<span style="font-size: 90%;">bye</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:29 UTC</span>

<span style="font-size: 90%;">Bye!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:12 UTC</span>

<span style="font-size: 90%;">New: I have added a "Decisions" comment to the agenda with all the things we decided. This should make things more transparent for the future and help with the memory.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:18 UTC</span>

<span style="font-size: 90%;">Bye everyone!</span>

**fgs** <span style="color: grey; font-size: 90%;">21:45:26 UTC</span>

<span style="font-size: 90%;">_@dune73_ I might go for the crs summit</span>

**fgs** <span style="color: grey; font-size: 90%;">21:45:38 UTC</span>

<span style="font-size: 90%;">I need to check. When it will take place?</span>

