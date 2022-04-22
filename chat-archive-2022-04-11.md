### Mon, Apr 11th, 2022

**walter** <span style="color: grey; font-size: 90%;">18:31:39 UTC</span>

<span style="font-size: 90%;">Hello, hello! I am wondering who is here on this irregular “pre-RC1” meet!</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:32:07 UTC</span>

<span style="font-size: 90%;">hey</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:14 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**walter** <span style="color: grey; font-size: 90%;">18:32:30 UTC</span>

<span style="font-size: 90%;">Christian could not make it so I will be the host. Sadly I was sick for a few days so I didn’t prepare that well. There was a lot of activity. So, I think I will make a quick agenda on GitHub. OK?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:10 UTC</span>

<span style="font-size: 90%;">Sure!</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:08 UTC</span>

<span style="font-size: 90%;">Here it is! [https://github.com/coreruleset/coreruleset/issues/2491](https://github.com/coreruleset/coreruleset/issues/2491)</span>

**walter** <span style="color: grey; font-size: 90%;">18:34:49 UTC</span>

<span style="font-size: 90%;">I think we can go fast with the first few ones.</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:20 UTC</span>

<span style="font-size: 90%;">First, [#2417](https://github.com/coreruleset/coreruleset/issues/#2417) is merged :partying_face: after some amazing work. So, that’s 1-nil!</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:35 UTC</span>

<span style="font-size: 90%;">The second question, is [Refactor scoring variables #2417](https://github.com/coreruleset/coreruleset/pull/2417) tested on coraza?</span>

**walter** <span style="color: grey; font-size: 90%;">18:35:40 UTC</span>

<span style="font-size: 90%;">Did anyone manage to do that?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:06 UTC</span>

<span style="font-size: 90%;">_@jptosso_?</span>

**walter** <span style="color: grey; font-size: 90%;">18:37:30 UTC</span>

<span style="font-size: 90%;">If we didn’t get to it, I would say it’s not a blocker. It can be tested on Coraza during the RC1 period. But we have to keep in mind to run it on Coraza. If we don’t have the resources (sadly I’m not running Coraza yet) _@jptosso_ might like to test it and he can take a little time during RC1.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:37:49 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:37:59 UTC</span>

<span style="font-size: 90%;">Sounds reasonable!</span>

**jptosso** <span style="color: grey; font-size: 90%;">18:38:04 UTC</span>

<span style="font-size: 90%;">Don't worry we are running crs tests this week </span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:43:16 UTC</span>

<span style="font-size: 90%;">May be I'll finish the new release of ftwrunner, which will supports coraza engine...</span>

**walter** <span style="color: grey; font-size: 90%;">18:38:51 UTC</span>

<span style="font-size: 90%;">Awesome! We will treat it not as a blocker for publishing RC1, but will consider the compatibility a must for the final release.</span>

**walter** <span style="color: grey; font-size: 90%;">18:40:51 UTC</span>

<span style="font-size: 90%;">OK next one! Is [https://github.com/coreruleset/coreruleset/pull/2349](https://github.com/coreruleset/coreruleset/pull/2349) ready? Yes, it is! :partying_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:16 UTC</span>

<span style="font-size: 90%;">On to the next one: PR to remove DoS rules from base? [Remove RE packages and DoS rules (move to plugins) #2469](https://github.com/coreruleset/coreruleset/pull/2469)</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:19 UTC</span>

<span style="font-size: 90%;">Yes. No negative reports so far :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:41:55 UTC</span>

<span style="font-size: 90%;">And also this is merged! :partying_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:41:56 UTC</span>

<span style="font-size: 90%;">Did it, accidentally broke it, fixed it, then merged it. = Done.</span>

**walter** <span style="color: grey; font-size: 90%;">18:42:35 UTC</span>

<span style="font-size: 90%;">Then the next point (I’m trying to make this a fast meet) - plugins ready? I confess I have not followed this process closely.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:09 UTC</span>

<span style="font-size: 90%;">All plugins were finished last week. Then the issue about enabling/disabling plugins came up.</span>

**airween** <span style="color: grey; font-size: 90%;">18:43:16 UTC</span>

<span style="font-size: 90%;">May be I'll finish the new release of ftwrunner, which will supports coraza engine...</span>

↳ **airween** <span style="color: grey; font-size: 90%;">18:43:16 UTC</span>

<span style="font-size: 90%;">May be I'll finish the new release of ftwrunner, which will supports coraza engine...</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:20 UTC</span>

<span style="font-size: 90%;">When I looked at the repo, I see that the exclusion packages are gone, but I did not have the time to test the plugins. But that can be done during RC1.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:21 UTC</span>

<span style="font-size: 90%;">I think all plugins need reworking now…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:43:47 UTC</span>

<span style="font-size: 90%;">Hello everyone</span>

**walter** <span style="color: grey; font-size: 90%;">18:43:48 UTC</span>

<span style="font-size: 90%;">I was afraid of that too. But I think it’s the right call to allow them to be disabled (and then re-enabled) to use them in a razor sharp fashion.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:03 UTC</span>

<span style="font-size: 90%;">There are also some plugins that still need testing. But that's not urgent</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:13 UTC</span>

<span style="font-size: 90%;">And I think we should fix the plugins before releasing the RC1.</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:16 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:43 UTC</span>

<span style="font-size: 90%;">It should not be difficult work…</span>

**walter** <span style="color: grey; font-size: 90%;">18:44:46 UTC</span>

<span style="font-size: 90%;">I can help</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:51 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ Made a valid point earlier: anyone who currently relies on RE packages being enabled/disabled cannot test RC1 currently.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:44:54 UTC</span>

<span style="font-size: 90%;">_@theMiddle_ had some concerns about that</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:45:13 UTC</span>

<span style="font-size: 90%;">me too, enable/disable via variable for me it's really important</span>

**walter** <span style="color: grey; font-size: 90%;">18:45:27 UTC</span>

<span style="font-size: 90%;">Yes for me too…</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:38 UTC</span>

<span style="font-size: 90%;">Do we have an exact plan/instructions on how to fix the plugins?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:45:44 UTC</span>

<span style="font-size: 90%;">Or is that conversation still ongoing?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:45:55 UTC</span>

<span style="font-size: 90%;">Which plugins are that?
</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:46:33 UTC</span>

<span style="font-size: 90%;">(we don't have to do all of them for RC1, just the ones that had original RE)</span>

**walter** <span style="color: grey; font-size: 90%;">18:46:47 UTC</span>

<span style="font-size: 90%;">I don’t know if we have an issue about that, but we could come up with a proposal now, then have a day for others to comment on it, then implement it, then release the RC1 a few days later…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:47:02 UTC</span>

<span style="font-size: 90%;">The exclusion one for me are vital and the dummy plugin seems to implement the enable/disable correctly</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:47:09 UTC</span>

<span style="font-size: 90%;">I think all of these ones need reworking:</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:20 UTC</span>

<span style="font-size: 90%;">agreed</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:41 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/dummy-plugin/blob/main/plugins/dummy-after.conf](https://github.com/coreruleset/dummy-plugin/blob/main/plugins/dummy-after.conf)</span>

**walter** <span style="color: grey; font-size: 90%;">18:47:47 UTC</span>

<span style="font-size: 90%;">Here is an example of the dummy plugin.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:47:51 UTC</span>

<span style="font-size: 90%;">I don't think we need DoS for v3 yet</span>

**walter** <span style="color: grey; font-size: 90%;">18:48:13 UTC</span>

<span style="font-size: 90%;">I’m not sure I love it that much.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:48:27 UTC</span>

<span style="font-size: 90%;">Also IP reputation plugin? Is that a thing now?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:48:35 UTC</span>

<span style="font-size: 90%;">I guess that will also need this new system.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:48:54 UTC</span>

<span style="font-size: 90%;">Oh right. There's a whole other discussion going on there.</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:08 UTC</span>

<span style="font-size: 90%;">I am coming from a different angle than _@theMiddle_ I think. I think, if you put a plugin in the directory, it should self-enable, UNLESS you disable it. In my opinion, this gives the least stress and work for the administrator, while still giving the option to selectively use the plugins.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:49:31 UTC</span>

<span style="font-size: 90%;">Agree</span>

**walter** <span style="color: grey; font-size: 90%;">18:49:46 UTC</span>

<span style="font-size: 90%;">So I was thinking more like, SecRule TX:dummy_plugin_enabled "@eq 0" -> skip</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:49:52 UTC</span>

<span style="font-size: 90%;">But I usually disable all by default in all config and enable only what I need</span>

**walter** <span style="color: grey; font-size: 90%;">18:50:39 UTC</span>

<span style="font-size: 90%;">What do you think?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:46 UTC</span>

<span style="font-size: 90%;">Which would also work.</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:03 UTC</span>

<span style="font-size: 90%;">There are multiple scenarios I can think of:
</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:54:35 UTC</span>

<span style="font-size: 90%;">A plugin is enabled unless it’s explicitly disabled. (Easy installing, but tweaking is possible)That makes the most sense, right? Because you have to explicitly download the plugin and symlink/copy the files into place, so you know it's there: it won't be a surprise if it's enabled by default, you put the files there manually.</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">18:57:43 UTC</span>

<span style="font-size: 90%;">That's also true, if you download the plugin you are going to enable it somewhere, maybe not always true if you have many different websites on the same setup</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:56:09 UTC</span>

<span style="font-size: 90%;">I'm wondering if we should make upgrading to 3.4 less disruptive by including the right configuration to enable exlusions on setup conf as for the current version. IDK if this could help users or not</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:59 UTC</span>

<span style="font-size: 90%;">If we do option 2 it will be just like that: automatic enablement (but people have to download the exclusion plugins).</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:57:43 UTC</span>

<span style="font-size: 90%;">That's also true, if you download the plugin you are going to enable it somewhere, maybe not always true if you have many different websites on the same setup</span>

↳ **theMiddle** <span style="color: grey; font-size: 90%;">18:57:43 UTC</span>

<span style="font-size: 90%;">That's also true, if you download the plugin you are going to enable it somewhere, maybe not always true if you have many different websites on the same setup</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:59:56 UTC</span>

<span style="font-size: 90%;">I think we have to make a decision. I suggest that we go for option 2, as is currently planned, unless any of you explicitly veto and feel this needs more work.</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:14 UTC</span>

<span style="font-size: 90%;">I don’t think we have any haters for option 2 so I suggest we do it like this!</span>

**walter** <span style="color: grey; font-size: 90%;">19:00:53 UTC</span>

<span style="font-size: 90%;">Any opinions about the variable name? The dummy plugin now has TX:dummy-plugin_enabled which has a - and a _. I think I’d prefer: TX:dummy_plugin_enabled as we do with our other variables.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:01:30 UTC</span>

<span style="font-size: 90%;">Ah, I think I see the reason for that:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:02:15 UTC</span>

<span style="font-size: 90%;">That's taking the form "plugin-name_enabled", and currently all plugins are hyphenated, e.g., dos-protection-modsecurity-v2, wordpress-rule-exclusions, etc.</span>

**walter** <span style="color: grey; font-size: 90%;">19:02:31 UTC</span>

<span style="font-size: 90%;">ahhh</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:39 UTC</span>

<span style="font-size: 90%;">good point. That would enable some scripting</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:05 UTC</span>

<span style="font-size: 90%;">yes good point</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:28 UTC</span>

<span style="font-size: 90%;">otherwise, we could also just set TX:dummy-plugin 0/1</span>

**walter** <span style="color: grey; font-size: 90%;">19:03:41 UTC</span>

<span style="font-size: 90%;">but maybe that is less clear</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:00 UTC</span>

<span style="font-size: 90%;">what am I doing? am I disabling it, enabling it? no, scratch that</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:13 UTC</span>

<span style="font-size: 90%;">It's less clear. We also don't know whether we'll want to introduce additional vars in the future, then the namespacing would come in handy</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:51 UTC</span>

<span style="font-size: 90%;">alright. shall we leave it like this, then? TX:dummy-plugin_enabled</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:04 UTC</span>

<span style="font-size: 90%;">Agree but mixing dash and underscore also triggers me :joy:</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:11 UTC</span>

<span style="font-size: 90%;">yeah I know right :sob:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:20 UTC</span>

<span style="font-size: 90%;">Ok for me btw</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:05:36 UTC</span>

<span style="font-size: 90%;">dummy-PLUGIN_Enabled</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:05:44 UTC</span>

<span style="font-size: 90%;">(Sorry :stuck_out_tongue: )</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:05:44 UTC</span>

<span style="font-size: 90%;">Lol</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:47 UTC</span>

<span style="font-size: 90%;">aaaa</span>

**walter** <span style="color: grey; font-size: 90%;">19:06:59 UTC</span>

<span style="font-size: 90%;">Ok, let’s stick to the current format then. We just have to inverse the skip logic. If the variable is unset, or 1, or anything, the plugin runs. If the variable is 0, the plugin skips.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:07:44 UTC</span>

<span style="font-size: 90%;">I hope that users will read the documentation and they don't expect to have exclusions as is</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:07:54 UTC</span>

<span style="font-size: 90%;">? Isn't that how it works now?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:03 UTC</span>

<span style="font-size: 90%;">More or less</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:25 UTC</span>

<span style="font-size: 90%;">i mean, now you don't need to download anything else that the crs</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:28 UTC</span>

<span style="font-size: 90%;">right now the exclusions are disabled by default..</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:53 UTC</span>

<span style="font-size: 90%;">but we should definitely put a little prose in crs-setup.conf where the exclusions used to be. I will note this as a todo.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:09:31 UTC</span>

<span style="font-size: 90%;">Agree on having a comment at the same position of the current exclusion config</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:01 UTC</span>

<span style="font-size: 90%;">I’ll do that</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:07 UTC</span>

<span style="font-size: 90%;">now a big question…</span>

**walter** <span style="color: grey; font-size: 90%;">19:11:19 UTC</span>

<span style="font-size: 90%;">do you know of any blockers that would warrant shifting the RC1 (a few days) into the future so we can fix them before unleashing them on the testers?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:11:37 UTC</span>

<span style="font-size: 90%;">I think this needs resolution:
[https://github.com/coreruleset/coreruleset/pull/2488](https://github.com/coreruleset/coreruleset/pull/2488)</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:03 UTC</span>

<span style="font-size: 90%;">I just need some guidance on what the new default reporting level will be, now that we've introduced 6 levels of reporting.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:34 UTC</span>

<span style="font-size: 90%;">I made a sensible guess, but I don't think it should be based only on my decision/guess :stuck_out_tongue:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:12 UTC</span>

<span style="font-size: 90%;">I also think this needs a look: [https://github.com/coreruleset/coreruleset/issues/2433](https://github.com/coreruleset/coreruleset/issues/2433)</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:26 UTC</span>

<span style="font-size: 90%;">oh yes, the reputation rules…</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:55 UTC</span>

<span style="font-size: 90%;">they are kind of mixed up with our own counter, several external data sources….</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:24 UTC</span>

<span style="font-size: 90%;">If we want to move them, we have to do it now or wait til the next major release</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:42 UTC</span>

<span style="font-size: 90%;">yes exactly</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:54 UTC</span>

<span style="font-size: 90%;">I think they belong more in a plugin…</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:22 UTC</span>

<span style="font-size: 90%;">especially because you have to get maxmind DB’s, dnsbl API keys, etc… it’s definitely not something for a default setup</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:31 UTC</span>

<span style="font-size: 90%;">I have personally never used them</span>

**walter** <span style="color: grey; font-size: 90%;">19:17:07 UTC</span>

<span style="font-size: 90%;">but I guess I would have to, if we move them and they’d have to be tested carefully. :D</span>

**walter** <span style="color: grey; font-size: 90%;">19:18:02 UTC</span>

<span style="font-size: 90%;">the DO_REPUT_BLOCK also appears in REQUEST-949… I wonder if we can even cleanly cut that out of there…</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:18:04 UTC</span>

<span style="font-size: 90%;">On the other hand, we could leave it for the next major release and gain more experience with how the plugin infrastructure works...</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:21 UTC</span>

<span style="font-size: 90%;">What's the outstanding action needed here?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:26 UTC</span>

<span style="font-size: 90%;">Is it just to approve [https://github.com/coreruleset/coreruleset/pull/2483](https://github.com/coreruleset/coreruleset/pull/2483) ?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:18:36 UTC</span>

<span style="font-size: 90%;">That should be simple enough to do.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:19:14 UTC</span>

<span style="font-size: 90%;">The philosophical discussion about how many plugins to split it into is valid, but doesn't stop us approving and merging this PR.</span>

**walter** <span style="color: grey; font-size: 90%;">19:19:21 UTC</span>

<span style="font-size: 90%;">I think this is a sensible comment
[dune73](https://github.com/dune73) commented [yesterday](https://github.com/coreruleset/coreruleset/pull/2483#issuecomment-1094216762)
I’d opt to remove both and create two separate plugins. As it happens I started to re-visit GeoIP for ModSec2 again, namely because MaxMind is chanding free access to their databases etc.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:19:29 UTC</span>

<span style="font-size: 90%;">The whole thing needs testing. And also some decisions on how to block from plugins, e.g. early blocking versus hard blocking from plugins</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:19:56 UTC</span>

<span style="font-size: 90%;">"[dune73](https://github.com/dune73)  commented [21 hours ago](https://github.com/coreruleset/coreruleset/pull/2483#issuecomment-1094378558)
    Ready to merge this one here?"
[studersi](https://github.com/studersi)  commented [13 hours ago](https://github.com/coreruleset/coreruleset/pull/2483#issuecomment-1094595594)
    Rebased to fix conflicts.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:20:03 UTC</span>

<span style="font-size: 90%;">It seems ready to review and merge, though, no?</span>

**walter** <span style="color: grey; font-size: 90%;">19:20:58 UTC</span>

<span style="font-size: 90%;">True! I can do that. And it’s true, we could initially release without those plugins, and then finish them later.</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:10 UTC</span>

<span style="font-size: 90%;">People really dependent on them would have to wait a little bit before upgrading.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:34 UTC</span>

<span style="font-size: 90%;">_@theMiddle_? Would that include you?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:22:16 UTC</span>

<span style="font-size: 90%;">nope and agree with dune on maxmind</span>

**walter** <span style="color: grey; font-size: 90%;">19:23:42 UTC</span>

<span style="font-size: 90%;">maybe we even finish the plugins before 4.0 final release…</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:16 UTC</span>

<span style="font-size: 90%;">but for now, I’ve moved it to “Todo after release”</span>

**walter** <span style="color: grey; font-size: 90%;">19:24:45 UTC</span>

<span style="font-size: 90%;">Alright, I’m merging the removal of the reputation rules :slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:00 UTC</span>

<span style="font-size: 90%;">Let's get back to the issue _@xanadu_ pointed out</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:05 UTC</span>

<span style="font-size: 90%;">yes please</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:26:19 UTC</span>

<span style="font-size: 90%;">I've taken a look. It looks good to me but I don't have any opinion on the change and I haven't tested it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:27:04 UTC</span>

<span style="font-size: 90%;">[#2488](https://github.com/coreruleset/coreruleset/issues/#2488)?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:27:17 UTC</span>

<span style="font-size: 90%;">yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:38 UTC</span>

<span style="font-size: 90%;">It's tricky and time-consuming to test. It took me about an hour.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:27:50 UTC</span>

<span style="font-size: 90%;">But it feels important enough that someone else should probably test it.</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:15 UTC</span>

<span style="font-size: 90%;">I agree. Shall I spend time tomorrow on this?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:22 UTC</span>

<span style="font-size: 90%;">If you have time?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:28:30 UTC</span>

<span style="font-size: 90%;">That would be marvellous, if so.</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:51 UTC</span>

<span style="font-size: 90%;">Well yes I planned to put out the RC1 but I’d rather polish as much as possible before that.</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:03 UTC</span>

<span style="font-size: 90%;">So I will review this tomorrow.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:10 UTC</span>

<span style="font-size: 90%;">Amazing. Thank you.</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:14 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:29:31 UTC</span>

<span style="font-size: 90%;">I wrote my testing commands in the PR notes, which may or may not be helpful.</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:02 UTC</span>

<span style="font-size: 90%;">yes I saw some lovely comments :heart:</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:20 UTC</span>

<span style="font-size: 90%;">I’ll take it for a spin. Ok, let’s see if we have more…</span>

**walter** <span style="color: grey; font-size: 90%;">19:30:54 UTC</span>

<span style="font-size: 90%;">I think not, as far as I’m aware. Just, we have to adapt the plugins to allow disabling.</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:11 UTC</span>

<span style="font-size: 90%;">I could also spend time tomorrow on this.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:31:37 UTC</span>

<span style="font-size: 90%;">If not, I can take a look at the end of the week (public holiday on Friday in the UK for Easter, maybe elsewhere too?)</span>

**walter** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">Yep, same here, but I’m working anyway</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:31:54 UTC</span>

<span style="font-size: 90%;">Same here</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:17 UTC</span>

<span style="font-size: 90%;">We even have the next Monday off. Do you?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:32:24 UTC</span>

<span style="font-size: 90%;">yeah</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:32:30 UTC</span>

<span style="font-size: 90%;">Here too</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:30 UTC</span>

<span style="font-size: 90%;">Yep :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:13 UTC</span>

<span style="font-size: 90%;">Ok, so it won’t make sense to put out a RC1 and beat on the drums then anyway, because nobody will read it. Reschedule the RC1 to Tue 19 - assuming we have changed all the plugins?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">Sounds good</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:20 UTC</span>

<span style="font-size: 90%;">OK, then the last point on the agenda: are there any PRs we ideally want to include, if reasonably quick?</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:32 UTC</span>

<span style="font-size: 90%;">I saw a fix by azurit for example</span>

**walter** <span style="color: grey; font-size: 90%;">19:35:37 UTC</span>

<span style="font-size: 90%;">[#2490](https://github.com/coreruleset/coreruleset/issues/#2490)</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:07 UTC</span>

<span style="font-size: 90%;">it’s still pending a comment by _@maxleske_</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:23 UTC</span>

<span style="font-size: 90%;">but I would be happy to include it if that is addressed</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:28 UTC</span>

<span style="font-size: 90%;">yes, I think that one is pretty much good to go</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:36:45 UTC</span>

<span style="font-size: 90%;">I'll add it to the milestone</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:37:33 UTC</span>

<span style="font-size: 90%;">I think the rest can wait. We need to make the cut somewhere :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">Agreed.</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:09 UTC</span>

<span style="font-size: 90%;">Okay, I’m out of items! :partying_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:28 UTC</span>

<span style="font-size: 90%;">Oh, there was also a point about all plugins missing CRS copyright notices by accident… I'll get that sorted.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:39 UTC</span>

<span style="font-size: 90%;">(No issue yet, I'll make one.)</span>

**walter** <span style="color: grey; font-size: 90%;">19:38:48 UTC</span>

<span style="font-size: 90%;">Oh nice!</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:03 UTC</span>

<span style="font-size: 90%;">Who will edit all the plugins? I can do it but maybe we can split the work? Start with the dummy plugin first, get comments on it, then pretty much copy-paste it to the other ones?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:40:25 UTC</span>

<span style="font-size: 90%;">I can help</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:41 UTC</span>

<span style="font-size: 90%;">OK, i’ll put both our names on there and we will sort it out</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:53 UTC</span>

<span style="font-size: 90%;">Then I think we are done for tonight! :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:41:58 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/2491](https://github.com/coreruleset/coreruleset/issues/2491) Here are the notes</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:11 UTC</span>

<span style="font-size: 90%;">Thanks for chairing the meeting!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:12 UTC</span>

<span style="font-size: 90%;">Thanks for managing!</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:32 UTC</span>

<span style="font-size: 90%;">Thanks for developing! :smile:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:42:34 UTC</span>

<span style="font-size: 90%;">Thanks!</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:42:38 UTC</span>

<span style="font-size: 90%;">bb</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:42:44 UTC</span>

<span style="font-size: 90%;">Night.</span>

**walter** <span style="color: grey; font-size: 90%;">19:42:45 UTC</span>

<span style="font-size: 90%;">Speak to you soon.</span>

**Aryeh Berman** <span style="color: grey; font-size: 90%;">20:04:01 UTC</span>

<span style="font-size: 90%;">For ModSecurity-nginx, does the modsecurity_rules_file directive replace all other modsecurity_rules_file directives in a higher scope, or does it override?</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:33 UTC</span>

<span style="font-size: 90%;">_@Aryeh Berman_ as I know it depends where do you put. If you put it into a vhost context (server), then it overrides only for that context.</span>

↳ **Aryeh Berman** <span style="color: grey; font-size: 90%;">20:08:25 UTC</span>

<span style="font-size: 90%;">I have a global modsecurity_rules_file directive in nginx.conf , and then I have another directive in a specific location block. Will that location block use both files, and the second file will override the first one, or does the second directive replace the first one, and any rules that I want for both need to be specified in both?</span>

↳ **Aryeh Berman** <span style="color: grey; font-size: 90%;">20:09:40 UTC</span>

<span style="font-size: 90%;">The global directive points to a regular modsecurity.conf. The one in the location block points to a file that just disables some rules.</span>

↳ **Aryeh Berman** <span style="color: grey; font-size: 90%;">20:10:01 UTC</span>

<span style="font-size: 90%;">Will the rest of the rules still apply to that location?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:10:57 UTC</span>

<span style="font-size: 90%;">I think yes, but I would have to check (but unfortunately now I don't have too much time...)</span>

↳ **Aryeh Berman** <span style="color: grey; font-size: 90%;">20:13:06 UTC</span>

<span style="font-size: 90%;">Ok, thank you.</span>

↳ **airween** <span style="color: grey; font-size: 90%;">20:15:30 UTC</span>

<span style="font-size: 90%;">but be careful wit order of rules and phases. Eg. if you use ctl action to disable an another rule, and that rule activated in phase:2, you can't disable another rule in phase:1</span>

↳ **Aryeh Berman** <span style="color: grey; font-size: 90%;">20:16:09 UTC</span>

<span style="font-size: 90%;">Right. Here I was just using SecRuleRemoveById.</span>

