### Mon, May 15th, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:32:25 UTC</span>

<span style="font-size: 90%;">Hi there, time for the CRS chat. We have a few casulaties who can't make it due to sickness and the like. Let's see who's around?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:32:49 UTC</span>

<span style="font-size: 90%;">Hello</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:32:53 UTC</span>

<span style="font-size: 90%;">Hi</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:56 UTC</span>

<span style="font-size: 90%;">hi</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:33:07 UTC</span>

<span style="font-size: 90%;">hiii</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:33:34 UTC</span>

<span style="font-size: 90%;">ciao!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:24 UTC</span>

<span style="font-size: 90%;">Hey, hey, good to see you all.</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:47 UTC</span>

<span style="font-size: 90%;">hi guys</span>

**airween** <span style="color: grey; font-size: 90%;">18:35:18 UTC</span>

<span style="font-size: 90%;">sorry, I have to go soon for 15 mins away</span>

**airween** <span style="color: grey; font-size: 90%;">18:35:29 UTC</span>

<span style="font-size: 90%;">but later I will be here</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:57 UTC</span>

<span style="font-size: 90%;">Maybe we want to start with the secparsing agenda item then, before you have to leave.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:27 UTC</span>

<span style="font-size: 90%;">If I got this right, _@jit_ wants to extend it to startup time rule exclusion directives. Do I get this right?</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:36:36 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:36:47 UTC</span>

<span style="font-size: 90%;">I was having problem with that, too.</span>

**jit** <span style="color: grey; font-size: 90%;">18:36:48 UTC</span>

<span style="font-size: 90%;">Hi guys.</span>

**jit** <span style="color: grey; font-size: 90%;">18:36:52 UTC</span>

<span style="font-size: 90%;">I again missed the 1st meeting of the month.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:58 UTC</span>

<span style="font-size: 90%;">Or was it you _@azurIt_? (sorry if yes)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:12 UTC</span>

<span style="font-size: 90%;">No worries, _@jit_. Very nice to see you around!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:37:13 UTC</span>

<span style="font-size: 90%;">It was me, first, then Jit and he also created a PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:21 UTC</span>

<span style="font-size: 90%;">Ah, got you, thanks.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:37:29 UTC</span>

<span style="font-size: 90%;">is threre a issue nr?</span>

**airween** <span style="color: grey; font-size: 90%;">18:37:32 UTC</span>

<span style="font-size: 90%;">sorry, what are the time rule exclusions?</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:37:37 UTC</span>

<span style="font-size: 90%;">In the agenda.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:37:56 UTC</span>

<span style="font-size: 90%;">Haha, it's too simple :slightly_smiling_face:</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">18:39:42 UTC</span>

<span style="font-size: 90%;">Sorry, it was supposed to be an aswear for _@theMiddle_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">PR [https://github.com/coreruleset/secrules_parsing/issues/43](https://github.com/coreruleset/secrules_parsing/issues/43)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:35 UTC</span>

<span style="font-size: 90%;">Startup time rule exclusions start the moment you read the config. That's the SecRuleRemoveById and friends. The runtime one work via ctl: action.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:50 UTC</span>

<span style="font-size: 90%;">See cheatsheet at [netnea.com](http://netnea.com) just in case.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:49 UTC</span>

<span style="font-size: 90%;">What are we supposed to discuss with this agenda item? If secrules parsing needs this, or the quality of the PR?</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:40:09 UTC</span>

<span style="font-size: 90%;">I think only the quality of the PR.</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:24 UTC</span>

<span style="font-size: 90%;">oh, sorry - I meant those are like special some timing rules :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:37 UTC</span>

<span style="font-size: 90%;">Cool. So what do you think _@airween_?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:40:41 UTC</span>

<span style="font-size: 90%;">isn't there some review to solve in that PR?</span>

**jit** <span style="color: grey; font-size: 90%;">18:41:27 UTC</span>

<span style="font-size: 90%;">I've added a new commit with changes. If anybody can verify whether what I did is right, it'd be great.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:41:29 UTC</span>

<span style="font-size: 90%;">So, can anyone do a review?</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:37 UTC</span>

<span style="font-size: 90%;">sure, I can take it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:40 UTC</span>

<span style="font-size: 90%;">So we're basically in favor, we have a PR and _@airween_ will check it out and work with _@jit_ to get it merged?</span>

**airween** <span style="color: grey; font-size: 90%;">18:42:41 UTC</span>

<span style="font-size: 90%;">so we are talking about this, right?
[https://github.com/coreruleset/secrules_parsing/pull/46](https://github.com/coreruleset/secrules_parsing/pull/46)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:53 UTC</span>

<span style="font-size: 90%;">43 or 46?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:01 UTC</span>

<span style="font-size: 90%;">_@jit_? _@azurIt_?</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:03 UTC</span>

<span style="font-size: 90%;">46 is the PR</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:43:06 UTC</span>

<span style="font-size: 90%;">43 is issue and 46 is PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:17 UTC</span>

<span style="font-size: 90%;">Ah, thanks. Sorry, I overlooked this.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:51 UTC</span>

<span style="font-size: 90%;">So we're done here?</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:43:58 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:13 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:24 UTC</span>

<span style="font-size: 90%;">Then let's turn to the Scanner / UA agent overhaul.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:33 UTC</span>

<span style="font-size: 90%;">The PR has been around for a few weeks now and the experience is that the PL2 rule triggers a ton of FPs. This is not entirely surprising, since it's based on a huge list of know automatic user agents with some known more or less benign UAs excluded.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:27 UTC</span>

<span style="font-size: 90%;">What we're currently doing is removing all those UAs that hit our servers (thanks _@theMiddle_ / _@azurIt_) with non-malicious intent. And the trajectory is all the rest will alert at PL2.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:51 UTC</span>

<span style="font-size: 90%;">We can continue with this game for a long time, since we still have like 1.8K UAs on this PL2 deny-list.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:03 UTC</span>

<span style="font-size: 90%;">The question is, is this the right strategy.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:30 UTC</span>

<span style="font-size: 90%;">I think it's minimally better than what we have now (an outdated small list we're maintaining poorly).</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:48:46 UTC</span>

<span style="font-size: 90%;">BTW, is this really what Cloudflare is blocking?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">I can not see who we can substantially improve it. An alternative would be to drop every check beyond the new PL1 rule that has the truely evil security scanners. All the rest would then be dropped until somebody recreates something similar as a plugin. For me, this would be viable, since it's really, really hard to draw a line between benign and malicious, namely based on only the UA.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:22 UTC</span>

<span style="font-size: 90%;">No, short answer: Nothing to do with Cloudflare.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:57 UTC</span>

<span style="font-size: 90%;">I'm for blocking only known bad actors.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:49:58 UTC</span>

<span style="font-size: 90%;">For me, it looks like something like 'block everything except major browsers'.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:18 UTC</span>

<span style="font-size: 90%;">agree with _@maxleske_</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:22 UTC</span>

<span style="font-size: 90%;">And maybe that as PL3/4?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:42 UTC</span>

<span style="font-size: 90%;">also, it scares me a lot all lists made by "single word"</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:58 UTC</span>

<span style="font-size: 90%;">it's really hard to identify all possible FPs</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:45 UTC</span>

<span style="font-size: 90%;">_@maxleske_ You opt to move the current PL1 rule that prevents sqlmap to PL3/4?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:07 UTC</span>

<span style="font-size: 90%;">_@azurIt_ Your impression is very close to reality, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:46 UTC</span>

<span style="font-size: 90%;">That rule also carries nmap, nuclei, fuzz faster, zgrab, nessus, massan ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:06 UTC</span>

<span style="font-size: 90%;">No, sorry. I was referring to _@azurIt_'s comment: "block everything except major browsers". That might be something for PL3/4, but it probably depends a lot on the use case. So maybe it's too restrictive</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:35 UTC</span>

<span style="font-size: 90%;">Got you. Thanks.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:54:27 UTC</span>

<span style="font-size: 90%;">Why semrush and ahrefs were removed from the PL2 list?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:54:40 UTC</span>

<span style="font-size: 90%;">they're not bad actor</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:54:53 UTC</span>

<span style="font-size: 90%;">But both of them are soooooooooooooooooooooooo agressive.</span>

**jit** <span style="color: grey; font-size: 90%;">18:55:04 UTC</span>

<span style="font-size: 90%;">_@azurIt_ suggestion is apt, but I think we need to take into consideration some crawler bots that index sites for search engines</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:55:17 UTC</span>

<span style="font-size: 90%;">They were taking down my servers, i'm blocking them for years.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:55:21 UTC</span>

<span style="font-size: 90%;">that doesn't means a security problem</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:55:28 UTC</span>

<span style="font-size: 90%;">even google bot can be aggressive</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:48 UTC</span>

<span style="font-size: 90%;">Which might be good fro a plugin...</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:56:01 UTC</span>

<span style="font-size: 90%;">Yes it means, they are literally doing DDoS attacks.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">I'd rather not want to talk about individual decisions here. More the general strategy.</span>

**jit** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">Exactly blocking good crawler bots is not okay</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">if a crawler takes down your server it's not a DoS :slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:56:34 UTC</span>

<span style="font-size: 90%;">If it is doing 1000 requests per second from 100 IPs, it is.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:36 UTC</span>

<span style="font-size: 90%;">And I get the feeling we agree on the really, really bad stuff, but afterwards it's difficult.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:57:12 UTC</span>

<span style="font-size: 90%;">I receive a lot of crawl from semrush but never see 1000 RPS from 100 IPs</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:27 UTC</span>

<span style="font-size: 90%;">The PR has 3 rules now: PL1: superagressive stuff, PL2: 1.9K list minus more or less benign automatic agents, PL4: every automatic agent.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:57:29 UTC</span>

<span style="font-size: 90%;">it's a SEO tool guys, it's not a security scanner</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:58:10 UTC</span>

<span style="font-size: 90%;">Both of them were DDoSing my servers, they are not good bots.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:21 UTC</span>

<span style="font-size: 90%;">If we agree on the PL1 rule, do we really drop the PL2 rule and what about the PL4 rule that stretches to googlebot too. Keep that or remove it?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:59:05 UTC</span>

<span style="font-size: 90%;">we can't block a service because we have problem with our servers. We should always think about CRS use cases</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:59:20 UTC</span>

<span style="font-size: 90%;">That's not true _@theMiddle_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:26 UTC</span>

<span style="font-size: 90%;">For _@azurIt_ it's a use case :slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:59:39 UTC</span>

<span style="font-size: 90%;">Even bots of services must behave correctly.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:41 UTC</span>

<span style="font-size: 90%;">But again, I think that kind of thing could live in a plugin instead</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:00:06 UTC</span>

<span style="font-size: 90%;">Maybe you are not hosting 1000s of domains on one server (with is a common case for webhostings).</span>

**airween** <span style="color: grey; font-size: 90%;">19:00:14 UTC</span>

<span style="font-size: 90%;">(I'm back)</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:00:19 UTC</span>

<span style="font-size: 90%;">So you can't see what they are doing.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:01:04 UTC</span>

<span style="font-size: 90%;">For example, Googlebot is not behaving like this, it has limits for requests per target IP.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:02:35 UTC</span>

<span style="font-size: 90%;">Yes. But it'll crawl for different domains separately. Which is why you're getting thousand RPS on one server.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:03:53 UTC</span>

<span style="font-size: 90%;">Yes but it can be done correctly. You cannot do hundreds of requests per second only because you want to crawl 1000 domains which hosts on the same server.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:05:26 UTC</span>

<span style="font-size: 90%;">That's fair. Maybe you're right but for a normal company that'd not be the case.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:38 UTC</span>

<span style="font-size: 90%;">It's clear that we address different use cases. The question is do we any good with this PL2 rule or will people have to disable it immediately bc of that one agent they want to allow (it's a \@pmFromFile rule).</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:03:24 UTC</span>

<span style="font-size: 90%;">ok, but semrush it's a service, have you used it? It doesn't send 1000RPS for a single usage. Maybe you have a specific setup that doesn't fit well with the semrush crawler. But we can't block it for all the world on all integrators just because we have problems on our servers. I mean, if I login to my semrush and query my website I'm expecting to not being blocked by the WAF</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:22 UTC</span>

<span style="font-size: 90%;">Guys, this discussion is not getting us anywhere. We need to discuss the rule architecture not if semrush is a bad bully.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:56 UTC</span>

<span style="font-size: 90%;">Do we want to block most of the automatic UAs or do we drop that attempt completely from the rule set.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:12 UTC</span>

<span style="font-size: 90%;">If we keep it, then you guys can sort it out if you want semrush in said rule or not.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:48 UTC</span>

<span style="font-size: 90%;">yes but understand what is evil or not should be important before blocking a list of crawler</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:06:17 UTC</span>

<span style="font-size: 90%;">We are talking about PL2, so it can do some FPs.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:07:01 UTC</span>

<span style="font-size: 90%;">Generally, i like the new lists and rules, we only need to tune it more.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:07:06 UTC</span>

<span style="font-size: 90%;">yes but I can accept some FPs at PL2 because we blocked some real browser instead of a bad bot. But it's a problem if we block a tool that is not malicious per se</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:07 UTC</span>

<span style="font-size: 90%;">_@maxleske_, _@franbuehler_,@themi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:48 UTC</span>

<span style="font-size: 90%;">_@maxleske_, _@franbuehler_, _@theMiddle_ you all opted to drop the PL2 rule above. Still agree on that? I'm torn and it seems _@azurIt_ would rather keep and tune.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:09:26 UTC</span>

<span style="font-size: 90%;">What about to keep blocking only really evil things (scanners and so) in CRS and create a plugin from other data?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:30 UTC</span>

<span style="font-size: 90%;">I think it's worth considering dropping the rule from core CRS. I do believe that _@azurIt_ is right, we need the rule in some form to satisfy hosters (I used to work for one).</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:09:50 UTC</span>

<span style="font-size: 90%;">Ahhh, so difficult. I don't have strong feelings anymore!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:05 UTC</span>

<span style="font-size: 90%;">Is confusion a feeling? :wink:</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">19:12:06 UTC</span>

<span style="font-size: 90%;">It is a state of mind</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:29 UTC</span>

<span style="font-size: 90%;">I worked 40-60 hours on this PR and the more distance I get the worse I feel about it. If we remove all the stuff that actually appears in the log, then we end up blocking the stuff that is no longer existing in the wild and the list is only there for historical reasons.
We could totally make it a plugin, though. If that would help / satisfy hosters, though.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:14:49 UTC</span>

<span style="font-size: 90%;">I'm totally for keeping the data at least in some form and i didn't mean i'm against integration also in the core CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:57 UTC</span>

<span style="font-size: 90%;">What do you think about keeping the question open until the next meeting and then take the decision? Maybe somebody has a better idea by then.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:16:22 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:17:08 UTC</span>

<span style="font-size: 90%;">But if i understand the conversation correctly, i'm not the one who needs to be convienced. :)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:50 UTC</span>

<span style="font-size: 90%;">I just to make sure we're all on the same page here and I am really not sure and so are several others in the chat.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:19:25 UTC</span>

<span style="font-size: 90%;">BTW, _@theMiddle_ said somewhere in the PR that we should unblock all google bots - first i think that, too, but while i was searching for FPs i found few google UAs which we should block.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:20:43 UTC</span>

<span style="font-size: 90%;">Unfortunately i can't remember which it was but it belong to something like a google web creation platform which runs on google servers and use it's IPs and it was possible to code it to crawl webs.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:06 UTC</span>

<span style="font-size: 90%;">google sheets</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:18 UTC</span>

<span style="font-size: 90%;">LOADFROMXML / LOADFROMHTML ro something like that</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">are used to crawl websites</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:21:31 UTC</span>

<span style="font-size: 90%;">Maybe. Fortunately, Google was not allowing to change the UA identification.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:21:40 UTC</span>

<span style="font-size: 90%;">I saw it was really used for bots.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:41 UTC</span>

<span style="font-size: 90%;">yes but it's a google sheet feature</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:49 UTC</span>

<span style="font-size: 90%;">yes it is</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:22:02 UTC</span>

<span style="font-size: 90%;">really used for crawler and scrapers</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:20 UTC</span>

<span style="font-size: 90%;">An additional problem with the UA lists is that whatever we do, the bad actors will simply change the UA. So it's a very limited use case anyways and it's not aiming for the dangerous stuff. More the annoying stuff.</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:23:56 UTC</span>

<span style="font-size: 90%;">yes! that's why we just need to focus on security tool or bad actor for UA list</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:22:53 UTC</span>

<span style="font-size: 90%;">but my question is: are we really want to block a google feature because it could be used for crawl websites?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:47 UTC</span>

<span style="font-size: 90%;">Let's look at this outside the meeting, please.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:23:53 UTC</span>

<span style="font-size: 90%;">_@dune73_ But it's not always the case. For example, we can effectively block [shodan.io](http://shodan.io) and also other tools. Also, we will drop scriptkiddies.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:23:56 UTC</span>

<span style="font-size: 90%;">yes! that's why we just need to focus on security tool or bad actor for UA list</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:23:56 UTC</span>

<span style="font-size: 90%;">yes! that's why we just need to focus on security tool or bad actor for UA list</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:04 UTC</span>

<span style="font-size: 90%;">If we postpone the UA topic, there is nothing else on the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:16 UTC</span>

<span style="font-size: 90%;">Is there anything else we should talk about?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:09 UTC</span>

<span style="font-size: 90%;">This is one of the last open areas for CRS4. I hope we can create a clear roadmap for the release at the next meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:38 UTC</span>

<span style="font-size: 90%;">Looks like we're making it under 1 hour. Thank you for your participation.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:12 UTC</span>

<span style="font-size: 90%;">Thank you and good night to everyone.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:29:20 UTC</span>

<span style="font-size: 90%;">thanks, bye</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:29:21 UTC</span>

<span style="font-size: 90%;">wow, that was quick today</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:29:27 UTC</span>

<span style="font-size: 90%;">bye bye</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:38 UTC</span>

<span style="font-size: 90%;">Good bye everyone.</span>

**jit** <span style="color: grey; font-size: 90%;">19:29:46 UTC</span>

<span style="font-size: 90%;">Good night, everyone.</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:09 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:30:10 UTC</span>

<span style="font-size: 90%;">yeah, but it's not over for me :smile: have to do some maintenance of few servers now. Bye!</span>

