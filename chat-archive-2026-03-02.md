### Mon, Mar 2nd, 2026

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:02 UTC</span>

<span style="font-size: 90%;">Welcome to our March Monthly chat! :party-crs:</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:13 UTC</span>

<span style="font-size: 90%;">hey-hey!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:30:38 UTC</span>

<span style="font-size: 90%;">hello</span>

**airween** <span style="color: grey; font-size: 90%;">19:30:40 UTC</span>

<span style="font-size: 90%;">How is the weather is Oslo? :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:30:50 UTC</span>

<span style="font-size: 90%;">Cold :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:31:16 UTC</span>

<span style="font-size: 90%;">But people make you feel warm in here :slightly_smiling_face:</span>

**azurit** <span style="color: grey; font-size: 90%;">19:31:28 UTC</span>

<span style="font-size: 90%;">Hi</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:32:19 UTC</span>

<span style="font-size: 90%;">Evening!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:32:55 UTC</span>

<span style="font-size: 90%;">Just one thing before we start with topics: we will be releasing v4.25.0 as our first v4 LTS by end of Month.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:28 UTC</span>

<span style="font-size: 90%;">This is really exciting. We have been working for more than 2 years on releases, and this is going to be a huge milestone.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:33:42 UTC</span>

<span style="font-size: 90%;">Cheers to the team and everyone else around that will make this possible.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:20 UTC</span>

<span style="font-size: 90%;">I'll be posting more information about how/when, and what's next after the release. Exciting times ahead!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:34:47 UTC</span>

<span style="font-size: 90%;">Let's start with our first discussion topic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:35:17 UTC</span>

<span style="font-size: 90%;">FPs increase in [https://github.com/coreruleset/coreruleset/pull/4446](https://github.com/coreruleset/coreruleset/pull/4446)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:37 UTC</span>

<span style="font-size: 90%;">Honestly, we should be able to discuss this in the PR.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:36:38 UTC</span>

<span style="font-size: 90%;">I was talking about this with Esad.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:36:39 UTC</span>

<span style="font-size: 90%;">But anyway.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:02 UTC</span>

<span style="font-size: 90%;">It is clear to me that the `ls` alias with one and two letters might be a problem</span>

**azurit** <span style="color: grey; font-size: 90%;">19:37:05 UTC</span>

<span style="font-size: 90%;">He wanted to be here to discuss it but he was not able to make it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:31 UTC</span>

<span style="font-size: 90%;">Do we know which is the source of the increase?</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:55:12 UTC</span>

<span style="font-size: 90%;">I already mentioned it in the PR, but the issue is that `.*` is used in the evasion prefix, there's already an open issue on this and that's a big reason for the false positive increase. [https://github.com/coreruleset/coreruleset/issues/4356](https://github.com/coreruleset/coreruleset/issues/4356)</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">06:38:44 UTC</span>

<span style="font-size: 90%;">JFYI it looks like the increase was coming from `ll`</span>

### Mon, Mar 2nd, 2026

**fzipitria** <span style="color: grey; font-size: 90%;">19:37:43 UTC</span>

<span style="font-size: 90%;">There are many commands that were added there.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:37:55 UTC</span>

<span style="font-size: 90%;">He was asking to me review and approve this PR but i was not feeling so to decide by my own.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:38:15 UTC</span>

<span style="font-size: 90%;">Honestly, i'm not sure if that FPs increase is or isn't a problem.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:18 UTC</span>

<span style="font-size: 90%;">We aim to never add new natural language FPs at PL1, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:38:21 UTC</span>

<span style="font-size: 90%;">Is it `cargo`? `shred`? Those look like common english words</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:38:23 UTC</span>

<span style="font-size: 90%;">This seems not great</span>

**azurit** <span style="color: grey; font-size: 90%;">19:39:04 UTC</span>

<span style="font-size: 90%;">Yeah. i wasn't ok with that it, too.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:39:54 UTC</span>

<span style="font-size: 90%;">I would say let's get some compromise: we can probably add most of those. But we should be able to take the ones that make FPs.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:40:16 UTC</span>

<span style="font-size: 90%;">I would like to hear an opinion why FP increase is NOT a problem.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:40:26 UTC</span>

<span style="font-size: 90%;">`cargo`, `shred`, `rust` are very basic words to not match everywhere</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:53:03 UTC</span>

<span style="font-size: 90%;">The `shred` and `rust` commands are already excluded at PL-1.</span>

### Mon, Mar 2nd, 2026

**azurit** <span style="color: grey; font-size: 90%;">19:40:29 UTC</span>

<span style="font-size: 90%;">But, probably, only Esad can give us that info.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:40:44 UTC</span>

<span style="font-size: 90%;">He thought that it is not a problem.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:40:58 UTC</span>

<span style="font-size: 90%;">Also, `rust` is not a thing.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:00 UTC</span>

<span style="font-size: 90%;">Anyway</span>

**azurit** <span style="color: grey; font-size: 90%;">19:41:03 UTC</span>

<span style="font-size: 90%;">He said: "The false positive increases should only really be an issue in natural language contexts, so imo real world false positive increase will be pretty low."</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:19 UTC</span>

<span style="font-size: 90%;">Hmmm... no bueno.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:33 UTC</span>

<span style="font-size: 90%;">I would answer in the PR. We'll figure it out</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:41:50 UTC</span>

<span style="font-size: 90%;">Maybe just removing a couple and moving to PL2 would do.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:42:29 UTC</span>

<span style="font-size: 90%;">Also remember this might get into LTS, and people will be basically disabling the rule. ¯\_(ツ)_/¯</span>

**azurit** <span style="color: grey; font-size: 90%;">19:42:51 UTC</span>

<span style="font-size: 90%;">Yeah, does not sounds good.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:01 UTC</span>

<span style="font-size: 90%;">Ok, for the record, I'll handle this one.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:06 UTC</span>

<span style="font-size: 90%;">Next topic</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:43:25 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/nextcloud-rule-exclusions-plugin/issues/146](https://github.com/coreruleset/nextcloud-rule-exclusions-plugin/issues/146) Should we split the Collabora Online rules into it's own plugin?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:44:07 UTC</span>

<span style="font-size: 90%;">Too bad Easd is not here.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:07 UTC</span>

<span style="font-size: 90%;">Who proposed this one?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:09 UTC</span>

<span style="font-size: 90%;">Ah</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:12 UTC</span>

<span style="font-size: 90%;">Ugh</span>

**azurit** <span style="color: grey; font-size: 90%;">19:44:24 UTC</span>

<span style="font-size: 90%;">I cannot decide, first time i hear about that software.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:44:32 UTC</span>

<span style="font-size: 90%;">I would say :blob-yes:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:37 UTC</span>

<span style="font-size: 90%;">Hi there, sorry for being late.</span>

**Craniums** <span style="color: grey; font-size: 90%;">19:45:12 UTC</span>

<span style="font-size: 90%;">Hello sorry to jump in but this seems to be very specific use cases </span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:12 UTC</span>

<span style="font-size: 90%;">If the rules start to pop up, and it is a different branch, maybe it deserves a new plugin.</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:57:02 UTC</span>

<span style="font-size: 90%;">The Nextcloud Plugin is already pretty big with about 125 rule exclusions.</span>

### Mon, Mar 2nd, 2026

**michela** <span style="color: grey; font-size: 90%;">19:45:35 UTC</span>

<span style="font-size: 90%;">Hi! Are there any Collabora exclusions in CRS at present?</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:57:32 UTC</span>

<span style="font-size: 90%;">Not in CRS, but in the Nextcloud Plugin.</span>

### Mon, Mar 2nd, 2026

**fzipitria** <span style="color: grey; font-size: 90%;">19:45:36 UTC</span>

<span style="font-size: 90%;">But then we don't have a rule of thumb on when something can split from a plugin to a different one</span>

**azurit** <span style="color: grey; font-size: 90%;">19:45:58 UTC</span>

<span style="font-size: 90%;">Michela: No.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:46:32 UTC</span>

<span style="font-size: 90%;">Looks like about 9 Collabora rules in the Nextcloud exclusion package currently</span>

**michela** <span style="color: grey; font-size: 90%;">19:46:42 UTC</span>

<span style="font-size: 90%;">Coincidentally, I just actually installed Collabora at our company for internal use. So, this is interesting to me. I have not seen any false-positives with it yet, but we aren't really using it yet.</span>

**michela** <span style="color: grey; font-size: 90%;">19:47:11 UTC</span>

<span style="font-size: 90%;">My opinion is that those exclusions should remain in the Nextcloud plug-in.</span>

**michela** <span style="color: grey; font-size: 90%;">19:47:36 UTC</span>

<span style="font-size: 90%;">My reasoning is that Collabora is a common addition to Nextcloud installations.</span>

**michela** <span style="color: grey; font-size: 90%;">19:48:13 UTC</span>

<span style="font-size: 90%;">Collabora mostly enables users to edit documents in Nextcloud, the same way they can edit Google Drive documents with Google Docs on the web.</span>

**michela** <span style="color: grey; font-size: 90%;">19:48:55 UTC</span>

<span style="font-size: 90%;">Users expect that sort of integration and those features now. So, I reckon most Nextcloud implementations will now also include Collabora.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:49:45 UTC</span>

<span style="font-size: 90%;">Sounds good</span>

**azurit** <span style="color: grey; font-size: 90%;">19:50:13 UTC</span>

<span style="font-size: 90%;">It is possible to just install Nextcloud plugin also for Collabora? Without doing any tweaks or so.</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:58:57 UTC</span>

<span style="font-size: 90%;">It'll work but there are some fairly broad rule-exclusions in the plugin that are only safe for Nextcloud. For instance WebDAV methods are allowed since Nextcloud makes very heavy use of it across multiple URL paths.</span>

### Mon, Mar 2nd, 2026

**azurit** <span style="color: grey; font-size: 90%;">19:50:17 UTC</span>

<span style="font-size: 90%;">Will it work?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:50:42 UTC</span>

<span style="font-size: 90%;">Also, won't nextcloud work also for owncloud?</span>

##### Tue, Mar 3rd, 2026

↳ **unknown user** <span style="color: grey; font-size: 90%;">04:59:47 UTC</span>

<span style="font-size: 90%;">It might, but they're both taking very different paths so I imagine not for long especially with their recent rewrite.</span>

### Mon, Mar 2nd, 2026

**azurit** <span style="color: grey; font-size: 90%;">19:50:53 UTC</span>

<span style="font-size: 90%;">Probably.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:50:59 UTC</span>

<span style="font-size: 90%;">But not sure.</span>

**michela** <span style="color: grey; font-size: 90%;">19:51:10 UTC</span>

<span style="font-size: 90%;">I'm sure it would, yah? That would result in having some additional exclusions that are potentially not required for Collabora to run, but they will not inhibit it's operation.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:51:37 UTC</span>

<span style="font-size: 90%;">The unnecessary extra exclusions would also likely be for non-existent locations, so shouldn't be a security risk, I guess</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:51:47 UTC</span>

<span style="font-size: 90%;">(Probably)</span>

**michela** <span style="color: grey; font-size: 90%;">19:51:51 UTC</span>

<span style="font-size: 90%;">yah.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:52:04 UTC</span>

<span style="font-size: 90%;">I agree it does not looks like a problem.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:05 UTC</span>

<span style="font-size: 90%;">So then... we keep Collabora now with nextcloud?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:52:30 UTC</span>

<span style="font-size: 90%;">Perfect.</span>

**michela** <span style="color: grey; font-size: 90%;">19:52:50 UTC</span>

<span style="font-size: 90%;">I imagine that the Nextcloud exclusions would also work with Owncloud. They are similar, though if I remember correctly, Nextcloud is a hard fork of Owncloud. So, those running Owncloud may need to do additional testing and exclusion-writing.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:53:19 UTC</span>

<span style="font-size: 90%;">My opinion: If our Nextcloud plugin works also for Collabora (with some mild side effects, like few unneeded exclusions without any security risk) then i recommned to NOT split it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:54:47 UTC</span>

<span style="font-size: 90%;">For the record: we keep Colalbora with nextcloud for the time being.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:55:25 UTC</span>

<span style="font-size: 90%;">One thing.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:56:01 UTC</span>

<span style="font-size: 90%;">If we go the way i described then, maybe, we should somehow let Collabora users know that they should use our Nextcloud plugin.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:56:18 UTC</span>

<span style="font-size: 90%;">Let's add that to the readme then</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:56:30 UTC</span>

<span style="font-size: 90%;">Can you followup on that _@azurit_?</span>

↳ **azurit** <span style="color: grey; font-size: 90%;">19:56:41 UTC</span>

<span style="font-size: 90%;">Sure.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:57:08 UTC</span>

<span style="font-size: 90%;">Thx</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:56:33 UTC</span>

<span style="font-size: 90%;">IDK why we put this issue [https://github.com/coreruleset/coreruleset/issues/4502](https://github.com/coreruleset/coreruleset/issues/4502) for discussing. Can we do it in the issue itself?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:57:32 UTC</span>

<span style="font-size: 90%;">I would say [https://github.com/coreruleset/coreruleset/issues/4440](https://github.com/coreruleset/coreruleset/issues/4440) is the last thing to discuss</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:04 UTC</span>

<span style="font-size: 90%;">To me, this is basically adding a new dimension to CRS. It would make a discussion for v5</span>

**azurit** <span style="color: grey; font-size: 90%;">19:58:05 UTC</span>

<span style="font-size: 90%;">Is airween online?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:58:15 UTC</span>

<span style="font-size: 90%;">Regarding [#4502](https://github.com/coreruleset/coreruleset/issues/#4502).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:58:18 UTC</span>

<span style="font-size: 90%;">ping _@airween_</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:26 UTC</span>

<span style="font-size: 90%;">yep</span>

**airween** <span style="color: grey; font-size: 90%;">19:58:57 UTC</span>

<span style="font-size: 90%;">I just added the issue because I'm the duty - the mentioned PR is merged, and generated FP's</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:59:32 UTC</span>

<span style="font-size: 90%;">Is it a bug in the modified regex?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:59:35 UTC</span>

<span style="font-size: 90%;">We should discuss it.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:00:42 UTC</span>

<span style="font-size: 90%;">Just a note: Guy is running on PL2.</span>

**airween** <span style="color: grey; font-size: 90%;">20:00:55 UTC</span>

<span style="font-size: 90%;">_@xanadu_ probably yes, see the report's log:
[msg "Detects MySQL comment-/space-obfuscated injections and backtick termination"] [data "Matched Data: , like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Googlebot/2.1;  [http://www.google.com/bot.html](http://www.google.com/bot.html)) found within REQUEST_HEADERS:User-Agent:</span>

**azurit** <span style="color: grey; font-size: 90%;">20:01:41 UTC</span>

<span style="font-size: 90%;">`(KHTML, like Gecko)`</span>

**azurit** <span style="color: grey; font-size: 90%;">20:02:57 UTC</span>

<span style="font-size: 90%;">Should not trigger.</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:32 UTC</span>

<span style="font-size: 90%;">[https://regex101.com/r/f2GzP7/1](https://regex101.com/r/f2GzP7/1)</span>

**azurit** <span style="color: grey; font-size: 90%;">20:03:42 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:03:45 UTC</span>

<span style="font-size: 90%;">:sweat_smile:</span>

**airween** <span style="color: grey; font-size: 90%;">20:03:56 UTC</span>

<span style="font-size: 90%;">okay, _@xanadu_ won :stuck_out_tongue:</span>

**Craniums** <span style="color: grey; font-size: 90%;">20:04:16 UTC</span>

<span style="font-size: 90%;">:joy::joy:</span>

**azurit** <span style="color: grey; font-size: 90%;">20:04:31 UTC</span>

<span style="font-size: 90%;">What about regex before [#4476](https://github.com/coreruleset/coreruleset/issues/#4476) ?</span>

**airween** <span style="color: grey; font-size: 90%;">20:05:13 UTC</span>

<span style="font-size: 90%;">let me check</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:01 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121#diff-ffff196fd301a0b25ec989[…]d88f24c6c31267ea2b8ed24L834](https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121#diff-ffff196fd301a0b25ec989e607586c033a21de733d88f24c6c31267ea2b8ed24L834)</span>

**airween** <span style="color: grey; font-size: 90%;">20:06:39 UTC</span>

<span style="font-size: 90%;">old:
(?i),.*?[\"'\)0-9`-f][\"'`](?:[\"'`].*?[\"'`]|(?:\r?\n)?\z|[^\"'`]+)|[^0-9A-Z_a-z]select.+[^0-9A-Z_a-z]*?from|(?:alter|(?:(?:cre|trunc|upd)at|renam)e|d(?:e(?:lete|sc)|rop)|(?:inser|selec)t|load)[\s\x0b]*?\([\s\x0b]*?space[\s\x0b]*?\(new:
(?i),.*?(?:[\)0-9a-f](?:$|[\"'`](?:$|[^\"'`]+[\"'`])|(?:\r?\n)?\z)|[\"'`][^\"'`]+[\"'`])|[^0-9A-Z_a-z]select.+[^0-9A-Z_a-z]*?from|(?:alter|(?:(?:cre|trunc|upd)at|renam)e|d(?:e(?:lete|sc)|rop)|(?:inser|selec)t|load)[\s\x0b]*?\([\s\x0b]*?space[\s\x0b]*?\(</span>

**azurit** <span style="color: grey; font-size: 90%;">20:07:33 UTC</span>

<span style="font-size: 90%;">Yes, it does not match that UA header.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:07:39 UTC</span>

<span style="font-size: 90%;">(the old one)</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:25 UTC</span>

<span style="font-size: 90%;">here is the `.ra` file's diff:
[https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121](https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121)</span>

**azurit** <span style="color: grey; font-size: 90%;">20:08:41 UTC</span>

<span style="font-size: 90%;">We should not block Google bot on PL2.</span>

**airween** <span style="color: grey; font-size: 90%;">20:08:49 UTC</span>

<span style="font-size: 90%;">yeah'</span>

**airween** <span style="color: grey; font-size: 90%;">20:09:30 UTC</span>

<span style="font-size: 90%;">perhaps this line causes the problem?
[https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121#diff-7a163d318c5edc8bcb7f08[…]211ded9f3fdedcc6f592R16-R17](https://github.com/coreruleset/coreruleset/commit/6f855a42169ae1f4f94c708d7e36e4ee88930121#diff-7a163d318c5edc8bcb7f0889083a6b80c158cefa1cb3211ded9f3fdedcc6f592R16-R17)</span>

**airween** <span style="color: grey; font-size: 90%;">20:10:01 UTC</span>

<span style="font-size: 90%;">`,.*?`</span>

**azurit** <span style="color: grey; font-size: 90%;">20:11:46 UTC</span>

<span style="font-size: 90%;">That line is a comment.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:11:56 UTC</span>

<span style="font-size: 90%;">AH, not, sorry.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:13:08 UTC</span>

<span style="font-size: 90%;">Here is the change: [https://github.com/coreruleset/coreruleset/pull/4476/changes#diff-7a163d318c5edc8bcb7f0889083a6b80c158cefa1cb3211ded9f3fdedcc6f592L7](https://github.com/coreruleset/coreruleset/pull/4476/changes#diff-7a163d318c5edc8bcb7f0889083a6b80c158cefa1cb3211ded9f3fdedcc6f592L7)</span>

**azurit** <span style="color: grey; font-size: 90%;">20:14:20 UTC</span>

<span style="font-size: 90%;">This is a tough one. It needs to be deeply analyzed.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:14:58 UTC</span>

<span style="font-size: 90%;">Or we need more info from theseion.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:15:31 UTC</span>

<span style="font-size: 90%;">Good one</span>

**azurit** <span style="color: grey; font-size: 90%;">20:16:33 UTC</span>

<span style="font-size: 90%;">But i agree that there is probably an issue which needs to be fixed before LTS.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:17:43 UTC</span>

<span style="font-size: 90%;">Can we tag it somehow so we will look at it before LTS? So we can continue with other issues.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:17:59 UTC</span>

<span style="font-size: 90%;">I can have a look at it this week. I'll self-assign the issue.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:19:22 UTC</span>

<span style="font-size: 90%;">So, we have this last one: [https://github.com/coreruleset/coreruleset/issues/4440](https://github.com/coreruleset/coreruleset/issues/4440)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:10 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">20:20:15 UTC</span>

<span style="font-size: 90%;">I'm semi afk</span>

**azurit** <span style="color: grey; font-size: 90%;">20:20:49 UTC</span>

<span style="font-size: 90%;">What do you, guys and girls, think about it?</span>

**michela** <span style="color: grey; font-size: 90%;">20:21:44 UTC</span>

<span style="font-size: 90%;">I think we should not add this new score type.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:21:58 UTC</span>

<span style="font-size: 90%;">I haven't had time to read all of the replies in the thread… but, if a rule is "definitely an attack" then it should be set to `deny` and not anomaly_score=+25 :shrug:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:22:21 UTC</span>

<span style="font-size: 90%;">And it's different from 1 app to another. If it's "definitely an attack" for me, maybe for your app it's not</span>

**michela** <span style="color: grey; font-size: 90%;">20:23:15 UTC</span>

<span style="font-size: 90%;">True.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:23:23 UTC</span>

<span style="font-size: 90%;">_@xanadu_ You are right - it does not have sense to raise score as providers will just 'adapt' to it (in bad sense). If we really want to force something to be blocked, then we should use a 'deny' action, or similar. But i don't think we want to force anything like this.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:24:17 UTC</span>

<span style="font-size: 90%;">So, my suggestion is to deny that PR.</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:25:34 UTC</span>

<span style="font-size: 90%;">The idea is interesting, but maybe the timing and implementation isn't quite right.</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:24 UTC</span>

<span style="font-size: 90%;">wait, is there any implementation? I thought it's just an issue...</span>

**michela** <span style="color: grey; font-size: 90%;">20:26:42 UTC</span>

<span style="font-size: 90%;">One of the points I made in the PR, in addition to that this score could easily be worked around, is that CRS can already do everything that the writer of the PR would like the new score mechanism to do</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:26:43 UTC</span>

<span style="font-size: 90%;">*suggested implementation</span>

**azurit** <span style="color: grey; font-size: 90%;">20:26:45 UTC</span>

<span style="font-size: 90%;">Sorry, it's just an issue/idea.</span>

**airween** <span style="color: grey; font-size: 90%;">20:26:51 UTC</span>

<span style="font-size: 90%;">ah, okay, thanks</span>

**michela** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">It appears to me that this adds complexity without tangible benefit.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:27:58 UTC</span>

<span style="font-size: 90%;">I believe it will make things [worse](https://github.com/coreruleset/coreruleset/issues/4440#issuecomment-3848363828).</span>

**airween** <span style="color: grey; font-size: 90%;">20:28:05 UTC</span>

<span style="font-size: 90%;">so our decision is that we don't want to add this feature and close the issue, right?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:29:39 UTC</span>

<span style="font-size: 90%;">The fundamental idea to change rule scoring to have "very very bad, almost certainly an attack" is interesting. But maybe things like protocol rules would be more appropriate :thinking_face:</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:29:47 UTC</span>

<span style="font-size: 90%;">E.g. "Invalid HTTP Request Line" can never be good…</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:29:56 UTC</span>

<span style="font-size: 90%;">But maybe a v5 thing as mentioned already</span>

**michela** <span style="color: grey; font-size: 90%;">20:30:39 UTC</span>

<span style="font-size: 90%;">Well, in those cases, couldn't the anomaly score be adjusted to reflect such a threat?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:30:59 UTC</span>

<span style="font-size: 90%;">Sure</span>

**azurit** <span style="color: grey; font-size: 90%;">20:31:00 UTC</span>

<span style="font-size: 90%;">What do you mean?</span>

**azurit** <span style="color: grey; font-size: 90%;">20:31:05 UTC</span>

<span style="font-size: 90%;">Adjusted how?</span>

**michela** <span style="color: grey; font-size: 90%;">20:33:00 UTC</span>

<span style="font-size: 90%;">I don't know how much we need to discuss further, as we've already made our decision but if it is widely believed that a rule has zero false-positive risk, then I suppose we could cause it to be blocked in other ways, without adding a new scoring mechanism.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:33:03 UTC</span>

<span style="font-size: 90%;">The only situations i see to be suitable for `deny`  or similar action are, for example, blocking of a specific CVE.</span>

**michela** <span style="color: grey; font-size: 90%;">20:33:55 UTC</span>

<span style="font-size: 90%;">I think my point still stands then. haha</span>

**azurit** <span style="color: grey; font-size: 90%;">20:34:12 UTC</span>

<span style="font-size: 90%;">But it's a little out of scope or CRS i think.</span>

**azurit** <span style="color: grey; font-size: 90%;">20:34:25 UTC</span>

<span style="font-size: 90%;">Yes. Sure. Let's close it.</span>

**airween** <span style="color: grey; font-size: 90%;">20:36:34 UTC</span>

<span style="font-size: 90%;">so, then we finished?</span>

**azurit** <span style="color: grey; font-size: 90%;">20:37:54 UTC</span>

<span style="font-size: 90%;">Yes!</span>

**jit** <span style="color: grey; font-size: 90%;">20:38:12 UTC</span>

<span style="font-size: 90%;">Goodnight folks!</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:38:31 UTC</span>

<span style="font-size: 90%;">Night!</span>

**michela** <span style="color: grey; font-size: 90%;">20:38:35 UTC</span>

<span style="font-size: 90%;">Bye for now, everyone!</span>

**airween** <span style="color: grey; font-size: 90%;">20:39:02 UTC</span>

<span style="font-size: 90%;">good night!</span>

**azurit** <span style="color: grey; font-size: 90%;">20:39:08 UTC</span>

<span style="font-size: 90%;">Good night.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:39:39 UTC</span>

<span style="font-size: 90%;">Good night!! Bye.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">20:40:00 UTC</span>

<span style="font-size: 90%;">[https://github.com/coreruleset/coreruleset/issues/4507#issuecomment-3986562874](https://github.com/coreruleset/coreruleset/issues/4507#issuecomment-3986562874)
I hope I got everything right, if not please correct me...</span>

