### Mon, Aug 19th, 2024

**airween** <span style="color: grey; font-size: 90%;">18:31:45 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:48 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:17 UTC</span>

<span style="font-size: 90%;">Evening</span>

**jit** <span style="color: grey; font-size: 90%;">18:33:12 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:11 UTC</span>

<span style="font-size: 90%;">No chat tonight?</span>

**jit** <span style="color: grey; font-size: 90%;">18:36:34 UTC</span>

<span style="font-size: 90%;">Let's discuss my pending PR :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:36:40 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ wrote a message this afternoon, so I think there is a chat, but I'm not sure....</span>

**airween** <span style="color: grey; font-size: 90%;">18:36:46 UTC</span>

<span style="font-size: 90%;">Tonight will be a speciel chat: we can discuss about everything :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:44 UTC</span>

<span style="font-size: 90%;">Nothing on the agenda, so let's talk about _@jit_'s PR and then see what's left.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:39:05 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/3780](https://github.com/coreruleset/coreruleset/pull/3780) this one?</span>

**jit** <span style="color: grey; font-size: 90%;">18:40:32 UTC</span>

<span style="font-size: 90%;">Yes. Max has other ideas, so it's stalled</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:01 UTC</span>

<span style="font-size: 90%;">What did you want to discuss specifically _@jit_?</span>

**jit** <span style="color: grey; font-size: 90%;">18:42:14 UTC</span>

<span style="font-size: 90%;">Should we progress on developing the PR, or should I close it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:48 UTC</span>

<span style="font-size: 90%;">My idea was for someone to test my idea of adding `,` to the prefix, as I've mentioned in the PR. I would only close your PR if that works out as I hope. It's going to be either you or me who will do the testing, I suspect.</span>

**jit** <span style="color: grey; font-size: 90%;">18:45:02 UTC</span>

<span style="font-size: 90%;">Okay, then. Tell me what needs to be done and I'll look into it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:11 UTC</span>

<span style="font-size: 90%;">I wrote everything you should need in the PR comment. If you're not sure what to do, leave a comment there and I'll try to improve.</span>

**jit** <span style="color: grey; font-size: 90%;">18:48:22 UTC</span>

<span style="font-size: 90%;">If it's added to the cmdline processor, then we can use it in some of our assembly files. I think some assembly files already implement it</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:48 UTC</span>

<span style="font-size: 90%;">Exactly my point.</span>

**jit** <span style="color: grey; font-size: 90%;">18:49:36 UTC</span>

<span style="font-size: 90%;">Okay, will test if it works as expected, i.e blocks the payloads.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:42 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:29 UTC</span>

<span style="font-size: 90%;">Sorry, I'm in a call.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:42 UTC</span>

<span style="font-size: 90%;">I saw in the dev channel, that _@dune73_ asked us to brainstorm a rule for a "friendly CDN" (who we will not name here) could test (see agenda).</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:46 UTC</span>

<span style="font-size: 90%;">Any ideas?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:25 UTC</span>

<span style="font-size: 90%;">Personally, I'd be interested in the performance of the RCE rules, but that will probably be quite a messy experiment.</span>

**jit** <span style="color: grey; font-size: 90%;">18:51:52 UTC</span>

<span style="font-size: 90%;">But doesn't the CDN have their own WAF?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:54 UTC</span>

<span style="font-size: 90%;">Maybe something more exotic, so we could maybe determine whether we don't need that rule anymore?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:13 UTC</span>

<span style="font-size: 90%;">The might use our rules.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:28 UTC</span>

<span style="font-size: 90%;">Ok, hi everyone! :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:53 UTC</span>

<span style="font-size: 90%;">You can use the CRS in this CDN WAF. They have their own rules, but also the CRS.</span>

**jit** <span style="color: grey; font-size: 90%;">18:53:34 UTC</span>

<span style="font-size: 90%;">Double bonanza, then...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">RCE rules ++</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:15 UTC</span>

<span style="font-size: 90%;">I think we should have an idea of the amount of FPs we get with the rce rules</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">There has been many reports and issues</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:49 UTC</span>

<span style="font-size: 90%;">And a test like this could give us a proper idea on performance and FPs</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:55:10 UTC</span>

<span style="font-size: 90%;">Is there a main, single RCE rule we would want to test the most?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:55:26 UTC</span>

<span style="font-size: 90%;">The exact criteria here aren't clear, but it sounded like 1 rule we get to test</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:55:30 UTC</span>

<span style="font-size: 90%;">Or maybe 1 at a time?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:36 UTC</span>

<span style="font-size: 90%;">Probably 932230?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:37 UTC</span>

<span style="font-size: 90%;">I think the generic one that _@fzipitria_ and I developed would be interesting (932240)</span>

**jit** <span style="color: grey; font-size: 90%;">18:56:24 UTC</span>

<span style="font-size: 90%;">I was thinking one of the wordlists based rules, those are more prone to FPs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:06 UTC</span>

<span style="font-size: 90%;">240 is PL2 right?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">Yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:55 UTC</span>

<span style="font-size: 90%;">The only thing is that _@Esad Cetiner_ and I are currently trying to improve the RCE rules, so they are going to change slightly in the next week or two (hopefully). So if we wanted to test those rules we should wait until we've merged the change.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:06 UTC</span>

<span style="font-size: 90%;">932230 and 932240 are **very** good candidates</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">Yes</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:13 UTC</span>

<span style="font-size: 90%;">And yes, we should do that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:21 UTC</span>

<span style="font-size: 90%;">Wait a couple of weeks won't hurt.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:35 UTC</span>

<span style="font-size: 90%;">But we are targeting probably v4.7.0, right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:49 UTC</span>

<span style="font-size: 90%;">Yes, probably</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:55 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:26 UTC</span>

<span style="font-size: 90%;">Probably it would take some time to get all the things in place, but we can say we are targeting the test for that release</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:58 UTC</span>

<span style="font-size: 90%;">And I think it will help if we tell that sooner so their teams can do their preparation</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:02 UTC</span>

<span style="font-size: 90%;">4.6  is this week?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:08 UTC</span>

<span style="font-size: 90%;">Yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:20 UTC</span>

<span style="font-size: 90%;">Let's say 4.8. I'd rather do this right.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:42 UTC</span>

<span style="font-size: 90%;">Sounds good. 4.8 will be by October</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:11 UTC</span>

<span style="font-size: 90%;">Any other candidates?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:11 UTC</span>

<span style="font-size: 90%;">The weeks before our retreat</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:34 UTC</span>

<span style="font-size: 90%;">Hmmm</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:53 UTC</span>

<span style="font-size: 90%;">What about the logical rule for sql?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:02:32 UTC</span>

<span style="font-size: 90%;">That one too, yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:12 UTC</span>

<span style="font-size: 90%;">The rules that _@xanadu_ had analysed would also be nice. To compare the corpus analysis against real world traffic.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:32 UTC</span>

<span style="font-size: 90%;">That one too, yes.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:02:32 UTC</span>

<span style="font-size: 90%;">That one too, yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:39 UTC</span>

<span style="font-size: 90%;">Definitely.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:56 UTC</span>

<span style="font-size: 90%;">I guess at this point we should be going for a wiki page with a list.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:16 UTC</span>

<span style="font-size: 90%;">With priorities and the "why" we want to test that rule?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:27 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:31 UTC</span>

<span style="font-size: 90%;">Perfect</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:41 UTC</span>

<span style="font-size: 90%;">I'll create the page, add the ones mentioned here</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:04:34 UTC</span>

<span style="font-size: 90%;">Yes, sounds good. I can also have a look at my tunings and what rules I often find and tune. Maybe I can add these rules there too.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:14 UTC</span>

<span style="font-size: 90%;">Ok. Any other topics we should discuss tonight?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:44 UTC</span>

<span style="font-size: 90%;">Just let you know that I'm working with Starr Brown on getting all set for the developer retreat asap.</span>

**jit** <span style="color: grey; font-size: 90%;">19:07:36 UTC</span>

<span style="font-size: 90%;">I won't be able to come :unamused:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:52 UTC</span>

<span style="font-size: 90%;">Bummer. Maybe next year.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:11 UTC</span>

<span style="font-size: 90%;">And I have a document (locally) with topics for the retreat that I will be sharing soon</span>

**azurit** <span style="color: grey; font-size: 90%;">19:08:14 UTC</span>

<span style="font-size: 90%;">Hi</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:35 UTC</span>

<span style="font-size: 90%;">Right. Let's call it an evening then. Unless _@azurit_ has something urgent to discuss?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:08:56 UTC</span>

<span style="font-size: 90%;">No, thanks.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:09:23 UTC</span>

<span style="font-size: 90%;">I'm sorry i missed it all.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:36 UTC</span>

<span style="font-size: 90%;">No worries. Good night everyone!</span>

**azurit** <span style="color: grey; font-size: 90%;">19:09:41 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:09:44 UTC</span>

<span style="font-size: 90%;">Good night</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:48 UTC</span>

<span style="font-size: 90%;">Night.</span>

**jit** <span style="color: grey; font-size: 90%;">19:09:58 UTC</span>

<span style="font-size: 90%;">Goodnight :sleeping::zzz::zzz:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:05 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**airween** <span style="color: grey; font-size: 90%;">19:12:49 UTC</span>

<span style="font-size: 90%;">GN</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:41 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3785#issuecomment-2297258938](https://github.com/coreruleset/coreruleset/issues/3785#issuecomment-2297258938)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:25:39 UTC</span>

<span style="font-size: 90%;">Started with [https://github.com/coreruleset/coreruleset/wiki/Project-for-CDN-testing-CRS-rules](https://github.com/coreruleset/coreruleset/wiki/Project-for-CDN-testing-CRS-rules)</span>

