### Mon, Feb 15th, 2021

**dune73** <span style="color: grey; font-size: 90%;">19:31:50 UTC</span>

<span style="font-size: 90%;">Hello, hello, it's time for our monthly issue chat. Who's around to join?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:10 UTC</span>

<span style="font-size: 90%;">i’m around</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:15 UTC</span>

<span style="font-size: 90%;">Hi _@csanders_! Good to see you. How is it going?</span>

**airween** <span style="color: grey; font-size: 90%;">19:33:20 UTC</span>

<span style="font-size: 90%;">hi all</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:26 UTC</span>

<span style="font-size: 90%;">Hi _@airween_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:30 UTC</span>

<span style="font-size: 90%;">I reckon Seattle is not quite as cold as Rochester in Winter, or is it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:38 UTC</span>

<span style="font-size: 90%;">Hello _@airween_. Thanks for joining.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:06 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:23 UTC</span>

<span style="font-size: 90%;">Hey _@franbuehler_! Now, we're already the 4 of us.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:27 UTC</span>

<span style="font-size: 90%;">_@csanders_, do you feel like taking on an issue or two yourself? We sure have plenty.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:22 UTC</span>

<span style="font-size: 90%;">We've been in our thirties with the open issues for 2 months or so, but last week we shot over 40 again. I closed a few today, so we are at 37, but it would be good to get below 30 in a stable way.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:41 UTC</span>

<span style="font-size: 90%;">If it's lower than 30, I think we will be able to keep a decent overview and address them as they come in.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:50 UTC</span>

<span style="font-size: 90%;">Or at least that's what I am dreaming of.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">OK, let's start then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:10 UTC</span>

<span style="font-size: 90%;">Our agenda is at [https://github.com/coreruleset/coreruleset/issues/1992](https://github.com/coreruleset/coreruleset/issues/1992)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:20 UTC</span>

<span style="font-size: 90%;">Before we dive into the issues: _@airween_ could you give us your status on the blocking-early feature on ModSecurity3? They way I understand Andrei, we're ready to roll. Or do we need a release of the connector module from Trustwave?</span>

**airween** <span style="color: grey; font-size: 90%;">19:40:18 UTC</span>

<span style="font-size: 90%;">hey all!

no, we don't need to wait, Andrei merged the patch into Nginx connector, so the blocking-early feature can work with v3</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:58 UTC</span>

<span style="font-size: 90%;">But people need to compile an updated connector themselves, don't they?</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:36 UTC</span>

<span style="font-size: 90%;">yes, all user needs to recompile the connector</span>

**airween** <span style="color: grey; font-size: 90%;">19:41:56 UTC</span>

<span style="font-size: 90%;">but imho that's normal</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:09 UTC</span>

<span style="font-size: 90%;">[https://github.com/SpiderLabs/ModSecurity-nginx/issues/238#issuecomment-772778867](https://github.com/SpiderLabs/ModSecurity-nginx/issues/238#issuecomment-772778867)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:34 UTC</span>

<span style="font-size: 90%;">So if we release our blog post, we need to tell the people to re-compile from HEAD. Or can we tell them they only need to recompile under certain conditions?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:14 UTC</span>

<span style="font-size: 90%;">I think the difference is that you can compile a new release, or you can compile from a git checkout. For production policies that makes a big difference in many enterprises.</span>

**airween** <span style="color: grey; font-size: 90%;">19:44:19 UTC</span>

<span style="font-size: 90%;">I think the difference is that you can compile a new release, or you can compile from a git checkout. - yes, it's clear

that's a good question what we should do</span>

**airween** <span style="color: grey; font-size: 90%;">19:45:34 UTC</span>

<span style="font-size: 90%;">I prefer that we need to clarify the situation:
</span>

**airween** <span style="color: grey; font-size: 90%;">19:46:02 UTC</span>

<span style="font-size: 90%;">and it's important, that this is a connector bug, not the library bug</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:01 UTC</span>

<span style="font-size: 90%;">That's all? If yes, I can update the blog post with this, and with the additional description, that switching off the engine in a container no longer works with 3.3.1-RC1 and onwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:10 UTC</span>

<span style="font-size: 90%;">And then we release the blog post during the week.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:12 UTC</span>

<span style="font-size: 90%;">Agreed?</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:23 UTC</span>

<span style="font-size: 90%;">yes, I think that's it - _@theMiddle_, other opinion?</span>

**airween** <span style="color: grey; font-size: 90%;">19:47:33 UTC</span>

<span style="font-size: 90%;">btw I agree</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:09 UTC</span>

<span style="font-size: 90%;">@walter, you around?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:47 UTC</span>

<span style="font-size: 90%;">OK, unless we hear anything else, this is what we're going to do.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:27 UTC</span>

<span style="font-size: 90%;">I have no update on the sponsoring. They have paid the invoice, but they are not reacting to my messages about making an announcement and without the announcement, I feel kind of stalled.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:51 UTC</span>

<span style="font-size: 90%;">So I guess I'll continue to pester them and then we announce and then a new life for CRS starts.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:52:36 UTC</span>

<span style="font-size: 90%;">Thanks for your work on this!!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:19 UTC</span>

<span style="font-size: 90%;">So the first item on the agenda - I just added a few - is 1999. This is an reiteration of known issues around the DoS rules. As I am about to remove those and move them into a separate plugin rule set, I self-assigned this issue.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:51 UTC</span>

<span style="font-size: 90%;">Next one is [#1589](https://github.com/coreruleset/coreruleset/issues/#1589).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:15 UTC</span>

<span style="font-size: 90%;">It brings an idea by _@theMiddle_ that he almost finished into a PR. I think it would be worthwhile to include this into the next major release. On the other hand, I get fed up with the FPs on 920350 and I get the feeling it's time to move the rule to PL2. 1589 is about additional rules as well, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:19 UTC</span>

<span style="font-size: 90%;">Could somebody of you look through this and:
</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:06 UTC</span>

<span style="font-size: 90%;">Any takers?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:15 UTC</span>

<span style="font-size: 90%;">_@csanders_?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:59:37 UTC</span>

<span style="font-size: 90%;">hmmm, I think this one is a bit out of my wheel house</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:51 UTC</span>

<span style="font-size: 90%;">(I checked the developers links on [https://github.com/coreruleset/coreruleset/wiki/Developer-Links](https://github.com/coreruleset/coreruleset/wiki/Developer-Links) and it looks like you need more issues on your plate)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:14 UTC</span>

<span style="font-size: 90%;">OK. Nevermind. Maybe somebody else will pick it up or _@theMiddle_ kicks the can further down the road.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:15 UTC</span>

<span style="font-size: 90%;">I def do L:)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:48 UTC</span>

<span style="font-size: 90%;">Let's move on to [#2007](https://github.com/coreruleset/coreruleset/issues/#2007) then. It's an FP on 942300.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:54 UTC</span>

<span style="font-size: 90%;">Or a few FPs to be exact.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:50 UTC</span>

<span style="font-size: 90%;">In general I like 942xxx issues :slightly_smiling_face:
I can try to resolve it. I have 3 assigned issues which I did not touch (ok one is almost resolved).
I can try and take this 4th issue too.</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:08 UTC</span>

<span style="font-size: 90%;">I can take this on i think if you’re too busy _@franbuehler_</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:04:17 UTC</span>

<span style="font-size: 90%;">Oh, yes, please.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:04 UTC</span>

<span style="font-size: 90%;">Thank you _@csanders_.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:05:12 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:13 UTC</span>

<span style="font-size: 90%;">[#2006](https://github.com/coreruleset/coreruleset/issues/#2006) is an FP on 941120. Information is a bit sparse, but it might be enough, since the payload the alert looks complete.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:53 UTC</span>

<span style="font-size: 90%;">Probably identical with [#1867](https://github.com/coreruleset/coreruleset/issues/#1867) that went stale.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:03 UTC</span>

<span style="font-size: 90%;">I suggest I close 2006 in favor of 1867.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:08:14 UTC</span>

<span style="font-size: 90%;">yes, they seem to have the same problem with base64 encoded strings.</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:08 UTC</span>

<span style="font-size: 90%;">hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:22 UTC</span>

<span style="font-size: 90%;">When I looked into 1867 / 941120 a few weeks ago, I could not see a real solution. What do you think?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:26 UTC</span>

<span style="font-size: 90%;">Hello @walter!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:30 UTC</span>

<span style="font-size: 90%;">Hi _@walter_</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:47 UTC</span>

<span style="font-size: 90%;">didn’t we already fix [#2006](https://github.com/coreruleset/coreruleset/issues/#2006) by including a \b word separator?</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:08 UTC</span>

<span style="font-size: 90%;">this user is on 3.1.0 still</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:20 UTC</span>

<span style="font-size: 90%;">oh, no, we didn’t - I was wrong</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:44 UTC</span>

<span style="font-size: 90%;">we did restrict FPs but his case would still be triggered</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:11:56 UTC</span>

<span style="font-size: 90%;">Yes, there is no easy solution.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:11 UTC</span>

<span style="font-size: 90%;">At least I don't see it</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:50 UTC</span>

<span style="font-size: 90%;">if we exhaustively list the actually existing event handlers, maybe we should move this to PL2</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:13:00 UTC</span>

<span style="font-size: 90%;">This rule seems to be too strict for PL1 matching everything onxxx.</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:00 UTC</span>

<span style="font-size: 90%;">it’s not really necessary one might even argue…</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:23 UTC</span>

<span style="font-size: 90%;">(except for when new event handers are introduced and we lag in adding them)</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:22 UTC</span>

<span style="font-size: 90%;">I’m up for moving this rule to PL2</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:57 UTC</span>

<span style="font-size: 90%;">That would be a solution</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:34 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:16:43 UTC</span>

<span style="font-size: 90%;">I think that makes sense</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:16:49 UTC</span>

<span style="font-size: 90%;">Yes, me too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:05 UTC</span>

<span style="font-size: 90%;">Who does the PR?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:18 UTC</span>

<span style="font-size: 90%;">to just switch it to PL2</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:23 UTC</span>

<span style="font-size: 90%;">yep</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:27 UTC</span>

<span style="font-size: 90%;">I can handle that</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:30 UTC</span>

<span style="font-size: 90%;">great!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:31 UTC</span>

<span style="font-size: 90%;">thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:12 UTC</span>

<span style="font-size: 90%;">Next one is [#2005](https://github.com/coreruleset/coreruleset/issues/#2005). An FP when you submit .. as payload and it triggers a path traversal on 930110.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:34 UTC</span>

<span style="font-size: 90%;">The reporter argues that it should at least come with a slash / backslash in order to trigger.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:38 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:01 UTC</span>

<span style="font-size: 90%;">hmmm, that seems safe to me!</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:27 UTC</span>

<span style="font-size: 90%;">well, unless it’s an API that provides a dirlisting</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:39 UTC</span>

<span style="font-size: 90%;">it would show files up one level in the tree</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:54 UTC</span>

<span style="font-size: 90%;">I have also never seen .. as a legitimate parameter, so it’s a bit of a rare case I presume</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:38 UTC</span>

<span style="font-size: 90%;">The API case is rather rare and I do not think we need to protect against that in PL1.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:46 UTC</span>

<span style="font-size: 90%;">I also never saw ..</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:53 UTC</span>

<span style="font-size: 90%;">If only dot's it's rather 3 of them.</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:10 UTC</span>

<span style="font-size: 90%;">the rule would also get a lot simpler if we’d just turn it into @pm ../ ..\ /.. \..</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:53 UTC</span>

<span style="font-size: 90%;">hmm, that might open up more FPs scratch that!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:45 UTC</span>

<span style="font-size: 90%;">Can we do this without lookaround - or maybe add a chained rule that whitelists ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">Or we tell the user to make a day. :smiling_imp:</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:02 UTC</span>

<span style="font-size: 90%;">or break it up into two sub patterns?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:41 UTC</span>

<span style="font-size: 90%;">The tests are quite comprehensive for the rule btw</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:06 UTC</span>

<span style="font-size: 90%;">yes quite good!</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:21 UTC</span>

<span style="font-size: 90%;">they would fail my quick @pm proposal</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:55 UTC</span>

<span style="font-size: 90%;">shall I do this one?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:12 UTC</span>

<span style="font-size: 90%;">If you volunteer, that would be very nice.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:05 UTC</span>

<span style="font-size: 90%;">I think a more complex regex that enforces at least a slash on the left or one on the right would be doable. Or the chain, idea that might be faster as the chain only executes on payloads that trigger the basic regex.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:40 UTC</span>

<span style="font-size: 90%;">Final one (unless you insist on more issues): 2001</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:43 UTC</span>

<span style="font-size: 90%;">Another FP on 920300. We've been here before. Please read my comment on the issue.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:31:51 UTC</span>

<span style="font-size: 90%;">I very often exclude this rule for end-to-end or API tests. And I also already heard that we (CRS) test on something that's not enforced by an RFC.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:48 UTC</span>

<span style="font-size: 90%;">I think we should kill the rule or move to PL3.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:33:05 UTC</span>

<span style="font-size: 90%;">But on the other hand it could also be a hint for a bad client...</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:09 UTC</span>

<span style="font-size: 90%;">hmm, but it is already in PL2 and we assume people to remedy it</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:22 UTC</span>

<span style="font-size: 90%;">10:SecRuleRemoveById 920300</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:26 UTC</span>

<span style="font-size: 90%;">i see that I remove it in my config ;’0</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:06 UTC</span>

<span style="font-size: 90%;">It's just a lot of people. And if Chrome does it by default, what are we to trigger an alert for it. I mean what's the point if everybody has to disable it?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:34:27 UTC</span>

<span style="font-size: 90%;">For me it would be ok to remove the rule...</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:54 UTC</span>

<span style="font-size: 90%;">I don’t understand why he got the alert because Chrome sends UA Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 so it does include AppleWebKit</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:42 UTC</span>

<span style="font-size: 90%;">This on the other hand is a good question.</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:52 UTC</span>

<span style="font-size: 90%;">unless chrome doesn’t do that for download links..</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:12 UTC</span>

<span style="font-size: 90%;">I suspect ModSecurity here (haven’t heard back from our customer yet whether they use it or not, and whether that’s the culprit here)</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:23 UTC</span>

<span style="font-size: 90%;">so it’s not fully clear if we were the ones blocking it…</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:44 UTC</span>

<span style="font-size: 90%;">I can’t reproduce when I reenable the rule</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:32 UTC</span>

<span style="font-size: 90%;">Me neither, I admit. But I would not be surprised for Chrome to skip UA when it skips Accept as well.</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:46 UTC</span>

<span style="font-size: 90%;">can confirm it sends normal UA to me</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:10 UTC</span>

<span style="font-size: 90%;">But either way, the rule pops up again and again and I am constantly updating the rule exclusion on this one for [netnea.com](http://netnea.com)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:39:48 UTC</span>

<span style="font-size: 90%;">I could write the PR (removal of the rule) because I would make some people happy with it :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:03 UTC</span>

<span style="font-size: 90%;">from my git logs, I disabled the rule because PHP SoapClient does not respect it</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:22 UTC</span>

<span style="font-size: 90%;">and we have a lot of SOAP clients</span>

**walter** <span style="color: grey; font-size: 90%;">20:41:26 UTC</span>

<span style="font-size: 90%;">so, I still suspect this person is not actually hitting this rule…  but the usefulness of the rule can be debated</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:06 UTC</span>

<span style="font-size: 90%;">I'm +1 on removing the rule. Given we are adding rules with every release, there is nothing wrong with removing rules that cause too much pain.</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:22 UTC</span>

<span style="font-size: 90%;">I wouldn’t mind removing the rule</span>

**airween** <span style="color: grey; font-size: 90%;">20:42:49 UTC</span>

<span style="font-size: 90%;">moving it to PL3 is better choice IMHO</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:52 UTC</span>

<span style="font-size: 90%;">or moving it to PL3 since the rule in itself does what it says, and can be useful</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:21 UTC</span>

<span style="font-size: 90%;">PL3 is fine with me as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:32 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ you are not running PL3, or are you?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:43:45 UTC</span>

<span style="font-size: 90%;">PL4.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:53 UTC</span>

<span style="font-size: 90%;">So would your peers still be happy with this rule shifted to a higher PL?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:00 UTC</span>

<span style="font-size: 90%;">PL4?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:02 UTC</span>

<span style="font-size: 90%;">Really?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:44:09 UTC</span>

<span style="font-size: 90%;">Yes, PL4.</span>

**airween** <span style="color: grey; font-size: 90%;">20:44:16 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ is a hero</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:44:18 UTC</span>

<span style="font-size: 90%;">No, not really, but it's ok.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:44:33 UTC</span>

<span style="font-size: 90%;">:grin:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:41 UTC</span>

<span style="font-size: 90%;">PL4 is almost the same as killing the rule, so I am OK.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:03 UTC</span>

<span style="font-size: 90%;">PL 3 is fine for me. It doesn't matter PL3 or 4 for me.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:23 UTC</span>

<span style="font-size: 90%;">(-> bring a  rule to the issue chat and anything can happen! We call it the rule roulette!)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:35 UTC</span>

<span style="font-size: 90%;">So who does the PR?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:44 UTC</span>

<span style="font-size: 90%;">I can do it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:49 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:51 UTC</span>

<span style="font-size: 90%;">Move to PL3??</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:03 UTC</span>

<span style="font-size: 90%;">Your call. Those who do the work get to make the decisions.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:30 UTC</span>

<span style="font-size: 90%;">I don't like decisions :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:33 UTC</span>

<span style="font-size: 90%;">But we will of course do a full review of your PR afterwards and tell you to change to PL.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:46:42 UTC</span>

<span style="font-size: 90%;">Hahaha</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:45 UTC</span>

<span style="font-size: 90%;">s/to/the/</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:03 UTC</span>

<span style="font-size: 90%;">I think the number of issues assigned in the issue chat should depend on the number of people attending. So from my point of view, we're good.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:12 UTC</span>

<span style="font-size: 90%;">OK if we close this?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:48:46 UTC</span>

<span style="font-size: 90%;">And if you are bored, look at this teaser of Swiss Cyber Storm in a nutshell:
[https://www.youtube.com/watch?v=5-vuhYwqMEQ&feature=emb_logo](https://www.youtube.com/watch?v=5-vuhYwqMEQ&feature=emb_logo)
Sharing welcome.</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:46 UTC</span>

<span style="font-size: 90%;">thanks!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:50:19 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:50:40 UTC</span>

<span style="font-size: 90%;">Thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:51:05 UTC</span>

<span style="font-size: 90%;">Bye and good night to everyone or good day for Chaim!</span>

**walter** <span style="color: grey; font-size: 90%;">20:51:15 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:51:29 UTC</span>

<span style="font-size: 90%;">Bye! And thank you all for joining.</span>

**airween** <span style="color: grey; font-size: 90%;">20:51:39 UTC</span>

<span style="font-size: 90%;">good night!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:51:49 UTC</span>

<span style="font-size: 90%;">night</span>

