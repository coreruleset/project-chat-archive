### Mon, May 4th, 2020

**walter** <span style="color: grey; font-size: 90%;">18:30:00 UTC</span>

<span style="font-size: 90%;">hello all!</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:32 UTC</span>

<span style="font-size: 90%;">I have only 30 minutes this time, so I hope to be as useful as possible within that timebox</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">18:31:52 UTC</span>

<span style="font-size: 90%;">hello everybody :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:04 UTC</span>

<span style="font-size: 90%;">Then we better rush! Welcome everybody. Is it the 6 of us, or who is here too?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:25 UTC</span>

<span style="font-size: 90%;">May the 4th be with us</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:34:54 UTC</span>

<span style="font-size: 90%;">no star wars emoji's :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:44 UTC</span>

<span style="font-size: 90%;">I'll just start right away to save time: [#1707](https://github.com/coreruleset/coreruleset/issues/#1707): _@walter_ did you have the opportunity to check this in prod?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:12 UTC</span>

<span style="font-size: 90%;">You said you would test and merge.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">18:34:16 UTC</span>

<span style="font-size: 90%;">hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:21 UTC</span>

<span style="font-size: 90%;">Hi Mirko!</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:40 UTC</span>

<span style="font-size: 90%;">I have tested this and found no false positives. At the other hand, I also didn’t find any hits. But, I’ll merge it now. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:59 UTC</span>

<span style="font-size: 90%;">thank you</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:38 UTC</span>

<span style="font-size: 90%;">and the same goes for [#1734](https://github.com/coreruleset/coreruleset/issues/#1734), i’ve run this in production for about 4 weeks with no reports of FP</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:37:10 UTC</span>

<span style="font-size: 90%;">My customer said they only tested on test systems, not on prod yet...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:13 UTC</span>

<span style="font-size: 90%;">[#1708](https://github.com/coreruleset/coreruleset/issues/#1708): It seems this discussion is still ongoing between _@airween_ and _@Mirko Dziadzka_. Anything to say about the status here?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:31 UTC</span>

<span style="font-size: 90%;">_@franbuehler_: is this 1734 or 1707?</span>

**airween** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">not from me :disappointed:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:37:45 UTC</span>

<span style="font-size: 90%;">1734</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:37:47 UTC</span>

<span style="font-size: 90%;">sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:52 UTC</span>

<span style="font-size: 90%;">thanks _@franbuehler_</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">18:38:54 UTC</span>

<span style="font-size: 90%;">regarding [#1708](https://github.com/coreruleset/coreruleset/issues/#1708) - I like to understand why the more complex regex is faster. Until now, it seem that the order of groups has changed. This may be a result of this perl module to commbine regex, but I didn't checked it yet</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:57 UTC</span>

<span style="font-size: 90%;">I just measured the performance of different regexes, and found that in case of 942210 the first fix is faster</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:31 UTC</span>

<span style="font-size: 90%;">but there aren't the regex.data changes for first commit</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:57 UTC</span>

<span style="font-size: 90%;">So can we conclude that you guys will look into this some more? Ideally we can merge between here and June, or we are too late for 3.3 release.</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:07 UTC</span>

<span style="font-size: 90%;">summary: we need more time; and I wrote there we should re-open a new PR</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:21 UTC</span>

<span style="font-size: 90%;">that makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:21 UTC</span>

<span style="font-size: 90%;">_@airween_: Do you need the contact email for Allan?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">18:40:23 UTC</span>

<span style="font-size: 90%;">should happen in May, yes</span>

**airween** <span style="color: grey; font-size: 90%;">18:40:57 UTC</span>

<span style="font-size: 90%;">I think I have email for Allan, we're emailing before in private in another topics (modsec)</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:27 UTC</span>

<span style="font-size: 90%;">just didn't wanted to disturb - guess he see the notifications from GH</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:15 UTC</span>

<span style="font-size: 90%;">Good. I hope you guys can sort this out. Can I note down that the two of you  will try to merge or open a new PR & merge during May?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">18:42:33 UTC</span>

<span style="font-size: 90%;">ok</span>

**airween** <span style="color: grey; font-size: 90%;">18:42:47 UTC</span>

<span style="font-size: 90%;">sure</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:51 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:05 UTC</span>

<span style="font-size: 90%;">[#1710](https://github.com/coreruleset/coreruleset/issues/#1710) is ready to be merged, I see.</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:22 UTC</span>

<span style="font-size: 90%;">but don't forget, there are still another one rule with this effect, and there is no issue about that</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:42 UTC</span>

<span style="font-size: 90%;">Please open an issue ...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:43:56 UTC</span>

<span style="font-size: 90%;">yes for 1710</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:24 UTC</span>

<span style="font-size: 90%;">[#1734](https://github.com/coreruleset/coreruleset/issues/#1734) and [#1735](https://github.com/coreruleset/coreruleset/issues/#1735) seem equally ready for merging. Any opposition?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:45:01 UTC</span>

<span style="font-size: 90%;">not from my side</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:04 UTC</span>

<span style="font-size: 90%;">merge!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:33 UTC</span>

<span style="font-size: 90%;">How about [#1738](https://github.com/coreruleset/coreruleset/issues/#1738)? (-> rule exclusions)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:35 UTC</span>

<span style="font-size: 90%;">Do it!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:39 UTC</span>

<span style="font-size: 90%;">Hmm</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:12 UTC</span>

<span style="font-size: 90%;">totally ready to merge :wink:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:12 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:18 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:23 UTC</span>

<span style="font-size: 90%;">1738 is difficult for us to test. It's Walter's business.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:25 UTC</span>

<span style="font-size: 90%;">1738 and 1739 are extension to existing rule exclusions by @Waler.Nobody checked, but I think we can merge them nevertheless. Not so dangerous here.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:46:26 UTC</span>

<span style="font-size: 90%;">So, yes, merge</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:10 UTC</span>

<span style="font-size: 90%;">Cool. So it's a bit of a merge-fest tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:22 UTC</span>

<span style="font-size: 90%;">[#1740](https://github.com/coreruleset/coreruleset/issues/#1740) is more tricky, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:38 UTC</span>

<span style="font-size: 90%;">This on hold until we hear from _@fgs_ again?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:22 UTC</span>

<span style="font-size: 90%;">1740 touches the same rule as 1748.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:48:38 UTC</span>

<span style="font-size: 90%;">I would merge 1748 first and then rebase and change the 1740 PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:08 UTC</span>

<span style="font-size: 90%;">Would that solve any open issues with 1740 (sorry, I'm a bit out of the loop here)?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:49:58 UTC</span>

<span style="font-size: 90%;">No, but indeed, I could solve the case sensitive issue in this same PR 1748</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:25 UTC</span>

<span style="font-size: 90%;">So the situation for 1740 just gets cleaner after 1748 is merged?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:39 UTC</span>

<span style="font-size: 90%;">CT header is sooo complex.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:50:57 UTC</span>

<span style="font-size: 90%;">They touch the same rule, the same line in the file.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:51:05 UTC</span>

<span style="font-size: 90%;">But solve another problem...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:39 UTC</span>

<span style="font-size: 90%;">I see. So I just note that 1748 comes first and we'll see afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:42 UTC</span>

<span style="font-size: 90%;">OK?</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:56 UTC</span>

<span style="font-size: 90%;">makes sense</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:12 UTC</span>

<span style="font-size: 90%;">yes.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:15 UTC</span>

<span style="font-size: 90%;">it’s a bit of a pity that [#1748](https://github.com/coreruleset/coreruleset/issues/#1748) changes the format of a configuration setting, is that the only way to solve the problem?</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:29 UTC</span>

<span style="font-size: 90%;">e.g people have to (potentially) make a change to their crs-setup.conf</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:35 UTC</span>

<span style="font-size: 90%;">maybe we should note this in release notes of some kind…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:48 UTC</span>

<span style="font-size: 90%;">We'll definitely have to note that, yes.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:52:52 UTC</span>

<span style="font-size: 90%;">Yes, that's true. I didnt' think about that.
But it's the only solution I found.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:53:21 UTC</span>

<span style="font-size: 90%;">I had to use the
@within</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:22 UTC</span>

<span style="font-size: 90%;">I think most people will leave this setting alone though, and those who change it area already pretty hardcore</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:53:55 UTC</span>

<span style="font-size: 90%;">operator because rx behaves differently on v2 and v3.</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:06 UTC</span>

<span style="font-size: 90%;">ugh yeah</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:54:07 UTC</span>

<span style="font-size: 90%;">I hope, I'm right, _@airween_??</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:12 UTC</span>

<span style="font-size: 90%;">well, I think the solution is very nice :)</span>

**airween** <span style="color: grey; font-size: 90%;">18:54:13 UTC</span>

<span style="font-size: 90%;">yes, absolutely</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">I think we can do with a note in the release notes. As Walter says, this is for hardcore users.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:54:40 UTC</span>

<span style="font-size: 90%;">And when I use the within operator I had to insert delimiters...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:04 UTC</span>

<span style="font-size: 90%;">Of course, we can also complain about different behaviours in v2 and v3.... That's always an option, but brought no progress so far.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:55:14 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:50 UTC</span>

<span style="font-size: 90%;">Basically [#1748](https://github.com/coreruleset/coreruleset/issues/#1748) is ready to be merged, then?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:12 UTC</span>

<span style="font-size: 90%;">It works on my machine</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:13 UTC</span>

<span style="font-size: 90%;">:wink:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:54 UTC</span>

<span style="font-size: 90%;">I could ask a customer to test it for a week or two?</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:23 UTC</span>

<span style="font-size: 90%;">I think a defect in this rule would probably show up in test traffic quickly!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:33 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:57:55 UTC</span>

<span style="font-size: 90%;">Do we want to wait for two weeks or so?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:13 UTC</span>

<span style="font-size: 90%;">So we merge and pray for heavy tests for 3.3 PR 1?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:22 UTC</span>

<span style="font-size: 90%;">RC 1 I meant</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:29 UTC</span>

<span style="font-size: 90%;">Yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:53 UTC</span>

<span style="font-size: 90%;">And what I would like so say: Thank you _@airween_ for your great support!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:20 UTC</span>

<span style="font-size: 90%;">OK, so let's merge. The tests are passing after all. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:38 UTC</span>

<span style="font-size: 90%;">looks good to me!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:59:44 UTC</span>

<span style="font-size: 90%;">Great, thank you. I will work on 1740 then again!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:52 UTC</span>

<span style="font-size: 90%;">[#1742](https://github.com/coreruleset/coreruleset/issues/#1742): I think we should say thank you in a polite way, but drop this. It is not our job to fix FPs in recommended rules. Even it is annoying from a user perspective.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:04 UTC</span>

<span style="font-size: 90%;">Even if it is (sorry)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:02:07 UTC</span>

<span style="font-size: 90%;">Yes, we would mix CRS and recommended rules here...</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:00 UTC</span>

<span style="font-size: 90%;">oh but I do know his pain</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:16 UTC</span>

<span style="font-size: 90%;">rule 200002 is such a pain in the ass, and I do exclude it in WordPress IIRC</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:27 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:35 UTC</span>

<span style="font-size: 90%;">basically everything that accepts uploads is liable to get this on a ‘weird’ filename</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:54 UTC</span>

<span style="font-size: 90%;">so I won’t mind excluding 200002</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:04 UTC</span>

<span style="font-size: 90%;">just to be practical</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:43 UTC</span>

<span style="font-size: 90%;">so I think this PR would be good, if it fits the style, there was some comment about that</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:54 UTC</span>

<span style="font-size: 90%;">200004 is far worse when you live next to French speakers.</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:19 UTC</span>

<span style="font-size: 90%;">thankfully that is rare here :grin:</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:33 UTC</span>

<span style="font-size: 90%;">the rule hit, I mean</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:24 UTC</span>

<span style="font-size: 90%;">L'application.docx uploaded in IE is a deadsure FP around here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:23 UTC</span>

<span style="font-size: 90%;">So who agrees with @Walter on 200002 in the Nextcould rules.
I mean it is true that we should put the users first and they do not give a damn who provided those stupid rules.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:27 UTC</span>

<span style="font-size: 90%;">Tough one</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:09:14 UTC</span>

<span style="font-size: 90%;">Yes, tough one</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:17 UTC</span>

<span style="font-size: 90%;">I'm really torn.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:39 UTC</span>

<span style="font-size: 90%;">I think that it provides a good point on our side.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:17 UTC</span>

<span style="font-size: 90%;">But I think the order should be different</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:33 UTC</span>

<span style="font-size: 90%;">I would match the REQUEST_FILENAME first</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:26 UTC</span>

<span style="font-size: 90%;">Generally yes, but given you are using Nextcloud and thus webdav and streq is a very fast operator...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:41 UTC</span>

<span style="font-size: 90%;">It is also very easy to read that way.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:56 UTC</span>

<span style="font-size: 90%;">Well, this will provide a benefit for our users</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:04 UTC</span>

<span style="font-size: 90%;">So I would say yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:15 UTC</span>

<span style="font-size: 90%;">So we accept and merge. Final opposition?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:12:23 UTC</span>

<span style="font-size: 90%;">No, I can live with it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:24 UTC</span>

<span style="font-size: 90%;">Even when mixing is difficult to digest</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:01 UTC</span>

<span style="font-size: 90%;">merge :ok_hand:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:31 UTC</span>

<span style="font-size: 90%;">OK. We merge.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:54 UTC</span>

<span style="font-size: 90%;">[#1743](https://github.com/coreruleset/coreruleset/issues/#1743) is by the same contributor. I'd say we merge.</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:56 UTC</span>

<span style="font-size: 90%;">I have to fly right now, it was a short but very mergeable session, good luck!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:09 UTC</span>

<span style="font-size: 90%;">Good night, @Walter. Thank you.</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">19:14:19 UTC</span>

<span style="font-size: 90%;">Bye walter</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:03 UTC</span>

<span style="font-size: 90%;">Any opinions on 1743?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:15:13 UTC</span>

<span style="font-size: 90%;">bye Walter</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:05 UTC</span>

<span style="font-size: 90%;">I think we merge 1743</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:06 UTC</span>

<span style="font-size: 90%;">looks good</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:11 UTC</span>

<span style="font-size: 90%;">yes!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:15 UTC</span>

<span style="font-size: 90%;">Seems clear than the other</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:30 UTC</span>

<span style="font-size: 90%;">okidoki. Another merge.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:42 UTC</span>

<span style="font-size: 90%;">[#1744](https://github.com/coreruleset/coreruleset/issues/#1744) is a docker fix.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">If that is the real syntax, we should merge</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">Isn't that BACKEND now?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:18:41 UTC</span>

<span style="font-size: 90%;">Hi all! I'm finally coming back to home after 2 month, sorry! I read all asap</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:03 UTC</span>

<span style="font-size: 90%;">Hello _@theMiddle_ - so good to see you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:04 UTC</span>

<span style="font-size: 90%;">I also find PROXYLOCATION :see_no_evil:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:25 UTC</span>

<span style="font-size: 90%;">This is a mess</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:30 UTC</span>

<span style="font-size: 90%;">Yes it is!!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:32 UTC</span>

<span style="font-size: 90%;">the crs container has UPSTREAM</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:36 UTC</span>

<span style="font-size: 90%;">I will check this one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:42 UTC</span>

<span style="font-size: 90%;">But the modsecurity-docker has BACKEND</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:46 UTC</span>

<span style="font-size: 90%;">Doesn't make sense</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:47 UTC</span>

<span style="font-size: 90%;">If we continue with the meeting for long enough, I'm sure _@fgs_ and _@emphazer_ will also join...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:50 UTC</span>

<span style="font-size: 90%;">I use PROXYLOCATION for owasp/modsecurity-crs:v3.2-modsec2-apache</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:20:01 UTC</span>

<span style="font-size: 90%;">:open_mouth:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:20:06 UTC</span>

<span style="font-size: 90%;">So 3 names for the same</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:13 UTC</span>

<span style="font-size: 90%;">So we assign _@franbuehler_ for review?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:20:25 UTC</span>

<span style="font-size: 90%;">Yes! They should have used my first proposal and don't change it!!!!!!!!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:20:45 UTC</span>

<span style="font-size: 90%;">Yes, I will investigate it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:20:54 UTC</span>

<span style="font-size: 90%;">(I normally use BACKEND)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:09 UTC</span>

<span style="font-size: 90%;">UPSTREAM seems to come from nginx</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:21:17 UTC</span>

<span style="font-size: 90%;">I think that is what I used too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">But I don't mind as we are consistent</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:59 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:46 UTC</span>

<span style="font-size: 90%;">[#1745](https://github.com/coreruleset/coreruleset/issues/#1745) is a welcome nobrainer by @arween I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:48 UTC</span>

<span style="font-size: 90%;">Merge?</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:53 UTC</span>

<span style="font-size: 90%;">yes</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">19:23:00 UTC</span>

<span style="font-size: 90%;">yes please :wink:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:14 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:21 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:51 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">[#1746](https://github.com/coreruleset/coreruleset/issues/#1746): This seems simple  enough, but I think we should still have a formal review. It's a change of a regex after all.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:18 UTC</span>

<span style="font-size: 90%;">Does this scare you?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:57 UTC</span>

<span style="font-size: 90%;">Hello? Is there still anybody around?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">19:28:15 UTC</span>

<span style="font-size: 90%;">yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:28:26 UTC</span>

<span style="font-size: 90%;">I didn't answer, because it's my PR</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:28:35 UTC</span>

<span style="font-size: 90%;">So someone else should review it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:28:49 UTC</span>

<span style="font-size: 90%;">Yes, sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:50 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:59 UTC</span>

<span style="font-size: 90%;">Do we have volunteers for a review?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:12 UTC</span>

<span style="font-size: 90%;">It's a relatively simple ...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:29:23 UTC</span>

<span style="font-size: 90%;">I can do it</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:36 UTC</span>

<span style="font-size: 90%;">thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:08 UTC</span>

<span style="font-size: 90%;">Thanks _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:37 UTC</span>

<span style="font-size: 90%;">And thank you for the comment on the PR _@Mirko Dziadzka_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:36 UTC</span>

<span style="font-size: 90%;">And we come to the final one: [#1750](https://github.com/coreruleset/coreruleset/issues/#1750). Ready 2B merged, I presume.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:49 UTC</span>

<span style="font-size: 90%;">yes!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:06 UTC</span>

<span style="font-size: 90%;">Yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:25 UTC</span>

<span style="font-size: 90%;">I fully trust _@airween_</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:33 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:45 UTC</span>

<span style="font-size: 90%;">as you can see, there isn't so much modifications... :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:51 UTC</span>

<span style="font-size: 90%;">it's very simple</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:06 UTC</span>

<span style="font-size: 90%;">confirmed</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:20 UTC</span>

<span style="font-size: 90%;">just please review my notes about the rules which doesn't get the ver action</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:27 UTC</span>

<span style="font-size: 90%;">Yes, it's just a very long list of changes! But it looks good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:37 UTC</span>

<span style="font-size: 90%;">OK, we're done with the PRs in 63 minutes. And what a list it was. Thank you for all your great contributions.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:10 UTC</span>

<span style="font-size: 90%;">Contributing absolutely nothing to this project in weeks makes me feel very bad, but then seeing how much you all get done is still great.</span>

**airween** <span style="color: grey; font-size: 90%;">19:35:02 UTC</span>

<span style="font-size: 90%;">who will merge the PR's?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:44 UTC</span>

<span style="font-size: 90%;">The decisions are noted. Anybody can do it. Last time _@franbuehler_ executed everything. Which was a relief for me.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:36:03 UTC</span>

<span style="font-size: 90%;">I can do it again.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:11 UTC</span>

<span style="font-size: 90%;">[https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1749#issuecomment-623634756](https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1749#issuecomment-623634756)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:16 UTC</span>

<span style="font-size: 90%;">thank you very much.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:27 UTC</span>

<span style="font-size: 90%;">Migration</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:18 UTC</span>

<span style="font-size: 90%;">So we wanted to migrate our repo, but TW called it off in the last moment in March because they did not like how we wanted it transferred. They prefer a copy and they keep the old one as an archive.</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:15 UTC</span>

<span style="font-size: 90%;">is there any possibility to copy a repository?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:17 UTC</span>

<span style="font-size: 90%;">Meanwhile _@fzipitria_ has invested a lot of brainz into coming up with a very cool script that uses the API to copy all issues from one repo to a new repo while (.... drums roling ....) using the same issues ID!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:38:37 UTC</span>

<span style="font-size: 90%;">Wow! This is great!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">You can see it now</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:54 UTC</span>

<span style="font-size: 90%;">It is below each issue :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">This has now been tested and we are ready to give it another shot. We are aiming for Wed 13 of May.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:11 UTC</span>

<span style="font-size: 90%;">What is the link to the test again?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:39:33 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is a genius!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:39:41 UTC</span>

<span style="font-size: 90%;">[https://github.com/crstest01/owasp-modsecurity-crs](https://github.com/crstest01/owasp-modsecurity-crs)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:49 UTC</span>

<span style="font-size: 90%;">This is very impressive. Also: I love the nice migration bot that works for us.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:00 UTC</span>

<span style="font-size: 90%;">Everything is in the [https://github.com/fzipi/crs-migration](https://github.com/fzipi/crs-migration) repo</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:16 UTC</span>

<span style="font-size: 90%;">There we have all the steps in the future migration</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:49 UTC</span>

<span style="font-size: 90%;">Please let me know if you see something fishy, or the order should be different, or whatever you want</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:04 UTC</span>

<span style="font-size: 90%;">I think it would be worthwhile to really check this out.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:16 UTC</span>

<span style="font-size: 90%;">If we make a mistake now, we might suffer for a long time.</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:23 UTC</span>

<span style="font-size: 90%;">sorry guys, I'm so tired and I dont feel good. Have to go.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">Good night _@airween_, thanks for joining and your great work!</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:52 UTC</span>

<span style="font-size: 90%;">take care, bye!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:19 UTC</span>

<span style="font-size: 90%;">good night Ervin!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:41 UTC</span>

<span style="font-size: 90%;">_@nerrehmit_ or _@theMiddle_: Do you think you could look through the issues and see if the copying worked?</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">19:46:01 UTC</span>

<span style="font-size: 90%;">sure, I can give it a go :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:24 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:38 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ What else do you think needs checking?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:17 UTC</span>

<span style="font-size: 90%;">I think that PRs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:29 UTC</span>

<span style="font-size: 90%;">I mean, we explicitly choose to create an issue</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:38 UTC</span>

<span style="font-size: 90%;">Tracking PRs is a complex process</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:06 UTC</span>

<span style="font-size: 90%;">So I ended up using issues to point to original PRs, just to not lose those</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:24 UTC</span>

<span style="font-size: 90%;">I guess that's more or less about it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:55 UTC</span>

<span style="font-size: 90%;">It's going to be difficult to check the 1749 migrated ones</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:09 UTC</span>

<span style="font-size: 90%;">I just think that a few dozens getting close scrutiny should turn up any blatant issues.
Subtle issues are unlikely to cause much pain as most issues are closed anyways.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:31 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:45 UTC</span>

<span style="font-size: 90%;">_@nerrehmit_ Thank you very much. I suggest you look through all the open PRs, most open issues and then maybe 10 closed issues or so.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:59 UTC</span>

<span style="font-size: 90%;">Thank you in advance.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:19 UTC</span>

<span style="font-size: 90%;">btw: Ideally until the end of the week, so _@fzipitria_ still gets some time to fix things.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:40 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">19:53:01 UTC</span>

<span style="font-size: 90%;">sounds good. When was the sync last performed _@fzipitria_ so that I know which differences are ok (because they were created in the meantime)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:49 UTC</span>

<span style="font-size: 90%;">Yesterday</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:53 UTC</span>

<span style="font-size: 90%;">Up to 1749</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:03 UTC</span>

<span style="font-size: 90%;">(Today's agenda)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:47 UTC</span>

<span style="font-size: 90%;">Very cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:58 UTC</span>

<span style="font-size: 90%;">Is there anything else under "other issues"?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:55:42 UTC</span>

<span style="font-size: 90%;">no</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:20 UTC</span>

<span style="font-size: 90%;">Nope</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:21 UTC</span>

<span style="font-size: 90%;">I get the feeling we are losing touch with some of our developers.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:58 UTC</span>

<span style="font-size: 90%;">Yes, what happened?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:08 UTC</span>

<span style="font-size: 90%;">Federico is hardly attending anymore as is Chaim. All for good reasons of course and maybe that's just how life develops. But it is painful for the project...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:45 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:59:02 UTC</span>

<span style="font-size: 90%;">yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:39 UTC</span>

<span style="font-size: 90%;">Well, let's wait and see the new normal, as they say</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:18 UTC</span>

<span style="font-size: 90%;">Do you think there anything wrong from your side, or is it just that we need to look for more / new developers as we are likely to have a turnover of like 20-30% per year?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:03 UTC</span>

<span style="font-size: 90%;">I think that it is difficult to keep the engagement up all the time</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:31 UTC</span>

<span style="font-size: 90%;">And that we are lucky to have you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:40 UTC</span>

<span style="font-size: 90%;">Agreed. Hence the turnover</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:43 UTC</span>

<span style="font-size: 90%;">:blush:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:02:09 UTC</span>

<span style="font-size: 90%;">Some of them will come, but others not so much</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:10 UTC</span>

<span style="font-size: 90%;">I can assure you that I have a very hard time of letting go of projects. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:18 UTC</span>

<span style="font-size: 90%;">Yes, that's true. I think without _@dune73_ the project would not move so fast and maybe would stop..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:05 UTC</span>

<span style="font-size: 90%;">Or somebody else would fill the void. Anybody can be replaced if there is enough interest. It's just that we have been growing for 3-4 years and now we started to shrink again.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:31 UTC</span>

<span style="font-size: 90%;">Yes, this is true. Do we want to talk about this in the next meeting?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:36 UTC</span>

<span style="font-size: 90%;">Like having a meta-meeting??</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:46 UTC</span>

<span style="font-size: 90%;">And I think if I was more active as an ambassdor we could recruit more developers. But I am buried in other stuff.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:50 UTC</span>

<span style="font-size: 90%;">Talk about this problem I mean</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:01 UTC</span>

<span style="font-size: 90%;">We could schedule it under "other issues"</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:04:10 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:04:29 UTC</span>

<span style="font-size: 90%;">It's difficult to recruit more developers, isn't it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:04:46 UTC</span>

<span style="font-size: 90%;">We can think about other aspects we want to tackle</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:01 UTC</span>

<span style="font-size: 90%;">Or how to engage with the community</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:42 UTC</span>

<span style="font-size: 90%;">For a long time living below trustwave's umbrella has limited adding people</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:05:58 UTC</span>

<span style="font-size: 90%;">It has been more open recently</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:18 UTC</span>

<span style="font-size: 90%;">And I hope moving will give the project a better visibility</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:21 UTC</span>

<span style="font-size: 90%;">True. Swimming free from TW might help in this regard.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:39 UTC</span>

<span style="font-size: 90%;">OK, let's schedule a talk about this for the next meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:52 UTC</span>

<span style="font-size: 90%;">So we move to the open issues?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:06:58 UTC</span>

<span style="font-size: 90%;">Yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:17 UTC</span>

<span style="font-size: 90%;">Ooookk...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:22 UTC</span>

<span style="font-size: 90%;">We have 41 open and a few ones will get closed after we merge several PRs, I reckon.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:16 UTC</span>

<span style="font-size: 90%;">_@nerrehmit_ has already volunteered for review work. I am working day and night for things beyond my control already, so Iwon't take on more issues.
_@Mirko Dziadzka_ Are you still around and willing to volunteer for one or two issues?</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:09:35 UTC</span>

<span style="font-size: 90%;">Still here.</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:09:49 UTC</span>

<span style="font-size: 90%;">Yes, assign someone to me. I can make a PR</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:10:02 UTC</span>

<span style="font-size: 90%;">s/someone/something/</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:33 UTC</span>

<span style="font-size: 90%;">Thank you. That's most welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:17 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ and _@fzipitria_: do you have capacity to take on something (on top)?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:39 UTC</span>

<span style="font-size: 90%;">I would try</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:44 UTC</span>

<span style="font-size: 90%;">Yes, I'll try. I'm looking through the list.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:31 UTC</span>

<span style="font-size: 90%;">Volunteering for issues is best :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:05 UTC</span>

<span style="font-size: 90%;">Through the list of open issues...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:06 UTC</span>

<span style="font-size: 90%;">Now that migration just needs to be done, I can open up</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:14:14 UTC</span>

<span style="font-size: 90%;">There are not many anymore. The bot is wonderful!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:28 UTC</span>

<span style="font-size: 90%;">I'm self-assigning 1751. All it takes is an explanation I guess. Maybe a better comment on the rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:16:29 UTC</span>

<span style="font-size: 90%;">I'll assign myself to 1736</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:58 UTC</span>

<span style="font-size: 90%;">I will take 1666. It's probably a lot of work...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:29 UTC</span>

<span style="font-size: 90%;">Maybe we can give [#1737](https://github.com/coreruleset/coreruleset/issues/#1737) to _@walter_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:47 UTC</span>

<span style="font-size: 90%;">[#1666](https://github.com/coreruleset/coreruleset/issues/#1666): Yes, I wonder how this came about. I thought I had filled the gaps for 3.2 already.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:17:57 UTC</span>

<span style="font-size: 90%;">Ah, really?!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:12 UTC</span>

<span style="font-size: 90%;">Yes. At least my memory tells me so.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:21 UTC</span>

<span style="font-size: 90%;">Well I will have a look at it!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:31 UTC</span>

<span style="font-size: 90%;">Please remind me to look through my test traffic and see if I have true positives for these rules.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:08 UTC</span>

<span style="font-size: 90%;">1737 to Walter, yes, why not. if he has the time...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:25 UTC</span>

<span style="font-size: 90%;">We can at least try...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:31 UTC</span>

<span style="font-size: 90%;">yes!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:08 UTC</span>

<span style="font-size: 90%;">@Mirko:Would you be so kind and take on 1727?</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:20:11 UTC</span>

<span style="font-size: 90%;">I started looking at 1666 and at least some of them do indeed lack a yaml file in the regression tests</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:20:32 UTC</span>

<span style="font-size: 90%;">forgot to add, looked at the issue a couple month back before someone else voluntered to take over</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:39 UTC</span>

<span style="font-size: 90%;">The guy called me in the issue but I never even responded. :sweat:</span>

**Mirko Dziadzka** <span style="color: grey; font-size: 90%;">20:21:09 UTC</span>

<span style="font-size: 90%;">I can look at [https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1727](https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1727)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:15 UTC</span>

<span style="font-size: 90%;">Do you want to take 1666, _@nerrehmit_??</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">I can take 1711</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:21:45 UTC</span>

<span style="font-size: 90%;">self-assigned it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:46 UTC</span>

<span style="font-size: 90%;">Thank you _@Mirko Dziadzka_.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:58 UTC</span>

<span style="font-size: 90%;">Thanks _@franbuehler_</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:22:22 UTC</span>

<span style="font-size: 90%;">no lets please leave it with you and I might chime in if I get a free minute. School is a lot of work right now and unfortunately corona is not making things easier</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:53 UTC</span>

<span style="font-size: 90%;">What do you think about [https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1726](https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1726) ?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:03 UTC</span>

<span style="font-size: 90%;">Ok, so I have two new issues. That's good for the moment</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:18 UTC</span>

<span style="font-size: 90%;">And if I have too much time, I'll take another one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:22 UTC</span>

<span style="font-size: 90%;">We chatted about the dos rules</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:37 UTC</span>

<span style="font-size: 90%;">Oh, sorry</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:53 UTC</span>

<span style="font-size: 90%;">???</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:57 UTC</span>

<span style="font-size: 90%;">Will take that one</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:24:02 UTC</span>

<span style="font-size: 90%;">Doesn't make sense at all</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:13 UTC</span>

<span style="font-size: 90%;">I don't think we support 3.0.0 also</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:23 UTC</span>

<span style="font-size: 90%;">Which one is that?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:32 UTC</span>

<span style="font-size: 90%;">1726</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:33 UTC</span>

<span style="font-size: 90%;">Ah 1726.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:51 UTC</span>

<span style="font-size: 90%;">Cool.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:10 UTC</span>

<span style="font-size: 90%;">Thank you everybody for taking on these issues. This looks very promising now!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:19 UTC</span>

<span style="font-size: 90%;">I think that's OK for tonight, is not it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:21 UTC</span>

<span style="font-size: 90%;">?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:26:29 UTC</span>

<span style="font-size: 90%;">It's ok for tonight!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:26:55 UTC</span>

<span style="font-size: 90%;">I will update the agenda issue and then close it.</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:16 UTC</span>

<span style="font-size: 90%;">Thanks a lot!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:21 UTC</span>

<span style="font-size: 90%;">See you next time!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:27:22 UTC</span>

<span style="font-size: 90%;">So have a good night or wonderful day!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:36 UTC</span>

<span style="font-size: 90%;">Thanks everybody!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:27:43 UTC</span>

<span style="font-size: 90%;">Thank you everbody!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:48 UTC</span>

<span style="font-size: 90%;">This was such a clean meeting again.</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:27:56 UTC</span>

<span style="font-size: 90%;">Thanks and have a good day/night :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:59 UTC</span>

<span style="font-size: 90%;">And so productive. We have quite the hang of it now.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:28:07 UTC</span>

<span style="font-size: 90%;">Yes!!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:28:24 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:28:56 UTC</span>

<span style="font-size: 90%;">:wave:</span>

