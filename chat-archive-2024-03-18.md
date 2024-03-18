### Mon, Mar 18th, 2024

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">19:30:18 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:31 UTC</span>

<span style="font-size: 90%;">Hello everybody, time for the CRS meeting.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:40 UTC</span>

<span style="font-size: 90%;">Hi</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:46 UTC</span>

<span style="font-size: 90%;">Hey :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:21 UTC</span>

<span style="font-size: 90%;">Evening.</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:23 UTC</span>

<span style="font-size: 90%;">hi guys!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:16 UTC</span>

<span style="font-size: 90%;">We're probably a bit reduced tonight since a few people excuse themselves. And _@airween_ and _@fzipitria_ don't have much time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:22 UTC</span>

<span style="font-size: 90%;">So we better get going.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:33:35 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**jit** <span style="color: grey; font-size: 90%;">19:33:47 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">(Adding the numbers is a bit hard... 934140, for example, is a new rule in v4...)</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:34:18 UTC</span>

<span style="font-size: 90%;">Yes, but he named so many rules now ...</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">19:34:28 UTC</span>

<span style="font-size: 90%;">I think all these rules are new … at least for us.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:34:42 UTC</span>

<span style="font-size: 90%;">I've only seen the two from the security issue</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">19:35:08 UTC</span>

<span style="font-size: 90%;">934140, 942522 and 941400</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:01 UTC</span>

<span style="font-size: 90%;">We have two items on the agenda, formally.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:34 UTC</span>

<span style="font-size: 90%;">Both have the potential to delay our release.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:19 UTC</span>

<span style="font-size: 90%;">Let's attack the \v issue first.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:26 UTC</span>

<span style="font-size: 90%;">We just merged a PR that is meant to solve it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">Is this really over with this?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:51 UTC</span>

<span style="font-size: 90%;">Should be, according to _@airween_'s tests and my analysis</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:04 UTC</span>

<span style="font-size: 90%;">Very good.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:08 UTC</span>

<span style="font-size: 90%;">The issue actually only occurred because we put \v back into the expression</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:38 UTC</span>

<span style="font-size: 90%;">Could you briefly summarize the problem and the context. I tried to understand, but I failed and I think it would be worthwhile to have it in the minutes of our meeting.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:35 UTC</span>

<span style="font-size: 90%;">Sure</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:39 UTC</span>

<span style="font-size: 90%;">In Perl, \s does not include the verticle tab (VT). In PCRE (all versions) VT is included in \s.  RE2 (in Perl mode) is Perl compatible, which means it doesn't include VT in \s.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">In order to fix that, we modified the regular expressions we generate to include VT in \s , simply by adding \v. However, we failed to realize that \v actually expands to multiple code points.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:21 UTC</span>

<span style="font-size: 90%;">Now, in the old PCRE implementation, if you had a range like [\v-a], the range token - would simply be interpreted as a literal, so [\v\-a] , but silently (and depending on compilation options). PCRE2 does this better actually, and signals an error, which is what brought the issue to our attention.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:08 UTC</span>

<span style="font-size: 90%;">Since all we had originally wanted was to include VT, we've now changed the augmentation to include \x0b (VT) instead of \v, which is valid as range start.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:29 UTC</span>

<span style="font-size: 90%;">(done)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:47 UTC</span>

<span style="font-size: 90%;">Got you. The change in v4 was the thing I missed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">What I still don't get: How can \v be multiple code points in Unicode?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:52 UTC</span>

<span style="font-size: 90%;">\v expands to something like VT, FF, ...Those are all in ASCII</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:49 UTC</span>

<span style="font-size: 90%;">         U+000A     Linefeed (LF)
         U+000B     Vertical tab (VT)
         U+000C     Form feed (FF)
         U+000D     Carriage return (CR)
         U+0085     Next line (NEL)
         U+2028     Line separator
         U+2029     Paragraph separator</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:14 UTC</span>

<span style="font-size: 90%;">I see. Did not see this coming.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:23 UTC</span>

<span style="font-size: 90%;">Just like \s includes \t.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">Sure thing. I just did not think \v would be more than U+000B.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:08 UTC</span>

<span style="font-size: 90%;">Glad this is solved.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">Yes, that's what got me too. But that was my error, when I had introduced the change originally.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:53 UTC</span>

<span style="font-size: 90%;">For the record: I take it the CI/CD permission problems we had last week are solved too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:57 UTC</span>

<span style="font-size: 90%;">Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:27 UTC</span>

<span style="font-size: 90%;">Yes, but the changelog PR workflow doesn't fully work yet. I haven't had time to fix it yet.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:37 UTC</span>

<span style="font-size: 90%;">I'll let you know, when it's done</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:42 UTC</span>

<span style="font-size: 90%;">No rush. But thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:56 UTC</span>

<span style="font-size: 90%;">Good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:14 UTC</span>

<span style="font-size: 90%;">There is also a ModSec2 problem around that brings troubles for our docker container.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:24 UTC</span>

<span style="font-size: 90%;">_@airween_: Could you summarize that situation?</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:36 UTC</span>

<span style="font-size: 90%;">yes, I try</span>

**airween** <span style="color: grey; font-size: 90%;">19:50:30 UTC</span>

<span style="font-size: 90%;">mod_security2 (and libmodsecurity3) supports both pcre (old) and pcre2 (new) regex engines. You can decide which version you want to use in compilation time with --with-pcre2.</span>

**airween** <span style="color: grey; font-size: 90%;">19:51:07 UTC</span>

<span style="font-size: 90%;">In our CI/CD pipeline we use modsecurity-crs-docker container, which uses the old version.</span>

**airween** <span style="color: grey; font-size: 90%;">19:51:25 UTC</span>

<span style="font-size: 90%;">this is why this error wasn't caught</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:13 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ wanted to upgrade the docker container, but the stable (last released version old mod_secuirty2) has a bug - which is solved, but not released yet</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:32 UTC</span>

<span style="font-size: 90%;">that's it :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:08 UTC</span>

<span style="font-size: 90%;">Yup</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:11 UTC</span>

<span style="font-size: 90%;">Your explanation sure breaks down a huge debug session into an easy to digest chunk.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:23 UTC</span>

<span style="font-size: 90%;">Is someone taking down decision notes?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:41 UTC</span>

<span style="font-size: 90%;">No decisions yet, but happy to do so.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:14 UTC</span>

<span style="font-size: 90%;">Need to run for my class :runner:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:28 UTC</span>

<span style="font-size: 90%;">While we're at it: We also found out, that our nginx docker container does not log detection alerts in the error.log. This is because it runs on warn, but non-blocking rules are logged as info on nginx...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:38 UTC</span>

<span style="font-size: 90%;">And so far there is nothing we can do outside of running on info.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:04 UTC</span>

<span style="font-size: 90%;">The decision is taken by the webserver, not by ModSec...</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:19 UTC</span>

<span style="font-size: 90%;">in that issue the problem was that user didn't notice which version he uses exactly. I always grab the released v4.0.0 (by tag), not from v4.0/dev nor main branches.</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:46 UTC</span>

<span style="font-size: 90%;">I think the other problem is a derived issue</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:51 UTC</span>

<span style="font-size: 90%;">but more important :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:59 UTC</span>

<span style="font-size: 90%;">and the first one helped us</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:40 UTC</span>

<span style="font-size: 90%;">btw: now what is the expected way to contribute the rule set? Send PR's to main?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:59:33 UTC</span>

<span style="font-size: 90%;">Yes, main</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:56 UTC</span>

<span style="font-size: 90%;">?</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:58 UTC</span>

<span style="font-size: 90%;">and what about v4.0/dev and v4.0/main?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:19 UTC</span>

<span style="font-size: 90%;">Ah, I guess a branch cleanup would be helpful.</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:25 UTC</span>

<span style="font-size: 90%;">yeah'</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:39 UTC</span>

<span style="font-size: 90%;">OK, that much on these fronts. Anything to add or do we move to the ReDoS security issue that was discovered by _@Mirko Dziadzka_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:59:33 UTC</span>

<span style="font-size: 90%;">Yes, main</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:59:33 UTC</span>

<span style="font-size: 90%;">Yes, main</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:49 UTC</span>

<span style="font-size: 90%;">That does not seem to be the case. So let me give you the intro</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:44 UTC</span>

<span style="font-size: 90%;">_@Mirko Dziadzka_ reported a serious of mostly new rules that are under the suspicion of causing regular expression DoS (-> ReDoS).
This is always an issue for us, but here it seems to be aggrevated.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:01 UTC</span>

<span style="font-size: 90%;">We're tracking this as a security problem with the ID 3QA.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:04 UTC</span>

<span style="font-size: 90%;">The problem is the use of .* in many regular expressions.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:27 UTC</span>

<span style="font-size: 90%;">_@Mirko Dziadzka_ What I do not get so far: Is every .* affected and if not, why not?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:05:42 UTC</span>

<span style="font-size: 90%;">It depends … but mostly, yes. There is an implicit .* at the beginning of every regex because we use search in the regex. If you repeat the text between the implicit and the explicit .* in the input, there are multiple points to match it. When you then trigger backtracking, you get O(n^2) beheaviour. If you have multiple like in 941400 you get easily O(n^3) ….
Some regex engines handle this better than others, but as long as we use backtracking regex engines, this is a problem. re2 is probably not affected.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:06:34 UTC</span>

<span style="font-size: 90%;">In all this cases, you easily run into PCRE limits exceeded if this configured properly</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">For 934140 I did sent in a proposal on how to fix the regex.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:49 UTC</span>

<span style="font-size: 90%;">Thanks for that one.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:09:02 UTC</span>

<span style="font-size: 90%;">This will probably also work for 942522</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:07 UTC</span>

<span style="font-size: 90%;">We have .* in like 50+ rules. Do you think it is possible to address them all with this technique or some other one?
(let's postpone the question if we should for a few minutes)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:57 UTC</span>

<span style="font-size: 90%;">For the non-devs in the audience: We are tracking the issue and the conversation about the rules themselves in a private repo. Mirko's workaround / solution is archived there. It's one hell of a regex.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:20 UTC</span>

<span style="font-size: 90%;">We've used lookahead emulating expressions in other cases already, and we actually have a script to automate generation of such expressions.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:13:29 UTC</span>

<span style="font-size: 90%;">> Mirko’s workaround / solution is archived there. It’s one hell of a regex.
It is straight forward, Not sure how easy it is to generate the anchoring part. You have to express a negative constraint in a positive way.

pure PCRE would be probably a lot simpler. re2 propably does not have the problem.
As I mentioned, I only looked at this with python-re</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:15:26 UTC</span>

<span style="font-size: 90%;">What I think we need to do is to get a lay of the land. It's likely that _@Mirko Dziadzka_ has listed the worst ones but we don't really know about how many bad rules we're really talking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:39 UTC</span>

<span style="font-size: 90%;">True that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:15:54 UTC</span>

<span style="font-size: 90%;">Once we have a better picture, we can decide whether we want to fix a handful manually, or whether we need a more automated approach.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:12 UTC</span>

<span style="font-size: 90%;">I'd second that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:17 UTC</span>

<span style="font-size: 90%;">And, of course, as _@fzipitria_ proposed, we should detect ReDos in the CI pipeline.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:25 UTC</span>

<span style="font-size: 90%;">That would be cool.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:16:31 UTC</span>

<span style="font-size: 90%;">But hard.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:16:44 UTC</span>

<span style="font-size: 90%;">Does regexploit detect this issue? We used to use that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:16:54 UTC</span>

<span style="font-size: 90%;">No, unfortunately not.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:16:54 UTC</span>

<span style="font-size: 90%;">All these examples rely on looking at the regex and creating “bad” input.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:54 UTC</span>

<span style="font-size: 90%;">I think it only covers some cases.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:24 UTC</span>

<span style="font-size: 90%;">It could be a problem that might take some fuzzing.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:11 UTC</span>

<span style="font-size: 90%;">I think we can start with all unanchored expressions that include .* , look through those manually and try to classify them.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:45 UTC</span>

<span style="font-size: 90%;">Unless _@Mirko Dziadzka_ has already done that...?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:57 UTC</span>

<span style="font-size: 90%;">Now we are aware of the problem on PCRE, but PCRE match limits are a viable workaround for that problem and we suspect RE2 and friends are not affected. Also: We never hear of ReDoS aginst CRS in the wild.
So: How big is the problem really and do we need to spend resources on it?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:18:59 UTC</span>

<span style="font-size: 90%;">I stoped after the 3rd one …</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:52 UTC</span>

<span style="font-size: 90%;">But, from your experience, 3.3.5 seemed to be okayisch. So should we only look at new  rules in v4?</span>

**airween** <span style="color: grey; font-size: 90%;">20:19:55 UTC</span>

<span style="font-size: 90%;">[https://devina.io/redos-checker](https://devina.io/redos-checker) is a good tool, but it's an online tool and unfortunately I don't see any API</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:21:22 UTC</span>

<span style="font-size: 90%;">Well … /@\{.*\}"/ is vulnerable</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:21:43 UTC</span>

<span style="font-size: 90%;">yeah :slightly_smiling_face:</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:23:39 UTC</span>

<span style="font-size: 90%;">nice thing: it gives you the attack pattern … thanks for sharing</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:24:54 UTC</span>

<span style="font-size: 90%;">one more tool:
[https://github.com/2bdenny/ReScue](https://github.com/2bdenny/ReScue)

but [Devina.io](http://Devina.io) is better, I guess</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:47:13 UTC</span>

<span style="font-size: 90%;">_@airween_ It looks like it's this project, maybe?
[https://github.com/makenowjust-labs/recheck/tree/main](https://github.com/makenowjust-labs/recheck/tree/main)</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:47:43 UTC</span>

<span style="font-size: 90%;">I have no idea if it easily works solo without the website component (I don't do Scala).</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:20:09 UTC</span>

<span style="font-size: 90%;">The problem with PCRE match limits … it is hard to set them to the right value.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:10 UTC</span>

<span style="font-size: 90%;">There are more problems, I think, but ReDoS is also a big problem and it's not overly attractive to make our regexes even more complicated. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:54 UTC</span>

<span style="font-size: 90%;">I also wonder if it would not be a better investment to try and convince ModSecurity to release RE2 support.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:22:23 UTC</span>

<span style="font-size: 90%;">That would be great but we'll still have to support users of PCRE for a while....</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:22:39 UTC</span>

<span style="font-size: 90%;">and re2 is slower on average</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:22:51 UTC</span>

<span style="font-size: 90%;">But yes, it is the better engine.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:42 UTC</span>

<span style="font-size: 90%;">We have to support it, but I would be OK with supporting them with an upgrade path and a transparent communication there might be ReDoS lurking.
There is always DoS with a WAF anyways.</span>

**airween** <span style="color: grey; font-size: 90%;">20:23:46 UTC</span>

<span style="font-size: 90%;">there is a pending PR for libmodsecurity3 which implements RE2:
[https://github.com/owasp-modsecurity/ModSecurity/pull/2012](https://github.com/owasp-modsecurity/ModSecurity/pull/2012)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:55 UTC</span>

<span style="font-size: 90%;">I know.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:08 UTC</span>

<span style="font-size: 90%;">Nothing in sight for ModSec2 though, but this could be a reason to bring it on.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:36 UTC</span>

<span style="font-size: 90%;">Maybe we need to get an overview of the size of the newly found ReDoS problem first, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:49 UTC</span>

<span style="font-size: 90%;">Final question from my side. Is .*? also a problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:25:27 UTC</span>

<span style="font-size: 90%;">_@Mirko Dziadzka_ you are in a unique position. As a vendor, are you basically blocked at the moment from transitioning to v4?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:25:40 UTC</span>

<span style="font-size: 90%;">To the best of my knowledge, it is basically the same in the backtracking case. DOS is always the no-match case.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:08 UTC</span>

<span style="font-size: 90%;">So it is a problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:12 UTC</span>

<span style="font-size: 90%;">.*? Can even be worse, depending on the context.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:26:13 UTC</span>

<span style="font-size: 90%;">? only controls wich part you want in the match case.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:29 UTC</span>

<span style="font-size: 90%;">Yes, but I thought maybe ... :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:57 UTC</span>

<span style="font-size: 90%;">"/.*?/ is safe"

[https://devina.io/redos-checker](https://devina.io/redos-checker)</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:28:00 UTC</span>

<span style="font-size: 90%;">but .* too</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:28:22 UTC</span>

<span style="font-size: 90%;">then [Devina.io](http://Devina.io) is not the best :smile:</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:28:48 UTC</span>

<span style="font-size: 90%;">Difference between /.*.*/ and /.*x.*/</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:28:52 UTC</span>

<span style="font-size: 90%;">But it's correct. .* by itself isn't an issue.</span>

↳ **Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:29:38 UTC</span>

<span style="font-size: 90%;">What you need is .*? but with the semantic of “do not backtrack”</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:27:26 UTC</span>

<span style="font-size: 90%;">You need something like PCRE extensions like (*COMMIT) … for the Prolog programmers .. the same as a cut  operator.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:37 UTC</span>

<span style="font-size: 90%;">Yes, of course. I said CONTEXT :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:29 UTC</span>

<span style="font-size: 90%;">Now is this something we want to hold back 4.1.0 over? Or is it something we try to grind through step by step in coming months?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:29:42 UTC</span>

<span style="font-size: 90%;">_@Mirko Dziadzka_ you are in a unique position. As a vendor, are you basically blocked at the moment from transitioning to v4?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:30:13 UTC</span>

<span style="font-size: 90%;">We are thinking about this. Not yet decided.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:30:30 UTC</span>

<span style="font-size: 90%;">Maybe we only update part of the rules for now.</span>

**airween** <span style="color: grey; font-size: 90%;">20:30:47 UTC</span>

<span style="font-size: 90%;">once I chatted with one of the PCRE author (he is a Hungarian guy), he told me with this tool anyone can inspect the PCRE compatible regexes against redos

[https://github.com/zherczeg/repan](https://github.com/zherczeg/repan)

but I'm afraid it's not complete yet</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:20 UTC</span>

<span style="font-size: 90%;">sorry guys, I have to go</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:23 UTC</span>

<span style="font-size: 90%;">I don't think this blocks a release. Creating a release does not mean "we fixed all issues", just "we made some improvements"</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:11 UTC</span>

<span style="font-size: 90%;">Exactly my thinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:46 UTC</span>

<span style="font-size: 90%;">_@Mirko Dziadzka_ what do you think about the right approach to this ReDoS problem?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:35:05 UTC</span>

<span style="font-size: 90%;">This is a good question.  All of the below ….
1: Having a tool which reports the problem
2: look at the worst offenders.
3: see if we can change some of these regexes automatically
4: rely on PCRE_MATCH_LIMIT
5: change to re2 and friends</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:27 UTC</span>

<span style="font-size: 90%;">That's a good list.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:31 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:16 UTC</span>

<span style="font-size: 90%;">Everything outside of item 4 is very complex, though. But who does not like a good challenge from time to time. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:38 UTC</span>

<span style="font-size: 90%;">So thank you for reporting and we'll see how we can address this adequately.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:14 UTC</span>

<span style="font-size: 90%;">Are there any other topics we want to address tonight?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:40 UTC</span>

<span style="font-size: 90%;">Guess not. :slightly_smiling_face:
Thank you all for attending and the good conversations. I learnt a thing or two in this meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:48 UTC</span>

<span style="font-size: 90%;">Bye bye</span>

**jit** <span style="color: grey; font-size: 90%;">20:39:04 UTC</span>

<span style="font-size: 90%;">Goodnight everyone</span>

**jit** <span style="color: grey; font-size: 90%;">20:39:42 UTC</span>

<span style="font-size: 90%;">Next time the meeting will be one hour early :slightly_smiling_face:</span>

