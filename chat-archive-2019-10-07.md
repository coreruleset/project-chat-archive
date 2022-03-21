### Mon, Oct 7th, 2019

**dune73** <span style="color: grey; font-size: 90%;">18:32:29 UTC</span>

<span style="font-size: 90%;">Hello, hello. It's CRS community chat time. Anybody here?
Hello _@emphazer_!</span>

**fgs** <span style="color: grey; font-size: 90%;">18:32:40 UTC</span>

<span style="font-size: 90%;">:raised_hand:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:47 UTC</span>

<span style="font-size: 90%;">Hi _@fgs_!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:32:50 UTC</span>

<span style="font-size: 90%;">Hi all!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:32:50 UTC</span>

<span style="font-size: 90%;">Hi</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:56 UTC</span>

<span style="font-size: 90%;">Hi all!</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">18:33:08 UTC</span>

<span style="font-size: 90%;">Hi</span>

**Steven Wojcik** <span style="color: grey; font-size: 90%;">18:33:10 UTC</span>

<span style="font-size: 90%;">Hi all! I am going ot be pretty silent and just see how everyone gets along for a while :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:24 UTC</span>

<span style="font-size: 90%;">Hello everybody. Welcome _@Steven Wojcik_ and _@nerrehmit_! Great to have you guys with us!</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:29 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Reza** <span style="color: grey; font-size: 90%;">18:33:57 UTC</span>

<span style="font-size: 90%;">_@Reza_ has joined the channel</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:33:58 UTC</span>

<span style="font-size: 90%;">hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:29 UTC</span>

<span style="font-size: 90%;">Hello _@Reza_ ! Right in time!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:34:37 UTC</span>

<span style="font-size: 90%;">Hey friends</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:54 UTC</span>

<span style="font-size: 90%;">Hello _@csanders_: We really missed you in Amsterdam!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:35:07 UTC</span>

<span style="font-size: 90%;">I missed you all more</span>

**csanders** <span style="color: grey; font-size: 90%;">18:35:17 UTC</span>

<span style="font-size: 90%;">Sorry I couldn't be there</span>

**airween** <span style="color: grey; font-size: 90%;">18:35:26 UTC</span>

<span style="font-size: 90%;">hi all</span>

**csanders** <span style="color: grey; font-size: 90%;">18:35:35 UTC</span>

<span style="font-size: 90%;">Hey _@airween_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:50 UTC</span>

<span style="font-size: 90%;">Hola _@csanders_!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:35:57 UTC</span>

<span style="font-size: 90%;">Buenos</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:03 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:06 UTC</span>

<span style="font-size: 90%;">Our agenda is at <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1567>
And like I said, it's really rather stuffed. So we will probably take a bit longer than usually. Or be super efficient.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:07 UTC</span>

<span style="font-size: 90%;">We have a long list of PRs. We usually take them first, but we might want to do all the other things first tonight. Are there opinions?</span>

**fgs** <span style="color: grey; font-size: 90%;">18:37:35 UTC</span>

<span style="font-size: 90%;">I’d agree with that. Let’s talk about the PRs at the end.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:15 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:28 UTC</span>

<span style="font-size: 90%;">OK. Let's do it that way for a change.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:51 UTC</span>

<span style="font-size: 90%;">We had a very, very cool CRS summit in Amsterdam. Most of you were there and we had so much fun.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:11 UTC</span>

<span style="font-size: 90%;">We also did a bit of a planning meeting and came up with things we would like to see in CRS 3.3.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:35 UTC</span>

<span style="font-size: 90%;">Of course this is non-binding, but if we announce our plans, then make they have a bigger chance to become reality.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:11 UTC</span>

<span style="font-size: 90%;">I'll go quickly through the items and explain / comment them if necessary. Others please chime in or tell me if I am wrong with something.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:49 UTC</span>

<span style="font-size: 90%;">Header whitelisting. _@franbuehler_ and I and _@theMiddle_ and more people started with http header whitelisting rules. Probably for PL4 or so.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:07 UTC</span>

<span style="font-size: 90%;">The idea is to whitelist all headers where possible and have a complete list of http request header that we accept.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:37 UTC</span>

<span style="font-size: 90%;">This will take quite a bit of work, but the it is really beneficial and many attacks will be blocked that way. Speak HTTP Request smuggling and what not.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:18 UTC</span>

<span style="font-size: 90%;">Tagging: We are not happy with the minimal and coarse tagging that we do. We have been feeling like overhauling this for quite some tiem and I even promised to pull this off. But I never did.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:46 UTC</span>

<span style="font-size: 90%;">Now _@fzipitria_ said he will look to find a student to do that and we all think that's a great idea and a typical job for a student.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:33 UTC</span>

<span style="font-size: 90%;">Non-European languages cause a lot of problems for CRS. Or the other way around. We need to improve our support. But it's a tedious area and I have yet to see a volunteer take this one.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:26 UTC</span>

<span style="font-size: 90%;">We wanted to do a workshop at the CloudFest conference in Germany back in March to look into CRS for hosting providers. We had to cancel this, but some hosters are still interested and CPanel is interested to join with us to do this.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:52 UTC</span>

<span style="font-size: 90%;">That would be CloudFest 2020 in March. And a possible result would be a rules exclusion package for hosters.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:45:21 UTC</span>

<span style="font-size: 90%;">I'm and to make that :)</span>

**csanders** <span style="color: grey; font-size: 90%;">18:45:35 UTC</span>

<span style="font-size: 90%;">Able</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:58 UTC</span>

<span style="font-size: 90%;">We generally want better rules for all things JS, this builds on the new NodeJS rules and boils down to improve the protection of the MEAN stack. I see some interest from _@franbuehler_ fo this.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:07 UTC</span>

<span style="font-size: 90%;">_@csanders_: That would be the hosting rules package?</span>

**csanders** <span style="color: grey; font-size: 90%;">18:46:22 UTC</span>

<span style="font-size: 90%;">I meant make it to the conference</span>

**csanders** <span style="color: grey; font-size: 90%;">18:46:26 UTC</span>

<span style="font-size: 90%;">:-P</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:46 UTC</span>

<span style="font-size: 90%;">The same is true for python protection, where we are quite thin so far.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">Yes, I want to work on rules protetcting the MEAN stack.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:02 UTC</span>

<span style="font-size: 90%;">Cool, _@csanders_.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:47:12 UTC</span>

<span style="font-size: 90%;">I plan a conference talk on this, so I have to do something :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">18:47:21 UTC</span>

<span style="font-size: 90%;">Wrt the mean stuff in starting to see lack of good Json support starting to be a major issue</span>

**csanders** <span style="color: grey; font-size: 90%;">18:47:36 UTC</span>

<span style="font-size: 90%;">*im</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:07 UTC</span>

<span style="font-size: 90%;">My new pet project is transformations and how to get better coverage via better handling of encoded payloads. It's a continous work and I am slowly getting a hang of this.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:30 UTC</span>

<span style="font-size: 90%;">We thought we were quite good vs the new HTTP Request Smuggling that is all the rage with PenTesters / Bounty Hunters these days, but then James Kettle presented at the AppSec and suddenly we looked not so well. So we need to get to the bottom of this. _@fgs_ has already reactivated a PR we retired in Spring when we did not really understand the problem (it seems).</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:28 UTC</span>

<span style="font-size: 90%;">What's the purpose of the transformations?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:44 UTC</span>

<span style="font-size: 90%;">We talked to the Burp / PortSwigger guys in AMS too (-> James Kettle, Gareth Heynes). They confirmed that
- CRS seems to be better than the competition and they are sorry WAFs have such a bad reputation and how that affects us</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:50:47 UTC</span>

<span style="font-size: 90%;">too bad that i missed that :-(</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:43 UTC</span>

<span style="font-size: 90%;">- They do not know how CRS really stacks against all their attacks, because they do not know who runs it, CRS does not advertise its being used and they hate the hassle to set up a test site</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:06 UTC</span>

<span style="font-size: 90%;">- They would be open to run their payload against a public demo site</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:02 UTC</span>

<span style="font-size: 90%;">So we agreed we should setup something along the lines of demo-pl[1-4].<http://coreruleset.org|coreruleset.org> that allows to submit payloads and returns the rules being triggered.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:15 UTC</span>

<span style="font-size: 90%;">I have that mostly done</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:18 UTC</span>

<span style="font-size: 90%;">:)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:53:19 UTC</span>

<span style="font-size: 90%;">nice idea!</span>

**csanders** <span style="color: grey; font-size: 90%;">18:53:36 UTC</span>

<span style="font-size: 90%;">The only part remaining is the DNS</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:54 UTC</span>

<span style="font-size: 90%;">Can you give us a time-frame _@csanders_?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:54:05 UTC</span>

<span style="font-size: 90%;">when you say payload, you mean the raw request/[response]?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:17 UTC</span>

<span style="font-size: 90%;">Right now, the conversation is still warm, so I think we should deliver this soon.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:30 UTC</span>

<span style="font-size: 90%;">I'd love to do this by the end of the week</span>

**csanders** <span style="color: grey; font-size: 90%;">18:54:51 UTC</span>

<span style="font-size: 90%;">Esp if it's a priority</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">Wonderful.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:55:45 UTC</span>

<span style="font-size: 90%;">I'll try and finish it tonight in fact</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:51 UTC</span>

<span style="font-size: 90%;">awesome</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">_@airween_: transformations allow ModSecurity to decode say a hex-encoded payload and then run the normal rules on the result. There are like 35 transformations in total. 15-20 are actually useful.</span>

**csanders** <span style="color: grey; font-size: 90%;">18:56:21 UTC</span>

<span style="font-size: 90%;">Brb taking off finally</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:07 UTC</span>

<span style="font-size: 90%;">We also concluded, that we will never be able to fix all the open issues, so it's better to actually close them with a "won't fix" instead of having them clog our processes.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:43 UTC</span>

<span style="font-size: 90%;">We plan to setup a bot / automatic service, that comments an issue that has been stale for too long and then after a grace period, the issue will really be closed.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:09 UTC</span>

<span style="font-size: 90%;">Some people in the room (mostly me) felt uneasy about this, but it is the only way forward.</span>

**fgs** <span style="color: grey; font-size: 90%;">18:58:28 UTC</span>

<span style="font-size: 90%;">One bot to close them all!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:36 UTC</span>

<span style="font-size: 90%;">And finally: we would like to run another CRS community summit in 2020. AppSec has been announced for June in Dublin, the Wednesday of said week would be June 17, 2020 in Dublin.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:43 UTC</span>

<span style="font-size: 90%;">We will depend on upstream for setting up a bot, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:06 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:08 UTC</span>

<span style="font-size: 90%;">Sadly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:14 UTC</span>

<span style="font-size: 90%;">No, the bot can be done via a .stale.yaml file afaics.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:33 UTC</span>

<span style="font-size: 90%;">Look in the marketplace. I think I posted a link a few days back.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:01:18 UTC</span>

<span style="font-size: 90%;">You still need to install the app</span>

**fgs** <span style="color: grey; font-size: 90%;">19:01:26 UTC</span>

<span style="font-size: 90%;">I think that needs perms in the repo</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:03 UTC</span>

<span style="font-size: 90%;">I see. Yes, that makes sense.
Is there somebody that would take that bot thing into his / her hands? I think there is the technology, but also timeframes, correct wording, etc to do.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:35 UTC</span>

<span style="font-size: 90%;">The thing is that we need interacting with upstream... otherwise I can do it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:28 UTC</span>

<span style="font-size: 90%;">Upstream? As in distribution? As in ModSec or as in Spiderlabs?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:37 UTC</span>

<span style="font-size: 90%;">Spiderlabs</span>

**csanders** <span style="color: grey; font-size: 90%;">19:04:41 UTC</span>

<span style="font-size: 90%;">If all else fails I can manually write some selenium script to do it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:45 UTC</span>

<span style="font-size: 90%;">Anyway, if you volunteer _@fzipitria_, the lead team can try and get the permissions sorted. We are about to schedule a call with the new responsible person at TW.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:46 UTC</span>

<span style="font-size: 90%;">The one that controls the organization</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:56 UTC</span>

<span style="font-size: 90%;">Excellent.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:01 UTC</span>

<span style="font-size: 90%;">That may work/help</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:01 UTC</span>

<span style="font-size: 90%;">Thanks for volunteering.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:05:02 UTC</span>

<span style="font-size: 90%;">:) better option ^^</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:33 UTC</span>

<span style="font-size: 90%;">I think that's it for the planning meeting in Amsterdam. Anything else?
As a side note: I attended a talk of the OWASP SAMM project. Project Lead Bart de Win explained how they do an annual project retreat with the core contributors and that this is being paid by sponsors. All the money is funneled via OWASP HQ and I have now asked via mail how they pull this off. Working with HQ can be very cumbersome and getting sponsoring money in the project account seems  a major feat to me.
But whatever, I would love to do this and we have so many commercial users now, we should be able to get this done too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:57 UTC</span>

<span style="font-size: 90%;">Next item (we're slowly getting to the bottom in this section).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:19 UTC</span>

<span style="font-size: 90%;">We are not signing our releases. We should start to sign them.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:33 UTC</span>

<span style="font-size: 90%;">GPG or something along those lines.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:11:12 UTC</span>

<span style="font-size: 90%;">Sign, checksum or both?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:22 UTC</span>

<span style="font-size: 90%;">_@csanders_ / _@walter_: I guess that's a job for one of us.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:25 UTC</span>

<span style="font-size: 90%;">Both</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:29 UTC</span>

<span style="font-size: 90%;">_@fgs_: I guess both.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:11:44 UTC</span>

<span style="font-size: 90%;">Because the complexity is quite different.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:11:50 UTC</span>

<span style="font-size: 90%;">I’d agree that we should do both.</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:57 UTC</span>

<span style="font-size: 90%;">I’ve already put the checksums on <http://coreruleset.org/installation/|coreruleset.org/installation/> but haven’t had experience with signing yet</span>

**fgs** <span style="color: grey; font-size: 90%;">19:11:59 UTC</span>

<span style="font-size: 90%;">(complexity wrt handling the key)</span>

**fgs** <span style="color: grey; font-size: 90%;">19:12:17 UTC</span>

<span style="font-size: 90%;">Can we attach the sum to the releases page too?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:18 UTC</span>

<span style="font-size: 90%;">_@walter_ I would like to have them as a file</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:22 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:29 UTC</span>

<span style="font-size: 90%;">My idea is to check them automatically</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:37 UTC</span>

<span style="font-size: 90%;">So who wants to create an issue and self-assign?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:59 UTC</span>

<span style="font-size: 90%;">I can do it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:16 UTC</span>

<span style="font-size: 90%;">I think we should have the checksum in a different place than github</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:18 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ you mean on <http://coreruleset.org/|coreruleset.org/>?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:20 UTC</span>

<span style="font-size: 90%;">Just in case</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:27 UTC</span>

<span style="font-size: 90%;">Yeah, even both</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:36 UTC</span>

<span style="font-size: 90%;">We can upload the same file to both places</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:47 UTC</span>

<span style="font-size: 90%;">Some people will just read the hashes</span>

**fgs** <span style="color: grey; font-size: 90%;">19:14:10 UTC</span>

<span style="font-size: 90%;">Yes, I wonder how many will check the signature</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:18 UTC</span>

<span style="font-size: 90%;">Some people will automate the check, downloading releases from GH and check with checksums in <http://coresuleset.org|coresuleset.org></span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:35 UTC</span>

<span style="font-size: 90%;">And others will check the GPG signature</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:01 UTC</span>

<span style="font-size: 90%;">Thank you for volunteering (again)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:33 UTC</span>

<span style="font-size: 90%;">Close to this: We have reached Best Practice Accreditation at <https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/502></span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:54 UTC</span>

<span style="font-size: 90%;">Big thank you to _@fzipitria_ who pushed this forward for a very long time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:47 UTC</span>

<span style="font-size: 90%;">There is a new feature / tab on github, that allows projects to setup a security policy and gives the project a way to deal with security issues out of the view. We probably want to give this a try - also to prevent security researches to publish false negatives / get CVEs! for false negatives when they could simply tell us instead.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:02 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:32 UTC</span>

<span style="font-size: 90%;">_@csanders_ said he was writing something</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:31 UTC</span>

<span style="font-size: 90%;">_@csanders_: Can you confirm?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:42 UTC</span>

<span style="font-size: 90%;">Guess he is away from the keyboard. But who needs confirmation. I'll just write him down as the volunteer. hehe.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:39 UTC</span>

<span style="font-size: 90%;">Now _@SpartanTri_: You would like to talk about base64 decoding everywhere. This touches on the more general transformation / decoding ideas I am working on. But would you like to explain your thinking here?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:53 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_: You around?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:25:59 UTC</span>

<span style="font-size: 90%;">Yep</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:26:10 UTC</span>

<span style="font-size: 90%;">On the mobile</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:27 UTC</span>

<span style="font-size: 90%;">Can you explain your thinking, or do we postpone this?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:26:39 UTC</span>

<span style="font-size: 90%;">I like the idea of the decoding, base 64 especially </span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:27:06 UTC</span>

<span style="font-size: 90%;">But without overdoing it to avoid a huge performance penalty </span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:27:25 UTC</span>

<span style="font-size: 90%;">Base64 will introduce already a it of false positives </span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:47 UTC</span>

<span style="font-size: 90%;">But do you want to add this to all the rules where you think it makes sense? Or how to go about it?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:29:59 UTC</span>

<span style="font-size: 90%;">What is the reasoning behind adding base64 to most (all?) rules?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:30:27 UTC</span>

<span style="font-size: 90%;">The thing with b64 is that it can be anywhere and would hide all type of attacks</span>

**fgs** <span style="color: grey; font-size: 90%;">19:30:53 UTC</span>

<span style="font-size: 90%;">Sure, but can we say the same about base 62?</span>

**fgs** <span style="color: grey; font-size: 90%;">19:31:00 UTC</span>

<span style="font-size: 90%;">Or any other encoding?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:31:07 UTC</span>

<span style="font-size: 90%;">Not every app would be compatible</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:31:40 UTC</span>

<span style="font-size: 90%;">Base64 is the most used by far</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:13 UTC</span>

<span style="font-size: 90%;">This is where my plans come in. I would enable all these additional decodings at a higher PL. Ideally 3, because that would give PL3 a real raison d'être and PL3 is ran by people who know how to handle  FPs and can usually live with the performance issue.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:17 UTC</span>

<span style="font-size: 90%;">it wuold be useful if we can identify ARGS with b64 value and then exclude it from some rules...</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:18 UTC</span>

<span style="font-size: 90%;">it would be nice to activate it optional... but i guess thats not possible....</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:32:44 UTC</span>

<span style="font-size: 90%;">It is</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:33:02 UTC</span>

<span style="font-size: 90%;">Check the poc in my account</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:17 UTC</span>

<span style="font-size: 90%;">Can you link it quickly, please?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:33:19 UTC</span>

<span style="font-size: 90%;">I prefer a enable disable approach </span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:34:20 UTC</span>

<span style="font-size: 90%;"><https://github.com/spartantri/owasp-modsecurity-crs/tree/v3.3/devb64decoder?files=1></span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:34:44 UTC</span>

<span style="font-size: 90%;">As many of the interesting payloads are pl1 or pl2</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:34:59 UTC</span>

<span style="font-size: 90%;">Check not payloads</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:35:02 UTC</span>

<span style="font-size: 90%;">Sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:53 UTC</span>

<span style="font-size: 90%;">You are extremely close to my proposal with this (you were probably faster), but how do you get the rules to look at this?</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:03 UTC</span>

<span style="font-size: 90%;">_@emphazer_: <https://github.com/spartantri/owasp-modsecurity-crs/blob/34a327c25f6a6a87b16c671ddfbde93206f48848/crs-setup.conf.example#L245-L251>
_@theMiddle_: <https://github.com/spartantri/owasp-modsecurity-crs/blob/34a327c25f6a6a87b16c671ddfbde93206f48848/rules/REQUEST-901-INITIALIZATION.conf#L334-L346></span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:03 UTC</span>

<span style="font-size: 90%;">Sed replacement on |ARGS| </span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:03 UTC</span>

<span style="font-size: 90%;">nice!</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:26 UTC</span>

<span style="font-size: 90%;">Tested with the container on Apache </span>

**emphazer** <span style="color: grey; font-size: 90%;">19:37:26 UTC</span>

<span style="font-size: 90%;">wow</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:37:36 UTC</span>

<span style="font-size: 90%;">2.9modsec</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:39 UTC</span>

<span style="font-size: 90%;">Looks very promising. Do you have some measures about performance drop?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:11 UTC</span>

<span style="font-size: 90%;">So people would need to run sed on the rules?</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:17 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_: I think there are some missed rules, where ARGS exists but the new variable don't</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:38:19 UTC</span>

<span style="font-size: 90%;">seems a good idea, idk if it could be a performance killer, but def. seems something nice to have</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:38:21 UTC</span>

<span style="font-size: 90%;">that would be very interesting.  a performance comparison.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:38:33 UTC</span>

<span style="font-size: 90%;">Not yet I’m building it</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:39:00 UTC</span>

<span style="font-size: 90%;">Yes that would happen on rules that are derived from other rules with run time cars</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:39:41 UTC</span>

<span style="font-size: 90%;">No just had to implement it on our rule set</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:43 UTC</span>

<span style="font-size: 90%;">I sent to you a script in private what can helps to you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">Performance: I have been posting performance information of my more holistic approach above. Just the base64 decoding will be quite fast. However, the rules execution will drop by 20% because the extended ARGS will have to include a Regex.</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:32 UTC</span>

<span style="font-size: 90%;">yeah I’ve also been concerned about performance…</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:36 UTC</span>

<span style="font-size: 90%;">but in this case where the new variable `TX:/b64decoded_*/` added, we can remove the action `t:base64Decode` - or am I wrong?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:17 UTC</span>

<span style="font-size: 90%;">_@SpartanTri_: I think we want a very similar thing, I am simply looking at all useful transformations, but enabling / disabling them separately is entirely possible. I suggest we join forces and come up with a complete proposal.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:31 UTC</span>

<span style="font-size: 90%;">@aireween: t:base64Decode has zero performance impact when compared to the TX:/^b64decoded_*/ which is bloody expensive and you need to set it up at startup time.</span>

**fgs** <span style="color: grey; font-size: 90%;">19:43:42 UTC</span>

<span style="font-size: 90%;">How common are these attacks?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:43:45 UTC</span>

<span style="font-size: 90%;">SecRuleUpdateTargetById</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:02 UTC</span>

<span style="font-size: 90%;">SecRuleUpdateTargetById at startup time.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:09 UTC</span>

<span style="font-size: 90%;">I think it is mostly a bypass, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:25 UTC</span>

<span style="font-size: 90%;">SecRuleUpdateTargetById 13120,920250,920270,920370,920230,920271,920272,920273,920460,921110,921120,921130,930120,931100,931120,931130,932100,932105,932110,932115,932120,932130,932140,932150,932160,932171,932106,932190,933100,933120,933130,933140,933200,933150,933160,933170,933180,933210,933151,933131,933161,933190,934100,941100,941110,941120,941130,941140,941160,941170,941180,941190,941200,941210,941220,941230,941240,941250,941260,941270,941280,941290,941300,941310,941350,941360,941370,941150,941320,941330,941340,941380,942100,942140,942160,942170,942190,942220,942230,942240,942250,942270,942280,942290,942320,942350,942360,942500,942110,942120,942130,942150,942180,942200,942210,942260,942300,942310,942330,942340,942361,942370,942380,942390,942400,942410,942470,942480,942430,942440,942450,942510,942251,942490,942431,942460,942511,942432,943100,944100,944110,944110,944120,944130,944200,944210,944240,944250,944300 TX:/^tf_*/</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:44:27 UTC</span>

<span style="font-size: 90%;">Yep so you can remove the performance impact </span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:44:38 UTC</span>

<span style="font-size: 90%;">Use range</span>

**fgs** <span style="color: grey; font-size: 90%;">19:44:42 UTC</span>

<span style="font-size: 90%;">But it relies on the backend to be useful</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:03 UTC</span>

<span style="font-size: 90%;">No, range does not work, because some rules don't do ARGS.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:45:32 UTC</span>

<span style="font-size: 90%;">What about a new tag</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:45:37 UTC</span>

<span style="font-size: 90%;">To handle it by tag</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:47 UTC</span>

<span style="font-size: 90%;">And I do not see how you can remove performance impact. What we must strive to do is making sure that people who do not want this, do not get the performance loss of the TX:/^tf_*/. That is 20%.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:46:19 UTC</span>

<span style="font-size: 90%;">It’s load time not runtime the engine does a clean up before loading</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:23 UTC</span>

<span style="font-size: 90%;">That's why it's probably better to instruct people to issue SecRuleUpdateTargetById than adding the TX by default.</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:42 UTC</span>

<span style="font-size: 90%;">did you check if SecRuleUpdateTargetById works in ModSec 3?</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">not saying it doesn’t but :wink:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:47:06 UTC</span>

<span style="font-size: 90%;">Hehehe </span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:12 UTC</span>

<span style="font-size: 90%;">Nope. Every SecRule will execute the RegEx to complete the target list. That results in a reduction of the throughput of 20%.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:47:19 UTC</span>

<span style="font-size: 90%;">Considering all surprises with v3</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:47:24 UTC</span>

<span style="font-size: 90%;">We have to check</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:47:37 UTC</span>

<span style="font-size: 90%;">If enabled yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:41 UTC</span>

<span style="font-size: 90%;">Yes, we will need to check.</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:56 UTC</span>

<span style="font-size: 90%;">it will be more slower on ModSec3, I guess...</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:48:03 UTC</span>

<span style="font-size: 90%;">That’s we we updatetarget at load time</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:48:17 UTC</span>

<span style="font-size: 90%;">Everything is slower in v3</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:10 UTC</span>

<span style="font-size: 90%;">ModSec2 has a cache store for the transactions - if there is a transformation in a rule, and it finished, the engine push the transformed value into the cache. ModSec3 doesn't have.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:53 UTC</span>

<span style="font-size: 90%;">Transformation cache? I thought that was introduced around 2.5.7 and kicked before 2.6.0 came out. Am I so wrong about this?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:13 UTC</span>

<span style="font-size: 90%;">Ah, transactions. Sorry. Read transformations.</span>

**airween** <span style="color: grey; font-size: 90%;">19:50:33 UTC</span>

<span style="font-size: 90%;">hmmm... don't know exactly, have to check - but dew days ago I searched something in the code, and then realised that there is a cache</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:50:44 UTC</span>

<span style="font-size: 90%;">Could we please continue with the agenda please?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:04 UTC</span>

<span style="font-size: 90%;">Anyways. We more or less know what we want, we are not so sure if this brings a lot in terms of security and _@SpartanTri_ and I will simply continue to work on this and come up with a joint PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:06 UTC</span>

<span style="font-size: 90%;">OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:55 UTC</span>

<span style="font-size: 90%;">Before we return to the PRs, there is a proposal that was submitted by _@Reza_. Are you still around _@Reza_? Do you want to explain?
It's a fairly complex topic, so I think we should give it like 10 minutes and then continue the discussion at some other time.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:53:17 UTC</span>

<span style="font-size: 90%;">ya, im here</span>

**Reza** <span style="color: grey; font-size: 90%;">19:53:29 UTC</span>

<span style="font-size: 90%;">So I started a project a few years ago called TextGlass (<https://textglass.com/>).</span>

**Reza** <span style="color: grey; font-size: 90%;">19:53:41 UTC</span>

<span style="font-size: 90%;">The goal of the project is to create a viable ecosystem of text parsing and classification clients. Rule writers would only be concerned with writing their rules (domains) and these domains would run across a number of languages and platforms.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:54:08 UTC</span>

<span style="font-size: 90%;">Basically there are a lot of parallels between TextGlass and the CRS <-> modsecurity relationship.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">19:54:26 UTC</span>

<span style="font-size: 90%;">Interesting </span>

**Reza** <span style="color: grey; font-size: 90%;">19:54:34 UTC</span>

<span style="font-size: 90%;">I am familiar with the CRS and my thought was that if there is interest in starting something fresh, then this is the platform for that.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:54:52 UTC</span>

<span style="font-size: 90%;">TextGlass is still very early, so its possible to add the features needed for something more complex like CRS rule matching.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:55:09 UTC</span>

<span style="font-size: 90%;">And most importantly, TextGlass is open, everyone who wants to join will get a piece of the pie.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:55:21 UTC</span>

<span style="font-size: 90%;"><end></span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:59 UTC</span>

<span style="font-size: 90%;">Wow. That was quick. Thank you.</span>

**Reza** <span style="color: grey; font-size: 90%;">19:56:10 UTC</span>

<span style="font-size: 90%;">yes, kind of had the pitch ready to go :slightly_smiling_face:</span>

**Reza** <span style="color: grey; font-size: 90%;">19:56:25 UTC</span>

<span style="font-size: 90%;">ping me if you are interested</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:40 UTC</span>

<span style="font-size: 90%;">Do you want to share your email?</span>

**Reza** <span style="color: grey; font-size: 90%;">19:57:04 UTC</span>

<span style="font-size: 90%;">yes, <mailto:reza@naghibi.com|reza@naghibi.com> or <mailto:project@textglass.org|project@textglass.org></span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:37 UTC</span>

<span style="font-size: 90%;">What are your next steps here? Is there anything we can do / should do to make this work for you?</span>

**Reza** <span style="color: grey; font-size: 90%;">19:57:41 UTC</span>

<span style="font-size: 90%;">and for some background, I worked with _@Steven Wojcik_ designing the modsecurity integration with Varnish Enterprise</span>

**Reza** <span style="color: grey; font-size: 90%;">19:58:33 UTC</span>

<span style="font-size: 90%;">probably understanding where to start with the ruleset</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:35 UTC</span>

<span style="font-size: 90%;">... that we saw at the CRS summitin AMS</span>

**Reza** <span style="color: grey; font-size: 90%;">19:58:49 UTC</span>

<span style="font-size: 90%;">is there anything that can be improved, should we just port it over</span>

**Reza** <span style="color: grey; font-size: 90%;">19:59:43 UTC</span>

<span style="font-size: 90%;">it would have to be JSON based, the key to getting wide support is making the clients as easy to digest as possible by using the lowest common denominator building blocks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:01 UTC</span>

<span style="font-size: 90%;">The new msc_pyparser stuff from _@airween_ will make it very easy for you to transform the rules in a form that can be fed into textglass, I think. And such a transposing is probably the best start.</span>

**Reza** <span style="color: grey; font-size: 90%;">20:00:09 UTC</span>

<span style="font-size: 90%;">yup</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:54 UTC</span>

<span style="font-size: 90%;">What is much more difficult is a different behaviour or expressing different things with our rules. Going beyond ModSec so to say.</span>

**Reza** <span style="color: grey; font-size: 90%;">20:02:11 UTC</span>

<span style="font-size: 90%;">well, textglass does pattern matching, so that allows it to match thousands of rules in a single pass</span>

**Reza** <span style="color: grey; font-size: 90%;">20:02:31 UTC</span>

<span style="font-size: 90%;">and that is the basis for the engine, currently</span>

**Reza** <span style="color: grey; font-size: 90%;">20:03:04 UTC</span>

<span style="font-size: 90%;">but it can match any number of patterns, keep state, variables, etc</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:12 UTC</span>

<span style="font-size: 90%;">Very nice. I think everybody has a certain idea of your project. Thank you for joining us and we're looking forward to hear more from you!</span>

**Reza** <span style="color: grey; font-size: 90%;">20:03:14 UTC</span>

<span style="font-size: 90%;">so its *almost* there</span>

**Reza** <span style="color: grey; font-size: 90%;">20:03:22 UTC</span>

<span style="font-size: 90%;">yes, thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:35 UTC</span>

<span style="font-size: 90%;">I hope you can get some traction.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:53 UTC</span>

<span style="font-size: 90%;">Back to our agenda then. I suggest we start with the PRs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:45 UTC</span>

<span style="font-size: 90%;">1585 has been very active during the meeting. _@fgs_ and friends: have you reached a conclusion or does this still take more work?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:05:35 UTC</span>

<span style="font-size: 90%;">I believe so. :+1: for the changes.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:11 UTC</span>

<span style="font-size: 90%;">Maybe we can discuss about having a exclusion file for monitoring tools?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:06:55 UTC</span>

<span style="font-size: 90%;">Or we can talk at a different time, once we have more rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:55 UTC</span>

<span style="font-size: 90%;">Hmm</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:13 UTC</span>

<span style="font-size: 90%;">It depends. Once you have  a rule it's annoying to move it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:35 UTC</span>

<span style="font-size: 90%;">Do you think people would want to enable an exclusion package so they can get their monitoring solution around the FPs?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:07:47 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:48 UTC</span>

<span style="font-size: 90%;">Should not we avoid monitoring FPs by default?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:07:52 UTC</span>

<span style="font-size: 90%;">I already do that</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:03 UTC</span>

<span style="font-size: 90%;">Oh, I meant to have a separate file. Not necessarily an opt-in file.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:12 UTC</span>

<span style="font-size: 90%;">A data file?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:30 UTC</span>

<span style="font-size: 90%;">No, a new file just for monitoring tools</span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:55 UTC</span>

<span style="font-size: 90%;">Not sure if we should spend too much time on this now.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:09:16 UTC</span>

<span style="font-size: 90%;">Was just a proposal after reading [#1583](https://github.com/coreruleset/coreruleset/issues/#1583)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:35 UTC</span>

<span style="font-size: 90%;">Just quickly: You mean REQUEST-903.9007-Monitoring-Tools?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:09:48 UTC</span>

<span style="font-size: 90%;">Yup</span>

**fgs** <span style="color: grey; font-size: 90%;">20:10:07 UTC</span>

<span style="font-size: 90%;">Something along those lines</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:28 UTC</span>

<span style="font-size: 90%;">I do not like this idea very much. But let's get going with the agenda and continue the conversation some other time.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:54 UTC</span>

<span style="font-size: 90%;">But about this PR: You guys will finish it and we're done with it for tonight?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:20 UTC</span>

<span style="font-size: 90%;">I think it's done, right _@fgs_?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:11:29 UTC</span>

<span style="font-size: 90%;">Yup, they are good to go IMO</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:37 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:00 UTC</span>

<span style="font-size: 90%;">1584 is a better documentation for GeoIP. Has anybody reviewed this?</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:57 UTC</span>

<span style="font-size: 90%;">oooh my, did the crs-setup.conf still refer to our deleted upgrade.py file? that’s my oversight</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:35 UTC</span>

<span style="font-size: 90%;">this LGTM, but I haven’t tried yet, but it looks good</span>

**fgs** <span style="color: grey; font-size: 90%;">20:13:46 UTC</span>

<span style="font-size: 90%;">I had a quick look but need to review all the details.
Happy to work with _@fzipitria_ to get it merged</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:13:47 UTC</span>

<span style="font-size: 90%;">Good explanation. But I did not test it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:19 UTC</span>

<span style="font-size: 90%;">Sounds good. Thanks and if you have comments, when please add it to the PR so _@fgs_ can merge eventually.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:06 UTC</span>

<span style="font-size: 90%;">1583 has been mentioned before. Do we want to leave this for the moment until we have a strategy for monitoring tools? (Happy to take this offline and join a discussion)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:15:36 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:19 UTC</span>

<span style="font-size: 90%;">I wouldn’t mind merging it for the time being as I am not foreseeing so many monitoring tools..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:29 UTC</span>

<span style="font-size: 90%;">Fair enough. Do you want to self-assign and we continue?</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:02 UTC</span>

<span style="font-size: 90%;">sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:07 UTC</span>

<span style="font-size: 90%;">Cool. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:36 UTC</span>

<span style="font-size: 90%;">With the next one (1581) we have a welcome contribution from a new contributor, but it fails due to broken tests, it seems.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:57 UTC</span>

<span style="font-size: 90%;">_@fgs_: You looked into this: Do you need support here or can you handle this yourself?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:19:25 UTC</span>

<span style="font-size: 90%;">I will work with _@emphazer_ to get this sorted.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:33 UTC</span>

<span style="font-size: 90%;">Thank you guys.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:50 UTC</span>

<span style="font-size: 90%;">awesome</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:20:09 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">OK. The next are a dozen of new tests I added across a dozen PRs. People noticed, that I sometimes wrap payloads in `"` and sometimes in `'`. I think _@fgs_ opted to merge. But the stuff is still open. Do you want me to redo before mergind or do we ignore this - possibly review _everything_ in tree in the future (I do not think we have a clear policy here).</span>

**fgs** <span style="color: grey; font-size: 90%;">20:21:53 UTC</span>

<span style="font-size: 90%;">I’m inclined to the latter</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:22 UTC</span>

<span style="font-size: 90%;">Btw: The tests are based on the portswigger XSS cheatsheet and extend rules with too few unit tests with new alerts (due to these XSS attacks).</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:35 UTC</span>

<span style="font-size: 90%;">I don’t mind the format as long as it’s valid YAML…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:49 UTC</span>

<span style="font-size: 90%;">It's definitely valid and all tests pass.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:22:52 UTC</span>

<span style="font-size: 90%;">PR1583 would allow space for SSRF</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:23:18 UTC</span>

<span style="font-size: 90%;">Yeah, we were talking about that</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:23:45 UTC</span>

<span style="font-size: 90%;">I think the User-Agent check would mostly prevent that, right?</span>

↳ **fgs** <span style="color: grey; font-size: 90%;">20:24:48 UTC</span>

<span style="font-size: 90%;">That’d also be the case for the other rule too</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:25:49 UTC</span>

<span style="font-size: 90%;">exactly</span>

↳ **walter** <span style="color: grey; font-size: 90%;">20:26:01 UTC</span>

<span style="font-size: 90%;">I think it’s covered</span>

↳ **SpartanTri** <span style="color: grey; font-size: 90%;">20:27:26 UTC</span>

<span style="font-size: 90%;">I think its ok to list it and add it commented but not enabled by default</span>

↳ **fgs** <span style="color: grey; font-size: 90%;">20:27:48 UTC</span>

<span style="font-size: 90%;">This would be a good reason to have an exclusion file :slightly_smiling_face:</span>

↳ **SpartanTri** <span style="color: grey; font-size: 90%;">20:29:08 UTC</span>

<span style="font-size: 90%;">I agree, I would prefer this as file and add a warning or something so when it comes to a bad softwre being exploited the CVE stays on their side not ours</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">20:30:39 UTC</span>

<span style="font-size: 90%;">Good. Let's go for a file then, I see the benefits</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:54 UTC</span>

<span style="font-size: 90%;">very nice to have those tests :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:10 UTC</span>

<span style="font-size: 90%;">Very nice, thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:58 UTC</span>

<span style="font-size: 90%;">There is more in my report in the blog posts. In fact we have thousands of rule alerts and all payloads in the report in the blog post. So if anybody wants to have a go?
(-> BTW: Very good first issues: Just grab a few payloads and create new tests out of it)</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:24:00 UTC</span>

<span style="font-size: 90%;">its trusting too much on the host, the rule seems ok if enabled manually not by default</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:55 UTC</span>

<span style="font-size: 90%;">Can somebody merge these tests and we go on?</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:07 UTC</span>

<span style="font-size: 90%;">haha sure! let me do it</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:28 UTC</span>

<span style="font-size: 90%;">good for my KPIs</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:32 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:29 UTC</span>

<span style="font-size: 90%;">1565 is also a new contribution. But I see it needs more work. Correct _@fgs_?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:05 UTC</span>

<span style="font-size: 90%;">Or just more background to make a good judgement?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:28:22 UTC</span>

<span style="font-size: 90%;">Yes, we need to sort out the details I think</span>

**fgs** <span style="color: grey; font-size: 90%;">20:28:49 UTC</span>

<span style="font-size: 90%;">I will talk to the reporter</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:49 UTC</span>

<span style="font-size: 90%;">Anybody wants to join said discussion? I'd like to get the meeting over, so better take this offline</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:13 UTC</span>

<span style="font-size: 90%;">It seems the volunteers are slowly pulling out. So it's with you _@fgs_. Thank you for taking care of this. Please shout if you get stuck,</span>

**fgs** <span style="color: grey; font-size: 90%;">20:30:21 UTC</span>

<span style="font-size: 90%;">Will do, ty.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:39 UTC</span>

<span style="font-size: 90%;">I have not looked into 1548. Anybody covering this?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:31:19 UTC</span>

<span style="font-size: 90%;">Not me.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:56 UTC</span>

<span style="font-size: 90%;">I think a lot of base64 stuff got into the PR</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:01 UTC</span>

<span style="font-size: 90%;">this PR is a bit unclear to me</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:09 UTC</span>

<span style="font-size: 90%;">probably better to start a clear new one…</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:13 UTC</span>

<span style="font-size: 90%;">This looks fairly innocent, but then it's a huge  change set. Probably a mistake _@SpartanTri_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:32 UTC</span>

<span style="font-size: 90%;">I guess.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:32:40 UTC</span>

<span style="font-size: 90%;">which one?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:46 UTC</span>

<span style="font-size: 90%;">1548</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:47 UTC</span>

<span style="font-size: 90%;">[#1548](https://github.com/coreruleset/coreruleset/issues/#1548)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:48 UTC</span>

<span style="font-size: 90%;">your 1548</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:33:02 UTC</span>

<span style="font-size: 90%;">checking</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:34:02 UTC</span>

<span style="font-size: 90%;">mmm oops yep synced my b64 with 3.3, this was all merged already, I will close thisone</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:12 UTC</span>

<span style="font-size: 90%;">OK. Thanks.</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:34:32 UTC</span>

<span style="font-size: 90%;">closed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:36 UTC</span>

<span style="font-size: 90%;">1538: _@theMiddle_ Could you explain what you are trying to achieve with this PR?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:36:15 UTC</span>

<span style="font-size: 90%;">it just removes a deprecated transformation function (t:removeComments) that I've used in 941370 rule</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:37:03 UTC</span>

<span style="font-size: 90%;">removing `t:removeComments` it was necessary to change the rx too</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:13 UTC</span>

<span style="font-size: 90%;">Hm, but it also changes the regex and introduces new transformations ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:17 UTC</span>

<span style="font-size: 90%;">Also maybe I forgot: How is t:removeComments depreceated?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:38:23 UTC</span>

<span style="font-size: 90%;">yes, removing `t:removeComments` many payloads stop triggering the rule, so I chaged the rx too in order to catch all payloads</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:38:52 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-%28v2.x%29#removeComments></span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:58 UTC</span>

<span style="font-size: 90%;">Payloads used in the tests?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:39:51 UTC</span>

<span style="font-size: 90%;">yes, I've changed all tests to be more stricter</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:57 UTC</span>

<span style="font-size: 90%;">Thank you for the link. I think I have seen this discussion back in 2016...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:07 UTC</span>

<span style="font-size: 90%;">Is this the the only use of removeComments in CRS?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:40:29 UTC</span>

<span style="font-size: 90%;">Yes</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:40:35 UTC</span>

<span style="font-size: 90%;">yes it seems</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:50 UTC</span>

<span style="font-size: 90%;">Then this all makes a lot of sense. Thank you for explaining. Seems to be ready to be merged.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:40:54 UTC</span>

<span style="font-size: 90%;">my fault, didn't read the wiki before using it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:55 UTC</span>

<span style="font-size: 90%;">_@fgs_: Can you make sure this is merged ASAP?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:42:02 UTC</span>

<span style="font-size: 90%;">Will do</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:05 UTC</span>

<span style="font-size: 90%;">thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:28 UTC</span>

<span style="font-size: 90%;">Let's move to 1534 then. I think we have _@nerrehmit_ in the chat unless he fell asleep.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:32 UTC</span>

<span style="font-size: 90%;">Thank you for the contribution.</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:42:40 UTC</span>

<span style="font-size: 90%;">I'm still awake :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:52 UTC</span>

<span style="font-size: 90%;">_@fgs_ you volunteered to take a look, but you have a lot on your table these days.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:43:24 UTC</span>

<span style="font-size: 90%;">I have forgotten :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:39 UTC</span>

<span style="font-size: 90%;">No worries. Can you revive this effort or should I take over?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:44:04 UTC</span>

<span style="font-size: 90%;">No, I will do a sweep this week</span>

**fgs** <span style="color: grey; font-size: 90%;">20:44:15 UTC</span>

<span style="font-size: 90%;">Unless someone else wants to take it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:31 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: I saw you touch the keyboard ..</span>

**fgs** <span style="color: grey; font-size: 90%;">20:44:35 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ I saw you typing :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:44:48 UTC</span>

<span style="font-size: 90%;">Hahah, yes I could review it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:54 UTC</span>

<span style="font-size: 90%;">thank you!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:20 UTC</span>

<span style="font-size: 90%;">Almost done</span>

**fgs** <span style="color: grey; font-size: 90%;">20:45:25 UTC</span>

<span style="font-size: 90%;">I removed myself and added you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:26 UTC</span>

<span style="font-size: 90%;">1525</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:09 UTC</span>

<span style="font-size: 90%;">We need somebody to review this fix by _@fgs_. Volunteers?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:15 UTC</span>

<span style="font-size: 90%;">This has been idle for quite a while.</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:19 UTC</span>

<span style="font-size: 90%;">I think I’ve tested this, I’ll take it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:28 UTC</span>

<span style="font-size: 90%;">Thank you _@walter_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:07 UTC</span>

<span style="font-size: 90%;">1310: This is back from the grave after James Kettle presented his reasearch at DefCon and AppSec. I would like to join with _@fgs_ to extend this to fix the problem completely, since it takes more than only this rule.</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:40 UTC</span>

<span style="font-size: 90%;">right, it turned out to be a bit harder right?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:16 UTC</span>

<span style="font-size: 90%;">It's all about bypasses and hiding malicious T-E headers from the RP.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:36 UTC</span>

<span style="font-size: 90%;">So we probably need to look on the left and on the right as well. But this PR is a very good base.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:16 UTC</span>

<span style="font-size: 90%;">It's the essential bit in my eyes. But 3.3 development has only just started, so we can invest some more thinking into this - even more so as most commercial vendors have the problem too.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:51:17 UTC</span>

<span style="font-size: 90%;">We know that for nginx and apache it’s a nop</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:51:30 UTC</span>

<span style="font-size: 90%;">I'm almost falling asleep. Good night :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:35 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:41 UTC</span>

<span style="font-size: 90%;">same here, good night _@franbuehler_ :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:54 UTC</span>

<span style="font-size: 90%;">I am not convinced, but I need to watch his presentation and extract all his payloads.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:51:58 UTC</span>

<span style="font-size: 90%;">Since both decided to go for unsetting the header</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:52:17 UTC</span>

<span style="font-size: 90%;">good night</span>

**dune73** <span style="color: grey; font-size: 90%;">20:52:33 UTC</span>

<span style="font-size: 90%;">He had a few really dirty tricks. Most was based on the idea that the RP does not even notice there is a header, but the backend processes it as a separate header and bingo.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:52:59 UTC</span>

<span style="font-size: 90%;">Right. And we should have another rule to cover that.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:53:11 UTC</span>

<span style="font-size: 90%;">But it really depends on what the webserver does before it passed the payload.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:18 UTC</span>

<span style="font-size: 90%;">But anyways, we are done with the agenda and we will get this done together.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:53:23 UTC</span>

<span style="font-size: 90%;">So we should test it with some RL bypasses</span>

**dune73** <span style="color: grey; font-size: 90%;">20:53:48 UTC</span>

<span style="font-size: 90%;">Thanks everybody for joining. I hope future meetings will be shorter again.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:54:10 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:54:15 UTC</span>

<span style="font-size: 90%;">:fireworks:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:18 UTC</span>

<span style="font-size: 90%;">_@fgs_: Absolutely. Let me come up with those RL bypasses, then we do unit tests and then we write rules to protect against it.</span>

**fgs** <span style="color: grey; font-size: 90%;">20:54:30 UTC</span>

<span style="font-size: 90%;">Sounds good to me</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:09 UTC</span>

<span style="font-size: 90%;">alright! goodbye everybody :wave: :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:55:23 UTC</span>

<span style="font-size: 90%;">thanks, bye!</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:55:28 UTC</span>

<span style="font-size: 90%;">good night :wave:</span>

**airween** <span style="color: grey; font-size: 90%;">20:55:42 UTC</span>

<span style="font-size: 90%;">good night</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:55:42 UTC</span>

<span style="font-size: 90%;">Good night</span>

**fgs** <span style="color: grey; font-size: 90%;">20:55:44 UTC</span>

<span style="font-size: 90%;">bye bye all!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:55:47 UTC</span>

<span style="font-size: 90%;">Good night everybody!</span>

