### Mon, Jun 1st, 2026

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:36 UTC</span>

<span style="font-size: 90%;">Hey hey :wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:53 UTC</span>

<span style="font-size: 90%;">Welcome to our June monthly chat</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:55 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:30:58 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:04 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:15 UTC</span>

<span style="font-size: 90%;">Nice to see you all</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:31:29 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**jit** <span style="color: grey; font-size: 90%;">18:31:45 UTC</span>

<span style="font-size: 90%;">Hi everyone!</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">heyya'</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:32 UTC</span>

<span style="font-size: 90%;">Just to remember, this month we will have our first LTS patch release by EOM</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:41 UTC</span>

<span style="font-size: 90%;">EOM?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:45 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:59 UTC</span>

<span style="font-size: 90%;">End of Month…?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:07 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:23 UTC</span>

<span style="font-size: 90%;">Nice</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:44 UTC</span>

<span style="font-size: 90%;">We are coordinating some strings with upstream :grin:</span>

**Dan Kegel** <span style="color: grey; font-size: 90%;">18:34:13 UTC</span>

<span style="font-size: 90%;">... upstream?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:28 UTC</span>

<span style="font-size: 90%;">Modsecurity :sunglasses:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:48 UTC</span>

<span style="font-size: 90%;">Beloved friend project</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:17 UTC</span>

<span style="font-size: 90%;">Anyway</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:32 UTC</span>

<span style="font-size: 90%;">We have one big topic for today in our chat</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:36 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4646](https://github.com/coreruleset/coreruleset/issues/4646)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:00 UTC</span>

<span style="font-size: 90%;">Should we enable crs_validate_utf8_encoding by default? Reference: Rule bypassing in PL2 using overlong UTF-8 encodings</span>

**airween** <span style="color: grey; font-size: 90%;">18:36:31 UTC</span>

<span style="font-size: 90%;">Beloved friend projecthaha :smile:</span>

**Dan Kegel** <span style="color: grey; font-size: 90%;">18:37:14 UTC</span>

<span style="font-size: 90%;">sounds good to me.  It's a utf-8 world these days, and the few using something else can disable the rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">Do we expect any fallout? Do we know of large installations who enabled this without problems?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:34 UTC</span>

<span style="font-size: 90%;">What about also recommending it for LTS?</span>

**jit** <span style="color: grey; font-size: 90%;">18:38:38 UTC</span>

<span style="font-size: 90%;">Turns out about 99% of web uses it [https://w3techs.com/technologies/details/en-utf8](https://w3techs.com/technologies/details/en-utf8)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:33 UTC</span>

<span style="font-size: 90%;">I'd rather run this on 4.x before recommending it backwards.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:39:38 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:48 UTC</span>

<span style="font-size: 90%;">Recommending, not enabling</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:38 UTC</span>

<span style="font-size: 90%;">I meant, changing the default for main</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:48 UTC</span>

<span style="font-size: 90%;">But adding words in LTS</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:58 UTC</span>

<span style="font-size: 90%;">I can not recommend on such a thin base of experience.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:14 UTC</span>

<span style="font-size: 90%;">But maybe I'm just uninformed: Do we expect any fallout? Do we know of large installations who enabled this without problems?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:59 UTC</span>

<span style="font-size: 90%;">Do you know people that actually uses utf-16?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:08 UTC</span>

<span style="font-size: 90%;">Unfortunately, yes :disappointed:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:40 UTC</span>

<span style="font-size: 90%;">Well, then we just need to make things clearly publicly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:54 UTC</span>

<span style="font-size: 90%;">Do good communication</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:08 UTC</span>

<span style="font-size: 90%;">And maybe target 4.25.2</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:38 UTC</span>

<span style="font-size: 90%;">Is that bleeding-edge?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:40 UTC</span>

<span style="font-size: 90%;">Or LTS?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:24 UTC</span>

<span style="font-size: 90%;">That's LTS</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:31 UTC</span>

<span style="font-size: 90%;">In 4 months</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:12 UTC</span>

<span style="font-size: 90%;">As we don't seem to have any data one way or the other here, does it make more sense to put changes into bleeding-edge, get feedback from users, and then that data informs future decisions?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:24 UTC</span>

<span style="font-size: 90%;">It feels a little like we don't really know if this will break things or not</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:52 UTC</span>

<span style="font-size: 90%;">Yes of course</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:10 UTC</span>

<span style="font-size: 90%;">Let's do that, and revisit LTS in Q4</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:18 UTC</span>

<span style="font-size: 90%;">Would that work?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:46:30 UTC</span>

<span style="font-size: 90%;">That sounds great</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:39 UTC</span>

<span style="font-size: 90%;">That sounds like a solid plan.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:41 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:25 UTC</span>

<span style="font-size: 90%;">Awesome. So for the decision, we'll enable by default now for main, and see if we backport later.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:47:39 UTC</span>

<span style="font-size: 90%;">I'll write it down.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:07 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:14 UTC</span>

<span style="font-size: 90%;">That's all we had for tonight</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:28 UTC</span>

<span style="font-size: 90%;">Hold on</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:29 UTC</span>

<span style="font-size: 90%;">Thanks everyone, and see you next one!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:34 UTC</span>

<span style="font-size: 90%;">What about Vienna?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:44 UTC</span>

<span style="font-size: 90%;">Who's coming? Any plans for the evenings?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:52 UTC</span>

<span style="font-size: 90%;">Where are the best parties?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:59 UTC</span>

<span style="font-size: 90%;">What's the latest program for the WAF day?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:09 UTC</span>

<span style="font-size: 90%;">I'm posting that this week</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">Any plans for the evenings?:beer:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:44 UTC</span>

<span style="font-size: 90%;">And will repost on OWASP</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:50 UTC</span>

<span style="font-size: 90%;">_@airween_ how long will you stay?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:50 UTC</span>

<span style="font-size: 90%;">For better reach</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:13 UTC</span>

<span style="font-size: 90%;">Who else is coming?</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:24 UTC</span>

<span style="font-size: 90%;">I hope I can arrive on Tuesday evening, and will leave on Thursday late afternoon/evening</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:34 UTC</span>

<span style="font-size: 90%;">so two nights</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:51:25 UTC</span>

<span style="font-size: 90%;">I don't know yet. First, I planned to come, but now I'm not sure anymore... I need to make a decision soon...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:41 UTC</span>

<span style="font-size: 90%;">Ah, I thought you booked already. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:50 UTC</span>

<span style="font-size: 90%;">At least I have my ticket for the conference.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:05 UTC</span>

<span style="font-size: 90%;">No, no bookings yet.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:09 UTC</span>

<span style="font-size: 90%;">I'll be there from Tuesday night until Saturday or Sunday.</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:45 UTC</span>

<span style="font-size: 90%;">Do we want to book a common accommodation?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:12 UTC</span>

<span style="font-size: 90%;">Let me know if you want to</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:25 UTC</span>

<span style="font-size: 90%;">I didn't book anything yet</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">But also there is F1 happening</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:52 UTC</span>

<span style="font-size: 90%;">But do you plan to attend, _@fzipitria_?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:58 UTC</span>

<span style="font-size: 90%;">F1 as in car race?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:04 UTC</span>

<span style="font-size: 90%;">May have to book then soon. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:11 UTC</span>

<span style="font-size: 90%;">Yes. Not attending the race.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">Same here, I will likely be there, but I haven’t booked anything yet. I’m still waiting for one confirmation</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:02 UTC</span>

<span style="font-size: 90%;">That race is 200km from Vienne. I doubt there is any fallout.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:13 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:25 UTC</span>

<span style="font-size: 90%;">I'll see what I can do, no promises</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:32 UTC</span>

<span style="font-size: 90%;">[https://www.redbullring.com/de/anreise/](https://www.redbullring.com/de/anreise/)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:04 UTC</span>

<span style="font-size: 90%;">For the common accomodation: let me know until when I have to decide...</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:44 UTC</span>

<span style="font-size: 90%;">or at least we should choose a district where we will be close to each other (and close to the conference center)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:01 UTC</span>

<span style="font-size: 90%;">Where is the conf center anyways? I did not check yet.</span>

**airween** <span style="color: grey; font-size: 90%;">18:59:46 UTC</span>

<span style="font-size: 90%;">Austria Center
Bruno-Kreisky-Platz 1
Wien, Austria</span>

**airween** <span style="color: grey; font-size: 90%;">18:59:51 UTC</span>

<span style="font-size: 90%;">[https://owasp.glueup.com/event/owasp-global-appsec-eu-2026-vienna-austria-162243/](https://owasp.glueup.com/event/owasp-global-appsec-eu-2026-vienna-austria-162243/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:42 UTC</span>

<span style="font-size: 90%;">Sounds good. Looking forward to see you there.</span>

**jit** <span style="color: grey; font-size: 90%;">19:02:47 UTC</span>

<span style="font-size: 90%;">It's OWASP's silver jubilee :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:50 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:25 UTC</span>

<span style="font-size: 90%;">Sounds like we're done. Good night everybody.</span>

**jit** <span style="color: grey; font-size: 90%;">19:11:03 UTC</span>

<span style="font-size: 90%;">Good night everyone! :night_with_stars:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:34 UTC</span>

<span style="font-size: 90%;">Night!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:43 UTC</span>

<span style="font-size: 90%;">Good night everyone.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:35 UTC</span>

<span style="font-size: 90%;">Good night</span>

**airween** <span style="color: grey; font-size: 90%;">19:16:12 UTC</span>

<span style="font-size: 90%;">GN!</span>

