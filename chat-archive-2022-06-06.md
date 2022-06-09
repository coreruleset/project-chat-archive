### Mon, Jun 6th, 2022

**dune73** <span style="color: grey; font-size: 90%;">18:31:23 UTC</span>

<span style="font-size: 90%;">Hey, hey, welcome to our monthly project chat. It's a bit of a special chat as we are not following our usual agenda. Instead we need to come up with a plan how to work through the many bug bounty findings.
Please find the agenda at [https://github.com/coreruleset/coreruleset/issues/2539](https://github.com/coreruleset/coreruleset/issues/2539)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:46 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:05 UTC</span>

<span style="font-size: 90%;">Hello Max!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:32:13 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:32:15 UTC</span>

<span style="font-size: 90%;">Ciao a tutti!</span>

**airween** <span style="color: grey; font-size: 90%;">18:32:21 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:36 UTC</span>

<span style="font-size: 90%;">hello!!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:50 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:52 UTC</span>

<span style="font-size: 90%;">Hey, hey, good to see you all!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:14 UTC</span>

<span style="font-size: 90%;">Hope _@fzipitria_ will join us as well. This is important tonight.</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:31 UTC</span>

<span style="font-size: 90%;">I saw him creating issues until late at night, so I hope he had some sleep :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:43 UTC</span>

<span style="font-size: 90%;">Before we really start. We have a a fileshare now, because we really need one.
This is meant for developers with commit rights.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:49 UTC</span>

<span style="font-size: 90%;">https://drive.google.com/drive/folders/REDACTED<span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:32 UTC</span>

<span style="font-size: 90%;">_@dune73_ You sure you want to share that link in this channel?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:40 UTC</span>

<span style="font-size: 90%;">I see that some have not yet asked for access. Please do, so we can respond to the requests and we know everybody is able to read stuff there. Name the two important confidential documents about the bug bounty findings.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:53 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Is this a problem?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:07 UTC</span>

<span style="font-size: 90%;">Well, you still have to grant access :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:30 UTC</span>

<span style="font-size: 90%;">Hey! :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:36:36 UTC</span>

<span style="font-size: 90%;">You might get spammed with robots trying to request access :robot_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:42 UTC</span>

<span style="font-size: 90%;">That's the idea. But true that if somebody sets up a crs-like google persona, we might be tricked.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:36:56 UTC</span>

<span style="font-size: 90%;">lol</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:57 UTC</span>

<span style="font-size: 90%;">I will remove the link for the archive.</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:59 UTC</span>

<span style="font-size: 90%;">You convinced me to finally give google my real name.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:10 UTC</span>

<span style="font-size: 90%;">Witold is your real name?</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:14 UTC</span>

<span style="font-size: 90%;">no :rolling_on_the_floor_laughing:</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:25 UTC</span>

<span style="font-size: 90%;">but I was sick of the “who is Witold?” messages</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:30 UTC</span>

<span style="font-size: 90%;">Now I am puzzled. :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:38 UTC</span>

<span style="font-size: 90%;">we told you!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:37:42 UTC</span>

<span style="font-size: 90%;">Ahaha</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:18 UTC</span>

<span style="font-size: 90%;">Just granted access to a certain Franziska. Hope it's you. :slightly_smiling_face:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:39:02 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:22 UTC</span>

<span style="font-size: 90%;">Good, so before we dive into the swamp, you probably saw that F5/NGINX has announced an EOL for ModSecurity support. This comes after the Trustwave announcement of course.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:48 UTC</span>

<span style="font-size: 90%;">It's also a natural move for our sponsor F5 / NGINX, since this allows them to migrate users to their F5 WAF offering.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:12 UTC</span>

<span style="font-size: 90%;">For the time being there is no change in sponsoring, but I expect less interest in pushing Trustwave to fix bugs.</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:59 UTC</span>

<span style="font-size: 90%;">Yeah, that’s a possibility. At the other hand they might have a contract for several years.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:20 UTC</span>

<span style="font-size: 90%;">But maybe we need friends at Nginx to push/help motivate them.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:42 UTC</span>

<span style="font-size: 90%;">Then for the record and because this is public: A big integrator invited 20 WAF security researchers to a limited, private bug bounty program. The program was a big success and the researchers did not disappoint. Yet we are in the very difficult situation that we are a swamped with bypassing payloads that we need to resolve. Some of these findings are really hard to fix. A blog post is upcoming.

Tonight, we will try to come up with a plan on how to fix the various issues.

Also: This affects the release plan of CRS v4 (in a negative way).</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:47 UTC</span>

<span style="font-size: 90%;">Yes. For a short summary, the event has ran for 2 weeks and was about researchers trying to bypass the CRS. This lead to no fewer than 160 findings, of which some were serious, and some affect the engine instead of the rules, so we expect to have to work together with Trustwave and Coraza in order to fix some issues there. After this, the hackers were invited to create PRs for a money bonus, and we got quite some nice PRs, some of which were good to merge and some will need some handholding.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:20 UTC</span>

<span style="font-size: 90%;">3/5 of the findings do not have a PR yet. Many of them are duplicates though. Still, every duplicate will have to be checked by hand. Since a Bug Bounty has a more coarse understanding of a duplicate than we, since we want to make sure the "almost identical" payload is really also caught.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:20 UTC</span>

<span style="font-size: 90%;">@Walter and _@fzipitria_ you worked through all the findings and categorized them in a spreadsheet.
What did you do exactly (without touching on individual findings)?</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:30 UTC</span>

<span style="font-size: 90%;">What we did most importantly was group them. For instance, we got about 10 reports about people trying to get RCE by adding a command (not in our wordlist). Example: find . -exec foo. We grouped these, because they can be solved probably with one commit. That should lower our workload a lot.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:03 UTC</span>

<span style="font-size: 90%;">And further, it might help us to split the issues between people who are experienced in the field of the bypass.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:38 UTC</span>

<span style="font-size: 90%;">Did you de-couple the bug bounty findings? As in "We are sure every bug has 1 row in the spreadsheet and those bug bounty findings with more than one bug have multiple entries".</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:49 UTC</span>

<span style="font-size: 90%;">We tried, but hmm, we were working from Intigriti’s spreadsheet, so maybe we should have another look to see if there is missing information.</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:01 UTC</span>

<span style="font-size: 90%;">In any case, here is the sheet: [https://docs.google.com/spreadsheets/d/1_duWN0PlX7mAQ-fwYDyudmJ6J-P9TScS/edit#gid=154264918](https://docs.google.com/spreadsheets/d/1_duWN0PlX7mAQ-fwYDyudmJ6J-P9TScS/edit#gid=154264918)</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:47 UTC</span>

<span style="font-size: 90%;">I just sorted by “Grouping” column, here you can see the different categories/solutions of findings.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:56 UTC</span>

<span style="font-size: 90%;">This effectively means we still have to work through all the reports on the Intitriti platform and check if we have identified all the bugs. Correct?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:20 UTC</span>

<span style="font-size: 90%;">Probably as a secondary task, yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:34 UTC</span>

<span style="font-size: 90%;">The "grouping" is very helpful. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:15 UTC</span>

<span style="font-size: 90%;">You did not yet decide which findings / fixes will be backported, if I see this correctly. (I'm asking since we talked about this in separate leader meeting).</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:23 UTC</span>

<span style="font-size: 90%;">Also, “complexity” is a guess of how hard it will be to fix it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:43 UTC</span>

<span style="font-size: 90%;">No, that’s true. Didn’t think of 3.x at all really.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:00 UTC</span>

<span style="font-size: 90%;">We have priorities</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:33 UTC</span>

<span style="font-size: 90%;">I think we decided that we were going to backport the severe full bypasses, but not more. I think this might be < 10 issues?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:33 UTC</span>

<span style="font-size: 90%;">So anything with priority high might be considered, but not certain to be backported</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:39 UTC</span>

<span style="font-size: 90%;">OK.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:41 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:17 UTC</span>

<span style="font-size: 90%;">I created a column “Backport” and will fill it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:55:21 UTC</span>

<span style="font-size: 90%;">how it works with backporting? we should commit to old branch?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:55:55 UTC</span>

<span style="font-size: 90%;">we create a pr to old branch, yes.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">18:56:10 UTC</span>

<span style="font-size: 90%;">but only on the ones we deemed to be backported</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:21 UTC</span>

<span style="font-size: 90%;">Another question: I've seen a full bypass that you gave priority "medium". Is this a mistake? Can I fix it?</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:29 UTC</span>

<span style="font-size: 90%;">Yes, please fix it</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:32 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">So the full bypasses should all have priority "high". Are there other findings in this priority?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:16 UTC</span>

<span style="font-size: 90%;">If so, can we put the full bypasses higher?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:26 UTC</span>

<span style="font-size: 90%;">critical?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:37 UTC</span>

<span style="font-size: 90%;">Also because I want to be able to filter for the full bypasses and I think so far that's not possible.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:42 UTC</span>

<span style="font-size: 90%;">I'd be happy with "critical".</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:46 UTC</span>

<span style="font-size: 90%;">critical :+1:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:50 UTC</span>

<span style="font-size: 90%;">When you looked through all the findings, did you encounter additional full bypasses? I think I spotted two not on the full bypass list. Added them in then meantime, but did not really dig into them.</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:11 UTC</span>

<span style="font-size: 90%;">I think one, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:32 UTC</span>

<span style="font-size: 90%;">Ah, yes. One.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:39 UTC</span>

<span style="font-size: 90%;">Is PA09KYZT a bypass? It wasn't on the bypass list.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:58:58 UTC</span>

<span style="font-size: 90%;">Unless it's a duplicate</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:59:41 UTC</span>

<span style="font-size: 90%;">mmm</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:01 UTC</span>

<span style="font-size: 90%;">No, It's not on the list. Could be added though. Opinions?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:00:11 UTC</span>

<span style="font-size: 90%;">hmmm</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:17 UTC</span>

<span style="font-size: 90%;">(Without getting specific please, this is still meant to be confidential)</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:44 UTC</span>

<span style="font-size: 90%;">Hmm, it’s a bypass I think. PA09 sends Content-Type: text/plain and no body processor is running on this. However, some applications still accept the input.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:01:03 UTC</span>

<span style="font-size: 90%;">I try to not spoil nothing here but, I would not happy to create rules for that case</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:35 UTC</span>

<span style="font-size: 90%;">I was thinking about it, I was thinking we could activate the urlencoded body processor. Everything will end up in ARGS_NAMES, but we will still see it.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:01:35 UTC</span>

<span style="font-size: 90%;">you can literally send everything</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:08 UTC</span>

<span style="font-size: 90%;">Anyway, this is a “hard” one :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:02:21 UTC</span>

<span style="font-size: 90%;">moreover, I don't remember an exploit that use that specific CT in an application that use urlencoded or json or others</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:34 UTC</span>

<span style="font-size: 90%;">So we add it to the list.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:49 UTC</span>

<span style="font-size: 90%;">The full bypass list I mean.</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:54 UTC</span>

<span style="font-size: 90%;">same here, but I would guess there are many applications that don’t check the Content-Type</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:24 UTC</span>

<span style="font-size: 90%;">so in any case: what would be our best plan?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:04:18 UTC</span>

<span style="font-size: 90%;">maybe we can try to have a pre-condition like "if CT is xyz so apply the following list of rules on the raw request body"</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:38 UTC</span>

<span style="font-size: 90%;">We should probably move from priority highest to lowest. At the other hand, there are a lot of “easy” ones which might be nice to do in a spare few hours.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:48 UTC</span>

<span style="font-size: 90%;">Then we'll need a new column for "full bypass", since a full bypass might not be critical</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:08 UTC</span>

<span style="font-size: 90%;">I do not follow you _@walter_. "Lowest" for this finding?</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:00 UTC</span>

<span style="font-size: 90%;">I mean for all findings</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:07:15 UTC</span>

<span style="font-size: 90%;">But is a full bypass not inherently "critical"? Can there be a non-critical full bypass?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:35 UTC</span>

<span style="font-size: 90%;">I must have misunderstood...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:17 UTC</span>

<span style="font-size: 90%;">So you are saying we should talk about lowest findings first here in the meeting, since they are so easy? Really do not get it ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:47 UTC</span>

<span style="font-size: 90%;">No, I am just saying, if someone has a few spare hours and don’t want to fry their brains too much, it will also be helpful to close a lot of the “easy” ones, we’ll have to get to them somewhere in time anyway. But, obviously the higher severity ones need professional management.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:06 UTC</span>

<span style="font-size: 90%;">Got it. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:21 UTC</span>

<span style="font-size: 90%;">Anything that is off the table helps to give us a clearer vision.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:45 UTC</span>

<span style="font-size: 90%;">That means, we should merge whatever we feel can be merged. Correct?</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:01 UTC</span>

<span style="font-size: 90%;">Exactly, but please update the sheet :slightly_smiling_face: !</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:25 UTC</span>

<span style="font-size: 90%;">Then I will reach out to sponsors and integrators with details about the criticals / full bypasses.</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:31 UTC</span>

<span style="font-size: 90%;">I made a status column in column 2, open ,merged, maybe “busy” to show what we’re currently working on.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:49 UTC</span>

<span style="font-size: 90%;">This is helpful.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:20 UTC</span>

<span style="font-size: 90%;">Is this the moment where we bring in additional help for the full bypasses? We had people ask. If so, we could set something up.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:41 UTC</span>

<span style="font-size: 90%;">Separate slack? ?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:48 UTC</span>

<span style="font-size: 90%;">You mean, working with the researchers directly?</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:01 UTC</span>

<span style="font-size: 90%;">You mean people from Trustwave, Coraza? Maybe a separate, empty channel would be better then.</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:16 UTC</span>

<span style="font-size: 90%;">We might also start thinking of a cool name for the bug.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:32 UTC</span>

<span style="font-size: 90%;">Yes, people from TW, Coraza, 1-2 other volunteers from integrators / sposnors.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:39 UTC</span>

<span style="font-size: 90%;">Better empty channel then. OK with me.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:14:40 UTC</span>

<span style="font-size: 90%;">but please, create a dedicated logo with Paint</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:16 UTC</span>

<span style="font-size: 90%;"></span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:25 UTC</span>

<span style="font-size: 90%;">How do we approach the non-criticals on the spreadsheet. Divide them up by the groups tonight? (Probably a bit much to chew on). Or dividing up the HIGHs by group tonight? (And ask everybody to look the LOWs if they are bored.)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:02 UTC</span>

<span style="font-size: 90%;">What we were talking in the weekend</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:06 UTC</span>

<span style="font-size: 90%;">The latter</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:14 UTC</span>

<span style="font-size: 90%;">Was to just start with lows</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:32 UTC</span>

<span style="font-size: 90%;">I’ve created some issues to start digging, based on the sheet</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:50 UTC</span>

<span style="font-size: 90%;">We need to create more issues form there</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:56 UTC</span>

<span style="font-size: 90%;">Yes very good idea</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:18 UTC</span>

<span style="font-size: 90%;">Medium ones will require way more work</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:24 UTC</span>

<span style="font-size: 90%;">Got you.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:34 UTC</span>

<span style="font-size: 90%;">Low prio -> create issues and mark for v4?</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:42 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:42 UTC</span>

<span style="font-size: 90%;">Low ones can be solved individually</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:55 UTC</span>

<span style="font-size: 90%;">Medium might require team up</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:19:14 UTC</span>

<span style="font-size: 90%;">And high and critical a council</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:32 UTC</span>

<span style="font-size: 90%;">What about the idea to extract payloads from all the findings, make them into tests and commit them to a separate private repo?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:20:04 UTC</span>

<span style="font-size: 90%;">For those who make sense, yes?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:20:27 UTC</span>

<span style="font-size: 90%;">I mean, if we need to add words to a list, I would not create a test for every word</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:20:46 UTC</span>

<span style="font-size: 90%;">Sure thing. But all the rest ...</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:21:02 UTC</span>

<span style="font-size: 90%;">all the rest, yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:50 UTC</span>

<span style="font-size: 90%;">Who's going to create the issues for low prio? It would be annoying if we created duplicates.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:14 UTC</span>

<span style="font-size: 90%;">Why should the repo be private?</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:17 UTC</span>

<span style="font-size: 90%;">I think if you change the status from ‘open’ to ‘busy’, others will know not to touch it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:34 UTC</span>

<span style="font-size: 90%;">Well there are quite some zero-days in the tests…</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:57 UTC</span>

<span style="font-size: 90%;">It would seem dangerous to publish them before we have a patch</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:03 UTC</span>

<span style="font-size: 90%;">But we'd make them public once we're patched?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:13 UTC</span>

<span style="font-size: 90%;">Yes, exactly.</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:26 UTC</span>

<span style="font-size: 90%;">Yes, then they should be copypasted as normal tests in the fix.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:21:52 UTC</span>

<span style="font-size: 90%;">If tests are going on private repo (presumably to not help attackers), should we push updates/fixes to private repo, as it would probably be relatively easy to reverse engineer the exploit from the fix?</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:23:15 UTC</span>

<span style="font-size: 90%;">True, the added new rules and the tests for them will show the weaknesses. But the volume of issues is so high, I don’t see a good workflow to keep it all private until the end.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:55 UTC</span>

<span style="font-size: 90%;">We could freeze the public repo until we're done...</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">Only work on the private repo and the rebase</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:54 UTC</span>

<span style="font-size: 90%;">Wait, what patched means? 90% of the people will not have patches, unless critical</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:55 UTC</span>

<span style="font-size: 90%;">That way you have the test ready when you write your rule to mitigate an attack.
Idea: Test file has the finding ID as file anme.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:22:03 UTC</span>

<span style="font-size: 90%;">Just to be clear, do we want to create GH issues for medium issues as well?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:22:46 UTC</span>

<span style="font-size: 90%;">Will the GitHub actions stuff all work correctly if we put tests in a different repo and write the patch in another repo?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">No, you copy the test into your PR once you are ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:41 UTC</span>

<span style="font-size: 90%;">The tests repo is more of a library with pre-prepared tests.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:55 UTC</span>

<span style="font-size: 90%;">We could freeze the public repo until we're done...</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:23:15 UTC</span>

<span style="font-size: 90%;">True, the added new rules and the tests for them will show the weaknesses. But the volume of issues is so high, I don’t see a good workflow to keep it all private until the end.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:55 UTC</span>

<span style="font-size: 90%;">We could freeze the public repo until we're done...</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">Only work on the private repo and the rebase</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:17 UTC</span>

<span style="font-size: 90%;">It separates the examination of all the findings from the creation of dozens of PRs.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">Only work on the private repo and the rebase</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:23:15 UTC</span>

<span style="font-size: 90%;">True, the added new rules and the tests for them will show the weaknesses. But the volume of issues is so high, I don’t see a good workflow to keep it all private until the end.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:23:55 UTC</span>

<span style="font-size: 90%;">We could freeze the public repo until we're done...</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:24:20 UTC</span>

<span style="font-size: 90%;">Only work on the private repo and the rebase</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:47 UTC</span>

<span style="font-size: 90%;">Because when you examine a finding, you are in the best position to write a test with the payload the researcher submitted. Otherwise you will have to go back...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:10 UTC</span>

<span style="font-size: 90%;">And it will be easy to prove we have covered everything afterwards.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:03 UTC</span>

<span style="font-size: 90%;">so we need to turn off our check</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:20 UTC</span>

<span style="font-size: 90%;">We have a test that checks we have tests for every rule commited</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:02 UTC</span>

<span style="font-size: 90%;">Honestly, I do not see us fix everything in public in one big chunk.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:10 UTC</span>

<span style="font-size: 90%;">Here's a proposal:
</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:33 UTC</span>

<span style="font-size: 90%;">Maybe for the full bypasses, but the rest are basically normal bypasses and that's daily business and I do not see the need to keep them confidential until an eventual release.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:34 UTC</span>

<span style="font-size: 90%;">The private repo would be a copy of the public repo at the beginning</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:04 UTC</span>

<span style="font-size: 90%;">Nice proposal (minus the release v4), but I think it's risky to freeze.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:06 UTC</span>

<span style="font-size: 90%;">Well, as long as the full bypasses aren't huge, merging them all back later should be ok.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:48 UTC</span>

<span style="font-size: 90%;">Minus v4 because I do not see us do a milestone release with known bypasses, daily business or not.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:18 UTC</span>

<span style="font-size: 90%;">But maybe we need to be creative / eat painkillers and push through like you propose. Really not sure.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:49 UTC</span>

<span style="font-size: 90%;">So, "low" gets committed to the public repo, along with tests.
Anything higher than low goes in a private repo. Right?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:29:54 UTC</span>

<span style="font-size: 90%;">What do you mean "no v4"? v4 would contain the fixes for the bypasses, wouldn't it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:21 UTC</span>

<span style="font-size: 90%;">What we can do - and probably should do - is create private fixes for the full bypasses, backport them and then release updates for the old release trees - together with merging them into the v4 tree in public.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:30:43 UTC</span>

<span style="font-size: 90%;">How confident are we that multiple lows don't chain together to make a high/critical? This is something good pentestets do all the time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">_@maxleske_ yes absolutely. But I think we can not release v4 with only the criticals fixed and the highs kept private or listed in a known issues file.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:31:32 UTC</span>

<span style="font-size: 90%;">usually lows are "missing words in that wordlist" or something similar</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:33 UTC</span>

<span style="font-size: 90%;">I agree. I was thinking of v4 release containing everything</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:52 UTC</span>

<span style="font-size: 90%;">OK. Then I got your proposal wrong. Glad we agree.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:34 UTC</span>

<span style="font-size: 90%;"> Just to be clear, do we want to create GH issues for medium issues as well?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:40 UTC</span>

<span style="font-size: 90%;">_@walter_ and _@fzipitria_ what do you think? Private development of full bypass fixes, backporting and then release of old release lines, while we withhold v4?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:57 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Not sure about the issue question.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:15 UTC</span>

<span style="font-size: 90%;">We should definitely use slack threads for topics</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:27 UTC</span>

<span style="font-size: 90%;">It is very confusing if not</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">we're IRC nostalgic</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:52 UTC</span>

<span style="font-size: 90%;">(sorry. I hate threads :sweat_smile: )</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">Yeah, threads get confusing quickly.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">Then ¯\\\_(ツ)\_/¯</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:03 UTC</span>

<span style="font-size: 90%;">I second _@maxleske_</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:08 UTC</span>

<span style="font-size: 90%;">I think working in a private repo might just work, but for how long can we do this? I don’t know how much time we will need.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:24 UTC</span>

<span style="font-size: 90%;">We need the time we need</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:27 UTC</span>

<span style="font-size: 90%;">No need to freeze the public repo I think.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:42 UTC</span>

<span style="font-size: 90%;">No, but we need to be consistent and rebase quickly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:08 UTC</span>

<span style="font-size: 90%;">That is correct. We will see which rules are affected quickly though. Also: Probably mostly new rules for the Criticals.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:31 UTC</span>

<span style="font-size: 90%;">I think we need to act quickly. This is involving a lot of people and it is difficult to keep this confidential.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:35:51 UTC</span>

<span style="font-size: 90%;">What we should not do (note to self): make huge changes to the repo, like rewrite comments etc. That will make our lives painful</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:05 UTC</span>

<span style="font-size: 90%;">So rather work on this with most of our resources.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:11 UTC</span>

<span style="font-size: 90%;">We should merge that asap</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:23 UTC</span>

<span style="font-size: 90%;">"that"?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:23 UTC</span>

<span style="font-size: 90%;">will do</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:23 UTC</span>

<span style="font-size: 90%;">But the problem is that we still need to merge the PRs from the BB</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:34 UTC</span>

<span style="font-size: 90%;">(the comment stuff)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:40 UTC</span>

<span style="font-size: 90%;">Ah, got you. Thanks.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:41 UTC</span>

<span style="font-size: 90%;">Otherwise there will be conflicts</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:52 UTC</span>

<span style="font-size: 90%;">And we can’t ask people to rebase</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:59 UTC</span>

<span style="font-size: 90%;">They might be unresponsive</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:03 UTC</span>

<span style="font-size: 90%;">Yep, and also the PRs from the BB might have to be prioritized up a little bit, because the hackers will go on do other things with their time.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:37:10 UTC</span>

<span style="font-size: 90%;">Some already are unresponsive :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:17 UTC</span>

<span style="font-size: 90%;">Let's merge those quickly if we can and then setup the private repo for the criticals.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:22 UTC</span>

<span style="font-size: 90%;">That’s why we need to merge those quickly</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:22 UTC</span>

<span style="font-size: 90%;">OK!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:27 UTC</span>

<span style="font-size: 90%;">Confirmation: All fixes for the criticals will be released together if we can. Maybe without those where a fix is not in our hands. Correct?</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:40 UTC</span>

<span style="font-size: 90%;">Yes! :pray:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:46 UTC</span>

<span style="font-size: 90%;">I will go through the open PR's and check what needs to be merged now (low hanging fruit)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:02 UTC</span>

<span style="font-size: 90%;">Very good. I have a clearer picture now. Thank you all.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:34 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ _@walter_ I'm still not clear on issue criticality. Are only "critical" issues private? Or everything above "low"? -> GH issues in the public repo only for "low" issues?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:28 UTC</span>

<span style="font-size: 90%;">Personally, I think only the criticals should be private. But I wonder wether we want to open issues with a description / PoC payload for High and Medium.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:09 UTC</span>

<span style="font-size: 90%;">Not high?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:20 UTC</span>

<span style="font-size: 90%;">¯\\\_(ツ)\_/¯</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">high contains full bypass too...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:14 UTC</span>

<span style="font-size: 90%;">If it's not a full bypass I would treat it as daily business.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ Critical has only been decided on 45 min ago. Full bypasses still have to be moved to critical.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:18 UTC</span>

<span style="font-size: 90%;">Under normal circumstances, I'd keep it confidential, but we are try to avoid drowning here and we need to make compromises to stay afloat as a project.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:45:29 UTC</span>

<span style="font-size: 90%;">so agree with _@dune73_</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:45:30 UTC</span>

<span style="font-size: 90%;">So, if it's daily business, then let's create GH issues too, so we can work like always.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:07 UTC</span>

<span style="font-size: 90%;">:face_with_head_bandage:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:23 UTC</span>

<span style="font-size: 90%;"></span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:26 UTC</span>

<span style="font-size: 90%;">Is that correct?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:36 UTC</span>

<span style="font-size: 90%;">non-critical and that not involve TW...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:46:58 UTC</span>

<span style="font-size: 90%;">one of the high it might need TW actions....</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:58 UTC</span>

<span style="font-size: 90%;">Yes. And I think Max is right that it's easier for us to create issues as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:49 UTC</span>

<span style="font-size: 90%;">But can we do the issues without the PoC payload in public? At least that. I mean people are seriously depending on us and if we publish SQLi bypasses at high PL without providing a fix immediately ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:48:09 UTC</span>

<span style="font-size: 90%;">Sure, we all have access to intigrity</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:49:04 UTC</span>

<span style="font-size: 90%;">I'm still not sure about the tests. How do we split the tests if we don't want to publish payloads?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:49:19 UTC</span>

<span style="font-size: 90%;">Maybe it's simpler than I'm imagining…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:56 UTC</span>

<span style="font-size: 90%;">Tests are meant to go into a separate private, non-connected repo. When you write the PR to fix the finding, you fetch the test and add it to your PR.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:30 UTC</span>

<span style="font-size: 90%;">Once we think we have fixed everything, we can run the full bug bounty test suite and everything should be blocked and we can archive  that separate repo.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:50:48 UTC</span>

<span style="font-size: 90%;">ouch</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:51:13 UTC</span>

<span style="font-size: 90%;">How do you do that, though? I don't follow how you can write and submit a 'finished' PR in public if you aren't testing it.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:21 UTC</span>

<span style="font-size: 90%;">but you mean, testing using GH action as well? not in our local env?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:51:36 UTC</span>

<span style="font-size: 90%;">How do you connect the two things, the PR and the test? Won't they be two separate issues?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:52:08 UTC</span>

<span style="font-size: 90%;">Oh, we test locally?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:11 UTC</span>

<span style="font-size: 90%;">Am I naive? I meant to test locally until you create the PR. it should pass immediately afterwards, should not it?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:52:17 UTC</span>

<span style="font-size: 90%;">Ahhhh.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:23 UTC</span>

<span style="font-size: 90%;">and maybe, if the PR contains a new rule it has comments that probably say a lot about payload and exploit</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:52:32 UTC</span>

<span style="font-size: 90%;">Why not just not worry about publishing the PoC (for the ones that aren't full bypass). If the view is this is business as usual and we're not going to have a coordinated release to fix them all, it'll be hard for end users to patch a continuous drip feed of fixes, and PoC can soon be inferred from fixes</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:19 UTC</span>

<span style="font-size: 90%;">But it's still better to have a fix in the repo than a known PoC without a fix.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:50 UTC</span>

<span style="font-size: 90%;">Maybe I was exaggerating with the business as usual a bit. I mean when we get a high rule bypass via mail at [security@coreruleset.org](mailto:security@coreruleset.org), it's not really business as usual. It's just that the stream of bug bounty findings made me consider these as relatively tame when compared to the ciriticals.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:54:50 UTC</span>

<span style="font-size: 90%;">But a fix that isn't back ported is pretty inaccessible to most users</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:29 UTC</span>

<span style="font-size: 90%;">Pretty inaccessible to most users, but maybe not so much to integrators who have the capacity to backport themselves.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:26 UTC</span>

<span style="font-size: 90%;">So what do we decide here. I'm really torn. I would like to keep things simple. Still, we can add PoC to the spreadsheet easily and I would hate to have sponsors go crazy over the publication of PoCs without a fix.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:55 UTC</span>

<span style="font-size: 90%;">Their perspective is entirely different and they might only see the tip of the iceberg.</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:04 UTC</span>

<span style="font-size: 90%;">Sorry, I made an error in the sheet. Here is the new sheet: [https://docs.google.com/spreadsheets/d/1kITamNJajR_zVsDuRxQ0Xw2D0agMAuCW/edit#gid=154264918](https://docs.google.com/spreadsheets/d/1kITamNJajR_zVsDuRxQ0Xw2D0agMAuCW/edit#gid=154264918)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:35 UTC</span>

<span style="font-size: 90%;">_@walter_ You found the best solution: delete the spreadsheet! Job done.</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:43 UTC</span>

<span style="font-size: 90%;">:sweat_smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:45 UTC</span>

<span style="font-size: 90%;">:partying_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:38 UTC</span>

<span style="font-size: 90%;">So, how should we proceed? I created a column “Assigned” in the sheet, maybe those who take up an issue put their name there?</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:22 UTC</span>

<span style="font-size: 90%;">I would volunteer to help the hackers finish their PRs, or fix them myself if they are unresponsive. So I would put my name there.</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:39 UTC</span>

<span style="font-size: 90%;">But if others are already working with hackers, please put your name there :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:00 UTC</span>

<span style="font-size: 90%;">How about this: we tackle critical and low first. Then we can concentrate on working on the medium ones together one at a time.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:15 UTC</span>

<span style="font-size: 90%;">I think that would be a smart move.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:27 UTC</span>

<span style="font-size: 90%;">great idea.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:30 UTC</span>

<span style="font-size: 90%;">Are there any specific PRs we need to talk through tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:37 UTC</span>

<span style="font-size: 90%;">?</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:04:37 UTC</span>

<span style="font-size: 90%;">That way we can get clean fixes and backports out and coordinate</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:43 UTC</span>

<span style="font-size: 90%;">If we're lucky we will have sorted out the duplicates and the existing PRs by that time and there are only a reasonable amount of HIGHs and MEDIUMs left afterwards.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:22 UTC</span>

<span style="font-size: 90%;">I don't have anything from my side to look at I think</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:30 UTC</span>

<span style="font-size: 90%;">oh, there are 3 issues which affect the engines?</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:36 UTC</span>

<span style="font-size: 90%;">I have to check them</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:46 UTC</span>

<span style="font-size: 90%;">I mean the another two</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:04 UTC</span>

<span style="font-size: 90%;">I think there might be more, but these seem unfixable from CRS perspective.</span>

**airween** <span style="color: grey; font-size: 90%;">20:07:18 UTC</span>

<span style="font-size: 90%;">right</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:27 UTC</span>

<span style="font-size: 90%;">Yes, let's see what TW says during the week when we give them the details.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:35 UTC</span>

<span style="font-size: 90%;">We'll see clearer afterwards.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:51 UTC</span>

<span style="font-size: 90%;">For the record: We'll involve Coraza too in that communication.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:19 UTC</span>

<span style="font-size: 90%;">From my perspective we can soon close the meeting, but there is a related item on the agenda.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:09:15 UTC</span>

<span style="font-size: 90%;">are we sure we want to send details about full bypasses? Or we'll send them just a brief of all problems?</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:23 UTC</span>

<span style="font-size: 90%;">I won’t mind. The earlier and more information the better.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:10:26 UTC</span>

<span style="font-size: 90%;">we need to send details to engine teams obviously</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:36 UTC</span>

<span style="font-size: 90%;">My plan was to do briefs and selected details for TW and those who need to know.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:51 UTC</span>

<span style="font-size: 90%;">Usually they ask when they want to know more.</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:57 UTC</span>

<span style="font-size: 90%;">Great. Then I will continue working with the hackers on their PRs to get merged as fast as possible. Tomorrow i’ll self-assign the issues in the sheet.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:01 UTC</span>

<span style="font-size: 90%;">So the item on the agenda is this: We have been bitten quite a few times in this bug bounty by incomplete word lists. That means we have an outdated list of keywords, the researchers noted, ran the diff and tried to come up with an exploit for anything in the delta. _@fzipitria_ thinks we need a process to stay on top of things.</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:26 UTC</span>

<span style="font-size: 90%;">Yes, that was a very good remark. For instance there is a github GTFObins where you can find unix commands that run other commands, in order to get around command name blockings. Ideally, we should have a process to do this. Could do it on a calendar, or when we are planning a release.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:05 UTC</span>

<span style="font-size: 90%;">I think the first step would be to assemble the sources / standards for these word lists, write them down as a comment.
And then maybe add the date in the comment when the list was last checked / updated.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:35 UTC</span>

<span style="font-size: 90%;">We could then do a calendar to check that. Or have a bot send us a reminder every n days.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:50 UTC</span>

<span style="font-size: 90%;">Or it becomes a dev-on-duty duty.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:10 UTC</span>

<span style="font-size: 90%;">Actually, that last remark was meant as a joke. :smiling_imp:</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:30 UTC</span>

<span style="font-size: 90%;">Thankfully. :slightly_smiling_face: That seems terrible.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:16:40 UTC</span>

<span style="font-size: 90%;">I would says we can “botify” this</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:16:47 UTC</span>

<span style="font-size: 90%;">The creation of the issue, I mean</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:19 UTC</span>

<span style="font-size: 90%;">I really think we should. Like we check this regularly and if we do not update, we get an automatic issue with the word list after 120 days.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:17:43 UTC</span>

<span style="font-size: 90%;">So does this mean that routine regular tasks are open now?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:18:08 UTC</span>

<span style="font-size: 90%;">Some similar things were suggested in past meetings but avoided because we didn't want to to regular tasks like this.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:18:14 UTC</span>

<span style="font-size: 90%;">I forget the other suggestions, but they were good.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:18:27 UTC</span>

<span style="font-size: 90%;">Especially if we can automate with a bot</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:51 UTC</span>

<span style="font-size: 90%;">I immediately forgot them as well. But if we really thought we would not bother, then the bug bounty has taught us a lesson.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:20:09 UTC</span>

<span style="font-size: 90%;">i like the idea to botify the wordlist issue</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:20:35 UTC</span>

<span style="font-size: 90%;">it should be done on everything... commands, sql syntax, php, nodejs, python, etc...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:51 UTC</span>

<span style="font-size: 90%;">So the botification of boring tasks is accepted. Or at least the botification of the nagging. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:11 UTC</span>

<span style="font-size: 90%;">I agree, _@theMiddle_ Whereever we have word lists.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:17 UTC</span>

<span style="font-size: 90%;">For that we need to do some work first</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:17 UTC</span>

<span style="font-size: 90%;">:+1:  Create a new repo for scrapers</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:21:32 UTC</span>

<span style="font-size: 90%;">then we'll need a bot that remind us the issue created by bots</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:21:41 UTC</span>

<span style="font-size: 90%;">But I'd postpone this until after v4</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:21:58 UTC</span>

<span style="font-size: 90%;"></span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:22:19 UTC</span>

<span style="font-size: 90%;">love it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:22 UTC</span>

<span style="font-size: 90%;">4. define a cadence for updating</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:28 UTC</span>

<span style="font-size: 90%;">I don’t want to update weekly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:22:47 UTC</span>

<span style="font-size: 90%;">but we might have quarterly releases, that at least will. update this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:21 UTC</span>

<span style="font-size: 90%;">Glad we agree on this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:44 UTC</span>

<span style="font-size: 90%;">I suggest we add this immediately where we see it, and then after v4 we try and identify word lists in a systematic way.</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:46 UTC</span>

<span style="font-size: 90%;">Also another thing that might be of interest: the bug bounty organizer is going to do a second bug bounty involving various OSS projects of which CRS is one. This will be around august. But fortunately that event will only take two days, so I don’t expect a deluge of reports like we got this time.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:24:31 UTC</span>

<span style="font-size: 90%;">Created an issue for it: [https://github.com/coreruleset/coreruleset/issues/2621](https://github.com/coreruleset/coreruleset/issues/2621)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:24:52 UTC</span>

<span style="font-size: 90%;">lol, famous last words :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:25:22 UTC</span>

<span style="font-size: 90%;">Me neither, if we fix the stuff from this one, and tell them to test against “nightly” :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:46 UTC</span>

<span style="font-size: 90%;">I really wonder if we can fix all this until mid August.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:47 UTC</span>

<span style="font-size: 90%;">but yes two days and more experience this time... it shouldn't be a pain</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:26:12 UTC</span>

<span style="font-size: 90%;">We should do the retreat early...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:26:32 UTC</span>

<span style="font-size: 90%;">next week :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:26:47 UTC</span>

<span style="font-size: 90%;">:rocket:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:27:17 UTC</span>

<span style="font-size: 90%;">We talked about doing retreats twice a year, but probably not this one</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:20 UTC</span>

<span style="font-size: 90%;">Gorgeous idea.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:56 UTC</span>

<span style="font-size: 90%;">But glad you mention. Retreat probably from Oct 29, and we're looking at Northern Italy now.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:26 UTC</span>

<span style="font-size: 90%;">Ideally somewhere around Milano (-> international airport).</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:36 UTC</span>

<span style="font-size: 90%;">Airport lobby?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:39 UTC</span>

<span style="font-size: 90%;">I had a friend with a hotel in mind, but he sold the hotel.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:28:44 UTC</span>

<span style="font-size: 90%;">Torino has an airport too :smile:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:28:44 UTC</span>

<span style="font-size: 90%;">or 1st class lounge...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:49 UTC</span>

<span style="font-size: 90%;">"Around" not "within".</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:52 UTC</span>

<span style="font-size: 90%;">For the record: Hungary was discussed too, but the political situation around Orban and the martial law got us thinking. So maybe some day in the future, but Italy this time.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:59 UTC</span>

<span style="font-size: 90%;">Our Southern Switzerland. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:03 UTC</span>

<span style="font-size: 90%;">Very close to Milano.</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:24 UTC</span>

<span style="font-size: 90%;">what about holding a weekly 20:30 meet to assign issues, talk about our progress and discuss roadbumps/controversial decisions?</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:34 UTC</span>

<span style="font-size: 90%;">for the next weeks/months</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:45 UTC</span>

<span style="font-size: 90%;">but we should need a place like hackervilla (maybe this time with more rooms and ipv4)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:00 UTC</span>

<span style="font-size: 90%;">Sounds good. But we should treat it more like a daily stand up to keep it short</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:10 UTC</span>

<span style="font-size: 90%;">Yes, it should be short</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:12 UTC</span>

<span style="font-size: 90%;">I find this works well with working together on a project remotely</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:22 UTC</span>

<span style="font-size: 90%;">(I LOVE IPv4!!)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:31:59 UTC</span>

<span style="font-size: 90%;">Every Monday then?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:18 UTC</span>

<span style="font-size: 90%;">I see the need, but I do not think I can make "every monday".</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:32:22 UTC</span>

<span style="font-size: 90%;">Ooh, the non-meeting Mondays?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:36 UTC</span>

<span style="font-size: 90%;">The non-meeting Mondays would become meeting ones ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:43 UTC</span>

<span style="font-size: 90%;">My wife will hate me.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:32:45 UTC</span>

<span style="font-size: 90%;">Then people who aren't interested in the bug squashing can stick to the regular Mondays</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:48 UTC</span>

<span style="font-size: 90%;">I think we need a bit more close contact to keep going and keep motivated</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:07 UTC</span>

<span style="font-size: 90%;">It would certainly be useful.</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:23 UTC</span>

<span style="font-size: 90%;">I’ll plan it and we’ll see who turns up :)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:33:43 UTC</span>

<span style="font-size: 90%;">It doesn't matter if not everyone shows up. Even just a few people meeting will help us keep pushing on</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:33:46 UTC</span>

<span style="font-size: 90%;">chat or video meet?</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:56 UTC</span>

<span style="font-size: 90%;">chat works fine for me..</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:34:02 UTC</span>

<span style="font-size: 90%;">oky</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:34:38 UTC</span>

<span style="font-size: 90%;">Anything else? I need to catch some sleep</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:02 UTC</span>

<span style="font-size: 90%;">then I would say, take a nice look at the list, and if you like a high priority issue, put your name on it :)</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:12 UTC</span>

<span style="font-size: 90%;">and we’ll see next Monday how we progressed</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:20 UTC</span>

<span style="font-size: 90%;">Perfect. Thank you all.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:35:51 UTC</span>

<span style="font-size: 90%;">Good night. See you next Monday!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:35:58 UTC</span>

<span style="font-size: 90%;">Night!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:02 UTC</span>

<span style="font-size: 90%;">See you around!</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:02 UTC</span>

<span style="font-size: 90%;">Is there anyone who still needs access to the Intigrity system? It can be useful to see the hacker’s full description and the discussions.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:36:36 UTC</span>

<span style="font-size: 90%;">_@dune73_ if we go for Milano, do you need some help finding a place?</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:10 UTC</span>

<span style="font-size: 90%;">Bye everyone!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:37:22 UTC</span>

<span style="font-size: 90%;">Good night</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:37:25 UTC</span>

<span style="font-size: 90%;">nite all!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:18 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ Yes, please.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:38:21 UTC</span>

<span style="font-size: 90%;">:wave: !</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:26 UTC</span>

<span style="font-size: 90%;">DM!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:38:39 UTC</span>

<span style="font-size: 90%;">yep</span>

