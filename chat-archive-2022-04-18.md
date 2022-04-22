### Mon, Apr 18th, 2022

**dune73** <span style="color: grey; font-size: 90%;">18:31:11 UTC</span>

<span style="font-size: 90%;">Hey, hey, it's still a holiday in some countries, but we still planned a chat for tonight. Issue chat - badly prepared though - and a few things to clear out before v4.0-RC1 can be published.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:30 UTC</span>

<span style="font-size: 90%;">Who's around?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:40 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**walter** <span style="color: grey; font-size: 90%;">18:31:51 UTC</span>

<span style="font-size: 90%;">Hello! Yes, it’s still holiday here, but no family visits today. :slightly_smiling_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:07 UTC</span>

<span style="font-size: 90%;">Happy Easter :rabbit2::egg::rabbit:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:39 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:33:03 UTC</span>

<span style="font-size: 90%;">Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:42 UTC</span>

<span style="font-size: 90%;">All exhausted from the family holidays, but we're back home again and the friends and family have all left (and most of the kids in bed...)</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:18 UTC</span>

<span style="font-size: 90%;">Yeah, same here. I run on caffeine today and will likely sleep like a bear tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:34:46 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:05 UTC</span>

<span style="font-size: 90%;">So let’s chat! Shall we focus on the todo’s left for 4.0-RC1 and perhaps 4.0-final?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:08 UTC</span>

<span style="font-size: 90%;">Shall we tackle the pending RC1 first? You mentioned a few open threads _@walter_</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:26 UTC</span>

<span style="font-size: 90%;">Yes, let's do that. And then add some important issues that need discussion.</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:46 UTC</span>

<span style="font-size: 90%;">If I go to the 4.0 milestone there are quite some issues there (but some can be done after RC1)</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:47 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/milestone/10](https://github.com/coreruleset/coreruleset/milestone/10)</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:06 UTC</span>

<span style="font-size: 90%;">Last week meeting notes are here with a checklist: [https://github.com/coreruleset/coreruleset/issues/2491](https://github.com/coreruleset/coreruleset/issues/2491)</span>

**walter** <span style="color: grey; font-size: 90%;">18:36:28 UTC</span>

<span style="font-size: 90%;">The checklist is mostly done EXCEPT for the plugins enablement, which we should nail before RC1.</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:13 UTC</span>

<span style="font-size: 90%;">If I understand correctly, _@dune73_ suggested boilerplate for the plugins, but it did not implement the choice we made last meeting to default enable… Let me take a look…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:26 UTC</span>

<span style="font-size: 90%;">OK. I also think this is the very thing that needs being done for RC1. Other than that, I think there is time after RC1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:27 UTC</span>

<span style="font-size: 90%;">_@dune73_ Did you read my message in the other channel?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:53 UTC</span>

<span style="font-size: 90%;">I meant to implement default enable.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:08 UTC</span>

<span style="font-size: 90%;">_@maxleske_ Probably not. Which one. (Been away from screen several days)</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:12 UTC</span>

<span style="font-size: 90%;">[https://owasp.slack.com/archives/G01K88J8SDB/p1650273797098459](https://owasp.slack.com/archives/G01K88J8SDB/p1650273797098459)</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:23 UTC</span>

<span style="font-size: 90%;">I looked at your change to the dummy plugin and I’m confused. My understanding was that we would stick to the following convention for now:In [https://github.com/coreruleset/dummy-plugin/commit/6bf335d93576cc971cc6d8e3331b10115d032d8a](https://github.com/coreruleset/dummy-plugin/commit/6bf335d93576cc971cc6d8e3331b10115d032d8a) you appear to have changed that to
That change is fine by me but I just want to make sure that we all have the same intention.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:38:31 UTC</span>

<span style="font-size: 90%;">Yes, that was the question</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:02 UTC</span>

<span style="font-size: 90%;">I did not see this question.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:39:18 UTC</span>

<span style="font-size: 90%;">One of us is reading the rules wrong. Let me check again.</span>

**walter** <span style="color: grey; font-size: 90%;">18:39:39 UTC</span>

<span style="font-size: 90%;">In our last meet we discussed the options and we chose:
There are multiple scenarios: Option 2 is chosen with no dissent.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:11 UTC</span>

<span style="font-size: 90%;">Here is the enabling / disabling rule:
SecRule &TX:dummy-plugin_enabled "@eq 1" "id:9500099,phase:1,pass,nolog,chain"
   SecRule TX:dummy-plugin_enabled "@eq 0" "ctl:ruleRemoveById=9500100-9500999"</span>

**dune73** <span style="color: grey; font-size: 90%;">18:40:51 UTC</span>

<span style="font-size: 90%;">When there is no dummy-plugin_enabled var, then the rule does not hit and the plugin is left intact. -> Default on.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:56 UTC</span>

<span style="font-size: 90%;">Ok, let’s see, so that first checks for presence of the variable (is that chain necessary and can we just do with a SecRule eq 0?)</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:14 UTC</span>

<span style="font-size: 90%;">And is a skip not easier to maintain than rule removals?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:17 UTC</span>

<span style="font-size: 90%;">If there is a variable and it is eq 0, the plugin is disabled by removing the rules for the current transaction.</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:21 UTC</span>

<span style="font-size: 90%;">Or is there a reason why that don’t work.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">The problem with skips is that it's 5 phases to skip. Thus 5 rules, vs. 1 chained rule.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:45 UTC</span>

<span style="font-size: 90%;">Ah yes. I missed the @eq 1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:42:15 UTC</span>

<span style="font-size: 90%;">However, the dummy plugin is disabled by default right? You have an additional rule that sets the var to 0</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:42 UTC</span>

<span style="font-size: 90%;">I had implemented the skip variant, explained it, did not get any feedback, tried out the rule-removal variant and I think it is way easier to implement, even if it is a bit harder to read. But that's a question of commenting it properly.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:17 UTC</span>

<span style="font-size: 90%;">SecRule &TX:dummy-plugin_enabled "@eq 0" "id:9500010,\
    phase:1,\
    pass,\
    nolog,\
    ver:'dummy-plugin/0.0.1',\
    setvar:'tx.dummy-plugin_enabled=0'"</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:57 UTC</span>

<span style="font-size: 90%;">@Walter chain: You mean remove the chain and simply check value of var and if it is not existing, the rule is not executed?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:02 UTC</span>

<span style="font-size: 90%;">That should work, yes.</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:03 UTC</span>

<span style="font-size: 90%;">_@dune73_ yes!</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:15 UTC</span>

<span style="font-size: 90%;">if the variable is not present, the rule won’t fire</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:52 UTC</span>

<span style="font-size: 90%;">That would give us:
SecRule TX:dummy-plugin_enabled "@eq 0" "id:9500099,phase:1,pass,nolog,ctl:ruleRemoveById=9500100-9500999"</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:05 UTC</span>

<span style="font-size: 90%;">:+1: That looks great</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:44 UTC</span>

<span style="font-size: 90%;">Assuming this works - and I think it will - I agree this is preferred and easier to read.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:46:24 UTC</span>

<span style="font-size: 90%;">_@maxleske_ what is the 9500010 you sent above? That would be setting it as default=off, would not it.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:39 UTC</span>

<span style="font-size: 90%;">Exactly, that's why I'm asking...</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:39 UTC</span>

<span style="font-size: 90%;">it’s here now [https://github.com/coreruleset/dummy-plugin/blob/main/plugins/dummy-config.conf](https://github.com/coreruleset/dummy-plugin/blob/main/plugins/dummy-config.conf)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:23 UTC</span>

<span style="font-size: 90%;">Ah, my bad. Sorry.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:39 UTC</span>

<span style="font-size: 90%;">I mean, that's fine but I wasn't sure whether that was there for documentation.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:47:43 UTC</span>

<span style="font-size: 90%;">I've been playing around with this and seemed to have commited a trial version.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:20 UTC</span>

<span style="font-size: 90%;">But speaking of: I would not mind removing the config file actually.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:42 UTC</span>

<span style="font-size: 90%;">Completely? Or just for the dummy plugin?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:58 UTC</span>

<span style="font-size: 90%;">dummy-plugin fixed</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:24 UTC</span>

<span style="font-size: 90%;">It could be good to have a config file example for people who want to make configurable plugins. But for the dummy plugin, it could be just an example using text like tx.dummy-plugin_yourvariable</span>

**dune73** <span style="color: grey; font-size: 90%;">18:49:30 UTC</span>

<span style="font-size: 90%;">I've commited it anew. Now the plugin file only carries the enabling rule as a comment. So it is in fact empty.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:16 UTC</span>

<span style="font-size: 90%;">Ok. That's better :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:20 UTC</span>

<span style="font-size: 90%;">what about making a little “crs-setup.conf” like file with a comment and an unused variable?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:12 UTC</span>

<span style="font-size: 90%;">For the dummy that would be cool, I think.

And adding a comment that tells people that they can also do plugins without a config file as long as the disabling rule is present in the -before.conf.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:15 UTC</span>

<span style="font-size: 90%;">Do we agree this is how we want to implement this? I can do this tonight for the dummy plugin. But then we ought to follow suit with the other plugins too. The ...00099 rule is relatively easy to do, but I would not want to merge without review.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:38 UTC</span>

<span style="font-size: 90%;">(The ctl statement has to be double-checked!)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:47 UTC</span>

<span style="font-size: 90%;">Or automated. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:53:58 UTC</span>

<span style="font-size: 90%;">Good for me. I was just waiting for the moment I could go and modify the other plugins</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:00 UTC</span>

<span style="font-size: 90%;">What about:
# If your plugin is configurable with variables (like limits, strictness, etc.)
# you can add your variables here. Leave them commented out, so that interested
# users can activate the variable by removing the comment chars.
#
# Example variable:
#
#SecAction \
# “id:9500990,\
#  phase:1,\
#  nolog,\
#  pass,\
#  t:none,\
#  setvar:tx.dummy_plugin-myvariable=1”</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:54:45 UTC</span>

<span style="font-size: 90%;">dummy-plugin_myvariable :stuck_out_tongue:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:50 UTC</span>

<span style="font-size: 90%;">Thanks. I'm not entirely happy with the wording, but we can finish this tonight after the chat.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:21 UTC</span>

<span style="font-size: 90%;">(we had some fun with variable naming last week in the chat)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:30 UTC</span>

<span style="font-size: 90%;">We have to make sure that the variable names are very clear. I like <pluginname-plugin>_whatever .</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:56:00 UTC</span>

<span style="font-size: 90%;">Yes, we agreed that that form was a good idea</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:04 UTC</span>

<span style="font-size: 90%;">Ah, it seems I missed that part of the party. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">Cool. Thanks.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:42 UTC</span>

<span style="font-size: 90%;">So we're done for this? I finish the dummy plugin with a text based on Walter's proposal and Max will update the other plugins afterwards?</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:59 UTC</span>

<span style="font-size: 90%;">I think we’re on the same page, so that sounds great :+1:</span>

**walter** <span style="color: grey; font-size: 90%;">18:57:17 UTC</span>

<span style="font-size: 90%;">and you’ll remove the chain?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:38 UTC</span>

<span style="font-size: 90%;">I'll remove the chain and add a comment what this rule does and that the plugin is default-on.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:01 UTC</span>

<span style="font-size: 90%;">I'll turn to documenting this and the VirtualHost enabling / disabling options after RC1 is out.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:58:50 UTC</span>

<span style="font-size: 90%;">What else to deal with before RC1?</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:43 UTC</span>

<span style="font-size: 90%;">We could take a look at [https://github.com/coreruleset/coreruleset/milestone/10](https://github.com/coreruleset/coreruleset/milestone/10)</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:34 UTC</span>

<span style="font-size: 90%;">shall we briefly list them?</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:41 UTC</span>

<span style="font-size: 90%;">[#2499](https://github.com/coreruleset/coreruleset/issues/#2499) - the meeting notes.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:42 UTC</span>

<span style="font-size: 90%;">Please go ahead.</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:03 UTC</span>

<span style="font-size: 90%;">[#2498](https://github.com/coreruleset/coreruleset/issues/#2498) - I want the new docs to be online at release, but not necessarily for RC1. However, we will need to explain plugins carefully, since it’s new for everybody. I haven’t read the plugins page of the docs but if I miss anything I will add it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:33 UTC</span>

<span style="font-size: 90%;">But I think there is not much on the WordPress docs/ page which is not yet in the Big Docs. Xanadu has offered to add it.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:13 UTC</span>

<span style="font-size: 90%;">Important to remember: we will need both v3.3.2 docs for future reference and new v4.0 docs. We don't currently have the ability to differentiate between them…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:03:40 UTC</span>

<span style="font-size: 90%;">I think the plugin documentation is basically OK. But the whole enabling / disabling has to be updated.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:43 UTC</span>

<span style="font-size: 90%;">For example: paranoia level content needs adjusting for v4, but we need to keep the old v3.3.2 stuff.</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:51 UTC</span>

<span style="font-size: 90%;">I think for now, probably we should do with one docs and just handle both cases in one page. Otherwise, duplicating the whole tree per version will cause us a lot of work.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:01 UTC</span>

<span style="font-size: 90%;">That's a huge pain.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:04:06 UTC</span>

<span style="font-size: 90%;">But probably a conversation for another time.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:04:24 UTC</span>

<span style="font-size: 90%;">I'd rather have a tree per version.</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:32 UTC</span>

<span style="font-size: 90%;">I think the differences are not so huge that we can make do with a “If you have 3.x, do this, if you have 4.x, do that”</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:36 UTC</span>

<span style="font-size: 90%;">We don’t need a whole tree</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:56 UTC</span>

<span style="font-size: 90%;">But we shall discuss this another time as Andrew proposes</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:59 UTC</span>

<span style="font-size: 90%;">OK</span>

**dune73** <span style="color: grey; font-size: 90%;">19:05:03 UTC</span>

<span style="font-size: 90%;">Fine with me.</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:46 UTC</span>

<span style="font-size: 90%;">[#2492](https://github.com/coreruleset/coreruleset/issues/#2492) - the copyright notices - I think this is (almost) done</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:55 UTC</span>

<span style="font-size: 90%;">[@dune73](https://github.com/dune73) : Are you happy to merge the copyright notice PRs on:
[https://github.com/coreruleset/dummy-plugin](https://github.com/coreruleset/dummy-plugin)
[https://github.com/coreruleset/auto-decoding-plugin](https://github.com/coreruleset/auto-decoding-plugin)
[https://github.com/coreruleset/incubator-plugin](https://github.com/coreruleset/incubator-plugin)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:40 UTC</span>

<span style="font-size: 90%;">Yes, absolutely.</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:43 UTC</span>

<span style="font-size: 90%;">Merging.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:04 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:54 UTC</span>

<span style="font-size: 90%;">[#2491](https://github.com/coreruleset/coreruleset/issues/#2491) - our last meeting notes.</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:05 UTC</span>

<span style="font-size: 90%;">[#2495](https://github.com/coreruleset/coreruleset/issues/#2495) - [https://github.com/coreruleset/coreruleset/issues/2475](https://github.com/coreruleset/coreruleset/issues/2475)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:09:18 UTC</span>

<span style="font-size: 90%;">Simon failed to reproduce the problem and I need to look into it some for (I'm the original reporter).
In any case it's an edge case with reporting and nobody gives a shit if this works for RC1 or not.</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:35 UTC</span>

<span style="font-size: 90%;">haha, language!!!</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:48 UTC</span>

<span style="font-size: 90%;">well then let’s leave it open</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:57 UTC</span>

<span style="font-size: 90%;">[#2474](https://github.com/coreruleset/coreruleset/issues/#2474)</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:02 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2474](https://github.com/coreruleset/coreruleset/issues/2474)</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:13 UTC</span>

<span style="font-size: 90%;">I think this is now closable due to the PRs, right? :+1:</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:31 UTC</span>

<span style="font-size: 90%;">I merged the last changes to the reporting this afternoon.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:10:40 UTC</span>

<span style="font-size: 90%;">Exactly.</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:09 UTC</span>

<span style="font-size: 90%;">[#2453](https://github.com/coreruleset/coreruleset/issues/#2453) another meeting agenda</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:17 UTC</span>

<span style="font-size: 90%;">[#2452](https://github.com/coreruleset/coreruleset/issues/#2452) [https://github.com/coreruleset/coreruleset/issues/2452](https://github.com/coreruleset/coreruleset/issues/2452)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:26 UTC</span>

<span style="font-size: 90%;">I think reporting is ready for RC1. I asked whether we want even more granular reporting level, but that's probably academic and could be discussed after RC1.</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:58 UTC</span>

<span style="font-size: 90%;">If you can make it look like a bug it can be integrated after RC1 :wink:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:22 UTC</span>

<span style="font-size: 90%;">[#2452](https://github.com/coreruleset/coreruleset/issues/#2452): I think most of this is answered in the existing documentation.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:46 UTC</span>

<span style="font-size: 90%;">But I agree it might be out of sync with the various locations.</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:57 UTC</span>

<span style="font-size: 90%;">I think the plugin documentation is quite good already - [https://coreruleset.org/docs/configuring/plugins/](https://coreruleset.org/docs/configuring/plugins/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:13:12 UTC</span>

<span style="font-size: 90%;">That's what I meant to say.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:13:49 UTC</span>

<span style="font-size: 90%;">Plugin registry PR needs merging</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:52 UTC</span>

<span style="font-size: 90%;">the plugin-registry repo is there, [https://github.com/coreruleset/plugin-registry](https://github.com/coreruleset/plugin-registry) but may be out-of-date</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:11 UTC</span>

<span style="font-size: 90%;">i'll go over it</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:18 UTC</span>

<span style="font-size: 90%;">OK :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">.../docs is of better quality than the dummy-plugin documentation, also.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:14:58 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/plugin-registry/pull/8](https://github.com/coreruleset/plugin-registry/pull/8)
That should bring it up to date (it is indeed currently out of date.)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:15:30 UTC</span>

<span style="font-size: 90%;">Let's merge then!</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:32 UTC</span>

<span style="font-size: 90%;">Then shall we just merg?</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:38 UTC</span>

<span style="font-size: 90%;">I merg’d.</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:51 UTC</span>

<span style="font-size: 90%;">do we want to keep [https://github.com/coreruleset/coreruleset/issues/2452](https://github.com/coreruleset/coreruleset/issues/2452) open? not all the ideas were addressed, such as a .yaml file for automatic consumption</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:08 UTC</span>

<span style="font-size: 90%;">Hi guys!</span>

**airween** <span style="color: grey; font-size: 90%;">19:17:15 UTC</span>

<span style="font-size: 90%;">sorry for the late...</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:23 UTC</span>

<span style="font-size: 90%;">np</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:17:27 UTC</span>

<span style="font-size: 90%;">Should we add the version number and maybe a current status to that registry table? e.g. the v3 plugin for DoS still requires some testing</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:00 UTC</span>

<span style="font-size: 90%;">I think it's a nice checklist to have once we're through with all the plugins</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:11 UTC</span>

<span style="font-size: 90%;">updating the version number will be a drag, but a status would be nice - and even a purpose (‘draft’, ‘research’, ‘exclusion’, ‘detection’)</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:18:46 UTC</span>

<span style="font-size: 90%;">I'll do that then</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:14 UTC</span>

<span style="font-size: 90%;">[#2452](https://github.com/coreruleset/coreruleset/issues/#2452) I mean</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:46 UTC</span>

<span style="font-size: 90%;">I'll do that then</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:18:46 UTC</span>

<span style="font-size: 90%;">I'll do that then</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:15 UTC</span>

<span style="font-size: 90%;">We have "type" in the plugin registry. I'd be open to use this for for purpose as well.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:36 UTC</span>

<span style="font-size: 90%;">Thus resulting in e.g. "Official; Research"</span>

**dune73** <span style="color: grey; font-size: 90%;">19:19:43 UTC</span>

<span style="font-size: 90%;">Or we group them in the README.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:04 UTC</span>

<span style="font-size: 90%;">I think we're talking about two different concepts.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:23 UTC</span>

<span style="font-size: 90%;">I want the status for e.g., "beta", "WIP"</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:42 UTC</span>

<span style="font-size: 90%;">But I agree, opening the type could be interesting</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:11 UTC</span>

<span style="font-size: 90%;">yes, a stability field would be great</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:35 UTC</span>

<span style="font-size: 90%;">Happy to explore the options. But better after RC1. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:21:53 UTC</span>

<span style="font-size: 90%;">(I'll start to do stickers: "We'll do this after RC1")</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:00 UTC</span>

<span style="font-size: 90%;">That is fine.</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:36 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2443](https://github.com/coreruleset/coreruleset/issues/2443) - will we need this slide deck soon?</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:55 UTC</span>

<span style="font-size: 90%;">We could distill it from the blogpost and the CHANGED file.</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">So I’d say after RC1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:04 UTC</span>

<span style="font-size: 90%;">I agreed on a "What's new in CRS4" presentation May 9. So I guess I have some pressure. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:17 UTC</span>

<span style="font-size: 90%;">That’s a lifetime!</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:25 UTC</span>

<span style="font-size: 90%;">But not needed for RC1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:36 UTC</span>

<span style="font-size: 90%;">Tried to postpone the talk to September, but no avail. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:01 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2433](https://github.com/coreruleset/coreruleset/issues/2433)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:36 UTC</span>

<span style="font-size: 90%;">Lost track here a bit. Has this been done?</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:37 UTC</span>

<span style="font-size: 90%;">Is this plugin already there? let me look..</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:03 UTC</span>

<span style="font-size: 90%;">0 results for all repositories matching reputation</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:32 UTC</span>

<span style="font-size: 90%;">seems not done yet, but I would really advocate doing it now</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:56 UTC</span>

<span style="font-size: 90%;">[Move IP reputation rules to separate plugin #2433](https://github.com/coreruleset/coreruleset/issues/2433) - Bring back IP reputation functionality as 2 separate plugins. See [comment](https://github.com/coreruleset/coreruleset/pull/2483#issuecomment-1094216762)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:09 UTC</span>

<span style="font-size: 90%;">No, plugin is certainly not done. But are the rules still there?</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:14 UTC</span>

<span style="font-size: 90%;">last week we thought that we could remove it and make the plugins later</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:23 UTC</span>

<span style="font-size: 90%;">what do you think?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:23 UTC</span>

<span style="font-size: 90%;">Yes, that's my thinking.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:31 UTC</span>

<span style="font-size: 90%;">You want the plugins for RC1?</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:45 UTC</span>

<span style="font-size: 90%;">No</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:53 UTC</span>

<span style="font-size: 90%;">people who depend on it, can wait a bit</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:01 UTC</span>

<span style="font-size: 90%;">it will be dozens</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:14 UTC</span>

<span style="font-size: 90%;">but, we still have to remove the code carefully from 4.0.</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:19 UTC</span>

<span style="font-size: 90%;">volunteers? :smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:27 UTC</span>

<span style="font-size: 90%;">That already happened, no?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:34 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/pull/2483](https://github.com/coreruleset/coreruleset/pull/2483)</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:38 UTC</span>

<span style="font-size: 90%;">That was in the merged PR</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:42 UTC</span>

<span style="font-size: 90%;">ah excellent</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:56 UTC</span>

<span style="font-size: 90%;">Confirmed. The rules are gone.</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:30 UTC</span>

<span style="font-size: 90%;">awesome, closing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:28:36 UTC</span>

<span style="font-size: 90%;">+1</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:53 UTC</span>

<span style="font-size: 90%;">was the same done for the DoS rules?</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:58 UTC</span>

<span style="font-size: 90%;">[#2373](https://github.com/coreruleset/coreruleset/issues/#2373)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:18 UTC</span>

<span style="font-size: 90%;">Gone even before the IP reputation</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:19 UTC</span>

<span style="font-size: 90%;">What about the plugin? Is there a separate issue for "Make an IP reputation plugin"?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:28 UTC</span>

<span style="font-size: 90%;">Or was that the issue that was just closed?</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:40 UTC</span>

<span style="font-size: 90%;">It’s currently just a checklist item in the meeting notes.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:52 UTC</span>

<span style="font-size: 90%;">That seems easy to forget.</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:06 UTC</span>

<span style="font-size: 90%;">OK I’ll create an issue</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">Let's open two issues for the 2 plugins we need.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:30:20 UTC</span>

<span style="font-size: 90%;">2 please.</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:17 UTC</span>

<span style="font-size: 90%;">One for the GeoIP check, and one for our own “reput” system?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:00 UTC</span>

<span style="font-size: 90%;">If \@rbl is our own, then yes.</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:36 UTC</span>

<span style="font-size: 90%;">Oh no I thought about the variable that gets expired and we keep blocking the IP address (or something - never properly looked at it)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:41 UTC</span>

<span style="font-size: 90%;">Maybe we discuss the plugins we really want after RC1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:34:00 UTC</span>

<span style="font-size: 90%;">The "after-RC1" sticker will also have a glitter option.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:34:26 UTC</span>

<span style="font-size: 90%;">:sparkles:</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:09 UTC</span>

<span style="font-size: 90%;">OK let’s move on toooo..</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:20 UTC</span>

<span style="font-size: 90%;">[#2394](https://github.com/coreruleset/coreruleset/issues/#2394) [https://github.com/coreruleset/coreruleset/issues/2394](https://github.com/coreruleset/coreruleset/issues/2394)</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:42 UTC</span>

<span style="font-size: 90%;">Seems to be work in progress. But no worry, it can be released when it’s done.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:15 UTC</span>

<span style="font-size: 90%;">Yes, waiting to hear from the tester</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:59 UTC</span>

<span style="font-size: 90%;">[#2389](https://github.com/coreruleset/coreruleset/issues/#2389) [https://github.com/coreruleset/coreruleset/issues/2389](https://github.com/coreruleset/coreruleset/issues/2389) You seemed to have found a solution for this!</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:51 UTC</span>

<span style="font-size: 90%;">So a ‘engine compatibility’ field in the plugin registry will also be interesting. This one would have a checkmark for v3, the other one for v2.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:06 UTC</span>

<span style="font-size: 90%;">Ah, good idea.</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:06 UTC</span>

<span style="font-size: 90%;">it needs to be tested but who oh who runs Nginx?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:19 UTC</span>

<span style="font-size: 90%;">My former employer would</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:38 UTC</span>

<span style="font-size: 90%;">_@theMiddle_'s former employer too. :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">There are also a couple of interested people that opened issues for the workaround</span>

**dune73** <span style="color: grey; font-size: 90%;">19:39:14 UTC</span>

<span style="font-size: 90%;">Do we really need that field though. Is not it 95% all and very few exceptions that can be covered in the specific readme?</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:16 UTC</span>

<span style="font-size: 90%;">Well, let’s keep it beta until they come back with their results.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:39:47 UTC</span>

<span style="font-size: 90%;">Agreed. We already designated those two plugins by putting the version in the plugin name</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:01 UTC</span>

<span style="font-size: 90%;">yes, that is clear enough IMHO</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:55 UTC</span>

<span style="font-size: 90%;">do we leave this issue open? it’s really an issue on the plugin</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:07 UTC</span>

<span style="font-size: 90%;">but it could be hard to remember</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:41:33 UTC</span>

<span style="font-size: 90%;">Yes please. But you can remove the milestone, I guess</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:47 UTC</span>

<span style="font-size: 90%;">done.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:41:55 UTC</span>

<span style="font-size: 90%;">Cool. What else?</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:15 UTC</span>

<span style="font-size: 90%;">there are three issues about converting RE packages to plugins</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:40 UTC</span>

<span style="font-size: 90%;">I’m sure they are great, but they might be in need of some testing</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:54 UTC</span>

<span style="font-size: 90%;">I could take the Wordpress plugin</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:20 UTC</span>

<span style="font-size: 90%;">then there is phpBB and phpMyAdmin</span>

**walter** <span style="color: grey; font-size: 90%;">19:43:54 UTC</span>

<span style="font-size: 90%;">I could also install phpmyadmin…</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:10 UTC</span>

<span style="font-size: 90%;">FWIW, once I'd moved the RE packages I signed up for over to plugins, and then Azurit gave the thumbs up, I simply closed the issues :speak_no_evil:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:22 UTC</span>

<span style="font-size: 90%;">Unless someone has time to install and test DokuWiki, XenForo, etc. etc.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:27 UTC</span>

<span style="font-size: 90%;">Azurit worked on these two plugins, did not he?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:40 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:44:46 UTC</span>

<span style="font-size: 90%;">I've reviewed, they look good to me.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:01 UTC</span>

<span style="font-size: 90%;">I mean it's relatively easy to test for basic functionality (plugin removes existing FPs) without running the software. But it's substantial work to confirm the plugin covers 95+% of false positives for a given software.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:12 UTC</span>

<span style="font-size: 90%;">Unless you run e.g. WP on a scale like Walter.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:46:23 UTC</span>

<span style="font-size: 90%;">So I do not really know.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:27 UTC</span>

<span style="font-size: 90%;">I vimdiff'ed the old and the new, and confirmed all looks good.</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:02 UTC</span>

<span style="font-size: 90%;">I will give the WP plugin a whirl.</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:01 UTC</span>

<span style="font-size: 90%;">anyone who is interested in phpMyAdmin? otherwise I can try</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:48 UTC</span>

<span style="font-size: 90%;">If we're happy with the existing RE functionality transposed to plugin, I think the vimdiff and 1-2 checks is enough.</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:22 UTC</span>

<span style="font-size: 90%;">phpMyAdmin has changed significantly for the new phpMyAdmin version right? so I’d like to install that new version and try it. but, can be done after RC1.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:49:28 UTC</span>

<span style="font-size: 90%;">phpMyAdmin software has a new release though and it all runs under index.php now. Very tough for a future RE plugin / pkg.</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:47 UTC</span>

<span style="font-size: 90%;">yes, it’s a difficult one</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:59 UTC</span>

<span style="font-size: 90%;">and especially interesting to only enable on /phpmyadmin</span>

**dune73** <span style="color: grey; font-size: 90%;">19:50:38 UTC</span>

<span style="font-size: 90%;">Yep.</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:39 UTC</span>

<span style="font-size: 90%;">I’ll volunteer (after RC1)</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:48 UTC</span>

<span style="font-size: 90%;">we need volunteers for testing the phpBB plugin</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:00 UTC</span>

<span style="font-size: 90%;">in any case I can do a test install as well</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:52:10 UTC</span>

<span style="font-size: 90%;">there are two plugins though: the current one and then the update for 5.1</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:52:56 UTC</span>

<span style="font-size: 90%;">If we're checking all the new plugins, then there's also:
Drupal
Nextcloud
Dokuwiki
cPanel
XenForo</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:04 UTC</span>

<span style="font-size: 90%;">yes…</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:53:07 UTC</span>

<span style="font-size: 90%;">Those were done with a check but no proper testing.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:53:14 UTC</span>

<span style="font-size: 90%;">IMO that's an enormous amount of work.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:23 UTC</span>

<span style="font-size: 90%;">Yes, it really is.</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:34 UTC</span>

<span style="font-size: 90%;">I will put the XenForo just in prod, I have one customer using it and they like me so if there’s a hickup they won’t be mad</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:11 UTC</span>

<span style="font-size: 90%;">for the rest, we’ll just rely on the separate release schedules for the plugins</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:17 UTC</span>

<span style="font-size: 90%;">Maybe we need to make things transparent with the RE plugins and keep a "last updated / tested officially at xxx" for every plugin.</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:25 UTC</span>

<span style="font-size: 90%;">good idea!</span>

**walter** <span style="color: grey; font-size: 90%;">19:54:32 UTC</span>

<span style="font-size: 90%;">this is what [wordpress.org](http://wordpress.org) also does with their plugin registry</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:42 UTC</span>

<span style="font-size: 90%;">It won't be beautiful, though.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:59 UTC</span>

<span style="font-size: 90%;">But it might incentivize people to contribute.</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:05 UTC</span>

<span style="font-size: 90%;">alright, I’ve written: For other plugins, we don’t really have the infrastructure and time to set up instances of every app. We will rely on bug reports and frequent releases.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:54 UTC</span>

<span style="font-size: 90%;">I like this.</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:14 UTC</span>

<span style="font-size: 90%;">This is all that was assigned with the 4.0 label!</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:17 UTC</span>

<span style="font-size: 90%;">So in short…</span>

**walter** <span style="color: grey; font-size: 90%;">19:57:58 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:58:23 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:58:28 UTC</span>

<span style="font-size: 90%;">For RC1</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:40 UTC</span>

<span style="font-size: 90%;">Brillant. Thank you.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:59:06 UTC</span>

<span style="font-size: 90%;">_@maxleske_ how long do you need to copy&paste the stuff from dummy plugin to the other ones?</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:58 UTC</span>

<span style="font-size: 90%;">maybe tomorrow is a bit ambitious to fix all the plugins, but I can spend my time usefully on compiling the CHANGES and CONTRIBUTORS files.</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:00:20 UTC</span>

<span style="font-size: 90%;">Two evenings maybe, so Wednesday or Thursday</span>

**walter** <span style="color: grey; font-size: 90%;">20:00:22 UTC</span>

<span style="font-size: 90%;">I think we also need to blog extensively about how plugins work, so it might be a little too much on my plate for tomorrow.</span>

**walter** <span style="color: grey; font-size: 90%;">20:01:05 UTC</span>

<span style="font-size: 90%;">two evenings sound fair!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:33 UTC</span>

<span style="font-size: 90%;">You mean these blogs need to go out before RC1?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:43 UTC</span>

<span style="font-size: 90%;">Why are existing blogs + /docs not enough?</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:16 UTC</span>

<span style="font-size: 90%;">They might be enough, but I think it deserves some special attention in the RC1 blog.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:02:40 UTC</span>

<span style="font-size: 90%;">Ah, get it. You mean an RC1 blog that does a decent job introducing plugins.</span>

**walter** <span style="color: grey; font-size: 90%;">20:02:42 UTC</span>

<span style="font-size: 90%;">But you’re right, the documentation is already quite good and we could point there.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:01 UTC</span>

<span style="font-size: 90%;">Now my only problem is my Friday is super full</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:08 UTC</span>

<span style="font-size: 90%;">I could do a RC1 release on Monday.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:38 UTC</span>

<span style="font-size: 90%;">Meanwhile we might have already addressed some plugin issues so I’m not feeling too bad about this</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:45 UTC</span>

<span style="font-size: 90%;">OK.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:53 UTC</span>

<span style="font-size: 90%;">RC1 on Monday seems fair.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:09 UTC</span>

<span style="font-size: 90%;">Great I will reserve that day</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:10 UTC</span>

<span style="font-size: 90%;">It's all taking longer than expected, but it's also getting better than expected.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:24 UTC</span>

<span style="font-size: 90%;">exactly :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:04:33 UTC</span>

<span style="font-size: 90%;">That points to a release in June and I think that would be cool.</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:15 UTC</span>

<span style="font-size: 90%;">Alright!</span>

**walter** <span style="color: grey; font-size: 90%;">20:05:25 UTC</span>

<span style="font-size: 90%;">Then I think we’re good to go for tonight :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:05:38 UTC</span>

<span style="font-size: 90%;">:zzz:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:39 UTC</span>

<span style="font-size: 90%;">I agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:43 UTC</span>

<span style="font-size: 90%;">And I have work to do. :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:01 UTC</span>

<span style="font-size: 90%;">_@maxleske_ I'll ping you when I'm done.</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:14 UTC</span>

<span style="font-size: 90%;">I pinned the notes for today with the todos: [https://github.com/coreruleset/coreruleset/issues/2499](https://github.com/coreruleset/coreruleset/issues/2499)</span>

**maxleske** <span style="color: grey; font-size: 90%;">20:06:23 UTC</span>

<span style="font-size: 90%;">Thanks Walter!
Good night everyone.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:07:09 UTC</span>

<span style="font-size: 90%;">Good night :star2:</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:27 UTC</span>

<span style="font-size: 90%;">good night and thanks everyone :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:30 UTC</span>

<span style="font-size: 90%;">Thank you all and good night!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:07:34 UTC</span>

<span style="font-size: 90%;">Do we need to carry over any outstanding tasks from [https://github.com/coreruleset/coreruleset/issues/2491](https://github.com/coreruleset/coreruleset/issues/2491)?</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:41 UTC</span>

<span style="font-size: 90%;">I did that</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:52 UTC</span>

<span style="font-size: 90%;">o no I didn’t, but I will</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:08:16 UTC</span>

<span style="font-size: 90%;">Night!</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:47 UTC</span>

<span style="font-size: 90%;">bye bye!</span>

