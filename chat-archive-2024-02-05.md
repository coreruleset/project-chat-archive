### Mon, Feb 5th, 2024

**maxleske** <span style="color: grey; font-size: 90%;">19:30:10 UTC</span>

<span style="font-size: 90%;">:blob-wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">Hey, hey, time for the meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:23 UTC</span>

<span style="font-size: 90%;">Please find the agenda at [https://github.com/coreruleset/coreruleset/issues/3529](https://github.com/coreruleset/coreruleset/issues/3529)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:38 UTC</span>

<span style="font-size: 90%;">And thank you all for helping to fill it out. This has been a real collaborative effort.</span>

**jit** <span style="color: grey; font-size: 90%;">19:30:47 UTC</span>

<span style="font-size: 90%;">Hi everyone :slightly_smiling_face:</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">19:31:43 UTC</span>

<span style="font-size: 90%;">:saluting_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">Good evening/night/morning !</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:04 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:13 UTC</span>

<span style="font-size: 90%;">'evening</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:47 UTC</span>

<span style="font-size: 90%;">Good evening </span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:58 UTC</span>

<span style="font-size: 90%;">Good to see you all.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:12 UTC</span>

<span style="font-size: 90%;">Wondering if _@fzipitria_ is also here.</span>

**Edgars Voroboks** <span style="color: grey; font-size: 90%;">19:33:17 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:35 UTC</span>

<span style="font-size: 90%;">Franziska excused herself since she is on holiday.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:15 UTC</span>

<span style="font-size: 90%;">Other than that, important discussion tonight, since we need to define the release plan - for next week!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:07 UTC</span>

<span style="font-size: 90%;">I'm here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:09 UTC</span>

<span style="font-size: 90%;">That's also why _@Alessandro Monachesi_ joined us. Glad he could make it on relatively short notice. (_@Edgars Voroboks_ Alessandro is a hand that CRS hires for occasional PR support).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:22 UTC</span>

<span style="font-size: 90%;">Good to see you _@fzipitria_.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">Me too :sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:40 UTC</span>

<span style="font-size: 90%;">So biggest news is apparently the start of OWASP ModSecurity. Suddenly, everything was very fast.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:10 UTC</span>

<span style="font-size: 90%;">But the first release under the OWASP roof is done and everybody is now waiting for the CRS release.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:05 UTC</span>

<span style="font-size: 90%;">I got the understanding our containers are affected by security problem on the OS level. What is the status here.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:25 UTC</span>

<span style="font-size: 90%;">No, they are not necessarily.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">In general, base images may be compromised but that's unlikely in our case.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:39 UTC</span>

<span style="font-size: 90%;">Very good. I'll add that to the security status.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:30 UTC</span>

<span style="font-size: 90%;">I wrote the following about the rule situation (with updates by other team members):

* Hard technical bugs with v4 are fixed, what remains is work on FPs (only major rule left is 932236, is being actively discussed) and non-critical bugs.

Is this correct? I just want to be double sure.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:10 UTC</span>

<span style="font-size: 90%;">_@jit_ can you please confirm that none of the bypasses you reported are pressing or persisting problems for the release of v4 (I think it's all solved.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:41:50 UTC</span>

<span style="font-size: 90%;">None whatsoever. Everything is fixed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:55 UTC</span>

<span style="font-size: 90%;">Hmm. So do we agree we are technically ready for the release? (Sorry to pester everybody, but I want to be double sure)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:35 UTC</span>

<span style="font-size: 90%;">IMO yes, once we've looked at the open issues from _@xanadu_'s analysis (932236 mainly)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:01 UTC</span>

<span style="font-size: 90%;">But even if, that would not be a deal breaker or do you think it would?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:23 UTC</span>

<span style="font-size: 90%;">If yes, we need a plan. If not, I think we just let it roll.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:30 UTC</span>

<span style="font-size: 90%;">Probably not, if we're willing to live with the FPs</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:38 UTC</span>

<span style="font-size: 90%;">It's a new rule in 4.0 that adds many FPs. That's the context.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:45:06 UTC</span>

<span style="font-size: 90%;">If it is not fixable quickly, we can instruct users to write rule exclusions and fix in the future.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:22 UTC</span>

<span style="font-size: 90%;">Exactly my thinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:56 UTC</span>

<span style="font-size: 90%;">Good, good.
_@fzipitria_ You looked into the sandbox today / yesterday. How is the situation? (It better be ready for CRS v4 and people wanting to test).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:22 UTC</span>

<span style="font-size: 90%;">The sandbox will be working for the release</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:42 UTC</span>

<span style="font-size: 90%;">We still need to push new containers for the release, once its out there</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:29 UTC</span>

<span style="font-size: 90%;">Sure thing. There was (is?) a bit of a mess with the selection of CRS version via header. Andrea promised to fix this in Autumn, but I think he never delivered. Do you have an overview of this?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:39 UTC</span>

<span style="font-size: 90%;">Nope</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:47 UTC</span>

<span style="font-size: 90%;">If there is a ticket, I can try to follow up</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:53 UTC</span>

<span style="font-size: 90%;">...time permits</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:49:21 UTC</span>

<span style="font-size: 90%;">Good evening. Sorry I'm late</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:34 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/crs-sandbox/issues/67](https://github.com/coreruleset/crs-sandbox/issues/67)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:40 UTC</span>

<span style="font-size: 90%;">Hello _@Paul Beckett_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:28 UTC</span>

<span style="font-size: 90%;">Can you self-assign this _@fzipitria_ or do we want to give it to somebody else?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:50:55 UTC</span>

<span style="font-size: 90%;">I'm probably going to destroy the sandbox and start from scratch</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:10 UTC</span>

<span style="font-size: 90%;">If we could clean this up for 4.0, it would be really good, since it's really hard to use the sandbox if you are not sure what version is giving you these results.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">Is it so bad, we have to start over? That sounds like undocumented and not properly deployed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:25 UTC</span>

<span style="font-size: 90%;">But anyways, is there more on the status of individual projects?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:53:22 UTC</span>

<span style="font-size: 90%;">I reviewed my pending issues/PR's, and found these ones:

[https://github.com/coreruleset/coreruleset/issues/3428](https://github.com/coreruleset/coreruleset/issues/3428)

[https://github.com/coreruleset/coreruleset/issues/2390](https://github.com/coreruleset/coreruleset/issues/2390)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:36 UTC</span>

<span style="font-size: 90%;">Personally, I'm done and I think we can move on.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:13 UTC</span>

<span style="font-size: 90%;">We've merged the schema PR for go-ftw today, so I can move forward with implementing the necessary changes for us to run the nginx test suite</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:22 UTC</span>

<span style="font-size: 90%;">I reviewed my pending issues/PR's, and found these ones:

[https://github.com/coreruleset/coreruleset/issues/3428](https://github.com/coreruleset/coreruleset/issues/3428)

[https://github.com/coreruleset/coreruleset/issues/2390](https://github.com/coreruleset/coreruleset/issues/2390)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:53:22 UTC</span>

<span style="font-size: 90%;">I reviewed my pending issues/PR's, and found these ones:

[https://github.com/coreruleset/coreruleset/issues/3428](https://github.com/coreruleset/coreruleset/issues/3428)

[https://github.com/coreruleset/coreruleset/issues/2390](https://github.com/coreruleset/coreruleset/issues/2390)</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:38 UTC</span>

<span style="font-size: 90%;">we can fix the first one easily</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:02 UTC</span>

<span style="font-size: 90%;">That would be nice one to fix before the release.</span>

**airween** <span style="color: grey; font-size: 90%;">19:54:18 UTC</span>

<span style="font-size: 90%;">the second one... well, I think we can skip that - but most problem was solved meantime in the engine :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:29 UTC</span>

<span style="font-size: 90%;">The recommended rules are not so important anymore, I think, since I find the ModSecurity project being much more open for improvements...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:28 UTC</span>

<span style="font-size: 90%;">Good. So let's move to project discussions.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:56 UTC</span>

<span style="font-size: 90%;">I've added GSoC to the agenda. We were very late last year and promised to be there from the beginning this year. That's about now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:13 UTC</span>

<span style="font-size: 90%;">But the question is, do we want to do this again / can we do this again?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:57:29 UTC</span>

<span style="font-size: 90%;">Especially with the release...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:45 UTC</span>

<span style="font-size: 90%;">It is / was meant to be a recruitment device, but this does not really work (and it's not only our fault, other OWASP projects report the same).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:12 UTC</span>

<span style="font-size: 90%;">And honestly, we have a bit of a hard time bringing the PoC GSoC results into a production ready state.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:51 UTC</span>

<span style="font-size: 90%;">Not being able to run the performance measuring framework from 2023 will be painful moving forward (and I really think we must try hard to make this one work).</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:22 UTC</span>

<span style="font-size: 90%;">If we don't have a solid gold idea for an awesome GSoC project (I don't think we do right now, do we?) then could we take 2024 off as a break year? And rejoin in 2025?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:26 UTC</span>

<span style="font-size: 90%;">We can totally make a return in 2025. There is no pressure in this regard.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:49 UTC</span>

<span style="font-size: 90%;">What do you think _@fzipitria_ - you did most of the coaching work last year.</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:37 UTC</span>

<span style="font-size: 90%;">just one more question regarding to release of v4.0: do we want to close this before the release?

[https://github.com/coreruleset/coreruleset/pull/3347](https://github.com/coreruleset/coreruleset/pull/3347)</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:07 UTC</span>

<span style="font-size: 90%;">then we can left the 3.2 with a final patch</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:15 UTC</span>

<span style="font-size: 90%;">_@emphazer_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:18 UTC</span>

<span style="font-size: 90%;">_@emphazer_ How close is this? _@fzipitria_ would prefer to get rid of 3.2 the moment we release 4.0.
This idea would go a bit against this.</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:08 UTC</span>

<span style="font-size: 90%;">I understand, this is why I asked: that would be the last update</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:19 UTC</span>

<span style="font-size: 90%;">and it's not so big effort</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:55 UTC</span>

<span style="font-size: 90%;">there are few reviews, if _@emphazer_ fixes them, I can make a release - and that's it</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:05:48 UTC</span>

<span style="font-size: 90%;">It doesn't look hard to fix. Anybody could do it.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:06:15 UTC</span>

<span style="font-size: 90%;">I know... if _@emphazer_ does not enough time I can make it</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:06:47 UTC</span>

<span style="font-size: 90%;">Let me do it, then you can stay the reviewer</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:10 UTC</span>

<span style="font-size: 90%;">I'll make the changes you requested tomorrow.</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:15 UTC</span>

<span style="font-size: 90%;">I know... if _@emphazer_ does not enough time I can make it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:06:15 UTC</span>

<span style="font-size: 90%;">I know... if _@emphazer_ does not enough time I can make it</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:06:47 UTC</span>

<span style="font-size: 90%;">Let me do it, then you can stay the reviewer</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:01 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ are you OK with a final 3.2 release? This would go out together with 4.0.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">Well, I guess that means we do it if it's ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:21 UTC</span>

<span style="font-size: 90%;">And no loud voices for GSoC participation. I think _@xanadu_ is right, that we have ideas, but not really a striking topic.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:00 UTC</span>

<span style="font-size: 90%;">For the record: Here are our current ideas: [https://github.com/coreruleset/coreruleset/wiki/DevRetreat23DiscussionGSoC2024](https://github.com/coreruleset/coreruleset/wiki/DevRetreat23DiscussionGSoC2024)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:28 UTC</span>

<span style="font-size: 90%;">I don't think we need a v3.2 version. It is a 6 years old branch. ¯\\\_(ツ)\_/¯</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:09 UTC</span>

<span style="font-size: 90%;">And I would not waste one cpu cycle from anyone unless v4 is out</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:25 UTC</span>

<span style="font-size: 90%;">We technically still need to do work on plugins. I mean, writing tests.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:35 UTC</span>

<span style="font-size: 90%;">It is true that those who care about security did not stay on 3.2, but updated in the meantime. So we probably only have 3.2 users who won't be bothered to update anyway.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:01 UTC</span>

<span style="font-size: 90%;">But if it's almost free for us, I would not mind. I'm open either way.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:39 UTC</span>

<span style="font-size: 90%;">If that's the case then I wouldn't do it. We don't really have the means to test it without _@emphazer_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:44 UTC</span>

<span style="font-size: 90%;">Well, my wording may be a bit strong ... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:22 UTC</span>

<span style="font-size: 90%;">_@airween_: Any hard feelings if we drop this?</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:12 UTC</span>

<span style="font-size: 90%;">no - but we are almost done with it, so... I feel that would be the wasted time :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:35 UTC</span>

<span style="font-size: 90%;">Technically correct, but this was too long in the making.</span>

**airween** <span style="color: grey; font-size: 90%;">20:17:41 UTC</span>

<span style="font-size: 90%;">okay</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:12 UTC</span>

<span style="font-size: 90%;">Good, so CRS v4 release planning.</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:41 UTC</span>

<span style="font-size: 90%;">do we want so cancel for good (close the PR) or want to open it later?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:00 UTC</span>

<span style="font-size: 90%;">I've closed it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:39 UTC</span>

<span style="font-size: 90%;">The big things to do for v4 is describe it (anew) in a blog post and to update the changelog.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:15 UTC</span>

<span style="font-size: 90%;">Unfortunately, there are still some 200-300 items that have to be rewritten into the new stricter format. This includes rule id and PL lookup.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:53 UTC</span>

<span style="font-size: 90%;">Lately I thought that the lookups can be automated as can the mapping of the author. And once that is there, the rewriting with the more formal description is relatively easy.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:46 UTC</span>

<span style="font-size: 90%;">[I just shared a new draft for the release poster on the dev channel. Please comment there.]</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:49 UTC</span>

<span style="font-size: 90%;">We can split those among us again, like we did last time</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:23 UTC</span>

<span style="font-size: 90%;">Agreed: once we established clear guidelines it was actually not too difficult.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:32 UTC</span>

<span style="font-size: 90%;">Just repetition.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:09 UTC</span>

<span style="font-size: 90%;">OK. But do we want to try to automate the lookup first? Because this is now the hard work. Rewriting is indeed very simple.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:23:24 UTC</span>

<span style="font-size: 90%;">Sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:50 UTC</span>

<span style="font-size: 90%;">GH cli should make that relatively easy, I think.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:25:04 UTC</span>

<span style="font-size: 90%;">Yes, probably</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:59 UTC</span>

<span style="font-size: 90%;">I'll give it a go and then we share the rewording, OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:54 UTC</span>

<span style="font-size: 90%;">As for the blog post. This will apparently be lengthy. It has to cover the biggest new features and maybe tell the story of v4 as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:10 UTC</span>

<span style="font-size: 90%;">The changelog has a list of the features we think are big.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:59 UTC</span>

<span style="font-size: 90%;">There is also technical documentation or blog posts that would help (on individual plugins, migrating from 3.3 to 4.0) but I think this does not necessarily have to be there for 4.0.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:57 UTC</span>

<span style="font-size: 90%;">The big installations won't migrate on day 1, so even if we would love to have transformation scripts and stuff, we can release without and then create those based on demand (personally, I think describing a setup to run the two rule sets in parallel would be useful).</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:34 UTC</span>

<span style="font-size: 90%;">would it be help if I make the "rule-diff"? I can make it in text and JSON format (see this message: [https://owasp.slack.com/archives/G01K88J8SDB/p1698351987849589](https://owasp.slack.com/archives/G01K88J8SDB/p1698351987849589))</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:48 UTC</span>

<span style="font-size: 90%;">I think this would be nice to have it as a supplement document, but I do not see it as central, since people are not used to this format (in comparison to a good old changelog).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:59 UTC</span>

<span style="font-size: 90%;">So I would link it from the blog post / release notes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:48 UTC</span>

<span style="font-size: 90%;">_@xanadu_ and _@Alessandro Monachesi_: Is this blog post / release notes document something you could work on together?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:38:18 UTC</span>

<span style="font-size: 90%;">I'd be happy to help with the release notes / technical part. I guess because 4.0.0 is a big, milestone release, it will be more of a press release sort of feel? Which I would definitely leave to the expertise of _@Alessandro Monachesi_ :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:08 UTC</span>

<span style="font-size: 90%;">I wonder how much press release style we want to do. Alessandro talked about a formal press release, but I do not really see much sense in this. The cool think is the technical part and people who do not understand the technical part will wait for commercial integrators or engineers to bring it to them, don't they?</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:42:20 UTC</span>

<span style="font-size: 90%;">Sure! I guess I will need to discuss the contents with _@dune73_ and then ask _@xanadu_ for help with the technical details. But I agree with _@xanadu_ that the text probably doesn’t have to be too technical and more strategic.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:43:03 UTC</span>

<span style="font-size: 90%;">I dont’t think we need a real press release. But probably a text that conveys the bigger picture for the  v4 release.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:41 UTC</span>

<span style="font-size: 90%;">Yes, true.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:10 UTC</span>

<span style="font-size: 90%;">So the idea is I transport the stuff in the Changelog to Alessandro, he makes it into a big text and _@xanadu_ reviews?</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:44:20 UTC</span>

<span style="font-size: 90%;">We could always go into the interesting technical details in separate blog posts later</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:28 UTC</span>

<span style="font-size: 90%;">That's my thinking.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:44:50 UTC</span>

<span style="font-size: 90%;">Works for me. _@xanadu_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:51 UTC</span>

<span style="font-size: 90%;">I would say that we need to present only a big picture</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:00 UTC</span>

<span style="font-size: 90%;">In an ideal world, we had prepared those in the time leading up to the release, but this did not go ideally.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:45:16 UTC</span>

<span style="font-size: 90%;">Sure, drop me a line if and when I can be of help and I will :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:23 UTC</span>

<span style="font-size: 90%;">And we need to talk about the quality improvements</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:30 UTC</span>

<span style="font-size: 90%;">The QT framework, etc.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:45:32 UTC</span>

<span style="font-size: 90%;">Happy to review / write / assist with whatever bits of technical copy etc.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:42 UTC</span>

<span style="font-size: 90%;">QT == Quantitative Testing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:46:15 UTC</span>

<span style="font-size: 90%;">And also that people need to expect releases with a cadence, in the future</span>

**dune73** <span style="color: grey; font-size: 90%;">20:47:31 UTC</span>

<span style="font-size: 90%;">Good thinking. There should be a roadmap section. This can also have a few remarks on OWASP ModSecurity.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:04 UTC</span>

<span style="font-size: 90%;">Anything else on v4?</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">20:48:42 UTC</span>

<span style="font-size: 90%;">May I ask all of you: What do you think are the highlights of v4?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:49:07 UTC</span>

<span style="font-size: 90%;">plugins</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:49:25 UTC</span>

<span style="font-size: 90%;">better spread of rules over PL levels</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:49:55 UTC</span>

<span style="font-size: 90%;">work on quality (qt framework, automation, more tests)</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">All(?) of the old regular expression patterns have been broken up into clean and maintainable formats (lots of tidying)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:53 UTC</span>

<span style="font-size: 90%;">All of the above plus better coverage thanks to Bug Bounty program.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:51:14 UTC</span>

<span style="font-size: 90%;">150 (bug bounty) findings incorporated into v4.0?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:51:20 UTC</span>

<span style="font-size: 90%;">Or some similarly impressive number</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:57 UTC</span>

<span style="font-size: 90%;">It's ~ 510 individual findings in 180 reports ...</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:53:09 UTC</span>

<span style="font-size: 90%;">Ah, yes, reports I was thinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:12 UTC</span>

<span style="font-size: 90%;">And a changelog consisting of X entries.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:53:51 UTC</span>

<span style="font-size: 90%;">number of merged PRs would also be cool to see</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:49 UTC</span>

<span style="font-size: 90%;">That's the one I have in mind. It's a mindblowing number.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:51 UTC</span>

<span style="font-size: 90%;">Which plugins are going to be included in this release?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:06 UTC</span>

<span style="font-size: 90%;">We moved stuff from the core to plugins</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:12 UTC</span>

<span style="font-size: 90%;">Which ones will be supported?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:16 UTC</span>

<span style="font-size: 90%;">They are only being linked.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:48 UTC</span>

<span style="font-size: 90%;">It is a big change for those who used exceptions</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:52 UTC</span>

<span style="font-size: 90%;">I'd say we support the official ones. But several ones of them are not as well tested as they should be (which is in fact no difference to 3.3)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:58 UTC</span>

<span style="font-size: 90%;">I'd say the plugins are linked.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:37 UTC</span>

<span style="font-size: 90%;">Maybe the release notes link the plugin registry. Or they have individual links to the rule exclusions plugins and then some more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:43 UTC</span>

<span style="font-size: 90%;">I see your question makes sense.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:52 UTC</span>

<span style="font-size: 90%;">Do you want to come up with a list, or should I make a proposal with Alessandro and then the team reviews?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:58:36 UTC</span>

<span style="font-size: 90%;">The plugin registry already lists which plugins are tested. Shouldn't we just use that list?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:12 UTC</span>

<span style="font-size: 90%;">Yes. But it really looks better if we make direct links and don't throw people with existing rule exclusion package usage onto the plugin registry.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:21 UTC</span>

<span style="font-size: 90%;">Do we want to link the ones we have tested?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:33 UTC</span>

<span style="font-size: 90%;">And link the plugin registry for the rest?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:59:55 UTC</span>

<span style="font-size: 90%;">That's what I meant</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:48 UTC</span>

<span style="font-size: 90%;">Then let's use this as a base and you guys can always review.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:23 UTC</span>

<span style="font-size: 90%;">So we move to the final point on the agenda?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:43 UTC</span>

<span style="font-size: 90%;">So we have this in the agenda:

fix: add = prefix to RCE rules and remove ^ from rule 932236 (PL2) [#3531](https://github.com/coreruleset/coreruleset/issues/#3531) -> PR tries to solve natural language FP in 932236 at PL2 (Natural language FPs with rule 932236 PL2 [#3511](https://github.com/coreruleset/coreruleset/issues/#3511)). BUT if we remove the start of string ^, 8 tests are failing. Is the removing of ^ safe enough and do we want to adjust the tests (some of them BB)? @franbuehler could work on this from Saturday on again or someone else can take it if that's too late.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:05:44 UTC</span>

<span style="font-size: 90%;">The issue I was looking for the BB data for is a different one.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">21:07:18 UTC</span>

<span style="font-size: 90%;">Ah, sorry. I messed this up then.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:34 UTC</span>

<span style="font-size: 90%;">I think we are a bit in the dark with regards to the bug bounty findings here, since we lost access to the Intigrity program. _@fzipitria_ you said you could recover the data. Any success?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:01 UTC</span>

<span style="font-size: 90%;">No, I said I was going to see what was happening</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:11 UTC</span>

<span style="font-size: 90%;">I guess we all were kicked out?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:05:29 UTC</span>

<span style="font-size: 90%;">(I was.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:05:44 UTC</span>

<span style="font-size: 90%;">The issue I was looking for the BB data for is a different one.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:05:44 UTC</span>

<span style="font-size: 90%;">The issue I was looking for the BB data for is a different one.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">21:07:18 UTC</span>

<span style="font-size: 90%;">Ah, sorry. I messed this up then.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:31 UTC</span>

<span style="font-size: 90%;">Yes, we were kicked out.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:36 UTC</span>

<span style="font-size: 90%;">So not even you have access?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:52 UTC</span>

<span style="font-size: 90%;">Should I initiate contact with Intigriti anew and ask for a dump?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:08:21 UTC</span>

<span style="font-size: 90%;">That would probably be enough. We don't need the accounts necessarily</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:53 UTC</span>

<span style="font-size: 90%;">I took note.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:09 UTC</span>

<span style="font-size: 90%;">Do we need this immediately / before v.4 or is 2-3 weeks enough?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:10:55 UTC</span>

<span style="font-size: 90%;">The PR was already merged after _@fzipitria_ had agreed with my assessment. So it's no longer urgent.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:11:15 UTC</span>

<span style="font-size: 90%;">For the record, this is that PR: [https://github.com/coreruleset/coreruleset/pull/3528](https://github.com/coreruleset/coreruleset/pull/3528)</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:17 UTC</span>

<span style="font-size: 90%;">Got you. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:00 UTC</span>

<span style="font-size: 90%;">What do we do with the item on the agenda? The question Franziska posed stands.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:13:31 UTC</span>

<span style="font-size: 90%;">I've opened an alternative PR, _@xanadu_ has already run the numbers against it. I want to run another test with the start of string match removed to see the difference. When that is done I think we'll have enough information to decide how to proceed.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:11 UTC</span>

<span style="font-size: 90%;">So you guys can take this on and if unsure you report back?</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:14:18 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:14 UTC</span>

<span style="font-size: 90%;">Sounds cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:16:11 UTC</span>

<span style="font-size: 90%;">This seems to be the end of it. I suggest we define next Monday for a formal GO/NO-GO decision for the release. OK?</span>

**jit** <span style="color: grey; font-size: 90%;">21:16:19 UTC</span>

<span style="font-size: 90%;">Goodnight everyone :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:22 UTC</span>

<span style="font-size: 90%;">Thank you all for participating! And good night.</span>

**Alessandro Monachesi** <span style="color: grey; font-size: 90%;">21:17:29 UTC</span>

<span style="font-size: 90%;">Goodnight or whatever time of day it is!:wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:17:39 UTC</span>

<span style="font-size: 90%;">bb</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:17:44 UTC</span>

<span style="font-size: 90%;">Night night</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:18:15 UTC</span>

<span style="font-size: 90%;">Thanks to all of you, night!</span>

**airween** <span style="color: grey; font-size: 90%;">21:18:54 UTC</span>

<span style="font-size: 90%;">good night!</span>

