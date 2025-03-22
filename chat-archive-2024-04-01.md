### Mon, Apr 1st, 2024

**dune73** <span style="color: grey; font-size: 90%;">18:30:25 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly CRS chat. No joke.
Here is our agenda
[https://github.com/coreruleset/coreruleset/issues/3636](https://github.com/coreruleset/coreruleset/issues/3636)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:33 UTC</span>

<span style="font-size: 90%;">Anybody around?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:33 UTC</span>

<span style="font-size: 90%;">Welcome!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:37 UTC</span>

<span style="font-size: 90%;">Yup</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">Hey _@fzipitria_, glad I'm not alone. :slightly_smiling_face:</span>

**jit** <span style="color: grey; font-size: 90%;">18:31:51 UTC</span>

<span style="font-size: 90%;">Hi everyone</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:58 UTC</span>

<span style="font-size: 90%;">:bender:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:15 UTC</span>

<span style="font-size: 90%;">Hello _@jit_. Welcome. What time is it in your place now? (We're in Summertime here now)</span>

**jit** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;">Its 12:00 AM 2nd April here. So April fools doesn't apply to me.:sweat_smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:24 UTC</span>

<span style="font-size: 90%;">Well played, well played. And I'll never get around the XX:30min delay or advance in the time. Round hours, ok, but half hours ... :exploding_head:</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:35:57 UTC</span>

<span style="font-size: 90%;">We grew up with it, so can't complain about half hours. :man-shrugging:</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:40 UTC</span>

<span style="font-size: 90%;">hi there</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:32 UTC</span>

<span style="font-size: 90%;">Hello _@airween_. Let's wait for a couple of minutes to see if it's only the 4 of us.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:36:23 UTC</span>

<span style="font-size: 90%;">Hi, i'm here only partially.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:21 UTC</span>

<span style="font-size: 90%;">Hello _@azurit_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">Since it's already on the agenda, could you share what plugins you have in mind? What else is coming?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:40:26 UTC</span>

<span style="font-size: 90%;">These plugins can probably be accepted as official:
[https://github.com/azurit/modsecurity-database-logging-plugin](https://github.com/azurit/modsecurity-database-logging-plugin)
[https://github.com/azurit/modsecurity-xxe-lua-plugin](https://github.com/azurit/modsecurity-xxe-lua-plugin)
[https://github.com/azurit/modsecurity-xxe-plugin](https://github.com/azurit/modsecurity-xxe-plugin)
[https://github.com/azurit/modsecurity-geoip-plugin](https://github.com/azurit/modsecurity-geoip-plugin)</span>

**azurit** <span style="color: grey; font-size: 90%;">18:40:54 UTC</span>

<span style="font-size: 90%;">And this one official or unofficial, must be decided:
[https://github.com/azurit/modsecurity-false-positive-report-plugin](https://github.com/azurit/modsecurity-false-positive-report-plugin)</span>

**azurit** <span style="color: grey; font-size: 90%;">18:42:47 UTC</span>

<span style="font-size: 90%;">I have also one plugin in mind - some kind of notification plugin. If specific (based on configuration) rules are triggered, the notification is send via email or other channels (for example webshells rules).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:08 UTC</span>

<span style="font-size: 90%;">Would that be an individual or custom rule?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:15 UTC</span>

<span style="font-size: 90%;">Ah, webshells, get it.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:49 UTC</span>

<span style="font-size: 90%;">That could be interesting. One usually does that via a log platform, but if you do not want that, then this could be an alternative option.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:43:51 UTC</span>

<span style="font-size: 90%;">You probably really want to know everytime a webshell is triggered.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:03 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:19 UTC</span>

<span style="font-size: 90%;">OK, it's 15' into the meeting and it's the 5 of us. Do we go about this, or do we cancel?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:26 UTC</span>

<span style="font-size: 90%;">We're usually 7-10 people.</span>

**airween** <span style="color: grey; font-size: 90%;">18:45:25 UTC</span>

<span style="font-size: 90%;">we can continue, I guess</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:11 UTC</span>

<span style="font-size: 90%;">We can continue. If decisions need to be taken with more people, we can do it next week :shrug:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:35 UTC</span>

<span style="font-size: 90%;">But I don't see blocking issues</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:40 UTC</span>

<span style="font-size: 90%;">OK, then let's go about it.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:23 UTC</span>

<span style="font-size: 90%;">No that much happening outside development, first meeting of the SecLang Round Table happened and that was a good start.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:48 UTC</span>

<span style="font-size: 90%;">6 weeks after CRS4 and 1 week after CRS 4.1, I think it's safe to say the release(s) were successful.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:01 UTC</span>

<span style="font-size: 90%;">No big bugs reported so far, no crazy amount of false positives.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:38 UTC</span>

<span style="font-size: 90%;">There will certainly be problems coming with wider enterprise adoption, but it will be little by little, not an avalanche of reports ruining our team.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:55 UTC</span>

<span style="font-size: 90%;">Maybe, but not necessarily</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:05 UTC</span>

<span style="font-size: 90%;">v4 is a new standard in quality, imho</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:05 UTC</span>

<span style="font-size: 90%;">Think so too and I am glad we did not ship anything really bad we did not notice.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:12 UTC</span>

<span style="font-size: 90%;">Development is currently rather slow, so it might be a good period to declare the next release LTS. Before we start to do big rearchitecture stuff, overhauling rules because of DoS concerns etc. What do you think?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:32 UTC</span>

<span style="font-size: 90%;">I'm not in a hurry to declare anything now.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:43 UTC</span>

<span style="font-size: 90%;">Also.. what does it mean for something to be LTS?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:53 UTC</span>

<span style="font-size: 90%;">That is not in our policy I mean.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:59 UTC</span>

<span style="font-size: 90%;">For how long?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:07 UTC</span>

<span style="font-size: 90%;">Probably, that we will backport fixes etc.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:09 UTC</span>

<span style="font-size: 90%;">Is it 3 years? 5? 10?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:25 UTC</span>

<span style="font-size: 90%;">I'd say it should be 3, but 5 would be better.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:37 UTC</span>

<span style="font-size: 90%;">Are we sure about this?</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">why do we want to declare years, and not versions?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:56 UTC</span>

<span style="font-size: 90%;">The difficulty is not declaring it, the difficulty is executing on the promise.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:18 UTC</span>

<span style="font-size: 90%;">I think users would rather hear years than versions for their long term planning.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">Why do we need to engage in LTS? Why not providers?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:42 UTC</span>

<span style="font-size: 90%;">Because providers don't really know anything about CRS.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:52 UTC</span>

<span style="font-size: 90%;">See Debian updates of ModSec and CRS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:53 UTC</span>

<span style="font-size: 90%;">Then they pay some other company?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:07 UTC</span>

<span style="font-size: 90%;">Unless they pay us, I mean</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:32 UTC</span>

<span style="font-size: 90%;">We cannot make progress if we need to support LTS for 5 years.</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:47 UTC</span>

<span style="font-size: 90%;">_See Debian updates of ModSec and CRS._ - what should we see in this case?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:08 UTC</span>

<span style="font-size: 90%;">If anything, I would say that the lack of people for moving on and doing cool things is our limit</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:02 UTC</span>

<span style="font-size: 90%;">Well, we did not do much with 3.2 and 3.3 really. And now that the Changelog is automated, I do not think maintenance is that much of a drag anymore.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:24 UTC</span>

<span style="font-size: 90%;">I mean we should not plan to backport fixes for individual false negatives.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:44 UTC</span>

<span style="font-size: 90%;">But false positive fixes if they are reported and major security stuff, namely with the rule set.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:46 UTC</span>

<span style="font-size: 90%;">Then we need to figure it out what means to be an LTS</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:03 UTC</span>

<span style="font-size: 90%;">Because we keep evolving and looking back 5 years makes me cry a little</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">On how we are now</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:26 UTC</span>

<span style="font-size: 90%;">E.g. making a backport on 3.2 was a painful task that we never finished</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:34 UTC</span>

<span style="font-size: 90%;">But really because we had deviated that much from 3.2 and it was all a mess. I think backporting to 4.x will be easier.
But we should certainly define maintenance and LTS and make it a policy.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:43 UTC</span>

<span style="font-size: 90%;">Also because our users asked for it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:22 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:57 UTC</span>

<span style="font-size: 90%;">I think starting a document with comments (again, probably drive/docs is the best option) will be the reasonable option</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:00 UTC</span>

<span style="font-size: 90%;">So we can work async</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:29 UTC</span>

<span style="font-size: 90%;">OK, yes, let's do that then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:39 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:43 UTC</span>

<span style="font-size: 90%;">And the consensus seems to be to not rush this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:56 UTC</span>

<span style="font-size: 90%;">Cool, I'll create the document and link it here when done</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:08 UTC</span>

<span style="font-size: 90%;">Two question on status _@fzipitria_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:08 UTC</span>

<span style="font-size: 90%;">So people can add their comments</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:17 UTC</span>

<span style="font-size: 90%;">How close are we to new website?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:25 UTC</span>

<span style="font-size: 90%;">I would say 95%</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:28 UTC</span>

<span style="font-size: 90%;">I think 2-3 blog posts created since you started.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:35 UTC</span>

<span style="font-size: 90%;">Those need to be migrated</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:39 UTC</span>

<span style="font-size: 90%;">OK, a bit more work and release in the next 2 weeks?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:50 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:57 UTC</span>

<span style="font-size: 90%;">How can we help?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:00 UTC</span>

<span style="font-size: 90%;">I'll create a ticket with the remaining work</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:17 UTC</span>

<span style="font-size: 90%;">It is mostly about proofreading in most cases</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:25 UTC</span>

<span style="font-size: 90%;">+1</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:27 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:30 UTC</span>

<span style="font-size: 90%;">:bow:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:46 UTC</span>

<span style="font-size: 90%;">The website overtook your work on the sandbox relaunch. Where is that standing?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:25 UTC</span>

<span style="font-size: 90%;">Its frozen right now because I was blocked on making our new containers work</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:52 UTC</span>

<span style="font-size: 90%;">The nginx container has changed a bit and with that and the compose things were failing</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:57 UTC</span>

<span style="font-size: 90%;">Got you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:25 UTC</span>

<span style="font-size: 90%;">Can this be fixed within a useful time frame?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:12 UTC</span>

<span style="font-size: 90%;">I hope so. Probably if I sleep 1 or 2 hours per day I can handle that also :stuck_out_tongue:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:46 UTC</span>

<span style="font-size: 90%;">Plan to devote more time in the next two weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:39 UTC</span>

<span style="font-size: 90%;">Sorry for pestering you, will this be another 80h of work, or what are we looking at (I have no idea what it takes to get this flying again)?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:18 UTC</span>

<span style="font-size: 90%;">no, it's not probably that much</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:38 UTC</span>

<span style="font-size: 90%;">I'm only planning to fix [https://github.com/coreruleset/coreruleset/issues/3609](https://github.com/coreruleset/coreruleset/issues/3609) on this release</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:47 UTC</span>

<span style="font-size: 90%;">We still need to do an overhaul</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:02 UTC</span>

<span style="font-size: 90%;">OK. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:23 UTC</span>

<span style="font-size: 90%;">Let's get going with the agenda then:
[https://github.com/coreruleset/coreruleset/issues/3623](https://github.com/coreruleset/coreruleset/issues/3623)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:15 UTC</span>

<span style="font-size: 90%;">This is a problem with a security scanner like [ssllabs.com](http://ssllabs.com). [internet.nl](http://internet.nl) in this particular case.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:38 UTC</span>

<span style="font-size: 90%;">They check for available encoding, by sending an accept-encoding header with all potentially available encodings.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:06 UTC</span>

<span style="font-size: 90%;">Resulting in a 60-80 byte long header. And they ask us to grow our arbitrary limit of 50 chars.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:29 UTC</span>

<span style="font-size: 90%;">We have set the limit because it felt right, after an overflow on this header on some Windows system.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:08 UTC</span>

<span style="font-size: 90%;">Alternatively, they could also split their request in two, but they prefer not to do that because of the complexity of the code and what it would mean to the 10-20 HTTP requests they are doing right now ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:03 UTC</span>

<span style="font-size: 90%;">So do we comply and ask them to stop doing such exotic things?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:17:13 UTC</span>

<span style="font-size: 90%;">What about to make that limit configurable?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:42 UTC</span>

<span style="font-size: 90%;">I don't think it a crucial limit for us. The attacks were way bigger that the conservative 50 value we chose</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:43 UTC</span>

<span style="font-size: 90%;">If we make it configurable, then it's 1 additional variable and at least a 901 rule that checks for the configurable variable.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:57 UTC</span>

<span style="font-size: 90%;">I would really avoid another rule over this problem.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:08 UTC</span>

<span style="font-size: 90%;">So we double to 100 and we're done?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:19:56 UTC</span>

<span style="font-size: 90%;">Well, if it doesn't mean any harm.. But i must say that i never heard of internet.nl.. I mean,how many of our users are using their services?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:18 UTC</span>

<span style="font-size: 90%;">No idea. I've maybe seen them before 1-2 times. Nothing big, but we obviously annoy them and their users, which I can understand and relate to.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:44 UTC</span>

<span style="font-size: 90%;">Funny thing is, they are a security open source project and we're too. And they are really within the RFC with what they are doing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:27 UTC</span>

<span style="font-size: 90%;">OK, 100 and we move on with the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:50 UTC</span>

<span style="font-size: 90%;">We have crossed off the release topic already.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:02 UTC</span>

<span style="font-size: 90%;">So the plugins. Thanks for the list _@azurit_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:21 UTC</span>

<span style="font-size: 90%;">We do not really have a formalized process to get them into the plugin registry.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:29 UTC</span>

<span style="font-size: 90%;">I think it's about time we make it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:55 UTC</span>

<span style="font-size: 90%;">Would an issue per plugin on the registry repo with checkboxes help?</span>

**airween** <span style="color: grey; font-size: 90%;">19:25:44 UTC</span>

<span style="font-size: 90%;">could you explain this?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:27:13 UTC</span>

<span style="font-size: 90%;">A new PR template? I think it makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:43 UTC</span>

<span style="font-size: 90%;">_@airween_ We lack a process to accept new plugins. There are a few administrative tasks, but also a need for a more formalized review.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:55 UTC</span>

<span style="font-size: 90%;">A PR template is a good idea, indeed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:13 UTC</span>

<span style="font-size: 90%;">Maybe this is something _@azurit_ could do and then we try it out for his plugins.</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:33 UTC</span>

<span style="font-size: 90%;">I meant the formalization steps in details :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:17 UTC</span>

<span style="font-size: 90%;">but may be that's not important at the moment</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:28 UTC</span>

<span style="font-size: 90%;">Can't name them from back of my head.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:41 UTC</span>

<span style="font-size: 90%;">_@azurit_ is probably bringing his daughter to bed.</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:44 UTC</span>

<span style="font-size: 90%;">okay, no worries</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:46 UTC</span>

<span style="font-size: 90%;">I'll talk to him tomorrow.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:32 UTC</span>

<span style="font-size: 90%;">Finally docker container. Since Felipe and I have already talked this through and no real additional docker know-how here, I suggest we postpone this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:40 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:00 UTC</span>

<span style="font-size: 90%;">Other than: _@airween_, _@azurit_ and _@jit_ you are very welcome to comment on the google doc linked in the agenda.</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:23 UTC</span>

<span style="font-size: 90%;">I can check out later</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:33 UTC</span>

<span style="font-size: 90%;">(in details)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:34 UTC</span>

<span style="font-size: 90%;">Good. So is there anything else for tonight?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:49 UTC</span>

<span style="font-size: 90%;">No, nice and short. Love it!</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:46 UTC</span>

<span style="font-size: 90%;">_No, nice and short. Love it!_ - haha, we can make a limit for items and participants for monthly chats :smile:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:35:24 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/wiki/New-plugin-creation-and-integration](https://github.com/coreruleset/coreruleset/wiki/New-plugin-creation-and-integration)</span>

**azurit** <span style="color: grey; font-size: 90%;">19:36:04 UTC</span>

<span style="font-size: 90%;">This is what dune probably meant (regarding plugins).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:28 UTC</span>

<span style="font-size: 90%;">Yes, that was it, but making it into a PR template looks like a good plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:35 UTC</span>

<span style="font-size: 90%;">Thanks for attending and good night.</span>

**jit** <span style="color: grey; font-size: 90%;">19:39:41 UTC</span>

<span style="font-size: 90%;">Goodnight everyone. :blush:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:39:45 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:37 UTC</span>

<span style="font-size: 90%;">good night!</span>

