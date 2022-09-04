### Mon, Aug 1st, 2022

**dune73** <span style="color: grey; font-size: 90%;">18:30:25 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's time for the CRS chat.</span>

**walter** <span style="color: grey; font-size: 90%;">18:30:32 UTC</span>

<span style="font-size: 90%;">hi!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:30:36 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:30:48 UTC</span>

<span style="font-size: 90%;">Hey _@walter_ and _@xanadu_ how is that hackathon coming along?</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:53 UTC</span>

<span style="font-size: 90%;">Hello _@airween_. Back from Italy?</span>

**airween** <span style="color: grey; font-size: 90%;">18:32:12 UTC</span>

<span style="font-size: 90%;">yes, we are at home again (unfortunately...)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:32:19 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:27 UTC</span>

<span style="font-size: 90%;">Hello _@franbuehler_</span>

**Karel** <span style="color: grey; font-size: 90%;">18:32:30 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:48 UTC</span>

<span style="font-size: 90%;">Wonder wether _@theMiddle_ got home from Bretagne too - or he melted on the cliffs at 45°C or so?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:02 UTC</span>

<span style="font-size: 90%;">Welcome to our Slack _@Karel_ - so nice to have you with us.</span>

**Karel** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;">Happy to be here! :slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:33:18 UTC</span>

<span style="font-size: 90%;">Hi.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:33 UTC</span>

<span style="font-size: 90%;">Hello _@azurIt_! Good to have our hero here with us.</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:41 UTC</span>

<span style="font-size: 90%;">Well, the first day for me was getting back into the routine… I didn’t feel great in the morning but I handled 3 findings, one PR is ready for merge after review, other one is merged. Now I’m working on upstreaming some new XenForo rules to the plugin.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:56 UTC</span>

<span style="font-size: 90%;">_@Karel_: Azurit used July to create curl-calls for every bug bounty submission, including the duplicates.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:37 UTC</span>

<span style="font-size: 90%;">We will use those to serve as test during the development for the remaining fixes.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:36:00 UTC</span>

<span style="font-size: 90%;">More than 500 curl 'scripts' for 177 submissions were created!</span>

**Karel** <span style="color: grey; font-size: 90%;">18:36:08 UTC</span>

<span style="font-size: 90%;">I see, why not the usual YAML tests? Or do these curl calls still need to be converted into YAML tests?</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:35 UTC</span>

<span style="font-size: 90%;">yes there are also YAML tests! airween made a tool to convert them</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:39 UTC</span>

<span style="font-size: 90%;">They can be converted via a new script by _@airween_.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:49 UTC</span>

<span style="font-size: 90%;">Soon in both directions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:57 UTC</span>

<span style="font-size: 90%;">ftw-yaml <-> curl</span>

**airween** <span style="color: grey; font-size: 90%;">18:37:18 UTC</span>

<span style="font-size: 90%;">but it's important: YAML tests does not have correct log_contains field value, so we can't use them actually</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:51 UTC</span>

<span style="font-size: 90%;">Apparently it takes some thinking which rule is supposed to detect an attack, yes.</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:53 UTC</span>

<span style="font-size: 90%;">yes but that’s a matter of filling in the correct ruleId right?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:01 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:03 UTC</span>

<span style="font-size: 90%;">yes</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:38:14 UTC</span>

<span style="font-size: 90%;">Yes, it's do-able i think.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:26 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Karel** <span style="color: grey; font-size: 90%;">18:38:30 UTC</span>

<span style="font-size: 90%;">Tests are still super hard to get right. Dealing with them so far hasn't been a walk in the park. Go-ftw tends to break a lot, so I often rely on the GitHub action</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:39:14 UTC</span>

<span style="font-size: 90%;">Let’s team on that.</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">18:39:45 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:50 UTC</span>

<span style="font-size: 90%;">_@airween_: It would be nice if the curl->yaml conversion would take an optional parameter to assign the rule id for log_contains.</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:07 UTC</span>

<span style="font-size: 90%;">right, that's easy to add</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:48 UTC</span>

<span style="font-size: 90%;">OK, if we get started for real?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:02 UTC</span>

<span style="font-size: 90%;">The agenda is at [https://github.com/coreruleset/coreruleset/issues/2690](https://github.com/coreruleset/coreruleset/issues/2690)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:12 UTC</span>

<span style="font-size: 90%;">I've added a few news items, most of you are aware of.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:16 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:33 UTC</span>

<span style="font-size: 90%;">Important: CRS developer retreat: Saturday Oct 30 to Saturday November 6, 2022. We'll stay in the Villa Cagnola near Varese, Italy. That's 20-30 min from Milano airport.</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:02 UTC</span>

<span style="font-size: 90%;">Oct 30 is a Sunday</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:18 UTC</span>

<span style="font-size: 90%;">We got a very good price as it's outside holiday season. It's easy to reach from Switzerland (where several developers live) and from Milano airport.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:34 UTC</span>

<span style="font-size: 90%;">Oops. I messed that up.</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:47 UTC</span>

<span style="font-size: 90%;">No problem, but do we arrive at saturday or sun?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:55 UTC</span>

<span style="font-size: 90%;">Saturday Oct 29 to Saturday November 5, 2022</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:28 UTC</span>

<span style="font-size: 90%;">There is the idea for some to stay until Sunday November 6, but people will have to pay that final night themselves. CRS pays the hotel until Saturday.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:17 UTC</span>

<span style="font-size: 90%;">Please take notice of the date and hopefully we will get the complete project together - or almost.</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:31 UTC</span>

<span style="font-size: 90%;">Hope so! :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:12 UTC</span>

<span style="font-size: 90%;">So _@walter_ is hosting a bug bounty findings hackathon this week. We have several developers taking part and hope to close as many of the open reports as possible. Priority is on the easy ones, if I am not mistaken.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:28 UTC</span>

<span style="font-size: 90%;">@Walter would you mind giving us plan briefly?</span>

**airween** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">I would take the family for a quick weekend trip to Milano from Friday to Sunday, so I planned I'll arrive on Sunday</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:02 UTC</span>

<span style="font-size: 90%;">I don’t have a set plan, I think it’s important to just get those open issues down. That’s why I recommended to start with easy ones. As we get more confidence, I hope we can tackle the more complex ones. Today, Franziska and I created some PRs, which is nice for a start. I think our velocity will go up over the week.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:43 UTC</span>

<span style="font-size: 90%;">Thank you,.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:05 UTC</span>

<span style="font-size: 90%;">Yes, I hope so too! My start was a bit slow, I had to fix ftw again. But I hope to work faster tomorrow!</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:35 UTC</span>

<span style="font-size: 90%;">Yeah, I had some trouble with python, but finally got my feet wet with the new regexp-assemble tool :ok_hand:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:45 UTC</span>

<span style="font-size: 90%;">Looking fwd to see all these PRs. I'm sorry I can not really join for more than here and there ...</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:10 UTC</span>

<span style="font-size: 90%;">The documentation on regexp-assemble was excellent by the way.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:16 UTC</span>

<span style="font-size: 90%;">Coordination is via the devs channel so far is not it. But it could be here too, could not it?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:32 UTC</span>

<span style="font-size: 90%;">Nice to hear about the documentation. I got the same impression.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:44 UTC</span>

<span style="font-size: 90%;">Yes, I would say it’s best to keep in touch a lot over the dev channel, ask for reviews, etc.</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:17 UTC</span>

<span style="font-size: 90%;">Maybe it’s nice to add a column to the sheet with “Date fixed” so we have some numbers. KPIs!!!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:23 UTC</span>

<span style="font-size: 90%;">Given the reports are not public, I see the point in talking in a closed channel about them.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:36 UTC</span>

<span style="font-size: 90%;">Having a date to the fix would be interesting.</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:23 UTC</span>

<span style="font-size: 90%;">But we already have 70 merged ones with no dates, sooooo… well, at least we could start now.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:37 UTC</span>

<span style="font-size: 90%;">If we look at the performance for July, we have 10 PRs merged which is relatively low compared to Winter and Spring. THis is a season problem, but also an effect of our dev pipeline being clogged with bug bounty findings.</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:40 UTC</span>

<span style="font-size: 90%;">Anyway, don’t bother. Let’s continue the meet.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:20 UTC</span>

<span style="font-size: 90%;">I'm confident with the curl calls ready and the Hackathon, we'll get over this hill and will leave this experience in a better shape.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:47 UTC</span>

<span style="font-size: 90%;">I think the same.</span>

**Karel** <span style="color: grey; font-size: 90%;">18:53:43 UTC</span>

<span style="font-size: 90%;">By the way, I haven't heard anything regarding [#2581](https://github.com/coreruleset/coreruleset/issues/#2581) yet, why is that? As far as I can tell, it should be ready to get merged</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:55 UTC</span>

<span style="font-size: 90%;">There are a few burning open questions, some with regards to PR. I think we should sort these out before we turn to the PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:23 UTC</span>

<span style="font-size: 90%;">2581 is on the agenda for tonight. We'll merge during the meeting if it's ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:57 UTC</span>

<span style="font-size: 90%;">So if you do not mind let's talk about the sandbox.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:22 UTC</span>

<span style="font-size: 90%;">There is a new header you can use to tell the sandbox to return a 403 if the anomaly scores meets the threshold.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:41 UTC</span>

<span style="font-size: 90%;">This is useful for certain use cases, namely newbies checking out CRS.</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:15 UTC</span>

<span style="font-size: 90%;">Yes, or people using tooling</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:19 UTC</span>

<span style="font-size: 90%;">In other use cases you do not want that, you want the 200 and the dump of the rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:37 UTC</span>

<span style="font-size: 90%;">Now the open question is, do we want to make this the default behaviour?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:53 UTC</span>

<span style="font-size: 90%;">That would mean you need to issue a http header if you want to be sure you get a 200.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:09 UTC</span>

<span style="font-size: 90%;">Would our 403 responses contain the full rules dump like the 200?</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:13 UTC</span>

<span style="font-size: 90%;">In my opinion it makes sense to make 403 the default behavior. We will still send the response output, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:41 UTC</span>

<span style="font-size: 90%;">That's the case from the back of my head. _@fzipitria_ please confirm.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:27 UTC</span>

<span style="font-size: 90%;">We're taling about [https://github.com/coreruleset/crs-sandbox/issues/28](https://github.com/coreruleset/crs-sandbox/issues/28)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:06 UTC</span>

<span style="font-size: 90%;">But I can't seem to find the discussion about the use cases where this question was dealt with too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:24 UTC</span>

<span style="font-size: 90%;">Either way, the rules have to be listed in the response, that's obvious.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:55 UTC</span>

<span style="font-size: 90%;">curl -v -H 'x-crs-mode: blocking' -H 'x-crs-paranoia-level: 4' -H 'x-format-output: txt-matched-rules' [http://sandbox.coreruleset.org/anything](http://sandbox.coreruleset.org/anything)\?id=alias%20j%3Da%3B%20c%24jt
*   Trying 52.4.200.1:80...
* Connected to sandbox.coreruleset.org (52.4.200.1) port 80 (#0)
> GET /anything?id=alias%20j%3Da%3B%20c%24jt HTTP/1.1
> Host: sandbox.coreruleset.org
> User-Agent: curl/7.71.1
> Accept: */*
> x-crs-mode: blocking
> x-crs-paranoia-level: 4
> x-format-output: txt-matched-rules
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 403 Forbidden
< Date: Mon, 01 Aug 2022 19:01:45 GMT
< Content-Type: text/plain; charset=iso-8859-1
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Unique-ID: YugjGftRsKOn4C5Ph9mAmgAAAMs
< x-backend: apache-nightly
< 
920273 PL4 Invalid character in request (outside of very strict set)
942432 PL4 Restricted SQL Character Anomaly Detection (args): # of special characters exceeded (2)
949110 PL1 Inbound Anomaly Score Exceeded (Total Score: 8)
980130 PL1 Inbound Anomaly Score Exceeded (Total Inbound Score: 8 - SQLI=3,XSS=0,RFI=0,LFI=0,RCE=0,PHPI=0,HTTP=0,SESS=0): individual paranoia level scores: 0, 0, 0, 8
* Connection #0 to host sandbox.coreruleset.org left intact</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:03 UTC</span>

<span style="font-size: 90%;">So we have the 403 and the rules.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:04 UTC</span>

<span style="font-size: 90%;">I think it's quite nice for scripting to have two different response codes</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:11 UTC</span>

<span style="font-size: 90%;">a good use case could be somebody just running sqlmap, which should handle this gracefully.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:31 UTC</span>

<span style="font-size: 90%;">Without having to add custom headers to sqlmap.</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:51 UTC</span>

<span style="font-size: 90%;">Is there a really strong argument for having 200 as a default?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:41 UTC</span>

<span style="font-size: 90%;">I think the most important use case was security researcher using a full blown backend application in the browser - and having to add http headers in the browser.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:14 UTC</span>

<span style="font-size: 90%;">It's a bit a pity _@fzipitria_ seems to have been summoned by his masters.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:25 UTC</span>

<span style="font-size: 90%;">He was rather in favor of 200.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:06:23 UTC</span>

<span style="font-size: 90%;">Hey! Sorry completely missed that is meeting day</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:28 UTC</span>

<span style="font-size: 90%;">I make the following proposal: Unless Felipe and maybe _@theMiddle_ bring some cutting arguments in favor of 200 we'll change to 403 by default during the week. OK?</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:37 UTC</span>

<span style="font-size: 90%;">Check!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:52 UTC</span>

<span style="font-size: 90%;">Hey, hey _@theMiddle_. Still in holiday mood? :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:57 UTC</span>

<span style="font-size: 90%;">Mention me cause so that I can update the docs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:13 UTC</span>

<span style="font-size: 90%;">Yes, we need to have this option in the docs as well. Of course.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:07:48 UTC</span>

<span style="font-size: 90%;">At home from Sunday, I need some time to restart :joy:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:02 UTC</span>

<span style="font-size: 90%;">Have you talked about challenges for sandbox?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:14 UTC</span>

<span style="font-size: 90%;">No, we did not. Anything to cover on that front?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:51 UTC</span>

<span style="font-size: 90%;">Didn't pushed on repo bit I've done some challenge for sqli and rce</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:02 UTC</span>

<span style="font-size: 90%;">I can do the same easily for different xss</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:11 UTC</span>

<span style="font-size: 90%;">And also ssti</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:22 UTC</span>

<span style="font-size: 90%;">Ops, sorry I mean ssrd</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:27 UTC</span>

<span style="font-size: 90%;">Ssrf</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:36 UTC</span>

<span style="font-size: 90%;">Damn phone :joy:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:46 UTC</span>

<span style="font-size: 90%;">Sound good.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:10:03 UTC</span>

<span style="font-size: 90%;">When all should be ready?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:07 UTC</span>

<span style="font-size: 90%;">Are you OK with the "403 if threshold met" behaviour by default for the sandbox?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:10:18 UTC</span>

<span style="font-size: 90%;">Yep</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:21 UTC</span>

<span style="font-size: 90%;">We are no longer part of the Bug Bounty event in August.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:33 UTC</span>

<span style="font-size: 90%;">Maybe you overlooked that notice.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:10:35 UTC</span>

<span style="font-size: 90%;">Ah Oky!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:43 UTC</span>

<span style="font-size: 90%;">So you have more time.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:10:55 UTC</span>

<span style="font-size: 90%;">That's good</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:01 UTC</span>

<span style="font-size: 90%;">The point was that we could not accept anything but a very little scope and they were not easy with that.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:11:12 UTC</span>

<span style="font-size: 90%;">I see</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:23 UTC</span>

<span style="font-size: 90%;">Let's look at the next item.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:25 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/2562](https://github.com/coreruleset/coreruleset/pull/2562)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:44 UTC</span>

<span style="font-size: 90%;">Here we have a particular question: Should .axd be restricted by default.</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:07 UTC</span>

<span style="font-size: 90%;">I think someone (azurit?) mentioned that the .axd files are actually used by the browser</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:14 UTC</span>

<span style="font-size: 90%;">Or should it be restricted from by default from PL2? (Or not at all, but present as a commented out option in setup.conf)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:09 UTC</span>

<span style="font-size: 90%;">If we do it from PL2, then we would change a modsec config variable from PL1 to PL2 and we have not done this before. Could be rather complicated or unintuitive for the users.</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:12 UTC</span>

<span style="font-size: 90%;">Hmm. We give users the option to set their own preferences. Then PL2 would override this? That feels complex and counterintuitive to me.</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:27 UTC</span>

<span style="font-size: 90%;">haha, brain sync</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:29 UTC</span>

<span style="font-size: 90%;">For the record, we removed axd from the restricted list in 1925.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:15 UTC</span>

<span style="font-size: 90%;">(The question only came up when reviewing this otherwise perfect PR.)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:14:43 UTC</span>

<span style="font-size: 90%;">If we removed .axd in 7 Dec 2020 and no one has noticed or complained… maybe we keep it simple and take it out for good :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:15:06 UTC</span>

<span style="font-size: 90%;">Assuming there are no objections or good reasons to add it back in.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:18 UTC</span>

<span style="font-size: 90%;">I'd agree to that. And if somebody has hard feelings we're open for a PR that adds a commented out variant with .axd to crs-setup.conf.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:31 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:32 UTC</span>

<span style="font-size: 90%;">Great plan.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:53 UTC</span>

<span style="font-size: 90%;">Agreed. I'd add a comment to the rule file though, explaining the decision</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:01 UTC</span>

<span style="font-size: 90%;">Otherwise someone will want to put it back in.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:09 UTC</span>

<span style="font-size: 90%;">Feel free to PR. Happy to merge.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:36 UTC</span>

<span style="font-size: 90%;">I'll sort that out tomorrow and add a note about AXD being removed, then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:46 UTC</span>

<span style="font-size: 90%;">And now for the really hard question: [#2591](https://github.com/coreruleset/coreruleset/issues/#2591).</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:59 UTC</span>

<span style="font-size: 90%;">Aaaaah</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:01 UTC</span>

<span style="font-size: 90%;">Please let me smmarize and then _@Karel_ and _@maxleske_ can correct me.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:30 UTC</span>

<span style="font-size: 90%;">We have a problem on Accept-Header that would best be solved via a look-around. But we do not want such advanced regex stuff in our rules anymore.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:39 UTC</span>

<span style="font-size: 90%;">:innocent:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:58 UTC</span>

<span style="font-size: 90%;">Sorry, I’m back</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:39 UTC</span>

<span style="font-size: 90%;">So we have 2 options to deal with this:
</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:23 UTC</span>

<span style="font-size: 90%;">Max therefore proposed to merge his regex as a temporary solution to the problem and incorporate Karel's script in the long run.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:02 UTC</span>

<span style="font-size: 90%;">Karel - please correct me if I'm wrong - would rather see the better regex created with the PoC script.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">_@maxleske_: Could you explain what the CONs against merging the "better" regex are right now?</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:30 UTC</span>

<span style="font-size: 90%;">So the PoC script is not totally finished, but it is in a state that would generate this particular regex?</span>

**Karel** <span style="color: grey; font-size: 90%;">19:22:50 UTC</span>

<span style="font-size: 90%;">Correct _@walter_</span>

**Karel** <span style="color: grey; font-size: 90%;">19:23:00 UTC</span>

<span style="font-size: 90%;">the current issue now is that it won't accept more than two input values</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:11 UTC</span>

<span style="font-size: 90%;">The script ought to be integrated into regex-assembly do get a clean solution.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:12 UTC</span>

<span style="font-size: 90%;">The regular expression _@Karel_ provided works, so yes, it would indeed be an option to use it right now. The only point against it is that it only handles two character sets and the script currently can't handle more than two</span>

**Karel** <span style="color: grey; font-size: 90%;">19:23:27 UTC</span>

<span style="font-size: 90%;">I think I know what the problem is and how to fix it though</span>

**Karel** <span style="color: grey; font-size: 90%;">19:23:42 UTC</span>

<span style="font-size: 90%;">Another issue is that even if I did, it would only be able to handle literal values</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:49 UTC</span>

<span style="font-size: 90%;">Alright. And it can be legal to send more charsets with a q precedence, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:10 UTC</span>

<span style="font-size: 90%;">Ah, yes. Important detail. And the regex of Max is more flexible in terms of charset, but less elegant.</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">19:24:52 UTC</span>

<span style="font-size: 90%;">For what it's worth, we should be able to actually solve this using a PCRE lexer and reversing the regex</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:25:16 UTC</span>

<span style="font-size: 90%;">That’s the way of thinking :partyparrot:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:27:24 UTC</span>

<span style="font-size: 90%;">For what it's worth, we should be able to actually solve this using a PCRE lexer and reversing the regex - if you like the pain, you should take a look this:
[https://github.com/zherczeg/repan](https://github.com/zherczeg/repan)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:13 UTC</span>

<span style="font-size: 90%;">_@walter_ correct</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:21 UTC</span>

<span style="font-size: 90%;">Max’s regex also is ReDOSable, which is not good</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:39 UTC</span>

<span style="font-size: 90%;">We could put length limits on the header</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:44 UTC</span>

<span style="font-size: 90%;">Yes, although regexploit doesn't seem to think so :shrug:</span>

**Karel** <span style="color: grey; font-size: 90%;">19:24:52 UTC</span>

<span style="font-size: 90%;">For what it's worth, we should be able to actually solve this using a PCRE lexer and reversing the regex</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">19:24:52 UTC</span>

<span style="font-size: 90%;">For what it's worth, we should be able to actually solve this using a PCRE lexer and reversing the regex</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:25:16 UTC</span>

<span style="font-size: 90%;">That’s the way of thinking :partyparrot:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:27:24 UTC</span>

<span style="font-size: 90%;">For what it's worth, we should be able to actually solve this using a PCRE lexer and reversing the regex - if you like the pain, you should take a look this:
[https://github.com/zherczeg/repan](https://github.com/zherczeg/repan)</span>

**Karel** <span style="color: grey; font-size: 90%;">19:25:37 UTC</span>

<span style="font-size: 90%;">I couldn't find any out of the box Python libraries for this however</span>

**Karel** <span style="color: grey; font-size: 90%;">19:25:45 UTC</span>

<span style="font-size: 90%;">Might have to look further into that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:02 UTC</span>

<span style="font-size: 90%;">New proposal: if _@Karel_ can get the script to work with more than two charsets we could use the regex generated from there. Then we can wait to integrate the script until it's polished.</span>

**Karel** <span style="color: grey; font-size: 90%;">19:26:22 UTC</span>

<span style="font-size: 90%;">Actually, there might be an even better solution</span>

**Karel** <span style="color: grey; font-size: 90%;">19:26:45 UTC</span>

<span style="font-size: 90%;">since loose scripts are undesirable, we should be able to extend the regexp-assemble preprocessor and make it part of the data files</span>

**Karel** <span style="color: grey; font-size: 90%;">19:27:07 UTC</span>

<span style="font-size: 90%;">That way you could include an assemble block and dynamically generate them without the need for an external script</span>

**Karel** <span style="color: grey; font-size: 90%;">19:27:28 UTC</span>

<span style="font-size: 90%;">Perhaps even snoop off the optimizations of the perl script</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:45 UTC</span>

<span style="font-size: 90%;">That is my (longterm) plan.</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">19:29:08 UTC</span>

<span style="font-size: 90%;">If that is too long-term, we can limit it to just literal strings</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:31:44 UTC</span>

<span style="font-size: 90%;">Sorry, what do you mean by "literal strings"?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:17 UTC</span>

<span style="font-size: 90%;">_@Karel_: How about multi-charset support for the script as a temporary solution?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:27 UTC</span>

<span style="font-size: 90%;">To close the PR we need a solution ASAP.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:52 UTC</span>

<span style="font-size: 90%;">Well it's not the only open PR, but if I was Karel, I'd get uneasy. :slightly_smiling_face:</span>

**Karel** <span style="color: grey; font-size: 90%;">19:29:08 UTC</span>

<span style="font-size: 90%;">If that is too long-term, we can limit it to just literal strings</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">19:29:08 UTC</span>

<span style="font-size: 90%;">If that is too long-term, we can limit it to just literal strings</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:31:44 UTC</span>

<span style="font-size: 90%;">Sorry, what do you mean by "literal strings"?</span>

**Karel** <span style="color: grey; font-size: 90%;">19:29:19 UTC</span>

<span style="font-size: 90%;">_@dune73_ you underestimate my perfectionism :laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:36 UTC</span>

<span style="font-size: 90%;">I probably do, I probably do.</span>

**Karel** <span style="color: grey; font-size: 90%;">19:29:49 UTC</span>

<span style="font-size: 90%;">I think the regexp-assemble extending proposal is a good idea though. Even if we just limit to literal strings</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:47 UTC</span>

<span style="font-size: 90%;">It's a very good idea, but that is apparently not a near-term solution and the PR should be merged earlier.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:51 UTC</span>

<span style="font-size: 90%;">I'm really torn.</span>

**Karel** <span style="color: grey; font-size: 90%;">19:31:53 UTC</span>

<span style="font-size: 90%;">_@maxleske_ how good do you feel about your regex? Something about the sophisticated-ness doesn't sit well with me, but it's the only way that does not rely on a 3rd party tool</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:32 UTC</span>

<span style="font-size: 90%;">Out of curiosity: why you say affected by redos if regexploit didn't find anything?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:50 UTC</span>

<span style="font-size: 90%;">I feel confident but I wouldn't assume that it would withstand all scrutiny.</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">It surely won’t be as bad as having broken recommended rules for 10 years. :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:57 UTC</span>

<span style="font-size: 90%;">(actually, there's a small fix to the regex I originally proposed that brings the performance within _@Karel_’s regex, so I'm not sure that it's still dosable)</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:07 UTC</span>

<span style="font-size: 90%;">I feel tempted by starting with the (fixed) regexp for now, and revisit the issue when the script is going places.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">What is the fixed regexp? The one from Max?</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:35 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:06 UTC</span>

<span style="font-size: 90%;">For the charset reasons (in light of ModSec being really poor with non-EU charsets)?</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:01 UTC</span>

<span style="font-size: 90%;">Well, I would say, it will be months until we have a new RC. If the regexp causes FP or we find a bypass, we likely have time for plan B.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:13 UTC</span>

<span style="font-size: 90%;">I see.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:59 UTC</span>

<span style="font-size: 90%;">_@Karel_ can you live with that temporary solution? The idea is to work with your script here, but not until it supports more charsets. We're already hurting people with mixed or non-EU charsets. Making their ModSec life even more miserable would be unfair.</span>

**Karel** <span style="color: grey; font-size: 90%;">19:42:51 UTC</span>

<span style="font-size: 90%;">Yes, I can, mostly because my approach cannot support e.g. iso-8551-[xy]  without including them as standalone entries (iso-8551-x  and iso-8551-y). That might put a heavier burden on maintenance</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:13 UTC</span>

<span style="font-size: 90%;">Thank you very much.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:54 UTC</span>

<span style="font-size: 90%;">And thank you all for your considerate contributions in this discussion. And for explaining everything to me in the PR.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:11 UTC</span>

<span style="font-size: 90%;">Thanks for talking it through again!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:22 UTC</span>

<span style="font-size: 90%;">With that being said, 75min into the meeting and we have cracked a few tough nuts.</span>

**Karel** <span style="color: grey; font-size: 90%;">19:44:23 UTC</span>

<span style="font-size: 90%;">Though I'd love to take a closer look at _@maxleske_’s regular expression, there might still be ways to improve readability, because it'll probably stay there for a while until we can work on long-term goals. This is something I should be able to do on my own, however. Shouldn't cause you any additional workload _@maxleske_ :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:08 UTC</span>

<span style="font-size: 90%;">I'd love that! In fact, I was going to write the regex with regexp-assemble and comment the different parts.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:07 UTC</span>

<span style="font-size: 90%;">During the retreat can we have a training for regexp assemble?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:07 UTC</span>

<span style="font-size: 90%;">Good, so let's look at the rest of the agenda.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:11 UTC</span>

<span style="font-size: 90%;">Asking for a friend</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:47:26 UTC</span>

<span style="font-size: 90%;">I told you don't tell them I asked this... :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:30 UTC</span>

<span style="font-size: 90%;">Yes! But do see the docs page about it. It’s really good!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:32 UTC</span>

<span style="font-size: 90%;">lol sure :smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:46 UTC</span>

<span style="font-size: 90%;">Regexp school! Sign me up</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:24 UTC</span>

<span style="font-size: 90%;">_@xanadu_ is thinking about a technical blog post to address FPs questions via a body of text as part of our regular testing. This has been discussed before but it's nice to see somebody pick it up.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:52 UTC</span>

<span style="font-size: 90%;">For Google Summer of Code, we have 2 project running as you probably know.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:18 UTC</span>

<span style="font-size: 90%;">One is about CVE testing automation and it's seems to make some great progress and I presume a positive mid-term evaluation (due last week).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:31 UTC</span>

<span style="font-size: 90%;">How is the machine learning project's mid-term evaluation?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:45 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ / _@fzipitria_?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:54 UTC</span>

<span style="font-size: 90%;">We discussed about it and if we should let the mentee pass or not. We decided to submit e "pass" but with the addition "we are not sure about it".</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:04 UTC</span>

<span style="font-size: 90%;">I have to go in a few minutes, I have had a very busy day and have to do a few $dayjob tasks before passing out…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:52 UTC</span>

<span style="font-size: 90%;">Thank you _@franbuehler_. That means you are uneasy, but you let her continue for the time being and she knows she has to deliver or the project is cancelled. Correct?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:34 UTC</span>

<span style="font-size: 90%;">Yes, she knows that she really has to deliver now and that if the project slows down again we will tell Google about it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:02 UTC</span>

<span style="font-size: 90%;">For the record: ML project had the best submission / project plan, but what we have seen so far has been unsatisfying, also because she did not follow her own plan (with more or less good reasons, but still).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:08 UTC</span>

<span style="font-size: 90%;">OK. So that is covered too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:16 UTC</span>

<span style="font-size: 90%;">I suggest we turn to the open PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:18 UTC</span>

<span style="font-size: 90%;">OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:33 UTC</span>

<span style="font-size: 90%;">We'll take it LIFO. :slightly_smiling_face:
[#2702](https://github.com/coreruleset/coreruleset/issues/#2702): hackathon submission. _@fzipitria_ you reviewed already. So ready to merge or do we assign anybody?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:58 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:23 UTC</span>

<span style="font-size: 90%;">I see everybody is exhausted. Let's volunteer _@fzipitria_ as reviewer and you merge when you think it ready. OK?</span>

**Karel** <span style="color: grey; font-size: 90%;">19:56:45 UTC</span>

<span style="font-size: 90%;">I see everybody is exhaustedUnusually exhausted if I'm being honest :sweat_smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:57:18 UTC</span>

<span style="font-size: 90%;">assigned</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:42 UTC</span>

<span style="font-size: 90%;">In [#2677](https://github.com/coreruleset/coreruleset/issues/#2677), we have a few commands that could profit from adding the @ flag to avoid some false positives.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:50 UTC</span>

<span style="font-size: 90%;">The question is which commans.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:19 UTC</span>

<span style="font-size: 90%;">I did a new pass trying to find “english” words</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:40 UTC</span>

<span style="font-size: 90%;">In the end, we could add it to any command that receives parameters</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:49 UTC</span>

<span style="font-size: 90%;">For people like me: @ instructs regex-assembly to add a construct after the keyword. That construct looks for whitespace.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:58 UTC</span>

<span style="font-size: 90%;">But we will always have things like top</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:07 UTC</span>

<span style="font-size: 90%;">yep…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:13 UTC</span>

<span style="font-size: 90%;">A common word, that is a command with no params</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:15 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:27 UTC</span>

<span style="font-size: 90%;">c’est la vie </span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:29 UTC</span>

<span style="font-size: 90%;">Yes. id is another one</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:35 UTC</span>

<span style="font-size: 90%;">yep</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:48 UTC</span>

<span style="font-size: 90%;">I think we traditionally add it to English words, but most commands are not. My impression was just that the PR is somewhat inconsistent.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:01:23 UTC</span>

<span style="font-size: 90%;">Also, the old rule wasn't very strict on which words would have the @, so I don't think we need to be pedantic about it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:56 UTC</span>

<span style="font-size: 90%;">So we'll merge as is?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:44 UTC</span>

<span style="font-size: 90%;">_@xanadu_ had a comment about matching python. Not sure if we still need the custom regex for python now...</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:03:02 UTC</span>

<span style="font-size: 90%;">Sorry friends, i have to go. Good night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:19 UTC</span>

<span style="font-size: 90%;">I must also sign off. Thank you all!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:20 UTC</span>

<span style="font-size: 90%;">Bye _@azurIt_. Thank you for joining. Very nice to see you in the meeting.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:20 UTC</span>

<span style="font-size: 90%;">I think this particular rule is okay because it's not looking for a weird suffix, so there isn't a big hole for evasions, I think.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:50 UTC</span>

<span style="font-size: 90%;">But since it always matches python, do we need to look for any suffixes?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:28 UTC</span>

<span style="font-size: 90%;">Ah, good one</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:32 UTC</span>

<span style="font-size: 90%;">I don't know. What's the rationale for the
'[23]?(?:\.[0-9.]+)?(?:[dmu]+)?
in this context?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:40 UTC</span>

<span style="font-size: 90%;">It's definitely needed elsewhere</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:04:46 UTC</span>

<span style="font-size: 90%;">But maybe not here?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:05:18 UTC</span>

<span style="font-size: 90%;">Let's discuss that in the PR.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:27 UTC</span>

<span style="font-size: 90%;">Unless the ##!$ \b messes things up? Not sure.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:35 UTC</span>

<span style="font-size: 90%;">It didn't seem to cause a problem when testing.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:05:57 UTC</span>

<span style="font-size: 90%;">Sorry, I have to go too. Could someone fill the decisions here from PR 2677 on??

[https://github.com/coreruleset/coreruleset/issues/2690#issuecomment-1201615925](https://github.com/coreruleset/coreruleset/issues/2690#issuecomment-1201615925)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:06:07 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:25 UTC</span>

<span style="font-size: 90%;">bb</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:36 UTC</span>

<span style="font-size: 90%;">I can take over</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:06:58 UTC</span>

<span style="font-size: 90%;">Thank you!!</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:08:22 UTC</span>

<span style="font-size: 90%;">np</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:02 UTC</span>

<span style="font-size: 90%;">Good, so who is shepherding this PR to be merged?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:22 UTC</span>

<span style="font-size: 90%;">_@maxleske_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:34 UTC</span>

<span style="font-size: 90%;">I see you are already assinged ..</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:07:55 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:14 UTC</span>

<span style="font-size: 90%;">All sorted out then. Thanks. Feel free to merge if you see it ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:27 UTC</span>

<span style="font-size: 90%;">Similar situation [#2676](https://github.com/coreruleset/coreruleset/issues/#2676).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:08:57 UTC</span>

<span style="font-size: 90%;">Can be merged. _@fzipitria_?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:09:36 UTC</span>

<span style="font-size: 90%;">Let me see. Probably yes.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:10:10 UTC</span>

<span style="font-size: 90%;">Yes. Can be merged.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:03 UTC</span>

<span style="font-size: 90%;">Is there anything we need to take care of together here?
I suggest _@maxleske_ deals with it the same way.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:09:13 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:50 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:51 UTC</span>

<span style="font-size: 90%;">Oops, I left a cryptic comment on that one and didn't follow up earlier… Same story, I think: it doesn't need anything special about adding the anti-evasion patterns, just like 2677</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:10:23 UTC</span>

<span style="font-size: 90%;">Ok, thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:10:37 UTC</span>

<span style="font-size: 90%;">Ok, we can remove both then</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:10 UTC</span>

<span style="font-size: 90%;">[#2666](https://github.com/coreruleset/coreruleset/issues/#2666) is again a tricky one. We have a new contributor with a negative lookaround to deal with Japanese charset.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:16 UTC</span>

<span style="font-size: 90%;">What do we do?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:49 UTC</span>

<span style="font-size: 90%;">No lookarounds.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:50 UTC</span>

<span style="font-size: 90%;">(Our contributing guidelines say that we do not want lookaround if I'm not mistaken.)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:26 UTC</span>

<span style="font-size: 90%;">So do we politely close the PR after Max has explained the alternative look-around emulation?</span>

**Karel** <span style="color: grey; font-size: 90%;">20:12:48 UTC</span>

<span style="font-size: 90%;">That's pretty much the only option right now, no?</span>

**Karel** <span style="color: grey; font-size: 90%;">20:13:01 UTC</span>

<span style="font-size: 90%;">Unless they manually create an emulated look around</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:13 UTC</span>

<span style="font-size: 90%;">Well, they are RedHat.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:21 UTC</span>

<span style="font-size: 90%;">Yes. I'd ask for an emulated lookaround.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:13:23 UTC</span>

<span style="font-size: 90%;">They might devote some time to solve this :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:28 UTC</span>

<span style="font-size: 90%;">Somebody can also volunteer to shepherd the PR wit the said alternative emulation.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:55 UTC</span>

<span style="font-size: 90%;">I'll do it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:56 UTC</span>

<span style="font-size: 90%;">If it's RedHat, then there might be some value to followup and ask them to walk the extra mile.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:02 UTC</span>

<span style="font-size: 90%;">Thank you _@maxleske_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:12 UTC</span>

<span style="font-size: 90%;">[#2663](https://github.com/coreruleset/coreruleset/issues/#2663)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:40 UTC</span>

<span style="font-size: 90%;">I need to document removals</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:43 UTC</span>

<span style="font-size: 90%;">This is ready to be merged, but there is a final comment.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:02 UTC</span>

<span style="font-size: 90%;">Yes, exactly. Can you do this? Afterwards it's ready to be merged AFAICS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:15:17 UTC</span>

<span style="font-size: 90%;">One of the things I thought is to add everything and left the ones commented</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:15:46 UTC</span>

<span style="font-size: 90%;">It will be easier to compare in future diffs I think</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:15:50 UTC</span>

<span style="font-size: 90%;">++</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:57 UTC</span>

<span style="font-size: 90%;">Nice thought.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:15:58 UTC</span>

<span style="font-size: 90%;">Ok, sounds like a plan</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:24 UTC</span>

<span style="font-size: 90%;">We have plenty of reviewers assigned here. Feel free to merge once Felipe is done.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:21 UTC</span>

<span style="font-size: 90%;">[#2637](https://github.com/coreruleset/coreruleset/issues/#2637) is a welcome contribution from long term contact _@Ruben Van Vreeland_. Unfortunately the tests fail. What do we do?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:20 UTC</span>

<span style="font-size: 90%;">I can take a look. Shouldn't be hard.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:09 UTC</span>

<span style="font-size: 90%;">I think he did not adopt the tests when changing the rules. But I migh tbe mistaken.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:17 UTC</span>

<span style="font-size: 90%;">Thank you _@maxleske_.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:19 UTC</span>

<span style="font-size: 90%;">Yes, my idea too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:36 UTC</span>

<span style="font-size: 90%;">We're halfway through.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:27 UTC</span>

<span style="font-size: 90%;">[#2595](https://github.com/coreruleset/coreruleset/issues/#2595): This is a bug bounty fix. Has been open for very long, probably due to failing tests.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:38 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ you planned to look into the failures. Did you have time for that?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:49 UTC</span>

<span style="font-size: 90%;">Yes, but I need to debug this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:00 UTC</span>

<span style="font-size: 90%;">Sorry, my wife is no longer able to handle the kids (national holiday, everybody is a bit over-excited). I need to quit and support here.
Please somebody take over.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:01 UTC</span>

<span style="font-size: 90%;">It is weird that it doesn’t work as expected</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:19 UTC</span>

<span style="font-size: 90%;">Ok, let me see what’s next</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:22:52 UTC</span>

<span style="font-size: 90%;">[#2591](https://github.com/coreruleset/coreruleset/issues/#2591) was already tackled</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:01 UTC</span>

<span style="font-size: 90%;">Excellent</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:13 UTC</span>

<span style="font-size: 90%;">Then [#2584](https://github.com/coreruleset/coreruleset/issues/#2584)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:36 UTC</span>

<span style="font-size: 90%;">Looks like it has conflicts still</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:59 UTC</span>

<span style="font-size: 90%;">There is the Resolve conflicts button available</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:10 UTC</span>

<span style="font-size: 90%;">That we can use in this case</span>

**airween** <span style="color: grey; font-size: 90%;">20:24:50 UTC</span>

<span style="font-size: 90%;">have you tried it ever?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:24 UTC</span>

<span style="font-size: 90%;">Done</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:28 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**airween** <span style="color: grey; font-size: 90%;">20:25:40 UTC</span>

<span style="font-size: 90%;">you are a hero! :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:59 UTC</span>

<span style="font-size: 90%;">Oops</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:26:09 UTC</span>

<span style="font-size: 90%;">I think I did it the other way around :rolling_on_the_floor_laughing:</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">I think you might be right :sweat_smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:01 UTC</span>

<span style="font-size: 90%;">I've assigned _@walter_ to review since he was working on it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:22 UTC</span>

<span style="font-size: 90%;">Ok, I’ll try to fix that one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">Next [#2581](https://github.com/coreruleset/coreruleset/issues/#2581)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">Thanks (although, I think that merge should work)</span>

**Karel** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">I think you might be right :sweat_smile:</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">I think you might be right :sweat_smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:45 UTC</span>

<span style="font-size: 90%;">nope, didn't :smile:</span>

**Karel** <span style="color: grey; font-size: 90%;">20:27:52 UTC</span>

<span style="font-size: 90%;">Python failed but Go didn't, make it make sense</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:18 UTC</span>

<span style="font-size: 90%;">[#2581](https://github.com/coreruleset/coreruleset/issues/#2581)?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:28:23 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:29:01 UTC</span>

<span style="font-size: 90%;">Looks like a nice rule, with extensive testing</span>

**Karel** <span style="color: grey; font-size: 90%;">20:29:12 UTC</span>

<span style="font-size: 90%;">Very nice rule indeed, props to the author</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:29:44 UTC</span>

<span style="font-size: 90%;">No data file</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:30:35 UTC</span>

<span style="font-size: 90%;">This is a stricter sibling and the original didn't have one either :((</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:30:13 UTC</span>

<span style="font-size: 90%;">We need a reviewer. Any takers?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:30:27 UTC</span>

<span style="font-size: 90%;">I can do a review</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:30:31 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**Karel** <span style="color: grey; font-size: 90%;">20:30:35 UTC</span>

<span style="font-size: 90%;">This is a stricter sibling and the original didn't have one either :((</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:30:35 UTC</span>

<span style="font-size: 90%;">This is a stricter sibling and the original didn't have one either :((</span>

**Karel** <span style="color: grey; font-size: 90%;">20:30:43 UTC</span>

<span style="font-size: 90%;">so I had nothing to base it off unfortunately</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:30:46 UTC</span>

<span style="font-size: 90%;">No, that’s a fault on us</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:04 UTC</span>

<span style="font-size: 90%;">We still need to do the reverse for many rules, sadly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:13 UTC</span>

<span style="font-size: 90%;">And derive meaning</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:26 UTC</span>

<span style="font-size: 90%;">(probably something that might happen in the dev retreat)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:50 UTC</span>

<span style="font-size: 90%;">Let’s move to the [#2575](https://github.com/coreruleset/coreruleset/issues/#2575)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:05 UTC</span>

<span style="font-size: 90%;">This one looks to be more work</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:12 UTC</span>

<span style="font-size: 90%;">Haven't we already a rule for php variable function?</span>

**Karel** <span style="color: grey; font-size: 90%;">20:32:53 UTC</span>

<span style="font-size: 90%;">Yes, but this is a stricter sibling _@theMiddle_</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:33:11 UTC</span>

<span style="font-size: 90%;">Ops sorry was reading the 2581</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:35 UTC</span>

<span style="font-size: 90%;">[#2575](https://github.com/coreruleset/coreruleset/issues/#2575) needs to be tested on traffic, apparently.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:58 UTC</span>

<span style="font-size: 90%;">And there is stuff missing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:01 UTC</span>

<span style="font-size: 90%;">So we need a taker</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:34:07 UTC</span>

<span style="font-size: 90%;">Oh, I think I remember this one. IIRC it was this bit
[\"'`]\s*?;which raised some eyebrows.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:34:10 UTC</span>

<span style="font-size: 90%;">Since the author did not respond, we need to do it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:21 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:43 UTC</span>

<span style="font-size: 90%;">Who has traffic to run this?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:20 UTC</span>

<span style="font-size: 90%;">What was the "second issue"?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:35:39 UTC</span>

<span style="font-size: 90%;">Doesn’t address all vulns</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:35:52 UTC</span>

<span style="font-size: 90%;">Partial for 5UXE4RK0</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:36:23 UTC</span>

<span style="font-size: 90%;">k</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:36:36 UTC</span>

<span style="font-size: 90%;">I’ll assign this temporarily to Walter</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:36:48 UTC</span>

<span style="font-size: 90%;">He has offered in the past to run with traffic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:36:58 UTC</span>

<span style="font-size: 90%;">Until we have a better option ¯\\\_(ツ)\_/¯</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:24 UTC</span>

<span style="font-size: 90%;">:thumbsup:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:31 UTC</span>

<span style="font-size: 90%;">Last one!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:37:39 UTC</span>

<span style="font-size: 90%;">Yes. We have conflicts here</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:37:39 UTC</span>

<span style="font-size: 90%;">[#2573](https://github.com/coreruleset/coreruleset/issues/#2573)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:10 UTC</span>

<span style="font-size: 90%;">Can you rebase this one and address comments _@Karel_?</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:40:30 UTC</span>

<span style="font-size: 90%;">Will do!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:35 UTC</span>

<span style="font-size: 90%;">I've requested changes too. I'd say, we wait for _@Karel_ to address that</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:40:38 UTC</span>

<span style="font-size: 90%;">Will do!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:52 UTC</span>

<span style="font-size: 90%;">I think it is a really good PRs, and makes a nice usage on regexp-assemble</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:02 UTC</span>

<span style="font-size: 90%;">I agree</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:05 UTC</span>

<span style="font-size: 90%;">Cool, then we are done for the day.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:15 UTC</span>

<span style="font-size: 90%;">We made progress! :partyparrot:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:41 UTC</span>

<span style="font-size: 90%;">phew</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:39:43 UTC</span>

<span style="font-size: 90%;">Good evening. Just got back from wedding. Sorry I missed the meeting</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:59 UTC</span>

<span style="font-size: 90%;">perfect timing Paul, we just finished :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:07 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**Karel** <span style="color: grey; font-size: 90%;">20:40:18 UTC</span>

<span style="font-size: 90%;">Let the archive show that the meeting is finished</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:23 UTC</span>

<span style="font-size: 90%;">Have a good night everyone!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:31 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:40:32 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:40:34 UTC</span>

<span style="font-size: 90%;">bb</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:37 UTC</span>

<span style="font-size: 90%;">I'm back too!</span>

**Karel** <span style="color: grey; font-size: 90%;">20:40:38 UTC</span>

<span style="font-size: 90%;">Will do!</span>

↳ **Karel** <span style="color: grey; font-size: 90%;">20:40:38 UTC</span>

<span style="font-size: 90%;">Will do!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:40:40 UTC</span>

<span style="font-size: 90%;">Good night</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:40:40 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:46 UTC</span>

<span style="font-size: 90%;">Thank you all very much. This was much productive.</span>

**airween** <span style="color: grey; font-size: 90%;">20:40:48 UTC</span>

<span style="font-size: 90%;">good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:40:50 UTC</span>

<span style="font-size: 90%;"><END OF MEETING></span>

