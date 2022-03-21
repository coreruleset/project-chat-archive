### Mon, Feb 4th, 2019

**csanders** <span style="color: grey; font-size: 90%;">19:30:09 UTC</span>

<span style="font-size: 90%;">hey _@theMiddle_</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:17 UTC</span>

<span style="font-size: 90%;">a lot of folks are sick or busy today</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:21 UTC</span>

<span style="font-size: 90%;">but i think we have a good agenda!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:30:49 UTC</span>

<span style="font-size: 90%;">yeah, lot of PRs and new issues!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:55 UTC</span>

<span style="font-size: 90%;">yup</span>

**csanders** <span style="color: grey; font-size: 90%;">19:30:56 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:00 UTC</span>

<span style="font-size: 90%;">some good, some bad :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:31:08 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">19:31:13 UTC</span>

<span style="font-size: 90%;">lets wait just a few to see if others joiin</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:31:25 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:38 UTC</span>

<span style="font-size: 90%;">Hi everybody!</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:53 UTC</span>

<span style="font-size: 90%;">Hello all! I’ll be here for a short while, but still failing a health checks, so probably a bit shorter and less useful than normal :stuck_out_tongue:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:00 UTC</span>

<span style="font-size: 90%;">hi _@franbuehler_, hi _@walter_ :wave::skin-tone-2:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:32:05 UTC</span>

<span style="font-size: 90%;">hi folks!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:02 UTC</span>

<span style="font-size: 90%;">lets start this bad boy off</span>

**fgs** <span style="color: grey; font-size: 90%;">19:33:09 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:14 UTC</span>

<span style="font-size: 90%;">hi _@fgs_</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:20 UTC</span>

<span style="font-size: 90%;">hi _@fgs_!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:33:37 UTC</span>

<span style="font-size: 90%;">_@csanders_ I did not have the time to check your messages on Slack, sorry! I will check them this week.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:42 UTC</span>

<span style="font-size: 90%;">it's all good</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">i just am seeing your issue about docker now :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:33:53 UTC</span>

<span style="font-size: 90%;">but i think i got most of those</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:02 UTC</span>

<span style="font-size: 90%;">so this will be good :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:21 UTC</span>

<span style="font-size: 90%;">i pivoted to something else in the meantime and we can catch up this week or so</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:25 UTC</span>

<span style="font-size: 90%;">so anyhow lets jump into this</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:29 UTC</span>

<span style="font-size: 90%;">Release 3.1.1 release because of [#1276](https://github.com/coreruleset/coreruleset/issues/#1276) (JWall compatibility)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:34:47 UTC</span>

<span style="font-size: 90%;">I know we talked about a 3.1.1 release earlier</span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:11 UTC</span>

<span style="font-size: 90%;">I have no problem packaging this now if folks don't want to cherry pick anything</span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">_@walter_ one of the things to consider here is what we'll do about [#1277](https://github.com/coreruleset/coreruleset/issues/#1277)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:37 UTC</span>

<span style="font-size: 90%;">AKA GeoIP</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:35:38 UTC</span>

<span style="font-size: 90%;">hello everybody </span>

**csanders** <span style="color: grey; font-size: 90%;">19:35:41 UTC</span>

<span style="font-size: 90%;">hey _@emphazer_</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:02 UTC</span>

<span style="font-size: 90%;">I see I closed [#1277](https://github.com/coreruleset/coreruleset/issues/#1277) so :wink: do we need to do something?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:13 UTC</span>

<span style="font-size: 90%;">i know you made some changes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:22 UTC</span>

<span style="font-size: 90%;">do you want to backport to 3.1.1?</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:25 UTC</span>

<span style="font-size: 90%;">oh wait I thought we were going to thank _@emphazer_ for making the geoIP converter by asking him to write a blog :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:39 UTC</span>

<span style="font-size: 90%;">haha (yes also that, it was awesome</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:36:40 UTC</span>

<span style="font-size: 90%;">haha</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:41 UTC</span>

<span style="font-size: 90%;">oh that update tool? yeah get rid of it in 3.1.1 :+1: it’s an oversight that we left it in for 3.1</span>

**csanders** <span style="color: grey; font-size: 90%;">19:36:42 UTC</span>

<span style="font-size: 90%;">i've used it once :wink:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:04 UTC</span>

<span style="font-size: 90%;">okay i'll take responsiblity for making a PR to remove the stuff from the 3.1x branch</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:14 UTC</span>

<span style="font-size: 90%;">anything else we think needs to go into 3.1.x</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:25 UTC</span>

<span style="font-size: 90%;">i.e things that won't break existing compatibility</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:37:35 UTC</span>

<span style="font-size: 90%;">since the last update on github.  I recommend for everybody to re run the script!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:37:44 UTC</span>

<span style="font-size: 90%;">:-X okay :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:03 UTC</span>

<span style="font-size: 90%;">hmmmm</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:38:27 UTC</span>

<span style="font-size: 90%;">btw I'm writing currently on a blog post. and I will explain why</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:32 UTC</span>

<span style="font-size: 90%;">cool!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:25 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:39:51 UTC</span>

<span style="font-size: 90%;">but believe me guys. pls re run it.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:39:58 UTC</span>

<span style="font-size: 90%;">i will tonight :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:01 UTC</span>

<span style="font-size: 90%;">okay, i'm not hearing anything else to add to 3.1.1</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:16 UTC</span>

<span style="font-size: 90%;">so i will remove the scripts and package it out as well</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:24 UTC</span>

<span style="font-size: 90%;">moving quickly</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:31 UTC</span>

<span style="font-size: 90%;">_@walter_ i know there was talk about Cloudfest workshop</span>

**csanders** <span style="color: grey; font-size: 90%;">19:40:43 UTC</span>

<span style="font-size: 90%;">I wasn't involved in the discussion any idea what _@dune73_ was planning?</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:01 UTC</span>

<span style="font-size: 90%;">we will have a CRS hackathon, emphazer and I will be hosting it</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:41:08 UTC</span>

<span style="font-size: 90%;">cool!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:09 UTC</span>

<span style="font-size: 90%;">oh, AWESOME!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:41:16 UTC</span>

<span style="font-size: 90%;">care to share details about when/wherE?</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:18 UTC</span>

<span style="font-size: 90%;">there will be some Open-Source-Hacker and on the first day they get to choose a project</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:24 UTC</span>

<span style="font-size: 90%;">so we don’t know how many people will choose us :sweat_smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:30 UTC</span>

<span style="font-size: 90%;">but I guess we should have a good presentation :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:34 UTC</span>

<span style="font-size: 90%;"><https://www.cloudfest.com/hackathon></span>

**walter** <span style="color: grey; font-size: 90%;">19:41:36 UTC</span>

<span style="font-size: 90%;">we are on here!</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:10 UTC</span>

<span style="font-size: 90%;">it’s free and you even get the hotel and train (within Germany) free so please come :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:42:18 UTC</span>

<span style="font-size: 90%;">Really awesome!</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:24 UTC</span>

<span style="font-size: 90%;">you can even attend the main cloudfest conference after</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:25 UTC</span>

<span style="font-size: 90%;">the date is March 23-25</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:33 UTC</span>

<span style="font-size: 90%;">yes!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:37 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:53 UTC</span>

<span style="font-size: 90%;">it’s really in the south of Germany, it’s almost near Basel</span>

**csanders** <span style="color: grey; font-size: 90%;">19:42:58 UTC</span>

<span style="font-size: 90%;">sounds like a great opportunity if you're over there!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">ouch, I’m at codemotion at Rome in that days</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:01 UTC</span>

<span style="font-size: 90%;">really crazy, I didn’t know Germany was that big</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:43:17 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">19:43:22 UTC</span>

<span style="font-size: 90%;">lol</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:28 UTC</span>

<span style="font-size: 90%;">so we don’t really know what kind of people will come to us… cloudfest as a whole is aimed at network/sysadmins/hosters… so maybe we get a lot of sysadmins (who could help us on documentation, exclusion sets), but maybe we get python coders who can help us develop tooling</span>

**Slackbot** <span style="color: grey; font-size: 90%;">19:44:29 UTC</span>

<span style="font-size: 90%;">The OWASP developer guide: <https://www.owasp.org/index.php/OWASP_Guide_Project></span>

**csanders** <span style="color: grey; font-size: 90%;">19:44:52 UTC</span>

<span style="font-size: 90%;">haha, thanks slackbot?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:45:14 UTC</span>

<span style="font-size: 90%;">alright any other details you want to add?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:45:28 UTC</span>

<span style="font-size: 90%;">Thanks _@walter_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:46 UTC</span>

<span style="font-size: 90%;">it will probably be cool so if you’re around, come hack with us!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:15 UTC</span>

<span style="font-size: 90%;">Ok, and you say everything is free? Hotel and train too?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:15 UTC</span>

<span style="font-size: 90%;">perfect, speaking of places to come hack with us... our next topic is AppSecGlobal Tel Aviv</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:33 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ yes, apparently it’s all sponsored!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:39 UTC</span>

<span style="font-size: 90%;">Wow!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:46:43 UTC</span>

<span style="font-size: 90%;">I will think about it!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:46:57 UTC</span>

<span style="font-size: 90%;">I know some people are thinking of submitting presentations to AppSecGlobal Tel Aviv</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:01 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:47:02 UTC</span>

<span style="font-size: 90%;">you only have to get to the German border</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:02 UTC</span>

<span style="font-size: 90%;">I plan to be there (i think)</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:18 UTC</span>

<span style="font-size: 90%;">I’m also interested to join in Tel Aviv!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:29 UTC</span>

<span style="font-size: 90%;">I'm not quite sure about what my talk should be</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:37 UTC</span>

<span style="font-size: 90%;">I think _@walter_ was also planning a talk</span>

**csanders** <span style="color: grey; font-size: 90%;">19:47:39 UTC</span>

<span style="font-size: 90%;">(CFP)</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:01 UTC</span>

<span style="font-size: 90%;">no I unplanned that :stuck_out_tongue: don’t have the energy and time to make it good. maybe next year!</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:22 UTC</span>

<span style="font-size: 90%;">haha, well i'm fine with making a talk about CRS possibly about setting up honeypots at scale</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:33 UTC</span>

<span style="font-size: 90%;">if anyone is interested i'm considering that</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:42 UTC</span>

<span style="font-size: 90%;">PM me</span>

**csanders** <span style="color: grey; font-size: 90%;">19:48:50 UTC</span>

<span style="font-size: 90%;">we'd love to see folks there also :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:43 UTC</span>

<span style="font-size: 90%;">I don't know yet...</span>

**csanders** <span style="color: grey; font-size: 90%;">19:49:52 UTC</span>

<span style="font-size: 90%;">well it's not till map 26-30th</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:04 UTC</span>

<span style="font-size: 90%;">CFP ends April 10th</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:09 UTC</span>

<span style="font-size: 90%;">so stay tuned :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:17 UTC</span>

<span style="font-size: 90%;">how about we move onto the next topic</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:18 UTC</span>

<span style="font-size: 90%;">CRS swag, proposal by @fzipi</span>

**csanders** <span style="color: grey; font-size: 90%;">19:50:26 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ you around?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:23 UTC</span>

<span style="font-size: 90%;">guessing no</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:27 UTC</span>

<span style="font-size: 90%;">we'll see if he shows up in a bit</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:33 UTC</span>

<span style="font-size: 90%;">so moving onto the next point</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:33 UTC</span>

<span style="font-size: 90%;">[#1277](https://github.com/coreruleset/coreruleset/issues/#1277) GeoIP deprecated their old database, so our upgrade script and our documentation are currently not valid.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:51:43 UTC</span>

<span style="font-size: 90%;">which _@emphazer_ has pretty much solved for us</span>

**csanders** <span style="color: grey; font-size: 90%;">19:52:09 UTC</span>

<span style="font-size: 90%;">any additional comments on that ?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:52:53 UTC</span>

<span style="font-size: 90%;">No. Blog post is pending, right?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:53:06 UTC</span>

<span style="font-size: 90%;">yes</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:16 UTC</span>

<span style="font-size: 90%;">:stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:21 UTC</span>

<span style="font-size: 90%;">alright</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:25 UTC</span>

<span style="font-size: 90%;">last topic before we get to PRs</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:26 UTC</span>

<span style="font-size: 90%;">Core Rule Set Container discussion: [#1290](https://github.com/coreruleset/coreruleset/issues/#1290)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:34 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ I think i agree with you on ALL of these</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:39 UTC</span>

<span style="font-size: 90%;">and I think we'll add them</span>

**csanders** <span style="color: grey; font-size: 90%;">19:53:50 UTC</span>

<span style="font-size: 90%;">my only question now for _@franbuehler_ and the rest of the channel</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:03 UTC</span>

<span style="font-size: 90%;">do you think it makes sense to remove the seperate owasp/core-rule-set dockerhub repo</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:12 UTC</span>

<span style="font-size: 90%;">and just make a -crs tag for owasp/modsecurity</span>

**csanders** <span style="color: grey; font-size: 90%;">19:54:23 UTC</span>

<span style="font-size: 90%;">anyone have any feelings one way or the other?</span>

**csanders** <span style="color: grey; font-size: 90%;">19:55:20 UTC</span>

<span style="font-size: 90%;">alright, i'm not hearing much so i'll make that decision offline with _@franbuehler_</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:01 UTC</span>

<span style="font-size: 90%;">In the owasp/core-rule-set dockerhub repo you have more Dockerfiles, right?</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:04 UTC</span>

<span style="font-size: 90%;">I have no comments on it, which is good news :stuck_out_tongue:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:56:22 UTC</span>

<span style="font-size: 90%;">yeah but we can add a number of tags</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:22 UTC</span>

<span style="font-size: 90%;">my best wish is to change engines from apache to nginx…</span>

**csanders** <span style="color: grey; font-size: 90%;">19:56:30 UTC</span>

<span style="font-size: 90%;">i think we're gonna support both</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:41 UTC</span>

<span style="font-size: 90%;">airween has done amazing work trying to get our CRS tests to work on nginx, and he has found a number of libmodsec bugs :see_no_evil:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:56:44 UTC</span>

<span style="font-size: 90%;">Yes, support both is good, I think.</span>

**csanders** <span style="color: grey; font-size: 90%;">19:56:55 UTC</span>

<span style="font-size: 90%;">so the idea i'm floating is the following</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">the good news is, if I may summarize, that he got the number of test failures very very low</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:11 UTC</span>

<span style="font-size: 90%;">build NGINX and Apache images ontop of their repos</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:19 UTC</span>

<span style="font-size: 90%;">build version v2 and v3</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:22 UTC</span>

<span style="font-size: 90%;">for each</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:30 UTC</span>

<span style="font-size: 90%;">and provide v2 and v3 support for ubuntu as well</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:34 UTC</span>

<span style="font-size: 90%;">or debian</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:39 UTC</span>

<span style="font-size: 90%;">no feeling either way</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:41 UTC</span>

<span style="font-size: 90%;">(probably debian</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:43 UTC</span>

<span style="font-size: 90%;">but the bad news is, that debian won’t accept a high number of downstream patches, so really TW should release a fixed libmodsec3…</span>

**csanders** <span style="color: grey; font-size: 90%;">19:57:46 UTC</span>

<span style="font-size: 90%;">given _@airween_</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:05 UTC</span>

<span style="font-size: 90%;">yeah that would be awesome, but I won’t put pressure :stuck_out_tongue_winking_eye:</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:15 UTC</span>

<span style="font-size: 90%;">hi there</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:16 UTC</span>

<span style="font-size: 90%;">but _@franbuehler_ has a bunch of good feedback to add</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:24 UTC</span>

<span style="font-size: 90%;">hey _@airween_ :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:25 UTC</span>

<span style="font-size: 90%;">I'm here...</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:34 UTC</span>

<span style="font-size: 90%;">hello :smile:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:58:36 UTC</span>

<span style="font-size: 90%;">hi</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:48 UTC</span>

<span style="font-size: 90%;">just saying we may support debian over ubuntu as our first class docker image (not based on nginx/apache's)</span>

**csanders** <span style="color: grey; font-size: 90%;">19:58:52 UTC</span>

<span style="font-size: 90%;">because you are awesome</span>

**csanders** <span style="color: grey; font-size: 90%;">19:59:10 UTC</span>

<span style="font-size: 90%;">really the build steps will be the same but you never know :wink:</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:34 UTC</span>

<span style="font-size: 90%;">sorry, need to re-read the messages above.. :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">19:59:56 UTC</span>

<span style="font-size: 90%;">haha :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:36 UTC</span>

<span style="font-size: 90%;">well, if you have feedback chime in as we go</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:47 UTC</span>

<span style="font-size: 90%;">what does it mean "TW"?</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:51 UTC</span>

<span style="font-size: 90%;">TrustWave</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:54 UTC</span>

<span style="font-size: 90%;">ah</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:55 UTC</span>

<span style="font-size: 90%;">sorry</span>

**csanders** <span style="color: grey; font-size: 90%;">20:00:58 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:00 UTC</span>

<span style="font-size: 90%;">did I summarize the situation correctly? :stuck_out_tongue:</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:09 UTC</span>

<span style="font-size: 90%;">ok, I think I found myself :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:30 UTC</span>

<span style="font-size: 90%;">yes, the last release of libmodsecurity 3 is 3.0.3</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:45 UTC</span>

<span style="font-size: 90%;">but there are more, than 40 patches in the current master</span>

**airween** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">and I guess about 8 pending PR's</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:24 UTC</span>

<span style="font-size: 90%;">and I'm sure I'll found more in the future</span>

**csanders** <span style="color: grey; font-size: 90%;">20:02:25 UTC</span>

<span style="font-size: 90%;">i'm sure that a new release will come soon given that</span>

**airween** <span style="color: grey; font-size: 90%;">20:02:32 UTC</span>

<span style="font-size: 90%;">would be good</span>

**csanders** <span style="color: grey; font-size: 90%;">20:02:48 UTC</span>

<span style="font-size: 90%;">alright... this brings us to our 11 PR's - Our first one is one I made today that _@fgs_ will be happy to see <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1301></span>

**airween** <span style="color: grey; font-size: 90%;">20:02:49 UTC</span>

<span style="font-size: 90%;">but the planned milestone is so far</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:16 UTC</span>

<span style="font-size: 90%;">this is pretty basic, but paves the way for people to do alot more</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:25 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/ModSecurity/milestone/13></span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:28 UTC</span>

<span style="font-size: 90%;">it brings in a repo that allows for processing the rules</span>

**csanders** <span style="color: grey; font-size: 90%;">20:03:47 UTC</span>

<span style="font-size: 90%;">(yikes)</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:11 UTC</span>

<span style="font-size: 90%;">Awesome!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:20 UTC</span>

<span style="font-size: 90%;">essentially this builds on your work</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:21 UTC</span>

<span style="font-size: 90%;">I’m def happy too see that :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:34 UTC</span>

<span style="font-size: 90%;">to add a modular rule parser</span>

**fgs** <span style="color: grey; font-size: 90%;">20:04:35 UTC</span>

<span style="font-size: 90%;">(the PR I mean)</span>

**csanders** <span style="color: grey; font-size: 90%;">20:04:45 UTC</span>

<span style="font-size: 90%;">so this adds support for this to travis</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:00 UTC</span>

<span style="font-size: 90%;">for right now it's just doing basic correctness checking of rules</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:02 UTC</span>

<span style="font-size: 90%;">```
6.84s$ python secrules_parsing/secrules_parser.py -c -f rules/*.conf
Syntax OK: rules/REQUEST-901-INITIALIZATION.conf
Syntax OK: rules/REQUEST-903.9001-DRUPAL-EXCLUSION-RULES.conf
Syntax OK: rules/REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
Syntax OK: rules/REQUEST-903.9003-NEXTCLOUD-EXCLUSION-RULES.conf
Syntax OK: rules/REQUEST-903.9004-DOKUWIKI-EXCLUSION-RULES.conf
Syntax OK: rules/REQUEST-903.9005-CPANEL-EXCLUSION-RULES.conf
Syntax OK: rules/REQUEST-905-COMMON-EXCEPTIONS.conf
Syntax OK: rules/REQUEST-910-IP-REPUTATION.conf
Syntax OK: rules/REQUEST-911-METHOD-ENFORCEMENT.conf
Syntax OK: rules/REQUEST-912-DOS-PROTECTION.conf
Syntax OK: rules/REQUEST-913-SCANNER-DETECTION.conf
Syntax OK: rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
Syntax OK: rules/REQUEST-921-PROTOCOL-ATTACK.conf
Syntax OK: rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
Syntax OK: rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
Syntax OK: rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
Syntax OK: rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
Syntax OK: rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
Syntax OK: rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
Syntax OK: rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
Syntax OK: rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf
Syntax OK: rules/REQUEST-949-BLOCKING-EVALUATION.conf
Syntax OK: rules/RESPONSE-950-DATA-LEAKAGES.conf
Syntax OK: rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
Syntax OK: rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
Syntax OK: rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
Syntax OK: rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
Syntax OK: rules/RESPONSE-959-BLOCKING-EVALUATION.conf
Syntax OK: rules/RESPONSE-980-CORRELATION.conf
```</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:27 UTC</span>

<span style="font-size: 90%;">but the api is exposed so that one can easily modify the code to add checking for things like does it say capture but not use the groups</span>

**fgs** <span style="color: grey; font-size: 90%;">20:05:44 UTC</span>

<span style="font-size: 90%;">yeah, cool</span>

**csanders** <span style="color: grey; font-size: 90%;">20:05:47 UTC</span>

<span style="font-size: 90%;"><https://github.com/CRS-support/secrules_parsing></span>

**csanders** <span style="color: grey; font-size: 90%;">20:06:34 UTC</span>

<span style="font-size: 90%;">seems to be working fine, its a pretty minor PR so whenever someone approves it it can be merged</span>

**csanders** <span style="color: grey; font-size: 90%;">20:06:55 UTC</span>

<span style="font-size: 90%;">let me know if anyone has more feedback</span>

**fgs** <span style="color: grey; font-size: 90%;">20:07:02 UTC</span>

<span style="font-size: 90%;">I was planning to take a look</span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:05 UTC</span>

<span style="font-size: 90%;">perfect</span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:12 UTC</span>

<span style="font-size: 90%;">lets quickly move to <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1300></span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:26 UTC</span>

<span style="font-size: 90%;">lol</span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:31 UTC</span>

<span style="font-size: 90%;">we've been implored to ignore it for now</span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:36 UTC</span>

<span style="font-size: 90%;">so i guess we will :slightly_smiling_face:</span>

**fgs** <span style="color: grey; font-size: 90%;">20:07:45 UTC</span>

<span style="font-size: 90%;">Yeah, tests are failing for unknown reasons</span>

**csanders** <span style="color: grey; font-size: 90%;">20:07:58 UTC</span>

<span style="font-size: 90%;">let me know if you neeed help going forward</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:08 UTC</span>

<span style="font-size: 90%;">let's move onto <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1298></span>

**fgs** <span style="color: grey; font-size: 90%;">20:08:09 UTC</span>

<span style="font-size: 90%;">Which made me wonder if we need to add verbose support for ftw</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:40 UTC</span>

<span style="font-size: 90%;">we can change our image maybe to spit out more fail info</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:47 UTC</span>

<span style="font-size: 90%;">_@walter_ i know you said you'd throw some time for testing</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:48 UTC</span>

<span style="font-size: 90%;">yeah I should review [#1298](https://github.com/coreruleset/coreruleset/issues/#1298)</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:53 UTC</span>

<span style="font-size: 90%;">still planning on that  in the next few months?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:08:56 UTC</span>

<span style="font-size: 90%;">*weeks</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:02 UTC</span>

<span style="font-size: 90%;">yes for next week!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:09:06 UTC</span>

<span style="font-size: 90%;">alright!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:09:10 UTC</span>

<span style="font-size: 90%;">we'll keep moving on</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:15 UTC</span>

<span style="font-size: 90%;">would you like to have this in 3.1.1? WordPress 5.0 will default to this API so I guess it will hit us</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:26 UTC</span>

<span style="font-size: 90%;">and it seems like a trivial patch</span>

**csanders** <span style="color: grey; font-size: 90%;">20:09:46 UTC</span>

<span style="font-size: 90%;">when is 5.0 release date?</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:56 UTC</span>

<span style="font-size: 90%;">it’s already out! :weary:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:09 UTC</span>

<span style="font-size: 90%;">yeah probably we can backpatch</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:21 UTC</span>

<span style="font-size: 90%;">its simple enough</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:23 UTC</span>

<span style="font-size: 90%;">alright then I can merge this sooner… I’ll try tomorrow, otherwise Thursday absolute latest?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:24 UTC</span>

<span style="font-size: 90%;">if you get it submitted</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:27 UTC</span>

<span style="font-size: 90%;">okay</span>

**csanders** <span style="color: grey; font-size: 90%;">20:10:29 UTC</span>

<span style="font-size: 90%;">sounds good</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:32 UTC</span>

<span style="font-size: 90%;">check</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:24 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1297></span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:28 UTC</span>

<span style="font-size: 90%;">that is our next one</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:34 UTC</span>

<span style="font-size: 90%;">i think it's like 99% of the way there</span>

**csanders** <span style="color: grey; font-size: 90%;">20:11:44 UTC</span>

<span style="font-size: 90%;">just the test needs to be added</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:05 UTC</span>

<span style="font-size: 90%;">oh it has been</span>

**csanders** <span style="color: grey; font-size: 90%;">20:12:08 UTC</span>

<span style="font-size: 90%;">are we good to merge this?</span>

**fgs** <span style="color: grey; font-size: 90%;">20:12:24 UTC</span>

<span style="font-size: 90%;">From my POV it is</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:12:32 UTC</span>

<span style="font-size: 90%;">think so...</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:32 UTC</span>

<span style="font-size: 90%;">oh wow, well spotted</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:12:42 UTC</span>

<span style="font-size: 90%;">yes, thanks to _@fgs_ that made the test yaml</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:01 UTC</span>

<span style="font-size: 90%;">alright, you guys have gone back and forth on this a bit</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:04 UTC</span>

<span style="font-size: 90%;">so i'm gonna merge it</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:04 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:13:19 UTC</span>

<span style="font-size: 90%;">it has been merged, nice job !</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:25 UTC</span>

<span style="font-size: 90%;">would that be a backport candidate?</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:29 UTC</span>

<span style="font-size: 90%;">it’s fixing a hole</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:33 UTC</span>

<span style="font-size: 90%;">for 3.1.1</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:06 UTC</span>

<span style="font-size: 90%;">its dangorus because people aren't expecting that to change</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:12 UTC</span>

<span style="font-size: 90%;">and may have made exclusions based on it already</span>

**fgs** <span style="color: grey; font-size: 90%;">20:14:40 UTC</span>

<span style="font-size: 90%;">true but at the same time it might be causing FN</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:51 UTC</span>

<span style="font-size: 90%;">the change is VERY minor</span>

**csanders** <span style="color: grey; font-size: 90%;">20:14:57 UTC</span>

<span style="font-size: 90%;">i am find with backpatching to 3.1.1</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:03 UTC</span>

<span style="font-size: 90%;">*fine</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:22 UTC</span>

<span style="font-size: 90%;">so it shall be done :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:25 UTC</span>

<span style="font-size: 90%;">onto our next PR</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:26 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1294></span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:29 UTC</span>

<span style="font-size: 90%;">another bypass</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:54 UTC</span>

<span style="font-size: 90%;">there is a lot of comments here</span>

**csanders** <span style="color: grey; font-size: 90%;">20:15:59 UTC</span>

<span style="font-size: 90%;">where are we with this one, i'm not up to date</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:16:04 UTC</span>

<span style="font-size: 90%;">sorry, I made some noise in this PR :confused:</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:22 UTC</span>

<span style="font-size: 90%;">well I like this PR :smile: just haven’t had time to run it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:17:32 UTC</span>

<span style="font-size: 90%;">I’m testing this rule in production. I’ve put it in PL1, but I don’t know if all agree with that</span>

**fgs** <span style="color: grey; font-size: 90%;">20:17:32 UTC</span>

<span style="font-size: 90%;">looks g2g to me</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:28 UTC</span>

<span style="font-size: 90%;">Nice work, _@theMiddle_!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:39 UTC</span>

<span style="font-size: 90%;">IMHO it’s not prone to many FPs</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:44 UTC</span>

<span style="font-size: 90%;">PL1 would also be my choice :+1:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:18:55 UTC</span>

<span style="font-size: 90%;">nice</span>

**csanders** <span style="color: grey; font-size: 90%;">20:18:57 UTC</span>

<span style="font-size: 90%;">that sounds like we have a number of votes that it is ready to merge</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:01 UTC</span>

<span style="font-size: 90%;">any against?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:19:12 UTC</span>

<span style="font-size: 90%;">hearing none, i'll go ahead and merge this</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:29 UTC</span>

<span style="font-size: 90%;">:tada:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:02 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1292></span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:20:03 UTC</span>

<span style="font-size: 90%;">ops, wrong emoticons :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:06 UTC</span>

<span style="font-size: 90%;">this is an awesome PR</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:31 UTC</span>

<span style="font-size: 90%;">i know _@SpartanTri_ wanted some additions but I think we should add those after as this users doesn't seem like he has bandwidth to fix</span>

**csanders** <span style="color: grey; font-size: 90%;">20:20:52 UTC</span>

<span style="font-size: 90%;">_@walter_ not quite sure i remember your feedback but were you asking for changes?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:21:11 UTC</span>

<span style="font-size: 90%;">I’ve a question about this PR</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:18 UTC</span>

<span style="font-size: 90%;">no not really, just we need to remember to also make changes in `lfi-os-files.data`</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:23 UTC</span>

<span style="font-size: 90%;">but that could be a separate issue</span>

**walter** <span style="color: grey; font-size: 90%;">20:21:37 UTC</span>

<span style="font-size: 90%;">most of these entries should also go there</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:05 UTC</span>

<span style="font-size: 90%;">we can open a separate issue for that, we shouldn’t leave open PRs too long</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:22:40 UTC</span>

<span style="font-size: 90%;">Hi guys, jsut arrived, I was pretty busy</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:22:49 UTC</span>

<span style="font-size: 90%;">hi</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:49 UTC</span>

<span style="font-size: 90%;">hi _@SpartanTri_!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:23:04 UTC</span>

<span style="font-size: 90%;">heyho</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:23:06 UTC</span>

<span style="font-size: 90%;">you've been pretty active lately :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:08 UTC</span>

<span style="font-size: 90%;">I’ll edit and approve this PR</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:23:21 UTC</span>

<span style="font-size: 90%;">thanks, _@walter_</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:24 UTC</span>

<span style="font-size: 90%;">uhm, isn’t 920440 matching the whole list? `"@rx \.([^.]+)$"` … it should match `/.docker` or `/.git`, isn’t it?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:23:59 UTC</span>

<span style="font-size: 90%;">or maybe I’m misunderstanding the regex</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:00 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ later on in 920440, it will check the found extension in `tx.restricted_extensions`</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:21 UTC</span>

<span style="font-size: 90%;">so it will match `/.docker` but unless you have `docker` added to your blocked extensions, the rule will pass it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:31 UTC</span>

<span style="font-size: 90%;">right, sorry</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:31 UTC</span>

<span style="font-size: 90%;">so this is different</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:46 UTC</span>

<span style="font-size: 90%;">anyway I like these additions so I’ll merge them!</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:55 UTC</span>

<span style="font-size: 90%;">csanders has gone to the restroom for a bit so let’s go to the next PR….</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:56 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2:</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:57 UTC</span>

<span style="font-size: 90%;">which iiiisss…</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:43 UTC</span>

<span style="font-size: 90%;"><https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1287> -> this one is on hold for now</span>

**fgs** <span style="color: grey; font-size: 90%;">20:27:34 UTC</span>

<span style="font-size: 90%;">Just leave it for now</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:37 UTC</span>

<span style="font-size: 90%;">OK</span>

**fgs** <span style="color: grey; font-size: 90%;">20:27:41 UTC</span>

<span style="font-size: 90%;">I was in the middle of cleaning other things</span>

**fgs** <span style="color: grey; font-size: 90%;">20:27:45 UTC</span>

<span style="font-size: 90%;">so it’s taking a bit longer</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:04 UTC</span>

<span style="font-size: 90%;">I’ll assign to dune73 since he has commented he would merge :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:29 UTC</span>

<span style="font-size: 90%;">the next!</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:32 UTC</span>

<span style="font-size: 90%;">is… [#1286](https://github.com/coreruleset/coreruleset/issues/#1286) <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1286></span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:48 UTC</span>

<span style="font-size: 90%;">Hello everyone. Sorry for being so late. But glad to be here at last.</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:28:57 UTC</span>

<span style="font-size: 90%;">heyhoo</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:29:18 UTC</span>

<span style="font-size: 90%;">hi _@dune73_</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:29:40 UTC</span>

<span style="font-size: 90%;">Hi Christian</span>

**dune73** <span style="color: grey; font-size: 90%;">20:30:09 UTC</span>

<span style="font-size: 90%;">Please don't let me interrupt you. Or is the meeting already over?</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:51 UTC</span>

<span style="font-size: 90%;">no we are still working!</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:06 UTC</span>

<span style="font-size: 90%;">i’m wondering about this problem</span>

**csanders** <span style="color: grey; font-size: 90%;">20:31:09 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">20:31:12 UTC</span>

<span style="font-size: 90%;">welcome _@dune73_</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:31:21 UTC</span>

<span style="font-size: 90%;">why?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:31:37 UTC</span>

<span style="font-size: 90%;">Sorry, a little late</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:32:13 UTC</span>

<span style="font-size: 90%;">hi _@fzipitria_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:32:16 UTC</span>

<span style="font-size: 90%;">About the swag, I wrote some of the options that I got from asking and talking with people</span>

**dune73** <span style="color: grey; font-size: 90%;">20:32:21 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:32:44 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ you gonna be here for a bit?</span>

**csanders** <span style="color: grey; font-size: 90%;">20:32:51 UTC</span>

<span style="font-size: 90%;">if so can we circle back after we finish PRs?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:33:39 UTC</span>

<span style="font-size: 90%;">I think he is offline again...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:33:43 UTC</span>

<span style="font-size: 90%;">_@walter_: What are you wondering about exactly?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:43 UTC</span>

<span style="font-size: 90%;">Driving</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:51 UTC</span>

<span style="font-size: 90%;">about [#1286](https://github.com/coreruleset/coreruleset/issues/#1286), I think I agree with _@emphazer_ that we should not check `XML` with validateUrlEncoding, since `%` can legally be in those fields</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:55 UTC</span>

<span style="font-size: 90%;">I'm gonna be</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:35:00 UTC</span>

<span style="font-size: 90%;">In 15 minutes</span>

**fgs** <span style="color: grey; font-size: 90%;">20:35:30 UTC</span>

<span style="font-size: 90%;">_@walter_ is that for values, attributes, tags or all of them?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:35:55 UTC</span>

<span style="font-size: 90%;">so the change only removes the C-T header check isn't it but left XML in the other rules of the chain?</span>

**walter** <span style="color: grey; font-size: 90%;">20:36:38 UTC</span>

<span style="font-size: 90%;">_@fgs_ I’m actually not so familiar with if all of these are returned in the XML collection…</span>

**fgs** <span style="color: grey; font-size: 90%;">20:36:47 UTC</span>

<span style="font-size: 90%;">Right, me neither</span>

**fgs** <span style="color: grey; font-size: 90%;">20:36:59 UTC</span>

<span style="font-size: 90%;">I haven’t had time to dig any further</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:15 UTC</span>

<span style="font-size: 90%;">but, I would assume that the XML parser would reject invalid XML</span>

**fgs** <span style="color: grey; font-size: 90%;">20:37:37 UTC</span>

<span style="font-size: 90%;">So that’d include % if it was the case</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:37:38 UTC</span>

<span style="font-size: 90%;">this rule produced 20gb logs on our nextcloud server in 2days....</span>

**fgs** <span style="color: grey; font-size: 90%;">20:37:51 UTC</span>

<span style="font-size: 90%;">but since it’s causing FPs then I guess is either not choking or % is valid :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:09 UTC</span>

<span style="font-size: 90%;">% in the text node as in the example in the first post is absolutely valid</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:38:49 UTC</span>

<span style="font-size: 90%;">it makes no sense to let it match on text/xml</span>

**fgs** <span style="color: grey; font-size: 90%;">20:39:20 UTC</span>

<span style="font-size: 90%;">Maybe it’s how the rule is using XML</span>

**fgs** <span style="color: grey; font-size: 90%;">20:39:28 UTC</span>

<span style="font-size: 90%;">But I don’t have enough info atm to comment</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:39:29 UTC</span>

<span style="font-size: 90%;">then remove XML from all other rules in the chain as well</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:39:37 UTC</span>

<span style="font-size: 90%;">ok</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:44 UTC</span>

<span style="font-size: 90%;">yes!</span>

**csanders** <span style="color: grey; font-size: 90%;">20:41:26 UTC</span>

<span style="font-size: 90%;">alright, so what are the next steps?</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:16 UTC</span>

<span style="font-size: 90%;">I think if `XML:/*` is removed from lines 453 and 455, plus a comment about the change (removed xml) it looks good</span>

**fgs** <span style="color: grey; font-size: 90%;">20:43:36 UTC</span>

<span style="font-size: 90%;">I’d say add some test too</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:56 UTC</span>

<span style="font-size: 90%;">yes the example in post comment should be made a test</span>

**walter** <span style="color: grey; font-size: 90%;">20:44:25 UTC</span>

<span style="font-size: 90%;">plus ideally a positive, so a form submission with a loose `%` which DOES get validated and fails</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:44:36 UTC</span>

<span style="font-size: 90%;">done</span>

**walter** <span style="color: grey; font-size: 90%;">20:45:20 UTC</span>

<span style="font-size: 90%;">could you add 2 tests in a yaml? :smile:</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">20:45:35 UTC</span>

<span style="font-size: 90%;">not a form submission but an XML</span>

**fgs** <span style="color: grey; font-size: 90%;">20:45:44 UTC</span>

<span style="font-size: 90%;">I still think you want to check if the xml parser will choke on <%foo></%foo></span>

**emphazer** <span style="color: grey; font-size: 90%;">20:45:50 UTC</span>

<span style="font-size: 90%;">same here</span>

**fgs** <span style="color: grey; font-size: 90%;">20:46:07 UTC</span>

<span style="font-size: 90%;">So maybe add a test to ensure that does not reach the rule</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:33 UTC</span>

<span style="font-size: 90%;">my apache says 400 bad request on such XML</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:42 UTC</span>

<span style="font-size: 90%;">e.g. `curl -H 'Content-Type: text/xml' --data '<%ao></%ao>' <http://sim/>`</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:46 UTC</span>

<span style="font-size: 90%;">so I think we’re good</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:46:50 UTC</span>

<span style="font-size: 90%;">dont know any form submission for this case</span>

**fgs** <span style="color: grey; font-size: 90%;">20:46:54 UTC</span>

<span style="font-size: 90%;">we can still test with status:400</span>

**walter** <span style="color: grey; font-size: 90%;">20:46:57 UTC</span>

<span style="font-size: 90%;">oh!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:47:18 UTC</span>

<span style="font-size: 90%;">hmmm</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:47:33 UTC</span>

<span style="font-size: 90%;">% isnt allowed in the <></span>

**emphazer** <span style="color: grey; font-size: 90%;">20:47:43 UTC</span>

<span style="font-size: 90%;">never</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:04 UTC</span>

<span style="font-size: 90%;">yes, libxml takes care of that for us, so that’s good</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:48:10 UTC</span>

<span style="font-size: 90%;">yeah</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:11 UTC</span>

<span style="font-size: 90%;">but yes we can test for it even!</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:43 UTC</span>

<span style="font-size: 90%;">we just need one test which DOES match the rule</span>

**walter** <span style="color: grey; font-size: 90%;">20:48:47 UTC</span>

<span style="font-size: 90%;">to show that it still works</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:18 UTC</span>

<span style="font-size: 90%;">for instance `curl --data-raw 'blah=fo%xy' <http://sim/>`</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:35 UTC</span>

<span style="font-size: 90%;">which would hit the rule due to request_body</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:49:49 UTC</span>

<span style="font-size: 90%;">sweet</span>

**walter** <span style="color: grey; font-size: 90%;">20:49:58 UTC</span>

<span style="font-size: 90%;">could you make a yaml of those 3? :smile:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:50:10 UTC</span>

<span style="font-size: 90%;">sure</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:12 UTC</span>

<span style="font-size: 90%;">and add them to this PR</span>

**walter** <span style="color: grey; font-size: 90%;">20:50:17 UTC</span>

<span style="font-size: 90%;">then I’d say it’s a merge</span>

**csanders** <span style="color: grey; font-size: 90%;">20:50:29 UTC</span>

<span style="font-size: 90%;">#hurray</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:51:18 UTC</span>

<span style="font-size: 90%;">walter</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:51:22 UTC</span>

<span style="font-size: 90%;">I count 2</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:04 UTC</span>

<span style="font-size: 90%;">1. your FP from the post (SOAP-message) which should be allowed by 920420 after tyour fix; 2. a XML with `<%ao></%ao>` which should be blocked (with status 400);  3. a raw POST with `foo=%ao` which should be blocked by 920240</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:01 UTC</span>

<span style="font-size: 90%;">so 1 is the test that shows that the FP is closed, but 2 and 3 will demonstrate that after working on the rule its core purpose hasn’t been broken</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:54:46 UTC</span>

<span style="font-size: 90%;">ok</span>

**walter** <span style="color: grey; font-size: 90%;">20:54:53 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:00 UTC</span>

<span style="font-size: 90%;">feel free to assign to me if you turn into a problem</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:55:05 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face: </span>

**emphazer** <span style="color: grey; font-size: 90%;">20:55:11 UTC</span>

<span style="font-size: 90%;">thx</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:12 UTC</span>

<span style="font-size: 90%;">I gotta go soon because my energy levels are almost zero</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:20 UTC</span>

<span style="font-size: 90%;">I’ll respond when called :smile:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:55:20 UTC</span>

<span style="font-size: 90%;">same here</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:27 UTC</span>

<span style="font-size: 90%;">thanks for this PR, very nice fix</span>

**dune73** <span style="color: grey; font-size: 90%;">20:56:36 UTC</span>

<span style="font-size: 90%;">You guys went through the PRs from top down? That would mean we're done with the PRs for tonight?</span>

**walter** <span style="color: grey; font-size: 90%;">20:57:04 UTC</span>

<span style="font-size: 90%;">there’s still <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1284></span>

**csanders** <span style="color: grey; font-size: 90%;">20:57:15 UTC</span>

<span style="font-size: 90%;">yup</span>

**csanders** <span style="color: grey; font-size: 90%;">20:57:17 UTC</span>

<span style="font-size: 90%;">thanks Walter</span>

**dune73** <span style="color: grey; font-size: 90%;">20:57:31 UTC</span>

<span style="font-size: 90%;">True.</span>

**walter** <span style="color: grey; font-size: 90%;">20:58:19 UTC</span>

<span style="font-size: 90%;">and then finally I wondered if _@airween_ would have some requests for help from us, or maybe an idea if the inclusion of modsec3 in debian testing looks to go ahead or if it’s too troublesome (maybe not really CRS related but affects us all)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:58:45 UTC</span>

<span style="font-size: 90%;">Is _@airween_ around?</span>

**airween** <span style="color: grey; font-size: 90%;">20:58:59 UTC</span>

<span style="font-size: 90%;">I think the remained FALSE test comes by the libmodsec3</span>

**airween** <span style="color: grey; font-size: 90%;">20:59:29 UTC</span>

<span style="font-size: 90%;">now the number of false tests is about 36 I guess</span>

**airween** <span style="color: grey; font-size: 90%;">20:59:38 UTC</span>

<span style="font-size: 90%;">in case of Apache</span>

**airween** <span style="color: grey; font-size: 90%;">21:01:29 UTC</span>

<span style="font-size: 90%;">it's hard work to investigate all test one by one. The big help would be explain the syntax of rules :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">21:01:58 UTC</span>

<span style="font-size: 90%;">I'm a newbie :slightly_smiling_face:</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:13 UTC</span>

<span style="font-size: 90%;">the modsec rules?</span>

**airween** <span style="color: grey; font-size: 90%;">21:02:20 UTC</span>

<span style="font-size: 90%;">yes</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:25 UTC</span>

<span style="font-size: 90%;">ahh yeah it takes some time</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:39 UTC</span>

<span style="font-size: 90%;">we can explain to you but also feel free to ask in here</span>

**csanders** <span style="color: grey; font-size: 90%;">21:02:44 UTC</span>

<span style="font-size: 90%;">there are some very knowledgable folks</span>

**dune73** <span style="color: grey; font-size: 90%;">21:02:58 UTC</span>

<span style="font-size: 90%;">I see what you mean. Some of the rules are really tough and the debug log in libmodsec3 is not the big help it is with ModSec 2.9 I think.</span>

**airween** <span style="color: grey; font-size: 90%;">21:03:02 UTC</span>

<span style="font-size: 90%;">eg. now I fight with this:

SecRule &TX:restricted_headers "`@eq` 0" "id:901165,phase:1,pass,nolog,setvar:'tx.restricted_headers=/proxy/ /lock-token/ /content-range/ /translate/ /if/'"</span>

**airween** <span style="color: grey; font-size: 90%;">21:03:48 UTC</span>

<span style="font-size: 90%;">_@csanders_ yes, I experienced :slightly_smiling_face:, thanks for all help guys</span>

**dune73** <span style="color: grey; font-size: 90%;">21:03:50 UTC</span>

<span style="font-size: 90%;">It means: If the number of variables names tx.restricted_headers is eq 0, then it is undefined and will be defined as follows.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:22 UTC</span>

<span style="font-size: 90%;">& always indicates not the variable, but the counting of variables.</span>

**airween** <span style="color: grey; font-size: 90%;">21:04:32 UTC</span>

<span style="font-size: 90%;">but which symbol describes the "number of"?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:04:39 UTC</span>

<span style="font-size: 90%;">&</span>

**airween** <span style="color: grey; font-size: 90%;">21:04:43 UTC</span>

<span style="font-size: 90%;">ah'</span>

**airween** <span style="color: grey; font-size: 90%;">21:05:26 UTC</span>

<span style="font-size: 90%;">so, the `TX:restricted_headers` interprets as string, but &TX:restricted_headers is the number of variable with this name</span>

**walter** <span style="color: grey; font-size: 90%;">21:06:46 UTC</span>

<span style="font-size: 90%;">yes exactly!</span>

**airween** <span style="color: grey; font-size: 90%;">21:06:54 UTC</span>

<span style="font-size: 90%;">right, thanks</span>

**airween** <span style="color: grey; font-size: 90%;">21:07:34 UTC</span>

<span style="font-size: 90%;">should I ask the next one? Or still pending the CRS meeting?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:41 UTC</span>

<span style="font-size: 90%;">What do we do with 1284? It is better, but the numbers are still in a wrong range. Should I merge and then update by hand?</span>

**walter** <span style="color: grey; font-size: 90%;">21:07:53 UTC</span>

<span style="font-size: 90%;">I must check out sorry, good luck :smile:</span>

**csanders** <span style="color: grey; font-size: 90%;">21:07:54 UTC</span>

<span style="font-size: 90%;">we have that one PR and then schwag</span>

**dune73** <span style="color: grey; font-size: 90%;">21:07:57 UTC</span>

<span style="font-size: 90%;">_@airween_, could we take your questions some other time, please.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:01 UTC</span>

<span style="font-size: 90%;">thanks for sticking it out _@walter_</span>

**airween** <span style="color: grey; font-size: 90%;">21:08:05 UTC</span>

<span style="font-size: 90%;">okok</span>

**dune73** <span style="color: grey; font-size: 90%;">21:08:08 UTC</span>

<span style="font-size: 90%;">Thanks  _@walter_</span>

**walter** <span style="color: grey; font-size: 90%;">21:08:13 UTC</span>

<span style="font-size: 90%;">back to bed :heart_eyes:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:08:15 UTC</span>

<span style="font-size: 90%;">Bye _@walter_</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:35 UTC</span>

<span style="font-size: 90%;">feel better</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:08:39 UTC</span>

<span style="font-size: 90%;">cya _@walter_ </span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:08:41 UTC</span>

<span style="font-size: 90%;">bye _@walter_ get well</span>

**csanders** <span style="color: grey; font-size: 90%;">21:08:44 UTC</span>

<span style="font-size: 90%;">so for that PR where are we</span>

**airween** <span style="color: grey; font-size: 90%;">21:08:51 UTC</span>

<span style="font-size: 90%;">by _@walter_</span>

**dune73** <span style="color: grey; font-size: 90%;">21:09:35 UTC</span>

<span style="font-size: 90%;">Yes, 1284.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:11:18 UTC</span>

<span style="font-size: 90%;">It is better, but the numbers are still in a wrong range. Should I merge and then update by hand?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:11:30 UTC</span>

<span style="font-size: 90%;">i think thats the best way to fix the issue</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:49 UTC</span>

<span style="font-size: 90%;">OK. I'll do it that way then. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:12:53 UTC</span>

<span style="font-size: 90%;">On to swag!!!</span>

**csanders** <span style="color: grey; font-size: 90%;">21:13:26 UTC</span>

<span style="font-size: 90%;">haha</span>

**csanders** <span style="color: grey; font-size: 90%;">21:13:29 UTC</span>

<span style="font-size: 90%;">_@fzipitria_?</span>

**csanders** <span style="color: grey; font-size: 90%;">21:13:34 UTC</span>

<span style="font-size: 90%;">thanks _@dune73_</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:13:54 UTC</span>

<span style="font-size: 90%;">I think, _@fzipitria_ is not here, he's offline</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:14:55 UTC</span>

<span style="font-size: 90%;">I need a CRS pizza cutter</span>

**csanders** <span style="color: grey; font-size: 90%;">21:15:29 UTC</span>

<span style="font-size: 90%;">lol</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:33 UTC</span>

<span style="font-size: 90%;">If _@fzipitria_ is still travelling, let's turn to something else.</span>

**csanders** <span style="color: grey; font-size: 90%;">21:15:40 UTC</span>

<span style="font-size: 90%;">thats all that is left :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:15:49 UTC</span>

<span style="font-size: 90%;">I think it's about time _@theMiddle_ adds his name to the contribution file</span>

**csanders** <span style="color: grey; font-size: 90%;">21:15:56 UTC</span>

<span style="font-size: 90%;">here here!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:09 UTC</span>

<span style="font-size: 90%;">I'm five minutes away</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:21 UTC</span>

<span style="font-size: 90%;">But the main thing is that we need to decide</span>

**dune73** <span style="color: grey; font-size: 90%;">21:17:29 UTC</span>

<span style="font-size: 90%;">5 min away from the terminal?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:54 UTC</span>

<span style="font-size: 90%;">Which thing we want</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:17:58 UTC</span>

<span style="font-size: 90%;">Yes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:18:07 UTC</span>

<span style="font-size: 90%;">Stickers!!!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:12 UTC</span>

<span style="font-size: 90%;">_@csanders_: Can you make sure _@theMiddle_ gets write access on the repository?</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:21:02 UTC</span>

<span style="font-size: 90%;">thanks _@dune73_, really happy to contribute on CRS with you guys, learned a lot!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:18 UTC</span>

<span style="font-size: 90%;">Stickers is easy</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:38 UTC</span>

<span style="font-size: 90%;">Stickers are certainly a priority. I liked the one you did with CRS and claim. Not the full project title.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:18:50 UTC</span>

<span style="font-size: 90%;">Then a place to have the CRS3 poster printed.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:51 UTC</span>

<span style="font-size: 90%;">Surr</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:18:56 UTC</span>

<span style="font-size: 90%;">That's one thing</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:15 UTC</span>

<span style="font-size: 90%;">Which design we are going to use</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:19 UTC</span>

<span style="font-size: 90%;">And then (2nd priority) T-Shirts and or hoodies or polo shirts</span>

**dune73** <span style="color: grey; font-size: 90%;">21:19:36 UTC</span>

<span style="font-size: 90%;">Could you link the designs again? I saw them but it's way up there. Or upload to wiki...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:19:59 UTC</span>

<span style="font-size: 90%;">They might be from different provider@</span>

**csanders** <span style="color: grey; font-size: 90%;">21:20:20 UTC</span>

<span style="font-size: 90%;">hey guys i gotta run</span>

**csanders** <span style="color: grey; font-size: 90%;">21:20:25 UTC</span>

<span style="font-size: 90%;">but its great to talk to you all!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:21:01 UTC</span>

<span style="font-size: 90%;">I will write to you, _@csanders_! Bye</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:21:02 UTC</span>

<span style="font-size: 90%;">thanks _@dune73_, really happy to contribute on CRS with you guys, learned a lot!</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">21:21:02 UTC</span>

<span style="font-size: 90%;">thanks _@dune73_, really happy to contribute on CRS with you guys, learned a lot!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:31 UTC</span>

<span style="font-size: 90%;">Bye _@csanders_!</span>

**dune73** <span style="color: grey; font-size: 90%;">21:21:34 UTC</span>

<span style="font-size: 90%;">And thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">21:22:13 UTC</span>

<span style="font-size: 90%;">Nothing wrong with more than one provider. Or does it make things very complicated?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:26 UTC</span>

<span style="font-size: 90%;">No</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:38 UTC</span>

<span style="font-size: 90%;">We just need to get that tight</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:22:49 UTC</span>

<span style="font-size: 90%;">Someone needs to create accounts</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:01 UTC</span>

<span style="font-size: 90%;">We could go for stickermule</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:17 UTC</span>

<span style="font-size: 90%;">And then choose another one for tshirts</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:24 UTC</span>

<span style="font-size: 90%;">That's what a lot of projects do, is not it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:23:33 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**dune73** <span style="color: grey; font-size: 90%;">21:23:50 UTC</span>

<span style="font-size: 90%;">Sounds like a plan. I think the poster should be in the mix too. People really like it and I do not have any left.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:24:07 UTC</span>

<span style="font-size: 90%;">Yes, but one catch is that someone needs to handle the accounts</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:24:32 UTC</span>

<span style="font-size: 90%;">Should it be you _@dune73_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:01 UTC</span>

<span style="font-size: 90%;">I didn't create an account, but I think it could be shared maybe</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:46 UTC</span>

<span style="font-size: 90%;">Can we have an unpersonal project account and then 2-3 people get the PW?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:25:55 UTC</span>

<span style="font-size: 90%;">Will ask there.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:25:59 UTC</span>

<span style="font-size: 90%;">I do not mind sharing.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:04 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:30 UTC</span>

<span style="font-size: 90%;">I can give you the hires resolution of the poster.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:32 UTC</span>

<span style="font-size: 90%;">I'll will then ask for that to be created</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:36 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**dune73** <span style="color: grey; font-size: 90%;">21:26:45 UTC</span>

<span style="font-size: 90%;">The logo is on the OWASP wiki already in highest resolution.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:26:52 UTC</span>

<span style="font-size: 90%;">I saw it</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:27:15 UTC</span>

<span style="font-size: 90%;">I will try to figure it out a couple of designs for stickers</span>

**dune73** <span style="color: grey; font-size: 90%;">21:27:15 UTC</span>

<span style="font-size: 90%;">Would you mind linking all accounts and what we get from which provider in the wiki? OWASP or github?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:27:25 UTC</span>

<span style="font-size: 90%;">If you have ideas, let me know</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:27:34 UTC</span>

<span style="font-size: 90%;">Sure</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:28:23 UTC</span>

<span style="font-size: 90%;">Will update the wiki with the designs and providers</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:28:40 UTC</span>

<span style="font-size: 90%;">And need to catch up with all the messages</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:48 UTC</span>

<span style="font-size: 90%;">Cool. Let me know when you are done. I think we'll get the confirmation quickly.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:28:54 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:28:56 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:29:02 UTC</span>

<span style="font-size: 90%;">:sunglasses:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:29:17 UTC</span>

<span style="font-size: 90%;">So that is settled.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:29:26 UTC</span>

<span style="font-size: 90%;">Did you guys talk about a 3.1.1 release?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:30:24 UTC</span>

<span style="font-size: 90%;">A date? No.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:31:00 UTC</span>

<span style="font-size: 90%;">We only talked about what to backport.</span>

**dune73** <span style="color: grey; font-size: 90%;">21:31:30 UTC</span>

<span style="font-size: 90%;">@empahzer, how urgent is a 3.1.1 release from your perspective?</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:31:42 UTC</span>

<span style="font-size: 90%;">not urgent </span>

**dune73** <span style="color: grey; font-size: 90%;">21:32:09 UTC</span>

<span style="font-size: 90%;">Thank you for the confirmation. So the backport question is settled and we can look into 3.1.1 in March?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:32:47 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:33:24 UTC</span>

<span style="font-size: 90%;">We talked about some of the PRs from today and which ones to backport.
But not all PRs.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:33:43 UTC</span>

<span style="font-size: 90%;">we agree to backport 1297 if I’m not wrong</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:34:39 UTC</span>

<span style="font-size: 90%;">And: <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1294></span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:35:04 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:35:10 UTC</span>

<span style="font-size: 90%;">Yes, <https://github.com/SpiderLabs/owasp-modsecurity-crs/pull/1297> too</span>

**dune73** <span style="color: grey; font-size: 90%;">21:35:53 UTC</span>

<span style="font-size: 90%;">You all agreed to backport a new rule?</span>

**dune73** <span style="color: grey; font-size: 90%;">21:38:45 UTC</span>

<span style="font-size: 90%;">Well, I'll look it up for the monthly news then. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">21:38:59 UTC</span>

<span style="font-size: 90%;">Is there anything else, or do we close the meeting?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:40:20 UTC</span>

<span style="font-size: 90%;">uhm reading again the chat, but maybe _@csanders_ agreed to backport 1297 but not 1294</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:40:26 UTC</span>

<span style="font-size: 90%;">Yes, because its a VERY minor change....</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:40:30 UTC</span>

<span style="font-size: 90%;">I’ll ask him</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:40:37 UTC</span>

<span style="font-size: 90%;">oh oky</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:41:13 UTC</span>

<span style="font-size: 90%;">Ok, not sure...</span>

**dune73** <span style="color: grey; font-size: 90%;">21:42:05 UTC</span>

<span style="font-size: 90%;">We'll find out. But good we have a more or less date. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:42:38 UTC</span>

<span style="font-size: 90%;">I think _@dune73_ has a point, we have to think about this backport again.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:42:50 UTC</span>

<span style="font-size: 90%;">but 1276 will be backported right?</span>

**SpartanTri** <span style="color: grey; font-size: 90%;">21:43:26 UTC</span>

<span style="font-size: 90%;">got to go, have a good night</span>

**dune73** <span style="color: grey; font-size: 90%;">21:43:28 UTC</span>

<span style="font-size: 90%;">Absolutely. That's the reason to do 3.1.1.</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:43:46 UTC</span>

<span style="font-size: 90%;">ah ok. just wanted to be sure</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:43:57 UTC</span>

<span style="font-size: 90%;">good night _@SpartanTri_</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:44:05 UTC</span>

<span style="font-size: 90%;">good night, _@SpartanTri_</span>

**emphazer** <span style="color: grey; font-size: 90%;">21:44:08 UTC</span>

<span style="font-size: 90%;">good night </span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:44:13 UTC</span>

<span style="font-size: 90%;">good night _@SpartanTri_</span>

**dune73** <span style="color: grey; font-size: 90%;">21:44:37 UTC</span>

<span style="font-size: 90%;">Well, let's call it a day then. Bye everyone and thank you for participating and the work around the month. We're really making progress with this project!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">21:44:53 UTC</span>

<span style="font-size: 90%;">Bye everyone!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">21:45:01 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2: thanks, bye all!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:45:08 UTC</span>

<span style="font-size: 90%;">bye all!</span>

**airween** <span style="color: grey; font-size: 90%;">22:08:03 UTC</span>

<span style="font-size: 90%;">everyone gone to sleeping? :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:08:25 UTC</span>

<span style="font-size: 90%;">not yet :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">22:09:09 UTC</span>

<span style="font-size: 90%;">cool :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">22:09:29 UTC</span>

<span style="font-size: 90%;">what does this rule?

SecRule REQUEST_HEADERS_NAMES \"@rx ^.*$\" \"id:920450,phase:2,block,capture,t:none,t:lowercase,msg:'HTTP header is restricted by policy (%{MATCHED_VAR})',logdata:' Restricted header detected %{MATCHED_VAR}',ver:'OWASP_CRS/3.1.0',severity:'CRITICAL',setvar:'tx.header_name_%{tx.0}=/%{tx.0}/',chain</span>

**airween** <span style="color: grey; font-size: 90%;">22:09:48 UTC</span>

<span style="font-size: 90%;">the quoted marks are escaped, sorry</span>

**airween** <span style="color: grey; font-size: 90%;">22:10:37 UTC</span>

<span style="font-size: 90%;">I think the keyword is the "capture"</span>

**airween** <span style="color: grey; font-size: 90%;">22:10:44 UTC</span>

<span style="font-size: 90%;">and "MATCHED_VAR"</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:11:03 UTC</span>

<span style="font-size: 90%;">this is a chained rule, the rule chained to this check the header’s name against the restricted_headers variable</span>

**airween** <span style="color: grey; font-size: 90%;">22:11:38 UTC</span>

<span style="font-size: 90%;">but I don't see the "restricted_headers" expression in this rule</span>

**airween** <span style="color: grey; font-size: 90%;">22:12:07 UTC</span>

<span style="font-size: 90%;">the previous rule the restricted_headers had setted</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:12:11 UTC</span>

<span style="font-size: 90%;">you have the restricted_headers on the crs-setup file, defined at rule 900250</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:12:23 UTC</span>

<span style="font-size: 90%;">`setvar:'tx.restricted_headers=/proxy/ /lock-token/ /content-range/ /translate/ /if/'`</span>

**airween** <span style="color: grey; font-size: 90%;">22:12:26 UTC</span>

<span style="font-size: 90%;">yes</span>

**airween** <span style="color: grey; font-size: 90%;">22:12:56 UTC</span>

<span style="font-size: 90%;">but I don't see the reference for this stored variable in this rule</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:15:01 UTC</span>

<span style="font-size: 90%;">uhm maybe I’m not get it but: `setvar:'tx.header_name_%{tx.0}=/%{tx.0}/',\` this set the header name, and `SecRule TX:/^HEADER_NAME_/ "@within %{tx.restricted_headers}" \` this check it against the list</span>

**airween** <span style="color: grey; font-size: 90%;">22:15:24 UTC</span>

<span style="font-size: 90%;">yes, that's the previous rule</span>

**airween** <span style="color: grey; font-size: 90%;">22:15:41 UTC</span>

<span style="font-size: 90%;">sorry</span>

**airween** <span style="color: grey; font-size: 90%;">22:15:46 UTC</span>

<span style="font-size: 90%;">the next</span>

**airween** <span style="color: grey; font-size: 90%;">22:15:56 UTC</span>

<span style="font-size: 90%;">but I just staying at rule above</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:16:18 UTC</span>

<span style="font-size: 90%;">no they are the “same” rule, they are chained</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:18:41 UTC</span>

<span style="font-size: 90%;">both are separate “SecRule” but they are chained and have the same id. It fires if only both condition will match</span>

**airween** <span style="color: grey; font-size: 90%;">22:19:04 UTC</span>

<span style="font-size: 90%;">yes, that's clear</span>

**airween** <span style="color: grey; font-size: 90%;">22:19:38 UTC</span>

<span style="font-size: 90%;">now I'm looking for these two rule context:
```
      "SecRule &TX:restricted_headers \"@eq 0\" \"id:901165,phase:1,pass,nolog,setvar:'tx.restricted_headers=/proxy/ /lock-token/ /content-range/ /translate/ /if/'\"",
      "SecRule REQUEST_HEADERS_NAMES \"@rx ^.*$\" \"id:920450,phase:2,block,capture,t:none,t:lowercase,msg:'HTTP header is restricted by policy (%{MATCHED_VAR})',logdata:' Restricted header detected %{MATCHED_VAR}',ver:'OWASP_CRS/3.1.0',severity:'CRITICAL',setvar:'tx.header_name_%{tx.0}=/%{tx.0}/',chain"
```</span>

**airween** <span style="color: grey; font-size: 90%;">22:20:05 UTC</span>

<span style="font-size: 90%;">the first one is set up the restricted_headers in TX collection</span>

**airween** <span style="color: grey; font-size: 90%;">22:20:17 UTC</span>

<span style="font-size: 90%;">with value of "/proxy/ /lock-token/ /content-range/ /translate/ /if/"</span>

**airween** <span style="color: grey; font-size: 90%;">22:20:36 UTC</span>

<span style="font-size: 90%;">forgot the chain now</span>

**airween** <span style="color: grey; font-size: 90%;">22:21:40 UTC</span>

<span style="font-size: 90%;">suppose that there is only one header, eg. "Foobar: notempty"</span>

**airween** <span style="color: grey; font-size: 90%;">22:21:51 UTC</span>

<span style="font-size: 90%;">what happens with this header?</span>

**airween** <span style="color: grey; font-size: 90%;">22:22:02 UTC</span>

<span style="font-size: 90%;">in second rule?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:23:23 UTC</span>

<span style="font-size: 90%;">```
%{MATCHED_VAR} => Foobar
tx.header_name_%{tx.0}=/%{tx.0}/ => tx.header_name_Foobar=/Foobar/
```</span>

**airween** <span style="color: grey; font-size: 90%;">22:23:50 UTC</span>

<span style="font-size: 90%;">thanks!</span>

**airween** <span style="color: grey; font-size: 90%;">22:24:05 UTC</span>

<span style="font-size: 90%;">so, this is the expected behavior...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:25:29 UTC</span>

<span style="font-size: 90%;">no sorry:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:25:51 UTC</span>

<span style="font-size: 90%;">now should be right</span>

**airween** <span style="color: grey; font-size: 90%;">22:34:39 UTC</span>

<span style="font-size: 90%;">in the debug.log, I found this line:
Added regex subexpression TX.0: foobar</span>

**airween** <span style="color: grey; font-size: 90%;">22:38:42 UTC</span>

<span style="font-size: 90%;">later:
Saving variable: TX:header_name_foobar with value: /foobar/</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:39:03 UTC</span>

<span style="font-size: 90%;">yes, it seems legit</span>

**airween** <span style="color: grey; font-size: 90%;">22:39:23 UTC</span>

<span style="font-size: 90%;">but only one header added as subexpression</span>

**airween** <span style="color: grey; font-size: 90%;">22:39:41 UTC</span>

<span style="font-size: 90%;">and it doesn't matched with the restricted_headers</span>

**airween** <span style="color: grey; font-size: 90%;">22:40:49 UTC</span>

<span style="font-size: 90%;">that function iterates over the header, before ordered them, then reverse all, so the last header (by ABC) pushed to TX.0</span>

**airween** <span style="color: grey; font-size: 90%;">22:41:17 UTC</span>

<span style="font-size: 90%;">_after_ this it started to collect the headers again, and creates one-by-one</span>

**airween** <span style="color: grey; font-size: 90%;">22:41:50 UTC</span>

<span style="font-size: 90%;">eg:
TX:header_name_host -> /host/
TX:header_name_user-agent -> /user-agent/</span>

**airween** <span style="color: grey; font-size: 90%;">22:41:53 UTC</span>

<span style="font-size: 90%;">and so on</span>

**airween** <span style="color: grey; font-size: 90%;">22:42:13 UTC</span>

<span style="font-size: 90%;">then it starts to compare the headers with the TX.0 values</span>

**airween** <span style="color: grey; font-size: 90%;">22:42:46 UTC</span>

<span style="font-size: 90%;">and - what a surprise! - there is the last header... (what pushed at first place to TX.0)</span>

**airween** <span style="color: grey; font-size: 90%;">22:44:26 UTC</span>

<span style="font-size: 90%;">okay... I have to go to sleep... about 6 hours remained till morning :slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:46:25 UTC</span>

<span style="font-size: 90%;">:+1::skin-tone-2: idk why it doesn’t match, it should… each header should be passed on the chained 920450 and checked against the restricted headers list…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">22:46:49 UTC</span>

<span style="font-size: 90%;">oky, we’ll try to figure out “why it happens” tomorrow :smile:</span>

