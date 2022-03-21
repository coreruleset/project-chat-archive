### Mon, Jan 17th, 2022

**dune73** <span style="color: grey; font-size: 90%;">19:30:28 UTC</span>

<span style="font-size: 90%;">Hello, hello, time for some issues! How is it going?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:41 UTC</span>

<span style="font-size: 90%;">Ciao!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:08 UTC</span>

<span style="font-size: 90%;">hallo hallo</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:31:14 UTC</span>

<span style="font-size: 90%;">heyhooo</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:15 UTC</span>

<span style="font-size: 90%;">Hey guys, good to see you around!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:31:37 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:46 UTC</span>

<span style="font-size: 90%;">Airween called in sick today. But I wonder if _@fzipitria_ is back from his holidays.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:52 UTC</span>

<span style="font-size: 90%;">Hey _@Paul Beckett_!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:32:48 UTC</span>

<span style="font-size: 90%;">Hallo :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:51 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:54 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:11 UTC</span>

<span style="font-size: 90%;">Nice to see you all.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">Hey all!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:39 UTC</span>

<span style="font-size: 90%;">Hola!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:41 UTC</span>

<span style="font-size: 90%;">Before we get started - or as we get started, I'd like to hear your opinion on the Bug Bounty Plans.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:01 UTC</span>

<span style="font-size: 90%;">Walter and I did a meeting with Yahoo to take us under the umbrella of their bug bounty program.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:30 UTC</span>

<span style="font-size: 90%;">I concur on the scope, and that it might add a lot of complex changes to our rules</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">Also, we might need to issue regular updates for older versions, depending on severity</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:57 UTC</span>

<span style="font-size: 90%;">The basic architecture is: The is going to be a CRS Sub-Scope in the big Yahoo Bug Bounty. They to an initial triage and then fwd the issue to us. We fix it, then we tell them it's fixed and we advise on a bounty which they pay. 100%.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:33 UTC</span>

<span style="font-size: 90%;">The scoring base is going to be CVSS probably?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:35:54 UTC</span>

<span style="font-size: 90%;">They're going to pay for bypass? Or some other vuln like redos?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:05 UTC</span>

<span style="font-size: 90%;">They plan to do a first 2 week test run in Jan (!) / Feb, then readjustment, then another test run in Apr / May, then full public program from September.</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:29 UTC</span>

<span style="font-size: 90%;">I’ve also been thinking about this and I think in very rare cases, such as log4j, we have a good opportunity to help people protect themselves quickly. Christian had a good idea to create emergency plugins for this.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:36:31 UTC</span>

<span style="font-size: 90%;">Program on invite only?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:38 UTC</span>

<span style="font-size: 90%;">We shape the the various levels and a PL1 bypass is largely uninteresting so far.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:53 UTC</span>

<span style="font-size: 90%;">testruns: Invite only. From September: Fully open.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:00 UTC</span>

<span style="font-size: 90%;">Oh wow</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:15 UTC</span>

<span style="font-size: 90%;">Seems good, but who will write the terms?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:22 UTC</span>

<span style="font-size: 90%;">Probably you already did :rolling_on_the_floor_laughing:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:36 UTC</span>

<span style="font-size: 90%;">We write the terms and they can be adjusted after the test runs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:42 UTC</span>

<span style="font-size: 90%;">Let's not get too much into details.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:48 UTC</span>

<span style="font-size: 90%;">Cool</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:51 UTC</span>

<span style="font-size: 90%;">Sounds exciting!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:51 UTC</span>

<span style="font-size: 90%;">Makes sense</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:53 UTC</span>

<span style="font-size: 90%;">The problem is resources. And that is tough.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:37:56 UTC</span>

<span style="font-size: 90%;">Sounds cool</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:12 UTC</span>

<span style="font-size: 90%;">The problem is: They are going to throw a lot of money at this and this could starve us.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:38:19 UTC</span>

<span style="font-size: 90%;">I think biggest concern is the amount of work it could generate for us, and whether that will exceed capacity</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">If you pay X thousands of dollars for a bounty you want it fixed. So we need to deliver. And we already struggle with the issues we have.</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:50 UTC</span>

<span style="font-size: 90%;">Yes we made some sheets about possible classes of vulns and possible payouts. We will start with a limited run, so we won’t be swamped too much, and we will gain experience.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:18 UTC</span>

<span style="font-size: 90%;">Do you all think we can just let the test run arrive and see what happens?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:32 UTC</span>

<span style="font-size: 90%;">Acceptable time to repair is probably 30-60 days.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:39:36 UTC</span>

<span style="font-size: 90%;">Freezing all changes while the program is open, is it an option?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:50 UTC</span>

<span style="font-size: 90%;">That would delay our release plan.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:39:52 UTC</span>

<span style="font-size: 90%;">This should make us a little bit free</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:21 UTC</span>

<span style="font-size: 90%;">Triage is happening via the sandbox: If it is not exploitable via the sandbox they have to prove it's a Sandbox bug - or we will reject.
Our thought is that the dev-on-duty should be able to do the triage on the sandbox.</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:27 UTC</span>

<span style="font-size: 90%;">I don’t think we should do that, we can still accept issues. We will just be a little slower. But remember two years back when we had hundreds of issues. We managed to get out of that situation. I’m having a positive view, we can solve this in time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:16 UTC</span>

<span style="font-size: 90%;">Or is this too much to ask from the dev-on-duty? Unfortunately airween and _@azurIt_ are not here.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:42:56 UTC</span>

<span style="font-size: 90%;">It really depends on how many reports we will get per day/week...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:05 UTC</span>

<span style="font-size: 90%;">Absolutely.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:43:11 UTC</span>

<span style="font-size: 90%;">10 professional testers could create a lot of submissions in a short period.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:43:21 UTC</span>

<span style="font-size: 90%;">But yes, we have to start... Otherwise we don't know</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:50 UTC</span>

<span style="font-size: 90%;">For the record: 1st test will run with 5 pros and 5 strong amateurs.
We can steer volume via the bounty of course - but also by paying higher bounties for usable pull requests.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:43:50 UTC</span>

<span style="font-size: 90%;">I don't think we should expect the Dev on Duty person to triage. Just a personal opinion.</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:58 UTC</span>

<span style="font-size: 90%;">Another big Q is how do we validate entries? I expect some people coming with payloads that we aren’t able to verify: yes it passes CRS, but is it dangerous?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:18 UTC</span>

<span style="font-size: 90%;">Initially, the bounty will double if they deliver the report together with a pull report that we merge 1:1. Less if we use it as an inspiration.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:51 UTC</span>

<span style="font-size: 90%;">As Walter points out, validation is a problem. But then we have the yahoo BB team with us.</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:14 UTC</span>

<span style="font-size: 90%;">I understand. Maybe we could set up a bountry triage team, separate from the dev-on-duty?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:45:52 UTC</span>

<span style="font-size: 90%;">If bug bounty will pay significantly more for usable pull requests I think that could help a lot in terms of workload it generates for project</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:59 UTC</span>

<span style="font-size: 90%;">I would also feel better if we had a dedicated bug bounty team for the 1st test run. We can then learn from that experience.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:13 UTC</span>

<span style="font-size: 90%;">_@Paul_: Exactly our thinking.</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:47 UTC</span>

<span style="font-size: 90%;">We have various kinds of rules. I could handle reports for the PHP rules easily since I wrote them. Maybe Fran and Max could concentrate on the regexp wizardry.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:24 UTC</span>

<span style="font-size: 90%;">Paying the BB reporters for usable PRs is also net positive for our project: It forces red teamers to understand our project and our rules, thus improving their knowledge, thus raising the quality of their reports.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:48:19 UTC</span>

<span style="font-size: 90%;">I like the idea of having a team.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:48:43 UTC</span>

<span style="font-size: 90%;">But that will divert funds to testers :confused:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:46 UTC</span>

<span style="font-size: 90%;">I would love to have _@theMiddle_ in the team for the test run, since he is closer to red teaming than us blue team players.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:01 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ What do you mean?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:49:08 UTC</span>

<span style="font-size: 90%;">Yep, I really would love to join the team</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:22 UTC</span>

<span style="font-size: 90%;">We can pay the same money to our team, instead</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:43 UTC</span>

<span style="font-size: 90%;">I mean, if we pay extra for having a PR… why don’t we created the PR and receive the $$?</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:57 UTC</span>

<span style="font-size: 90%;">Yes, that would be a nice gesture if OWASP allows us to do this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:50:10 UTC</span>

<span style="font-size: 90%;">Just thinking on how to get funds on the project</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:46 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ That's what I meant with starvation of our project. The bb reporters will get rich and we might end up working our ass off - or we ruin our funds by trying to keep up with the pockets of Yahoo. They made it quite clear that the funds are meant for the reporters and not for the fixers.</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:00 UTC</span>

<span style="font-size: 90%;">I think it would make a lot of sense. This shifts our commitment from a free time journey to actual work with stress and deadlines.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:51:59 UTC</span>

<span style="font-size: 90%;">Well… I don’t understand the reasoning from Yahoo</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:52:06 UTC</span>

<span style="font-size: 90%;">If it becomes a big burden then we pull the plug and walk away, right? There's no formal/contractual obligation on CRS project?</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:10 UTC</span>

<span style="font-size: 90%;">I joined the project because I wanted to improve the world a little, but a few bucks would give me a feeling of appreciation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:12 UTC</span>

<span style="font-size: 90%;">I am very reluctant to start to pay for PRs in our team. How much for which PR? And who would work for free if you can get money for a PR. Once money is on the table it becomes challenging.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:43 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:50 UTC</span>

<span style="font-size: 90%;">But the project needs the money also</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:07 UTC</span>

<span style="font-size: 90%;">Yes, we need to have that money for the next retreat :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:16 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:26 UTC</span>

<span style="font-size: 90%;">Or getting better infra for testers</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:28 UTC</span>

<span style="font-size: 90%;">I think this can be one direction this could develop. But there is a risk it ruins us not only from a financial perspective, but also as a group of friends. And I would not risk that easily.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:53 UTC</span>

<span style="font-size: 90%;">Agreed. It is a difficult subject</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:01 UTC</span>

<span style="font-size: 90%;">Well, let’s see how it works</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:02 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:23 UTC</span>

<span style="font-size: 90%;">I mean the question is not imminent anyways. Let's see how the testrun develops and what lessons to draw from it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:49 UTC</span>

<span style="font-size: 90%;">I read that @Walter, _@theMiddle_ and _@franbuehler_ would be in the BB-team for the test run?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:55:13 UTC</span>

<span style="font-size: 90%;">Ok for me!</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:27 UTC</span>

<span style="font-size: 90%;">Sounds good to me. I’m not much of an attacker but I know my rules :smile:</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:56:10 UTC</span>

<span style="font-size: 90%;">Me neither!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:55:28 UTC</span>

<span style="font-size: 90%;">This will be very exciting. I would like to join the team!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:10 UTC</span>

<span style="font-size: 90%;">Me neither!</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:56:10 UTC</span>

<span style="font-size: 90%;">Me neither!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:26 UTC</span>

<span style="font-size: 90%;">Who else? Given the team will also have to fix things as far as possible, I think it takes more (hu)manpower.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:44 UTC</span>

<span style="font-size: 90%;">I can be around</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:51 UTC</span>

<span style="font-size: 90%;">_@azurIt_ might be in for the adventure, but I would rather not volunteer him without being around.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:18 UTC</span>

<span style="font-size: 90%;">What does "be around" constitute exactly? You will help out if time permits?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:34 UTC</span>

<span style="font-size: 90%;">(Sorry for being a pain in the a**)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:35 UTC</span>

<span style="font-size: 90%;">Yes, definitely</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:42 UTC</span>

<span style="font-size: 90%;">When does it start and end exactly? Because of vacation plans in February.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:57:48 UTC</span>

<span style="font-size: 90%;">Unfortunately things are pretty crazy in my personal life at the moment, so don't think I have the necessary time this needs to help</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:03 UTC</span>

<span style="font-size: 90%;">In other words, count me in</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:14 UTC</span>

<span style="font-size: 90%;">There is another meeting with hackerone + yahoo on Wednesday. We will probably fix dates then.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:20 UTC</span>

<span style="font-size: 90%;">ok</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:30 UTC</span>

<span style="font-size: 90%;">When are your holidays?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:58:30 UTC</span>

<span style="font-size: 90%;">I have the opposite problem to _@franbuehler_: I can maybe help, but only from February onward.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:56 UTC</span>

<span style="font-size: 90%;">_@xanadu_ could you be her backup depending on the date?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:56 UTC</span>

<span style="font-size: 90%;">Sportwoche Feb 5-13</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:12 UTC</span>

<span style="font-size: 90%;">So Andrew could come in from Feb 5.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:59:29 UTC</span>

<span style="font-size: 90%;">I could play backup but I'd rather not commit up front</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:50 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ and _@maxleske_: Perfectly understandable.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:27 UTC</span>

<span style="font-size: 90%;">OK, I think we have a team and all it takes to tackle this. You'll write history!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:34 UTC</span>

<span style="font-size: 90%;">Very well. Then let's look at the issues, so the meeting does not trag out too long.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:40 UTC</span>

<span style="font-size: 90%;">2319: Refactoring CRS variables</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:34 UTC</span>

<span style="font-size: 90%;">I think we have chewed this long enough now. We pretty much settled on new variable names for PL. Somebody will now have to describe the final solution based on Simon's proposal and then Simon or somebody else will have to do the PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:07 UTC</span>

<span style="font-size: 90%;">The PR should probably be coordinated since it's going to affect like every rules file and potentially every detection rule.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:18 UTC</span>

<span style="font-size: 90%;">Aren't we waiting on a PR so we can see exactly what the plan is? I thought that was where we were at</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:32 UTC</span>

<span style="font-size: 90%;">To review, that is.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:55 UTC</span>

<span style="font-size: 90%;">Hmm. Now, I think Simon waits for us to really tell him what exactly we want. Or did I get the discussion wrong the last time?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:05:24 UTC</span>

<span style="font-size: 90%;">I'm still not 100% sure what the plan/proposal is. Was hoping to see a PR to get a clearer idea, maybe.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:26 UTC</span>

<span style="font-size: 90%;">That is the point. It's not 100% clear so somebody should write down the plan. If we provide a PR and then start to discuss the details, a lot is going to be blocked because of this PR. Or many other PRs will be disrupted once this one merges.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:39 UTC</span>

<span style="font-size: 90%;">I think once we have the PR it should be merged quickly.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:00 UTC</span>

<span style="font-size: 90%;">(We used to have huge PRs linger for several months in the past and it very annoying.)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:36 UTC</span>

<span style="font-size: 90%;">_@xanadu_ I have a deal to propose. You asked to be involved with the plugin creation / Rule Exclusion migration. I could take on describing the final solution for 2319 if you take the transfer of the DoS rules into a plugin from me.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:15 UTC</span>

<span style="font-size: 90%;">It could be a good opening / intro into plugins, a good deed for the project and you would learn the DoS rules which could be interesting for you as you work for an integrator.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:35 UTC</span>

<span style="font-size: 90%;">The DoS rules look horrible and I never ever use them :laughing:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:09:51 UTC</span>

<span style="font-size: 90%;">But I will make the plugin. I agree, it's good experience.</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:05 UTC</span>

<span style="font-size: 90%;">haha yes they are</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:05 UTC</span>

<span style="font-size: 90%;">Super cool. So I'll sort out 2319. Thank you _@xanadu_. Big support here - and it can wait until February. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:18 UTC</span>

<span style="font-size: 90%;">2332: Status of the big backslah hunt and the question of design decisions</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:45 UTC</span>

<span style="font-size: 90%;">So one outcome of the backslash hunt is that we need to list these design decisions somewhere.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:12:08 UTC</span>

<span style="font-size: 90%;">`/docs/development/`?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:12 UTC</span>

<span style="font-size: 90%;">I mean it could be CONTIBUTING.md - or a wiki page, or /docs?
But we are piling up more and more.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:30 UTC</span>

<span style="font-size: 90%;">And we need to write it down or we lose track.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:43 UTC</span>

<span style="font-size: 90%;">The order of actions is such a decision already.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:13:26 UTC</span>

<span style="font-size: 90%;">CONTRIBUTING sounds right. There's the rule about rule file layout in there, that's about the same level.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:13:57 UTC</span>

<span style="font-size: 90%;">Should `/docs/development/` mirror CONTRIBUTING.MD?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:09 UTC</span>

<span style="font-size: 90%;">Good idea. It could</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:10 UTC</span>

<span style="font-size: 90%;">ohhhh yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:10 UTC</span>

<span style="font-size: 90%;">And be a prettier HTML version?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:14:25 UTC</span>

<span style="font-size: 90%;">'Single source of truth' etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:14:33 UTC</span>

<span style="font-size: 90%;">++</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:14:37 UTC</span>

<span style="font-size: 90%;">+++</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:42 UTC</span>

<span style="font-size: 90%;">As long as the mirror is automatic. I hate redundancy.</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:10 UTC</span>

<span style="font-size: 90%;">Well we could get rid of contributing, or just point to the documentation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:15:39 UTC</span>

<span style="font-size: 90%;">Our Hugo docs are also .md files, so could pull from the repo directly.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:44 UTC</span>

<span style="font-size: 90%;">Given the documentation is in a separate repo, getting rid of contributing would just mean we need to look further when we want to update it.</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:34 UTC</span>

<span style="font-size: 90%;">Yes, but looking up an .md file on GitHub is sort of annoying to me, while browsing beautiful documentation gives me more of a good feeling…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:16:59 UTC</span>

<span style="font-size: 90%;">We can link it easily probably</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:01 UTC</span>

<span style="font-size: 90%;">Absolutely. But if _@xanadu_ can make the export automatic, we get both.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:17:16 UTC</span>

<span style="font-size: 90%;">I'll have a look.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:00 UTC</span>

<span style="font-size: 90%;">But we agree on the design decisions in one place and _@xanadu_ tells us where this is going to me. OK?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:40 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ do you have them all in your mind? _@maxleske_ looked very deep into regex assembly too. I think that's the core areas where we took decisions.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:15 UTC</span>

<span style="font-size: 90%;">Sorry, got lost</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:19 UTC</span>

<span style="font-size: 90%;">What do you mean?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:19:44 UTC</span>

<span style="font-size: 90%;">regex assembly isn't happy with [\\\\]. \x5 is fine</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:19:54 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:20:00 UTC</span>

<span style="font-size: 90%;">Also "Best practice on anchoring regexs" maybe?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:04 UTC</span>

<span style="font-size: 90%;">Design decisions. What decisions did we take those last 2-3 years?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:20 UTC</span>

<span style="font-size: 90%;">Lazy matching also</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:39 UTC</span>

<span style="font-size: 90%;">Using re2 compatible stuff whenever possible.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:45 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:09 UTC</span>

<span style="font-size: 90%;">Once we start collecting it's probably quite a few.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:17 UTC</span>

<span style="font-size: 90%;">Let's write that down and I'll give it a look over w.r.t. assembly.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:21:29 UTC</span>

<span style="font-size: 90%;">Added to the wiki page.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:33 UTC</span>

<span style="font-size: 90%;">Good plan.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:40 UTC</span>

<span style="font-size: 90%;">We removed most lookbehind and lookafter</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:59 UTC</span>

<span style="font-size: 90%;">(that’s the re2 compatible stuff)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:09 UTC</span>

<span style="font-size: 90%;">But it will work also with hyperscan</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:11 UTC</span>

<span style="font-size: 90%;">And others</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:17 UTC</span>

<span style="font-size: 90%;">As for the backslash hunt: You're all good there or anything to discuss?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:36 UTC</span>

<span style="font-size: 90%;">IMHO we are good. We just need to do it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:42 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:46 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:58 UTC</span>

<span style="font-size: 90%;">[#2318](https://github.com/coreruleset/coreruleset/issues/#2318): _@walter_, you promised some FPs here. Is that still on your task list?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:23:00 UTC</span>

<span style="font-size: 90%;">(saw that we started already)</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:10 UTC</span>

<span style="font-size: 90%;">I haven’t scheduled it, but I will look at it on monday.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:39 UTC</span>

<span style="font-size: 90%;">[#2344](https://github.com/coreruleset/coreruleset/issues/#2344) aims to bring all tests up to a minimal standard so they stop to trigger rules for omission on accept-header and the like. This will help us with the status page and and is overall a welcome cleanup project. How do we attack this?</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:51 UTC</span>

<span style="font-size: 90%;">I think a copypastable skeleton in the wiki with tips and tricks would be a good idea.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:26:07 UTC</span>

<span style="font-size: 90%;">Skeleton is already there</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:26:14 UTC</span>

<span style="font-size: 90%;">It's a bit confusing.</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:15 UTC</span>

<span style="font-size: 90%;">ah!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:17 UTC</span>

<span style="font-size: 90%;">But it would take some updating.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:32 UTC</span>

<span style="font-size: 90%;">But how do we apply it to the 4-5K tests?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:26:38 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/blob/v3.4/dev/tests/regression/tests/positivetest.yaml.skeleton](https://github.com/coreruleset/coreruleset/blob/v3.4/dev/tests/regression/tests/positivetest.yaml.skeleton)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:26:55 UTC</span>

<span style="font-size: 90%;">Will try to do some yq magic</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:07 UTC</span>

<span style="font-size: 90%;">Great!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:13 UTC</span>

<span style="font-size: 90%;">I was wondering wether yq would exist!?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:27:23 UTC</span>

<span style="font-size: 90%;">Wait: how about adding a configuration parameter that adds standard headers?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:27 UTC</span>

<span style="font-size: 90%;">[https://mikefarah.gitbook.io/yq/](https://mikefarah.gitbook.io/yq/)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:28 UTC</span>

<span style="font-size: 90%;">But it can't fix things automatically, or can it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:43 UTC</span>

<span style="font-size: 90%;">It can</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:51 UTC</span>

<span style="font-size: 90%;">Provided we get the correct query</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:53 UTC</span>

<span style="font-size: 90%;">Wow. Cool.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:06 UTC</span>

<span style="font-size: 90%;">Then we could "enforce" our standard through the test harness</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:28:26 UTC</span>

<span style="font-size: 90%;">The problem is that we need to read the test’s intent</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:28 UTC</span>

<span style="font-size: 90%;">Unsure about the standards header. But true that it would avoid updating all the rules for "new" standard in the future.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:28:51 UTC</span>

<span style="font-size: 90%;">Do we have/need some tests that break these rules, for checking conformance to protocols?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:53 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ yes but we need to do that anyway</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:28:57 UTC</span>

<span style="font-size: 90%;">Probably no tests outside 920XXX should have custom headers</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:29 UTC</span>

<span style="font-size: 90%;">Let's not get into too much details, I see you guys have a decent set of ideas here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:42 UTC</span>

<span style="font-size: 90%;">Can we assign somebody?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:30:09 UTC</span>

<span style="font-size: 90%;">If someone wants to learn yq, that would be awesome</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:30:20 UTC</span>

<span style="font-size: 90%;">I can take it for next month if not</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:59 UTC</span>

<span style="font-size: 90%;">Looks like you will get to practice your yq-fu!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:03 UTC</span>

<span style="font-size: 90%;">But thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:38 UTC</span>

<span style="font-size: 90%;">Time to get done with this meeting. Let's just look at a few issues and if we can assign them to somebody and we're done.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:48 UTC</span>

<span style="font-size: 90%;">_@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:00 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ has [#2341](https://github.com/coreruleset/coreruleset/issues/#2341). Still OK?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:25 UTC</span>

<span style="font-size: 90%;">:eyes:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:51 UTC</span>

<span style="font-size: 90%;">Same for [#2343](https://github.com/coreruleset/coreruleset/issues/#2343)?</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:07 UTC</span>

<span style="font-size: 90%;">I already mreged that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:33:12 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:33:18 UTC</span>

<span style="font-size: 90%;">I can handle 2341</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:33 UTC</span>

<span style="font-size: 90%;">Ooops.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:56 UTC</span>

<span style="font-size: 90%;">And I closed another one just now. As far as I can see we're mostly done. Unless you want to put more issues on the table.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:58 UTC</span>

<span style="font-size: 90%;">Did you mean [#2334](https://github.com/coreruleset/coreruleset/issues/#2334)?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:56 UTC</span>

<span style="font-size: 90%;">Yes, but that is also assigned to _@fzipitria_... :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:08 UTC</span>

<span style="font-size: 90%;">I see this issue contains a nice pint for him</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:11 UTC</span>

<span style="font-size: 90%;">i know :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:13 UTC</span>

<span style="font-size: 90%;">just checking</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:46 UTC</span>

<span style="font-size: 90%;">So it looks like we're done then. Anything else?</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:12 UTC</span>

<span style="font-size: 90%;">not from my side!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:36:30 UTC</span>

<span style="font-size: 90%;">I added a Docker documentation thing to the agenda: please ignore it :laughing:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:36:49 UTC</span>

<span style="font-size: 90%;">I've had second thoughts. Better to concentrate on the CONTRIBUTING.MD => /docs/developers for now, I think.</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:52 UTC</span>

<span style="font-size: 90%;">next week I have my dev-on-duty. It’s been a while ago for me and the scope has expanded. would you mind if I ask some questions here?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:14 UTC</span>

<span style="font-size: 90%;">No problem. Just bring it here.</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:35 UTC</span>

<span style="font-size: 90%;">thanks!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:37 UTC</span>

<span style="font-size: 90%;">Please note that _@xanadu_ found a way to tell SO that it's the dev-on-duty talking.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:51 UTC</span>

<span style="font-size: 90%;">Moderators would always remove the greeting.</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:58 UTC</span>

<span style="font-size: 90%;">yes, I read that! very good lifehack. I’ll use it.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:13 UTC</span>

<span style="font-size: 90%;">Thank you all for joining!</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:20 UTC</span>

<span style="font-size: 90%;">thanks for organizing! :heart:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:38:42 UTC</span>

<span style="font-size: 90%;">You can also use the magic phrase "BEWARE THE XANADU'S WRATH" and they'll leave you alone :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:39:17 UTC</span>

<span style="font-size: 90%;">Thank you all and good night!!</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:39:29 UTC</span>

<span style="font-size: 90%;">Bye folks</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:39:33 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:39:37 UTC</span>

<span style="font-size: 90%;">Good night</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:50 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:40:00 UTC</span>

<span style="font-size: 90%;">good night</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:42:23 UTC</span>

<span style="font-size: 90%;">Bye everyone!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:44:03 UTC</span>

<span style="font-size: 90%;">:wave:</span>

