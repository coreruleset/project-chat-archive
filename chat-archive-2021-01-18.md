### Mon, Jan 18th, 2021

**dune73** <span style="color: grey; font-size: 90%;">19:31:41 UTC</span>

<span style="font-size: 90%;">Hello, hello, it's issue chat time. Welcome everybody.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:57 UTC</span>

<span style="font-size: 90%;">Our agenda is at [https://github.com/coreruleset/coreruleset/issues/1953](https://github.com/coreruleset/coreruleset/issues/1953)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:49 UTC</span>

<span style="font-size: 90%;">Hi guys.</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:03 UTC</span>

<span style="font-size: 90%;">hi there</span>

**Emile** <span style="color: grey; font-size: 90%;">19:33:10 UTC</span>

<span style="font-size: 90%;">hey o/</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">Before we start with the issues, I'd like to talk about the ModSec3 vulnerability of the day that we want to fight with a blog post and a workaround in the form of CRS 3.3.1-RC1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">Unfortunately, I am behind with the blog post - basically ready now - and we have surprising problems with the ModSec configuration / behaviour around this workaround.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:20 UTC</span>

<span style="font-size: 90%;">So we kind of need to assess the situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">_@airween_: Could you tell us the status of your attempts to reproduce the bad behaviour of our early-blocking feature / workaround reported in the ModSec issue?</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:08 UTC</span>

<span style="font-size: 90%;">yep</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:11 UTC</span>

<span style="font-size: 90%;">there was a problem when I checked first time the 3.3.1: if I sent a request like it was an attack, the webserver sent back the response without headers</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:09 UTC</span>

<span style="font-size: 90%;">but later an Nginx developer also noticed us, he ran into this problem</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:48 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ and me checked it again with the current code (modsecurity, modsecurity-connector), but couldn't reproduce the problem</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:00 UTC</span>

<span style="font-size: 90%;">anyway, now it works on Nginx too, but there is still an interesting behavior: after the first rule with block, the request processing continues...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:39:42 UTC</span>

<span style="font-size: 90%;">am I wrong or it could be an nginx connector issue?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">no, perhaps you're right. But the developer wrote he uses the current master state.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:56 UTC</span>

<span style="font-size: 90%;">and he is one of the author of connector :)</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:02 UTC</span>

<span style="font-size: 90%;">eg:


2021/01/14 10:53:38 [info] 587287[[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))](https://github.com/coreruleset/coreruleset/issues/[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))): *1 ModSecurity: Warning. Matched "Operator `PmFromFile' with parameter `scanners-user-agents.data' against variable `REQUEST_HEADERS:User-Agent' (Value: `Mozilla/5.00 (Nikto/2.1.5)' ) [file "/usr/share/modsecurity-crs/rules/REQUEST-913-SCANNER-DETECTION.conf"] [line "33"] [id "913100"] [rev ""] [msg "Found User-Agent associated with security scanner"] [data "Matched Data: nikto found within REQUEST_HEADERS:User-Agent: mozilla/5.00 (nikto/2.1.5)"] [severity "2"] [ver "OWASP_CRS/3.3.1"] [maturity "0"] [accuracy "0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-reputation-scanner"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "capec/1000/118/224/541/310"] [tag "PCI/6.5.10"] [hostname "::1"] [uri "/"] [unique_id "161062161853.669342"] [ref "o14,5v60,26t:lowercase"], client: ::1, server: _, request: "GET / HTTP/1.1", host: "localhost:8080"

2021/01/14 10:53:38 [error] 587287[[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))](https://github.com/coreruleset/coreruleset/issues/[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))): *1 [client ::1] ModSecurity: Access denied with code 403 (phase 1). Matched "Operator `Ge' with parameter `2' against variable `TX:ANOMALY_SCORE' (Value: `5' ) [file "/usr/share/modsecurity-crs/rules/REQUEST-949-BLOCKING-EVALUATION.conf"] [line "154"] [id "949111"] [rev ""] [msg "Inbound Anomaly Score Exceeded in phase 1 (Total Score: 5)"] [data ""] [severity "2"] [ver "OWASP_CRS/3.3.1"] [maturity "0"] [accuracy "0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-generic"] [hostname "::1"] [uri "/"] [unique_id "161062161853.669342"] [ref ""], client: ::1, server: _, request: "GET / HTTP/1.1", host: "localhost:8080"

2021/01/14 10:53:38 [error] 587287[[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))](https://github.com/coreruleset/coreruleset/issues/[[#587287](https://github.com/coreruleset/coreruleset/issues/#587287)](https://github.com/coreruleset/coreruleset/issues/[#587287](https://github.com/coreruleset/coreruleset/issues/#587287))): *1 [client ::1] ModSecurity: Access denied with code 403 (phase 3). Matched "Operator `Ge' with parameter `4' against variable `TX:OUTBOUND_ANOMALY_SCORE' (Value: `5' ) [file "/usr/share/modsecurity-crs/rules/RESPONSE-959-BLOCKING-EVALUATION.conf"] [line "138"] [id "959101"] [rev ""] [msg "Outbound Anomaly Score Exceeded in phase 3 (Total Score: 5)"] [data ""] [severity "2"] [ver "OWASP_CRS/3.3.1"] [maturity "0"] [accuracy "0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-generic"] [hostname "::1"] [uri "/"] [unique_id "161062161853.669342"] [ref ""], client: ::1, server: _, request: "GET / HTTP/1.1", host: "localhost:8080"

as you can see, there is a log entry in phase:1, but also a line in phase:3...</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">no, perhaps you're right. But the developer wrote he uses the current master state.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">no, perhaps you're right. But the developer wrote he uses the current master state.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:56 UTC</span>

<span style="font-size: 90%;">and he is one of the author of connector :)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:50 UTC</span>

<span style="font-size: 90%;">Oh, oh. Not good.</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:56 UTC</span>

<span style="font-size: 90%;">and he is one of the author of connector :)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:35 UTC</span>

<span style="font-size: 90%;">no, perhaps you're right. But the developer wrote he uses the current master state.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:40:56 UTC</span>

<span style="font-size: 90%;">and he is one of the author of connector :)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:23 UTC</span>

<span style="font-size: 90%;">And that behavior can be reproduced? (-> deny in phase 2, but phase 3 is being executed?)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:42:42 UTC</span>

<span style="font-size: 90%;">yes, it can be</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:03 UTC</span>

<span style="font-size: 90%;">sorry, edited my comment: after phase:1 there is an another rule in phase:3</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:42 UTC</span>

<span style="font-size: 90%;">yes, it can be</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:42:42 UTC</span>

<span style="font-size: 90%;">yes, it can be</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:58 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ got same result</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:43:07 UTC</span>

<span style="font-size: 90%;">yep</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:30 UTC</span>

<span style="font-size: 90%;">Do you also get this behaviour on 3.3.0 (without the early blocking).</span>

**airween** <span style="color: grey; font-size: 90%;">19:43:43 UTC</span>

<span style="font-size: 90%;">I didn't checked that</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:43:59 UTC</span>

<span style="font-size: 90%;">me neither</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:25 UTC</span>

<span style="font-size: 90%;">we can do some tests on 3.3.0</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:21 UTC</span>

<span style="font-size: 90%;">it smells like modsecurity v3 developers configure it always in “self contained” mode and they never fall in this kind of bugs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:35 UTC</span>

<span style="font-size: 90%;">Probably, yes. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">I think we need to know about 3.3.0. If it's there in 3.3.0, then it's just another ModSec3 bug. If it's not there in 3.3.0 and our early blocking kind of provokes ModSec3 to misbehave, then we can not release our blog post in good conscience I think, since it's going to look very ugly to our users. Also since running phase 3 probably means the attacking request has reached the backend, when it ought to have been blocked.</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:50 UTC</span>

<span style="font-size: 90%;">I think we should test it by a "raw" rule-set - 2-3 rules enough. First rule in phase:1 with block, second one in phase:3 also with block (and set a response which will trigger the rule). If we see both rule in log, then it's "independent" :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:30 UTC</span>

<span style="font-size: 90%;">Sounds like a plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:24 UTC</span>

<span style="font-size: 90%;">It's a bit of a pity, @lifeforms is not around, but if this is a CRS induced problem, we can not release the blog post and there is a serious problem for 3.4 too (since it comes with lots of phase:1 rules and early blocking too).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:53 UTC</span>

<span style="font-size: 90%;">For the moment, I suggest you guys perform the tests as proposed by _@airween_ and we hold back the blog post until we know for sure.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:58 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:07 UTC</span>

<span style="font-size: 90%;">lgtm</span>

**airween** <span style="color: grey; font-size: 90%;">19:52:22 UTC</span>

<span style="font-size: 90%;">sure, I'm going to make the rule set, stay tuned :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:31 UTC</span>

<span style="font-size: 90%;">Thank you guys.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:39 UTC</span>

<span style="font-size: 90%;">Are we done with this?</span>

**airween** <span style="color: grey; font-size: 90%;">19:53:45 UTC</span>

<span style="font-size: 90%;">I think yes, we're done</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:23 UTC</span>

<span style="font-size: 90%;">Cool. Then let's move to the issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:43 UTC</span>

<span style="font-size: 90%;">_@airween_ and _@Emile_, did you see that I merged said issue xxx.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:57 UTC</span>

<span style="font-size: 90%;">xxx=1817</span>

**Emile** <span style="color: grey; font-size: 90%;">19:55:08 UTC</span>

<span style="font-size: 90%;">Yep, thanks!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:53 UTC</span>

<span style="font-size: 90%;">So 1864 is a stale issue that was about to be closed by the bot and the original submitter asked on the ML we address it. So I've added it to the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:04 UTC</span>

<span style="font-size: 90%;">It's a simple FP in 930120.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:58:19 UTC</span>

<span style="font-size: 90%;">it's similar to issue 1922</span>

**Emile** <span style="color: grey; font-size: 90%;">19:58:24 UTC</span>

<span style="font-size: 90%;">Hum, We had similar experiences, I had patched our import to remove a few values  "remove": [".profile", ".nsr"]</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:59:09 UTC</span>

<span style="font-size: 90%;">i created a PR that should cover all of these cases.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:59:26 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1978](https://github.com/coreruleset/coreruleset/pull/1978)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:55 UTC</span>

<span style="font-size: 90%;">So 1978 also covers 1864?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:00:02 UTC</span>

<span style="font-size: 90%;">yes</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:00:09 UTC</span>

<span style="font-size: 90%;">it should</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:17 UTC</span>

<span style="font-size: 90%;">Ah, now I see the reference in the issue. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:23 UTC</span>

<span style="font-size: 90%;">So this is taken care of.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:00:30 UTC</span>

<span style="font-size: 90%;">maybe not</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:00:39 UTC</span>

<span style="font-size: 90%;">that PR is a bigger one, it's using Lua..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:56 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:00:56 UTC</span>

<span style="font-size: 90%;">not sure if you will like it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:20 UTC</span>

<span style="font-size: 90%;">On a purely conceptual level, I think it's a beautiful PR...</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:36 UTC</span>

<span style="font-size: 90%;">after a quick view: with two simple rules I can't reproduce the blocking early behavior</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:57 UTC</span>

<span style="font-size: 90%;">in that case, after the firs deny the engine returns 403</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:09 UTC</span>

<span style="font-size: 90%;">in phase:1</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:22 UTC</span>

<span style="font-size: 90%;">I need more check</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:18 UTC</span>

<span style="font-size: 90%;">Thank you for the status updare _@airween_.</span>

**Emile** <span style="color: grey; font-size: 90%;">20:04:47 UTC</span>

<span style="font-size: 90%;">Hum, Lua would prevent me from importing the patch in our third party runtime, but that shouldn’t be a blocker for the project</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:05:07 UTC</span>

<span style="font-size: 90%;">Why?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:05:20 UTC</span>

<span style="font-size: 90%;">Because my runtime doesn’t have a lua interpreter :smile:</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:05:41 UTC</span>

<span style="font-size: 90%;">Not possible to recompile modsec with Lua support?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:06:29 UTC</span>

<span style="font-size: 90%;">We’re not using modsec, we’re running it in a very specialized context so we reimplemented an engine to run CRS rules</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:06:38 UTC</span>

<span style="font-size: 90%;">ah</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:06:43 UTC</span>

<span style="font-size: 90%;">interesting</span>

**Emile** <span style="color: grey; font-size: 90%;">20:07:01 UTC</span>

<span style="font-size: 90%;">Simpler, faster, can ignore many hard problems modsec had to contend with</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:58 UTC</span>

<span style="font-size: 90%;">_@azurIt_: There are several issues with starting to use Lua in CRS. One of them is that alternative implementations of ModSec in order to run CRS aimed for a minimal code base and skipped the Lua integration. By starting to use Lua, we would annoy those alternatives, stick closer to the official ModSecurity, when we are actually welcoming alternative implementations. So it's a difficult call.</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:48 UTC</span>

<span style="font-size: 90%;">btw: using Lua will drops the independence of rule set...</span>

**Emile** <span style="color: grey; font-size: 90%;">20:09:09 UTC</span>

<span style="font-size: 90%;">I have a lower quality patch in mind. I would need to check with our false positives to see if it works but we could get away with a regex</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:34 UTC</span>

<span style="font-size: 90%;">That is 1864 _@Emile_?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:10:01 UTC</span>

<span style="font-size: 90%;">While i was developing this PR i had a solution without Lua but it was working only in modsec3 (and i didn't tested it much).</span>

**Emile** <span style="color: grey; font-size: 90%;">20:10:07 UTC</span>

<span style="font-size: 90%;">For 1864, to be an alternative for 1978.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:16 UTC</span>

<span style="font-size: 90%;">Thank you Emile.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:33 UTC</span>

<span style="font-size: 90%;">I think with 2 options, we are more than good for 1864.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:00 UTC</span>

<span style="font-size: 90%;">_@azurIt_: A regex solution that would not work in ModSec2? I'm curious. If you can dig it up, please share with me via DM.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:20 UTC</span>

<span style="font-size: 90%;">OK. Let's move on. This is supposed to be a fast meeting, but I am always dragging things out.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:45 UTC</span>

<span style="font-size: 90%;">1969 is one hell of a Nextcloud FP report.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:53 UTC</span>

<span style="font-size: 90%;">_@azurIt_: You self-assigned this already.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:08 UTC</span>

<span style="font-size: 90%;">Is that still OK with you, or do you have too much to take care of?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:12:27 UTC</span>

<span style="font-size: 90%;">It's ok but i wanted to discuss one thing.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:13:53 UTC</span>

<span style="font-size: 90%;">Problem in that issue is we are blocking YUM package manager because it's using python urlgrabber library and so it is identifying itself as (using User-Agent): ... urlgrabber/... yum/... ...</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:14:16 UTC</span>

<span style="font-size: 90%;">this is matched by rule checking for web crawlers, pattern 'grabber'</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:14:42 UTC</span>

<span style="font-size: 90%;">i think the only way here is to whitelist something but i'm not sure - we probably don'</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:14:57 UTC</span>

<span style="font-size: 90%;">t want to whotelist 'urlgrabber' as that library can be used by other crawlers</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:08 UTC</span>

<span style="font-size: 90%;">There are a few rules, where we whitelist via a chain right in the rule.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:15:09 UTC</span>

<span style="font-size: 90%;">but whitelisting 'yum' seems to be too general</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:15:28 UTC</span>

<span style="font-size: 90%;">it's a short word</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:45 UTC</span>

<span style="font-size: 90%;">920310 is a rule where we whitelist.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:56 UTC</span>

<span style="font-size: 90%;">It depends a bit where that is. In the UA?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:16:01 UTC</span>

<span style="font-size: 90%;">yes</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:16:19 UTC</span>

<span style="font-size: 90%;">User-Agent: urlgrabber/3.10 yum/3.4.3</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:16:44 UTC</span>

<span style="font-size: 90%;">would it be ok to whitelist 'yum/' ?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:16:50 UTC</span>

<span style="font-size: 90%;">hmmm</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:59 UTC</span>

<span style="font-size: 90%;">I think whitelisting grabber followed by yum would be totally OK in this context, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:07 UTC</span>

<span style="font-size: 90%;">It's exactly what 920310 does.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:17:12 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:33 UTC</span>

<span style="font-size: 90%;">Or do you have any other headers to chain as well?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:44 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ What do you think?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:17:51 UTC</span>

<span style="font-size: 90%;">No</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:59 UTC</span>

<span style="font-size: 90%;">no I agree with your last sentence</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:15 UTC</span>

<span style="font-size: 90%;">maybe is better to whitelist the whole UA</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:18:23 UTC</span>

<span style="font-size: 90%;">ok, all clear</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:38 UTC</span>

<span style="font-size: 90%;">How about the version number? We do not want to whitelist 3.10, or do we?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:19:12 UTC</span>

<span style="font-size: 90%;">I'm not very familiar with YUM so i don't know if it was using also other versions of that library.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:19:28 UTC</span>

<span style="font-size: 90%;">what if something like urlgrabber/[0-9.]+ yum/[0-9.]+ ?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:34 UTC</span>

<span style="font-size: 90%;">If not today, then tomorrow, so I think the version should be ignored.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:19:43 UTC</span>

<span style="font-size: 90%;">yes i agree</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:51 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ That's what I had in mind. Given the construction of the rule, the additional regex does not matter.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:25 UTC</span>

<span style="font-size: 90%;">Which brings us to 1979.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:20:40 UTC</span>

<span style="font-size: 90%;">There's a lot of discussion.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:57 UTC</span>

<span style="font-size: 90%;">_@azurIt_ asks for a different way of setting PL for rules. Namely a way that allows him to read the PL from within lua.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:03 UTC</span>

<span style="font-size: 90%;">It's a feature request.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:21:36 UTC</span>

<span style="font-size: 90%;">It turns out that my original idea is not ok so i would just ask how to get paranoia level into Lua.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:21:38 UTC</span>

<span style="font-size: 90%;">BUT</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:21:55 UTC</span>

<span style="font-size: 90%;">if we are not going to use Lua, we can skip this feature request..</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:22:54 UTC</span>

<span style="font-size: 90%;">I didn't know we are targeting also outside modsecurity.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:24:27 UTC</span>

<span style="font-size: 90%;">it’s a pity IMO, but I understand the compatibility problems</span>

**Emile** <span style="color: grey; font-size: 90%;">20:25:53 UTC</span>

<span style="font-size: 90%;">Most (all?) outside runtimes are proprietary though, so modsec is still a key target. But the relationship between the two projects is Complicated™, so when those outside runtime are communicating, they’re heard :slightly_smiling_face:</span>

**Emile** <span style="color: grey; font-size: 90%;">20:27:35 UTC</span>

<span style="font-size: 90%;">afaik, CRS is the base ruleset for at least Cloudflare, GCP, AWS, us (Sqreen), and I’d wager money none of them use ModSec</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:08 UTC</span>

<span style="font-size: 90%;">And a few more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:01 UTC</span>

<span style="font-size: 90%;">But nevermind. I'd like to talk a bit more of the feature request. The 2nd argument in favor is the redundancy that we have by setting the PL via the tag, but also via the position of the rule withing the config file.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:37 UTC</span>

<span style="font-size: 90%;">_@azurIt_ would like to simplify / automate this. And I think that would be sweet, if it can be kept simple and readable.</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:03 UTC</span>

<span style="font-size: 90%;">in the not so far future, I can imagine that we have a site, where customer can "build" an own rule set with help of a very simple form. Then he/she can choose the rules which needs Lua...</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:32:34 UTC</span>

<span style="font-size: 90%;">For my alternative to 1978, I was thinking of having both next to one another, with lua picked up if possible and my solution as a fallback</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:14 UTC</span>

<span style="font-size: 90%;">but the base of the rule set is "standard" CRS</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:32:47 UTC</span>

<span style="font-size: 90%;">_@dune73_ i think it won't be possible, at least not in tags, as modsecurity is dropping macro usage in tags from version 3.1</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:04 UTC</span>

<span style="font-size: 90%;">_@Emile_: If you execute the SecRuleScript Lua thing conditionally, it still has to be loaded by the engine during startup and I am not sure the engine allows for Script if it does not know about Script, if you know what I mean.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:35 UTC</span>

<span style="font-size: 90%;">It's likely an engine would refuse to start if a rule refers to a lua script if it does not come with lua support.</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:36:35 UTC</span>

<span style="font-size: 90%;">I mean, yeah but adding a tag to ignore is easier than adding a lua VM :slightly_smiling_face: And considering the format was never formally standardized, you get to set the standard to third party implementation</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:36:52 UTC</span>

<span style="font-size: 90%;">Especially since you’re starting to provide a rule parser</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:37:16 UTC</span>

<span style="font-size: 90%;">Can you show your solution?</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:39:09 UTC</span>

<span style="font-size: 90%;">It wouldn’t have been as good as yours, meant to replace %{file} in the patterns in your PR by [\w\.]+, then the /, ^ and $ you suggested</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:40:04 UTC</span>

<span style="font-size: 90%;">Something like (^[\w\.]+$)|(^/[\w\.]+[\W])|…</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:41:25 UTC</span>

<span style="font-size: 90%;">Similar to my other solution which wasn't working in modsec2, only v3:</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:41:37 UTC</span>

<span style="font-size: 90%;">SecRule ARGS "@pmFromFile lfi-os-files.data" \
    ....
    setvar:'tx.rx_pattern=%{tx.rx_pattern}|^%{tx.0}$|^/%{tx.0}|^%{tx.0}/|/%{tx.0}$',\
    chain"
    SecRule MATCHED_VARS "@rx (?:%{tx.rx_pattern})" \
        "setvar:'tx.lfi_score=+%{tx.critical_anomaly_score}',\ 
        setvar:'tx.anomaly_score_pl1=+%{tx.critical_anomaly_score}'"</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:42:18 UTC</span>

<span style="font-size: 90%;">actually, you’re right, that would be better for CRS</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:42:20 UTC</span>

<span style="font-size: 90%;">modsec2 is escaping macros when used with @rx so final pattern wasn't usable</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:42:40 UTC</span>

<span style="font-size: 90%;">but modsec3 is not escaping it so it should work</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:43:14 UTC</span>

<span style="font-size: 90%;">(I got lazy and didn’t implement variable support for now in our engine so %{tx.rx_pattern} wouldn’t work for us but again, that’s my problem, not CRS’)</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:43:58 UTC</span>

<span style="font-size: 90%;">I don’t think it was accidental, creating a regex state machine multiple time per request is… not fast</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:16 UTC</span>

<span style="font-size: 90%;">I am not seeing much comments on the naked idea of 1979, so let's move on to 1950.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:32 UTC</span>

<span style="font-size: 90%;">_@airween_, would you mind explaining it? I think you also have a question or two for us.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:35:33 UTC</span>

<span style="font-size: 90%;">modsec is ignoring rules with lua if lua support is not compiled</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:35:48 UTC</span>

<span style="font-size: 90%;">well, at least it should, i read that somewhere in the docs</span>

**airween** <span style="color: grey; font-size: 90%;">20:36:33 UTC</span>

<span style="font-size: 90%;">yeah, in my last comment, you can see that I've removed the / in all of three part from regexes</span>

**airween** <span style="color: grey; font-size: 90%;">20:37:30 UTC</span>

<span style="font-size: 90%;">it's just a suggestion, would be fine to review it by many eyes as possible</span>

**airween** <span style="color: grey; font-size: 90%;">20:38:25 UTC</span>

<span style="font-size: 90%;">and there is the [regex101](https://regex101.com/r/CR8G7J/1) test case, which uses the regression tests cases</span>

**airween** <span style="color: grey; font-size: 90%;">20:38:58 UTC</span>

<span style="font-size: 90%;">if there isn't any remarks, I'm going to make a PR</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:25 UTC</span>

<span style="font-size: 90%;">_@azurIt_: Would you mind checking that on ModSec2 and ModSec3? It would help with a decision.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:40:08 UTC</span>

<span style="font-size: 90%;">_@dune73_ ok</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:54 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:24 UTC</span>

<span style="font-size: 90%;">_@airween_: What are we losing by removing the / from the regex?</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:15 UTC</span>

<span style="font-size: 90%;">I think nothing to lose with that - at least based on regression tests. All test results are same</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:37 UTC</span>

<span style="font-size: 90%;">but that's why I sent a proposal</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:38 UTC</span>

<span style="font-size: 90%;">Yes, but I mean the slash was there for a reason, was not it?</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:02 UTC</span>

<span style="font-size: 90%;">yes, perhaps, but I don't know the reason</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:48 UTC</span>

<span style="font-size: 90%;">The comments point to PHP comments, if I get this right:
# - (/**/system)(ls/**/);</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:54 UTC</span>

<span style="font-size: 90%;">but as _@azurIt_ wrote there, the / is allowed in cookie</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:36 UTC</span>

<span style="font-size: 90%;">Yes, absolutely. It is allowed, that's why we get FPs.</span>

**airween** <span style="color: grey; font-size: 90%;">20:46:07 UTC</span>

<span style="font-size: 90%;">but as I know that rule uses replaceComments</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:55 UTC</span>

<span style="font-size: 90%;">Regression tests 933210-8 and -12 refer to the comments in question. So if we still cover those without the slash, then I think we are good to go. Or are there other opinions?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:47:19 UTC</span>

<span style="font-size: 90%;">hum, 933210 is a rule we had to blacklist due to FPs :thinking_face:
I wrote down (bla) (bla) as a trigger exemple</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:53:52 UTC</span>

<span style="font-size: 90%;">it’s still a valid PHP syntax :joy:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:22 UTC</span>

<span style="font-size: 90%;">ohhh... :open_mouth:</span>

**Emile** <span style="color: grey; font-size: 90%;">20:47:39 UTC</span>

<span style="font-size: 90%;">Hadn’t investigated further though</span>

**airween** <span style="color: grey; font-size: 90%;">20:47:44 UTC</span>

<span style="font-size: 90%;">as I remember, I ran the regression tests after this modification, and all test were passed</span>

**airween** <span style="color: grey; font-size: 90%;">20:48:21 UTC</span>

<span style="font-size: 90%;">but have to check again - I'll send a PR in next few days, if it is okay, and we can see</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:09 UTC</span>

<span style="font-size: 90%;">Yes, let's do that. We can also ask Federico to have a look. He is usually very critical with regex changes. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:49:21 UTC</span>

<span style="font-size: 90%;">sure, absolutely! :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:34 UTC</span>

<span style="font-size: 90%;">_@Emile_: It's like you have seen every possible FP for all our rules, don't you?</span>

**Emile** <span style="color: grey; font-size: 90%;">20:50:00 UTC</span>

<span style="font-size: 90%;">ahahah, we get a lot of traffic :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:11 UTC</span>

<span style="font-size: 90%;">Apparently, apparently. :slightly_smiling_face:</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:51:03 UTC</span>

<span style="font-size: 90%;">Honnestly, I stopped reporting everything I found because I was going to flood the project and it’s not helpful</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:51:29 UTC</span>

<span style="font-size: 90%;">However, I would gladly share the rules we flagged and. the kind of stuff we find as a reference :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:26 UTC</span>

<span style="font-size: 90%;">So let's look into 1949!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:58 UTC</span>

<span style="font-size: 90%;">These are exclusion rules candidates to shift into phase 1. 2 of them were confirmed by lifeforms, 3 are still undecided.</span>

**airween** <span style="color: grey; font-size: 90%;">20:52:02 UTC</span>

<span style="font-size: 90%;">it's just a small collection of few rules, which can move to lower phase</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:14 UTC</span>

<span style="font-size: 90%;">Anybody wants to have a 2nd look to confirm _@airween_?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:53:52 UTC</span>

<span style="font-size: 90%;">it’s still a valid PHP syntax :joy:</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:53:52 UTC</span>

<span style="font-size: 90%;">it’s still a valid PHP syntax :joy:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:55:22 UTC</span>

<span style="font-size: 90%;">ohhh... :open_mouth:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:54:43 UTC</span>

<span style="font-size: 90%;">PHP is a mess.</span>

**airween** <span style="color: grey; font-size: 90%;">20:55:47 UTC</span>

<span style="font-size: 90%;">so it means we have to keep the /...</span>

↳ **Emile** <span style="color: grey; font-size: 90%;">20:56:38 UTC</span>

<span style="font-size: 90%;">/ is not present in this payload… :grimacing:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:57:22 UTC</span>

<span style="font-size: 90%;">yes, I see :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:05 UTC</span>

<span style="font-size: 90%;">Not sure I get your interpretation, _@airween_. Care to share your reasoning=</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:08 UTC</span>

<span style="font-size: 90%;">?</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:12 UTC</span>

<span style="font-size: 90%;">eg

php> const bla = "system";
php> (bla)(/bin/ls)</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:35 UTC</span>

<span style="font-size: 90%;">or em I wrong?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:59:39 UTC</span>

<span style="font-size: 90%;">uhm no in that case it’s not possible without using quotes</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:59:50 UTC</span>

<span style="font-size: 90%;"></span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:00:28 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">21:00:51 UTC</span>

<span style="font-size: 90%;">For the record: I am self-assigning 1949 and will look into the rules in question.</span>

**airween** <span style="color: grey; font-size: 90%;">21:03:18 UTC</span>

<span style="font-size: 90%;">well, if the string must be as escaped by " or ', then we can remove the / - the escape characters are still in the regex. But also have to review by somebody</span>

**airween** <span style="color: grey; font-size: 90%;">21:04:17 UTC</span>

<span style="font-size: 90%;">this will also triggered:
(bla)("ls")</span>

**airween** <span style="color: grey; font-size: 90%;">21:05:03 UTC</span>

<span style="font-size: 90%;">and / doesn't count here</span>

**airween** <span style="color: grey; font-size: 90%;">21:05:06 UTC</span>

<span style="font-size: 90%;">any thoughts?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:20 UTC</span>

<span style="font-size: 90%;">Get it.</span>

**airween** <span style="color: grey; font-size: 90%;">21:05:40 UTC</span>

<span style="font-size: 90%;">okay, then as I wrote in next few days I'll send the PR</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:47 UTC</span>

<span style="font-size: 90%;">Yes, I think we can remove the slash now after this conversation.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:05:51 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ Do you agree?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:06:53 UTC</span>

<span style="font-size: 90%;">yep, ok for me! thanks _@airween_</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:20 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:50 UTC</span>

<span style="font-size: 90%;">Given we are only so few of us and it's getting late, I suggest we finish the meeting here and postpone the remaining issue in the agenda.</span>

**airween** <span style="color: grey; font-size: 90%;">21:10:50 UTC</span>

<span style="font-size: 90%;">there is only one issue left, or what else?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:14:27 UTC</span>

<span style="font-size: 90%;">In the agenda, yes.</span>

**airween** <span style="color: grey; font-size: 90%;">21:15:20 UTC</span>

<span style="font-size: 90%;">okay, then we are finished for today?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:34 UTC</span>

<span style="font-size: 90%;">I'd say so. Thank you all for joining.</span>

**airween** <span style="color: grey; font-size: 90%;">21:16:54 UTC</span>

<span style="font-size: 90%;">good night!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:17:06 UTC</span>

<span style="font-size: 90%;">thanks! good night!</span>

**Emile** <span style="color: grey; font-size: 90%;">21:17:21 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**azurIt** <span style="color: grey; font-size: 90%;">21:17:25 UTC</span>

<span style="font-size: 90%;">good night</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:06 UTC</span>

<span style="font-size: 90%;">Good night.</span>

