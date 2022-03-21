### Mon, Aug 2nd, 2021

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:31:03 UTC</span>

<span style="font-size: 90%;">Good evening. I'm keeping half an eye on chat via phone while looking after my daughter</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:31:49 UTC</span>

<span style="font-size: 90%;">hello everybody</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:53 UTC</span>

<span style="font-size: 90%;">hi</span>

**airween** <span style="color: grey; font-size: 90%;">18:34:01 UTC</span>

<span style="font-size: 90%;">hi all</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:34:57 UTC</span>

<span style="font-size: 90%;">Hi!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:37:59 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:04 UTC</span>

<span style="font-size: 90%;">Hi there, my wife lost a contact lens inside her eye. That's rather painful. Please start without me.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:51 UTC</span>

<span style="font-size: 90%;">okay, I guess we will start by working down the agenda: [https://github.com/coreruleset/coreruleset/issues/2169](https://github.com/coreruleset/coreruleset/issues/2169)</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:14 UTC</span>

<span style="font-size: 90%;">as for the sponsor developments, they are coming along quite nicely!</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:51 UTC</span>

<span style="font-size: 90%;">Christian knows more about this so we’ll leave detailed discussion for later I guess :)</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">let’s go to the Open PRs…</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:46 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/2168](https://github.com/coreruleset/coreruleset/pull/2168) in need of a quick review, maybe [@airween ](https://github.com/airween)</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:09 UTC</span>

<span style="font-size: 90%;">what do you think _@airween_? it looks like a small issue</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:13 UTC</span>

<span style="font-size: 90%;">yes, I'll check this, I'm going to assign it to myself.</span>

**airween** <span style="color: grey; font-size: 90%;">18:46:37 UTC</span>

<span style="font-size: 90%;">oh, it's already assigned to _@fzipitria_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:51 UTC</span>

<span style="font-size: 90%;">Sorry, was on calls :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:56 UTC</span>

<span style="font-size: 90%;">[I'm back. Lens retrieved. Mission accomplished. Apologies from my panicking wife.]</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:51 UTC</span>

<span style="font-size: 90%;">Nothing more to add with regards to sponsoring. It's coming along nicely, but it's apparently a lot of work.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:23 UTC</span>

<span style="font-size: 90%;">@Walter do you want to continue with hosting the meeting? I do not mind - or I can take over. You decide.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:47 UTC</span>

<span style="font-size: 90%;">if you could take over that would be my preference :slightly_smiling_face: I’m not as up to date as I’ve had a crunch month at work with 7 day work weeks, so I haven’t kept track very  well</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:56 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:50:10 UTC</span>

<span style="font-size: 90%;">Fine. (well not the 7 day work weeks).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:10 UTC</span>

<span style="font-size: 90%;">So 2168 is in good hands. I was just calling on _@airween_ to take a glance because he told us the remaining failing tests on NGINX were due to engine bugs and this looks like a bug in the tests and ModSecv3 being less forgiving (or whatever).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:18 UTC</span>

<span style="font-size: 90%;">Guess we can move on.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:21 UTC</span>

<span style="font-size: 90%;">next one is [https://github.com/coreruleset/coreruleset/pull/2163](https://github.com/coreruleset/coreruleset/pull/2163)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:25 UTC</span>

<span style="font-size: 90%;">2163 is a renaming PR. We used to name the 934 group after NodeJS, but now it looks like there will be very few NodeJS rules and we have a need for a generic application attack rule group.</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:33 UTC</span>

<span style="font-size: 90%;">sounds fair to me</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:10 UTC</span>

<span style="font-size: 90%;">Unfortunately, the PR fails on FTW, probably due to the renaming. theMiddle seems a bit lost. Could somebody with an ftw background take a look at this?</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:47 UTC</span>

<span style="font-size: 90%;">_@fzipitria_maybe?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:53 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:10 UTC</span>

<span style="font-size: 90%;">maybe the filenames are hardcoded somewhere?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:18 UTC</span>

<span style="font-size: 90%;">Thanks. Feel free to merge as soon as the tests pass. The PR looks good to me.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:24 UTC</span>

<span style="font-size: 90%;">hardcoded: Maybe, yes.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:43 UTC</span>

<span style="font-size: 90%;">2156 is a ctl cleanup PR. Maybe more to come.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:08 UTC</span>

<span style="font-size: 90%;">hi</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:15 UTC</span>

<span style="font-size: 90%;">2156 makes sense to me</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:16 UTC</span>

<span style="font-size: 90%;">ctl:ruleEngine off is a bit radical, removeByTag:OWASP_CRS seems more compatible with other rule sets. What do you think?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:37 UTC</span>

<span style="font-size: 90%;">Hello _@maxleske_! Great to see you. Wondered if you would show up.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:57:45 UTC</span>

<span style="font-size: 90%;">I think it makes sense. I never liked just turning off.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:47 UTC</span>

<span style="font-size: 90%;">I do not see anybody disagreeing. So I guess this is good to go.
_@azurIt_ also wonders what to do with other CRS specific stuff. Like variables / SecMarkers not named after CRS. Personally, I do not see this as a problem. We're known enough and the variables / SecMarkers carry very uncommon names.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:09 UTC</span>

<span style="font-size: 90%;">Merge right away, or somebody does a review?</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:21 UTC</span>

<span style="font-size: 90%;">I think it can be merged!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:49 UTC</span>

<span style="font-size: 90%;">Cool. Then please go about it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:57 UTC</span>

<span style="font-size: 90%;">done</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:28 UTC</span>

<span style="font-size: 90%;">2052 adds more teeth to an existing rules. Possibly also more FPs. We need a proper review.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:59:39 UTC</span>

<span style="font-size: 90%;">It's maybe also a candidate for the incubator to test the water.</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:01 UTC</span>

<span style="font-size: 90%;">I could test it out on live traffic for a few weeks</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:27 UTC</span>

<span style="font-size: 90%;">at first sight it doesn’t seem too dangerous…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:43 UTC</span>

<span style="font-size: 90%;">I agree. So would you do the review?</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:55 UTC</span>

<span style="font-size: 90%;">sure, I just check for FP’s, and then merge it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:23 UTC</span>

<span style="font-size: 90%;">Yes, I think that's all what's needed. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:50 UTC</span>

<span style="font-size: 90%;">[#2149](https://github.com/coreruleset/coreruleset/issues/#2149) is a very welcome cleanup of our regex assembly by _@maxleske_.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:25 UTC</span>

<span style="font-size: 90%;">I took a close look at the documentation and file format. But now we need a review or more bluntly: Somebody generating all the regexes anew and comparing the output.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:03:43 UTC</span>

<span style="font-size: 90%;">I could do this</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:44 UTC</span>

<span style="font-size: 90%;">FYI: For 3.3 or so we failed to get the regex assembly script to do a specific thing, so we duplicated the behaviour into a 2nd script with a subtle difference. But it was obviously a hack. Max has now merged the two and adds more flexibility to the way we use the script and the source files (-> Adding possibilities for empty lines and comments!)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:55 UTC</span>

<span style="font-size: 90%;">Thank you _@franbuehler_!</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:21 UTC</span>

<span style="font-size: 90%;">this is a nice change!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:49 UTC</span>

<span style="font-size: 90%;">Absolutely. It's so good to see dirty spots being cleaned up one after the other.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:57 UTC</span>

<span style="font-size: 90%;">Hope we are not adding too many new ones.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:56 UTC</span>

<span style="font-size: 90%;">2067 is the unfinished machine learning plugin. It was contributed from a student who won't be doing any work on this anymore. I do not think we can / should merge as is, but with some love, this could be made into something useful.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:21 UTC</span>

<span style="font-size: 90%;">Cutting down my optimism, I have to admit that it's unlikely I will find the time to do this anytime soon. (with soon being 2021)</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:12 UTC</span>

<span style="font-size: 90%;">ack</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:31 UTC</span>

<span style="font-size: 90%;">So if somebody looks for a new pet project, this could be it. And if not, we can also let it linger as unfinished PR for some more time.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:08:03 UTC</span>

<span style="font-size: 90%;">My plate is full :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:38 UTC</span>

<span style="font-size: 90%;">OK, then let's skip this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:44 UTC</span>

<span style="font-size: 90%;">2050 needs a reviewer with an interest in regex optimization. It's a simplification of the regex, but it might also introduce more FPs. So I am not sure it's worth it, but the existing ReDoS on the rule is probably also very bad. So it's hard to judge ...</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:10:46 UTC</span>

<span style="font-size: 90%;">I'll take it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:30 UTC</span>

<span style="font-size: 90%;">Thank you _@maxleske_. _@airween_?</span>

**airween** <span style="color: grey; font-size: 90%;">19:11:47 UTC</span>

<span style="font-size: 90%;">a side note: I made a small tool which collects the @rx operators and the arguments, and checks them against the REDOS. I've found that one with that tool</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:08 UTC</span>

<span style="font-size: 90%;">Nice! Could you link it in the issue?</span>

**airween** <span style="color: grey; font-size: 90%;">19:12:30 UTC</span>

<span style="font-size: 90%;">this is it, the 2050 (I guess)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:25 UTC</span>

<span style="font-size: 90%;">Cool one. I remember you showing said tool, I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:33 UTC</span>

<span style="font-size: 90%;">But I was not aware this was behind 2050.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:00 UTC</span>

<span style="font-size: 90%;">With 2049, we're in bit of a tricky situation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:01 UTC</span>

<span style="font-size: 90%;">TW has picked up our request to add more holistic JSON CT header. But only as a commented out suggestion, not as an update to the recommended rule 200001. They do not want to expand 200001, but think about introducing a new rule 200006 that does the same thing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:20 UTC</span>

<span style="font-size: 90%;">They also mention the recommended rules are more of a proposal and not meant to be comprehensive.</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:31 UTC</span>

<span style="font-size: 90%;">I like our solution</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:01 UTC</span>

<span style="font-size: 90%;">Yet, they are also asking for more opinions and I would appreciate if you could share your view in the ModSec PR where this discussion happens.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:30 UTC</span>

<span style="font-size: 90%;">After that discussion is over, we could also think about issuing our own recommended rules, this time a comprehensive variant!</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:35 UTC</span>

<span style="font-size: 90%;">I think we should merge it, it doesn’t harm if there are multiple rules setting it</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:44 UTC</span>

<span style="font-size: 90%;">even if TW updates their rules</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:49 UTC</span>

<span style="font-size: 90%;">That could in fact be a topic for the dev retreat.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:28 UTC</span>

<span style="font-size: 90%;">I am very reluctant to add redundancy here, as it makes debugging very hard, namely in the crazy case that TW mentions as a reason why they do not want to update 200001.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">There are more issues with the modsec recommended rules and a workshop on the topic could be very beneficial and end up with a vastly superior setup.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:10 UTC</span>

<span style="font-size: 90%;">-> the crazy case: People setting an exotic JSON CT, but it's not really JSON what they submit. When we start to body parse this as JSON, the parser will start to fail.
I think that's acceptable, but TW thinks it's not. With redundant twins of 200001, debugging that would become tricky for weak users.</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:59 UTC</span>

<span style="font-size: 90%;">I think this would probably be very rare</span>

**csanders** <span style="color: grey; font-size: 90%;">19:21:29 UTC</span>

<span style="font-size: 90%;">exceedingly, if they went through all that effort</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:32 UTC</span>

<span style="font-size: 90%;">(though I do sometimes have an app submitting non-json or just an empty file with a json Content-Type and getting it rejected by modsec)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:00 UTC</span>

<span style="font-size: 90%;">The empty file JSON is a classic source of pain with ModSec.</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:22:16 UTC</span>

<span style="font-size: 90%;">Sorry friends, i have to go, good night!</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:27 UTC</span>

<span style="font-size: 90%;">we could make a rule that switches off the JSON parser if content-length is 0 :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:28 UTC</span>

<span style="font-size: 90%;">So you guys think we should merge and see how this evolves? Or we wait for the dev retreat?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:22:36 UTC</span>

<span style="font-size: 90%;">good night azurit</span>

**dune73** <span style="color: grey; font-size: 90%;">19:22:37 UTC</span>

<span style="font-size: 90%;">Bye _@azurIt_! Thanks for joining!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:50 UTC</span>

<span style="font-size: 90%;">Personally, I would prefer to wait and to fork the recommended rules after we talk it through in October.</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:22 UTC</span>

<span style="font-size: 90%;">that’s also a good option. maybe then we could also set some more reasonable defaults for the PcreMatchLimits :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:25:13 UTC</span>

<span style="font-size: 90%;">_@jptosso_</span>

**dune73** <span style="color: grey; font-size: 90%;">19:25:45 UTC</span>

<span style="font-size: 90%;">Exactly. And look into the positioning of the rules. And kick 200004 and look into the proper position for 200005.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:26:23 UTC</span>

<span style="font-size: 90%;">The split between 'modsecurity.conf' and 'crs-setup.conf' is very confusing at first… Having a unified setup '.conf' file (which I think is what is being suggested here) would be amazing</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:16 UTC</span>

<span style="font-size: 90%;">Not sure we can make it into a single file. But no longer depending on a single additional config file from ModSec (which is also odd in the light of alternative engines being established).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:17 UTC</span>

<span style="font-size: 90%;">So what do we do? I can live with a merge now, but as I said, I'd prefer to wait some more.</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:19 UTC</span>

<span style="font-size: 90%;">I’m in favor of merging but I can see the other point too!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:41 UTC</span>

<span style="font-size: 90%;">Other opinions?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:00 UTC</span>

<span style="font-size: 90%;">Really a tough one</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:30:18 UTC</span>

<span style="font-size: 90%;">no clue...</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:31:41 UTC</span>

<span style="font-size: 90%;">I don't have a strong opinion here. But we are not in a hurry here and could wait with merging...</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:02 UTC</span>

<span style="font-size: 90%;">I would wait for now</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:40 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:43 UTC</span>

<span style="font-size: 90%;">@Walter can you live with we schedule this for October?</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:49 UTC</span>

<span style="font-size: 90%;">sure!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:02 UTC</span>

<span style="font-size: 90%;">In the meantime we can direct users to the new rule 200006 that has been merged as a comment.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:07 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:59 UTC</span>

<span style="font-size: 90%;">Two more to go. With 1993 we are a bit at an impasse as @Walter and I could not agree on basic plugin configuration / enabling at the previous meeting and we have not talked this through between us in the meantime.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:35:24 UTC</span>

<span style="font-size: 90%;">I suggest @Walter and I schedule a separate meeting in August so this can then proceed and the way is clear for future plugins.</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:21 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:55 UTC</span>

<span style="font-size: 90%;">Anything else to add here?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:36 UTC</span>

<span style="font-size: 90%;">The PR has been open quite some time - I do not know how Azurit feels about it. But a release is not imminent anyways, so I hope that's OK.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:22 UTC</span>

<span style="font-size: 90%;">Final one: 1975: This is just a check if there is suddenly somebody who uses NextCloud/Owncloud and could see him-/herself reviewing this PR properly. This is a contributing PR but we are not able to merge since no team member has any experience or time for this.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:41 UTC</span>

<span style="font-size: 90%;">I see few volunteers for 1975, so let's keep this open.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:08 UTC</span>

<span style="font-size: 90%;">Thank you all, this has been quick, we covered a lot of PRs on top of the 11 ones that we merged in July.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:46:48 UTC</span>

<span style="font-size: 90%;">_@dune73_ The issue appears to me to in part that there's functionality which could be used by some people but we can't make it available (even as an "alpha") because we can't put it into a release. Would it be feasible to put this into some kind of "plugin", e.g., git submodule or something so it can be pulled in even without an official release? As one of the people says, NextCloud appears to be unusable currently...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:27 UTC</span>

<span style="font-size: 90%;">Next item on the agenda is the status of the Coraza WAF, an alternative engine to ModSec.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:40 UTC</span>

<span style="font-size: 90%;">_@jptosso_ is here to give us an update. Please Juan!</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:42:21 UTC</span>

<span style="font-size: 90%;">Hey, thank you _@dune73_
Well, thank you for having me here, Coraza is an actual working port for modsecurity written in golang</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:42:45 UTC</span>

<span style="font-size: 90%;">It’s been in development for a year and it’s almost production ready.</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:55 UTC</span>

<span style="font-size: 90%;">very cool!</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:43:22 UTC</span>

<span style="font-size: 90%;">the architecture is similar and the APIs are already working and integrated with Caddy server</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:43:42 UTC</span>

<span style="font-size: 90%;">The idea with this project is to address some issues modsecurity team is not interested in</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:04 UTC</span>

<span style="font-size: 90%;">What do you mean by "architecture is similar"? Similar to ModSec? Or Caddy?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:44:48 UTC</span>

<span style="font-size: 90%;">to modsecurity, the APIs are similar and it works on the same principles, the main difference is Coraza uses token parsing instead of YACC</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:45:04 UTC</span>

<span style="font-size: 90%;">package main
import(
	"fmt"
	engine"github.com/jptosso/coraza-waf"
	"github.com/jptosso/coraza-waf/seclang"
)

func main() {
	// First we initialize our waf and our seclang parser
	waf := engine.NewWaf()
	parser := seclang.NewParser(waf)

	// Now we parse our rules
	parser.FromString(`SecRule REMOTE_ADDR "@rx .*" "id:1,phase:1,drop"`)

	// Then we create a transaction and assign some variables
	tx := waf.NewTransaction()
	tx.ProcessConnection("127.0.0.1", 8080, "127.0.0.1", 12345)

	tx.ProcessRequestHeaders()

	// Finally we check the transaction status
	if tx.Interrupted() {
		fmt.Println("Transaction was interrupted")
	}
}</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:45:13 UTC</span>

<span style="font-size: 90%;">this is a working sample for a Coraza transaction</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:46:22 UTC</span>

<span style="font-size: 90%;">right now Coraza is just a modsecurity implementation but the idea is to add some interesting enterprise features like
openapi support
enhanced logging (syslog and others)
antivirus native support
clustering
and more</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:46:35 UTC</span>

<span style="font-size: 90%;">[https://github.com/jptosso/coraza-waf#roadmap-long-term](https://github.com/jptosso/coraza-waf#roadmap-long-term)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:52 UTC</span>

<span style="font-size: 90%;">Oh, you have 113 stars already. Congratulations.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:11 UTC</span>

<span style="font-size: 90%;">Can you say anything about performance?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:47:22 UTC</span>

<span style="font-size: 90%;">yes, performance is of great importance</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:47:31 UTC</span>

<span style="font-size: 90%;">we are using libpcre just as modsecurity and its the main bottleneck</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:47:48 UTC</span>

<span style="font-size: 90%;">I can share an actual profiling graph</span>

**airween** <span style="color: grey; font-size: 90%;">19:48:02 UTC</span>

<span style="font-size: 90%;">and does Coraza support the libinjenction?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:48:21 UTC</span>

<span style="font-size: 90%;">yes, it’s integrated using CGO</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:48:31 UTC</span>

<span style="font-size: 90%;">I have been working on a golang port without success</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:48:59 UTC</span>

<span style="font-size: 90%;">I plan to use golang flags to compile CGO versions (with libinjection and libpcre) and without CGO (with golang implementation of libinejction and re2)</span>

**airween** <span style="color: grey; font-size: 90%;">19:49:31 UTC</span>

<span style="font-size: 90%;">is there any binary package?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:34 UTC</span>

<span style="font-size: 90%;">So RE2 and friends are on your roadmap (-> very important from my perspective)</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:49:54 UTC</span>

<span style="font-size: 90%;">you can use the working docker image</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:49:58 UTC</span>

<span style="font-size: 90%;">jptosso/coraza-waf</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:50:07 UTC</span>

<span style="font-size: 90%;"></span>

**jptosso** <span style="color: grey; font-size: 90%;">19:50:40 UTC</span>

<span style="font-size: 90%;">[https://medium.com/@jptosso/implementing-coraza-waf-with-docker-a55a995f055e](https://medium.com/@jptosso/implementing-coraza-waf-with-docker-a55a995f055e) here is a working wordpress implementation</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:13 UTC</span>

<span style="font-size: 90%;">PHP+Apache is the backend in this docker setup?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:51:19 UTC</span>

<span style="font-size: 90%;">yes</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:51:24 UTC</span>

<span style="font-size: 90%;">you can actually use caddy +fastcgi</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:51:31 UTC</span>

<span style="font-size: 90%;">but i believe apache is easier to explain</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:35 UTC</span>

<span style="font-size: 90%;">Cool. Something to run for real.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:46 UTC</span>

<span style="font-size: 90%;">I hear you are close to a v1.0 release?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:51:56 UTC</span>

<span style="font-size: 90%;">yes, so close</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:52:05 UTC</span>

<span style="font-size: 90%;">the api is almost stable, there are only some minor changes to expect</span>

**dune73** <span style="color: grey; font-size: 90%;">19:52:18 UTC</span>

<span style="font-size: 90%;">So it's like a matter of weeks?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:52:19 UTC</span>

<span style="font-size: 90%;">but they wont affect integrators, just internal functionalities</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:52:28 UTC</span>

<span style="font-size: 90%;">august is my deadline</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:52:46 UTC</span>

<span style="font-size: 90%;">with a coverage of 85%+</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:03 UTC</span>

<span style="font-size: 90%;">85% of the CRS testsuite?</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:53:14 UTC</span>

<span style="font-size: 90%;">actually coreruleset is fully supported</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:53:22 UTC</span>

<span style="font-size: 90%;">except by DDOS protections</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:33 UTC</span>

<span style="font-size: 90%;">Forget about those.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:53:41 UTC</span>

<span style="font-size: 90%;">Wow! Sounds to good to be true TBH :smile:</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:53:55 UTC</span>

<span style="font-size: 90%;">yea I havent implemented persistent collections yet</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:54:05 UTC</span>

<span style="font-size: 90%;">the dependencies required are too heavy</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:54:27 UTC</span>

<span style="font-size: 90%;">so I’m not sure if using a plugin architecture or hardcoding them</span>

**dune73** <span style="color: grey; font-size: 90%;">19:55:57 UTC</span>

<span style="font-size: 90%;">I would not add persistent collections for the time being. Few people use them and it's what makes the code so painful. CRS will outsource the DDoS stuff into a plugin soon and then we'll be free of persistent collections in the core release. I think that's all you need to support while establishing your software on the market.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:49 UTC</span>

<span style="font-size: 90%;">RE2 support, superior performance, small memory footprint and 100% coverage of the CRS test suite are much more important from my point of view.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:08 UTC</span>

<span style="font-size: 90%;">We need to push for that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:28 UTC</span>

<span style="font-size: 90%;">RE2 in all our regexes</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:57:34 UTC</span>

<span style="font-size: 90%;">I have to go to bed. Good night and bye :wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:58:05 UTC</span>

<span style="font-size: 90%;">I mostly agree. However, in our set up we relied heavily on the IP collection to do basic DOS filtering. I also wrote a rule to get clients to back off after producing too many failures from the backend, that rule also used collections.</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:58:34 UTC</span>

<span style="font-size: 90%;">So actually I need some help testing CRS, I have manually tested more than 1000 rules but there are 1000+ more to go
The actual tests are not compatible because they are meant for apache</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:43 UTC</span>

<span style="font-size: 90%;">I've used mod_evasive for thst</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:45 UTC</span>

<span style="font-size: 90%;">Bye _@franbuehler_!</span>

**jptosso** <span style="color: grey; font-size: 90%;">19:58:51 UTC</span>

<span style="font-size: 90%;">and Caddy won’t behave as apache</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:19 UTC</span>

<span style="font-size: 90%;">I would not expect "binary" compatibility</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:22 UTC</span>

<span style="font-size: 90%;">We should be able to help you there, I guess.</span>

**airween** <span style="color: grey; font-size: 90%;">19:59:38 UTC</span>

<span style="font-size: 90%;">I'm very happy to help in testing!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:39 UTC</span>

<span style="font-size: 90%;">Binary compatibility would be very nice, but would probably also need some work on our side.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:59:45 UTC</span>

<span style="font-size: 90%;">But more semantic one, were we achieve the same protection level</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:12 UTC</span>

<span style="font-size: 90%;">Could we add a Coraza setup to the Docker test containers?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:00:43 UTC</span>

<span style="font-size: 90%;">We can</span>

**dune73** <span style="color: grey; font-size: 90%;">20:00:50 UTC</span>

<span style="font-size: 90%;">_@maxleske_ That's all very useful and nice to do in ModSec, but there are alternatives beyond ModSec to accomplish this, so I think it should not be a priority for _@jptosso_.</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:00:53 UTC</span>

<span style="font-size: 90%;">_@airween_ that would be awesome !</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:01:02 UTC</span>

<span style="font-size: 90%;">But we need to rely on go-ftw</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:01:23 UTC</span>

<span style="font-size: 90%;">there is a repo, its outdated: [https://github.com/jptosso/coraza-ruleset](https://github.com/jptosso/coraza-ruleset)</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:01:34 UTC</span>

<span style="font-size: 90%;">I will update it today with tools to test coraza against CRS</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:53 UTC</span>

<span style="font-size: 90%;">What needs to happen so I can run Coraza in Apache and NGINX? So without the Caddy...</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:02:12 UTC</span>

<span style="font-size: 90%;">Well there is a chance, you can actually create a new package and use CGO externs</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:02:36 UTC</span>

<span style="font-size: 90%;">but I wouldn’t recommend it, as we spoke with _@fzipitria_, modern web servers are here to stay</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:02:45 UTC</span>

<span style="font-size: 90%;">and we should potentiate them</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:03:22 UTC</span>

<span style="font-size: 90%;">The reality is that we might take time to see this working in Apache or nginx</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:50 UTC</span>

<span style="font-size: 90%;">That might be true for startups, but the venerable ones will be around many years down the road.
What does it take on a dev level to make it happen the way ModSec3 has an API and an NGINX module that works with said ModSec3 API. Can you do the same with Coraza and all it takes somebody does the work, or is this more complicated (sorry, but I am not familiar with CGO externs and other things real programmers know).</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:06:39 UTC</span>

<span style="font-size: 90%;">technically modsecurity uses externs to create it’s libraries, it’s the same principle</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:06:46 UTC</span>

<span style="font-size: 90%;">but we would have to add C code to coraza</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:06:53 UTC</span>

<span style="font-size: 90%;">in order to create “exportable headers”</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:07:32 UTC</span>

<span style="font-size: 90%;">and the golang community doesn’t like CGO, it’s kind of a taboo</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:18 UTC</span>

<span style="font-size: 90%;">Why would you have to do this? Could not the NGINX/Apache module transpose the exportable headers into a format that the native Coraza can read in GO?</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:08:46 UTC</span>

<span style="font-size: 90%;">Yes but it requires a lot of C work, I would need a lot of help</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:09:21 UTC</span>

<span style="font-size: 90%;">but it would basically be the same as libmodsecurity with similar hooks</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:18 UTC</span>

<span style="font-size: 90%;">OK, got it. I see the big amount of work - and I also see it's not useful for you to make this a priority. But it might be for somebody else.</span>

**airween** <span style="color: grey; font-size: 90%;">20:10:26 UTC</span>

<span style="font-size: 90%;">and then we could embed Coraza in any kind of HTTP server, which written in C?</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:10:52 UTC</span>

<span style="font-size: 90%;">yes, using CGO and externs</span>

**airween** <span style="color: grey; font-size: 90%;">20:11:04 UTC</span>

<span style="font-size: 90%;">sounds fine</span>

**dune73** <span style="color: grey; font-size: 90%;">20:11:32 UTC</span>

<span style="font-size: 90%;">Thank you for this status update and the docker container. This is really cool.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:12:14 UTC</span>

<span style="font-size: 90%;">:man_dancing:</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:12:24 UTC</span>

<span style="font-size: 90%;">Thank you guys</span>

**dune73** <span style="color: grey; font-size: 90%;">20:12:48 UTC</span>

<span style="font-size: 90%;">You are most welcome.</span>

**jptosso** <span style="color: grey; font-size: 90%;">20:12:50 UTC</span>

<span style="font-size: 90%;">well if you have any comment or want to contribute you can find me here in slack or write me to [jptosso@gmail.com](mailto:jptosso@gmail.com)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:13:14 UTC</span>

<span style="font-size: 90%;">Thank you for joining. We're observing your progres eagerly.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:14:19 UTC</span>

<span style="font-size: 90%;">Time is moving fast. I'd like to talk a bit about our dev retreat in October and then maybe about more ideas to spend our money (OWASP kind of wants us to spend it in the year we're receiving it, so we better get going).</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:17 UTC</span>

<span style="font-size: 90%;">For the retreat, we have 4 full participants and 3 participants not the full weak, 3 tentative participants, 1 decline and 2 devs have not responded yet.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:16:33 UTC</span>

<span style="font-size: 90%;">So this comes along nicely and I take it we'll be between 6 and 10 people for most of the week. I think they have 7 or 8 rooms or so and I guess there is nothing wrong with bringing a mobile bed for a few nights to accomodate more people.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:20 UTC</span>

<span style="font-size: 90%;">I've started a wiki page at [https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-Topics](https://github.com/coreruleset/coreruleset/wiki/Dev-Retreat-Topics)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:18:03 UTC</span>

<span style="font-size: 90%;">If you have any idea what we could do there, please add it. It does not mean we will really do that once on site. But we will consider it together when we do the real program. So the more ideas the better.</span>

**airween** <span style="color: grey; font-size: 90%;">20:18:54 UTC</span>

<span style="font-size: 90%;">oh, looks like I can't attend for the full week. Here in .hu, where will the Autumn Holiday in schools on that day, and family wants me...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:02 UTC</span>

<span style="font-size: 90%;">Oh, oh.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:20:08 UTC</span>

<span style="font-size: 90%;">I have to go. Thanks and good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:26 UTC</span>

<span style="font-size: 90%;">Bye _@maxleske_ Thank you for participating.</span>

**airween** <span style="color: grey; font-size: 90%;">20:20:48 UTC</span>

<span style="font-size: 90%;">but I'm looking for some solution :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:21:31 UTC</span>

<span style="font-size: 90%;">Oh, dealing with the family during holidays will be tricky. Interested in your creative solution... :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:17 UTC</span>

<span style="font-size: 90%;">That much on the dev retreat. If you do not have any questions / suggestions beyond the wiki page for now, then let's move on.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:23:40 UTC</span>

<span style="font-size: 90%;">We have a budget of about 4K on dev-on-duty. I expect the dev retreat to be 8-10K. Azurit is writing a rule exclusion package for gold sponsor Kemp and that might be another 5-7K or so.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:04 UTC</span>

<span style="font-size: 90%;">Under the line, we have at least 20K that we can spend on useful things that are beneficial for our project.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:25:01 UTC</span>

<span style="font-size: 90%;">As I stated earlier, I would not mind being paid something for the coordination / communication / sponsoring work, but not before we are over 50K sponsoring per year.</span>

**airween** <span style="color: grey; font-size: 90%;">20:25:17 UTC</span>

<span style="font-size: 90%;">we can or we must? I mean, can we carry to the next year?</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:25 UTC</span>

<span style="font-size: 90%;">That doesn’t sound unreasonable. It is taking you a lot of effort.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:07 UTC</span>

<span style="font-size: 90%;">_@airween_: Let's say it's complicated and I spare you the details. Taking over too much will probably not work.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:26:30 UTC</span>

<span style="font-size: 90%;">Thanks @Walter, but let's postpone that until we have more to spare.</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:31 UTC</span>

<span style="font-size: 90%;">ah, I see</span>

**dune73** <span style="color: grey; font-size: 90%;">20:27:38 UTC</span>

<span style="font-size: 90%;">One thing that works nicely is the dev-on-duty and I was wondering what you guys would think about expanding it a bit and making it 200 USD per week. Like covering Twitter hashtags #ModSecurity #CRS3 #CoreRuleSet too?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:13 UTC</span>

<span style="font-size: 90%;">Azurit and Franbuehler have left already and they are engaged a lot as dev-on-duty, so we will obviously not take any decisions, but let's hear what you think?</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:43 UTC</span>

<span style="font-size: 90%;">sounds good to me!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:44 UTC</span>

<span style="font-size: 90%;">For me it's a way that serves the community and it allows a CRS dev to make some money aside. And if it's easy getting that money because there is actually very little work, then that's a benefit of being a CRS developer, I think. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:46 UTC</span>

<span style="font-size: 90%;">We could also pass on some money to other OWASP projects and become more popular within OWASP that way. Like the "CRS grant for promising new OWASP projects" of 2K USD per year. (But that's probably a lot of hassle for a jury and complicated to coordinate with HQ).</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:17 UTC</span>

<span style="font-size: 90%;">yeah, but preferably projects related to CRS…</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:33:40 UTC</span>

<span style="font-size: 90%;">If there are experienced Devs with time available, could some money be used to pay for development time for new features/rule categories?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:13 UTC</span>

<span style="font-size: 90%;">Another thing I have been discussing with Walter and Airween is a potential solution to the fake JSON that ModSec is writing. As you probably know, the ModSec alert message is taken as is and wrapped into JSON. People will then have to parse this themselves for their reports and everybody tries to reinvent the wheel.
I do not see Trustwave solving this anytime soon, but it's more and more a blocker for CRS adoption when I talk to customers / potential enterprise users.</span>

**walter** <span style="color: grey; font-size: 90%;">20:34:17 UTC</span>

<span style="font-size: 90%;">maybe we could even have a red team try to evade our protections</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:37 UTC</span>

<span style="font-size: 90%;">Commercial solutions of course come with great reporting features ...</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:54 UTC</span>

<span style="font-size: 90%;">A CRS bug bounty program sounds like a plan, yes!</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:14 UTC</span>

<span style="font-size: 90%;">I feel we get very little input from breakers</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:22 UTC</span>

<span style="font-size: 90%;">I guess they would rather keep their exploits to themselves…</span>

**walter** <span style="color: grey; font-size: 90%;">20:35:52 UTC</span>

<span style="font-size: 90%;">a bug bounty could solve that!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:35:53 UTC</span>

<span style="font-size: 90%;">Or we pay somebody to set up a real demo site so the breakers get something to grind their teeth into.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:36:39 UTC</span>

<span style="font-size: 90%;">Some might want to keep them to themselves, but bug disclosure can be pretty scary often resulting in people threatening to sue you. Participation in a bug bounty programme gives people a safe way of disclosing</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:57 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ Payment for generic rule development is certainly also an option. But I am somewhat afraid it kills the nature of a volunteer driven project. So I have a tendency to push for auxilliary projects that do not kill our incentives.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:37:28 UTC</span>

<span style="font-size: 90%;">Yes, disclosure policy or a bug bounty could be a way forward.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:38:05 UTC</span>

<span style="font-size: 90%;">As it happens, I am on very good terms with 2 bug bounty companies... I might be able to set up something with a profitable price tag.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:05 UTC</span>

<span style="font-size: 90%;">For the record: _@csanders_ has created a CRS demo site. But it stayed a proof of concept and it's not production ready.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:54 UTC</span>

<span style="font-size: 90%;">Do you have more ideas?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:41:06 UTC</span>

<span style="font-size: 90%;">For the JSON logging problem: Kemp is thinking about developing this themselves and using it as a unique selling point for their platform. I think that would make a lot of sense. But they told me they would also welcome somebody else pushing a solution they could re-use. But we ought to make up our mind in the next few weeks.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:43:09 UTC</span>

<span style="font-size: 90%;">How much would it cost to get the CRS fully audited? Or would that not be practical/worthwhile?</span>

**airween** <span style="color: grey; font-size: 90%;">20:43:11 UTC</span>

<span style="font-size: 90%;">in case of full native JSON log output, how do you imagine it? I mean does it need to keep the limit? (1131 byte)</span>

**dune73** <span style="color: grey; font-size: 90%;">20:43:28 UTC</span>

<span style="font-size: 90%;">Money is always a bit a tricky topic. Would you generally be OK if Walter and I talk this all through, consulting individual project members depending on the subject and move forward with spending projects?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:44:00 UTC</span>

<span style="font-size: 90%;">_@xanadu_ I have no f**ing clue. But we could try and get into the EU auditing program. That would be neat.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:45:04 UTC</span>

<span style="font-size: 90%;">Not sure if this is helpful... And realise it's a generic  modsec 'feature' not CRS, but for enterprise use one of the biggest barriers seems to be logging and log visualisation. Are there any projects that address either of these... Which could use funding?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:45:11 UTC</span>

<span style="font-size: 90%;">_@airween_: I'd say a best effort would be enough. JSON would mean you lose some information, but at least it's JSON. Or we do it outside ModSec and we can go beyond 1131 perhaps. Such a project would need a deep discussion on the goals.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:46:18 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_ Solving the JSON issue would be a basic building block to allow for better log integration and consequently reporting and visualisation afterwards. But when you can't even get the rule ID in a simple JSON format, that it's kind of moot.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:27 UTC</span>

<span style="font-size: 90%;">Repeating my question: Would you generally be OK if Walter and I talk this all through, consulting individual project members depending on the subject and move forward with spending projects?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:49:45 UTC</span>

<span style="font-size: 90%;">I do not want to push this down your throat, but September and afterwards December is close. :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">20:51:09 UTC</span>

<span style="font-size: 90%;">agree</span>

**walter** <span style="color: grey; font-size: 90%;">20:52:26 UTC</span>

<span style="font-size: 90%;">OK :slightly_smiling_face: no objections…</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:43 UTC</span>

<span style="font-size: 90%;">I guess everybody is almost asleepnow</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:45 UTC</span>

<span style="font-size: 90%;">I surely am</span>

**walter** <span style="color: grey; font-size: 90%;">20:53:55 UTC</span>

<span style="font-size: 90%;">shall we call it a day?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:54:39 UTC</span>

<span style="font-size: 90%;">My thumbs up was meant to indicate agreement with _@dune73_ spending suggestion</span>

**dune73** <span style="color: grey; font-size: 90%;">20:54:57 UTC</span>

<span style="font-size: 90%;">Yes, let's close this. Thank you all for participating! It's been fun seeing you all again!</span>

**emphazer** <span style="color: grey; font-size: 90%;">20:55:08 UTC</span>

<span style="font-size: 90%;">I wish everybody a good night</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:55:15 UTC</span>

<span style="font-size: 90%;">Good night everyone</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:55:24 UTC</span>

<span style="font-size: 90%;">Night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:55:32 UTC</span>

<span style="font-size: 90%;">see you in two weeks for the issues chat. I’ve reserved some time for working on my issues so hopefully I will have some good news</span>

**airween** <span style="color: grey; font-size: 90%;">20:56:49 UTC</span>

<span style="font-size: 90%;">good night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:56:53 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">21:03:18 UTC</span>

<span style="font-size: 90%;">Re: earlier comments about spending money, supporting other OWASP projects and testing rule evasion... I wonder whether we could get any join up with the ZAP project/community.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">21:03:43 UTC</span>

<span style="font-size: 90%;">:wave:</span>

