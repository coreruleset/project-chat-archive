### Mon, Dec 4th, 2023

**maxleske** <span style="color: grey; font-size: 90%;">19:30:07 UTC</span>

<span style="font-size: 90%;">Hi  all!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:31 UTC</span>

<span style="font-size: 90%;">Hi everyone!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:50 UTC</span>

<span style="font-size: 90%;">Welcome to the latest monthly chat for 2023! :tada:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:19 UTC</span>

<span style="font-size: 90%;">Hey, hey.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:34 UTC</span>

<span style="font-size: 90%;">The agenda for tonight is now at [https://github.com/coreruleset/coreruleset/issues/3398](https://github.com/coreruleset/coreruleset/issues/3398)</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:52 UTC</span>

<span style="font-size: 90%;">hi all</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:28 UTC</span>

<span style="font-size: 90%;">Let's do a quick round with the things that happened in the last month (other than our retreat)</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:36 UTC</span>

<span style="font-size: 90%;">Heyhoo</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:46 UTC</span>

<span style="font-size: 90%;">Hey</span>

**jit** <span style="color: grey; font-size: 90%;">19:32:56 UTC</span>

<span style="font-size: 90%;">Hi everyone...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:08 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:33:12 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:51 UTC</span>

<span style="font-size: 90%;">Folks from [https://www.opencre.org/](https://www.opencre.org/) contacted us to talk about CAPEC tags. So I think the work we did some years ago would be productive to others. I'm wondering if we have all our stuff in place for the new rules in v4 :thinking_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">Maybe we can do a quick script for checking the tags we had in v3.3.5 and the ones that changed in v4? _@airween_ Is this something that we might do quickly with the msc_pyparser?</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:20 UTC</span>

<span style="font-size: 90%;">yes, this is what I think about - I can take it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">Sure. I'll create the ticket after the chat.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:58 UTC</span>

<span style="font-size: 90%;">A new similar tool for testing using cli instead of using the sandbox: [https://github.com/AvalZ/modsecurity-cli](https://github.com/AvalZ/modsecurity-cli)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:28 UTC</span>

<span style="font-size: 90%;">Probably similar to what (again _@airween_) has written with his tester. But only supports v3.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:37:06 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:18 UTC</span>

<span style="font-size: 90%;">yes, it's similar. Last year (or two years ago) I completely rewritten that tool with version 1.0, the next plan is add something like those guys did</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:33 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:34 UTC</span>

<span style="font-size: 90%;">and yes, these tools supports only v3</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:57 UTC</span>

<span style="font-size: 90%;">but my tool supports Coraza too :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:05 UTC</span>

<span style="font-size: 90%;">:coraza-party:</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:13 UTC</span>

<span style="font-size: 90%;">(if that would have C bindings :disappointed:)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:40:19 UTC</span>

<span style="font-size: 90%;">Moving on: of course the community is getting nervous about the future of modsecurity. I don't think we should mention anything specific, other than there are efforts coming along the way to see how OWASP can help.</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:11 UTC</span>

<span style="font-size: 90%;">yes, I saw few tweets on Twitter, and I think too community are completely confused</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:18 UTC</span>

<span style="font-size: 90%;">We did implement tests, so there is an 80% coverage for PL1 isolated tests for the status page :tada:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:02 UTC</span>

<span style="font-size: 90%;">We detected a problem in the CRS sandbox that was unresponsive because of a filesystem got full. ¯\\\_(ツ)\_/¯</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:31 UTC</span>

<span style="font-size: 90%;">So now we increased disk space and managed to cleanup things a bit. This will give us more peace of mind in the future.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">The CRS Project is discussing a Security finding. We are going to handle this next in the discussions part.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:53 UTC</span>

<span style="font-size: 90%;">We fixed FPs in the nextcloud and WP plugins for v4.</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:35 UTC</span>

<span style="font-size: 90%;">FS is full by what?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:47 UTC</span>

<span style="font-size: 90%;">Logs. And containers.</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:50 UTC</span>

<span style="font-size: 90%;">(I'm just curious)</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:54 UTC</span>

<span style="font-size: 90%;">okay</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:57 UTC</span>

<span style="font-size: 90%;">thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:04 UTC</span>

<span style="font-size: 90%;">There is [https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/](https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/) in owncloud, I assume we might do something about it if it is not catched already. The fix is easy, btw.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:47:19 UTC</span>

<span style="font-size: 90%;">And you must run it in a container. So it depends in thedeployment. But having a 10.0 in CVSS is something crazy to see.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:42 UTC</span>

<span style="font-size: 90%;">There is a new tool proposal for changelog update automation, so that's cool.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:31 UTC</span>

<span style="font-size: 90%;">And you probably saw the blog posts related to the developer retreat, along with some new developer portraits! :party-crs:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:53 UTC</span>

<span style="font-size: 90%;">Big shout to _@Alessandro Monachesi_ for covering those</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:50:28 UTC</span>

<span style="font-size: 90%;">And we are glad he didn't ended being The gratest Dalmuti of all times :rolling_on_the_floor_laughing:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:00 UTC</span>

<span style="font-size: 90%;">I would like to start with the big topics for today.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:39 UTC</span>

<span style="font-size: 90%;">We need to define the course of action around security issue V3E. The issue is documented in private security tracker repo, along with technical details.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:08 UTC</span>

<span style="font-size: 90%;">In general, we the CRS project have been deeply involved with vendors to find solutions to problems we are concerned that might impact CRS users.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:03 UTC</span>

<span style="font-size: 90%;">Response times have been.. decent in past issues, but sometimes we didn't got to a common ground whether something should be fixed at the engine level or at the ruleset level.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:55:08 UTC</span>

<span style="font-size: 90%;">We had some reasonable response until this past week. We are still working towards bringing this to a safe place for everyone.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:07 UTC</span>

<span style="font-size: 90%;">But the uncertainty about this has prompted us to have something that could work as a workaround. Is this solution perfect? Well... not really. Because we think if the engines implement this as stated in the documentation, it should work as we use it in out ruleset.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:37 UTC</span>

<span style="font-size: 90%;">Now, because of the way we consider changes, we might live with this temporary, somehow imperfect solution for a long time. If we think CRS v4.x, of course.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:29 UTC</span>

<span style="font-size: 90%;">On the other hand, we won't rely on how engines implement this specific part, giving us more freedom to decide, independent on what the engines decido to do in the future.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:25 UTC</span>

<span style="font-size: 90%;">But... let's not forget this is a problem in the engine that makes us create workarounds to fix it to a standard behavior across our rules.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:12 UTC</span>

<span style="font-size: 90%;">So, in summary, we have established contacts and we have some reasonable feedback.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:02:04 UTC</span>

<span style="font-size: 90%;">BUT, this might just not be fixed in the engine in the near future. So this is where we need to find out and decide what to do next.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:02:49 UTC</span>

<span style="font-size: 90%;">Should we wait for, let's say, till the issues chat to have an answer form the vendor, and see if this is going to be fixed and when?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:05 UTC</span>

<span style="font-size: 90%;">If not, we can decide to just push our workaround, but we will carry it for a long time, knowing that this might be fixed by someone else in the next 6 months.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:26 UTC</span>

<span style="font-size: 90%;">Hopefully this is a reasonable introduction.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:44 UTC</span>

<span style="font-size: 90%;">Now, someone has an opinion on what to do next?</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:52 UTC</span>

<span style="font-size: 90%;">I think we can say to the vendor that we will fix this issue till the issue chat. If we will fix it, we must append some comment, why do we do that (also would communicate this).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:21 UTC</span>

<span style="font-size: 90%;">Sorry, which issue are we going to fix? Theirs?</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:42 UTC</span>

<span style="font-size: 90%;">yes - or what else?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:54 UTC</span>

<span style="font-size: 90%;">Ours. The CRS project :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:07:16 UTC</span>

<span style="font-size: 90%;">It is about what we are doing to do :wink:</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:05 UTC</span>

<span style="font-size: 90%;">may be I misunderstand something, but the engine has a bug,what we can fix with a rule, where we detect the malicious payload - am I right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:08:35 UTC</span>

<span style="font-size: 90%;">yes.</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:53 UTC</span>

<span style="font-size: 90%;">so, in this context I mean we fix their bug :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:09:37 UTC</span>

<span style="font-size: 90%;">And if the engine fixes their own bug? What happens with our workaround?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:04 UTC</span>

<span style="font-size: 90%;">Do we create a new major release? Or this change will be there until v5 in X years?</span>

**airween** <span style="color: grey; font-size: 90%;">20:10:58 UTC</span>

<span style="font-size: 90%;">of course it depends on our workaround. If we can solve the issue with a rule that catches only the specified payload, then that rule can stay in the rule set.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:00 UTC</span>

<span style="font-size: 90%;">My personal opinion is that I would wait till the issues chat to see how this develops. If we find that the vendor thinks this is not a problem at all, then we do our workaround and we protect our users.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:11:14 UTC</span>

<span style="font-size: 90%;">Do we have pressure? Why can't we just wait and give them some time?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:12:26 UTC</span>

<span style="font-size: 90%;">The issue was first documented 2 years ago. There are likely exploits in the wild. As a good citizen we should fix as soon as possible.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">on the one hand this is true.

On the other hand, how many times do they need? :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:34 UTC</span>

<span style="font-size: 90%;">"If we find that the vendor thinks this is not a problem at all," ?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:15 UTC</span>

<span style="font-size: 90%;">Then let's decide when this happens...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:12:24 UTC</span>

<span style="font-size: 90%;">That's exactly the idea :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:26 UTC</span>

<span style="font-size: 90%;">The issue was first documented 2 years ago. There are likely exploits in the wild. As a good citizen we should fix as soon as possible.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:12:26 UTC</span>

<span style="font-size: 90%;">The issue was first documented 2 years ago. There are likely exploits in the wild. As a good citizen we should fix as soon as possible.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">on the one hand this is true.

On the other hand, how many times do they need? :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:12:33 UTC</span>

<span style="font-size: 90%;">just to clarify, this bug is public since 2 years. And the technique to exploit the bug is well known since 2005 :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">on the one hand this is true.

On the other hand, how many times do they need? :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:12:26 UTC</span>

<span style="font-size: 90%;">The issue was first documented 2 years ago. There are likely exploits in the wild. As a good citizen we should fix as soon as possible.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">on the one hand this is true.

On the other hand, how many times do they need? :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:50 UTC</span>

<span style="font-size: 90%;">How much time? Probably not much. But then I don't write that code, nor the tests associated with it ¯\\\_(ツ)\_/¯</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:14 UTC</span>

<span style="font-size: 90%;">So, to have an answer, being yes or nay, this week is enough I think.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:31 UTC</span>

<span style="font-size: 90%;">To fix it, probably a bit more.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:16:39 UTC</span>

<span style="font-size: 90%;">You mean fix the issue in the engine?

I'm not sure about that. I think it's easy.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:37 UTC</span>

<span style="font-size: 90%;">I guess one could also argue that, given that it's been an issue for so long, a couple more weeks don't really make a difference.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:15:20 UTC</span>

<span style="font-size: 90%;">next week "you know who" will ask us another week to review the issue</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:16:26 UTC</span>

<span style="font-size: 90%;">That's why we have until the issues chat.</span>

**airween** <span style="color: grey; font-size: 90%;">20:16:39 UTC</span>

<span style="font-size: 90%;">You mean fix the issue in the engine?

I'm not sure about that. I think it's easy.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:16:39 UTC</span>

<span style="font-size: 90%;">You mean fix the issue in the engine?

I'm not sure about that. I think it's easy.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:30 UTC</span>

<span style="font-size: 90%;">keep in mind, we're talking about 2 bugs, 1 critical and the other one is an unexpected behavior</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:17:39 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:44 UTC</span>

<span style="font-size: 90%;">and the vendor will fix just one of those 2</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:17:59 UTC</span>

<span style="font-size: 90%;">But we must give the vendor time to answer.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:18:25 UTC</span>

<span style="font-size: 90%;">Time to answer. Not to fix.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:18:26 UTC</span>

<span style="font-size: 90%;">Must is a strong word. It seems like a good idea, though.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:16 UTC</span>

<span style="font-size: 90%;">We still need a bit of time anyway to finish performance tests and prepare for CVE publication, so wouldn't that fit pretty nicely with waiting until the issue chat? They get 2 weeks to ponder, we get 2 weeks to finalise and can publish immediately at that time.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:44 UTC</span>

<span style="font-size: 90%;">So what happens if this bug can also be reproduced in a major Cloud service? Do we interact with them? We have sponsors also. Are we going to interact with them first?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:18 UTC</span>

<span style="font-size: 90%;">I think we need to have an internal disclosure with our sponsors first also.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:38 UTC</span>

<span style="font-size: 90%;">That's why we need an answer first</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:20:54 UTC</span>

<span style="font-size: 90%;">I’m personally in favour of giving some reasonable time, but I would not postpone decisions. I think we need a clear timeline of what we are going to do and when based on positive or negative answers from the vendor</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:21:05 UTC</span>

<span style="font-size: 90%;">do we need an internal disclosure to our sponsor?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:21:08 UTC</span>

<span style="font-size: 90%;">before fixing?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:13 UTC</span>

<span style="font-size: 90%;">We have done that in the past.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:20 UTC</span>

<span style="font-size: 90%;">Bug Bounty, remember?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:43 UTC</span>

<span style="font-size: 90%;">That's why they are smart being our sponsors. They learn about problems first :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:52 UTC</span>

<span style="font-size: 90%;">We contact them when something is happening that might involve third parties. The CRS project is way bigger than our reference use case, ModSecurity.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:49 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ _@dune73_ How much time do you think it would take to finalise preparations for the fix, i.e., finish performance tests, finalise PR, prepare CVE?</span>

**airween** <span style="color: grey; font-size: 90%;">20:25:41 UTC</span>

<span style="font-size: 90%;">okay, +1 for the disclosure to our sponsors (if we wait for responses for this question)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:09 UTC</span>

<span style="font-size: 90%;">I think there should be a discussion how we want to work around this. This will have a big impact on the amount of work we need to do.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:28 UTC</span>

<span style="font-size: 90%;">Let's call the PR we have the big workaround.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:53 UTC</span>

<span style="font-size: 90%;">_@airween_ suggested a much simpler variant above: a new detection rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:15 UTC</span>

<span style="font-size: 90%;">If people are willing to do the work to protect our users, then why prevent us from doing it?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:26 UTC</span>

<span style="font-size: 90%;">I think that would be relatively simple. The big workaround is hard to grasp. It has a lot of strings attached.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:53 UTC</span>

<span style="font-size: 90%;">If a new detection can do it, why not doing it?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:29:08 UTC</span>

<span style="font-size: 90%;">I guess based on the rule itself anyone can figure out what's the problem - then it's a public disclosure</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:28:07 UTC</span>

<span style="font-size: 90%;">because the payload is not something you would block</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:28:12 UTC</span>

<span style="font-size: 90%;">isn't malicious per se</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:28:18 UTC</span>

<span style="font-size: 90%;">as we don't block ' or ;</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:21 UTC</span>

<span style="font-size: 90%;">As explored during the afternoon in the dev chat, it might bring new FPs to ModSec3 users.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:52 UTC</span>

<span style="font-size: 90%;">ModSec2 and Coraza should be unaffected. You could say with a new detection rule, the problem stays where it's being created ...</span>

**airween** <span style="color: grey; font-size: 90%;">20:29:08 UTC</span>

<span style="font-size: 90%;">I guess based on the rule itself anyone can figure out what's the problem - then it's a public disclosure</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:29:08 UTC</span>

<span style="font-size: 90%;">I guess based on the rule itself anyone can figure out what's the problem - then it's a public disclosure</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:29:42 UTC</span>

<span style="font-size: 90%;">guys, it's already public... there's a public issue opened 2 years ago</span>

**airween** <span style="color: grey; font-size: 90%;">20:30:11 UTC</span>

<span style="font-size: 90%;">you are right - then we can construct a rule and add it to rule set</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:31:21 UTC</span>

<span style="font-size: 90%;">I think a rule that block a non-malicious payload is not something we should do</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:31:44 UTC</span>

<span style="font-size: 90%;">we would just create new FPs</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:58 UTC</span>

<span style="font-size: 90%;">definitely. But we can try to make a rule which has minimal (or zero) FP. I do not know yet how, but let's try :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:34:05 UTC</span>

<span style="font-size: 90%;">I feel like we're moving away from the main discussion</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:16 UTC</span>

<span style="font-size: 90%;">Yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:34:29 UTC</span>

<span style="font-size: 90%;">There's too much here. On what do we need to decide tonight?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:35:33 UTC</span>

<span style="font-size: 90%;">What we are doing, as a project</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:01 UTC</span>

<span style="font-size: 90%;">I think we should be ready to publish a workaround before Christmas. But we need not decide which one tonight. We can also explore that until the issue chat.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:09 UTC</span>

<span style="font-size: 90%;">The extra time will give us leverage to work on a better solution</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:32 UTC</span>

<span style="font-size: 90%;">So we work on a fix, a better one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:51 UTC</span>

<span style="font-size: 90%;">And we will publish in two weeks.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:05 UTC</span>

<span style="font-size: 90%;">Given the discussion above, we don't seem ready to publish. I vote for getting everything lined up until the issue chat, with the goal to be able to release the fix immediately after the issue chat.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:33 UTC</span>

<span style="font-size: 90%;">That is exactly what we should do</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:07 UTC</span>

<span style="font-size: 90%;">Good plan. Not sure we are ready until the issue chat, but it's good if we try.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:44 UTC</span>

<span style="font-size: 90%;">Anyone else?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:46 UTC</span>

<span style="font-size: 90%;">Related question: What do you want to do if unnamed vendor promises a fix in January?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:18 UTC</span>

<span style="font-size: 90%;">Decide tonight or at the issue chat?</span>

**airween** <span style="color: grey; font-size: 90%;">20:41:58 UTC</span>

<span style="font-size: 90%;">what will we communicate on next days?

(That's what we do :slightly_smiling_face:)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:42:22 UTC</span>

<span style="font-size: 90%;">We publish our fix</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:39 UTC</span>

<span style="font-size: 90%;">correct.</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:51 UTC</span>

<span style="font-size: 90%;">if we publish our fix, will we open a CVE?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:43:12 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:43:30 UTC</span>

<span style="font-size: 90%;">Yes</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:30 UTC</span>

<span style="font-size: 90%;">then the plan is done</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:12 UTC</span>

<span style="font-size: 90%;">So let's write the plan in the meeting summary decisions</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:31 UTC</span>

<span style="font-size: 90%;">vendor will know this information, so it's up to them what they want to do and when</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:56 UTC</span>

<span style="font-size: 90%;">For me this really depends on the size of the workaround.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:17 UTC</span>

<span style="font-size: 90%;">Let's move forward.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:24 UTC</span>

<span style="font-size: 90%;">OK.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:45:38 UTC</span>

<span style="font-size: 90%;">sorry but I didn't get what's the plan</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:45:46 UTC</span>

<span style="font-size: 90%;">waiting?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:50 UTC</span>

<span style="font-size: 90%;">No</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:45:57 UTC</span>

<span style="font-size: 90%;">Just read above</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:46:27 UTC</span>

<span style="font-size: 90%;">We come with a fix in two weeks</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:46:50 UTC</span>

<span style="font-size: 90%;">which fix? because we have talked about a "better fix"</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:47:03 UTC</span>

<span style="font-size: 90%;">That's what we take two weeks to discuss</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:47:06 UTC</span>

<span style="font-size: 90%;">who and how? have we got a plan for a better fix?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:47:14 UTC</span>

<span style="font-size: 90%;">Because it's not settled</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:48:10 UTC</span>

<span style="font-size: 90%;">There was the issue with performance and the idea to use a different workaround.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:48:46 UTC</span>

<span style="font-size: 90%;">And the CVE prep work (whatever is left to do there)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:09 UTC</span>

<span style="font-size: 90%;">If vendor has a timeline defined in two weeks then we can consider. If not, we just publish</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:49:30 UTC</span>

<span style="font-size: 90%;">Let's move on to the next topic</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">:man-shrugging: ok</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:30 UTC</span>

<span style="font-size: 90%;">Sure. Do we have additional questions?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:33 UTC</span>

<span style="font-size: 90%;">Please ask</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:44 UTC</span>

<span style="font-size: 90%;">I'm driving now, so expect delays</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:50:58 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:51:02 UTC</span>

<span style="font-size: 90%;">you... you're driving? :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:03 UTC</span>

<span style="font-size: 90%;">PL5</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:14 UTC</span>

<span style="font-size: 90%;">I'm stopping to text.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:52:14 UTC</span>

<span style="font-size: 90%;">I could NOT to imagine this, and I see you in the car you are moving 50 meters and stop for 30 secs, moving 80 meters and stop for 40 secs... :smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:52:32 UTC</span>

<span style="font-size: 90%;">Montevideo traffic</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:52:51 UTC</span>

<span style="font-size: 90%;">okay, makes sense :smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:53:43 UTC</span>

<span style="font-size: 90%;">Also, I'm driving kids that can type :smiley::stuck_out_tongue_winking_eye:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:54:00 UTC</span>

<span style="font-size: 90%;">So they read to me and then I tell them what to write</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:54:05 UTC</span>

<span style="font-size: 90%;">oh, such a smart solution! :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:51:17 UTC</span>

<span style="font-size: 90%;">WATCH OUT! A CLIFF!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:51:18 UTC</span>

<span style="font-size: 90%;">lol</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:51:31 UTC</span>

<span style="font-size: 90%;">no so please, next topic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:39 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:46 UTC</span>

<span style="font-size: 90%;">No, no worries, we can go back</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:51:53 UTC</span>

<span style="font-size: 90%;">If something is not clear</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:52:12 UTC</span>

<span style="font-size: 90%;">no no, no problem, fix in 2 weeks</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:14 UTC</span>

<span style="font-size: 90%;">I could NOT to imagine this, and I see you in the car you are moving 50 meters and stop for 30 secs, moving 80 meters and stop for 40 secs... :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:52:14 UTC</span>

<span style="font-size: 90%;">I could NOT to imagine this, and I see you in the car you are moving 50 meters and stop for 30 secs, moving 80 meters and stop for 40 secs... :smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:52:32 UTC</span>

<span style="font-size: 90%;">Montevideo traffic</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:52:51 UTC</span>

<span style="font-size: 90%;">okay, makes sense :smile:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:53:43 UTC</span>

<span style="font-size: 90%;">Also, I'm driving kids that can type :smiley::stuck_out_tongue_winking_eye:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:54:00 UTC</span>

<span style="font-size: 90%;">So they read to me and then I tell them what to write</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:54:05 UTC</span>

<span style="font-size: 90%;">oh, such a smart solution! :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:52:19 UTC</span>

<span style="font-size: 90%;">But this might be another name change discussion :sunglasses:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:52:44 UTC</span>

<span style="font-size: 90%;">Regula!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:52:57 UTC</span>

<span style="font-size: 90%;">laser!</span>

**airween** <span style="color: grey; font-size: 90%;">20:53:45 UTC</span>

<span style="font-size: 90%;">next topic please :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:11 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:33 UTC</span>

<span style="font-size: 90%;">So we need a process for this</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:54:36 UTC</span>

<span style="font-size: 90%;">now I can't stop thinking felipe that stop every 100 meters to text</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:03 UTC</span>

<span style="font-size: 90%;">Near miss</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:05 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:55:24 UTC</span>

<span style="font-size: 90%;">Package delivered, so now I'm parked</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:28 UTC</span>

<span style="font-size: 90%;">Let's see how we can handle these things in the future</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:57:07 UTC</span>

<span style="font-size: 90%;">We need to have a vulnerability disclosure process</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:57:56 UTC</span>

<span style="font-size: 90%;">TBH, it's too late for me to have this discussion. I propose that one or two people create a proposal and then we discuss that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:58:15 UTC</span>

<span style="font-size: 90%;">(too late because it's late at night)</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:11 UTC</span>

<span style="font-size: 90%;">For context: we have a security policy and a section detailing "Reporting a Vulnerability", so maybe that needs a new section "CRS Vuln. Disclosure" or something?
[https://github.com/coreruleset/coreruleset/security/policy](https://github.com/coreruleset/coreruleset/security/policy)</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:24 UTC</span>

<span style="font-size: 90%;">Policy is there, just needs a new paragraph or two.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:28 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:59:37 UTC</span>

<span style="font-size: 90%;">And the process?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:59:48 UTC</span>

<span style="font-size: 90%;">Goes in the new paragraph.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:59:59 UTC</span>

<span style="font-size: 90%;">It takes far more than a new paragraph I'm afraid.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:28 UTC</span>

<span style="font-size: 90%;">And it's two fold: For the case where we are the vendor - there we have a bit of something - and the case where we are the security reporter, thus the case discussed tonight.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:00:29 UTC</span>

<span style="font-size: 90%;">Can anyone link to such an example policy?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:00:38 UTC</span>

<span style="font-size: 90%;">E.g. a project that has a good one to follow?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:41 UTC</span>

<span style="font-size: 90%;">I can look up a few ones.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:00:54 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:59 UTC</span>

<span style="font-size: 90%;">I've consulted several organisations on this question.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:04 UTC</span>

<span style="font-size: 90%;">We can follow this offline</span>

**dune73** <span style="color: grey; font-size: 90%;">21:01:30 UTC</span>

<span style="font-size: 90%;">Agreed. But maybe you want to decide who comes up with a proposal. Maybe a small team of 1-2-3 people.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:46 UTC</span>

<span style="font-size: 90%;">I can be part of that team</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">21:06:03 UTC</span>

<span style="font-size: 90%;">If possible, I would be happy to take part of the reasoning</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:01:51 UTC</span>

<span style="font-size: 90%;">Who else?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:05 UTC</span>

<span style="font-size: 90%;">I'd rather not be part of it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:02:18 UTC</span>

<span style="font-size: 90%;">I'll help</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:02:40 UTC</span>

<span style="font-size: 90%;">I think chatgpt want to help too</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:02:44 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:02:56 UTC</span>

<span style="font-size: 90%;">fot such thing it's really useful</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:03:00 UTC</span>

<span style="font-size: 90%;">Is that your alt handle _@theMiddle_? :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:06 UTC</span>

<span style="font-size: 90%;">But this more about deciding in our case</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:03:06 UTC</span>

<span style="font-size: 90%;">yes!!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:36 UTC</span>

<span style="font-size: 90%;">But I agree the wording can be better with help</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:37 UTC</span>

<span style="font-size: 90%;">If you guys and AI come up with a proposal, I'll be happy to review.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:41 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:49 UTC</span>

<span style="font-size: 90%;">Sounds good then</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:59 UTC</span>

<span style="font-size: 90%;">So...next topic?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:09 UTC</span>

<span style="font-size: 90%;">Absolutely!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:05:36 UTC</span>

<span style="font-size: 90%;">Define the threshold for fps</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:06:08 UTC</span>

<span style="font-size: 90%;">We now have a new way for testing FPs in text</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:07:09 UTC</span>

<span style="font-size: 90%;">So the quantitative testing is here to stay</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:07:42 UTC</span>

<span style="font-size: 90%;">I absolutely love what _@xanadu_ has done! However, I'm a bit concerned that the corpus doesn't accurately represent real world traffic. If we define thresholds from such a corpus they might become meaningless.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:59 UTC</span>

<span style="font-size: 90%;">Good thinking.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:08:20 UTC</span>

<span style="font-size: 90%;">I agree that, to some extent, we need to have more corpus probably.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:25 UTC</span>

<span style="font-size: 90%;">It also covers only ARGS so far. From what he hear, biggest number of FPs with v4-RC2 are in ARGS, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:02 UTC</span>

<span style="font-size: 90%;">Maybe we use what we have as a MVP for 4.0 (so it's being delayed too much) and expand afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:35 UTC</span>

<span style="font-size: 90%;">It's true that we decided to use quantiative testing after v4 is out, but we get so few FPs reports / issues when we know there must be more, it would be foolish somehow to ignore _@xanadu_'s work now that we have it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:10:10 UTC</span>

<span style="font-size: 90%;">Sounds reasonable. I just wouldn't publish the thresholds explicitly until we have a solid basis.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:10:11 UTC</span>

<span style="font-size: 90%;">The current/preliminary results can be used to squash FPs right now on a best efforts basis.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">21:10:37 UTC</span>

<span style="font-size: 90%;">Absolutely. I'm only thinking about the thresholds.</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:10:30 UTC</span>

<span style="font-size: 90%;">Policies on "PL 1 means X FPs per 10,000 requests" can be a future goal</span>

**dune73** <span style="color: grey; font-size: 90%;">21:10:45 UTC</span>

<span style="font-size: 90%;">OK. So we do not really decide on thresholds, but see what we can do and until we think it's OK to release now?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:11:49 UTC</span>

<span style="font-size: 90%;">I guess it's fine that way</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:01 UTC</span>

<span style="font-size: 90%;">Yes, I think that makes sense.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:12:21 UTC</span>

<span style="font-size: 90%;">Last topic then?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:30 UTC</span>

<span style="font-size: 90%;">If you look at [https://github.com/coreruleset/coreruleset/issues/3392#issuecomment-1832796222](https://github.com/coreruleset/coreruleset/issues/3392#issuecomment-1832796222), then it's fairly obvious what has to be done.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:36 UTC</span>

<span style="font-size: 90%;">_@xanadu_ can you share your script?</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:13:11 UTC</span>

<span style="font-size: 90%;">It's not quite in a reasonable/sensible state to share, but it will be soon. So, yes, very soon I can share it :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:13:21 UTC</span>

<span style="font-size: 90%;">Too much hard coded stuff atm.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:39 UTC</span>

<span style="font-size: 90%;">Please do. It would be much easier to improve the regexes for FP with the script in hand.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:13:53 UTC</span>

<span style="font-size: 90%;">Also happy to help improving the script.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:14:58 UTC</span>

<span style="font-size: 90%;">We can talk about back porting then</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:15:12 UTC</span>

<span style="font-size: 90%;">3.3.5 to 3.2.4</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:16:07 UTC</span>

<span style="font-size: 90%;">I have currently no news 
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:32 UTC</span>

<span style="font-size: 90%;">then ... That's our chat?</span>

**airween** <span style="color: grey; font-size: 90%;">21:20:00 UTC</span>

<span style="font-size: 90%;">it seems like yes...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:20:18 UTC</span>

<span style="font-size: 90%;">Good night everyone!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:20:27 UTC</span>

<span style="font-size: 90%;">Good night</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:27 UTC</span>

<span style="font-size: 90%;">Thank you for running this _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">21:20:30 UTC</span>

<span style="font-size: 90%;">Good night</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:20:31 UTC</span>

<span style="font-size: 90%;">Good night</span>

**airween** <span style="color: grey; font-size: 90%;">21:20:34 UTC</span>

<span style="font-size: 90%;">good night guys!</span>

**jit** <span style="color: grey; font-size: 90%;">21:20:37 UTC</span>

<span style="font-size: 90%;">Goodnight everyone</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">21:20:45 UTC</span>

<span style="font-size: 90%;">Night night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">21:21:01 UTC</span>

<span style="font-size: 90%;">Night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:21:11 UTC</span>

<span style="font-size: 90%;">Good night everyone!
Please review the meeting minutes if I understood everything right. Please correct it directly in the issue if not.
Thanks Felipe for running the meeting</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:21:20 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/3398#issuecomment-1839362211](https://github.com/coreruleset/coreruleset/issues/3398#issuecomment-1839362211)</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:22:44 UTC</span>

<span style="font-size: 90%;">Looks good, thanks</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:22:46 UTC</span>

<span style="font-size: 90%;">bb</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:22:57 UTC</span>

<span style="font-size: 90%;">bye bye</span>

