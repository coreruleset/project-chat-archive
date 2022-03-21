### Mon, Jul 1st, 2019

**dune73** <span style="color: grey; font-size: 90%;">18:31:02 UTC</span>

<span style="font-size: 90%;">Hello! So who's around for the chat?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:10 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:10 UTC</span>

<span style="font-size: 90%;">hi there</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:31:16 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">hello! I’m here, but I’m hoping we can do a bit of a quickie :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:29 UTC</span>

<span style="font-size: 90%;">Hello everybody! Good to see you around.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:35 UTC</span>

<span style="font-size: 90%;">heyhooooo</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:39 UTC</span>

<span style="font-size: 90%;">Here is the (empty) agenda. Please add items as you see fit.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:49 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1471></span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:34:10 UTC</span>

<span style="font-size: 90%;">I'm here too</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:24 UTC</span>

<span style="font-size: 90%;">Hello Allan, ve.ry nice of you to join us</span>

**fgs** <span style="color: grey; font-size: 90%;">18:34:47 UTC</span>

<span style="font-size: 90%;">I have a few minutes today unfortunately</span>

**fgs** <span style="color: grey; font-size: 90%;">18:34:55 UTC</span>

<span style="font-size: 90%;">but :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:17 UTC</span>

<span style="font-size: 90%;">_@fgs_: Is it better we cover topics that affect you now - or wait for an hour or so (assuming it's not a quickie...)</span>

**fgs** <span style="color: grey; font-size: 90%;">18:35:47 UTC</span>

<span style="font-size: 90%;">later might be better but i can’t guarantee I will be back in an hour</span>

**fgs** <span style="color: grey; font-size: 90%;">18:36:04 UTC</span>

<span style="font-size: 90%;">i will be back though, just not sure the timing :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:18 UTC</span>

<span style="font-size: 90%;">So we do it now?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:36:24 UTC</span>

<span style="font-size: 90%;">let’s start</span>

**fgs** <span style="color: grey; font-size: 90%;">18:36:33 UTC</span>

<span style="font-size: 90%;">and i will let you know if i have to leave</span>

**fgs** <span style="color: grey; font-size: 90%;">18:36:39 UTC</span>

<span style="font-size: 90%;">sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:47 UTC</span>

<span style="font-size: 90%;">OK. As Allan and _@fgs_ are here, I'd like to kick it off with the RE2 patches.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:00 UTC</span>

<span style="font-size: 90%;">This is definitely a direction we want to take.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:12 UTC</span>

<span style="font-size: 90%;">The question is: How can we make sure they are ready to be merged.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:27 UTC</span>

<span style="font-size: 90%;">Are the unit tests we have in place for these rules adequate?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:55 UTC</span>

<span style="font-size: 90%;">@allanrbo: Do you think this is ready to be merged (Travis is obviously happy with it)</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:36 UTC</span>

<span style="font-size: 90%;">I can see that how big work should to implement the RE2 to modsec2+Apache</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:45 UTC</span>

<span style="font-size: 90%;">and then we can check it "in-place"</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:53 UTC</span>

<span style="font-size: 90%;">_@airween_: You think it is a lot of work to implement - or not so much? And do we really need to test this on ModSec2?</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:27 UTC</span>

<span style="font-size: 90%;">I think that should't so *not* much - but I have never work with RE2...</span>

**csanders** <span style="color: grey; font-size: 90%;">18:40:32 UTC</span>

<span style="font-size: 90%;">hey folks sorry i'm late</span>

**fgs** <span style="color: grey; font-size: 90%;">18:40:58 UTC</span>

<span style="font-size: 90%;">Shall we start discussing 1458?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:41:17 UTC</span>

<span style="font-size: 90%;">Do we want to go through every one of them btw?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:20 UTC</span>

<span style="font-size: 90%;">Hey _@csanders_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:29 UTC</span>

<span style="font-size: 90%;">If you want to discuss them one by one...</span>

**fgs** <span style="color: grey; font-size: 90%;">18:41:48 UTC</span>

<span style="font-size: 90%;">Or should we do it offline perhaps?</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:41:56 UTC</span>

<span style="font-size: 90%;">_@dune73_ yes, I've tested all the changes, both manual and automated, and I've written in the pull requests how I've done so</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:18 UTC</span>

<span style="font-size: 90%;">Yes, the PRs are done in a exemplary manner.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:39 UTC</span>

<span style="font-size: 90%;">I think they are very well written</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:00 UTC</span>

<span style="font-size: 90%;">Personally, I think it would be better to define the testing / review strategy here and then discuss them offline / on github one by one and then merge.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:09 UTC</span>

<span style="font-size: 90%;">Otherwise everything will be kept back.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:43:28 UTC</span>

<span style="font-size: 90%;">I think they should be reviewed offline. I can review some of them.
But I think the PRs are well written and tested.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:43:31 UTC</span>

<span style="font-size: 90%;">Sounds good</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:46 UTC</span>

<span style="font-size: 90%;">I like the remark that it mostly hinges on our tests being complete, if we judge our tests to be competent, then the reviewing becomes a light task</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:18 UTC</span>

<span style="font-size: 90%;">Yes, I think we need to check out the tests next to the original rule, then maybe add more tests and then review.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:44:49 UTC</span>

<span style="font-size: 90%;">Sounds like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:39 UTC</span>

<span style="font-size: 90%;">Given _@fgs_ and _@franbuehler_ are our best RegEx experts (in the absence of Walter), I think it would be great if you two could divide them between the two. I might be able to add more tests, likely _@emphazer_ too.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:46:30 UTC</span>

<span style="font-size: 90%;">sure</span>

**fgs** <span style="color: grey; font-size: 90%;">18:47:15 UTC</span>

<span style="font-size: 90%;">fwiw, from a rather quick look, i don’t think 1458 is correct</span>

**fgs** <span style="color: grey; font-size: 90%;">18:47:50 UTC</span>

<span style="font-size: 90%;">not because the patterns are not equivalent, but because the intention is not preserved (even if the original pattern was wrong)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:00 UTC</span>

<span style="font-size: 90%;">;(</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:35 UTC</span>

<span style="font-size: 90%;">Would you volunteer to take this one over? _@franbuehler_ could then self-assign 2-3 of them as well.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:47 UTC</span>

<span style="font-size: 90%;">Yes, I will take the first 3.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:02 UTC</span>

<span style="font-size: 90%;">I will try to make my way through all of them leaving comments</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:07 UTC</span>

<span style="font-size: 90%;">I already did for the hyperscan one</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:10 UTC</span>

<span style="font-size: 90%;">That would be 1466, 62 and 61?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:49:13 UTC</span>

<span style="font-size: 90%;">But the more the merrier</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:49:20 UTC</span>

<span style="font-size: 90%;">fgs: I agree, as I wrote in the PR text, looks like their intention was something else. Here's what I wrote:
"It's kind of odd there was so much unused code in this regex, so maybe the intention was slightly different than what it actually did. However, since this is just a gate that decides which values to pass to @validateUrlEncoding, I don't think it matters that much. In the case of 920230 it was used to check for double encoding, and arguably it was and still is overly sensitive."</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:49:49 UTC</span>

<span style="font-size: 90%;">If I have problems reviewing them, I'll ask in the issue for help :wink:</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:50:40 UTC</span>

<span style="font-size: 90%;">this rule is chained with the @validateUrlEncoding, so it looks like just a gate in front of @validateUrlEncoding, maybe becuase @validateUrlEncoding is intense to run - I don't know. Either way, the rule that I'm changing here is unimportant, because it's the @validateUrlEncoding that's the real intention here.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:50:54 UTC</span>

<span style="font-size: 90%;">_@Allan Boll_ I missed that, sorry. I will go through them more carefully</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:30 UTC</span>

<span style="font-size: 90%;">_@fgs_ and _@franbuehler_: Please review these rules and merge them if you both agree they are ready. Allan is obviously around to explain things and support you. So I think that group of PRs is covered.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:33 UTC</span>

<span style="font-size: 90%;">OK?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:41 UTC</span>

<span style="font-size: 90%;">Ok</span>

**fgs** <span style="color: grey; font-size: 90%;">18:52:45 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:53:21 UTC</span>

<span style="font-size: 90%;">(y) yea I have this slack open most of the time, so questions are welcome anytime.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:27 UTC</span>

<span style="font-size: 90%;">Thank you very much.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:27 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:31 UTC</span>

<span style="font-size: 90%;">Let's move on then.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:49 UTC</span>

<span style="font-size: 90%;">[#1467](https://github.com/coreruleset/coreruleset/issues/#1467), also by Allan.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:07 UTC</span>

<span style="font-size: 90%;">I did not look at it. _@csanders_ and _@franbuehler_: What do you think?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:45 UTC</span>

<span style="font-size: 90%;">I started looking at it</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:52 UTC</span>

<span style="font-size: 90%;">so the point is pretty obvious</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:58 UTC</span>

<span style="font-size: 90%;">right now the docker images don't have FTW built in</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:12 UTC</span>

<span style="font-size: 90%;">this is because they are designed (or rather being better designed thanks to _@franbuehler_</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:20 UTC</span>

<span style="font-size: 90%;">) to be for others usage</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:29 UTC</span>

<span style="font-size: 90%;">we just add FTW on top for internal testing currently</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:57:11 UTC</span>

<span style="font-size: 90%;">the motivation was really just that I needed a one-liner to run the regression tests easily while making CRS changes. And yea, it seemed like the other docker images available were designed for something bigger.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:57:16 UTC</span>

<span style="font-size: 90%;">Unfortunately I have never checked what TravisCI does with this container.
Thank _@csanders_ for the explanation.
I'll first need to have a look at this PR.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:57:55 UTC</span>

<span style="font-size: 90%;">I think that is reasonable -- we should be able to add a switch pretty quickly to only minorly increase the size of the image, thoughts _@franbuehler_?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:14 UTC</span>

<span style="font-size: 90%;">FTW pulls quite a lot of dependencies, or am I wrong?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:58:34 UTC</span>

<span style="font-size: 90%;">but since it's just pip it'll be just one command line IRL</span>

**csanders** <span style="color: grey; font-size: 90%;">18:58:40 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">18:59:00 UTC</span>

<span style="font-size: 90%;">Need to go :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:11 UTC</span>

<span style="font-size: 90%;">Bye _@fgs_ and thanks for joining</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:59:30 UTC</span>

<span style="font-size: 90%;">Ah, that Docker stuff is hard.
So many requirements...</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">18:59:38 UTC</span>

<span style="font-size: 90%;">a major difference in this docker container vs. the other ones you're using, is that I'm basing it on just ubuntu18.04 with its built in modsec binaries. Because it seemed simpler.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:00 UTC</span>

<span style="font-size: 90%;">It's a work in progress ...</span>

**csanders** <span style="color: grey; font-size: 90%;">19:00:22 UTC</span>

<span style="font-size: 90%;">yup, we have the normal problem where ubuntu doesn't necc have the most updated (or downdated) version we need</span>

**csanders** <span style="color: grey; font-size: 90%;">19:00:38 UTC</span>

<span style="font-size: 90%;">but since it gets it from upstream, it is usually not a big problem for end users</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:01:52 UTC</span>

<span style="font-size: 90%;">I always voted for different images for ModSec and CRS but I am not sure now...
Then someone suggested an all in one multistage build and stop at different points. I did not check that yet.
But maybe we could add FTW as the last stage in multistage. No idea if that works.</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:01:55 UTC</span>

<span style="font-size: 90%;">actually, maybe that's a good thing for running the regression tests? That way we're sure they pass even on the modsec binaries that many users are probably going to be using. "apt-get install libapache2-mod-security2". Kind of like a lowest common denominator.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:56 UTC</span>

<span style="font-size: 90%;">Could the FTW installation be a build option? (As an alternative to the multistage build)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:03:01 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:02 UTC</span>

<span style="font-size: 90%;">_@Allan Boll_: Good point</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:14 UTC</span>

<span style="font-size: 90%;">Ah, build option, good idea.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:33 UTC</span>

<span style="font-size: 90%;">But then the image has to be built in the pipeline?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:04:02 UTC</span>

<span style="font-size: 90%;">Another tag maybe?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:15 UTC</span>

<span style="font-size: 90%;">Maybe.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:04:24 UTC</span>

<span style="font-size: 90%;">travis already builds it pretty much</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:04:33 UTC</span>

<span style="font-size: 90%;">And we need other tags for proxy and TLS too :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:39 UTC</span>

<span style="font-size: 90%;">_@csanders_ and _@franbuehler_: Can we trust this into your hands and move on?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:04:43 UTC</span>

<span style="font-size: 90%;">Ahhhhh!!!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:04:51 UTC</span>

<span style="font-size: 90%;">I think that shouldn't be an issue</span>

**csanders** <span style="color: grey; font-size: 90%;">19:04:56 UTC</span>

<span style="font-size: 90%;">i'll take charge of this change</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:02 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:05:08 UTC</span>

<span style="font-size: 90%;">the TLS and proxy stuff _@franbuehler_ has made a nice template for</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:08 UTC</span>

<span style="font-size: 90%;">_@Allan_: That OK with you?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:05:09 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:05:13 UTC</span>

<span style="font-size: 90%;">thanks you very very much to her</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:23 UTC</span>

<span style="font-size: 90%;">that sounds awesome!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:05:30 UTC</span>

<span style="font-size: 90%;">No, thank you _@csanders_!!</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:40 UTC</span>

<span style="font-size: 90%;">yeah I’ve also been cursing the one line thing and also made my own stupid docker images for it</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:55 UTC</span>

<span style="font-size: 90%;">but right now the base images seem to be in much beter shape</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:06:25 UTC</span>

<span style="font-size: 90%;">Ok, _@csanders_ and I will continue our work...</span>

**csanders** <span style="color: grey; font-size: 90%;">19:06:30 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**Allan Boll** <span style="color: grey; font-size: 90%;">19:06:48 UTC</span>

<span style="font-size: 90%;">yea I'm fine if you abandon this PR really. We're just using it internally here on my team to test things quickly without having to set up a more complex environment, so I thought others might also want such a one-liner.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:07:05 UTC</span>

<span style="font-size: 90%;">I like the idea</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:30 UTC</span>

<span style="font-size: 90%;">OK. So next in line is [#1450](https://github.com/coreruleset/coreruleset/issues/#1450). I think this is ready to be merged. Objections?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:07:50 UTC</span>

<span style="font-size: 90%;">none here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:19 UTC</span>

<span style="font-size: 90%;">Merged.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:09:30 UTC</span>

<span style="font-size: 90%;">looks good</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:41 UTC</span>

<span style="font-size: 90%;">[#1477](https://github.com/coreruleset/coreruleset/issues/#1477): Any comments?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:06 UTC</span>

<span style="font-size: 90%;">A welcome PR by _@theMiddle_. But nobody took the time to look at it so far.</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:27 UTC</span>

<span style="font-size: 90%;">these bypasses sound like something I would make a PR for :stuck_out_tongue: I like that little regexp trickery. shall I review and merge?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:06 UTC</span>

<span style="font-size: 90%;">Please do. Given _@theMiddle_ lists several payloads, I think it could do with some more unit tests.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:11:35 UTC</span>

<span style="font-size: 90%;">sure, no problem</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:27 UTC</span>

<span style="font-size: 90%;">Good. This brings us to the ReDoS stuff that our researcher suggested. I think _@emphazer_ took a look, or am I wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:44 UTC</span>

<span style="font-size: 90%;">And _@SpartanTri_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:43 UTC</span>

<span style="font-size: 90%;">Problem is, these PRs are all somewhat broken. Our researcher stopped responding and it's all a bit of a mess.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:54 UTC</span>

<span style="font-size: 90%;">So what do we do?</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:04 UTC</span>

<span style="font-size: 90%;">well since we know that they are not exploitable, I’d say they are mid-prio issues</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:26 UTC</span>

<span style="font-size: 90%;">I don’t know if the researcher has responded at all, seems he moved on</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:16:26 UTC</span>

<span style="font-size: 90%;">i agree</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:36 UTC</span>

<span style="font-size: 90%;">so we are on our own I think</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:18 UTC</span>

<span style="font-size: 90%;">He responded initially, then stopped responding (when we found out he never tested this against ModSec). On twitter he is still active with the topic and announced a paper (now that we released 3.1.1, which I think is fair)</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:42 UTC</span>

<span style="font-size: 90%;">ah okay!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:07 UTC</span>

<span style="font-size: 90%;">Yes, we are pretty much on our own to fix this. What we could do is extract the fix, put it into an issue and then close the broken PR. The problem I see right now is that our PR queue is clogged by stuff that needs action and the action does not happen.</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:53 UTC</span>

<span style="font-size: 90%;">yes you are right, we should do this</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:59 UTC</span>

<span style="font-size: 90%;">shall I take one of the issues?</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:04 UTC</span>

<span style="font-size: 90%;">maybe it’s not so bad to do it</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:23 UTC</span>

<span style="font-size: 90%;">and yes, if it’s too much hassle we can open a new PR and credit him manually</span>

**csanders** <span style="color: grey; font-size: 90%;">19:19:41 UTC</span>

<span style="font-size: 90%;">agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:49 UTC</span>

<span style="font-size: 90%;">Could you create the new issues and close the PRs? Or just one of them?</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:47 UTC</span>

<span style="font-size: 90%;">I assigned two out of three PR to myself, they are in rules I’ve written anyway!</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:22 UTC</span>

<span style="font-size: 90%;">the remaining one is <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1361> in SQLi rule</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:23 UTC</span>

<span style="font-size: 90%;">Which one is still open? I can self-assign then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:27 UTC</span>

<span style="font-size: 90%;">thanks</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:21:41 UTC</span>

<span style="font-size: 90%;">thanks to both of you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:13 UTC</span>

<span style="font-size: 90%;">Let's move to [#1345](https://github.com/coreruleset/coreruleset/issues/#1345). The purge PR. Any opinions or takers?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:22:49 UTC</span>

<span style="font-size: 90%;">taking a look</span>

**csanders** <span style="color: grey; font-size: 90%;">19:23:27 UTC</span>

<span style="font-size: 90%;">i think all of this has been rolled into the new images (maybe not the ubuntu one though</span>

**csanders** <span style="color: grey; font-size: 90%;">19:24:05 UTC</span>

<span style="font-size: 90%;">as a result AFAIK it can be closed</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:37 UTC</span>

<span style="font-size: 90%;">OK. Can you close it then?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:24:41 UTC</span>

<span style="font-size: 90%;">yup</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:07 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:49 UTC</span>

<span style="font-size: 90%;">[#1320](https://github.com/coreruleset/coreruleset/issues/#1320) it is then. Thank you for the good work here _@theMiddle_.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:00 UTC</span>

<span style="font-size: 90%;">thanks!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:26:23 UTC</span>

<span style="font-size: 90%;">unfortunately I still waiting modsec team for a solution</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:50 UTC</span>

<span style="font-size: 90%;">It's likely this PR is adding dust in the meantime.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:28 UTC</span>

<span style="font-size: 90%;">Let's say ModSec is getting a fix. Will this work on older ModSec versions too, but the detection not working?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:27:44 UTC</span>

<span style="font-size: 90%;">uhm good point, didn’t think about it</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:18 UTC</span>

<span style="font-size: 90%;">I think that will not work on v2</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:20 UTC</span>

<span style="font-size: 90%;">If it's just FTW that does not work, we can live with it. But we can't release rules that break CRS on old ModSec installations.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:13 UTC</span>

<span style="font-size: 90%;">Why is it exactly. Is not it just en empty REQUEST_BODY that is the issue here?</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:36 UTC</span>

<span style="font-size: 90%;">I’m also not in the loop, why would it not work on modsec2? we can skip on modsec versions AFAIK</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:47 UTC</span>

<span style="font-size: 90%;">as long as it parses, I wouldn’t mind having modsec3-only rules</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:11 UTC</span>

<span style="font-size: 90%;">maybe then I’ll upgrade (not really)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:11 UTC</span>

<span style="font-size: 90%;">yes, the problem is the empty REQUEST_BODY variable, but I’m worried about evasion too</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:39 UTC</span>

<span style="font-size: 90%;">Evasions for something we are not detecting today?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:31:26 UTC</span>

<span style="font-size: 90%;">sorry, worried about evasion but not on CRS. I think it’s a modsecurity issue</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:30 UTC</span>

<span style="font-size: 90%;">So you agree that the new rules would be parsed on ModSec 2.9.x (but the rules would simply be ignored). Or you might need to add a skip rule as 945xxx.</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">I wouldn’t see that as a blocking issue</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:11 UTC</span>

<span style="font-size: 90%;">nobody loses</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:33 UTC</span>

<span style="font-size: 90%;">Exactly my thinking. Because if that is covered, we can move to test the rules.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:36 UTC</span>

<span style="font-size: 90%;">yes, the rules would be ignored</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:12 UTC</span>

<span style="font-size: 90%;">I would really like to see some big installation running this (maybe without the scoring) on a fixed version of ModSec before we merge this.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:34:16 UTC</span>

<span style="font-size: 90%;">or, in other words, all those rules will never be triggered</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:42 UTC</span>

<span style="font-size: 90%;">in the 944xxx Java rules, we had one that blew up ModSec and we did not notice until production...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:54 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Thank you for the confirmation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:21 UTC</span>

<span style="font-size: 90%;">Or am I asking for too much?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:01 UTC</span>

<span style="font-size: 90%;">I think that _@airween_ has a working patch that fix this problem</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:29 UTC</span>

<span style="font-size: 90%;">Yes, but would anybody with a big installation put this patch into prod?</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:31 UTC</span>

<span style="font-size: 90%;">I think we need to clear this problem</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:46 UTC</span>

<span style="font-size: 90%;">not on a big installation :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:56 UTC</span>

<span style="font-size: 90%;">this issue doesn't come on v3, because it contains a bug :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:10 UTC</span>

<span style="font-size: 90%;">v2 works as documentation describe</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:35 UTC</span>

<span style="font-size: 90%;">oh so maybe a new v3 update will invalidate our rule</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:50 UTC</span>

<span style="font-size: 90%;">that’s a different situation…</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:53 UTC</span>

<span style="font-size: 90%;">the problem is that the CT is application/json or application/xml - and in this case the REQUEST_BODY doesn't exists</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:55 UTC</span>

<span style="font-size: 90%;">we are relying on undocumented behavior then</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:02 UTC</span>

<span style="font-size: 90%;">this works in v2 as well</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:17 UTC</span>

<span style="font-size: 90%;">but in v3, the REQUEST_BODY is also exists</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:24 UTC</span>

<span style="font-size: 90%;">and it will cause many FP because of it</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:27 UTC</span>

<span style="font-size: 90%;">no matter what is the CT</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:43 UTC</span>

<span style="font-size: 90%;">yes, that may be _@walter_</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:53 UTC</span>

<span style="font-size: 90%;">because of the special chars in XML and JSON, it’s very good that the REQUEST_BODY is not filled, when a client sends these C-T headers</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:11 UTC</span>

<span style="font-size: 90%;">there is a PR for v3, which fixes it, but this is just a plan</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:37 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/pull/2045></span>

**airween** <span style="color: grey; font-size: 90%;">19:40:50 UTC</span>

<span style="font-size: 90%;">I think, _@theMiddle_ wants to do something like not conform with this documented behavior :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:03 UTC</span>

<span style="font-size: 90%;">All summed up, we have a decent PR, but given the messy situation around XML and REQUEST_BODY in ModSec, we could lead our users on unstable ice, if we merge it - and then ModSec changes the behaviour after an update?</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:20 UTC</span>

<span style="font-size: 90%;">well rather… these rules only work because of a current bug in v3</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:34 UTC</span>

<span style="font-size: 90%;">you're right, _@walter_</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:47 UTC</span>

<span style="font-size: 90%;">that's what I said</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:11 UTC</span>

<span style="font-size: 90%;">and as the CRS project as a whole we need this bug to be fixed, because all those `< > { }` in JSON and XML will cause a mess of FPs for our users</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:19 UTC</span>

<span style="font-size: 90%;">yes but it’s really dangerous to let the user able to empty the REQUEST_BODY variable just by setting a CT. This should be different in modsec IMO</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:34 UTC</span>

<span style="font-size: 90%;">ok, it’s not a CRS problem, but it would be in the future</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:48 UTC</span>

<span style="font-size: 90%;">in the PR I did't hide the REQUEST_BODY, as it works in v2, so it could be work</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">hmm, well, if a client sets the CT header to XML or JSON, and the body is UNparseable then we already reject it… and if it parses correctly, the text nodes are passed on to us for scanning.. so we do scan the body contents but just with much better visibility into the contents. it’s just that we lose sight of the plain XML stream</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:24 UTC</span>

<span style="font-size: 90%;">so now I’m not so sure we should commit rules that sort of abuse this bug in v3 :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">I wish we could save the body, that would be so sweet</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:41 UTC</span>

<span style="font-size: 90%;">but in case of XXE you haven’t access to the external entity with what modsec parse</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:51 UTC</span>

<span style="font-size: 90%;">yes I agree, we lose that sadly :disappointed:</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:56 UTC</span>

<span style="font-size: 90%;">this is tough</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:09 UTC</span>

<span style="font-size: 90%;">maybe it’s the only scenario with this issue</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:32 UTC</span>

<span style="font-size: 90%;">I don't remember the result, but we discussed about it with _@theMiddle_</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:34 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:01 UTC</span>

<span style="font-size: 90%;">have to review the slack... :stuck_out_tongue:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:23 UTC</span>

<span style="font-size: 90%;">anyway, I wouldn’t merge it atm :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:30 UTC</span>

<span style="font-size: 90%;">It's really a hard problem.</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:53 UTC</span>

<span style="font-size: 90%;">yes, ideally we would work this out with modsec and get this functionality included in v3 as a real feature</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:56 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Would you mind letting this rest for a couple of months until the ModSec situation is sorted out?</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:22 UTC</span>

<span style="font-size: 90%;">I understand, but the documentation is clear: if the client sends the CT as application/xml|json, then there isn't REQUEST_BODY, so the `@re` operator has no effect...</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:44 UTC</span>

<span style="font-size: 90%;">yes the behavior of modsec 2.x is the only correct interpretation</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:14 UTC</span>

<span style="font-size: 90%;">Ideally you would close the PR and bring it back when it's ready (so we get a clean and neat list of PRs on github)</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">yes, I think is better</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:16 UTC</span>

<span style="font-size: 90%;">idk, maybe it’s the expected behavior and modsec will never change it…</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:16 UTC</span>

<span style="font-size: 90%;">could we apply the XML/JSON payload to the `@re`?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">yes, I think is better</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">yes, I think is better</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:19 UTC</span>

<span style="font-size: 90%;">Thank you for your understanding. It's really with a heavy heart...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:25 UTC</span>

<span style="font-size: 90%;">I like the PR a lot.</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:45 UTC</span>

<span style="font-size: 90%;">yes me too, I really want XXE protection, it really seems simple…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:50:00 UTC</span>

<span style="font-size: 90%;">no problem! thanks you all for understanding and reviewing it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:09 UTC</span>

<span style="font-size: 90%;">You are welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:27 UTC</span>

<span style="font-size: 90%;">Next on the list are 4 PRs that have the needs-action label. They are all on hold.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:41 UTC</span>

<span style="font-size: 90%;">Yes, two of them are mine. i self-assigned them.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:07 UTC</span>

<span style="font-size: 90%;">Can you give us a time frame until you fix them up?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:55 UTC</span>

<span style="font-size: 90%;">In the next two weeks, before my vacation</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:10 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:12 UTC</span>

<span style="font-size: 90%;">I have [#1403](https://github.com/coreruleset/coreruleset/issues/#1403) and totally forgot about this. I will fix it up and likely improve it a bit from remaining FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:15 UTC</span>

<span style="font-size: 90%;">What about your's @walter?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:25 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:01 UTC</span>

<span style="font-size: 90%;">I would also like 2 weeks so I can space it out a bit</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:08 UTC</span>

<span style="font-size: 90%;">Then there is only [#1329](https://github.com/coreruleset/coreruleset/issues/#1329). I think we exhausted the original submitter and he gave up. Can we fix it up and merge? Not sure what it still open.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:33 UTC</span>

<span style="font-size: 90%;">Did anybody follow this? Is it only the tests?</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:36 UTC</span>

<span style="font-size: 90%;">I think this is interesting, we’ll have to see what it does in terms of FP</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:48 UTC</span>

<span style="font-size: 90%;">the original submitter seems strapped for time though, so maybe we have to add tests</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:56 UTC</span>

<span style="font-size: 90%;">I would self-assign but already have a bit too many, it’s ambitious</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:36 UTC</span>

<span style="font-size: 90%;">Yes, think so too. Any takers? As it's probably only about tests, I'm looking over at _@emphazer_ a bit. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:38 UTC</span>

<span style="font-size: 90%;">(I think I f**cked up the PR section of the agenda when adding more items. Glad we are almost done with the PRs.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:01 UTC</span>

<span style="font-size: 90%;">OK, let's not delay too long. I'm taking this.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">thank you</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:20 UTC</span>

<span style="font-size: 90%;">lol, its all good</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:15 UTC</span>

<span style="font-size: 90%;">So we're done with the PRs. Issues are piling up, but I do not htink we have time to cover them here. Any issue that is really important and must be dealt with as a community?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:33 UTC</span>

<span style="font-size: 90%;">none here</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:37 UTC</span>

<span style="font-size: 90%;">none here</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:44 UTC</span>

<span style="font-size: 90%;">n.h.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:54 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:06 UTC</span>

<span style="font-size: 90%;">So there are a few other smaller issues I'd like to touch briefly.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:48 UTC</span>

<span style="font-size: 90%;">OWASP HQ & Board have new donation / sponsoring rules that I read as project no longer get to receive donations. They all go to OWASP HQ and project will need to ask for money.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:19 UTC</span>

<span style="font-size: 90%;">that seems a bit odd</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:28 UTC</span>

<span style="font-size: 90%;">_@csanders_ / _@walter_: Is this interpretation correct? And what do we do? I think we still have like 1-2K USD with OWASP on our accounts.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:40 UTC</span>

<span style="font-size: 90%;">i didn't see anything about this honestly</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:43 UTC</span>

<span style="font-size: 90%;">I have not followed the discussion sadly, hard so say</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:01 UTC</span>

<span style="font-size: 90%;">Yes it is odd. And it is because OWASP HQ is always short of funds and many chapters and projects have substantial funds they are not using.</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:07 UTC</span>

<span style="font-size: 90%;">was it posted to -leaders? maybe another list? i would imagine it should have caused a hard to miss drama</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:18 UTC</span>

<span style="font-size: 90%;">yes I can see that</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:20 UTC</span>

<span style="font-size: 90%;">It was a message on the leaders ML last week. By Mike Camon, the interim CEO.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:34 UTC</span>

<span style="font-size: 90%;">It's been in discussion for a considerable length of time.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:42 UTC</span>

<span style="font-size: 90%;">i'll have to follow up</span>

**csanders** <span style="color: grey; font-size: 90%;">20:01:56 UTC</span>

<span style="font-size: 90%;">it seems less than desirable</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:09 UTC</span>

<span style="font-size: 90%;">Tue, 25 Jun 2019 23:45:43 -0700 (PDT)</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:14 UTC</span>

<span style="font-size: 90%;">ah I see it now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:18 UTC</span>

<span style="font-size: 90%;">Subject: [leaders] Donations to the Foundation</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:19 UTC</span>

<span style="font-size: 90%;">`[leaders] Donations to the Foundation`</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:28 UTC</span>

<span style="font-size: 90%;">no responses, that’s srtange</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:30 UTC</span>

<span style="font-size: 90%;"><https://www.owasp.org/index.php/Attributed_Giving_Policy></span>

**walter** <span style="color: grey; font-size: 90%;">20:02:43 UTC</span>

<span style="font-size: 90%;">well to be fair it started a bit mundane so I guess I zoned out :joy:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:48 UTC</span>

<span style="font-size: 90%;">The Board of Directors at their April 2019 meeting adopted a resolution
that restricts donations and membership dues splits to gifts $1,000 and
above. The following outlines how charitable gifts are processed for the
OWASP Foundation.</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:50 UTC</span>

<span style="font-size: 90%;">note to self — should package bad news this way.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:57 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:09 UTC</span>

<span style="font-size: 90%;">haha</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:14 UTC</span>

<span style="font-size: 90%;">yes, I can see where those earmarked gifts are very troublesome for the central body</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:18 UTC</span>

<span style="font-size: 90%;">Maybe I overlooked the above paragraph as it seems to say that donations above 1K can still be sent to projects.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:53 UTC</span>

<span style="font-size: 90%;">it is very hard to parse -- i'm almost seeing the opposite</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:54 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:55 UTC</span>

<span style="font-size: 90%;">i imagine they end up with quite a sum of unusuable funds and liabilities</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:07 UTC</span>

<span style="font-size: 90%;">and you are not getting any interest on it these days either</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:09 UTC</span>

<span style="font-size: 90%;">If that is the case, I am mostly OK with the new rule. It would just mean that members should not be able to earmark their fees.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:15 UTC</span>

<span style="font-size: 90%;">so now it’s just a drag to them</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:36 UTC</span>

<span style="font-size: 90%;">yeah it can only be done for big amounts, which is not too bad</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:50 UTC</span>

<span style="font-size: 90%;">for smaller sums it’s better to use paypal anyway….</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:04 UTC</span>

<span style="font-size: 90%;">now if that would be formalized as acceptable behavior for a project, that would be a constructive  result</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:18 UTC</span>

<span style="font-size: 90%;">don’t let us email some scanned forms just to print stickers…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:33 UTC</span>

<span style="font-size: 90%;">Yes, I could live with that.</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:34 UTC</span>

<span style="font-size: 90%;">it’s not viable</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:08 UTC</span>

<span style="font-size: 90%;">allow projects to collect their owwn funds, through patreon, opencollective, <http://paypal.me|paypal.me> etc…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:09 UTC</span>

<span style="font-size: 90%;">I think it is best to read it carefully again and if we are not sure, we respond on the leader ML or in private to one of the board members we know.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:32 UTC</span>

<span style="font-size: 90%;">Nex topic is Swag.</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:35 UTC</span>

<span style="font-size: 90%;">it will save them huge administrative hassle too</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:45 UTC</span>

<span style="font-size: 90%;">and us</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:46 UTC</span>

<span style="font-size: 90%;">okay, bon!</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:49 UTC</span>

<span style="font-size: 90%;">swag swag swag</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:08 UTC</span>

<span style="font-size: 90%;">I got an unrelated redbubble order in the mail, they are quite fast and the quality seems decent</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:14 UTC</span>

<span style="font-size: 90%;">Swag: I have 200 CRS stickers here now. And _@fzipitria_ has set up our online shop. I think he is almost done.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:38 UTC</span>

<span style="font-size: 90%;">That is on redbubble exactly. I did the stickers with stickermule though.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:32 UTC</span>

<span style="font-size: 90%;">this will be good because i'm working mostly on the CDN and we can link the store nicely from there</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:34 UTC</span>

<span style="font-size: 90%;">We have a paypal account for this. It was very hard to get paypal working. I had to give my private name and my private credit card information. Otherwise we would need some sort of official paper about our organisation.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:36 UTC</span>

<span style="font-size: 90%;"><http://store.coreruleset.org|store.coreruleset.org></span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:43 UTC</span>

<span style="font-size: 90%;">when its ready</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:49 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:58 UTC</span>

<span style="font-size: 90%;">(also the demo will be the same way)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:06 UTC</span>

<span style="font-size: 90%;">Problem: The money is now linked to me privately. But the hassle to do it differently is huge.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:10:07 UTC</span>

<span style="font-size: 90%;">back, sorta</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:19 UTC</span>

<span style="font-size: 90%;">i'm not really concered right now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:19 UTC</span>

<span style="font-size: 90%;">One way (that would also help to deal with the OWASP HQ hunger for money) would be to create an independent association under Swiss law (-> Friends of CRS) and then get a proper mail address and accounts and then paypal. That is done in half an hour.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:23 UTC</span>

<span style="font-size: 90%;">Welcome back.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:38 UTC</span>

<span style="font-size: 90%;">Associations are very simple in Switzerland.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:46 UTC</span>

<span style="font-size: 90%;">And quite sound legally.</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:47 UTC</span>

<span style="font-size: 90%;">oh wow that’s nice, here it’s a huge hassle</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:13 UTC</span>

<span style="font-size: 90%;">the reporting requirements in NL are not so large, but you do have to maintain a balance book and send in every year</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:14 UTC</span>

<span style="font-size: 90%;">I would prefer that sooner or later as I do not like the responsibility to take care of public money under my own name.</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:25 UTC</span>

<span style="font-size: 90%;">same for me, the domain names could get assigned there also</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:42 UTC</span>

<span style="font-size: 90%;">would be a very small load off my back</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:46 UTC</span>

<span style="font-size: 90%;">You don't around here. And especially not, if you have less than 50K cashflow per year.</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:13 UTC</span>

<span style="font-size: 90%;">awesome, do you need to be a Swiss citizen?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:16 UTC</span>

<span style="font-size: 90%;">same in the us for the most part</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:17 UTC</span>

<span style="font-size: 90%;">And I doubt redbubble would get us in that range anytime soon. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">yeah I imagine the kickback per shirt is quite small</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:49 UTC</span>

<span style="font-size: 90%;">The good thing: You can have international members in Swiss associations. It's just beneficial if the treasurer lives in Switzerland as he has to visit the bank from time to time.</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:49 UTC</span>

<span style="font-size: 90%;">they are pretty inexpensive as is</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:06 UTC</span>

<span style="font-size: 90%;">too bad the bank secrecy is gone!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:27 UTC</span>

<span style="font-size: 90%;">I do not think we need or should take a decision now, but let's keep this in mind.</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:58 UTC</span>

<span style="font-size: 90%;">as far as I’m concerned you can set it up tomorrow</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:06 UTC</span>

<span style="font-size: 90%;">Oh, the bank secrecy is still active within Switzerland. Our gov still does not get to see the domestic accounts. Crazy, but that's the law.</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:07 UTC</span>

<span style="font-size: 90%;">if I die, the domain names are in my name, it’s kind of ugly</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:18 UTC</span>

<span style="font-size: 90%;">not having concrete plans mind you</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:14:31 UTC</span>

<span style="font-size: 90%;">_@dune73_ can I print some CRS sticker from stickermule as you done?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:33 UTC</span>

<span style="font-size: 90%;">hmm that is a problem :confused:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:44 UTC</span>

<span style="font-size: 90%;">don't die walter :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:03 UTC</span>

<span style="font-size: 90%;">yes that is the best workaround, but really, it’s better if we have some official structure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:06 UTC</span>

<span style="font-size: 90%;">_@theMiddle_: Just clone the OWASP swag project, take the CRS stuff from the folder (svg) and upload to stickermule.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:15:18 UTC</span>

<span style="font-size: 90%;">oh nice, thanks</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:31 UTC</span>

<span style="font-size: 90%;">what's annoying is this is really what OWASP is supposed to give us</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:39 UTC</span>

<span style="font-size: 90%;">OK, so you all see this as a viable option in the midterm.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:09 UTC</span>

<span style="font-size: 90%;">Yes, I see OWASP the same way. But they really are a drag with accounts and everything that is meant to support us.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:56 UTC</span>

<span style="font-size: 90%;">mmhm</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:18 UTC</span>

<span style="font-size: 90%;">overall they seem great but with organizations of that size and the accounting requirements, there’s a lot of CYA</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:23 UTC</span>

<span style="font-size: 90%;">I really like most of the people at OWASP HQ, but the policies are so centralized and the system is clogged</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:26 UTC</span>

<span style="font-size: 90%;">seen similar with other nonprofits</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:37 UTC</span>

<span style="font-size: 90%;">Sure thing.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:34 UTC</span>

<span style="font-size: 90%;">I do not really see a viable alternative global structure for OWASP, but the way it is is cumbersome. We're OK for as long as we do not have to work with them. But when we do, it's always a hassle.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:04 UTC</span>

<span style="font-size: 90%;">yes, it is definitely not Lean</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:23 UTC</span>

<span style="font-size: 90%;">OK. AppSec Global in Amsterdam in September.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:32 UTC</span>

<span style="font-size: 90%;">hoping to go</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:36 UTC</span>

<span style="font-size: 90%;">but still tentative</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:40 UTC</span>

<span style="font-size: 90%;">I’ll be there of course!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:46 UTC</span>

<span style="font-size: 90%;">We agreed we would not do our community summit in Tel Aviv, but in Amsterdam. Ideally on September 25, the 3rd training day.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:49 UTC</span>

<span style="font-size: 90%;">so, “our day” will be Wednesday right?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:03 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:28 UTC</span>

<span style="font-size: 90%;">I can share that hotels are already quite booked, so I would recommend booking fast(ly)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:36 UTC</span>

<span style="font-size: 90%;">We are talking to the organisers right now to find out if they have a room for us. If not, we might need to rent.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:43 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: Did you hear that?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:00 UTC</span>

<span style="font-size: 90%;">Yes :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:01 UTC</span>

<span style="font-size: 90%;">Rent a room for the summit ourselves.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:41 UTC</span>

<span style="font-size: 90%;">We should know during the week. OK, if I send out the invitations to our contacts next week. Maybe also do a blog post again?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:21:44 UTC</span>

<span style="font-size: 90%;">Where in AMS is it?</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:53 UTC</span>

<span style="font-size: 90%;">it’s at Amsterdam RAI conference center</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:58 UTC</span>

<span style="font-size: 90%;"><https://ams.globalappsec.org/></span>

**walter** <span style="color: grey; font-size: 90%;">20:22:03 UTC</span>

<span style="font-size: 90%;">you have a citizenM close by which is quite good</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:14 UTC</span>

<span style="font-size: 90%;">Exactly my thinking. :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:22:26 UTC</span>

<span style="font-size: 90%;">Is that close to Tij?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:43 UTC</span>

<span style="font-size: 90%;">Btw: I have submitted a CRS talk. But no training (as it's turned down every single time anyways).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:50 UTC</span>

<span style="font-size: 90%;">Anybody else submitted a talk?</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:54 UTC</span>

<span style="font-size: 90%;">I don’t know what Tij is</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:22:56 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:02 UTC</span>

<span style="font-size: 90%;">unless you mean the youth theatre school Tij :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:14 UTC</span>

<span style="font-size: 90%;">I did "Wokring with PLs". What did you submit _@franbuehler_?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:23:31 UTC</span>

<span style="font-size: 90%;">brouwerij ’t IJ, but no, not close</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:24:05 UTC</span>

<span style="font-size: 90%;">my "Putting a WAF into your DevOps Pipeline" talk</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:14 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">So basically we try to arrange this like we did last year and hope some additional people show up. There are definitely more integrators in our contact list now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:55 UTC</span>

<span style="font-size: 90%;">But I would be happy if somebody else could take over the organisation of the program of the afternoon. Like the talks we did last year.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:20 UTC</span>

<span style="font-size: 90%;">(I'm running Swiss Cyber Storm 3 weeks afterwards and that's quite a big pile of work)</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:34 UTC</span>

<span style="font-size: 90%;">(tumbleweed rolls by)</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:20 UTC</span>

<span style="font-size: 90%;">I would be part of a committee but find it a bit scary to do it on my own already</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:35 UTC</span>

<span style="font-size: 90%;">what about doing it together then?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:23 UTC</span>

<span style="font-size: 90%;">I have the contacts and I can certainly put you in touch and suggest / give you advice. So together would be OK, if you can take the lead and push it. It's the pushing that I won't be able to do (based on my experience with Cyber Storm).</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:09 UTC</span>

<span style="font-size: 90%;">that sounds good!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">Thank you!!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:03 UTC</span>

<span style="font-size: 90%;">Thank you Walter.</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:28 UTC</span>

<span style="font-size: 90%;">please send me your contacts and I will make them confess</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:39 UTC</span>

<span style="font-size: 90%;">So the only thing left on the Agenda is that we should talk to Mitre and have them pull back the CVEs that are not exploitable.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:42 UTC</span>

<span style="font-size: 90%;">Will do. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:33:58 UTC</span>

<span style="font-size: 90%;">Thank you :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:52 UTC</span>

<span style="font-size: 90%;">I think either _@SpartanTri_ or _@fzipitria_ had contacts with the CVE guys... Or am I messing something up in my head?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:36:33 UTC</span>

<span style="font-size: 90%;">I don't remember</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:08 UTC</span>

<span style="font-size: 90%;">I'll look into it. Time to finish this anyways.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:49 UTC</span>

<span style="font-size: 90%;">Thank you everybody for joining. I am very happy, that we found solutions for most of the PRs. I really hope we can start August with a clean pipeline with only new PRs.</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:14 UTC</span>

<span style="font-size: 90%;">me too. :+1: </span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:38:14 UTC</span>

<span style="font-size: 90%;">Thank you, _@dune73_!</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:30 UTC</span>

<span style="font-size: 90%;">then maybe in the next meeting we can think of cutting 3.2 already, or not?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:53 UTC</span>

<span style="font-size: 90%;">Yes, that is definitely the plan. Idea is to release by AppSec in September, I think.</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:55 UTC</span>

<span style="font-size: 90%;">I have some smallish things I would like to contribute such as object injections for some runtimes/languages</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:27 UTC</span>

<span style="font-size: 90%;">Hey! Sorry, today I've begun sort of some days off ....</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:34 UTC</span>

<span style="font-size: 90%;">not sure i’ll get to it in time but you can’t live without hope</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:47 UTC</span>

<span style="font-size: 90%;">Will read everything in a bit.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:50 UTC</span>

<span style="font-size: 90%;">Would definitely be welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:15 UTC</span>

<span style="font-size: 90%;">_@fzipitria_: Was it you who was in touch with Mitre / CVE?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:50 UTC</span>

<span style="font-size: 90%;">It's about the nonworking CVEs...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:42:56 UTC</span>

<span style="font-size: 90%;">Sorry, I have to go to bed now.
Good night and bye :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:01 UTC</span>

<span style="font-size: 90%;">Time to turn in too. Good night everybody!</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:13 UTC</span>

<span style="font-size: 90%;">good night</span>

