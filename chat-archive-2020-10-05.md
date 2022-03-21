### Mon, Oct 5th, 2020

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:43 UTC</span>

<span style="font-size: 90%;">Hi all!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:30:51 UTC</span>

<span style="font-size: 90%;">Hi</span>

**walter** <span style="color: grey; font-size: 90%;">18:30:53 UTC</span>

<span style="font-size: 90%;">hello everybody!</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:18 UTC</span>

<span style="font-size: 90%;">since Christian is not here today, for very sound reasons I may add :slightly_smiling_face: I will take over the agenda</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:25 UTC</span>

<span style="font-size: 90%;">hi there!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:19 UTC</span>

<span style="font-size: 90%;">before we start on the agenda, I’d like first to start with a question for _@azurIt_ as discussed by Christian and me, would you mind joining the project officially as a developer?  :slightly_smiling_face:</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:36 UTC</span>

<span style="font-size: 90%;">hello everybody :wave:</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:46 UTC</span>

<span style="font-size: 90%;">your recent contributions are great hence our idea</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:33:07 UTC</span>

<span style="font-size: 90%;">@walter thank you :slightly_smiling_face: yes, i would like to join</span>

**walter** <span style="color: grey; font-size: 90%;">18:33:31 UTC</span>

<span style="font-size: 90%;">that’s awesome, welcome on board :slightly_smiling_face: I will sort out the github stuff after the chat!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:33:39 UTC</span>

<span style="font-size: 90%;">ciao!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:34:06 UTC</span>

<span style="font-size: 90%;">thank you for trust!</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:19 UTC</span>

<span style="font-size: 90%;">welcome _@azurIt_! :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:19 UTC</span>

<span style="font-size: 90%;">shall we look at the agenda? [https://github.com/coreruleset/coreruleset/issues/1892](https://github.com/coreruleset/coreruleset/issues/1892)</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:55 UTC</span>

<span style="font-size: 90%;">start from the top? I’d love to try to make this meet as quick as possible, but as slow as needed</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:36:27 UTC</span>

<span style="font-size: 90%;">ok for me</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:36:36 UTC</span>

<span style="font-size: 90%;">[#1895](https://github.com/coreruleset/coreruleset/issues/#1895) -> if it fixes a FP on wordpress, I agree :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:36 UTC</span>

<span style="font-size: 90%;">Sounds good</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:36:41 UTC</span>

<span style="font-size: 90%;">sure</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:05 UTC</span>

<span style="font-size: 90%;">first one is [https://github.com/coreruleset/coreruleset/pull/1895](https://github.com/coreruleset/coreruleset/pull/1895)</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">apparently the site health emits some SQL status notices which trigger our outbound rule… not a big risk to disable that rule selectively IMHO</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:43 UTC</span>

<span style="font-size: 90%;">I see some thumbs up and no thumbs down so far, this could be a good workflow :slightly_smiling_face: merging?</span>

**airween** <span style="color: grey; font-size: 90%;">18:38:54 UTC</span>

<span style="font-size: 90%;">go</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:11 UTC</span>

<span style="font-size: 90%;">on to the next one: [https://github.com/coreruleset/coreruleset/pull/1894](https://github.com/coreruleset/coreruleset/pull/1894)</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:52 UTC</span>

<span style="font-size: 90%;">_@azurIt_ made a good comment on this. I excluded rule 921110 due to some modsec log which was emailed to me privately. but, I agree with it that it would be better to improve rule 921110…</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:02 UTC</span>

<span style="font-size: 90%;">and in that case, we shouldn’t have to exclude that rule here</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:37 UTC</span>

<span style="font-size: 90%;">the issue to improve the rule is in here: [https://github.com/coreruleset/coreruleset/issues/1883](https://github.com/coreruleset/coreruleset/issues/1883) and it is being worked on. so I think I better withdraw my proposal</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:23 UTC</span>

<span style="font-size: 90%;">that issue is not in the chat agenda, I haven’t followed it closely as I’m not so familiar with HTTP request smuggling myself… do we think it needs more attention? we could discuss about it</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:42:56 UTC</span>

<span style="font-size: 90%;">Unfortunately, i'm not familiar with that type of attack too but i assume that fix was tested.</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:19 UTC</span>

<span style="font-size: 90%;">shall I remove it from PR, pending the improvement of rule? we won’t have a release very soon, so there is still time to work on 921110</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:23 UTC</span>

<span style="font-size: 90%;">I think it would be better to schedule it (1883) to the next chat meeting</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:43 UTC</span>

<span style="font-size: 90%;">OK, let’s do that! in the meantime I will withdraw my commit</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:39 UTC</span>

<span style="font-size: 90%;">I think otherwise the PR is acceptable to you? the other changes are small. I could merge it after removing the 921110 reference.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:46 UTC</span>

<span style="font-size: 90%;">With this context, definitely</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:44:50 UTC</span>

<span style="font-size: 90%;">[#1883](https://github.com/coreruleset/coreruleset/issues/#1883) -> the FP example comes from a free text input. It could triggers any rules of the rule-set…</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:54 UTC</span>

<span style="font-size: 90%;">that’s true, but I did notice that the rule can come up rather often, and because it runs on REQUEST_BODY, it’s a bit hard to exclude specifically for one text field</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:02 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ - the problem is not that, see the last comment</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:47:45 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:38 UTC</span>

<span style="font-size: 90%;">this brings us to the next PR: [https://github.com/coreruleset/coreruleset/pull/1893](https://github.com/coreruleset/coreruleset/pull/1893)</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:50 UTC</span>

<span style="font-size: 90%;">this looks like some awesome work on providing an phpBB exclusion package!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:49:04 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:49:05 UTC</span>

<span style="font-size: 90%;">that’s nice</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:25 UTC</span>

<span style="font-size: 90%;">yes that’s awesome, forums are one of the most (successfuly) attacked sites</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:59 UTC</span>

<span style="font-size: 90%;">Why it is commented on phase 1?</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:08 UTC</span>

<span style="font-size: 90%;">perhaps because all the rules use phase 2… but still, I would prefer to keep it in, to keep consistency and just in case someone adds a phase 1 rule to the file later</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:51:12 UTC</span>

<span style="font-size: 90%;">Because none of the rules are working with headers only.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:51:26 UTC</span>

<span style="font-size: 90%;">But maybe i misunderstood something?</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:45 UTC</span>

<span style="font-size: 90%;">no you are correct, this should function perfectly.. it’s just the way we do it in all the other the exclusion files</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:52:06 UTC</span>

<span style="font-size: 90%;">What about performance?</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:26 UTC</span>

<span style="font-size: 90%;">I don’t know enough about the engine internals to say if it helps or hurts performance…</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:53:02 UTC</span>

<span style="font-size: 90%;">Will engine run that rules also in phase 1 if i uncomment it?</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:39 UTC</span>

<span style="font-size: 90%;">yes, it will</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:54:02 UTC</span>

<span style="font-size: 90%;">Then it probably hurts performance.</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:44 UTC</span>

<span style="font-size: 90%;">so would you say it’s better for performance to leave the 9007000 active? _@airween_</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:56:13 UTC</span>

<span style="font-size: 90%;">sorry, no :slightly_smiling_face:. I just though if the comments will removed then engine will evaluate it</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:52 UTC</span>

<span style="font-size: 90%;">I may be misunderstanding</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:08 UTC</span>

<span style="font-size: 90%;">you should replace these @rx op by something different, eg: @within</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:56:39 UTC</span>

<span style="font-size: 90%;">_@walter_ If rules are run in both phase 1 and 2, i think it will hurts performance as there's no (currently) reason to run them in phase 1, none of them will trigger anything.</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:16 UTC</span>

<span style="font-size: 90%;">I don’t know for certain if that’s true, I think if modsec is smart, it won’t have references to that rule in phase 1 at all.. but I don’t know for sure</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:02 UTC</span>

<span style="font-size: 90%;">if modsec does process all the rules in phase 1 (even skipping them), then removing the comment chars would improve performance</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:58:08 UTC</span>

<span style="font-size: 90%;">_@airween_ Will 'within' do it correctly? I mean, will it only match the whole words specified in parameter?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:58:49 UTC</span>

<span style="font-size: 90%;">I think yes, it will.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">18:59:16 UTC</span>

<span style="font-size: 90%;">Ok, i will update the rules using within.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:59:19 UTC</span>

<span style="font-size: 90%;">see the example:
[https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-(v2.x)#within](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-(v2.x)#within)</span>

↳ **walter** <span style="color: grey; font-size: 90%;">18:59:31 UTC</span>

<span style="font-size: 90%;">sounds good</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:00:37 UTC</span>

<span style="font-size: 90%;">What about that NOTE in the description?</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:02:40 UTC</span>

<span style="font-size: 90%;">I think it is doing matches the way i was afraid it is. And with that 'artifical' delimiters it looks realyl ugly.</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:03:00 UTC</span>

<span style="font-size: 90%;">Is performance really much higher then using @rx ?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:03:18 UTC</span>

<span style="font-size: 90%;">I will check that soon and will notify you</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:03:39 UTC</span>

<span style="font-size: 90%;">I think @rx has the higher cost</span>

↳ **walter** <span style="color: grey; font-size: 90%;">19:03:49 UTC</span>

<span style="font-size: 90%;">great. I would think performance is not a huge concern, as the first step is to match on the filename - processing will stop there for 99.9% of incoming requests</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:05:59 UTC</span>

<span style="font-size: 90%;">Cool. I really don't like to use 'within'. What about 'pm'?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:06:19 UTC</span>

<span style="font-size: 90%;">that's what I wanted to propose :slightly_smiling_face:</span>

↳ **azurIt** <span style="color: grey; font-size: 90%;">19:08:34 UTC</span>

<span style="font-size: 90%;">Ok :slightly_smiling_face: i will look at it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:13 UTC</span>

<span style="font-size: 90%;">as a last one, what do you think about the last section “unknown but seen in the wild” - looks like some google addon, but if it’s common, why not add it? looks like it won’t hurt</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:06:02 UTC</span>

<span style="font-size: 90%;">it would be nice to have it together with other google stuff, isn’t it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:35 UTC</span>

<span style="font-size: 90%;">I have covered some 3rd party extensions in the Xenforo profile as well, as they tend to be somewhat common</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:06:48 UTC</span>

<span style="font-size: 90%;">ah oky!</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:05 UTC</span>

<span style="font-size: 90%;">and I think sooner or later we’ll have to do this for wordpress as well, as some plugins are so common</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:22 UTC</span>

<span style="font-size: 90%;">e.g. WooCommerce</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:07:29 UTC</span>

<span style="font-size: 90%;">yeah definitely</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:07:39 UTC</span>

<span style="font-size: 90%;">_@walter_ i saw it on our servers and i was able to google it on some forum about phpbb - it was, something like, recommended solution for adding google adsense.</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:51 UTC</span>

<span style="font-size: 90%;">then I’d say just enable it :+1:</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:07:58 UTC</span>

<span style="font-size: 90%;">ok</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:09:45 UTC</span>

<span style="font-size: 90%;">I must add, that it involves editing phpbb files by hand.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:10:16 UTC</span>

<span style="font-size: 90%;">It wasn't, like, extension.</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:46 UTC</span>

<span style="font-size: 90%;">as for the first rule 9007000, we may have a misunderstanding so to clear up, I think it will be safer to uncomment it as a matter of style and to make sure another phpbb rule writer who uses phase 1, will also have the correct behavior (if we comment that rule out, then modsec won’t skip over this file if a user has crs_exclusions_phpbb=0)</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:43 UTC</span>

<span style="font-size: 90%;">anyway we can discuss further in the issue if needed :slightly_smiling_face: I will note in the issue.</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:17 UTC</span>

<span style="font-size: 90%;">next issue!</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:25 UTC</span>

<span style="font-size: 90%;">and of course thank you very much for putting this together</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:12:54 UTC</span>

<span style="font-size: 90%;">it was fun :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:02 UTC</span>

<span style="font-size: 90%;">yes it is! making exclusions is a lot of fun</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:08 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1887](https://github.com/coreruleset/coreruleset/pull/1887) next one!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:56 UTC</span>

<span style="font-size: 90%;">Don't we generate that regexp?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:14:16 UTC</span>

<span style="font-size: 90%;">yes, we do :)</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:56 UTC</span>

<span style="font-size: 90%;">this looks a little more complex</span>

**airween** <span style="color: grey; font-size: 90%;">19:14:16 UTC</span>

<span style="font-size: 90%;">yes, we do :)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">19:14:16 UTC</span>

<span style="font-size: 90%;">yes, we do :)</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:52 UTC</span>

<span style="font-size: 90%;">yes, this regexp is autogenerated from regexp-92100.txt</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:07 UTC</span>

<span style="font-size: 90%;">I think the regex got a prefix:
(?<!&#[0-9]{2})(?<!&#[0-9]{3})(?<!&#[0-9]{4})</span>

**airween** <span style="color: grey; font-size: 90%;">19:15:31 UTC</span>

<span style="font-size: 90%;">the generated part is same as before</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:16:21 UTC</span>

<span style="font-size: 90%;">Ok, so we should change that one instead</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:59 UTC</span>

<span style="font-size: 90%;">I see the problem yeah with html entities ending in ;  thus triggering a false positive…</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:07 UTC</span>

<span style="font-size: 90%;">but would this not open up a possibly bypass?</span>

**Piotr Pazoła** <span style="color: grey; font-size: 90%;">19:20:02 UTC</span>

<span style="font-size: 90%;">Hello guys. I'm the author of [#1887](https://github.com/coreruleset/coreruleset/issues/#1887). The case is to ignore the issue straight in the core rule. Maybe the second approach could be to make some exclusion, i.e. for specific charsets that I described in issue [#1886](https://github.com/coreruleset/coreruleset/issues/#1886) - the subset of iso-8859. I've made some test and seems to be fine, it's triggered even the html entity is the part of the value of arg</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:24 UTC</span>

<span style="font-size: 90%;">hi _@Piotr Pazoła_ and thank you for the well described issue!</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:43 UTC</span>

<span style="font-size: 90%;">I think this may need a bit of investigating, is anyone interested in reviewing it?</span>

**airween** <span style="color: grey; font-size: 90%;">19:21:53 UTC</span>

<span style="font-size: 90%;">_@Piotr Pazoła_ that should be fine to see more tests (under tests/regression/tests directory)</span>

**airween** <span style="color: grey; font-size: 90%;">19:22:43 UTC</span>

<span style="font-size: 90%;">both true positive and true negative cases</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:21 UTC</span>

<span style="font-size: 90%;">I won’t have time to look into it myself soon sadly</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:25 UTC</span>

<span style="font-size: 90%;">any takers? :wink:</span>

**Piotr Pazoła** <span style="color: grey; font-size: 90%;">19:25:01 UTC</span>

<span style="font-size: 90%;">Ok, I can write some yamls based on it what I describe in issue [#1886](https://github.com/coreruleset/coreruleset/issues/#1886) and I will try to make some additional tests</span>

**Piotr Pazoła** <span style="color: grey; font-size: 90%;">19:25:13 UTC</span>

<span style="font-size: 90%;">And it'll be cool to review the rule anyway</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:22 UTC</span>

<span style="font-size: 90%;">yes please that will help us ensure that it works as intended :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:25:36 UTC</span>

<span style="font-size: 90%;">I can try to review it.....</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:43 UTC</span>

<span style="font-size: 90%;">that would be lovely!</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:07 UTC</span>

<span style="font-size: 90%;">also, finally the result should also be pasted in the comment above:
# Then insert the assembled regexp into this template:
#
# SecRule REQUEST_COOKIES|!REQUEST_COOKIES:/__utm/|REQUEST_COOKIES_NAMES|ARGS_NAMES|ARGS|XML:/* "@rx ...</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:17 UTC</span>

<span style="font-size: 90%;">so that the next one autogenerating the rest of the regexp will also use your changes at the start of the regexp</span>

**Piotr Pazoła** <span style="color: grey; font-size: 90%;">19:26:49 UTC</span>

<span style="font-size: 90%;">Yes, right!</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:21 UTC</span>

<span style="font-size: 90%;">awesome!</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:30 UTC</span>

<span style="font-size: 90%;">then we’ll get back to it next meeting!</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:44 UTC</span>

<span style="font-size: 90%;">again, a lot of thanks for submitting - really good issue</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:12 UTC</span>

<span style="font-size: 90%;">next issue is a documentation one - [https://github.com/coreruleset/coreruleset/pull/1885](https://github.com/coreruleset/coreruleset/pull/1885)</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:36 UTC</span>

<span style="font-size: 90%;">looks good to me!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:13 UTC</span>

<span style="font-size: 90%;">approved by fgs, can be merged</span>

**airween** <span style="color: grey; font-size: 90%;">19:29:15 UTC</span>

<span style="font-size: 90%;">merge it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:22 UTC</span>

<span style="font-size: 90%;">done!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:29:31 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:29:39 UTC</span>

<span style="font-size: 90%;">hahahha</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:46 UTC</span>

<span style="font-size: 90%;">next one! [https://github.com/coreruleset/coreruleset/pull/1879](https://github.com/coreruleset/coreruleset/pull/1879)</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:21 UTC</span>

<span style="font-size: 90%;">this one is a bit weird as the source is unknown repository and it also contains phpBB stuff…</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:33 UTC</span>

<span style="font-size: 90%;">I think it’s probably best to start with a clean PR, but otherwise I agree with the contents!</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:30:47 UTC</span>

<span style="font-size: 90%;">heh, i even don't remember sending it, sorry for mess.</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:01 UTC</span>

<span style="font-size: 90%;">if you can remake it, we can merge it directly</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:08 UTC</span>

<span style="font-size: 90%;">alrighty! next one?</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:16 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1877](https://github.com/coreruleset/coreruleset/pull/1877)</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:33:04 UTC</span>

<span style="font-size: 90%;">This was my task from previous chat.</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:10 UTC</span>

<span style="font-size: 90%;">this is also from unknown repository and contains also some WordPress stuff, I guess some git trouble :smile:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:33:18 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:22 UTC</span>

<span style="font-size: 90%;">otherwise I think it’s great</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:54 UTC</span>

<span style="font-size: 90%;">there’s also a nice test and it passes</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:33:59 UTC</span>

<span style="font-size: 90%;">Stupid OT question: Can i fork some repository multiple times?</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:34:22 UTC</span>

<span style="font-size: 90%;">I'm probably misunderstanding how github works.</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:23 UTC</span>

<span style="font-size: 90%;">seems not possible :confused:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">No, I don't think so.</span>

**walter** <span style="color: grey; font-size: 90%;">19:34:30 UTC</span>

<span style="font-size: 90%;">but you can work in different branches!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:34:45 UTC</span>

<span style="font-size: 90%;">yes def different branches ftw</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:02 UTC</span>

<span style="font-size: 90%;">I would recommend, git co v3.4/dev and then starting a new branch like git co -b fix-92841</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:13 UTC</span>

<span style="font-size: 90%;">then do that work, then go back to v3.4/dev and restart for your second PR</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:42 UTC</span>

<span style="font-size: 90%;">then you can make a PR for every branch</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:35:51 UTC</span>

<span style="font-size: 90%;">ok, thank you.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:36:21 UTC</span>

<span style="font-size: 90%;">I still use Walters git manual from 2016!!</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:22 UTC</span>

<span style="font-size: 90%;">if you need help just shout here, we all have our troubles with git, but you live with it :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:26 UTC</span>

<span style="font-size: 90%;">next one!</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:27 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1876](https://github.com/coreruleset/coreruleset/pull/1876)</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:42 UTC</span>

<span style="font-size: 90%;">looks good to me!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:38:00 UTC</span>

<span style="font-size: 90%;">me too</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:34 UTC</span>

<span style="font-size: 90%;">I’m merging it!</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:09 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1868](https://github.com/coreruleset/coreruleset/pull/1868) is the next one</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:13 UTC</span>

<span style="font-size: 90%;">this seems to be still undergoing work? there’s an interesting conversion script included</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:40:29 UTC</span>

<span style="font-size: 90%;">This was my task, but I didn't do anything... Sorry :disappointed: Did not have the time.</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:48 UTC</span>

<span style="font-size: 90%;">I can sympathize. my time is also very much limited. sometimes it’s just like that. shall we shift it to a next meeting?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:40:51 UTC</span>

<span style="font-size: 90%;">Ah, no! That was not mine...</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:02 UTC</span>

<span style="font-size: 90%;">it seems that dune73 wants to blog about it :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:41:45 UTC</span>

<span style="font-size: 90%;">Yes! Sorry!
And thank you for your understanding. It was an other tasks... :smiley:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:42:10 UTC</span>

<span style="font-size: 90%;">So we still shift it to next meeting...</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:16 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**airween** <span style="color: grey; font-size: 90%;">19:42:49 UTC</span>

<span style="font-size: 90%;">ohhh... "The upcoming one about msc_pcretest." :heart:</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:59 UTC</span>

<span style="font-size: 90%;">that’s going to be good!</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:18 UTC</span>

<span style="font-size: 90%;">next one is next one is [https://github.com/coreruleset/coreruleset/pull/1848](https://github.com/coreruleset/coreruleset/pull/1848)</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:43:46 UTC</span>

<span style="font-size: 90%;">This look like my [#1877](https://github.com/coreruleset/coreruleset/pull/1877)</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:47 UTC</span>

<span style="font-size: 90%;">this seems to be a version that azurit made in [https://github.com/coreruleset/coreruleset/pull/1877](https://github.com/coreruleset/coreruleset/pull/1877)</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:06 UTC</span>

<span style="font-size: 90%;">ok, so I’ll close this with a nice message</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:10 UTC</span>

<span style="font-size: 90%;">since sempervictus didn’t reply since july</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:08 UTC</span>

<span style="font-size: 90%;">another one! [https://github.com/coreruleset/coreruleset/pull/1845](https://github.com/coreruleset/coreruleset/pull/1845)</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:38 UTC</span>

<span style="font-size: 90%;">seems to be ready for merge pending some more information</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:46:54 UTC</span>

<span style="font-size: 90%;">Looks like it has conflicts now</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:59 UTC</span>

<span style="font-size: 90%;">uh-oh…</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:30 UTC</span>

<span style="font-size: 90%;">okay, so we want to wait for that</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:26 UTC</span>

<span style="font-size: 90%;">it’s already getting a bit late, how long should we continue?</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:54 UTC</span>

<span style="font-size: 90%;">I may not be as fast as Christian with this… :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:35 UTC</span>

<span style="font-size: 90%;">is anybody still here even, lol</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:49:40 UTC</span>

<span style="font-size: 90%;">It's not because of you :slightly_smiling_face:</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">19:50:10 UTC</span>

<span style="font-size: 90%;">I'm here, reading quietly :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:18 UTC</span>

<span style="font-size: 90%;">I’ll just keep going then</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:26 UTC</span>

<span style="font-size: 90%;">the next issues are marked as needing some work…</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:50:37 UTC</span>

<span style="font-size: 90%;">sorry, i will be back, hopefully, in 30 minutes, i really have to go for a while :(</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:02 UTC</span>

<span style="font-size: 90%;">oh I really want to be in bed in 30 minutes :sweat_smile: they are doing construction here starting at 7AM :sob:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:51:25 UTC</span>

<span style="font-size: 90%;">Oh!</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:29 UTC</span>

<span style="font-size: 90%;">let’s see how far we can get :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:42 UTC</span>

<span style="font-size: 90%;">next issue is [https://github.com/coreruleset/coreruleset/pull/1878](https://github.com/coreruleset/coreruleset/pull/1878)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:02 UTC</span>

<span style="font-size: 90%;">Yeah, this one is easy</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:16 UTC</span>

<span style="font-size: 90%;">I like this</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:36 UTC</span>

<span style="font-size: 90%;">After merging we have two more that I need to work with</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:49 UTC</span>

<span style="font-size: 90%;">But now I would be able</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:03 UTC</span>

<span style="font-size: 90%;">do you want to keep working @within this PR or shall we merge already?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:53:24 UTC</span>

<span style="font-size: 90%;">It's ready to merge</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:32 UTC</span>

<span style="font-size: 90%;">doing it! thank you!</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:47 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1846](https://github.com/coreruleset/coreruleset/pull/1846) py3 support!</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:18 UTC</span>

<span style="font-size: 90%;">besides py3 it also uses latest ftw on master branch.. is that stable?</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:30 UTC</span>

<span style="font-size: 90%;">probably the best call, right?</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:12 UTC</span>

<span style="font-size: 90%;">it would help our project also to find regressions in ftw, although at times a regression might bog us down for a bit</span>

**walter** <span style="color: grey; font-size: 90%;">19:55:20 UTC</span>

<span style="font-size: 90%;">all in all, I think I approve!</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:09 UTC</span>

<span style="font-size: 90%;">but it’s marked as need-to-review by _@fgs_ so maybe we should have him make the final call</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:16 UTC</span>

<span style="font-size: 90%;">so let’s keep it assigned to him and open, OK?</span>

**airween** <span style="color: grey; font-size: 90%;">19:56:28 UTC</span>

<span style="font-size: 90%;">hmm... there was a failed test:
[https://github.com/coreruleset/coreruleset/pull/1846/checks?check_run_id=1083199936](https://github.com/coreruleset/coreruleset/pull/1846/checks?check_run_id=1083199936)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:09 UTC</span>

<span style="font-size: 90%;">Not yet</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:14 UTC</span>

<span style="font-size: 90%;">We still fail a test</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:30 UTC</span>

<span style="font-size: 90%;">Federico hasn't been able to fully migrate it to py3 yet</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:13 UTC</span>

<span style="font-size: 90%;">and maybe then they can cut a release and we won’t have to use master</span>

**walter** <span style="color: grey; font-size: 90%;">19:58:19 UTC</span>

<span style="font-size: 90%;">OK, leaving this one open for now then.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:25 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:07 UTC</span>

<span style="font-size: 90%;">on and on we go! [https://github.com/coreruleset/coreruleset/pull/1817](https://github.com/coreruleset/coreruleset/pull/1817)</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:59:28 UTC</span>

<span style="font-size: 90%;">Ah, this one was mine!</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:36 UTC</span>

<span style="font-size: 90%;">and also mine!</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:42 UTC</span>

<span style="font-size: 90%;">will we do it this month? :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:50 UTC</span>

<span style="font-size: 90%;">guess we’ll find out — not ready to merge right now.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:59:56 UTC</span>

<span style="font-size: 90%;">Yes  ;-)</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:22 UTC</span>

<span style="font-size: 90%;">maybe we should schedule a chat some timeslot to look at it together</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:26 UTC</span>

<span style="font-size: 90%;">for now, skipping!</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:50 UTC</span>

<span style="font-size: 90%;">it’s an important issue though, I feel ashamed for not handling it sooner.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">20:04:00 UTC</span>

<span style="font-size: 90%;">Don't feel ashamed!! As you said, we all have limited time...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:01:04 UTC</span>

<span style="font-size: 90%;">Thank you :heart_eyes:
Some chat to add some pressure, at least for me :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:47 UTC</span>

<span style="font-size: 90%;">sometimes hard things can become easy when you look at it with multiple eyes :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:56 UTC</span>

<span style="font-size: 90%;">I mean, more than 2</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:02:18 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:24 UTC</span>

<span style="font-size: 90%;">on we go to [https://github.com/coreruleset/coreruleset/pull/1794](https://github.com/coreruleset/coreruleset/pull/1794)</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:03:14 UTC</span>

<span style="font-size: 90%;">yeah, I’ve lost the point here sorry. I’ll check both 1794 and 1793 and try to finish them up</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:14 UTC</span>

<span style="font-size: 90%;">looks like there is some test failling..</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:28 UTC</span>

<span style="font-size: 90%;">ok :slightly_smiling_face: keeping them assigned to you and we’ll revisit next time.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:40 UTC</span>

<span style="font-size: 90%;">thank you</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:40 UTC</span>

<span style="font-size: 90%;">now there is [https://github.com/coreruleset/coreruleset/pull/1847](https://github.com/coreruleset/coreruleset/pull/1847)</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:01 UTC</span>

<span style="font-size: 90%;">but! the meeting notes that it may be superseded by another PR</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:26 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/1878](https://github.com/coreruleset/coreruleset/pull/1878) *</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:07 UTC</span>

<span style="font-size: 90%;">which was just merged</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:43 UTC</span>

<span style="font-size: 90%;">I’m not sure that it supersedes it, it looks to do something different…</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:07 UTC</span>

<span style="font-size: 90%;">I think they both cover different endpoints, right? so this PR [#1847](https://github.com/coreruleset/coreruleset/issues/#1847) is still relevant, it only needs to be rebased</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:09:26 UTC</span>

<span style="font-size: 90%;">I think the comment, that its superseded, is wrong...</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:45 UTC</span>

<span style="font-size: 90%;">maybe it meant that it would cause a conflict as they work on the same code</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:50 UTC</span>

<span style="font-size: 90%;">cause that’s the case!</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:55 UTC</span>

<span style="font-size: 90%;">ask for a rebase and merge?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:32 UTC</span>

<span style="font-size: 90%;">See comment here:
[https://github.com/coreruleset/coreruleset/pull/1847#issuecomment-688752970](https://github.com/coreruleset/coreruleset/pull/1847#issuecomment-688752970)</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:46 UTC</span>

<span style="font-size: 90%;">ah we already decided :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:48 UTC</span>

<span style="font-size: 90%;">great!</span>

**walter** <span style="color: grey; font-size: 90%;">20:10:53 UTC</span>

<span style="font-size: 90%;">I’ll @ the author</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:10:58 UTC</span>

<span style="font-size: 90%;">yes, in the last meeting.</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:57 UTC</span>

<span style="font-size: 90%;">great! last PR: [https://github.com/coreruleset/coreruleset/issues/1883](https://github.com/coreruleset/coreruleset/issues/1883)</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:09 UTC</span>

<span style="font-size: 90%;">this issue has quite some discussion already</span>

**airween** <span style="color: grey; font-size: 90%;">20:12:32 UTC</span>

<span style="font-size: 90%;">(it's not a PR yet :slightly_smiling_face:)</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:44 UTC</span>

<span style="font-size: 90%;">ooh haha</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:58 UTC</span>

<span style="font-size: 90%;">now I wish I went to the HTTP Request Smuggling talk at Appsec, instead I choose a not so interesting one</span>

**walter** <span style="color: grey; font-size: 90%;">20:13:08 UTC</span>

<span style="font-size: 90%;">so I’m a bit out of the loop here</span>

**airween** <span style="color: grey; font-size: 90%;">20:13:45 UTC</span>

<span style="font-size: 90%;">there is a suggestion for the regex, I've created a regex101 case, including the regression test subjects</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:01 UTC</span>

<span style="font-size: 90%;">but I think we should discuss it at next time</span>

**airween** <span style="color: grey; font-size: 90%;">20:14:13 UTC</span>

<span style="font-size: 90%;">it's too late now</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:26 UTC</span>

<span style="font-size: 90%;">yeah maybe a good one to start with :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:52 UTC</span>

<span style="font-size: 90%;">OK we’ll leave this one open. but it seems that we’ll likely solve this, which is good and will fix a lot of FP</span>

**walter** <span style="color: grey; font-size: 90%;">20:15:29 UTC</span>

<span style="font-size: 90%;">we have some other items (won’t call them non-issues :smile: )</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:29 UTC</span>

<span style="font-size: 90%;">First, the CRS kindergarten, which probably will be renamed. it’s a proposal for a process to start with rules before adding them to the ‘core’ blocking set: [https://gist.github.com/crsgists/da17ed749e48e879ba3f7de698cc221e](https://gist.github.com/crsgists/da17ed749e48e879ba3f7de698cc221e)</span>

**walter** <span style="color: grey; font-size: 90%;">20:17:28 UTC</span>

<span style="font-size: 90%;">it’s getting a bit late but it’s a good read. I would propose to note down any comments and discuss it at the next meeting (_@fzipitria_ _@SpartanTri_ there are some specific questions for you and me)</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:17 UTC</span>

<span style="font-size: 90%;">oh, CRS Meetings needs to decide on the name</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:20 UTC</span>

<span style="font-size: 90%;">we MUST decide</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:26 UTC</span>

<span style="font-size: 90%;">well, that’s an easy one</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:38 UTC</span>

<span style="font-size: 90%;">CRS Incubator - Everything is an incubator these days
		CRS Playground - this implies we play with the rules
		CRS Sandbox -
		CRS Testing - This sounds as if it would be more about
			testing the rule set than about new rules
		CRS Experimental - old school title, but a bit intimidating
			when you think about production setups</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:18:38 UTC</span>

<span style="font-size: 90%;">incubator?</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:49 UTC</span>

<span style="font-size: 90%;">these ones are suggested, I think incubator is fine honestly</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:08 UTC</span>

<span style="font-size: 90%;">playground is also not so bad and really playful</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:08 UTC</span>

<span style="font-size: 90%;">sandbox has so much meanings in infosec, and it would cause confusion</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:19:21 UTC</span>

<span style="font-size: 90%;">Yes, I first liked kindergarten most, but incubator fits better I think.</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:48 UTC</span>

<span style="font-size: 90%;">any one else? this is an easy contribution to make :smile:</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:20:00 UTC</span>

<span style="font-size: 90%;">give me a sec</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:03 UTC</span>

<span style="font-size: 90%;">Do we want to add thums up?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:07 UTC</span>

<span style="font-size: 90%;">Incubator</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:11 UTC</span>

<span style="font-size: 90%;">Playground</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:14 UTC</span>

<span style="font-size: 90%;">Sandbox</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:15 UTC</span>

<span style="font-size: 90%;">Testing</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:18 UTC</span>

<span style="font-size: 90%;">Experimental</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:20:26 UTC</span>

<span style="font-size: 90%;">kindergarten</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:53 UTC</span>

<span style="font-size: 90%;">looks like a landslide but we’ll wait another few seconds….</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:21:00 UTC</span>

<span style="font-size: 90%;">I just miss the word basic or something</span>

**Emile** <span style="color: grey; font-size: 90%;">20:21:10 UTC</span>

<span style="font-size: 90%;">(:wave: sorry, couldn’t make it for the meeting :grimacing:)</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:21:47 UTC</span>

<span style="font-size: 90%;">because it's a very limited basic rule set. so it would be more clear. but incubator would be okay for me</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:26 UTC</span>

<span style="font-size: 90%;">no this won’t be the basic rule set (PL0) that’s been proposed, if I understand you correctly</span>

**walter** <span style="color: grey; font-size: 90%;">20:22:52 UTC</span>

<span style="font-size: 90%;">it would be a playbox for new experimental rules</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:23:02 UTC</span>

<span style="font-size: 90%;">ah ok</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:16 UTC</span>

<span style="font-size: 90%;">so we can get real world input on their performance and false-positive rates</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:22 UTC</span>

<span style="font-size: 90%;">without blocking</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:23:31 UTC</span>

<span style="font-size: 90%;">then incubator would be perfect</span>

**walter** <span style="color: grey; font-size: 90%;">20:23:34 UTC</span>

<span style="font-size: 90%;">and rules would then ‘graduate’ to the core rule set on next release</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:23:39 UTC</span>

<span style="font-size: 90%;">:grin:</span>

**airween** <span style="color: grey; font-size: 90%;">20:23:52 UTC</span>

<span style="font-size: 90%;">it would be a playbox for new experimental rules - playbox is new, and that's the best :smile:</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:23 UTC</span>

<span style="font-size: 90%;">ok I’ll add it for thumbs:
playbox</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:24:32 UTC</span>

<span style="font-size: 90%;">playbox sounds really cool heheh</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:46 UTC</span>

<span style="font-size: 90%;">thumb it up!</span>

**walter** <span style="color: grey; font-size: 90%;">20:24:52 UTC</span>

<span style="font-size: 90%;">my thumb stays at incubator :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:21 UTC</span>

<span style="font-size: 90%;">voting ends at 22:25:00.000</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:25:28 UTC</span>

<span style="font-size: 90%;">:wink:</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:40 UTC</span>

<span style="font-size: 90%;">okay e-voting ended!</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:43 UTC</span>

<span style="font-size: 90%;">it’s gonna be incubator :stuck_out_tongue:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:26:04 UTC</span>

<span style="font-size: 90%;">:tada:</span>

**walter** <span style="color: grey; font-size: 90%;">20:26:14 UTC</span>

<span style="font-size: 90%;">please read the gist for your further comments and we’ll come back to it soon</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:43 UTC</span>

<span style="font-size: 90%;"></span>

**airween** <span style="color: grey; font-size: 90%;">20:27:50 UTC</span>

<span style="font-size: 90%;">(a quick off-topic side-note: Python 3.9 is out there:
[https://www.python.org/downloads/release/python-390/](https://www.python.org/downloads/release/python-390/))</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:51 UTC</span>

<span style="font-size: 90%;">it was problematic all afternoon for us</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:14 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">20:30:00 UTC</span>

<span style="font-size: 90%;">Maybe you have some infos to share _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">20:31:50 UTC</span>

<span style="font-size: 90%;">for CVE?</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:24 UTC</span>

<span style="font-size: 90%;">it's still in reserved state:
[https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15598)</span>

**airween** <span style="color: grey; font-size: 90%;">20:32:52 UTC</span>

<span style="font-size: 90%;">(and Spotify - don't know is there any connection between them)</span>

**airween** <span style="color: grey; font-size: 90%;">20:34:09 UTC</span>

<span style="font-size: 90%;">nothing new at there, we're still waiting to publish the CVE</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:34:27 UTC</span>

<span style="font-size: 90%;">[https://status.slack.com/2020-10/e8c094cc99aabf64](https://status.slack.com/2020-10/e8c094cc99aabf64)</span>

**walter** <span style="color: grey; font-size: 90%;">20:37:36 UTC</span>

<span style="font-size: 90%;">I guess we’ll have to close the meeting due to Slack downtime… Thank you all for contributing, and we’ll necessarily move the remaining items to next meeting… We’ll have an issues meeting 2 weeks from now where we talk about incoming issues. That meeting has not been so popular yet, but you are all invited to come and discuss / assign some of the issues!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:38:12 UTC</span>

<span style="font-size: 90%;">good night/day</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:38:13 UTC</span>

<span style="font-size: 90%;">I'm back, sorry.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:38:21 UTC</span>

<span style="font-size: 90%;">I'm back</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:38:33 UTC</span>

<span style="font-size: 90%;">but i'm havin some troubles with slack.</span>

**walter** <span style="color: grey; font-size: 90%;">20:39:01 UTC</span>

<span style="font-size: 90%;">yeah slack is troublesome, I’ve been trying to send messages for 10 minutes. let’s call it a day and see you hopefully in 2 weeks, otherwise next month!</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:41:10 UTC</span>

<span style="font-size: 90%;">me too, loaded new messages just now</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:39:04 UTC</span>

<span style="font-size: 90%;">Good night everybody.
Thank you _@walter_ for leading the meeting</span>

**airween** <span style="color: grey; font-size: 90%;">20:39:10 UTC</span>

<span style="font-size: 90%;">good night!</span>

**nerrehmit** <span style="color: grey; font-size: 90%;">20:39:19 UTC</span>

<span style="font-size: 90%;">bye bye</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:39:21 UTC</span>

<span style="font-size: 90%;">good night</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:39:25 UTC</span>

<span style="font-size: 90%;">See you! Good progress today!</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:39:48 UTC</span>

<span style="font-size: 90%;">is anyone staying?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:50 UTC</span>

<span style="font-size: 90%;">You're about to say good-bye? Just got back from the Cinema!</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:39:57 UTC</span>

<span style="font-size: 90%;">i'm still here</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:09 UTC</span>

<span style="font-size: 90%;">Hey _@azurIt_. How did it go?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:40:20 UTC</span>

<span style="font-size: 90%;">How was the movie?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:40:29 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/1892#issuecomment-703832606](https://github.com/coreruleset/coreruleset/issues/1892#issuecomment-703832606)</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:40:44 UTC</span>

<span style="font-size: 90%;">Quite well until slack does down. :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:40:46 UTC</span>

<span style="font-size: 90%;">I'm going to bed now...
Good night. Slack seems to have problems....</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:41:01 UTC</span>

<span style="font-size: 90%;">*goes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:05 UTC</span>

<span style="font-size: 90%;">Suprisingly good movie (-> "Eden für Jeden")</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:41:10 UTC</span>

<span style="font-size: 90%;">me too, loaded new messages just now</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:41:10 UTC</span>

<span style="font-size: 90%;">me too, loaded new messages just now</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:17 UTC</span>

<span style="font-size: 90%;">Too bad with slack.</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:41:31 UTC</span>

<span style="font-size: 90%;">back to IRC? :D</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:41:22 UTC</span>

<span style="font-size: 90%;">good night</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:31 UTC</span>

<span style="font-size: 90%;">Good night!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:41:31 UTC</span>

<span style="font-size: 90%;">back to IRC? :D</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">20:41:31 UTC</span>

<span style="font-size: 90%;">back to IRC? :D</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:41:52 UTC</span>

<span style="font-size: 90%;">_@dune73_ if you are staying for a while, can you help me with github a little?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:42:36 UTC</span>

<span style="font-size: 90%;">Shall I send you Walter's manual I always use?</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:42:45 UTC</span>

<span style="font-size: 90%;">Sure.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:43:19 UTC</span>

<span style="font-size: 90%;">Is it possible to send it via Slack?</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:43:33 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ can you send it to me too?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:43:36 UTC</span>

<span style="font-size: 90%;">I hope so...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:43:42 UTC</span>

<span style="font-size: 90%;">I'll try...</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:43:44 UTC</span>

<span style="font-size: 90%;">via mail?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:43 UTC</span>

<span style="font-size: 90%;">_@azurIt_: No, on my way to the bed, but I might have time tomorrow. Sorry.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:45:02 UTC</span>

<span style="font-size: 90%;">_@dune73_ no problem, thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:45:43 UTC</span>

<span style="font-size: 90%;">Check out:
git clone [https://github.com/user/coreruleset.git](https://github.com/user/coreruleset.git)
cd coreruleset
git remote add upstream [https://github.com/coreruleset/coreruleset](https://github.com/coreruleset/coreruleset)
git fetch upstream
git checkout v3.4/dev
git merge upstream/v3.4/dev (merge changes from upstream to local branch)
git push

git config --global user.name <user>
git config --global user.email "[<user>@gmail.com](mailto:user@gmail.com)"

New branch:
git checkout -b fix-fp-123
git push --set-upstream origin fix-fp-123

git add ...
git commit

Step Push your local changes to your fork at Github
git push

Pull request</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:51:20 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ Not sure if it all gets through.</span>

**azurIt** <span style="color: grey; font-size: 90%;">20:52:33 UTC</span>

<span style="font-size: 90%;">Maybe it will be better to use the email.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:56:45 UTC</span>

<span style="font-size: 90%;">We should add that info to the CONTRIBUTING.md maybe?</span>

