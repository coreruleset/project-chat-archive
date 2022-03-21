### Mon, Dec 6th, 2021

**dune73** <span style="color: grey; font-size: 90%;">19:31:10 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_ You effectively want to rebase on origin's HEAD?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">Hello everybody, time for our monthly CRS chat!</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:31:35 UTC</span>

<span style="font-size: 90%;">Hello !</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:35 UTC</span>

<span style="font-size: 90%;">hello!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:38 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:42 UTC</span>

<span style="font-size: 90%;">Please find the agenda at [https://github.com/coreruleset/coreruleset/issues/2291](https://github.com/coreruleset/coreruleset/issues/2291)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:44 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**studersi** <span style="color: grey; font-size: 90%;">19:31:45 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:31:56 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">Hello, hello. So nice to see so many people here. Hello _@studersi_ and _@jptosso_. Glad you made it too.</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:00 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:00 UTC</span>

<span style="font-size: 90%;">This is going to be a cool CRS week, since we plan to release the sandbox on Thursday - and we're almost there!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:12 UTC</span>

<span style="font-size: 90%;">Draft announcement already done.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:24 UTC</span>

<span style="font-size: 90%;">And I wrote to some journalists today as well.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:33:45 UTC</span>

<span style="font-size: 90%;">Hi, sorry friends, i don't feel well, i need to go to the bed. Good night!</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">take care!</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:34:43 UTC</span>

<span style="font-size: 90%;">Get well soon!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:54 UTC</span>

<span style="font-size: 90%;">Get better</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:06 UTC</span>

<span style="font-size: 90%;">Hello</span>

**airween** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">take care!</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">take care!</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:34:43 UTC</span>

<span style="font-size: 90%;">Get well soon!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:32 UTC</span>

<span style="font-size: 90%;">Good, then let's get started.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:34:37 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:16 UTC</span>

<span style="font-size: 90%;">So there have been a couple of blog posts around CRS, namely one from dutch ISP [slik.nl](http://slik.nl) (-> _@walter_)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:21 UTC</span>

<span style="font-size: 90%;">You find the links in the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:02 UTC</span>

<span style="font-size: 90%;">CRS dev-on-duty has been expanded to twitter as well and all dev-on-duty payments have been initiated at OWASP, looking forward to the payment in December.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:41 UTC</span>

<span style="font-size: 90%;">And then - just to make sure everybody hears this - Trustwave has officially rejected OWASP's / our proposal to hand over the EOL ModSecurity to OWASP.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:13 UTC</span>

<span style="font-size: 90%;">It looks like we have exhausted all options on that front and we think about setting our sails for more promising shores. More about that soon.</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:05 UTC</span>

<span style="font-size: 90%;">Yes. We wrote a little note to Ziv to explain the bad situation of ModSec, the clock that is ticking, and the needed investments, but no detailed reply so far. I guess it’s a done deal for them but I’ll give it 2% chance that they might reconsider.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:01 UTC</span>

<span style="font-size: 90%;">Looking at the PRs we merged, we kept up the momentum after the dev retreat and merged 31 PRs since early November, which is really impressive.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:27 UTC</span>

<span style="font-size: 90%;">Time for the open PRs, then.
[#2323](https://github.com/coreruleset/coreruleset/issues/#2323) is stuck with failing tests and it seems azurit is a bit at a loss. Could somebody cast an eye on this regex problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:13 UTC</span>

<span style="font-size: 90%;">I can do that</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:44 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:52 UTC</span>

<span style="font-size: 90%;">[#2300](https://github.com/coreruleset/coreruleset/issues/#2300) is meant as a regex simplification, but I do not get it. Am I wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:09 UTC</span>

<span style="font-size: 90%;">This looks like an invitation for FPs to me. See my final comment.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:36 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ is probably stuck in his car, but maybe somebody can point out where the problem is.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:57 UTC</span>

<span style="font-size: 90%;">I can take a look there too</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:23 UTC</span>

<span style="font-size: 90%;">great!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:41 UTC</span>

<span style="font-size: 90%;">You're most welcome _@maxleske_! Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:06 UTC</span>

<span style="font-size: 90%;">[#2299](https://github.com/coreruleset/coreruleset/issues/#2299) just needs an additional review and then it's time to merge.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:06 UTC</span>

<span style="font-size: 90%;">Hey all!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:36 UTC</span>

<span style="font-size: 90%;">Any volunteers for [#2299](https://github.com/coreruleset/coreruleset/issues/#2299) (outside _@maxleske_)?</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:19 UTC</span>

<span style="font-size: 90%;">I can do that, but I have still too many on my plate… but I have a test phpBB installed for this purpose so I can take it</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:38 UTC</span>

<span style="font-size: 90%;">I’ll take it!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:42 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:07 UTC</span>

<span style="font-size: 90%;">[#2290](https://github.com/coreruleset/coreruleset/issues/#2290) _@SpartanTri_ needs a bit of support with git here. Afterwards it seems good to go. _@fzipitria_ could you give him a hand?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:18 UTC</span>

<span style="font-size: 90%;">Sure</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:46 UTC</span>

<span style="font-size: 90%;">Ah, and I see that _@maxleske_ was waiting for reviewing too. Sorry, did not mean to interfere.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:02 UTC</span>

<span style="font-size: 90%;">But with both of you on the PR this should be solvable.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:55 UTC</span>

<span style="font-size: 90%;">I'll take [#2288](https://github.com/coreruleset/coreruleset/issues/#2288), since this is a script that I originally wrote. And thanks to a quick poll we now know, that everybody wants to have _- and the end of a regex character class.</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:09 UTC</span>

<span style="font-size: 90%;">yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:21 UTC</span>

<span style="font-size: 90%;">[#2259](https://github.com/coreruleset/coreruleset/issues/#2259) is not quite ready, but I think we need to talk this through quickly.</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:50 UTC</span>

<span style="font-size: 90%;">about creating a SSRF separate category?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:03 UTC</span>

<span style="font-size: 90%;">The question is whether we wand a separate ssrf_score - and a separate rules file for SSRF (possibly including request smuggling too).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:22 UTC</span>

<span style="font-size: 90%;">What do you all think?</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:49 UTC</span>

<span style="font-size: 90%;">it could be argued that it’s a variant of a local file inclusion - so could be under the LFI classification</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:02 UTC</span>

<span style="font-size: 90%;">I would rather not expand the categories too much…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:04 UTC</span>

<span style="font-size: 90%;">Is it, though?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:10 UTC</span>

<span style="font-size: 90%;">Or generic attack rules?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:41 UTC</span>

<span style="font-size: 90%;">[https://capec.mitre.org/data/definitions/664.html](https://capec.mitre.org/data/definitions/664.html) points to authentication bypass</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:55 UTC</span>

<span style="font-size: 90%;">I am also inclined to keep the categories (and rename the node attacks to generic).</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:28 UTC</span>

<span style="font-size: 90%;">a generic category would not be bad for me as a user</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:31 UTC</span>

<span style="font-size: 90%;">It makes sense to me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:43 UTC</span>

<span style="font-size: 90%;">And if things grow a lot, then we split</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:50 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:55 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:14 UTC</span>

<span style="font-size: 90%;">That's actually PR [#2163](https://github.com/coreruleset/coreruleset/issues/#2163).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:34 UTC</span>

<span style="font-size: 90%;">Yes, we are way behind in merging that one</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:42 UTC</span>

<span style="font-size: 90%;">And 2259 could fit into that new rules file.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:17 UTC</span>

<span style="font-size: 90%;">PR is an unfortunate case and it seems only _@airween_ can still help us there.</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:41 UTC</span>

<span style="font-size: 90%;">in 2259?</span>

**airween** <span style="color: grey; font-size: 90%;">19:55:55 UTC</span>

<span style="font-size: 90%;">oh, in 2163?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:01 UTC</span>

<span style="font-size: 90%;">But let's say that we need to merge that with a higher priority, so it becomes unstuck and we can then shift 2259 into said new category.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:07 UTC</span>

<span style="font-size: 90%;">_@airween_ yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:39 UTC</span>

<span style="font-size: 90%;">Can you look into these failed tests and shepherd the PR 2163 to merging, please?</span>

**airween** <span style="color: grey; font-size: 90%;">19:57:14 UTC</span>

<span style="font-size: 90%;">yes, I started to review that PR, but haven't found any solution yet... I need few days</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:04 UTC</span>

<span style="font-size: 90%;">I see. Can you tell us what the problem is? The tests are failing is all I know.</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:04 UTC</span>

<span style="font-size: 90%;">I assigned it to me</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:11 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:20 UTC</span>

<span style="font-size: 90%;">I don't know yet what's the problem. May be the FULL_REQUEST is in some encoded form... I've tried to turn on the REQUEST_BODY in previous phase, but still no luck</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:40 UTC</span>

<span style="font-size: 90%;">I have to debug it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:07 UTC</span>

<span style="font-size: 90%;">We can try to use encoded_request instead, that’s the line we were talking previous to this chat</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:23 UTC</span>

<span style="font-size: 90%;">Good thinking.</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:41 UTC</span>

<span style="font-size: 90%;">I'll check out that too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:43 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ you'll continue to be around of 2163, too?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:34 UTC</span>

<span style="font-size: 90%;">I guess he's left the chat to bury himself in the code. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:50 UTC</span>

<span style="font-size: 90%;">[#2236](https://github.com/coreruleset/coreruleset/issues/#2236) This is about a new test script by _@airween_ that checks rules and their format. The script is also meant to be added to our linting. I am not entirely sure about the status of the PR, though.</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:55 UTC</span>

<span style="font-size: 90%;">I will keep in touch with _@fzipitria_</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:12 UTC</span>

<span style="font-size: 90%;">this PR is also done</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:17 UTC</span>

<span style="font-size: 90%;">2236</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:45 UTC</span>

<span style="font-size: 90%;">please take a look to TODO.txt:
[https://github.com/coreruleset/coreruleset/pull/2236/files#diff-0e82ecf85a0fab5af3e583e9142731d73077cee9760502c4198e2fb956b6d28a](https://github.com/coreruleset/coreruleset/pull/2236/files#diff-0e82ecf85a0fab5af3e583e9142731d73077cee9760502c4198e2fb956b6d28a)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:51 UTC</span>

<span style="font-size: 90%;">So ready to be merged?</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:01 UTC</span>

<span style="font-size: 90%;">yes, it is</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:41 UTC</span>

<span style="font-size: 90%;">Any volunteers to check this out and review it?</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:42 UTC</span>

<span style="font-size: 90%;">so the TODO contains few other ideas what we can check too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:59 UTC</span>

<span style="font-size: 90%;">Maybe open issues for the TODOs if you think they are important.</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:10 UTC</span>

<span style="font-size: 90%;">I can add them later</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:31 UTC</span>

<span style="font-size: 90%;">So [#2236](https://github.com/coreruleset/coreruleset/issues/#2236) is ready for a review. _@Paul Beckett_ would you have time for this? I always get the feeling you have a strong operational view on scripts and unearth a lot of edge cases...</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:07:08 UTC</span>

<span style="font-size: 90%;">Happy to review [#2236](https://github.com/coreruleset/coreruleset/issues/#2236)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:18 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:23 UTC</span>

<span style="font-size: 90%;">[#2222](https://github.com/coreruleset/coreruleset/issues/#2222) is probably better addressed by a plugin. I'm scheduling a separate call with azurit to talk about some open questions around plugins this week, so we'll discuss that there as well.</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:22 UTC</span>

<span style="font-size: 90%;">that would be awesome</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:26 UTC</span>

<span style="font-size: 90%;">Time for [#2214](https://github.com/coreruleset/coreruleset/issues/#2214). I'm afraid I lost touch with this PR and what it does a bit. theMiddle is not here, so could somebody enlighten me?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:51 UTC</span>

<span style="font-size: 90%;">_@walter_ Azurit has some issues with the plugin format and I need to talk this through with him.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:34 UTC</span>

<span style="font-size: 90%;">[#2214](https://github.com/coreruleset/coreruleset/issues/#2214) was about an issue discussed in the dev channel? (Edited.)</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:39 UTC</span>

<span style="font-size: 90%;">That is solved now?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:49 UTC</span>

<span style="font-size: 90%;">Or were there other issues after the backslash issue?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:10:15 UTC</span>

<span style="font-size: 90%;">The backslash issue looks like something for [\\\\]</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:31 UTC</span>

<span style="font-size: 90%;">_@maxleske_ thought about that too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:28 UTC</span>

<span style="font-size: 90%;">Maybe we need to wait until theMiddle has finished moving his stuff to Torino...</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:53 UTC</span>

<span style="font-size: 90%;">yeah, let’s wait for his comment on this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:13 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:23 UTC</span>

<span style="font-size: 90%;">Final PR for tonight: [#2193](https://github.com/coreruleset/coreruleset/issues/#2193) It looks like _@maxleske_ is done with his new wrapper script for the msc_pyparser library / framework. _@airween_: Do you think it's ready to be merged?</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:46 UTC</span>

<span style="font-size: 90%;">lots of improvements have gone into this :+1:</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:50 UTC</span>

<span style="font-size: 90%;">yes, I think that's a very good job, congrats for it guys</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:07 UTC</span>

<span style="font-size: 90%;">:clap: :clap:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:11 UTC</span>

<span style="font-size: 90%;">It's all thanks to you and _@maxleske_ for the script!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:28 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ actually wrote it</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:35 UTC</span>

<span style="font-size: 90%;">I just refactored it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:35 UTC</span>

<span style="font-size: 90%;">True!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:47 UTC</span>

<span style="font-size: 90%;">Almost forgot about that, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:02 UTC</span>

<span style="font-size: 90%;">So it's a great team of 3 then!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:16 UTC</span>

<span style="font-size: 90%;">_@airween_ please feel free to merge</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:22 UTC</span>

<span style="font-size: 90%;">right</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:30 UTC</span>

<span style="font-size: 90%;">Good. Then let's move on to the open status of projects and open discussions.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:47 UTC</span>

<span style="font-size: 90%;">Sandbox: _@fzipitria_ do you have time to give us a brief status?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:24 UTC</span>

<span style="font-size: 90%;">Seems busy again.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:37 UTC</span>

<span style="font-size: 90%;">So here we go: The Sandbox is working and almost ready for prime time on Thursday.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:17:44 UTC</span>

<span style="font-size: 90%;">Here I am</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:54 UTC</span>

<span style="font-size: 90%;">Some open issues remain. The biggest one is logging / log archiving.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:17:55 UTC</span>

<span style="font-size: 90%;">:rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:22 UTC</span>

<span style="font-size: 90%;">And I would like to have 1-2 smaller issues fixed. But ultimately no real showstoppers around.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:18:28 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:37 UTC</span>

<span style="font-size: 90%;">The problem is now that almost only _@fzipitria_ is around to work on it this week.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:41 UTC</span>

<span style="font-size: 90%;">And he's busy too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:01 UTC</span>

<span style="font-size: 90%;">But we’ll deliver</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:09 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ what happens if we release without the log archiving?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:02 UTC</span>

<span style="font-size: 90%;">We can live with manual interactions until we fix it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:21 UTC</span>

<span style="font-size: 90%;">Meaning we take the logs out and then we process them</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:48 UTC</span>

<span style="font-size: 90%;">Cool. That seems doable.
And the "red carpet" can be done in time?</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:21:04 UTC</span>

<span style="font-size: 90%;">logs are being deleted right now</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:14 UTC</span>

<span style="font-size: 90%;">Oops</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:21 UTC</span>

<span style="font-size: 90%;">We should fix that :thinking_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:26 UTC</span>

<span style="font-size: 90%;">I'd like to get this ready for the release. The rest are minor bugs from my point of view.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:39 UTC</span>

<span style="font-size: 90%;">_@jptosso_ can you give a hand on the sandbox this week?</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:21:47 UTC</span>

<span style="font-size: 90%;">In case we keep de modsec_audit.log we should also add some log rotation</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:21:55 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:02 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:25 UTC</span>

<span style="font-size: 90%;">We're really a bit thin in that sub-project right now... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:42 UTC</span>

<span style="font-size: 90%;">Good. Let's move on to the status page, then.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:19 UTC</span>

<span style="font-size: 90%;">There is litterally no update. No response from OWASP about the credit card / cloud provider accounts question and we have not really looked into expanding go-ftw as a base for the status page yet.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:31 UTC</span>

<span style="font-size: 90%;">_@xanadu_ can you tell us anything about the plugins?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:24:19 UTC</span>

<span style="font-size: 90%;">Sure. I finished proofreading _@dune73_'s upcoming blog post about plugins this afternoon. Hopefully it can go live this week or next week, and then I'll import it into the new documentation system, too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:59 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:27 UTC</span>

<span style="font-size: 90%;">Azurit also had some comments. And _@xanadu_'s FP documentation is also almost done.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:40 UTC</span>

<span style="font-size: 90%;">How much more on the basic set of documentation?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:18 UTC</span>

<span style="font-size: 90%;">Simple PR [#2325](https://github.com/coreruleset/coreruleset/issues/#2325) came in during the meeting. Anybody want to quickly review and merge this?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:04 UTC</span>

<span style="font-size: 90%;">Anomaly Scoring is 95% complete. I need to add a section about Early Blocking Mode and then it is done.
False Positives and Tuning is now finished, I think, pending a re-review from _@dune73_ I think to check the final amendments.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:42 UTC</span>

<span style="font-size: 90%;">i can do [#2325](https://github.com/coreruleset/coreruleset/issues/#2325)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:50 UTC</span>

<span style="font-size: 90%;">I met a security officer last week and told her we now have a technical author in the CRS team and he was very jealous. It's a rare project to have a professional technical writer willing to do even more technical writing in his spare time.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:17 UTC</span>

<span style="font-size: 90%;">We've covered the "what is CRS" and we're writing a lot of "how does CRS work", but it would be good if someone would like to help write the "where is the CRS" content. Specifically:
:large_orange_square: Various Engine options
:large_orange_square: Various existing integrations in cloud and CDNs (-> touches on the "status page" idea as well)
those two topics.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:24 UTC</span>

<span style="font-size: 90%;">It kind of touches on the status page a little bit, too.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:28:34 UTC</span>

<span style="font-size: 90%;">Basically, if someone would like to list all the places CRS can be found</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:03 UTC</span>

<span style="font-size: 90%;">I think _@dune73_ has a good picture of that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:09 UTC</span>

<span style="font-size: 90%;">I reckon I have the most comprehensive list of CRS integrations.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:27 UTC</span>

<span style="font-size: 90%;">The same for the engines, actually.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:54 UTC</span>

<span style="font-size: 90%;">And it's probably time to share that knowledge with the wider public. Also in light of ModSec's EOL.</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:10 UTC</span>

<span style="font-size: 90%;">yes, that would be a very good signal to give off now</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:30:16 UTC</span>

<span style="font-size: 90%;">Maybe the ModSecurity section is just a picture of the Titanic sinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:01 UTC</span>

<span style="font-size: 90%;">The Titanic was a modern ship. I think we could make it a heavy Spanish Galeon.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:13 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:40 UTC</span>

<span style="font-size: 90%;">What's left for basic documentation afterwards, _@xanadu_?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:33:19 UTC</span>

<span style="font-size: 90%;">Possibly some content on Sampling Mode, probably a Developer Info page to bring together a lot of different pieces of information, and some sort of operational content.

At the Dev retreat we said we wanted to write:
:o: Basic operation
:o: Detailed practical operation
but it's not 100% clear what we wanted to write for those.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:33:38 UTC</span>

<span style="font-size: 90%;">Or we might just link to netnea for now for some of that.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:44 UTC</span>

<span style="font-size: 90%;">Sampling mode: Feel free to refactor my sampling mode blog post from [netnea.com](http://netnea.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:28 UTC</span>

<span style="font-size: 90%;">The operation part would warrant a separate discussion. I suggest we finish the rest and then look into that together with those interested.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:34:42 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:12 UTC</span>

<span style="font-size: 90%;">Good. 2 more topics to go. Sorry, _@walter_ but 60minute meetings are really tough. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:47 UTC</span>

<span style="font-size: 90%;">we’re doing good :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:13 UTC</span>

<span style="font-size: 90%;">We need to agree how to encode baskslashes in our rules. It seems there are two ways to do this. But which one do we prefer. Can we make this decision or does it take more time to weigh the PROs and CONs?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:37:09 UTC</span>

<span style="font-size: 90%;">I prefer \x5c ..... I find [\\\\] very confusing, and not really certain why that's required.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:14 UTC</span>

<span style="font-size: 90%;">I thought we had already decided after _@xanadu_’s excellent analysis?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:37:40 UTC</span>

<span style="font-size: 90%;">Yes, but afterwards I realised that several rules already use \x5c :weary:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:37:45 UTC</span>

<span style="font-size: 90%;">So we have 2 methods in use right now.</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:58 UTC</span>

<span style="font-size: 90%;">I like \x5c too. But that’s just bikeshedding, I must admit I haven’t looked into it deeply.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:38:21 UTC</span>

<span style="font-size: 90%;">I think \x5c plays nicely with regexp-assemble.py, while [\\\\] does not.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:33 UTC</span>

<span style="font-size: 90%;">Another reason good for me</span>

**airween** <span style="color: grey; font-size: 90%;">20:38:39 UTC</span>

<span style="font-size: 90%;">I prefer [\\\\], because when I look at the rule I can realize that there is an double escape sequence, but the \x5c is just a hieroglyph</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:42 UTC</span>

<span style="font-size: 90%;">In that case I actually also prefer \x5c. It makes more sense to the uninitiated.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:56 UTC</span>

<span style="font-size: 90%;">What about Coraza _@jptosso_?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:05 UTC</span>

<span style="font-size: 90%;">Valid point _@xanadu_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:23 UTC</span>

<span style="font-size: 90%;">I think \x5c will play better will all engines</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:39:26 UTC</span>

<span style="font-size: 90%;">For coraza it’s double escaping and it fails, I have to manually replace them</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:28 UTC</span>

<span style="font-size: 90%;">Just a heads up: I have plans to add a substitution mechanism to the regex files that would allow insertion of repeated sequences. Then we could properly document whatever we put in there.</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:39:35 UTC</span>

<span style="font-size: 90%;">\x5c works better</span>

**airween** <span style="color: grey; font-size: 90%;">20:39:48 UTC</span>

<span style="font-size: 90%;">if regexp-assemble.py supports only the \x5c, then there is no question - am I right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:00 UTC</span>

<span style="font-size: 90%;">And coraza’s compatibility</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:40:29 UTC</span>

<span style="font-size: 90%;">I agree with _@airween_ that \x5c looks much more odd, but I think we will simply have to document it very clearly, why we use it, and where/when to use it.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:40:47 UTC</span>

<span style="font-size: 90%;">And make sure everyone knows and understands it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:03 UTC</span>

<span style="font-size: 90%;">Would such an explanation go into CONTIRBUTING.md?</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:07 UTC</span>

<span style="font-size: 90%;">can we lint on it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:42:02 UTC</span>

<span style="font-size: 90%;">I thinks that [\\\\] would also need to be documented, so it's not that big a difference</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:11 UTC</span>

<span style="font-size: 90%;">can be for later. but i think we have a strong consensus now for going forward with \x5c</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:11 UTC</span>

<span style="font-size: 90%;">well, if we decide it I can add a test for [CRS rules check](https://github.com/coreruleset/coreruleset/pull/2236#) script which can check that there is no such \\, and [\\\\] in any @rx argument</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:38 UTC</span>

<span style="font-size: 90%;">Very good. So that's decided then.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:48 UTC</span>

<span style="font-size: 90%;">Moving on to the final topic for tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:35 UTC</span>

<span style="font-size: 90%;">_@studersi_ took a very close look at the use of various anomaly scoring variables and what he saw goes way beyond my worst fears: It's one big mess.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:53 UTC</span>

<span style="font-size: 90%;">So it's pretty clear we need to do something about this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:05 UTC</span>

<span style="font-size: 90%;">_@studersi_ has provided quite a detailed proposal to address the issue. This has found wide acclaim. But also some criticism.
I share some of the concerns too.
What I find difficult is the desire to go with a minimal set of variables and still be elegant and logical.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:53 UTC</span>

<span style="font-size: 90%;">And the ideas by Simon don't cover the 980xxx rules really and I think they should be cleaned up too. Also because the behaviour on ModSec 2 / 3 is different.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:09 UTC</span>

<span style="font-size: 90%;">But maybe that's a different problem and should be addressed separately.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:13 UTC</span>

<span style="font-size: 90%;">What do you all think?</span>

**studersi** <span style="color: grey; font-size: 90%;">20:47:12 UTC</span>

<span style="font-size: 90%;">I think cleaning up the 980xxx rules would make sense after cleaning up the variables. It is currently very difficult to understand these rules</span>

**studersi** <span style="color: grey; font-size: 90%;">20:47:34 UTC</span>

<span style="font-size: 90%;">This should be much easier afterwards I think</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:20 UTC</span>

<span style="font-size: 90%;">that would be a very good improvement, I agree that these rules are kind of scary!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:21 UTC</span>

<span style="font-size: 90%;">Good thinking, thanks.</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:21 UTC</span>

<span style="font-size: 90%;">I’m not sure if I should take up such a large project right now. I want to finish what I have on my plate right now. So I would prefer to pass on this one if possible.</span>

**studersi** <span style="color: grey; font-size: 90%;">20:50:18 UTC</span>

<span style="font-size: 90%;">I could make a PR that implements the solution I proposed in the issue</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:19 UTC</span>

<span style="font-size: 90%;">FYI: it is very hard to apply my tuning methodology on NGINX, since you can't enrich the access log with anomaly scores AFAICT. So it would be useful to have an optional 980xxx rule that could report scores for every rule. Outside of that there is little real use of additional 980 rules I think that can not be covered by 949110 / 959100, but it's worth a discussion.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:51:45 UTC</span>

<span style="font-size: 90%;">You mean, apart from the default log output?</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:19 UTC</span>

<span style="font-size: 90%;">(My personal life situation has improved now that my mother is in a “geriatric observation” care home for 6 weeks while they assess her, so she is well taken care off and we can take a bit of rest…)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:54 UTC</span>

<span style="font-size: 90%;">That sounds good given the situation, _@walter_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:23 UTC</span>

<span style="font-size: 90%;">Where I am not 100% in line with _@studersi_ is the details of the variable names. What do the others think?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:36 UTC</span>

<span style="font-size: 90%;">We really need to get this completely right.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:42 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**studersi** <span style="color: grey; font-size: 90%;">20:52:12 UTC</span>

<span style="font-size: 90%;">What would you suggest instead?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:13 UTC</span>

<span style="font-size: 90%;">We're looking forward to a major release. And we can not rename variables constantly. So it's like now and then no more for 5+ years.</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:37 UTC</span>

<span style="font-size: 90%;">agreed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:43 UTC</span>

<span style="font-size: 90%;">agreed</span>

**studersi** <span style="color: grey; font-size: 90%;">20:53:06 UTC</span>

<span style="font-size: 90%;">Would it make sense to differentiate between internal variables and variables intended for logging / jwall / ...</span>

**studersi** <span style="color: grey; font-size: 90%;">20:53:09 UTC</span>

<span style="font-size: 90%;">?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:22 UTC</span>

<span style="font-size: 90%;">The paranoia level is actually a blocking paranoia level. But we do not use that term in the rule set, only in the documentation. Maybe it would be beneficial we start to use it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:56 UTC</span>

<span style="font-size: 90%;">internal / external variables: Maybe, but I think elegance would mean to go with the same minimal set of variables everywhere and they all make perfect sense.</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:09 UTC</span>

<span style="font-size: 90%;">oh yeah, I remember that we set some variable because Jwall depended on it. but, when I look at the Jwall homepage, its last release was 2004….</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:18 UTC</span>

<span style="font-size: 90%;">Also: If we break jwall, jwall is dead, since I doubt Christian Bockermann will update it.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:54:26 UTC</span>

<span style="font-size: 90%;">If we are changing a name is it worth considering renaming executing?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:50 UTC</span>

<span style="font-size: 90%;">Well, if you use JWall still, then……</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:56 UTC</span>

<span style="font-size: 90%;">But then some people will stop updating CRS since they depend on jwall (hint: one of our sponsors might fall into that category)</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:05 UTC</span>

<span style="font-size: 90%;">ack</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:25 UTC</span>

<span style="font-size: 90%;">Well, we can patch JWall, if we think this is the right move</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:55:30 UTC</span>

<span style="font-size: 90%;">How about an optional rule? Or maybe we just set ANOMALY_SCORE at the end somewhere, and it doesn't affect anyone else?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:41 UTC</span>

<span style="font-size: 90%;">I don’t want to keep things broken :confused:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:55:53 UTC</span>

<span style="font-size: 90%;">JWall plugin?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:13 UTC</span>

<span style="font-size: 90%;">I agree 90% with _@studersi_'s proposal, but I want to see if we exhausted all ideas.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:57:29 UTC</span>

<span style="font-size: 90%;">It's a thorough, but complex, proposal. I might re-read it again.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:29 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ what is the problem with "executing"?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:58:11 UTC</span>

<span style="font-size: 90%;">i don't think it really describes what it's doing: it just says it's running, but not that it's reporting/logging but not blocking</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:15 UTC</span>

<span style="font-size: 90%;">You have a point there, _@Paul Beckett_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:59:16 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ I agree but IIUC the executing comes from executing PL.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:34 UTC</span>

<span style="font-size: 90%;">Blocking PL
&
Detection PL?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:45 UTC</span>

<span style="font-size: 90%;">Maybe that's more confusing…</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:51 UTC</span>

<span style="font-size: 90%;">They're both doing detection.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:54 UTC</span>

<span style="font-size: 90%;">Hmm.</span>

**walter** <span style="color: grey; font-size: 90%;">21:00:21 UTC</span>

<span style="font-size: 90%;">They sound clearer to me</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:00:25 UTC</span>

<span style="font-size: 90%;">"active" ~ "executing"?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:43 UTC</span>

<span style="font-size: 90%;">I'm not entirely happy with executing either, but it's not like I did not think about better alternatives. All I could come up with was puzzling too.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:01:03 UTC</span>

<span style="font-size: 90%;">Sorry my friends, I have to go to bed.
Good night!!!</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:01:10 UTC</span>

<span style="font-size: 90%;">bye!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:13 UTC</span>

<span style="font-size: 90%;">Blocking vs Logging PL?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:01:39 UTC</span>

<span style="font-size: 90%;">They're both logging, though. I feel like that's the tricky part.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:01:47 UTC</span>

<span style="font-size: 90%;">How to differentiate.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:08 UTC</span>

<span style="font-size: 90%;">ModSec uses the keyword "DetectionOnly".</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:02:16 UTC</span>

<span style="font-size: 90%;">That's even more confusing.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:02:18 UTC</span>

<span style="font-size: 90%;">blocking and non_blocking then?</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:19 UTC</span>

<span style="font-size: 90%;">that’s true, but I think blocking would imply logging</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:47 UTC</span>

<span style="font-size: 90%;">hmmm non_blocking</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:02:50 UTC</span>

<span style="font-size: 90%;">blocking and non_blocking sound really good to me</span>

**walter** <span style="color: grey; font-size: 90%;">21:02:53 UTC</span>

<span style="font-size: 90%;">so many good suggestions</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:11 UTC</span>

<span style="font-size: 90%;">But you all agree everything is better than "executing"?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:03:21 UTC</span>

<span style="font-size: 90%;">Not necessarily.</span>

**walter** <span style="color: grey; font-size: 90%;">21:03:37 UTC</span>

<span style="font-size: 90%;">‘executing’ is still in play but it has tough competition</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:42 UTC</span>

<span style="font-size: 90%;">The question is what is the value used for?</span>

**walter** <span style="color: grey; font-size: 90%;">21:03:45 UTC</span>

<span style="font-size: 90%;">non-blocking is extremely clear</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:08 UTC</span>

<span style="font-size: 90%;">But that meaning collides with detection only</span>

**walter** <span style="color: grey; font-size: 90%;">21:04:23 UTC</span>

<span style="font-size: 90%;">agreed :thinking_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:23 UTC</span>

<span style="font-size: 90%;">If modsec is in detection only, both are non-blocking</span>

**walter** <span style="color: grey; font-size: 90%;">21:04:36 UTC</span>

<span style="font-size: 90%;">blocking / detection?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:04:59 UTC</span>

<span style="font-size: 90%;">execution semantically was to get logs from the next PL</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:27 UTC</span>

<span style="font-size: 90%;">So you could tweak the rules before moving</span>

**studersi** <span style="color: grey; font-size: 90%;">21:05:29 UTC</span>

<span style="font-size: 90%;">I think the variables used to be called "monitoring_" before it was changed to "executing_"</span>

**studersi** <span style="color: grey; font-size: 90%;">21:05:41 UTC</span>

<span style="font-size: 90%;">would that be an option?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:05:47 UTC</span>

<span style="font-size: 90%;">I think that detection only is an overruling setting. So while it's conflicting, strictly speaking, I don't think it's confusing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:27 UTC</span>

<span style="font-size: 90%;">We can pause and regroup</span>

**airween** <span style="color: grey; font-size: 90%;">21:06:29 UTC</span>

<span style="font-size: 90%;">sorry guys, I have to go
:wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:56 UTC</span>

<span style="font-size: 90%;">And look for other options, and then after thinking a bit more</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:03 UTC</span>

<span style="font-size: 90%;">Vote on options</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:03 UTC</span>

<span style="font-size: 90%;">I have to go in a few mins too… :disappointed:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:11 UTC</span>

<span style="font-size: 90%;">We should list the options we discussed in the issue</span>

**studersi** <span style="color: grey; font-size: 90%;">21:07:23 UTC</span>

<span style="font-size: 90%;">Will do</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:27 UTC</span>

<span style="font-size: 90%;">As Christian said, this is going to affect people/projects for the next 5 years</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:54 UTC</span>

<span style="font-size: 90%;">Thank you all for sharing your idea.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:55 UTC</span>

<span style="font-size: 90%;">s</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:15 UTC</span>

<span style="font-size: 90%;">I think it's good to sum this up, sleep over it and then pick the discussions up in the issue again.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:37 UTC</span>

<span style="font-size: 90%;">Also: I think settling the "execution" term is a pre-condition for proper variable naming.</span>

**walter** <span style="color: grey; font-size: 90%;">21:08:40 UTC</span>

<span style="font-size: 90%;">yes, a lot of shower time has to be devoted to this</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:45 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:06 UTC</span>

<span style="font-size: 90%;">Thank you all for joining and contributing to very full agenda. Glad we were able to cover everything.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:15 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:09:20 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:09:26 UTC</span>

<span style="font-size: 90%;">Good night everyone!</span>

**jptosso** <span style="color: grey; font-size: 90%;">21:09:30 UTC</span>

<span style="font-size: 90%;">bye guys ! good night</span>

**studersi** <span style="color: grey; font-size: 90%;">21:09:33 UTC</span>

<span style="font-size: 90%;">Thanks everyone, good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:09:40 UTC</span>

<span style="font-size: 90%;">Bye!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:09:50 UTC</span>

<span style="font-size: 90%;">good night (sorry for opening the can of worms!)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:15 UTC</span>

<span style="font-size: 90%;">Somebody had to do it, _@Paul Beckett_ :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:10:18 UTC</span>

<span style="font-size: 90%;">I would have done the same _@Paul Beckett_ :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:41 UTC</span>

<span style="font-size: 90%;">So you guys came into the meeting with your daggers sharpened? :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:11:13 UTC</span>

<span style="font-size: 90%;">Always prepared...</span>

**walter** <span style="color: grey; font-size: 90%;">21:11:15 UTC</span>

<span style="font-size: 90%;">good night everyone!</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:11:20 UTC</span>

<span style="font-size: 90%;">bb</span>

