### Mon, Jun 2nd, 2025

**airween** <span style="color: grey; font-size: 90%;">18:31:07 UTC</span>

<span style="font-size: 90%;">aaaaand... good evening!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:31:12 UTC</span>

<span style="font-size: 90%;">Hello hello</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:31:24 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly chat. Let's see who made it</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">18:31:48 UTC</span>

<span style="font-size: 90%;">Hello</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:50 UTC</span>

<span style="font-size: 90%;">Evening</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">18:32:21 UTC</span>

<span style="font-size: 90%;">Hi! :slightly_smiling_face: </span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:01 UTC</span>

<span style="font-size: 90%;">Hello everybody!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:11 UTC</span>

<span style="font-size: 90%;">Very nice. Felipe just boarded the plane, so he'll probably be absent tonight.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:04 UTC</span>

<span style="font-size: 90%;">Well, first things first: congratulations to _@dune73_ once more for the OWASP Distinguished Lifetime Member Award! The recognition is fully deserved.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:35 UTC</span>

<span style="font-size: 90%;">Thank you very much _@maxleske_. It's a pity you all missed the party.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:53 UTC</span>

<span style="font-size: 90%;">Did you wear the helmet?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:26 UTC</span>

<span style="font-size: 90%;">No, but the prize (=trophy) is so heavy, it would qualify as a medieval mace.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:47 UTC</span>

<span style="font-size: 90%;">(price = trophy)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:51 UTC</span>

<span style="font-size: 90%;">Here is a photo in case you were wondering what you missed at the party.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:41 UTC</span>

<span style="font-size: 90%;">Well, looks like you got around a "medieval restaurant" this time :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:37 UTC</span>

<span style="font-size: 90%;">Very few medieval restaurants in Barçelona. So the coast was clear.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:39 UTC</span>

<span style="font-size: 90%;">I had posted the link to the agenda above. Please take a couple of minutes to read through it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:41 UTC</span>

<span style="font-size: 90%;">_@airween_ could you give us a quick update on ModSecurity versions and CVE's?</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">18:40:42 UTC</span>

<span style="font-size: 90%;">Hello :slightly_smiling_face:</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">18:40:51 UTC</span>

<span style="font-size: 90%;">I will join your party in 10 mins xD</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:51 UTC</span>

<span style="font-size: 90%;">Hi _@Muhamed Ayman_</span>

**airween** <span style="color: grey; font-size: 90%;">18:42:23 UTC</span>

<span style="font-size: 90%;">while I made the patches for stable and old-stable Debian, I realized that there is one more action which affected by the same bug as was the previous one. We chatted the solution is easy, but the last week was very busy, so I released the new version with that fix today.</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:09 UTC</span>

<span style="font-size: 90%;">even though the score is high (7.5) if someone uses only CRS, they do not affected (there is no `sanitizeArgs` action)</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:27 UTC</span>

<span style="font-size: 90%;">the new stable version is 2.9.10</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:41 UTC</span>

<span style="font-size: 90%;">that's it :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:30 UTC</span>

<span style="font-size: 90%;">Thanks. 2.9.10 hasn't been released yet as a container image but will be soon.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:44:31 UTC</span>

<span style="font-size: 90%;">Who "opened" the CVE? ModSecurity itself?</span>

**airween** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:53 UTC</span>

<span style="font-size: 90%;">So this 2.9 release fixes a variant of the original bug that forced the previous release two weeks ago?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:18 UTC</span>

<span style="font-size: 90%;">But the issue was reported to the project.</span>

**airween** <span style="color: grey; font-size: 90%;">18:45:22 UTC</span>

<span style="font-size: 90%;">Felipe noticed me that GH helps in handling of CVE's. Just opened a security advisory, there I can ask a CVE number.</span>

**airween** <span style="color: grey; font-size: 90%;">18:45:46 UTC</span>

<span style="font-size: 90%;"> So this 2.9 release fixes a variant of the original bug that forced the previous release two weeks ago?yes, we can say this is a variant</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:09 UTC</span>

<span style="font-size: 90%;">Here is the published security advisory:
[https://github.com/owasp-modsecurity/ModSecurity/security/advisories/GHSA-f82j-8pp7-cw2w](https://github.com/owasp-modsecurity/ModSecurity/security/advisories/GHSA-f82j-8pp7-cw2w)</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:31 UTC</span>

<span style="font-size: 90%;">I mentioned the other one (what _@dune73_ asked above)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:33 UTC</span>

<span style="font-size: 90%;">We only have one issue to talk about today, so _@dune73_, maybe you would like to give us a short summary of the WAF day in Barcelona?</span>

**airween** <span style="color: grey; font-size: 90%;">18:47:34 UTC</span>

<span style="font-size: 90%;">and thanks again for your help _@maxleske_ and _@fzipitria_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:29 UTC</span>

<span style="font-size: 90%;">Hmm.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:34 UTC</span>

<span style="font-size: 90%;">OK.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:52 UTC</span>

<span style="font-size: 90%;">So we had only a small num of people in the room, 12 or so.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:30 UTC</span>

<span style="font-size: 90%;">The usual suspects plus A. Schaff from Thales (15 years of experience or so), plus two Crowdstrike engineers and Ivan Novikov, CEO of Wallarm.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:04 UTC</span>

<span style="font-size: 90%;">Schaff presented their inhouse ModSec solution, many clues of how they operate it, but Thales is fairly strict with contributing back, so this is a bit of a black hole.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:58 UTC</span>

<span style="font-size: 90%;">CrowdStrike built a new solution that integrates CRS with their IP blacklisting capabilities. They way I got it, they force you to run their container to get all the benefits. But interesting conversations.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:52 UTC</span>

<span style="font-size: 90%;">JP presented the an overview of Coraza operating best practices, nothing overly surprising from a CRS perspective.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:34 UTC</span>

<span style="font-size: 90%;">Souyanja Namburi who works with JP presented a very technical talk that aims to optimize Regex processing. I am not sure I understood it correctly, but it's about preprocessing the payloads before they are fed into the regex engine for better performance. It's like you cover the evasions in a separate module and then run a simplified regex. She claims big performance wins.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">19:02:49 UTC</span>

<span style="font-size: 90%;">Perhaps unicode normalization, removing embedded nulls, normalizing full-width latin characters back to ascii, lowercasing/uppercasing everything? I'd love to watch the talk if there's a recording somewhere.</span>

↳ **dune73** <span style="color: grey; font-size: 90%;">19:17:34 UTC</span>

<span style="font-size: 90%;">Unfortunately, it has not been recorded, but I am sure she is open to explain it to you. She's on slack.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:46 UTC</span>

<span style="font-size: 90%;">Felipe gave a status overview of the SecLang.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:47 UTC</span>

<span style="font-size: 90%;">And I presented my Chaos Fortress plugin. Nothing new, but 6 months of positive experience on [netnea.com](http://netnea.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:08 UTC</span>

<span style="font-size: 90%;">Did I say Crowdstrike? I meant CrowdSec. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:35 UTC</span>

<span style="font-size: 90%;">I think that's it mostly.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:39 UTC</span>

<span style="font-size: 90%;">We'll get the slides.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:47 UTC</span>

<span style="font-size: 90%;">As always, the discussions were the best.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:17 UTC</span>

<span style="font-size: 90%;">It's a pity we can not attract more people to these meetings. More advanced planning / marketing could help. But it is relatively clear that the OWASP conference crowd is not overly interested in WAF right now. Also visible with the ModSec & CRS / Coraza presentations during the regular conference.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:36 UTC</span>

<span style="font-size: 90%;">There, Ervin talked about the past year of ModSec development and his plans.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:10 UTC</span>

<span style="font-size: 90%;">Participation is better than one would think from the outside, but it's definitely too much on the plate for him alone as lead developer.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:29 UTC</span>

<span style="font-size: 90%;">_@airween_ did I forget anything?</span>

**airween** <span style="color: grey; font-size: 90%;">19:00:55 UTC</span>

<span style="font-size: 90%;">I also had a presentation on WAF day about ModSec testing - I'll send the slides too</span>

**airween** <span style="color: grey; font-size: 90%;">19:01:37 UTC</span>

<span style="font-size: 90%;">And let me tell you a short story.

I was just leaving the venue (on 1st conference day) when a guy stopped in front of me and said he had attended my presentation. He hadn't used ModSecurity recently (due to his new job), but he used to use it a lot. And he still follows the project. He said he enjoyed the presentation and was very happy that the project is alive and under serious maintenance :).

I think it's worth working for these moments...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:41 UTC</span>

<span style="font-size: 90%;">Ah yes, all these talks are a bit puzzling in my head.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:35 UTC</span>

<span style="font-size: 90%;">Thanks very much guys.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:05 UTC</span>

<span style="font-size: 90%;">Before we get to the item on the agenda, I have one more question: has anyone ever heard of Myra WAF? Apparently, they use CRS in their product. The apparently serve large customers, such as banks and sell them the complete security works.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:36 UTC</span>

<span style="font-size: 90%;">[https://www.myrasecurity.com](https://www.myrasecurity.com)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:45 UTC</span>

<span style="font-size: 90%;">I thought they were only a DDoS company.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:06:02 UTC</span>

<span style="font-size: 90%;">We were contacted by someone working for a German bank, that's how I know.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:18 UTC</span>

<span style="font-size: 90%;">[https://www.myrasecurity.com/assets/79302/1715088801-myra_security_waf_en.pdf](https://www.myrasecurity.com/assets/79302/1715088801-myra_security_waf_en.pdf) covers the product, but they do not mention CRS nor ModSec.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:29 UTC</span>

<span style="font-size: 90%;">Maybe somebody should book a demo. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:02 UTC</span>

<span style="font-size: 90%;">Ok. Well, I just wanted to put it out there.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:46 UTC</span>

<span style="font-size: 90%;">Let's finally get to that one item on the agenda. _@franbuehler_, maybe you're best suited to explain?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:09:37 UTC</span>

<span style="font-size: 90%;">Yes, we received a PR [https://github.com/coreruleset/coreruleset/pull/4145](https://github.com/coreruleset/coreruleset/pull/4145) (thank you _@Muhamed Ayman_, btw. it's a good PR it also has tests).
It's very similar to an existing rule 941380 and we were not sure if we should delete this existing rule 941380 and work on the new rule.
As I'm writing now, I think we can also keep the old rule 941380 and work on a new rule that detects more template injection.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:10:08 UTC</span>

<span style="font-size: 90%;">It was very similar, the regex of the new rule is still growing :wink: and it's not so similar anymore.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:10:28 UTC</span>

<span style="font-size: 90%;">Do we want to delete the old rule 941380 or do we keep both rules (the old and the new one)?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:13 UTC</span>

<span style="font-size: 90%;">What are the argument against including all of _@Muhamed Ayman_'s additional patterns in 941380?</span>

↳ **Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:16:22 UTC</span>

<span style="font-size: 90%;">Sorry, I didn't get your question as folks are reacting in question marks xD
So what do you mean exactly?</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:11:31 UTC</span>

<span style="font-size: 90%;">{%%} and <%[=]?%></span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:12:02 UTC</span>

<span style="font-size: 90%;">I hope you got you correctly xD</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:12:03 UTC</span>

<span style="font-size: 90%;">I think the placement of the rule 941 (xss) or 934 (attacks-generic).
But yes, we could extend 941380.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:42 UTC</span>

<span style="font-size: 90%;">That's a point.</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:12:57 UTC</span>

<span style="font-size: 90%;">I'd rather extend 941380 instead of creating a new rule, existing users won't have to retune their installation in that case.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:14 UTC</span>

<span style="font-size: 90%;">Yes, that was also my argument, the existing tuning rules...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:13:24 UTC</span>

<span style="font-size: 90%;">I don't think we ever "moved" a rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:41 UTC</span>

<span style="font-size: 90%;">But we could also kick 941380 in favor of a new 934 rules. But this would cause new FPs unless users adjust their rule exclusions for 941380.</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:13:54 UTC</span>

<span style="font-size: 90%;">As I have mentioned in any open source code, you as a user need to check what upgrade/updates have been taken.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:14:53 UTC</span>

<span style="font-size: 90%;">While that is true, CRS is generally harder to update than other things, because of tuning. So we at least try to minimise such changes, where possible.</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:15:32 UTC</span>

<span style="font-size: 90%;">Especially higher paranoia levels can be hard to work with, I'd rather not add any more needless pain.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">v4 is still not LTS and is a moving target with each release. It should be okay to move a rule, if there is a good reason to, I think</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">I mean, if there is an announcement could be mentioned in the new release for that change, it will be good as far as I know</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:14:22 UTC</span>

<span style="font-size: 90%;">One argument for keeping 941380: it's my rule. But it's not a very strong argument I guess :wink:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:53 UTC</span>

<span style="font-size: 90%;">While that is true, CRS is generally harder to update than other things, because of tuning. So we at least try to minimise such changes, where possible.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:14:53 UTC</span>

<span style="font-size: 90%;">While that is true, CRS is generally harder to update than other things, because of tuning. So we at least try to minimise such changes, where possible.</span>

↳ **Esad Cetiner** <span style="color: grey; font-size: 90%;">19:15:32 UTC</span>

<span style="font-size: 90%;">Especially higher paranoia levels can be hard to work with, I'd rather not add any more needless pain.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:01 UTC</span>

<span style="font-size: 90%;">The problem is, we do not have an LTS. Since releasing CRS 4.0, I do not think we had real breaking change. So 4.0 - 4.14 or so is easy and then suddenly a hiccup.</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:16:22 UTC</span>

<span style="font-size: 90%;">I think I prefer the idea of smoother update experiences for users.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:42 UTC</span>

<span style="font-size: 90%;">We've never been totally strict with the rule categorization. But if a rule becomes 80% generic, then it probably should not reside with the XSS. I think it's a tough call and it's very hard to know the percentages in terms of traffic or attack numbers.</span>

**Michela Toscano** <span style="color: grey; font-size: 90%;">19:17:22 UTC</span>

<span style="font-size: 90%;">Even if it is the user / administrator's "fault" (they didn't check the release notes or test before upgrading), it's still not a good experience for something to be broken, particularly if we could have helped them avoid it.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:18:01 UTC</span>

<span style="font-size: 90%;">We could add to the release notes something like: extend and move rule 941380 to rule 934xxx</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:13 UTC</span>

<span style="font-size: 90%;">Personally, I'm against mixing different things in the same rule. There are two distinct syntaxes `{{...}}` and `{%...%}` and probably different pitfalls with both. Also, mixing makes maintenance harder because you have to very carefully document what actually is being tested by the rule. Additionally, it wouldn't be possible to turn one or the other off, only both at the same time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:19 UTC</span>

<span style="font-size: 90%;">Yes, sure, that's the least we can do. But it's still annoying.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:51 UTC</span>

<span style="font-size: 90%;">Ah, "the turn one or the other off" is an additional argument. Thanks.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:19:15 UTC</span>

<span style="font-size: 90%;">So, we would keep {{...}} in 941380 and write a new rule 934 for the other patterns?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:00 UTC</span>

<span style="font-size: 90%;">I would differentiate. If Jinja2, for example, is very close to Angular, then we could put that into the existing rule. And add a new rule for the Python stuff.</span>

↳ **jit** <span style="color: grey; font-size: 90%;">19:21:15 UTC</span>

<span style="font-size: 90%;">The syntaxes mentioned above are both Jinja2 related.</span>

↳ **Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:21:39 UTC</span>

<span style="font-size: 90%;">_@jit_ exactly!</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:22:11 UTC</span>

<span style="font-size: 90%;">Ok, didn't know that.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:22 UTC</span>

<span style="font-size: 90%;">_@Esad Cetiner_ Could you elaborate what you meant with "paranoia levels... can be painful"?</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:21:55 UTC</span>

<span style="font-size: 90%;">I just meant that higher paranoia levels are especially hard to work with, and I'd rather not add any extra workload</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:22:23 UTC</span>

<span style="font-size: 90%;">But splitting the new detections in a different rule is something I'd be in favor of, as long as the old rule isn't being removed.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:28 UTC</span>

<span style="font-size: 90%;">Are there any additional arguments one way or the other?</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:22:59 UTC</span>

<span style="font-size: 90%;">Can you clarify what is exactly mean by arguments? xD becuase I think I got you wrong at the first glance xD</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:23:32 UTC</span>

<span style="font-size: 90%;">I am little bit confused, do you mean thoughts? critism?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:23:47 UTC</span>

<span style="font-size: 90%;">As _@jit_ has pointed out, Jinja2 uses _both_ syntaxes, so my idea wouldn't work that well. But that fact makes me think even more that we should have a dedicated rule.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:31 UTC</span>

<span style="font-size: 90%;">Argument as "pro / contra argument in a discussion".</span>

↳ **Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:25:26 UTC</span>

<span style="font-size: 90%;">Good to know, thanks!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:25:19 UTC</span>

<span style="font-size: 90%;">I don't think we have other arguments.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:25:57 UTC</span>

<span style="font-size: 90%;">Maybe add comments to both rules that indicate the other rule. That could help in the future.</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:26:05 UTC</span>

<span style="font-size: 90%;">In the PR, I have mentioned also that there is no need for the **removeWhiteSpaces** filter</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:26:25 UTC</span>

<span style="font-size: 90%;">Ok, good to know.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:38:34 UTC</span>

<span style="font-size: 90%;">I will review your PR once it's ready. It's really good work, thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:26:25 UTC</span>

<span style="font-size: 90%;">Ok, good to know.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:26:25 UTC</span>

<span style="font-size: 90%;">Ok, good to know.</span>

↳ **franbuehler** <span style="color: grey; font-size: 90%;">19:38:34 UTC</span>

<span style="font-size: 90%;">I will review your PR once it's ready. It's really good work, thank you!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:27:05 UTC</span>

<span style="font-size: 90%;">So what I hear now is: keep both rules, add comments and also add comment about the other rule living in the other rules-file.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:34 UTC</span>

<span style="font-size: 90%;">I do not really have strong opinions one way or the other. It all has its pros and cons.</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:28:29 UTC</span>

<span style="font-size: 90%;">All options are available on the table from my side, if you want me to keep the following regex in the new rule: {%%}|<%[=]?%>, and add some comments.
I am fine</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:28:57 UTC</span>

<span style="font-size: 90%;">Sounds good to me. Thanks for your input everyone.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:29:10 UTC</span>

<span style="font-size: 90%;">This sound good to me too. Thank you for your inputs.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:28 UTC</span>

<span style="font-size: 90%;">Good discussion.</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:29:39 UTC</span>

<span style="font-size: 90%;">Thank you everyone, I really appreciate you thoughts.
I will update the PR in a couple of minutes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:05 UTC</span>

<span style="font-size: 90%;">Thanks _@Muhamed Ayman_ for your work!</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:30:37 UTC</span>

<span style="font-size: 90%;">I am so sorry for my poor composition skills, may be I am anxious as it is my first time to engage in such talks xD
P.S.
It is also my first time ever to contribute to open source community, so just bear with me please xD</span>

**dune73** <span style="color: grey; font-size: 90%;">19:31:10 UTC</span>

<span style="font-size: 90%;">You are doing very well Muhamed and we are very happy how you keep up!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:14 UTC</span>

<span style="font-size: 90%;">Don't worry, you're doing fine. Actually, more than fine, I would say :slightly_smiling_face:</span>

**Muhamed Ayman** <span style="color: grey; font-size: 90%;">19:31:29 UTC</span>

<span style="font-size: 90%;">Lovely, thanks! :heart:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:31 UTC</span>

<span style="font-size: 90%;">With that, we're at the end of our meeting. Does anyone have something to add? Something else to discuss?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:04 UTC</span>

<span style="font-size: 90%;">What are the plans with the dev summit?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:43 UTC</span>

<span style="font-size: 90%;">No plans yet. I'll talk to Felipe this week (probably), then we might know more.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:33:02 UTC</span>

<span style="font-size: 90%;">The next "CRS Community Call" was tentatively scheduled for this month. Is that plan on ice for now?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:47 UTC</span>

<span style="font-size: 90%;">As the moderator, I was wondering that too. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:52 UTC</span>

<span style="font-size: 90%;">Ah yes, thanks for the reminder. _@dune73_ we should talk about that. I'll ping you this week some time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:43 UTC</span>

<span style="font-size: 90%;">Sounds good.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:04 UTC</span>

<span style="font-size: 90%;">I think you should set a date for the dev summit soon. Then look for a place to host it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:26 UTC</span>

<span style="font-size: 90%;">FYI: Chances are, I can't attend this year. I have a new contract that is likely to climax in November.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:56 UTC</span>

<span style="font-size: 90%;">Seriously climaxing with gov and media attention.</span>

**airween** <span style="color: grey; font-size: 90%;">19:36:02 UTC</span>

<span style="font-size: 90%;">I can't attend this year.are you joking, right?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:27 UTC</span>

<span style="font-size: 90%;">I'm not joking, but the schedule is not in my hand on that front.</span>

**Dan Kegel** <span style="color: grey; font-size: 90%;">19:36:32 UTC</span>

<span style="font-size: 90%;">I have a wee question... what about [https://github.com/coreruleset/coreruleset/issues/3383](https://github.com/coreruleset/coreruleset/issues/3383) ?  Seems like a good source of false negatives...?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:46 UTC</span>

<span style="font-size: 90%;">Chances are everything is postponed, but the current trajectory tells me I'll be under water in November.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:38 UTC</span>

<span style="font-size: 90%;">_@Dan Kegel_ I do not think anybody picked this up as a task. So it's up for grabs - and lots of merits to be won.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:07 UTC</span>

<span style="font-size: 90%;">One of many "nice to have" things in our backlog...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:27 UTC</span>

<span style="font-size: 90%;">I guess that's all then. Have a nice evening / morning / day everyone, and thanks for joining.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:42 UTC</span>

<span style="font-size: 90%;">Thank you everybody!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:38:55 UTC</span>

<span style="font-size: 90%;">Thank you everybody and good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:39:02 UTC</span>

<span style="font-size: 90%;">Cheerio!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:15 UTC</span>

<span style="font-size: 90%;">(I should come up with some kind of end slogan: "Go forth and make the net a safer place", or something)</span>

**Esad Cetiner** <span style="color: grey; font-size: 90%;">19:39:19 UTC</span>

<span style="font-size: 90%;">Bye :blob-wave:</span>

**airween** <span style="color: grey; font-size: 90%;">19:39:25 UTC</span>

<span style="font-size: 90%;">good night!</span>

