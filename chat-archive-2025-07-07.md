### Mon, Jul 7th, 2025

**maxleske** <span style="color: grey; font-size: 90%;">18:30:37 UTC</span>

<span style="font-size: 90%;">Hi everyone, welcome to the monthly chat.</span>

**jit** <span style="color: grey; font-size: 90%;">18:30:39 UTC</span>

<span style="font-size: 90%;">Hi everyone :wave: </span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:42 UTC</span>

<span style="font-size: 90%;">Hello</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:46 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:30:48 UTC</span>

<span style="font-size: 90%;">Greetings</span>

**airween** <span style="color: grey; font-size: 90%;">18:30:57 UTC</span>

<span style="font-size: 90%;">Good evening!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:31:14 UTC</span>

<span style="font-size: 90%;">G'day</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:14 UTC</span>

<span style="font-size: 90%;">Here's the agenda for today's chat, please take a couple of minutes to read it: [https://github.com/coreruleset/coreruleset/issues/4184](https://github.com/coreruleset/coreruleset/issues/4184)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">Hello, hello!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:39 UTC</span>

<span style="font-size: 90%;">:wave: :blob-wave: :pikachu_wave:</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:15 UTC</span>

<span style="font-size: 90%;">Guys, can we start with issue [#4149](https://github.com/coreruleset/coreruleset/issues/#4149)</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">18:32:49 UTC</span>

<span style="font-size: 90%;">Hi!  :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:11 UTC</span>

<span style="font-size: 90%;">Hi Michela!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:21 UTC</span>

<span style="font-size: 90%;">So let's get started with [https://github.com/coreruleset/coreruleset/issues/4149](https://github.com/coreruleset/coreruleset/issues/4149)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:49 UTC</span>

<span style="font-size: 90%;">If I'm not mistaken, the size limitation is in fact a line length limitation that was lifted in Apache 2.4.8. This was still a thing in RedHat by the time we released 3.0.0. But I think the rules can be concatenated now. Obviously, we ought to do a test and all. And maybe I am overlooking something.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:58 UTC</span>

<span style="font-size: 90%;">That would be great. If that were the case, would we need to remain backwards compatible though?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:10 UTC</span>

<span style="font-size: 90%;">I think there is a size limit still</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:33 UTC</span>

<span style="font-size: 90%;">8192?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:38:56 UTC</span>

<span style="font-size: 90%;">Sounds about right.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Probably [here](https://github.com/apache/httpd/blob/trunk/include/httpd.h#L308)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:37 UTC</span>

<span style="font-size: 90%;">Also, would this effort really be worth it, considering that we want to start generating rules anyway? _@fzipitria_ what's your estimation of when we could get started with that?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:39:18 UTC</span>

<span style="font-size: 90%;">Not in the next two months, probably.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:39:39 UTC</span>

<span style="font-size: 90%;">So if we are eager to solve this, and someone has the time, then it can be reused later</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:40:06 UTC</span>

<span style="font-size: 90%;">true</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:51 UTC</span>

<span style="font-size: 90%;">Yes, there is always a limit. But it's beyond our rules AFAICT. Or maybe I'm just getting old and rusty.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:56 UTC</span>

<span style="font-size: 90%;">Sounds about right.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:38:56 UTC</span>

<span style="font-size: 90%;">Sounds about right.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Probably [here](https://github.com/apache/httpd/blob/trunk/include/httpd.h#L308)?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:40:08 UTC</span>

<span style="font-size: 90%;">Aren't some of the rules already longer than 8192? (I think it was 932236)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:52 UTC</span>

<span style="font-size: 90%;">1.1KB</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:41:12 UTC</span>

<span style="font-size: 90%;">aah nvm</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:41:13 UTC</span>

<span style="font-size: 90%;">Is that the current Apache line length limit?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:25 UTC</span>

<span style="font-size: 90%;">Those rules used to run into the limit, before we started splitting them.</span>

**airween** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Probably [here](https://github.com/apache/httpd/blob/trunk/include/httpd.h#L308)?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">18:38:56 UTC</span>

<span style="font-size: 90%;">Sounds about right.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Probably [here](https://github.com/apache/httpd/blob/trunk/include/httpd.h#L308)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:52 UTC</span>

<span style="font-size: 90%;">Trying to find the issue for the RCE rules that we had to split...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">That was a long, long time ago. I do not even know who had the idea. Probably Walter or me.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:22 UTC</span>

<span style="font-size: 90%;">This would require extending crs-toolchain, right?
And the person asking for this change probably isn't going to do the work on the toolchain.
So, does team CRS see enough benefit in this change for us to do the work?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:42 UTC</span>

<span style="font-size: 90%;">(I hope I haven't over-simplified there)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:33 UTC</span>

<span style="font-size: 90%;">The only two benefits I can think are: documenting it, and doing it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:55 UTC</span>

<span style="font-size: 90%;">Even if we have a full documentation on the problem that's a start</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:53 UTC</span>

<span style="font-size: 90%;">I can see the benefit of the automation but i don't see it outweighing the effort of implementation. Especially not with rule generation on the horizon.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:49:31 UTC</span>

<span style="font-size: 90%;">I still want to figure out, what the limit was. I'll take care of that and then respond to the issue. _@franbuehler_ are you taking the notes?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:49:46 UTC</span>

<span style="font-size: 90%;">Yes, I'm taking the notes.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:23 UTC</span>

<span style="font-size: 90%;">Let's move on to [https://github.com/coreruleset/coreruleset/pull/4179](https://github.com/coreruleset/coreruleset/pull/4179)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:49 UTC</span>

<span style="font-size: 90%;">As explained in the issue, this rule is part of a family and there is already a stricter sibling at PL3. The PR does not take that into account.

The limit of 12 special chars is somewhat arbitrary, but I used to run some tests like 8 years ago and the PL2: 12; PL3: 6; PL4: 2 was the result of these tests.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:09 UTC</span>

<span style="font-size: 90%;">These rules are annoying. Very much so. But also on the attacker.</span>

**airween** <span style="color: grey; font-size: 90%;">18:54:30 UTC</span>

<span style="font-size: 90%;">Just a quick note for [#4149](https://github.com/coreruleset/coreruleset/issues/#4149): I tried now with a long line (the length was 8212 bytes), and Apache allowed it...</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:55:04 UTC</span>

<span style="font-size: 90%;">Cool, let's document the max size in a ticket and let's see what can we do</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:55:40 UTC</span>

<span style="font-size: 90%;">I try to figure out what's the max length (if there is any limit)</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:55:01 UTC</span>

<span style="font-size: 90%;">they're also only a warning, those rules alone aren't enough to block a request unless you set the anomaly score threshold to 3 or lower</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:38 UTC</span>

<span style="font-size: 90%;">I would not have this rule or one from the family at PL1. But at PL2, it serves a very clear purpose: Whatever wizadry you are trying to pull off, it's likely involving a lot of special chars and we do not like that on this server.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:15 UTC</span>

<span style="font-size: 90%;">It might depend on the traffic?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:23 UTC</span>

<span style="font-size: 90%;">What about graphql or other stuff?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:56:55 UTC</span>

<span style="font-size: 90%;">If you have 12+ special chars in your input (e.g. a Markdown comment / blog post etc.) then you'll hit this rule and must tune it. But also with such traffic you hit many other rules, so tuning is inevitable.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:14 UTC</span>

<span style="font-size: 90%;">Probably all very painful. Thus rule exclusions. At PL2, where they have to be expected.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:57:15 UTC</span>

<span style="font-size: 90%;">And at PL2 already anyway, as noted above.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:58:22 UTC</span>

<span style="font-size: 90%;">I haven't seen anyone else complaining about this rule yet. We should ask:
> why are you impacted when this rule increases the warning score only?
> what kind of traffic are you looking at?
> don't you have other rule exclusions anyway?
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:13 UTC</span>

<span style="font-size: 90%;">I'm also interested in understanding the "why" on the rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:16 UTC</span>

<span style="font-size: 90%;">I think that the rule might still make sense for many users. If that's no longer the case though, we should definitely consider removing it, i.e., if everyone excludes it anyway.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:41 UTC</span>

<span style="font-size: 90%;">Agreed :point_up_2:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:11 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ / _@jit_ you guys have been working on this issue already. Would one of you take this?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:01:26 UTC</span>

<span style="font-size: 90%;">Yes, I can take this one and ask the questions you wrote above. I already have my opinion, I would let the rule at PL2. But let's discuss this with the reporter.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:01:38 UTC</span>

<span style="font-size: 90%;">Great, thanks!</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:03:44 UTC</span>

<span style="font-size: 90%;">I agree that it probably makes sense to leave this rule as is. I also think that if people exclude a rule, hopefully they at least consider confining their exclusion to the area where the false positive is (to a specified URI pattern, for example).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:14 UTC</span>

<span style="font-size: 90%;">Before we move on to the last item, I wanted to let you know that we're thinking about the next Community Call. We have a tentative date, August 18.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:10 UTC</span>

<span style="font-size: 90%;">So, last item: LTS release.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:11 UTC</span>

<span style="font-size: 90%;">We've been postponing an LTS release for quite a while now. I know that at least _@xanadu_ would like to see one soon, and there are probably other people out there that feel the same way.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:34 UTC</span>

<span style="font-size: 90%;">The question is, are we ready yet? If not, what needs to be done to get there? What kind of timeline do we need to consider from the perspective of our users (i.e., can we postpone until the summit?)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:50 UTC</span>

<span style="font-size: 90%;">I would like to hear your opinions.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:22 UTC</span>

<span style="font-size: 90%;">It needs to be a quality release that we can a.) be proud of having in the wild for a long time, and b.) is support-able for a long time.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:04 UTC</span>

<span style="font-size: 90%;">Re-grouping on the outstanding tasks (and having a clear list of 'must-haves') would be good. I think there are some list updates and stuff to finish</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:10:20 UTC</span>

<span style="font-size: 90%;">How long would the LTS be supported for?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:50 UTC</span>

<span style="font-size: 90%;">The OWASP CRS officially supports the two latest point releases with severe security patches.
We are happy to receive and merge PR's that address security issues in older versions of the project, but the team itself may choose not to fix these.
Along those lines, OWASP CRS team may not issue security notifications for unsupported software.</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:11:30 UTC</span>

<span style="font-size: 90%;">Hello
Sorry for jumping in late :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:11:32 UTC</span>

<span style="font-size: 90%;">That's the current policy. I don't know whether we actually have a policy for LTS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:08 UTC</span>

<span style="font-size: 90%;">If you take into account that 3.2 is used still in azure....</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:23 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:31 UTC</span>

<span style="font-size: 90%;">You can imagine that 8-10 years is a reasonable lts</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:55 UTC</span>

<span style="font-size: 90%;">markdown
| Version   | Supported          |
| --------- | ------------------ |
| 4.15.z    | :white_check_mark: |
| 4.14.z    | :white_check_mark: |
| 4.y.z     | :x: |
| 3.3.x     | :white_check_mark: |
| 3.2.x     | :x:                |
| 3.1.x     | :x:                |
| 3.0.x     | :x:                |
| 2.x       | :x:                |</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:18 UTC</span>

<span style="font-size: 90%;">Which is not a good decision for integrators, but anyway</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:24 UTC</span>

<span style="font-size: 90%;">According to our policy, the LTS would remain supported when we move to 5.x.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:50 UTC</span>

<span style="font-size: 90%;">The problem, for me, is that 5.x would be the first generated release...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:24 UTC</span>

<span style="font-size: 90%;">It looks like we first need to have an understanding what we mean by "LTS".</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:04 UTC</span>

<span style="font-size: 90%;">Ideally, I would like to have that discussion together with a plan (and possibly execution) as part of the summit.</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:15:25 UTC</span>

<span style="font-size: 90%;">Are older versions that are still used in LTS distributions sort of "de-facto" LTS releases? In other words, if someone reported a serious used with 3.2 used in Azure, would we make an update to it, or is that something we expect the distributions to address?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:15:33 UTC</span>

<span style="font-size: 90%;">We did all that at Budapest, but there's no harm in having further discussions</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">I found this: [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS). But that doesn't include a definition of "LTS" or a plan. Do you recall something different?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">Something different</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:18:43 UTC</span>

<span style="font-size: 90%;">I think that was a conversation that happened in my absence. I remember specifics being agreed at the 2023 retreat</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:18 UTC</span>

<span style="font-size: 90%;">Honestly, would you use a 10 years old antivirus?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:17 UTC</span>

<span style="font-size: 90%;">Sorry, I need to go. Kid needs my emotional support.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">I found this: [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS). But that doesn't include a definition of "LTS" or a plan. Do you recall something different?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">I found this: [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-2024-Topic:-LTS). But that doesn't include a definition of "LTS" or a plan. Do you recall something different?</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">Something different</span>

↳ **xanadu** <span style="color: grey; font-size: 90%;">19:18:43 UTC</span>

<span style="font-size: 90%;">I think that was a conversation that happened in my absence. I remember specifics being agreed at the 2023 retreat</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:32 UTC</span>

<span style="font-size: 90%;">Nope</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:17:38 UTC</span>

<span style="font-size: 90%;">Right. How relevant would CRS be, if it were 10 years old? Would we recommend people use it, even if it is getting "critical" updates? Also, all things considered, what's the difference between a CRS LTS that gets critical updates and just installing the latest release?</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">The delta is the difference. LTS will receive critical updates but no "new nonsense"</span>

↳ **Michela Toscano** <span style="color: grey; font-size: 90%;">19:19:37 UTC</span>

<span style="font-size: 90%;">haha. Okay. Does "new nonsense" mean new features then?  :blush:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:20:25 UTC</span>

<span style="font-size: 90%;">Yes, potentially.</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:50 UTC</span>

<span style="font-size: 90%;">Honestly, would you use a 10 years old antivirus?I think this is not a fair comparison. Most distribution provide virus database for older binaries.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:20 UTC</span>

<span style="font-size: 90%;">But the database is our rules</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">The delta is the difference. LTS will receive critical updates but no "new nonsense"</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">The delta is the difference. LTS will receive critical updates but no "new nonsense"</span>

↳ **Michela Toscano** <span style="color: grey; font-size: 90%;">19:19:37 UTC</span>

<span style="font-size: 90%;">haha. Okay. Does "new nonsense" mean new features then?  :blush:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:20:25 UTC</span>

<span style="font-size: 90%;">Yes, potentially.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:57 UTC</span>

<span style="font-size: 90%;">New nonsense means that people will adapt to the rules</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:10 UTC</span>

<span style="font-size: 90%;">And I see the value for integrators</span>

**airween** <span style="color: grey; font-size: 90%;">19:19:30 UTC</span>

<span style="font-size: 90%;">_@Michela Toscano_ I think the most of supported LTS distributions use CRS 3.3, which is supported by us. I do't think there is any older CRS in anywhere.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:20:11 UTC</span>

<span style="font-size: 90%;">Azure is 3.2</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:20:45 UTC</span>

<span style="font-size: 90%;">May be - I thought about open source Linux distributions.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:45 UTC</span>

<span style="font-size: 90%;">If you want to invest time into this, it should work for the next 5 years or so</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:30 UTC</span>

<span style="font-size: 90%;">Ok, lts is not for Linux</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:34 UTC</span>

<span style="font-size: 90%;">Is for integrators</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:21:45 UTC</span>

<span style="font-size: 90%;">So, then, 3.3 (and maybe 3.2) are already sort of LTS, it seems.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:58 UTC</span>

<span style="font-size: 90%;">3.3 is the only lts</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:22:00 UTC</span>

<span style="font-size: 90%;">3.3.x is essentially our current LTS</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:28 UTC</span>

<span style="font-size: 90%;">I think distributions would be happy if we covered the CVE's.

From the view of integrators' (like Azure): I have no idea :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:14 UTC</span>

<span style="font-size: 90%;">3.2.x is factually an LTS that is no longer supported by us, but still very much in use with commercial integrators.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:35 UTC</span>

<span style="font-size: 90%;">Then we clearly need a discussion</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:24:16 UTC</span>

<span style="font-size: 90%;">Seems like we have the first item of dev-retreat topics :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:42 UTC</span>

<span style="font-size: 90%;">:grinning:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:09 UTC</span>

<span style="font-size: 90%;">And knocking some doors</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:16 UTC</span>

<span style="font-size: 90%;">Seems like we have the first item of dev-retreat topics :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:24:16 UTC</span>

<span style="font-size: 90%;">Seems like we have the first item of dev-retreat topics :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:47 UTC</span>

<span style="font-size: 90%;">We appear to agree that we're not there yet. I like _@xanadu_'s idea of collecting stuff that we feel needs to go into the LTS. We can create a label on GitHub for that. As for definition and plan, I think that's easy to do at the retreat and pretty hard on Slack / GitHub. So I propose to make that a priority topic for the retreat.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:58 UTC</span>

<span style="font-size: 90%;">Incidentally, there's already a label `v4 LTS` :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:02 UTC</span>

<span style="font-size: 90%;">Does anyone feel that we need to address the LTS issue sooner?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:32 UTC</span>

<span style="font-size: 90%;">We had these discussions and made the necessary labels way back when, it feels a bit like we're going in circles</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:49 UTC</span>

<span style="font-size: 90%;">But it's not _urgent_. It can wait for another discussion in person.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:29:23 UTC</span>

<span style="font-size: 90%;">I agree. I do believe thought that we can get an LTS release out the door at the retreat, given how much v4 has stabilised in the mean time</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:57 UTC</span>

<span style="font-size: 90%;">Now _that_ would be something to shout about as a result from the retreat :grinning:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:30 UTC</span>

<span style="font-size: 90%;">I take that as a yes then :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:20 UTC</span>

<span style="font-size: 90%;">Thanks for your input everyone. Is there anything else you would like to discuss?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:56 UTC</span>

<span style="font-size: 90%;">If not I would like to end the chat with a little rhyme, curtesy of _@xanadu_:

:musical_note: Because web security is a mess
Come and help us develop CRS :notes:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:08 UTC</span>

<span style="font-size: 90%;">Good night everyone, and see you soon!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:20 UTC</span>

<span style="font-size: 90%;">See you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:28 UTC</span>

<span style="font-size: 90%;">Good night and bye</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:33:34 UTC</span>

<span style="font-size: 90%;">Goodbye</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">Cheers! Bye</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:34:05 UTC</span>

<span style="font-size: 90%;">Bye for now!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:18 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4184#issuecomment-3046213071](https://github.com/coreruleset/coreruleset/issues/4184#issuecomment-3046213071)</span>

