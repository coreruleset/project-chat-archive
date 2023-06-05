### Mon, Jun 5th, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's Monday and time for our CRS chat. Who is around?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:56 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:32:25 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**airween** <span style="color: grey; font-size: 90%;">18:32:36 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:46 UTC</span>

<span style="font-size: 90%;">Finally, I get to attend the first meeting of the month. :slightly_smiling_face:</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:51 UTC</span>

<span style="font-size: 90%;">heeeeyyyyhoooooooo :partyparrot:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:33:04 UTC</span>

<span style="font-size: 90%;">hey!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:33:12 UTC</span>

<span style="font-size: 90%;">Hey</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:33:13 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:21 UTC</span>

<span style="font-size: 90%;">Hi there, so good to see you all!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:33:27 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:12 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:07 UTC</span>

<span style="font-size: 90%;">We have a very full agenda. You can find it at [https://github.com/coreruleset/coreruleset/issues/3221](https://github.com/coreruleset/coreruleset/issues/3221)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:01 UTC</span>

<span style="font-size: 90%;">_@xanadu_ and I have overwritten each other's changes to the agenda several times. I hope it did not happen with other items as well. We have added the problem under project discussion. We need to find a way around this, since even reloading and being extra careful does not always help.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:03 UTC</span>

<span style="font-size: 90%;">Outside CRS dev, the biggest news is probably the release of Coraza v3. A long awaited great release.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:10 UTC</span>

<span style="font-size: 90%;">Congratulations on the Coraza team!</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:40:17 UTC</span>

<span style="font-size: 90%;">Thanks for the support from the CRS team. You are also part of this.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:43:02 UTC</span>

<span style="font-size: 90%;">Seriously, all the support questions we made both in Slack, GH, backchannel and offline. It was a joint effort.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:47 UTC</span>

<span style="font-size: 90%;">They also got serious with the libCoraza idea on NGINX, asking for contributors to join with this goal. We have re-scheduled this topic on our agenda too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:35 UTC</span>

<span style="font-size: 90%;">Looking through our various subprojects, I have share the name of the said silver sponsor who is upgrading into the dev channel.</span>

**JC** <span style="color: grey; font-size: 90%;">18:40:17 UTC</span>

<span style="font-size: 90%;">Thanks for the support from the CRS team. You are also part of this.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:40:17 UTC</span>

<span style="font-size: 90%;">Thanks for the support from the CRS team. You are also part of this.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:43:02 UTC</span>

<span style="font-size: 90%;">Seriously, all the support questions we made both in Slack, GH, backchannel and offline. It was a joint effort.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:35 UTC</span>

<span style="font-size: 90%;">We have a PR that we need to discuss briefly: [#3218](https://github.com/coreruleset/coreruleset/issues/#3218). It's about official support for HTTP/3 in the crs config.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:07 UTC</span>

<span style="font-size: 90%;">_@xanadu_ could you explain the problem / situation and what we need to decide?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:10 UTC</span>

<span style="font-size: 90%;">Whether to accept both HTTP/3 and HTTP/3.0 as valid protocol strings, I think that's the current question.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:33 UTC</span>

<span style="font-size: 90%;">Why not?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:43:41 UTC</span>

<span style="font-size: 90%;">My thinking was that if the RFC says "X" then maybe we should be less permissive and only accept option "X", maybe in case there's an exploit in the future?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:44:03 UTC</span>

<span style="font-size: 90%;">But I'm confused at this point, so I don't know anymore :shrug:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:42:48 UTC</span>

<span style="font-size: 90%;">Incidentally, I know that golang http/net requires the minor version</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:05 UTC</span>

<span style="font-size: 90%;">HAProxy too, it gets interpreted as 3.0</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:34 UTC</span>

<span style="font-size: 90%;">Is there anything wrong with accepting both?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:41 UTC</span>

<span style="font-size: 90%;">How do we handle that for HTTP 1 and 2?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:05 UTC</span>

<span style="font-size: 90%;">We carry both in crs-setup.conf</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:06 UTC</span>

<span style="font-size: 90%;">tx.allowed_http_versions=HTTP/1.0 HTTP/1.1 HTTP/2 HTTP/2.0</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:15 UTC</span>

<span style="font-size: 90%;">So it's inconsistent already.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;">I think HTTP/2 is only there for legacy compatibility reasons, I think.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:15 UTC</span>

<span style="font-size: 90%;">Well, we all know how RFC's aren't the real world. So I'd be careful with being too limiting at PL 1.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:01 UTC</span>

<span style="font-size: 90%;">I agree. We should not punish users if their UA is a bit relaxed in this regard.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:57 UTC</span>

<span style="font-size: 90%;">Agreed?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:31 UTC</span>

<span style="font-size: 90%;">Cool, thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:40 UTC</span>

<span style="font-size: 90%;">Anything else for subprojects?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:48 UTC</span>

<span style="font-size: 90%;">Nope :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:45 UTC</span>

<span style="font-size: 90%;">Good, then let's look at the dev retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:10 UTC</span>

<span style="font-size: 90%;">We're thinking into spending Sat Nov 4 - Sat Nov 11 around Budapest in Hungary. _@fzipitria_ is busy the week before. What do you all think?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">OWASP Appsec DC is the week before [https://dc.globalappsec.org/](https://dc.globalappsec.org/), maybe too close?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Budapest??? :smile:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Budapest is A-WE-SOME btw. Been there 5 times.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">Yeah, maybe Sat 11-18?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:57:01 UTC</span>

<span style="font-size: 90%;">I can do earlier also</span>

**JC** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">OWASP Appsec DC is the week before [https://dc.globalappsec.org/](https://dc.globalappsec.org/), maybe too close?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">OWASP Appsec DC is the week before [https://dc.globalappsec.org/](https://dc.globalappsec.org/), maybe too close?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Budapest??? :smile:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Budapest is A-WE-SOME btw. Been there 5 times.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">Yeah, maybe Sat 11-18?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:57:01 UTC</span>

<span style="font-size: 90%;">I can do earlier also</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:57 UTC</span>

<span style="font-size: 90%;">We're usually not attending that conference. At least not with a real delegation.</span>

**airween** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Budapest??? :smile:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">OWASP Appsec DC is the week before [https://dc.globalappsec.org/](https://dc.globalappsec.org/), maybe too close?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Budapest??? :smile:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Budapest is A-WE-SOME btw. Been there 5 times.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">Yeah, maybe Sat 11-18?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:57:01 UTC</span>

<span style="font-size: 90%;">I can do earlier also</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">a lot of pálinka that week? :clinking_glasses:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:34 UTC</span>

<span style="font-size: 90%;">mmmmmm</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">especially from walnut? :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:56:34 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">especially from walnut? :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">especially from walnut? :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:56:34 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:26 UTC</span>

<span style="font-size: 90%;">_@airween_ You are no longer interested to have us in Hungary? I thought it was more or less postponed from 2022 to 2023.</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:47 UTC</span>

<span style="font-size: 90%;">You are no longer interested to have us in Hungary? - no-no, I'm definitely interesting of course!!!</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:56 UTC</span>

<span style="font-size: 90%;">just wondering a bit :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:17 UTC</span>

<span style="font-size: 90%;">it's a surprise - but a nice surprise</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:50 UTC</span>

<span style="font-size: 90%;">All the better then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:12 UTC</span>

<span style="font-size: 90%;">So let's consider the date settled. We can start to announce it and hopefully we will have many participants.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:01:05 UTC</span>

<span style="font-size: 90%;">Sorry.... which date?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:02:22 UTC</span>

<span style="font-size: 90%;">I thought it was a proposal.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:03:05 UTC</span>

<span style="font-size: 90%;">_@dune73_ here :point_up:</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:30 UTC</span>

<span style="font-size: 90%;">Good evening, sorry I’m late, I am sick and slept through the alarm.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:16 UTC</span>

<span style="font-size: 90%;">Welcome @walter! Good to see you.</span>

**JC** <span style="color: grey; font-size: 90%;">19:01:36 UTC</span>

<span style="font-size: 90%;">:point_up_2:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">OWASP Appsec DC is the week before [https://dc.globalappsec.org/](https://dc.globalappsec.org/), maybe too close?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Budapest??? :smile:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Budapest is A-WE-SOME btw. Been there 5 times.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">Yeah, maybe Sat 11-18?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:57:01 UTC</span>

<span style="font-size: 90%;">I can do earlier also</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:57:53 UTC</span>

<span style="font-size: 90%;">But 1-3 Nov I'm booked</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:58:28 UTC</span>

<span style="font-size: 90%;">And considering that it takes me 16-18 hours to get anywhere, maybe Nov 4 is a bit tight</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:01:36 UTC</span>

<span style="font-size: 90%;">:point_up_2:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:48 UTC</span>

<span style="font-size: 90%;">Next up: _@fzipitria_ suggest to make the move and erase the ModSecurity from our name. It is obvious the original name does not do Coraza and commercial re-implementations justice and I hope we can make this step one day. They question is whether this is a good moment - or do we still rely on the ModSecurity too a strong degree.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:52 UTC</span>

<span style="font-size: 90%;">What do you all think?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:25 UTC</span>

<span style="font-size: 90%;">ModSecurity is still far more recognised than CRS, unfortunately. It seems foolish to abandon the recognition of ModSec at this point in time.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:03:26 UTC</span>

<span style="font-size: 90%;">difficult question…</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:37 UTC</span>

<span style="font-size: 90%;">Maybe a question to revisit in a year or so.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:42 UTC</span>

<span style="font-size: 90%;">Why?</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:43 UTC</span>

<span style="font-size: 90%;">I agree with _@xanadu_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:04 UTC</span>

<span style="font-size: 90%;">Every time there is a problem with modsecurity, someone thinks it is the CRS</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:04:09 UTC</span>

<span style="font-size: 90%;">agree with _@fzipitria_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:11 UTC</span>

<span style="font-size: 90%;">There is a lot of confusion</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:17 UTC</span>

<span style="font-size: 90%;">Nobody knows for certain</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:18 UTC</span>

<span style="font-size: 90%;">If we want to drop ModSec then let's push CRS more heavily and try to get more recognition for CRS on its own.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:22 UTC</span>

<span style="font-size: 90%;">The time isn't right yet.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:23 UTC</span>

<span style="font-size: 90%;">So let's decouple now.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:26 UTC</span>

<span style="font-size: 90%;">(IMO)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:32 UTC</span>

<span style="font-size: 90%;">It's going to take a long time to to this</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:42 UTC</span>

<span style="font-size: 90%;">I looked through the tutorials published last month. All of them explained CRS installation, but only one cared to mention CRS, they all talked of ModSecurity ...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:58 UTC</span>

<span style="font-size: 90%;">Plenty of Commercial cloud providers have their own OWASP CRS reimplementation</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:06 UTC</span>

<span style="font-size: 90%;">And no, they don't mention modsecurity</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:19 UTC</span>

<span style="font-size: 90%;">Good point _@fzipitria_.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:05:24 UTC</span>

<span style="font-size: 90%;">Maybe we should comment on such blog posts and try to push the name of CRS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:38 UTC</span>

<span style="font-size: 90%;">That's exactly what I'm pushing for</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:41 UTC</span>

<span style="font-size: 90%;">Let's move on</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:05:51 UTC</span>

<span style="font-size: 90%;">Personally I always prefer functional names that describe the product eg. WAF Core Rule Set, rather than named after a product.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:52 UTC</span>

<span style="font-size: 90%;">I tried doing that _@xanadu_, but it's troublesome.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:06:01 UTC</span>

<span style="font-size: 90%;">and moreover I've customers that say "the rules from owasp" it's not modsecurity the only problem in the name :joy:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:01 UTC</span>

<span style="font-size: 90%;">How much impact would the change have on DevOnDuty?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:20 UTC</span>

<span style="font-size: 90%;">Not much, I guess. I'd stick with the keywords.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:30 UTC</span>

<span style="font-size: 90%;">We can lurk around and decide</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:34 UTC</span>

<span style="font-size: 90%;">Unless we pick up _@Paul Beckett_’s proposal to add WAF to the name.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:45 UTC</span>

<span style="font-size: 90%;">But this change will take time to process</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:02 UTC</span>

<span style="font-size: 90%;">So my proposal is to move now with this, and in one year we will. be in better shape</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:08 UTC</span>

<span style="font-size: 90%;">I think if we do not take the decision to shift tonight, then we should come up with a plan what we can do as a project to make the world ready for the shift.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:22 UTC</span>

<span style="font-size: 90%;">I mean...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:26 UTC</span>

<span style="font-size: 90%;">OWASP changed the name</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:26 UTC</span>

<span style="font-size: 90%;">Then yes, maybe in 6 month or a year.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:33 UTC</span>

<span style="font-size: 90%;">Can't we do it?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:07:46 UTC</span>

<span style="font-size: 90%;">but i must agree. i met already a lot of ppl that think CRS and Modsecurity is the same.
Even some co-workers in my company think that… :sweat:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:50 UTC</span>

<span style="font-size: 90%;">We can, but the name shift of OWASP was minimal.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:52 UTC</span>

<span style="font-size: 90%;">In a year modsecurity is dead</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:09:02 UTC</span>

<span style="font-size: 90%;">I would say it's sleeping. But we have to wait July of 2024.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:03 UTC</span>

<span style="font-size: 90%;">The change would mainly affect newcomers, right? So I don't really see a big issue...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:08 UTC</span>

<span style="font-size: 90%;">Are we waiting for a dead project?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:32 UTC</span>

<span style="font-size: 90%;">No, I think the name change would affect us, since people would stop reading stuff about CRS without the keyword ModSecurity.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:47 UTC</span>

<span style="font-size: 90%;">I don't think so</span>

**JC** <span style="color: grey; font-size: 90%;">19:09:01 UTC</span>

<span style="font-size: 90%;">As an outsider, I think CRS 4.0 might not have same impact if it still associated to a EOL project. It feels contradictory you release a new thing that “is part” of something that is EOL whereas decoupling giving the sense of being alive and own</span>

**airween** <span style="color: grey; font-size: 90%;">19:09:02 UTC</span>

<span style="font-size: 90%;">I would say it's sleeping. But we have to wait July of 2024.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:09:02 UTC</span>

<span style="font-size: 90%;">I would say it's sleeping. But we have to wait July of 2024.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:09:19 UTC</span>

<span style="font-size: 90%;">Modsecurity is a big keyword….</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:24 UTC</span>

<span style="font-size: 90%;">Does people using CRS in cloud providers look for modsecurity?</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:43 UTC</span>

<span style="font-size: 90%;">probably not</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:45 UTC</span>

<span style="font-size: 90%;">I have customers who worked with me for >10 years and they still do not use CRS, but ModSecurity. Namely management. It's a name that sticks with them, CRS did not.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:09:53 UTC</span>

<span style="font-size: 90%;">From a keyword perspective, WAF would probably get more hits.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:07 UTC</span>

<span style="font-size: 90%;">But we cannot think about your personal customers</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:13 UTC</span>

<span style="font-size: 90%;">This is about the project</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:21 UTC</span>

<span style="font-size: 90%;">"OWASP WAF Core Rule Set" doesn't sound half bad...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:36 UTC</span>

<span style="font-size: 90%;">Please everyone take their vendors hats off for a second</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:46 UTC</span>

<span style="font-size: 90%;">And think about the project</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:56 UTC</span>

<span style="font-size: 90%;">What do We want?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:57 UTC</span>

<span style="font-size: 90%;">I do not care about my customers in this regard. I am using it as an example that year-long exposure to CRS did not erase the name ModSecurity. That's why. The brand is very strong. CRS as a brand is not.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:08 UTC</span>

<span style="font-size: 90%;">Thinking about the project, ModSecurity is well known, though. That is thinking about the project.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:09 UTC</span>

<span style="font-size: 90%;">Then let's push it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:20 UTC</span>

<span style="font-size: 90%;">Let's push for the brand</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:31 UTC</span>

<span style="font-size: 90%;">And it does not matter wether the project is EOL or whatever. It means attention and giving up attention should not be taken lightly.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:36 UTC</span>

<span style="font-size: 90%;">If we start now, in one year there will be something</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:11:43 UTC</span>

<span style="font-size: 90%;">I think that soon or later we'll need to remove the engine name from project name</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:01 UTC</span>

<span style="font-size: 90%;">Sooner or later yes. And I think we should start to come up with a plan.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:02 UTC</span>

<span style="font-size: 90%;">The sooner the better. Because we all know that changes take time</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:11 UTC</span>

<span style="font-size: 90%;">We can push our own brand without a rename. Push first, rename later.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:14 UTC</span>

<span style="font-size: 90%;">I agree that "CRS" isn't very strong. The term is too generic. But coupling it with "WAF" (or something similar) could make it work</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:13:21 UTC</span>

<span style="font-size: 90%;">I agree that "CRS" isn't very strong. - why? I think that's a really popular and well-known</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:13:45 UTC</span>

<span style="font-size: 90%;">Just for newcomers.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:33 UTC</span>

<span style="font-size: 90%;">It thought it might happen naturally, but honestly I am surprised by the strength of the ModSec brand.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:40 UTC</span>

<span style="font-size: 90%;">Where?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:49 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:19 UTC</span>

<span style="font-size: 90%;">Random people hitting dev-on-duty. People approaching me with questions. Random integrators writing tutorials ...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:41 UTC</span>

<span style="font-size: 90%;">We start saying we are CRS then</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:44 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**JC** <span style="color: grey; font-size: 90%;">19:14:09 UTC</span>

<span style="font-size: 90%;">Just a side note: In 2025 Compliance requirements PCI DSS 4 will look for a WAF and Modsec won’t be there, CRS will.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:17 UTC</span>

<span style="font-size: 90%;">It is about the message we send to the community</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:25 UTC</span>

<span style="font-size: 90%;">We are bigger than modsec, IMHO</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:15:11 UTC</span>

<span style="font-size: 90%;">you are right I guess but may be it's just a temporary state...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:41 UTC</span>

<span style="font-size: 90%;">I do this all the time with a clear concept and plan behind it. See how our logo does not carry the ModSec in most uses. We emphasize CRS very much, but ModSec does not go away by itself, so maybe we need to up the ante. But I would not abandon the name just yet.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:56 UTC</span>

<span style="font-size: 90%;">Why not?</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:11 UTC</span>

<span style="font-size: 90%;">you are right I guess but may be it's just a temporary state...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:15:11 UTC</span>

<span style="font-size: 90%;">you are right I guess but may be it's just a temporary state...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:22 UTC</span>

<span style="font-size: 90%;">Don't burn the bridge before you have built a new one.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:15:28 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:29 UTC</span>

<span style="font-size: 90%;">_@xanadu_ Don't you think actually renaming the project will have the most impact on acceptance? "Push first, rename later" seems to me like a sure way to create more confusion.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:44 UTC</span>

<span style="font-size: 90%;">This is not about burning a bridge</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:57 UTC</span>

<span style="font-size: 90%;">Again, all major cloud providers have OWASP CRS</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:16:11 UTC</span>

<span style="font-size: 90%;">If we don't start building our own brand now, by changing the name, why would we expect it to be any different/better in a years time?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:23 UTC</span>

<span style="font-size: 90%;">Wouldn't we?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:26 UTC</span>

<span style="font-size: 90%;">There's no plan</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:28 UTC</span>

<span style="font-size: 90%;">Are we going to be worse?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:28 UTC</span>

<span style="font-size: 90%;">No strategy</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:31 UTC</span>

<span style="font-size: 90%;">OK. What I fear is: We rename our project, we stop using ModSec, we continue to publish material and people no longer take notice. Maybe I'm wrong, but I am reluctant to try it out, since there is no way going back.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:16:39 UTC</span>

<span style="font-size: 90%;">We should have a clear plan, agree on it, and implement it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:51 UTC</span>

<span style="font-size: 90%;">We should agree on the change, not doing it now.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:10 UTC</span>

<span style="font-size: 90%;">If we don't agree, then why the plan?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:25 UTC</span>

<span style="font-size: 90%;">But we all agree, don't we? It's just the timing that's the issue</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:34 UTC</span>

<span style="font-size: 90%;">I don't think we agree</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:34 UTC</span>

<span style="font-size: 90%;">So then let's agree that we ultimately want to abandon ModSec. And then we continue the conversation during the next few weeks how to get there.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:07 UTC</span>

<span style="font-size: 90%;">Also our communication partner Alessandro should be part of the conversation I think (he's on holiday or I would have invited him for this topic)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:08 UTC</span>

<span style="font-size: 90%;">Hang on, "abandon ModSec" in the name or as an option?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">Just the name, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:34 UTC</span>

<span style="font-size: 90%;">As an option, no.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:34 UTC</span>

<span style="font-size: 90%;">I think ModSec should be erased. But I kind of like the WAF Core Rule Set idea.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:58 UTC</span>

<span style="font-size: 90%;">Only talking of name, of course.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:30 UTC</span>

<span style="font-size: 90%;">Sure. You all know that I want the CRS to be the universal rule set :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:50 UTC</span>

<span style="font-size: 90%;">So in the future I even feel constrained by the term WAF</span>

**jit** <span style="color: grey; font-size: 90%;">19:20:05 UTC</span>

<span style="font-size: 90%;">I like the phrase "OWASP Core Rule Set" more. It sounds like that the project is directly from OWASP.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:13 UTC</span>

<span style="font-size: 90%;">Could be a dead-end, but PCI is very strong for marketing purposes ...</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:20:23 UTC</span>

<span style="font-size: 90%;">OWASP WAF CRS is acronym soup…</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">agree OWASP Core Rule Set sounds better IMO</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:42 UTC</span>

<span style="font-size: 90%;">_@jit_ It would be OWASP WAF Core Rule Set, or short CRS as before.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:00 UTC</span>

<span style="font-size: 90%;">Or "OWASP Core Rule Set", what I thought we would have in mind.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:19 UTC</span>

<span style="font-size: 90%;">OWASP Core Rule Set</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:21:48 UTC</span>

<span style="font-size: 90%;">OWASP Rule Set?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:22:16 UTC</span>

<span style="font-size: 90%;">FZS :wink:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">agree OWASP Core Rule Set sounds better IMO</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">agree OWASP Core Rule Set sounds better IMO</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:24 UTC</span>

<span style="font-size: 90%;">Let's decide too quickly. Since we will come up with a plan, please leave this open. And then we continue the discussion.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:06 UTC</span>

<span style="font-size: 90%;">BTW, on deciding too quickly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:12 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:28 UTC</span>

<span style="font-size: 90%;">So we agree: We want to erase ModSec from our name and we want to develop a plan how to pull this off in a useful timeframe. Next topic?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:43 UTC</span>

<span style="font-size: 90%;">Previous topic, please.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:45 UTC</span>

<span style="font-size: 90%;">Sat Nov 4 - Sat Nov 11 around Budapest in Hungary</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:52 UTC</span>

<span style="font-size: 90%;">Did we voted on this?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:21 UTC</span>

<span style="font-size: 90%;">I think you proposed that date and nobody from the project objected. Anything amiss with the date?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:03 UTC</span>

<span style="font-size: 90%;">I said I had stuff until the 4th :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:13 UTC</span>

<span style="font-size: 90%;">Sadly, I'm in the other corner of the world</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:36 UTC</span>

<span style="font-size: 90%;">So you arrive on 5th. Or would you rather postpone another week?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:56 UTC</span>

<span style="font-size: 90%;">Who else has problems attending 4-11th?</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:19 UTC</span>

<span style="font-size: 90%;">uhm, the weather is not so nice here after mid November</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:27:31 UTC</span>

<span style="font-size: 90%;">I think JC wanted to be part of, but on those dates there is also DC</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:27:40 UTC</span>

<span style="font-size: 90%;">Or we can do earlier in Oct</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:43 UTC</span>

<span style="font-size: 90%;">Yes, he said so.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:14 UTC</span>

<span style="font-size: 90%;">Earlier in October is tough. School holidays and I moderate two conference the week from Oct 23.</span>

**airween** <span style="color: grey; font-size: 90%;">19:28:53 UTC</span>

<span style="font-size: 90%;">and what about before 23rd of Oct?</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:41 UTC</span>

<span style="font-size: 90%;">nice weather, tons of wine festivals... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:42 UTC</span>

<span style="font-size: 90%;">If you all prefer that, I won't block it.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:30:01 UTC</span>

<span style="font-size: 90%;">The week before Oct23 is not possible for me.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:17 UTC</span>

<span style="font-size: 90%;">taking a week on Oct for me is tough</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:31 UTC</span>

<span style="font-size: 90%;">But we all gain a week in Nov!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:48 UTC</span>

<span style="font-size: 90%;">We could do Sun-Sun, thus Nov 5 - 12th.</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">for me 6-16 oct is tough</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:16 UTC</span>

<span style="font-size: 90%;">That way _@fzipitria_ would be there for the start and we only miss _@JC_</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:44 UTC</span>

<span style="font-size: 90%;">when could _@JC_ join to us?</span>

**JC** <span style="color: grey; font-size: 90%;">19:33:26 UTC</span>

<span style="font-size: 90%;">Appsec is 1-3 nov so joining something the week after is tough.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:37:52 UTC</span>

<span style="font-size: 90%;">BTW in Appsec I will present about Coraza and most likely CRS 4 :p</span>

**JC** <span style="color: grey; font-size: 90%;">19:34:27 UTC</span>

<span style="font-size: 90%;">I could try to sneak one day or 1.5 days but depends on how I do arrange things at home. I am honoured you consider me in the decision but I guess what works best for OWASP CRS devs is the best.</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:05 UTC</span>

<span style="font-size: 90%;">who would it be good for Nov 5th - 12th?

And who wouldn't be good for that?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:52 UTC</span>

<span style="font-size: 90%;">Ok,  now looks settled.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:59 UTC</span>

<span style="font-size: 90%;">Thanks all for commenting.</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:48 UTC</span>

<span style="font-size: 90%;">_@xanadu_, _@Paul Beckett_, _@maxleske_?</span>

**JC** <span style="color: grey; font-size: 90%;">19:37:52 UTC</span>

<span style="font-size: 90%;">BTW in Appsec I will present about Coraza and most likely CRS 4 :p</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:37:52 UTC</span>

<span style="font-size: 90%;">BTW in Appsec I will present about Coraza and most likely CRS 4 :p</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:15 UTC</span>

<span style="font-size: 90%;">Should work for me, I'm flexible</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:55 UTC</span>

<span style="font-size: 90%;">Budapest is close to _@azurIt_, perhaps he will attend</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:38:57 UTC</span>

<span style="font-size: 90%;">Tricky for me as clashes with daughters birthday.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:15 UTC</span>

<span style="font-size: 90%;">Ah, too bad _@Paul Beckett_</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:41 UTC</span>

<span style="font-size: 90%;">I'm unsure at the moment.</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:10 UTC</span>

<span style="font-size: 90%;">right</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:17 UTC</span>

<span style="font-size: 90%;">I guess we'll see as the event draws nearer. For the moment it's just good to fix it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:02 UTC</span>

<span style="font-size: 90%;">Continue?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:11 UTC</span>

<span style="font-size: 90%;">So Coraza is now actively looking for somebody to work on the libCoraza nginx port.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:42:43 UTC</span>

<span style="font-size: 90%;">hmm... libCoraza...?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:30 UTC</span>

<span style="font-size: 90%;">Can somebody from the Coraza explain this some more? Where would we fit in?</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:43 UTC</span>

<span style="font-size: 90%;">hmm... libCoraza...?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:42:43 UTC</span>

<span style="font-size: 90%;">hmm... libCoraza...?</span>

**JC** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">So as we all know, nginx and apache are huge blockers for coraza to take over.</span>

**JC** <span style="color: grey; font-size: 90%;">19:43:20 UTC</span>

<span style="font-size: 90%;">We tried in the past with libcoraza but some difficulties were found.</span>

**JC** <span style="color: grey; font-size: 90%;">19:43:31 UTC</span>

<span style="font-size: 90%;">Now with v3 in place it is time to look at that iceberg and see how can we sort out.</span>

**JC** <span style="color: grey; font-size: 90%;">19:44:05 UTC</span>

<span style="font-size: 90%;">I had the faith we could overcome the problem in nginx with wasm but I now talk regularly with one maintainer at nginx and they won’t introduce wasm in nginx itself (although it is the go to solution for other nginx products)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:25 UTC</span>

<span style="font-size: 90%;">Whom are you in contact with?</span>

**JC** <span style="color: grey; font-size: 90%;">19:44:55 UTC</span>

<span style="font-size: 90%;">Matt Yacobucci, he introduced WASM in nginx-agent</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:05 UTC</span>

<span style="font-size: 90%;">Thanks.</span>

**JC** <span style="color: grey; font-size: 90%;">19:45:06 UTC</span>

<span style="font-size: 90%;">The plan is to roll out wasm in other products.</span>

**JC** <span style="color: grey; font-size: 90%;">19:45:38 UTC</span>

<span style="font-size: 90%;">And along with VMWare there will be some work to introduce proxy-wasm in apache but then _@airween_ had a point that we still need c bindings to succeed.</span>

**JC** <span style="color: grey; font-size: 90%;">19:46:20 UTC</span>

<span style="font-size: 90%;">So we need to lookback to libcoraza IMHO because it seems we are in a dead end.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:41 UTC</span>

<span style="font-size: 90%;">Where could we fit in?</span>

**JC** <span style="color: grey; font-size: 90%;">19:46:42 UTC</span>

<span style="font-size: 90%;">libcoraza isn’t easy to achieve, nor to maintain.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:55 UTC</span>

<span style="font-size: 90%;">And did you have contact with a potential person doing this?</span>

**JC** <span style="color: grey; font-size: 90%;">19:47:15 UTC</span>

<span style="font-size: 90%;">Nope, we did not (correct me _@fzipitria_)</span>

**JC** <span style="color: grey; font-size: 90%;">19:47:45 UTC</span>

<span style="font-size: 90%;">But we need to at least try one more time libcoraza. Where you fit in is that we need resources or ownership on that product.</span>

**JC** <span style="color: grey; font-size: 90%;">19:48:03 UTC</span>

<span style="font-size: 90%;">At the moment we don’t have a single company investing on libcoraza or a solution to get coraza in nginx.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:30 UTC</span>

<span style="font-size: 90%;">We did not.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:56 UTC</span>

<span style="font-size: 90%;">We did it a third thought with Juan Pablo last week. But we opened for more minds.</span>

**JC** <span style="color: grey; font-size: 90%;">19:49:39 UTC</span>

<span style="font-size: 90%;">So, if we found someone with the right skills, could we get sponsorship from CRS?</span>

**JC** <span style="color: grey; font-size: 90%;">19:50:24 UTC</span>

<span style="font-size: 90%;">Or a company around CRS?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:30 UTC</span>

<span style="font-size: 90%;">I think we talked about a sum, but given the size of the project you describe it might be more an incentive to get going. But maybe that's all it takes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:50:59 UTC</span>

<span style="font-size: 90%;">The problem, as I see it, is not having something.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:06 UTC</span>

<span style="font-size: 90%;">We can always ask existing sponsors. But given their business model, most of them have replaced ModSec already.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:09 UTC</span>

<span style="font-size: 90%;">Maintenance is the big burden</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:38 UTC</span>

<span style="font-size: 90%;">Also: coraza is not modsecurity</span>

**JC** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">I mean, libcoraza has limited functionality, it is not that it should developed from scratch. The main problem is who is going to own this? Who is going to debug memory issues? I think we need to find someone to own.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:48 UTC</span>

<span style="font-size: 90%;">If it works, I am confident enough people would support maintenance, since it would being used widely after the EOL of ModSec.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:53 UTC</span>

<span style="font-size: 90%;">Could the C code be generated? That would reduce the maintenance part.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:07 UTC</span>

<span style="font-size: 90%;">We have code already</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:15 UTC</span>

<span style="font-size: 90%;">For both</span>

**JC** <span style="color: grey; font-size: 90%;">19:52:22 UTC</span>

<span style="font-size: 90%;">Does someone knows of any company interested on be involved on this?</span>

**JC** <span style="color: grey; font-size: 90%;">19:52:28 UTC</span>

<span style="font-size: 90%;">as a company</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:40 UTC</span>

<span style="font-size: 90%;">So it's still a question of stabilization and making it production ready. And you think it takes an experienced Nginx developer?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:14 UTC</span>

<span style="font-size: 90%;">I know companies interested in running it. But none interested in developing it.</span>

**JC** <span style="color: grey; font-size: 90%;">19:53:25 UTC</span>

<span style="font-size: 90%;">I think the profile will be more like a C+Go person. The main barrier is sharing memory and pointers among the two.</span>

**JC** <span style="color: grey; font-size: 90%;">19:53:30 UTC</span>

<span style="font-size: 90%;">So not much of nginx</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:46 UTC</span>

<span style="font-size: 90%;">Thanks. Good to know the profile.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:54:46 UTC</span>

<span style="font-size: 90%;">Could also be a topic for a Master's thesis, don't you think?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:55:03 UTC</span>

<span style="font-size: 90%;">Indeed it could.</span>

**JC** <span style="color: grey; font-size: 90%;">19:54:57 UTC</span>

<span style="font-size: 90%;">This work takes time and effort, problem is exactly time. v3 was a milestone and we got there, now what we expect is the community to show up more in coraza itself and less on backing companies to continue maintaining it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:05 UTC</span>

<span style="font-size: 90%;">The product might not be perfect but if we emphasized memory safety...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:10 UTC</span>

<span style="font-size: 90%;">Could be. But stabilization does not sound like thesis.</span>

**JC** <span style="color: grey; font-size: 90%;">19:55:49 UTC</span>

<span style="font-size: 90%;">True.</span>

**JC** <span style="color: grey; font-size: 90%;">19:56:35 UTC</span>

<span style="font-size: 90%;">So TL;DR if it is about a budget, I can ask people, I personally have expertise in CGO but I don’t have the time to buy in that problem.</span>

**JC** <span style="color: grey; font-size: 90%;">19:56:56 UTC</span>

<span style="font-size: 90%;">But more important is the ownership.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:32 UTC</span>

<span style="font-size: 90%;">Glad you emphasize this that much.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:38 UTC</span>

<span style="font-size: 90%;">It's easily forgotten.</span>

**JC** <span style="color: grey; font-size: 90%;">19:57:38 UTC</span>

<span style="font-size: 90%;">Coraza team can not own at this point libcoraza.</span>

**JC** <span style="color: grey; font-size: 90%;">19:57:57 UTC</span>

<span style="font-size: 90%;">Even if we make it work.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:25 UTC</span>

<span style="font-size: 90%;">So we know the situation now and can continue to think how to solve this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:23 UTC</span>

<span style="font-size: 90%;">Next up: Security scanners.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:57 UTC</span>

<span style="font-size: 90%;">We pretty much ended the previous discussion with the stalement and the realization that it's very hard to agree what is an acceptable UA and what is a not-acceptable UA.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:01:19 UTC</span>

<span style="font-size: 90%;">All the easy topics tonight :joy:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:25 UTC</span>

<span style="font-size: 90%;">I have to go, that's getting too late for me. I'm sorry...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:50 UTC</span>

<span style="font-size: 90%;">I am personally leaning in the direction of keeping the brief list of very bad security scanners and kicking up all the rest. If anybody wants to keep my work around, it's better suited in a plugin, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:32 UTC</span>

<span style="font-size: 90%;">Drawing a line between ahrefs and the other crawlers and experimental stuff is very hard, especially when we want to do it in an automatic way. The sources just do not make this distinction.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:15 UTC</span>

<span style="font-size: 90%;">I tend to agree.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:21 UTC</span>

<span style="font-size: 90%;">I agree also</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:09 UTC</span>

<span style="font-size: 90%;">If we do it that way, we're mostly done. We just need to come up with a tag for the scanner rule and remove the rest from the PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:07 UTC</span>

<span style="font-size: 90%;">Other PR in this direction: Crawler rule is kicked, Scanner URIs are kicked (20 years old anyways and no sane attacker falls into this trap and even if, what do we gain when the server would respond with 404 anyways).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:12 UTC</span>

<span style="font-size: 90%;">Scanner headers: Not overly important, but very nice for fingerprinting CRS and the anomaly threshold. But rule is also outdated. I doubt it can be improved so we might just as well kick it or leaving it for the fingerprinting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:17 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:55 UTC</span>

<span style="font-size: 90%;">Sorry, what do you mean be scanner headers?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:38 UTC</span>

<span style="font-size: 90%;">acunetix-product
(acunetix web vulnerability scanner
acunetix-scanning-agreement
acunetix-user-agreement
myvar=1234
x-ratproxy-loop
bytes=0-,5-0,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9,5-10,5-11,5-12,5-13,5-14
x-scanner</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:05 UTC</span>

<span style="font-size: 90%;">cat scanners-headers.data</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:13 UTC</span>

<span style="font-size: 90%;">You can enumerate x-scanner and determine the anomaly score value that way. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:37 UTC</span>

<span style="font-size: 90%;">The rule is obviously nonsense. But I like the fingerprinting. Might be able to re-do this somewhere else.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:02 UTC</span>

<span style="font-size: 90%;">Do you generally agree with me and I just go ahead and prepare the PRs?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:28 UTC</span>

<span style="font-size: 90%;">I do not hear any different opinions. So I'll do as explained.</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:41 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:11 UTC</span>

<span style="font-size: 90%;">I had entered all the open wordlist issues in the agenda, but it got overwritten somehow - again.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:57 UTC</span>

<span style="font-size: 90%;">It's the following</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:18 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:48 UTC</span>

<span style="font-size: 90%;">JP is working on a PR for PHP function names. But the ones without any takers are the ones above.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:47 UTC</span>

<span style="font-size: 90%;">I would be very happy if we could divide these up and come up with the remaining PRs in the following weeks. Half of them are not overly difficult.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:39 UTC</span>

<span style="font-size: 90%;">2653 can probably also be postponed after CRSv4 since it's a response rule. So we would be down to 4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:58 UTC</span>

<span style="font-size: 90%;">2644 is an ancient list with files like .htaccess that should be intercepted when being uploaded. Certainly needs a major overhaul. I reckon the filenames can be taken out of other rule files ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">Sources I mean.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">It's a bit late already. Could we just say that everyone takes a peek until end of the week and hopefully they'll all get picked?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:22 UTC</span>

<span style="font-size: 90%;">Until the end of the week would be fine with me.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:37 UTC</span>

<span style="font-size: 90%;">Happy to contact people about their preferences... :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:21:17 UTC</span>

<span style="font-size: 90%;">Not sure I can manage to fix some of them alone, but I can spend some time helping on something</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:01 UTC</span>

<span style="font-size: 90%;">3 items on the list to go. No need to look into the agenda problem, but a direction for the other 2 items would be useful.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:42 UTC</span>

<span style="font-size: 90%;">PR 3219: Do we want to block 127.0.0.1 and friends in requests, or is this asking for too much problems. I am torn.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:58 UTC</span>

<span style="font-size: 90%;">What are the pros?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:23:14 UTC</span>

<span style="font-size: 90%;">The cons are it blocks people testing on localhost, tutorials that say use 127.0.0.1, etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:14 UTC</span>

<span style="font-size: 90%;">SSRF using this. Reportedly a lot.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:17 UTC</span>

<span style="font-size: 90%;">But it's PL1.</span>

**jit** <span style="color: grey; font-size: 90%;">20:23:23 UTC</span>

<span style="font-size: 90%;">I don't think 127.0.0.1 will be a problem in production.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:10 UTC</span>

<span style="font-size: 90%;">_@xanadu_ can you elaborate on this? How would the 127.0.0.1 arrive on the server as part of a request? Instructing a server to contact another server on 127.0.0.1?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:24 UTC</span>

<span style="font-size: 90%;">Or when editing the tutorial?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:24:49 UTC</span>

<span style="font-size: 90%;">When building engine+CRS. Not in a production reverse proxy, no.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:55 UTC</span>

<span style="font-size: 90%;">you already cannot use IPs</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">20:25:56 UTC</span>

<span style="font-size: 90%;">Numeric host header rule? That just warns, doesn't block atm.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:02 UTC</span>

<span style="font-size: 90%;">It is blocking</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:25:04 UTC</span>

<span style="font-size: 90%;">It's not uncommon in prod for their to be local agents performing service monitoring against 127.0.0.1</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:25 UTC</span>

<span style="font-size: 90%;">we have a whitelist for that :point_up:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:25:46 UTC</span>

<span style="font-size: 90%;">We already have a regex that does pretty much what's in this PR and that includes a match for localhost and 127.0.0.1, IIRC</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:54 UTC</span>

<span style="font-size: 90%;">Sure, 127.0.0.1 is used all over the place, but is it used as part of a HTTP request to another server?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:18 UTC</span>

<span style="font-size: 90%;">934120</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:26:42 UTC</span>

<span style="font-size: 90%;">That's actually a good point: would this be a CRITICAL level rule? The "Numeric host header detected" rule is only INFO level, I think? It doesn't score 5, that's for sure.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:49 UTC</span>

<span style="font-size: 90%;">_@maxleske_ so you think 3219 can easily include 127.0.0.1 as well?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">20:28:26 UTC</span>

<span style="font-size: 90%;">Not sure. 934120 is the sibling at PL 2. So maybe not.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:55 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:45 UTC</span>

<span style="font-size: 90%;">If "127.0.0.1 detected" is only scoring 2 or 3 on the anomaly score, then this is no problem at PL 1, right?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:55 UTC</span>

<span style="font-size: 90%;">Or is the idea that it should score 5?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:16 UTC</span>

<span style="font-size: 90%;">The PR is about 934110 and that is a critical rule, this scoring 5.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:29:21 UTC</span>

<span style="font-size: 90%;">Hmm, ok.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:21 UTC</span>

<span style="font-size: 90%;">We can also keep it for RC2 and see what happens. I am really unsure whether this hits in prod or not. It might, or it might be limited to blog posts where people explain things using 127.0.0.1 and friends.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">20:31:54 UTC</span>

<span style="font-size: 90%;">I don't think that'd be a problem in a blog post as the rule doesn't take REQUEST_BODY into consideration.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:30:55 UTC</span>

<span style="font-size: 90%;">Does this affect our containers for testing?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:07 UTC</span>

<span style="font-size: 90%;">I usually spin up a Docker ModSec+CRS and curl to localhost</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:31:36 UTC</span>

<span style="font-size: 90%;">*to test payloads, new rules, etc</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:10 UTC</span>

<span style="font-size: 90%;">but for 3219 we're talking about blocking or not something like '?url=[http://127.0.1](http://127.0.1)' or am I wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:12 UTC</span>

<span style="font-size: 90%;">It's only looking at cookies and args and request_filename. So I guess not. Host header is not covered.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:17 UTC</span>

<span style="font-size: 90%;">not the host header</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">Oh. Okay :slightly_smiling_face: Thanks for clarifying.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:32:26 UTC</span>

<span style="font-size: 90%;">I don't think so. It matches args and cookies</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:28 UTC</span>

<span style="font-size: 90%;">Exactly _@theMiddle_ .</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:32:55 UTC</span>

<span style="font-size: 90%;">blocking ipv4 and v6 in args, sounds legit</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:57 UTC</span>

<span style="font-size: 90%;">I'd say we give it a shot. 3rd party commenter really thinks this is the whole point of the rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:31 UTC</span>

<span style="font-size: 90%;">I think it's worth a shot too. It would look strange to have localhost or 127.0.0.1 in an argument.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:38 UTC</span>

<span style="font-size: 90%;">Alright then, final point for tonight:
v3.3.5. We agreed at the February meeting to do a 3.3.5 patch-based fix release with the scoring/PL fixes, along with a blog post.
</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:52 UTC</span>

<span style="font-size: 90%;">_@xanadu_ volunteered to write this, I think.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:35:07 UTC</span>

<span style="font-size: 90%;">Yes, happy to write it. Just need to know if we agree on what we will tell vendors and users.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:35:28 UTC</span>

<span style="font-size: 90%;">"We don't have time or resources to do a full release. Sponsor us pleeeeeease" ?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:35:30 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:53 UTC</span>

<span style="font-size: 90%;">Maybe more focus on bringing out CRSv4. Which is also true...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:58 UTC</span>

<span style="font-size: 90%;">Otherwise I agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:14 UTC</span>

<span style="font-size: 90%;">Anything to add there?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:08 UTC</span>

<span style="font-size: 90%;">Guess not. So let's close this. We'll think about a better way to edit the agenda before the next meeting and I thank you all for joining.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:44 UTC</span>

<span style="font-size: 90%;">This was a very long and fruitful meeting. Great results!</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:54 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:40:56 UTC</span>

<span style="font-size: 90%;">Good night everyone!</span>

**jit** <span style="color: grey; font-size: 90%;">20:41:08 UTC</span>

<span style="font-size: 90%;">Good night everyone.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:41:14 UTC</span>

<span style="font-size: 90%;">Good night</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:42:15 UTC</span>

<span style="font-size: 90%;">Good night</span>

**airween** <span style="color: grey; font-size: 90%;">20:47:10 UTC</span>

<span style="font-size: 90%;">good night!</span>

**JC** <span style="color: grey; font-size: 90%;">20:48:30 UTC</span>

<span style="font-size: 90%;">:sleeping:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:54:55 UTC</span>

<span style="font-size: 90%;">good night</span>

