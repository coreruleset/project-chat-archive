### Mon, May 5th, 2025

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:17 UTC</span>

<span style="font-size: 90%;">Hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:30:44 UTC</span>

<span style="font-size: 90%;">Hello everyone, welcome to the monthly chat</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:30:57 UTC</span>

<span style="font-size: 90%;">Nice to see _@S0obi_ and _@Michela Toscano_ as well :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:43 UTC</span>

<span style="font-size: 90%;">Evening</span>

**S0obi** <span style="color: grey; font-size: 90%;">18:31:52 UTC</span>

<span style="font-size: 90%;">Hello everyone!</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:52 UTC</span>

<span style="font-size: 90%;">'evening!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:12 UTC</span>

<span style="font-size: 90%;">I'll give you a couple of minutes to read through the agenda: [https://github.com/coreruleset/coreruleset/issues/4116](https://github.com/coreruleset/coreruleset/issues/4116)</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:47 UTC</span>

<span style="font-size: 90%;">Can we discuss the issue regarding performance comparison between pmFromFile and regex, first?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:55 UTC</span>

<span style="font-size: 90%;">Sure</span>

**jit** <span style="color: grey; font-size: 90%;">18:33:54 UTC</span>

<span style="font-size: 90%;">Just FYI, there is already some discussion in this issue [https://github.com/coreruleset/coreruleset/issues/3229](https://github.com/coreruleset/coreruleset/issues/3229).</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:34:55 UTC</span>

<span style="font-size: 90%;">IMO it is still a cool idea for a project and blog post</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:35:47 UTC</span>

<span style="font-size: 90%;">But someone has to  do the testing...</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:36:08 UTC</span>

<span style="font-size: 90%;">Yes. Hence why it has not happened since 2023 :slightly_smiling_face:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:36:16 UTC</span>

<span style="font-size: 90%;">It needs someone with time **and** interest.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:39:29 UTC</span>

<span style="font-size: 90%;">I think [msc_retest](https://github.com/digitalwave/msc_retest) could be good to test `@rx` operators. And I can make a similar small tool to emulate `@pmFromFile` operator. The results can be compared...</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:53:07 UTC</span>

<span style="font-size: 90%;">We probably need to add more information on that ticket on the things we want tested.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:53:24 UTC</span>

<span style="font-size: 90%;">E.g. not only time, but also resident memory, etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:42 UTC</span>

<span style="font-size: 90%;">_@jit_, why did you have this question? Is it because of the exception lists?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:39:23 UTC</span>

<span style="font-size: 90%;">Yes, the error and function/classes lists in particular.</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:29 UTC</span>

<span style="font-size: 90%;">I think [msc_retest](https://github.com/digitalwave/msc_retest) could be good to test `@rx` operators. And I can make a similar small tool to emulate `@pmFromFile` operator. The results can be compared...</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:35:47 UTC</span>

<span style="font-size: 90%;">But someone has to  do the testing...</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:36:08 UTC</span>

<span style="font-size: 90%;">Yes. Hence why it has not happened since 2023 :slightly_smiling_face:</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">18:36:16 UTC</span>

<span style="font-size: 90%;">It needs someone with time **and** interest.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:39:29 UTC</span>

<span style="font-size: 90%;">I think [msc_retest](https://github.com/digitalwave/msc_retest) could be good to test `@rx` operators. And I can make a similar small tool to emulate `@pmFromFile` operator. The results can be compared...</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:53:07 UTC</span>

<span style="font-size: 90%;">We probably need to add more information on that ticket on the things we want tested.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:53:24 UTC</span>

<span style="font-size: 90%;">E.g. not only time, but also resident memory, etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:31 UTC</span>

<span style="font-size: 90%;">The exception lists aren't that big though, right? And the regular expression created for them would be pretty minimal (probably). So I'm wondering whether we really need to consider this.
For me it's more about "explicit list" versus "generic pattern". The list is nice to read but needs to be updated, while a good generic expression can live for a long time.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:43:50 UTC</span>

<span style="font-size: 90%;">Some lists may grow over time. For e.g., the SQL errors list, which I can say doesn't covers all databases and their relevant errors.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:44:46 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/blob/main/rules/sql-errors.data](https://github.com/coreruleset/coreruleset/blob/main/rules/sql-errors.data)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:44:58 UTC</span>

<span style="font-size: 90%;">True. For these kinds of lists though, where there's often a lot of text to match, I don't think regular expressions make much sense.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:45:33 UTC</span>

<span style="font-size: 90%;">However, for "import ..." or "...Exception.java", regular expressions make a lot of sense to me.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">18:46:32 UTC</span>

<span style="font-size: 90%;">Still having data for performance penalties in such cases might be helpful. Anyways, airween has suggested to the testing, looking forward to the results. :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:46:56 UTC</span>

<span style="font-size: 90%;">Sure, I'm all for _@xanadu_'s project :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:47:10 UTC</span>

<span style="font-size: 90%;">_@airween_ are you sure you have time?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:48:05 UTC</span>

<span style="font-size: 90%;">Yes, I'm sure. Now I usually take my time with sleeping between midnight and 6am morning.... :slightly_smiling_face:</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:49:10 UTC</span>

<span style="font-size: 90%;">Oh, full 6 hours of sleep? We can use 5 hours from that time :stuck_out_tongue:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:49:47 UTC</span>

<span style="font-size: 90%;">My aim is to reduce this interval - this is why I offered... :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:18 UTC</span>

<span style="font-size: 90%;">As a side note, _@airween_ is currently helming ModSecurity solo. He's juggling a lot of things simultaneously.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:10 UTC</span>

<span style="font-size: 90%;">The next one is a ModSecurity issue, that we might have to handle in CRS: [https://github.com/coreruleset/coreruleset/issues/3696](https://github.com/coreruleset/coreruleset/issues/3696)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:20 UTC</span>

<span style="font-size: 90%;">It may be enough for us to mention the flag in the documentation. What do you think?</span>

**airween** <span style="color: grey; font-size: 90%;">18:51:44 UTC</span>

<span style="font-size: 90%;">Well, just let me notice you: hopefully I'm not alone, because I hope there will be many contributors who sends PR's :slightly_smiling_face:. To be precise I'm alone as a project leader.

Fortunately _@maxleske_ and _@fzipitria_ helped me to make reviews.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:00 UTC</span>

<span style="font-size: 90%;">I read this a few days ago and it seems complicated… Can anyone summarise the decision for CRS to make here?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:53:14 UTC</span>

<span style="font-size: 90%;">It's about the `request-early` compilation flag, right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:53 UTC</span>

<span style="font-size: 90%;">Correct. There's a flag in ModSecurity to _disable_ early processing, i.e., phase 1 will be skipped. This is bad for CRS v4. There's a potential workaround but I'm not sure that it even makes sense to run CRS with early early processing disabled. _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">Yes, that's what we found. But I think the "problem" can be solved easily: if someone uses CRS, don't use this flag (which is not used by default)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:58:07 UTC</span>

<span style="font-size: 90%;">Wait. Is there anyone in the world _not_ using CRS? :scream:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:59:23 UTC</span>

<span style="font-size: 90%;">I receive a newsletter from Atomicorp almost every day - I assume they have customers too :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:31 UTC</span>

<span style="font-size: 90%;">Thanks. So documentation then.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:56:59 UTC</span>

<span style="font-size: 90%;">Yes, I think documenting it is enough.</span>

**airween** <span style="color: grey; font-size: 90%;">18:57:05 UTC</span>

<span style="font-size: 90%;">We can add some notes to ModSecurity documentation, and mention this issue - but I think it's rather a CRS thing.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:57:53 UTC</span>

<span style="font-size: 90%;">Can someone take this and open an issue on GitHub to add the required documentation?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:58:36 UTC</span>

<span style="font-size: 90%;">I can open an issue.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:44 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:26 UTC</span>

<span style="font-size: 90%;">Next up: [https://github.com/coreruleset/coreruleset/pull/4094](https://github.com/coreruleset/coreruleset/pull/4094)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:59 UTC</span>

<span style="font-size: 90%;">The question is, whether to add a stricter sibling for this rule that detects `/inetpub` . Powershell does not require drive letters or backward slashes, so in theory `/inetpub` would be a way to bypass this rule. To avoid false positives, we still require the drive letter in the rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:18 UTC</span>

<span style="font-size: 90%;">This is an IIS specific rule</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:15 UTC</span>

<span style="font-size: 90%;">TBH, I don't know whether `/intepub` would actually work but I think we should assume it does (i.e., there's a way to execute powershell through some attack vector)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:31 UTC</span>

<span style="font-size: 90%;">Is it worth the extra rule?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:27 UTC</span>

<span style="font-size: 90%;">So the new rule would be a copy of 954100 but doesn't require the drive letter?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:03:35 UTC</span>

<span style="font-size: 90%;">pretty much</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:05:07 UTC</span>

<span style="font-size: 90%;">So, a response rule, at PL 2 (or higher), in the IIS-specific file `DATA-LEAKAGES-IIS.conf`. So, probably not everyone will run this… And we think it will be beneficial to IIS folks? Seems like a good idea to have it?</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:05:09 UTC</span>

<span style="font-size: 90%;">It would seem the most prudent action would be to add a rule for `/intepub`.  :thinking_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:13 UTC</span>

<span style="font-size: 90%;">Good point _@xanadu_. It's a response rule that probably will be disabled in many (?) cases.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:35 UTC</span>

<span style="font-size: 90%;">Any takers for opening an issue for that?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:06:54 UTC</span>

<span style="font-size: 90%;">I can open an issue for that too.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:41 UTC</span>

<span style="font-size: 90%;">Next: [https://github.com/coreruleset/coreruleset/pull/4111](https://github.com/coreruleset/coreruleset/pull/4111)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:09:54 UTC</span>

<span style="font-size: 90%;">`self` was reported as a false positive in the RCE rules</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:57 UTC</span>

<span style="font-size: 90%;">From what I found, `self` appears to be a keyword in Tcl and there are some proprietary shells that use Tcl (e.g., one from Cisco).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:03 UTC</span>

<span style="font-size: 90%;">It might be a niche, I'm really not familiar with Tcl. We can remove it IMO, as it's pretty specific and not much used to most of our user base, probably.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:08 UTC</span>

<span style="font-size: 90%;">Opinions?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:12 UTC</span>

<span style="font-size: 90%;">I think we can remove it. The command doesn't seem to be widely used.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:44 UTC</span>

<span style="font-size: 90%;">Yes, remove it</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:14:08 UTC</span>

<span style="font-size: 90%;">Out of curiosity, I didn't see how this could cause false positives. Perhaps I missed that. Does anyone here know?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:36 UTC</span>

<span style="font-size: 90%;"> curl -v  -X POST  [http://localhost](http://localhost)  \
    -H "Content-Type: application/json" \
    -d '{ "name": "text | SELF "  }'</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:44 UTC</span>

<span style="font-size: 90%;">(Value: `Compra a MODULAR ALUMINIO ESTRUCTURAL, STRUT PROFILE PG30 30X30 4 SLOTS | SELF TAPPING SCREW PG30 M1 (42 characters omitted)'</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:08 UTC</span>

<span style="font-size: 90%;">product descriptions. Always a favorite :slightly_smiling_face:</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:15:20 UTC</span>

<span style="font-size: 90%;">haha</span>

**azurit** <span style="color: grey; font-size: 90%;">19:15:28 UTC</span>

<span style="font-size: 90%;">Tcl is really old language. I was scripting IRC bots using it when i was 13 yo.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:50 UTC</span>

<span style="font-size: 90%;">How old are you now? :wink:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:15:58 UTC</span>

<span style="font-size: 90%;">39 :sweat_smile:</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:16:01 UTC</span>

<span style="font-size: 90%;">Sorry, I just followed that ticket link for [#4110](https://github.com/coreruleset/coreruleset/issues/#4110), and I see it now.   :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:08 UTC</span>

<span style="font-size: 90%;">no worries</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:30 UTC</span>

<span style="font-size: 90%;">Ok. _@franbuehler_ do you want to open another issue? :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:16:49 UTC</span>

<span style="font-size: 90%;">Oh, yes, of course :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:06 UTC</span>

<span style="font-size: 90%;">Oh</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:17:09 UTC</span>

<span style="font-size: 90%;">Ah, we already have a PR for it</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:11 UTC</span>

<span style="font-size: 90%;">A side note: as I know F5 uses Tcl for their WAF configuration</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:15 UTC</span>

<span style="font-size: 90%;">Yes :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:06 UTC</span>

<span style="font-size: 90%;">Thanks _@airween_. But would you agree that it's a niche? Also, F5 can take care of themselves. The turned away from CRS, didn't they?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:17 UTC</span>

<span style="font-size: 90%;">No one who can afford an F5 is using CRS :sweat_smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:23 UTC</span>

<span style="font-size: 90%;">:moneybag:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:38 UTC</span>

<span style="font-size: 90%;">(I'm half joking.)</span>

**airween** <span style="color: grey; font-size: 90%;">19:18:51 UTC</span>

<span style="font-size: 90%;">Yes, I just wrote this as "interesting" :slightly_smiling_face:</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:19:05 UTC</span>

<span style="font-size: 90%;">They are using a commercial WAF that uses CRS.  :stuck_out_tongue:</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:09 UTC</span>

<span style="font-size: 90%;">Once I read a post from F5 manager, where they definitely do not recommend use SecLang, because _"it's too complicated"_ - Tcl is much better. (NB: once I made a binding for a library which uses Tcl - and I have to tell you that Tcl is a disgusting :slightly_smiling_face:).

I ended up Tcl topic :stuck_out_tongue:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:01 UTC</span>

<span style="font-size: 90%;">Thanks for the closing words _@airween_ :slightly_smiling_face: I think we're at the end.
Is there anything else you would like to discuss tonight?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:22:01 UTC</span>

<span style="font-size: 90%;">They should choose Lua instead of Tcl.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:22:49 UTC</span>

<span style="font-size: 90%;">No, nothing from my side. Thank you for leading the meeting.</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:22:53 UTC</span>

<span style="font-size: 90%;">I think it would be really hard to know if the use of this command in services running on the Internet is niche or not.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:40 UTC</span>

<span style="font-size: 90%;">Agreed. All can know is that it's not something from the "well known" world.</span>

↳ **Michela Toscano** <span style="color: grey; font-size: 90%;">19:24:46 UTC</span>

<span style="font-size: 90%;">So, it's probably hard to know the risks of allowing it. I'm conflicted on the right way here, myself.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:25:13 UTC</span>

<span style="font-size: 90%;">On the RCE world, what `self` could mean?</span>

↳ **Michela Toscano** <span style="color: grey; font-size: 90%;">19:25:15 UTC</span>

<span style="font-size: 90%;">I wonder how common it is that this triggers false positives.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:25:57 UTC</span>

<span style="font-size: 90%;">Probably rare. On the other hand, I like throwing things out that we don't know anything about.</span>

↳ **Michela Toscano** <span style="color: grey; font-size: 90%;">19:26:18 UTC</span>

<span style="font-size: 90%;">Yah. Maybe by itself, it may not cause harm, without other commands run along with it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:21 UTC</span>

<span style="font-size: 90%;">Ha. Some GUIs were written in TCL/Tk a long time ago.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:35 UTC</span>

<span style="font-size: 90%;">Look how old we all are :smile:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:26:42 UTC</span>

<span style="font-size: 90%;">_"Tell us how old are you without telling us how old are you"_ :smile:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:27:30 UTC</span>

<span style="font-size: 90%;">"When I was young, computer fonts used to be green"</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:29:01 UTC</span>

<span style="font-size: 90%;">Oh, did you have a color TV back then? :stuck_out_tongue:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:25:15 UTC</span>

<span style="font-size: 90%;">Yes, Tk is drawing super-ugly GUIs. :joy:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:26:26 UTC</span>

<span style="font-size: 90%;">Like Windows 3.1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:05 UTC</span>

<span style="font-size: 90%;">Alright, let's close for tonight. Thanks all for attending. Have a good night / day!</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:12 UTC</span>

<span style="font-size: 90%;">GN!</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:27:25 UTC</span>

<span style="font-size: 90%;">Bye for now!  :slightly_smiling_face:</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:27:37 UTC</span>

<span style="font-size: 90%;">Get well, _@dune73_!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:29:04 UTC</span>

<span style="font-size: 90%;">Thanks! Bye!</span>

