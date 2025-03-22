### Mon, Sep 2nd, 2024

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:06 UTC</span>

<span style="font-size: 90%;">:wave: Hi everyone! Welcome to the monthly CRS chat! :party-crs:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:30:16 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:30:19 UTC</span>

<span style="font-size: 90%;">Evening</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:30:24 UTC</span>

<span style="font-size: 90%;">Hello</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:30:47 UTC</span>

<span style="font-size: 90%;">Hello, good evening</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:11 UTC</span>

<span style="font-size: 90%;">Luckily there is not much to discuss tonight, but we do have updates</span>

**azurit** <span style="color: grey; font-size: 90%;">18:31:25 UTC</span>

<span style="font-size: 90%;">Hi</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:56 UTC</span>

<span style="font-size: 90%;">So finally with release 4.6.0 there is a new check for multipart headers correctness, that was backported to 3.3.6</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:47 UTC</span>

<span style="font-size: 90%;">This was an interesting find and the reported was very nice in explaining the problem and how we could solve it and avoid some evasions.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:07 UTC</span>

<span style="font-size: 90%;">Hi there, still bringing the kids to be. I'll join you in a few min</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:03 UTC</span>

<span style="font-size: 90%;">I've been interacting on a daily basis with Starr Brown, OWASP's Director of Projects for CRS related stuff. The interaction has been great and I can say the project is aligned with her vision</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:52 UTC</span>

<span style="font-size: 90%;">She will be also starting to interact more with our Sponsors, as OWASP envisions that the main counterpart for any agreement should be that role.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:57 UTC</span>

<span style="font-size: 90%;">We are also discussing what things haven't worked and how to make things more agile for CRS (and maybe other projects).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:32 UTC</span>

<span style="font-size: 90%;">While there are no conclusions yet, I can say that things are evolving quickly and hopefully we can see improvements in the (very) near future</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:50 UTC</span>

<span style="font-size: 90%;">Let's start with the news on the inside developments</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:09 UTC</span>

<span style="font-size: 90%;">_@airween_ do you want to share the news on ModSecurity's new Web site?</span>

**airween** <span style="color: grey; font-size: 90%;">18:39:36 UTC</span>

<span style="font-size: 90%;">Sorry, I'm in a task, will back soon (15 min) and then, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:08 UTC</span>

<span style="font-size: 90%;">Ofc</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:41 UTC</span>

<span style="font-size: 90%;">There is a comment that I've copied from the agenda template that said: `(↓ Is it possible to clarify/state what the project discussion or decision is that we need to make here? Or should we move these issues to the issues chat so that we will have something to discuss at the issues chat?)`?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:55 UTC</span>

<span style="font-size: 90%;">I think it is really the case we want to make :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:21 UTC</span>

<span style="font-size: 90%;">There are two PRs two discuss.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:26 UTC</span>

<span style="font-size: 90%;">Who brought them in?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:49 UTC</span>

<span style="font-size: 90%;">I guess _@azurit_? :point_up:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:08 UTC</span>

<span style="font-size: 90%;">No, according to the PRs it was _@fzipitria_ :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:26 UTC</span>

<span style="font-size: 90%;">But I didn't bring them to that document :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:38 UTC</span>

<span style="font-size: 90%;">It was me who created the content from the wiki, hence I'm linked</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:45 UTC</span>

<span style="font-size: 90%;">Ah yes :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:25 UTC</span>

<span style="font-size: 90%;">We can discuss without whomever was the sponsor</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:32 UTC</span>

<span style="font-size: 90%;">Yes, the page history suggests it could have been azurit</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:39 UTC</span>

<span style="font-size: 90%;">What is the discussion? It isn't clear what we should discuss</span>

**azurit** <span style="color: grey; font-size: 90%;">18:44:40 UTC</span>

<span style="font-size: 90%;">Yes, it was me.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:42 UTC</span>

<span style="font-size: 90%;">A new approach to something?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:41 UTC</span>

<span style="font-size: 90%;">What are your expectations from the discussion? What needs to be decided?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:46:23 UTC</span>

<span style="font-size: 90%;">I wanted to discuss them because i opened that PRs quite a long time ago without any reaction.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:46:31 UTC</span>

<span style="font-size: 90%;">From other members.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:06 UTC</span>

<span style="font-size: 90%;">Both of them were already automatically closed.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:16 UTC</span>

<span style="font-size: 90%;">Two times.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:17 UTC</span>

<span style="font-size: 90%;">We're quite short on hands these days. So I think the best you can do is adding them to the meeting agenda.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:47:34 UTC</span>

<span style="font-size: 90%;">Isn't it this?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:38 UTC</span>

<span style="font-size: 90%;">So let's discus [https://github.com/coreruleset/coreruleset/pull/3720](https://github.com/coreruleset/coreruleset/pull/3720)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:47 UTC</span>

<span style="font-size: 90%;">I think it is a good approach</span>

**azurit** <span style="color: grey; font-size: 90%;">18:48:44 UTC</span>

<span style="font-size: 90%;">What about NOT catching `HAVING 1`?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:11 UTC</span>

<span style="font-size: 90%;">Was it being catched before?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:49:27 UTC</span>

<span style="font-size: 90%;">I see it as a big fuck up as it is the easiest way how to exploit this kind of vulnerability.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:49:41 UTC</span>

<span style="font-size: 90%;">But catching it will probably create lots of FPs.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:34 UTC</span>

<span style="font-size: 90%;">I think we should work on that PR to get it merged and address `HAVING 1` in a separate issue.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:15 UTC</span>

<span style="font-size: 90%;">There might be plenty of other bypasses</span>

**azurit** <span style="color: grey; font-size: 90%;">18:51:22 UTC</span>

<span style="font-size: 90%;">Ok. What about second problem, `HAVING true`? I wasn't sure if it will create FPs or not.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:39 UTC</span>

<span style="font-size: 90%;">Are we removing sql comments in that rule, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:02 UTC</span>

<span style="font-size: 90%;">To avoid `H/* */A/* 1 */V/* .. */`</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:52:22 UTC</span>

<span style="font-size: 90%;">It will in natural language: "having true grit"</span>

**azurit** <span style="color: grey; font-size: 90%;">18:52:25 UTC</span>

<span style="font-size: 90%;">Not sure. I was developing it quite some time ago.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:42 UTC</span>

<span style="font-size: 90%;">No problem</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:57 UTC</span>

<span style="font-size: 90%;">Just to see if we are tackling evasions, which others could be added</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:26 UTC</span>

<span style="font-size: 90%;">I agree to merge this one (after review) and target additional problems in following rules/PRs</span>

**azurit** <span style="color: grey; font-size: 90%;">18:53:29 UTC</span>

<span style="font-size: 90%;">I can expand my PR if there are other ways how to bypass that rule.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:38 UTC</span>

<span style="font-size: 90%;">Let's merge this one first</span>

**azurit** <span style="color: grey; font-size: 90%;">18:53:43 UTC</span>

<span style="font-size: 90%;">But current form of the rule is really bad.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:52 UTC</span>

<span style="font-size: 90%;">Maybe creating an issue with the things we want to add/test</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:57 UTC</span>

<span style="font-size: 90%;">And then start from there?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:02 UTC</span>

<span style="font-size: 90%;">Yes it is, but at least your PR improves on it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:08 UTC</span>

<span style="font-size: 90%;">I'll assing this one to me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:34 UTC</span>

<span style="font-size: 90%;">BTW, can you fix the conflict?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:54:40 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:49 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:56 UTC</span>

<span style="font-size: 90%;">Let's follow with [https://github.com/coreruleset/coreruleset/pull/3715](https://github.com/coreruleset/coreruleset/pull/3715)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:12 UTC</span>

<span style="font-size: 90%;">Same problem? Not follow up?</span>

**azurit** <span style="color: grey; font-size: 90%;">18:55:26 UTC</span>

<span style="font-size: 90%;">I did a refactor but some tests won't pass.</span>

**azurit** <span style="color: grey; font-size: 90%;">18:55:43 UTC</span>

<span style="font-size: 90%;">Not sure if my refactor is broken or something else happened.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:11 UTC</span>

<span style="font-size: 90%;">Ok, I can follow up with you on the issue itself</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:34 UTC</span>

<span style="font-size: 90%;">Only a couple tests failing. Maybe the tests are bad, or the update you made needs the tests to change. :smile: No problem, I'll try that one out</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:15 UTC</span>

<span style="font-size: 90%;">Any other PR we want to :eyes: ?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:46 UTC</span>

<span style="font-size: 90%;">I guess not for now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:47 UTC</span>

<span style="font-size: 90%;">Could you share a status of the dev retreat preparations? Should we start to talk about focus themes?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:01:10 UTC</span>

<span style="font-size: 90%;">I'm really looking forward to it!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:13 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:55 UTC</span>

<span style="font-size: 90%;">Starr was looking into the options (today OWASP HQ is out because of US Labor Day)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:30 UTC</span>

<span style="font-size: 90%;">She was going to meet with Center Parcs to get us a final quote</span>

**airween** <span style="color: grey; font-size: 90%;">19:02:32 UTC</span>

<span style="font-size: 90%;">Sorry, I'm back

So after a long outage finally we (OWASP) get back the [modsecurity.org](http://modsecurity.org) domain. Few months ago _@dune73_ ans _@Hubert Siwik_ started to prepare the new site with new content.

The website base's is the [Coreruleset.org](http://Coreruleset.org) :slightly_smiling_face: - we use Hugo and if you compare the two sites you can realize that the menu structure is also very similar :slightly_smiling_face:.

The site runs on GH pages, and it's also behind the Cloudflare.

Anyway, I think this is a very important step in project's life, we can inform our users.

Any many thanks for help to _@dune73_, _@fzipitria_, _@Hubert Siwik_, and _@maxleske_.</span>

##### Tue, Sep 3rd, 2024

↳ **Hubert Siwik** <span style="color: grey; font-size: 90%;">05:32:08 UTC</span>

<span style="font-size: 90%;">Thank you guys for remembering me!</span>

### Mon, Sep 2nd, 2024

**dune73** <span style="color: grey; font-size: 90%;">19:03:48 UTC</span>

<span style="font-size: 90%;">This is all on Hubert. He's the litteral genie that popped out of nowhere to help us here.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:35 UTC</span>

<span style="font-size: 90%;">I think the only thing missing now is the Trademark on the term "ModSecurity". This is something for HQ and their lawyers, but otherwise TW has completed the handover.</span>

**airween** <span style="color: grey; font-size: 90%;">19:04:38 UTC</span>

<span style="font-size: 90%;">He helped me in MRTS a bit too (just fyi)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:48 UTC</span>

<span style="font-size: 90%;">I'm aware of that.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:13 UTC</span>

<span style="font-size: 90%;">The nice thing about starting a "new" project is that you find help from people you have not met before.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:32 UTC</span>

<span style="font-size: 90%;">But we're moving away from CRS a bit. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">19:05:37 UTC</span>

<span style="font-size: 90%;">I asked the participants (TW, OWASP) that are we finally done or is there anything left in transfer process, but haven't got any answer.</span>

**airween** <span style="color: grey; font-size: 90%;">19:06:04 UTC</span>

<span style="font-size: 90%;">okay, that's it - sorry for the interrupt</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:18 UTC</span>

<span style="font-size: 90%;">np :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:31 UTC</span>

<span style="font-size: 90%;">These are indeed, good news for the ModSecurity project</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:47 UTC</span>

<span style="font-size: 90%;">And the community in general! :party-crs:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:05 UTC</span>

<span style="font-size: 90%;">Did we talk about the WARM project here?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:07:19 UTC</span>

<span style="font-size: 90%;">It was mentioned last meeting, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:25 UTC</span>

<span style="font-size: 90%;">OK</span>

**azurit** <span style="color: grey; font-size: 90%;">19:07:32 UTC</span>

<span style="font-size: 90%;">What's that?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:38 UTC</span>

<span style="font-size: 90%;">It should be approved by the project committee in their September meeting.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:19 UTC</span>

<span style="font-size: 90%;">It's an attempt to improve (CRS) rules (e.g. spread across paranoia levels) with the help of machine learning. Their planned step one: Assemble large sets of sample traffic (good and bad).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:45 UTC</span>

<span style="font-size: 90%;">Good luck with that</span>

**azurit** <span style="color: grey; font-size: 90%;">19:09:03 UTC</span>

<span style="font-size: 90%;">Sounds scary.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:11 UTC</span>

<span style="font-size: 90%;">(it has been a problem forever to get sample traffic)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:12 UTC</span>

<span style="font-size: 90%;">Look for scientific papers with author "Davide Ariu". Also worth to watch his Lisbon talk. It's easier to understand there than from the papers.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:44 UTC</span>

<span style="font-size: 90%;">And, just to remind me, how is this related to CRS? Are they using the rules?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:15 UTC</span>

<span style="font-size: 90%;">They are aiming for a general approach, but the test case is CRS.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:33 UTC</span>

<span style="font-size: 90%;">So they will  have their own models.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:09 UTC</span>

<span style="font-size: 90%;">Well, hopefully everything goes well  for them and then CRS can adapt and enhance detections</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:26 UTC</span>

<span style="font-size: 90%;">Imagine a rule set that is optimized for certain traffic it has been trained for and it used exactly those rules that are best to tell good from bad traffic. I doubt it can be generalized, but I am sure there is room to improve the scoring and the spread across the PLs for our rules. But it depends on the sample traffic.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:12:51 UTC</span>

<span style="font-size: 90%;">Sample traffic is always the problem.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:06 UTC</span>

<span style="font-size: 90%;">I see a bigger problem with AI than this: It will output some rules or modifications to our work without ANYONE to understand it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:24 UTC</span>

<span style="font-size: 90%;">Depends.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:02 UTC</span>

<span style="font-size: 90%;">If the output says: rule "xyz" has too many false positives in PL1, but on PL3 is fine, then it is valuable</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:22 UTC</span>

<span style="font-size: 90%;">For now their only target was SQLi, so I think things will take time to evolve</span>

**azurit** <span style="color: grey; font-size: 90%;">19:15:28 UTC</span>

<span style="font-size: 90%;">But will anyone understand why?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:53 UTC</span>

<span style="font-size: 90%;">Hopefully yes. But if not, we'll discuss it :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:02 UTC</span>

<span style="font-size: 90%;">Do they have to understand why?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:16:13 UTC</span>

<span style="font-size: 90%;">We need to understand.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:16:20 UTC</span>

<span style="font-size: 90%;">It is our primary work.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:24 UTC</span>

<span style="font-size: 90%;">Do we understand 100% of our rules?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:38 UTC</span>

<span style="font-size: 90%;">The good thing will be, that we should get into a position where we understand this published research. So far it's been a thesis we could not reproduce. This will improve now.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:17:31 UTC</span>

<span style="font-size: 90%;">I think we do understand all of our work as a group.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:17:54 UTC</span>

<span style="font-size: 90%;">My target is at some point to have the rules really understood. But there is history that not even Christian or myself know.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:08 UTC</span>

<span style="font-size: 90%;">And this should come with cleanup and documentation</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:19 UTC</span>

<span style="font-size: 90%;">But that's for CRS v...6?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:21 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:11 UTC</span>

<span style="font-size: 90%;">The doc is actually scheduled for the time after v4 is out. So about now.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:26 UTC</span>

<span style="font-size: 90%;">But I have a hard time finding the queue where people are lining up to attack this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:54 UTC</span>

<span style="font-size: 90%;">Dexter popped up a couple of weeks ago with a doc inititive. Did we bore him by not reacting? Are you still in touch _@fzipitria_?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:20:57 UTC</span>

<span style="font-size: 90%;">I'm in touch, but he doesn't react so quickly... if at all</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:22:54 UTC</span>

<span style="font-size: 90%;">Anyway, I think we covered up some topics today</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:27 UTC</span>

<span style="font-size: 90%;">I will be pestering OWASP HQ this next week for the developer retreat, so expect news</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:56 UTC</span>

<span style="font-size: 90%;">For all those who confirmed attending, I'll be sending you more details in DM</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:17 UTC</span>

<span style="font-size: 90%;">it would be good to get some news. 2 months are left, we should start to check the flight tickets and organize the event</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:36 UTC</span>

<span style="font-size: 90%;">That's priority -1 for me now</span>

**airween** <span style="color: grey; font-size: 90%;">19:24:38 UTC</span>

<span style="font-size: 90%;">how many people will attend?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:45 UTC</span>

<span style="font-size: 90%;">10-13</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:55 UTC</span>

<span style="font-size: 90%;">:crossed_fingers:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:25:46 UTC</span>

<span style="font-size: 90%;">For anyone that wants review on their PRs, feel free to ping me</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:23 UTC</span>

<span style="font-size: 90%;">See you at the issues chat in two weeks for those who will be around :wave: :party-crs:</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:30 UTC</span>

<span style="font-size: 90%;">issue 3809 would be a good topic for retreat</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:26:49 UTC</span>

<span style="font-size: 90%;">Please add to the wiki page :smile:</span>

**airween** <span style="color: grey; font-size: 90%;">19:26:57 UTC</span>

<span style="font-size: 90%;">okay</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:27:07 UTC</span>

<span style="font-size: 90%;">Good night! :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:10 UTC</span>

<span style="font-size: 90%;">Night.</span>

**airween** <span style="color: grey; font-size: 90%;">19:27:15 UTC</span>

<span style="font-size: 90%;">good night!</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:27:20 UTC</span>

<span style="font-size: 90%;">good night</span>

**azurit** <span style="color: grey; font-size: 90%;">19:27:22 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">19:27:25 UTC</span>

<span style="font-size: 90%;">Bye!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:29:27 UTC</span>

<span style="font-size: 90%;">bb!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:58 UTC</span>

<span style="font-size: 90%;">Good night!</span>

