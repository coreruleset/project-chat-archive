### Mon, Nov 20th, 2023

**dune73** <span style="color: grey; font-size: 90%;">19:31:18 UTC</span>

<span style="font-size: 90%;">Hello, meeting time. I dearly missed you all, so who is around?</span>

**airween** <span style="color: grey; font-size: 90%;">19:31:26 UTC</span>

<span style="font-size: 90%;">hey</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:31:30 UTC</span>

<span style="font-size: 90%;">Hii</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:31:35 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:26 UTC</span>

<span style="font-size: 90%;">Hi guys, welcome _@Esad Cetiner_ nice to have you with us.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:32:32 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">Hey _@Paul Beckett_ how is it going?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:32:54 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:33:22 UTC</span>

<span style="font-size: 90%;">Life is still very chaotic and busy :(</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:25 UTC</span>

<span style="font-size: 90%;">Xanadu excused himself and theMiddle is in Japan which may serve as a good excuse...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:20 UTC</span>

<span style="font-size: 90%;">hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:23 UTC</span>

<span style="font-size: 90%;">I feel like some of the dev retreat attendees may have developed overdose.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:34 UTC</span>

<span style="font-size: 90%;">Ah no, here is _@franbuehler_. Hello!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:01 UTC</span>

<span style="font-size: 90%;">Anybody know whether _@maxleske_ and _@fzipitria_ will be here?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:07 UTC</span>

<span style="font-size: 90%;">While we wait some 2-3 additional minutes, I'd like to share somethign I developed during the weekend.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:46 UTC</span>

<span style="font-size: 90%;">I have a ChatGPT setup that allows me to summarize conference presentations on youtube into a structures JSON and then print it out as Markdown.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:10 UTC</span>

<span style="font-size: 90%;">Here is Ervin's CRS Community Summit presentation from February:
# Dashboard Or LogParser by Ervin Hegedüs

## Summary

**Presenter**: Ervin Hegedüs
**Title**: Dashboard Or LogParser
**Category**: CRS Community Summit 2023
**Link**: [[https://www.youtube.com/watch?v=Oky2UDxyfvs](https://www.youtube.com/watch?v=Oky2UDxyfvs)](https://www.youtube.com/watch?v=Oky2UDxyfvs](https://www.youtube.com/watch?v=Oky2UDxyfvs))
**Length**: n.n.

**Summary of Presentation**: Ervin Hegedüs discusses the development of a security dashboard for parsing logs from ModSecurity 2 and 3, highlighting the technical challenges and future plans.

## Ideas

* Developing a dashboard to monitor server activities using ModSecurity 2 and 3, focusing on both disruptive and non-disruptive rule triggers.
* Parsing error logs instead of audit logs to provide developers and administrators with more granular information about security events.
* Creating a tool, MST Log Parser, to parse logs and provide a structured output for better visibility and analysis.

## Quotes

* "there is no any kind of product open source or commercial product where we can check what happens on our servers"
* "we expected want to know what happens on the servers"
* "I would like to talk about how the log parsing works because it's very important"

## Facts

* ModSecurity 2 and 3 are used to monitor server activities, but there is a lack of comprehensive open-source or commercial products for detailed log analysis.
* The MST Log Parser is developed in C for performance and compatibility, with bindings for PHP, Python, Ruby, and other languages.
* The dashboard aims to provide detailed information about server activities, including non-disruptive rule triggers, which are not typically shown in audit logs.

## Resources

* GitHub Repository: The MST Log Parser project is available on GitHub under the AGPL license, indicating its open-source nature and the community's ability to contribute. The repository is a resource for those interested in the technical implementation of the log parser and for developers who may want to contribute to or use the project." 
* Dashboard Application: The dashboard application developed by Ervin Hegedüs is designed to parse and display logs from ModSecurity in a structured and user-friendly manner. The application serves as a practical tool for administrators and developers to monitor and analyze security events in real-time.

## Recommendations

* Consider integrating the MST Log Parser into security monitoring workflows to enhance visibility into server activities and potential security events.
* Explore the GitHub repository for the MST Log Parser to understand its capabilities and contribute to its development.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:29 UTC</span>

<span style="font-size: 90%;">Nothing edited.</span>

**airween** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">wow</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:11 UTC</span>

<span style="font-size: 90%;">The quotes are hard, since the automatic youtube transcripts are low quality. But I still think the results are amazing. And having done dozens of these, I got valid JSON every single time.</span>

**airween** <span style="color: grey; font-size: 90%;">19:38:36 UTC</span>

<span style="font-size: 90%;">it has been created only from the YouTube video?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">I'm here</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:08 UTC</span>

<span style="font-size: 90%;">ai-download-and-extract.sh -p "Ervin Hegedüs" -c "CRS Community Summit 2023" -t "Dashboard Or LogParser" [https://www.youtube.com/watch?v=Oky2UDxyfvs](https://www.youtube.com/watch?v=Oky2UDxyfvs)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:12 UTC</span>

<span style="font-size: 90%;">That's it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:17 UTC</span>

<span style="font-size: 90%;">Hello _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:47 UTC</span>

<span style="font-size: 90%;">-c is category, so they are saved in a structured way locally.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:39:57 UTC</span>

<span style="font-size: 90%;">I thought chatgpt didn't have access to the internet, or are you downloading the subtitles and sending it to chatgpt?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:17 UTC</span>

<span style="font-size: 90%;">I get the subtitles via youtube API. That's super simple.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:23 UTC</span>

<span style="font-size: 90%;">The rest is also super simple.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:41 UTC</span>

<span style="font-size: 90%;">I had the first version after 2h or so. The rest was an exercise is cleaning things up.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:41:37 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:39 UTC</span>

<span style="font-size: 90%;">What you see above is the result of some 200-400 lines of code with 4 essential lines and a long prompt. Security blogger Daniel Miessler gave me the inspiration.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:45 UTC</span>

<span style="font-size: 90%;">Hello _@azurIt_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:09 UTC</span>

<span style="font-size: 90%;">Either way, not really our topic, but it might allow us to make our talks - any talks - more accessible.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:51 UTC</span>

<span style="font-size: 90%;">But before we leave this, here is a funny quote form Xanadu's talk. Youtube transcript got this wrong: "If a company wants to comply with PCI DSS they will have to install a wife in front of their web application."</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:05 UTC</span>

<span style="font-size: 90%;">So let's get started.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:19 UTC</span>

<span style="font-size: 90%;">We have a brief agenda, published at [https://github.com/coreruleset/coreruleset/issues/3385](https://github.com/coreruleset/coreruleset/issues/3385)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:27 UTC</span>

<span style="font-size: 90%;">Anything else to add?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:23 UTC</span>

<span style="font-size: 90%;">I do not see any additional topics, then let's look at the dev retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:44 UTC</span>

<span style="font-size: 90%;">The frontpage of the wiki lists all the topics.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:45:49 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/wiki](https://github.com/coreruleset/coreruleset/wiki)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:32 UTC</span>

<span style="font-size: 90%;">We tried to run 4 weeklong projects, 1 had to be dropped immediately because it proved to be impossible as of right now ([Cyclomatic Complexity](https://github.com/coreruleset/coreruleset/wiki/DevRetreat23ProjectCyclomaticComplexity)).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:07 UTC</span>

<span style="font-size: 90%;">The integration of ModSec3 / Coraza into our CI and the Status Page got a lot of attention with many people working on them.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:07 UTC</span>

<span style="font-size: 90%;">And the testing of FPs on a scale brought the most important results with regards to CRSv4. Xanadu worked on this and was able to identify several big sources of FPs. Issues are planned to be submitted during the week.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:20 UTC</span>

<span style="font-size: 90%;">The ModSec3 integration into our CI had 3-4 people look into a lot of ModSec3 deviations. This was mind blowing and _@airween_ is now assembling a (extending an existing) list that should improve the situation going forward.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:53 UTC</span>

<span style="font-size: 90%;">On the status page front we are able to detect if an individual rule is active or not on a service for 80% of our CRSv4 rules.</span>

**airween** <span style="color: grey; font-size: 90%;">19:50:06 UTC</span>

<span style="font-size: 90%;">Perhaps it takes a bit more time, because I've started to review the results, and I'm afraid there are some other bugs in libmodsecurity3... :disappointed:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:44 UTC</span>

<span style="font-size: 90%;">We have a platform that tests this automatically for Azure and almost as polished for Cloudflare and a PoC dashboard that displays the results.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:10 UTC</span>

<span style="font-size: 90%;">The status page won't be published immediately, but we have a PoC that covers all the important aspects.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:58 UTC</span>

<span style="font-size: 90%;">Then we spent a lot of time talking about a new rule language, this is taking up steam now - people interested in that discussion are welcome to join - and then we talked about a new name.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:59 UTC</span>

<span style="font-size: 90%;">The new name discussion had some groundhog day vibes too it and after days and days of talking we voted and got a tie. Almost everybody agreed that ModSecurity should be removed from the name, but then there was a progressive camp that wanted to adopt something completely new. And a more conservative camp of equal size that wanted to stick closer to Core Rule Set.
Since we were unable to agree and since we do not want to stick to ModSec in our name, the immediate solution is to do a minimal name change with removing ModSec from the name and using primarily CRS as our name (and pushing the Core Rule Set into the background). Chances are a new discussion will take place at the dev retreat 2024 and that a fully new name will then win.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:22 UTC</span>

<span style="font-size: 90%;">Did I describe this correctly? Please correct me if I'm wrong.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:27 UTC</span>

<span style="font-size: 90%;">And we will also adopt a new release policy starting CRS v4. It will probably mean that will do releases in a monthly rhythm and that we will define releases as LTS about once a year or so. LTS releases will get FP fixes and backports of security fixes.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:42 UTC</span>

<span style="font-size: 90%;">I think these are the core facts about the dev retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:05 UTC</span>

<span style="font-size: 90%;">The not so core items were a wonderful afternoon on Buda Castle hill with a splendid dinner.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:42 UTC</span>

<span style="font-size: 90%;">And then an impressive visit of the "House of Terror" museum and another splendid dinner (mainly in terms of quantity).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:55 UTC</span>

<span style="font-size: 90%;">And a lot of Jacuzzi and card games. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:41 UTC</span>

<span style="font-size: 90%;">Typing all this down still feels exhausting. Did I miss anyhting?</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:54 UTC</span>

<span style="font-size: 90%;">Most important discussions happened in Jacuzzi, of course.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:35 UTC</span>

<span style="font-size: 90%;">All the important discussions happened in the Jacuzzi. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:59 UTC</span>

<span style="font-size: 90%;">Here is me in front of the 2nd splendid restaurant.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:19 UTC</span>

<span style="font-size: 90%;">Please do not tell my medieval reenactment friends I went into a restaurant called "Sir Lancelot".</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:13 UTC</span>

<span style="font-size: 90%;">_@airween_ Do you want to add anything about the Dev retreat?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:56 UTC</span>

<span style="font-size: 90%;">It was an amazing week!! And Ervin did a wonderful job organizing it!
Thank you again. I felt really comfortable! The hotel, the trips to Budapest, the running... everything was just great!</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:30 UTC</span>

<span style="font-size: 90%;">with Franziska we founded the CRS Runner's Division. Anyone can join us on next retreats :slightly_smiling_face:</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">20:04:16 UTC</span>

<span style="font-size: 90%;">Wasn't that a source of your headaches? :wink:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:05:32 UTC</span>

<span style="font-size: 90%;">I don't think so :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:03:41 UTC</span>

<span style="font-size: 90%;">yes!!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:05 UTC</span>

<span style="font-size: 90%;">Well, I might stick with "Team Jacuzzi" if I am honest ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:26 UTC</span>

<span style="font-size: 90%;">But seriously _@airween_, very good job and very good choice of the restaurant hotel.</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:33 UTC</span>

<span style="font-size: 90%;">btw I think your summary is excellent and accurate</span>

**airween** <span style="color: grey; font-size: 90%;">20:04:57 UTC</span>

<span style="font-size: 90%;">thank you guys, I really enjoyed to organize this retreat for you. Really</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:06:59 UTC</span>

<span style="font-size: 90%;">And also thank you Christian for organizing this week!
You did a lot of work too :heart:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:13 UTC</span>

<span style="font-size: 90%;">Payments with OWASP and so on...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:02 UTC</span>

<span style="font-size: 90%;">Thank you. Appreciated. I really enjoyed this (even if the name change discussion took me to the edge ...)</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:08:39 UTC</span>

<span style="font-size: 90%;">:wave: Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:49 UTC</span>

<span style="font-size: 90%;">Hello _@Christian Treutler_, welcome to the chat.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:57 UTC</span>

<span style="font-size: 90%;">We just reviewed the dev retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:11 UTC</span>

<span style="font-size: 90%;">Thank you for joining and launching the rule language discussion anew.</span>

**Christian Treutler** <span style="color: grey; font-size: 90%;">20:10:00 UTC</span>

<span style="font-size: 90%;">My pleasure.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:48 UTC</span>

<span style="font-size: 90%;">OK, then let's move back to the agenda.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:03 UTC</span>

<span style="font-size: 90%;">CRSv4 RC2 has been out for a couple of weeks, but we hardly get any FP reports.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:28 UTC</span>

<span style="font-size: 90%;">The work of Xanadu during the dev retreat underlined there is a substantial amount of FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:49 UTC</span>

<span style="font-size: 90%;">His work concentrates on ARGS though. I think we will be able to address that in coming weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:25 UTC</span>

<span style="font-size: 90%;">But I am unsure of 92xxxx rules. I really fear we dump users into the pit with too many FPs in our 4.0 release.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:30 UTC</span>

<span style="font-size: 90%;">What do you all think?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:12:46 UTC</span>

<span style="font-size: 90%;">Which serial number is going to be the last RC?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:56 UTC</span>

<span style="font-size: 90%;">We have not decided this, but I see a substantial chance for a RC3.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:15:08 UTC</span>

<span style="font-size: 90%;">I don't think there are many false positives with the 92xxxx range, the 932xxx and 942xxx is where I've found most false positives.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:18 UTC</span>

<span style="font-size: 90%;">We also need to get a feeling for the quantitative testing on ARGS. This work is based on scholarly defined standard English sentences (for now). But that's not necessarily the same traffic a WAF gets on a freeform text input.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:48 UTC</span>

<span style="font-size: 90%;">The exception in to 92xxxx range being restricted headers, but I think we weeded that out.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:43 UTC</span>

<span style="font-size: 90%;">FYI: I am running CRS in prod on [netnea.com](http://netnea.com). And I had a tutorial reader complain tonight since the server banned him after he triggered 3-4 FPs... I really need to check the reports of the last few weeks.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:13 UTC</span>

<span style="font-size: 90%;">_@emphazer_ I think you are testing too, are you not? What is your impression? Only application rules triggering on ARGS and silly headers, or also protocol rules?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:43 UTC</span>

<span style="font-size: 90%;">Well, no news about FPs then.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:08 UTC</span>

<span style="font-size: 90%;">But we have a backport of the 3.3.5 release to the 3.2.x release line.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:30 UTC</span>

<span style="font-size: 90%;">Created by _@emphazer_. Did anybody take a closer look?</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:22:14 UTC</span>

<span style="font-size: 90%;">The most was ARGS and  ARGS_NAMES
</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:25 UTC</span>

<span style="font-size: 90%;">So Xanadu is right on track with this work.</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:23:50 UTC</span>

<span style="font-size: 90%;">There are still some changes to do. But was really busy the past 3 weeks. But finally at December my big project at my company is done</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:19 UTC</span>

<span style="font-size: 90%;">For those not at the dev summit: He ran 10K example standard phrases against CRS and calculated the number of FPs for every rule. There was an FP with "At ". Bringing one of the RCE rules to 9.8% of FPs.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:53 UTC</span>

<span style="font-size: 90%;">The idea would now be to push this down far below 1%. Ideally 0.01% (1 in 10K POST requests).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:12 UTC</span>

<span style="font-size: 90%;">That project kept you busy!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:25:38 UTC</span>

<span style="font-size: 90%;">That would be great</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:44 UTC</span>

<span style="font-size: 90%;">For PL1 apparently.</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:25:56 UTC</span>

<span style="font-size: 90%;">Yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:19 UTC</span>

<span style="font-size: 90%;">We do not want to delay 4.0 for too long of course, but if this approach is successful, we can do the same with other languages and raise the number of requests. There are samples with 1M hand-selected English sentences.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:36 UTC</span>

<span style="font-size: 90%;">As for 3.2.x, I think there is no rush (anymore). It would be OK to time the release together with 4.0. Or what do you think?</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:30:05 UTC</span>

<span style="font-size: 90%;">Sure</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:36 UTC</span>

<span style="font-size: 90%;">Other opinions? Or other things to talk about here?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:46 UTC</span>

<span style="font-size: 90%;">If there is nothing else to add, then I guess, we'll just close the meeting here.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:53 UTC</span>

<span style="font-size: 90%;">Thank you all for joining and good night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:34:05 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:34:07 UTC</span>

<span style="font-size: 90%;">Good night</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:34:09 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">20:34:20 UTC</span>

<span style="font-size: 90%;">Good Morning! (for me)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:41 UTC</span>

<span style="font-size: 90%;">Good Night!</span>

**airween** <span style="color: grey; font-size: 90%;">20:35:54 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:37:45 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**maxleske** <span style="color: grey; font-size: 90%;">21:05:36 UTC</span>

<span style="font-size: 90%;">Sorry, forgot about the meeting!</span>

**jit** <span style="color: grey; font-size: 90%;">21:16:08 UTC</span>

<span style="font-size: 90%;">Slept early, and I missed the meeting. :( 
Goodnight everyone.</span>

