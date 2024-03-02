### Mon, Jan 8th, 2024

**jit** <span style="color: grey; font-size: 90%;">19:31:03 UTC</span>

<span style="font-size: 90%;">Hi everyone :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:08 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:13 UTC</span>

<span style="font-size: 90%;">Hello everying, welcome to the meeting!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:28 UTC</span>

<span style="font-size: 90%;">Please find our agenda at [https://github.com/coreruleset/coreruleset/issues/3466](https://github.com/coreruleset/coreruleset/issues/3466)</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:32:14 UTC</span>

<span style="font-size: 90%;">Hi :wave:</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:32:27 UTC</span>

<span style="font-size: 90%;">Good evening 

</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:33 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**airween** <span style="color: grey; font-size: 90%;">19:32:38 UTC</span>

<span style="font-size: 90%;">hi there</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:45 UTC</span>

<span style="font-size: 90%;">Hey</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:32:59 UTC</span>

<span style="font-size: 90%;">Good evening! :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:26 UTC</span>

<span style="font-size: 90%;">Hello everybody, especially _@jit_ and _@Esad Cetiner_ who make the night their day with their participation!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:12 UTC</span>

<span style="font-size: 90%;">I hope you all had a good start with the new year. It will be very exciting for CRS since we're going to release v4!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:19 UTC</span>

<span style="font-size: 90%;">There is a notice in the agenda about the future of ModSecurity and how TW is now actively seeking an open source community. Please expect some news in the near future.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:40 UTC</span>

<span style="font-size: 90%;">Looking through the project news reads a bit like end-of-the year break, but _@maxleske_ has been hacking away as usual. I'd like to highlight that the new changelog update process will making future releases a lot easier as we'll continually update the changelog now (instead of the several hundred updates high pile for CRSv4).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:15 UTC</span>

<span style="font-size: 90%;">Then positive numbers for our financial accounts despite two sponsors dropping out relatively late in the year and we just lost another one for 2024. So finding new sponsors or renew sponsorship partnerships will be a priority this year (namely for me). If you have any contacts or you see a prospect sponsor, then please get in touch. This will - among other things - decide about the developer retreat 2024.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:13 UTC</span>

<span style="font-size: 90%;">Anything else to add to the news section?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:47 UTC</span>

<span style="font-size: 90%;">Then let's move on to the project discussions. We need to decide on a general regex pattern for multi-byte characters.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:12 UTC</span>

<span style="font-size: 90%;">_@xanadu_ and _@maxleske_ discussed this in [https://github.com/coreruleset/coreruleset/issues/3325](https://github.com/coreruleset/coreruleset/issues/3325) and we have a proposal by Max.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:37 UTC</span>

<span style="font-size: 90%;">Could you guys describe the problem (briefly :)) and the proposed solution (and alternative ones if they exist).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:43:32 UTC</span>

<span style="font-size: 90%;">We currently do a bad job with detecting multi-byte characters (e.g. UTF-8).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">They are a problem especially when used in character classes, like [abc`] .</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:24 UTC</span>

<span style="font-size: 90%;">Because PCRE by default deals with ASCII characters only, the backtick in the example would be interpreted as multiple bytes, something like [abc\xbe\xef]</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:40 UTC</span>

<span style="font-size: 90%;">That, however, is not equivalent, because that would match any character from that class, so \xef , for example.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:46:59 UTC</span>

<span style="font-size: 90%;">But what we actually wanted to match was the sequence \xbe\xef.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">The proposal fixes that issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:34 UTC</span>

<span style="font-size: 90%;">Would `  be matched at all?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:01 UTC</span>

<span style="font-size: 90%;">Yes, depending on the rest of the expression, since the first byte would match</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:38 UTC</span>

<span style="font-size: 90%;">I see. How widespread is the problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:48 UTC</span>

<span style="font-size: 90%;">Currently, not at all.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:48:54 UTC</span>

<span style="font-size: 90%;">2 rules IIRC</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:03 UTC</span>

<span style="font-size: 90%;">Phew. I was getting worried.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:09 UTC</span>

<span style="font-size: 90%;">So no CRSv4 showstopper.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:34 UTC</span>

<span style="font-size: 90%;">How does the solution look?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:49:46 UTC</span>

<span style="font-size: 90%;">They're all ugly :sweat_smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:01 UTC</span>

<span style="font-size: 90%;">True :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:50:27 UTC</span>

<span style="font-size: 90%;">The most portable one, IMO, is the one I proposed. It requires additions to the crs-toolchain.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:25 UTC</span>

<span style="font-size: 90%;">I understand that solution as follows: You take the multi-byte char out of the character class and make it a regex group that you concatenate as alternative via |? Correct?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:51:39 UTC</span>

<span style="font-size: 90%;">Correct</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:23 UTC</span>

<span style="font-size: 90%;">If we think non-European languages: Is this a pattern that would work for everything UTF-8 out there?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:52:56 UTC</span>

<span style="font-size: 90%;">I don't see, why not, assuming Unicode.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:49 UTC</span>

<span style="font-size: 90%;">Ugliness aside, I never saw how we could seriously work with non-European languages, but this idea makes it look like a solution that would at least work on the technical level.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:19 UTC</span>

<span style="font-size: 90%;">And the idea would then be to write the RA-Files in a more or less standard way and the crs-toolchain transposes this into the ugly regexes?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:55:05 UTC</span>

<span style="font-size: 90%;">Yes, we could use multi-byte characters, if we wanted.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:55:55 UTC</span>

<span style="font-size: 90%;">For added context: this conversation started when a CRS user reported a false positive for certain Chinese characters. The current situation is that 1 or 2 rules cause FPs with many, many random Unicode characters, so lots of FPs in Chinese, Japanese, Korean, etc.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:56:13 UTC</span>

<span style="font-size: 90%;">So addressing this issue should reduce FPs for those languages in CRS v4.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:21 UTC</span>

<span style="font-size: 90%;">Exactly!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">However, this only works if we adopt a great many regexes beyond the 2 rules in question. Correct?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:48 UTC</span>

<span style="font-size: 90%;">Or how do the Chinese FPs and this relate exactly. Or all the FPs on these rules?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:44 UTC</span>

<span style="font-size: 90%;">I think it's only 2 (maybe 3?) rules where we use multi-byte chars at the moment. So, _@maxleske_'s proposal would only require adjusting those 2 or 3 regexes (right?)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:18 UTC</span>

<span style="font-size: 90%;">And that solves the entire non-EU language FP problem? I expected it to be much worse.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:46 UTC</span>

<span style="font-size: 90%;">_@jit_ can you put this in perspective from your viewpoint?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">20:21:13 UTC</span>

<span style="font-size: 90%;">Yup, will do. Need to do tests of my own first.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:50 UTC</span>

<span style="font-size: 90%;">I'm pretty sure there are other issues but the FPs should be taken somewhat taken care of</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:09 UTC</span>

<span style="font-size: 90%;">Absolutely.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:23 UTC</span>

<span style="font-size: 90%;">Do we have an alternative approach that solves the problem for these 2-3 rules?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:27 UTC</span>

<span style="font-size: 90%;">3 currently:
</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:50 UTC</span>

<span style="font-size: 90%;">Option 2 and 3 are PCRE specific, I presume?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:03:58 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:08 UTC</span>

<span style="font-size: 90%;">So Hyperscan and RE2 are out?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:41 UTC</span>

<span style="font-size: 90%;">Very likely</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:55 UTC</span>

<span style="font-size: 90%;">Then let's not go down that lane.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:04 UTC</span>

<span style="font-size: 90%;">What's wrong with t:utf8toUnicode ?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:05:49 UTC</span>

<span style="font-size: 90%;">It uses an encoding scheme from IIS: %u<byte1><byte2></span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:18 UTC</span>

<span style="font-size: 90%;">It doesn't scale, but at least it would be supported by all engines that support the transformation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:06:45 UTC</span>

<span style="font-size: 90%;">Oh, there's another problem with that that I just realised</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:48 UTC</span>

<span style="font-size: 90%;">It's also not standard, so you couldn't copy the regex and run it with regex101, for example</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:06:56 UTC</span>

<span style="font-size: 90%;">It probably does not support anything above U+FFFF</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:07:01 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:07:07 UTC</span>

<span style="font-size: 90%;">So only up to 3-byte UTF-8 characters.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:14 UTC</span>

<span style="font-size: 90%;">So it's not really a generic solution.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:32 UTC</span>

<span style="font-size: 90%;">And the only generic solution you guys have found yet is the one laid down above?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:07:55 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:21 UTC</span>

<span style="font-size: 90%;">Chances are this brings a bit of a performance hit. What do you think?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:08:37 UTC</span>

<span style="font-size: 90%;">No, shouldn't have any impact on performance</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:10:00 UTC</span>

<span style="font-size: 90%;">I'll add some numbers on required changes and performance in the issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:28 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:56 UTC</span>

<span style="font-size: 90%;">I do not see any downside outside of harder to read regex / ugliness. Other opinions?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:11:39 UTC</span>

<span style="font-size: 90%;">Not much here. As long as we keep being compatible....</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:11:58 UTC</span>

<span style="font-size: 90%;">We would need to strictly enforce clear documentation as regexes with patterns like \xE2\x12\x34\x56 become incomprehensible</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:12:11 UTC</span>

<span style="font-size: 90%;">Another thing that I would do is to have a wishlist for engines to implement :smiley:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:12:13 UTC</span>

<span style="font-size: 90%;">Unless clearly stating what each pattern is, why is it there, etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:18 UTC</span>

<span style="font-size: 90%;">So we do this, while maintaining excellent documentation what is happening in these regexes?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:41 UTC</span>

<span style="font-size: 90%;">What do you mean?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:55 UTC</span>

<span style="font-size: 90%;">See _@xanadu_</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:26 UTC</span>

<span style="font-size: 90%;">Oh, you asked for confirmation?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:42 UTC</span>

<span style="font-size: 90%;">I sincerely hope that we can adopt threads in the future</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:46 UTC</span>

<span style="font-size: 90%;">I thought you were asking "what happens to the regexes"</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:15:07 UTC</span>

<span style="font-size: 90%;">Threads are difficult to follow and conversations get lost :shrug:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:16:02 UTC</span>

<span style="font-size: 90%;">(At least that is the case for the big monthly group discussions.)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:55 UTC</span>

<span style="font-size: 90%;">I do not see any opposition to the generic solution, so I conclude we have adopted this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:03 UTC</span>

<span style="font-size: 90%;">Does this need the v4 label?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:18:39 UTC</span>

<span style="font-size: 90%;">From my point of view, we can add this later</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:02 UTC</span>

<span style="font-size: 90%;">But it's a bypass on two rules, right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:11 UTC</span>

<span style="font-size: 90%;">No, FPs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:18 UTC</span>

<span style="font-size: 90%;">Ah, excellent</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:29 UTC</span>

<span style="font-size: 90%;">Then ship it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:38 UTC</span>

<span style="font-size: 90%;">Yes, let's add it later. It's a nuisance, but otherwise we never get v4 out the door.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:19:57 UTC</span>

<span style="font-size: 90%;">Which brings us to v4 and the 15 open issues (plus 2-3 bypasses in the private security tracker).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:06 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+label%3Av4](https://github.com/coreruleset/coreruleset/issues?q=is%3Aissue+is%3Aopen+label%3Av4)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:57 UTC</span>

<span style="font-size: 90%;">The good news from the quantitative testing is that it's not that bad. We can concentrate on the highest offenders there for the release and be done with it (if you ask me and that's also what the quantitative testing issues says).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:23 UTC</span>

<span style="font-size: 90%;">The question now is how to assign the 15 open issues / how to make sure this is being done in the coming weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:55 UTC</span>

<span style="font-size: 90%;">We have lost a lot of time in November and December over various discussions that did not bring is much closer to v4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:20 UTC</span>

<span style="font-size: 90%;">We have 3 bugs, 7 FPs and the rest is mostly administrative.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:23:21 UTC</span>

<span style="font-size: 90%;">I don't think we need to assign them. We can simply decide to focus on that list and whoever starts working on an item assigns themselves.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:29 UTC</span>

<span style="font-size: 90%;">I'm all for that solution.
But I would feel better if there was a real commitment form the team.
After Nov and Dec, I'm not really sure we have many volunteers.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">(I tried to get down to issues business last week, but I was busy with financial accounts, sponsoring newsletter, etc.)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:07 UTC</span>

<span style="font-size: 90%;">Well, I'm committed, just had to take a couple of days off over the new year. I'll try to put in a couple of hours each week.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:27:11 UTC</span>

<span style="font-size: 90%;">I can work on issues. I have to find out what issues can be taken, but I'll find out (some are already "in progress")</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:27:29 UTC</span>

<span style="font-size: 90%;">I'll try to push forward the things I've opened.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:35 UTC</span>

<span style="font-size: 90%;">_@jit_ is now working on the bypasses he discovered.
I see _@Matteo Pace_ is hacking away too. Do you have a focus on v4 labelled items?</span>

↳ **jit** <span style="color: grey; font-size: 90%;">20:32:33 UTC</span>

<span style="font-size: 90%;">Looks like I'll be fixing the bypasses then. :)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:30:22 UTC</span>

<span style="font-size: 90%;">Nope. I wanted to commit to what I said I would have done. But the PR is ready, so I can redirect the focus on v4 items from now on</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:37 UTC</span>

<span style="font-size: 90%;">Thank you _@Matteo Pace_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:07 UTC</span>

<span style="font-size: 90%;">Then let me ask Azurit tomorrow as well and with that workforce, we should get this over in a reasonable timeframe.</span>

**jit** <span style="color: grey; font-size: 90%;">20:32:33 UTC</span>

<span style="font-size: 90%;">Looks like I'll be fixing the bypasses then. :)</span>

↳ **jit** <span style="color: grey; font-size: 90%;">20:32:33 UTC</span>

<span style="font-size: 90%;">Looks like I'll be fixing the bypasses then. :)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:57 UTC</span>

<span style="font-size: 90%;">Personally, I do not see a need for a RC3. We got little feedback and I would not expect more after an RC3. And no big release-critical bugs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:05 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:34:21 UTC</span>

<span style="font-size: 90%;">I've been running CRSv4 RC2 for about a month and it's been going fine for me so far, I did find another FP which I'll open a PR for after the set one gets merged.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:48 UTC</span>

<span style="font-size: 90%;">So an somewhat optimistic trajectory is we have most issues sorted out in 2 weeks - at the next meeting - and can start the countdown for CRS v4 at that meeting.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:36:10 UTC</span>

<span style="font-size: 90%;">That would be nice :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:54 UTC</span>

<span style="font-size: 90%;">Indeed.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:16 UTC</span>

<span style="font-size: 90%;">Anything else to discuss tonight?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:43 UTC</span>

<span style="font-size: 90%;">Then thank you all for attending and good luck going forward!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:52 UTC</span>

<span style="font-size: 90%;">bb!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:39:56 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**jit** <span style="color: grey; font-size: 90%;">20:40:00 UTC</span>

<span style="font-size: 90%;">Goodnight everyone</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">20:40:18 UTC</span>

<span style="font-size: 90%;">good night everyone, thanks!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:40:25 UTC</span>

<span style="font-size: 90%;">Good Morning!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:40:33 UTC</span>

<span style="font-size: 90%;">Good night and bye bye :wave:
[https://github.com/coreruleset/coreruleset/issues/3466#issuecomment-1881762255](https://github.com/coreruleset/coreruleset/issues/3466#issuecomment-1881762255)</span>

**airween** <span style="color: grey; font-size: 90%;">20:41:48 UTC</span>

<span style="font-size: 90%;">good night!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:42:17 UTC</span>

<span style="font-size: 90%;">Good night!</span>

