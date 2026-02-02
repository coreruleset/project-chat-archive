### Mon, Feb 2nd, 2026

**dune73** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**michela** <span style="color: grey; font-size: 90%;">19:30:40 UTC</span>

<span style="font-size: 90%;">Hi!  :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:45 UTC</span>

<span style="font-size: 90%;">Heloooo!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:03 UTC</span>

<span style="font-size: 90%;">Hello</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:10 UTC</span>

<span style="font-size: 90%;">evening'</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:26 UTC</span>

<span style="font-size: 90%;">Hello</span>

**jit** <span style="color: grey; font-size: 90%;">19:32:05 UTC</span>

<span style="font-size: 90%;">Hi everyone!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">I'm impressed with all the merged PRs. Is this about the LTS coming up?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:34:45 UTC</span>

<span style="font-size: 90%;">Judging by the agenda, we don't have much to talk about tonight. Except for the LTS maybe. Any topics any of you want to talk about?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:35 UTC</span>

<span style="font-size: 90%;">There is a lot of unrest in OWASP about the upcoming new website and Meetup cancellation. We're not overly affected, but I think the project should know.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:27 UTC</span>

<span style="font-size: 90%;">What's there to say... Wait till it blows over... We have our own project website and don't really use Meetup. At some point, the OWASP website will have a new design and be hosted on a different platform. And maybe we need to do a bit of work on it before it goes live. That's my view at the moment. Haven't really been following everything.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:41 UTC</span>

<span style="font-size: 90%;">We are mostly using [lu.ma](http://lu.ma) now</span>

**michela** <span style="color: grey; font-size: 90%;">19:40:16 UTC</span>

<span style="font-size: 90%;">Hah. I didn't know what Luma was. So, I clicked that link and got a 500 status code response. It appears to be down. </span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:06 UTC</span>

<span style="font-size: 90%;">FYI: OWASP found out very late Meetup was raising the subscription fee for OWASP. OWASP HQ decided they could not really afford it anymore and started to remove groups and inform people about the cancellation on short notice. Hundreds of OWASP chapters managed their chapter exclusively via Meetup and they lost or run the risk of losing all their contacts (we talking of tens of thousands of contacts if not more). Last week HQ performed an 180 turn and now it's not quite clear what happens.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:24 UTC</span>

<span style="font-size: 90%;">So :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:44 UTC</span>

<span style="font-size: 90%;">In other news, we (i.e., Felipe) are forging ahead to the LTS release.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:07 UTC</span>

<span style="font-size: 90%;">Thanks to everyone who has been helping out.</span>

**michela** <span style="color: grey; font-size: 90%;">19:44:21 UTC</span>

<span style="font-size: 90%;">Business opportunity! Replace Meet-up.  :wink:</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:45:05 UTC</span>

<span style="font-size: 90%;">OWASP's plan was to use the new unfinished website to replace Meetup ... Go figure.</span>

↳ **michela** <span style="color: grey; font-size: 90%;">19:47:14 UTC</span>

<span style="font-size: 90%;">Interesting. I don't like Meet-Up but the trouble with that could be that many people might not know about the events or local groups. I suppose they will promote the groups another way.  :woman-shrugging:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:31 UTC</span>

<span style="font-size: 90%;">If I'm playing the devil's advocate: Does not merging that many PRs before an LTS grow the risk of bringing a lot of little tested stuff into the LTS?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:31 UTC</span>

<span style="font-size: 90%;">Doesn't really matter, IMO. It has to be in a state that we are happy with. It's more a point in time that matters, at least that's what I've gathered from the conversations we had in Bern.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:47 UTC</span>

<span style="font-size: 90%;">Also, merging a PR doesn't necessarily mean that the stuff is untested.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:51 UTC</span>

<span style="font-size: 90%;">But I get your point</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:59 UTC</span>

<span style="font-size: 90%;">Is not releasing an LTS a statement we believe this is really tested in production and we think it works. Here it's more like we ran the unit tests and we think it's OK.
We can always update the LTS of course, but I feel a bit uneasy.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:51 UTC</span>

<span style="font-size: 90%;">You could argue that. I did not get that impression from the USP guys. But there may be different opinions.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:48:54 UTC</span>

<span style="font-size: 90%;">Without reading through 20+ PRs, what is the general nature of what has been merged lately? Substantial changes, quality of life fixes, something else?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:49:04 UTC</span>

<span style="font-size: 90%;">If it's lots of little QoL things then that seems ok</span>

**azurit** <span style="color: grey; font-size: 90%;">19:50:11 UTC</span>

<span style="font-size: 90%;">Not only QoL.</span>

**michela** <span style="color: grey; font-size: 90%;">19:50:11 UTC</span>

<span style="font-size: 90%;">I think perhaps what matters most in this is what a LTS means to CRS. It's really a commitment to maintain a certain version of CRS for a longer period of time. So, any issues with these newer rules can be sorted in subsequent releases for the LTS, and some rules could even be removed if need be. At the same time, LTS releases are typically well tested and do not contain elements that are likely to be problematic for users. </span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:12 UTC</span>

<span style="font-size: 90%;">A bit of a mix of everything. But some interesting ones from Vincent, I believe.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:00 UTC</span>

<span style="font-size: 90%;">Yes. But as _@dune73_ said, we can always decide to postpone by a month or two.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:07 UTC</span>

<span style="font-size: 90%;">I'm very impressed by the work and I do not want to sound like I'm complaining. But I try to get a clear understanding where the project is going.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:38 UTC</span>

<span style="font-size: 90%;">Most of you that have production setups can run the new release and report back</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:41 UTC</span>

<span style="font-size: 90%;">Let me install this. Should at least give me some feeling.</span>

**michela** <span style="color: grey; font-size: 90%;">19:53:04 UTC</span>

<span style="font-size: 90%;">I'll deploy the latest release to a few production environments at least, but that is still a pretty small scale production test. </span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:47 UTC</span>

<span style="font-size: 90%;">Same here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:04 UTC</span>

<span style="font-size: 90%;">_@azurit_, are you installing too?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:54:16 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:54:50 UTC</span>

<span style="font-size: 90%;">I can install it on few servers but not on my whole infrastructure, as i'm still not (fully) on v4.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:35 UTC</span>

<span style="font-size: 90%;">Thanks. Testing these changes in the real world will help a lot.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:14 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:56:16 UTC</span>

<span style="font-size: 90%;">Any other topics to discuss?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:56:52 UTC</span>

<span style="font-size: 90%;">Plenty of but none is CRS related. :P</span>

**michela** <span style="color: grey; font-size: 90%;">19:57:58 UTC</span>

<span style="font-size: 90%;">The latest Heated Rivalry episodes, _@azurit_ ?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:58:51 UTC</span>

<span style="font-size: 90%;">You got me, never heard of it. :smile:</span>

**michela** <span style="color: grey; font-size: 90%;">19:59:25 UTC</span>

<span style="font-size: 90%;">Oh, check it out! It's a phenomenon. Also, it's Canadian!  :flag-ca: </span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:42 UTC</span>

<span style="font-size: 90%;">If there's nothing else, I would like to thank _@jit_ for all the work he's put into the project over the last couple years. He's announced that he will be stepping back from the project. He will still try and contribute from time to time, but certainly not in the volume he has been.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:00:53 UTC</span>

<span style="font-size: 90%;">Is it about Santa stealing food from grocery stores? :stuck_out_tongue_winking_eye::stuck_out_tongue_winking_eye:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:01:08 UTC</span>

<span style="font-size: 90%;">Thank you _@jit_. Hopefully we'll still see you around from time to time.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:02:15 UTC</span>

<span style="font-size: 90%;">_@jit_ Thanks!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:31 UTC</span>

<span style="font-size: 90%;">On that note, let's close for tonight.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:44 UTC</span>

<span style="font-size: 90%;">Thanks for showing up and see you in a couple of weeks</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:02:48 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**azurit** <span style="color: grey; font-size: 90%;">20:02:58 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:05 UTC</span>

<span style="font-size: 90%;">Good night and bye</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:06 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:09 UTC</span>

<span style="font-size: 90%;">Night!</span>

**jit** <span style="color: grey; font-size: 90%;">20:03:24 UTC</span>

<span style="font-size: 90%;">Goodnight!</span>

**michela** <span style="color: grey; font-size: 90%;">20:04:09 UTC</span>

<span style="font-size: 90%;">_@azurit_, to answer your question: not exactly. It's partly about hockey, and the guys are much hotter than Santa. :slightly_smiling_face:</span>

**azurit** <span style="color: grey; font-size: 90%;">20:05:00 UTC</span>

<span style="font-size: 90%;">Probably not something i'm going to enjoy. :stuck_out_tongue_winking_eye:</span>

