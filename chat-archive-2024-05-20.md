### Mon, May 20th, 2024

**airween** <span style="color: grey; font-size: 90%;">18:30:28 UTC</span>

<span style="font-size: 90%;">hi there :wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:30:44 UTC</span>

<span style="font-size: 90%;">Hi everyone. Time for our chat</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:30:46 UTC</span>

<span style="font-size: 90%;">Hello</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">18:31:52 UTC</span>

<span style="font-size: 90%;">Hey, Hello</span>

**jit** <span style="color: grey; font-size: 90%;">18:32:03 UTC</span>

<span style="font-size: 90%;">Hi everyone. :wave:</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:33:00 UTC</span>

<span style="font-size: 90%;">Hi</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:05 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:33:37 UTC</span>

<span style="font-size: 90%;">So, first item on the list is the GeoIP plugin. _@azurit_ isn't here it seems, _@fzipitria_ can you explain?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:34:54 UTC</span>

<span style="font-size: 90%;">Ok, in that case, let's postpone that discussion and pick it up in two weeks.</span>

**franbuehler** <span style="color: grey; font-size: 90%;">18:35:12 UTC</span>

<span style="font-size: 90%;">I'll take the notes...</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:19 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:42 UTC</span>

<span style="font-size: 90%;">Point 2 is also by _@azurit_, let's skip that one as well</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:55 UTC</span>

<span style="font-size: 90%;">Hey</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:35:56 UTC</span>

<span style="font-size: 90%;">Point 3 has been resolved</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:02 UTC</span>

<span style="font-size: 90%;">That was quick</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:04 UTC</span>

<span style="font-size: 90%;">:slightly_smiling_face:</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:36:43 UTC</span>

<span style="font-size: 90%;">Do you want to chime in _@fzipitria_? I figured it would be helpful if _@azurit_ were here.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:46 UTC</span>

<span style="font-size: 90%;">Sure</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:01 UTC</span>

<span style="font-size: 90%;">There is a new plugin</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:07 UTC</span>

<span style="font-size: 90%;">For doing GeoIP blocking</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:31 UTC</span>

<span style="font-size: 90%;">That still needs to be moved to the coreruleset org</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:25 UTC</span>

<span style="font-size: 90%;">The only thing remaining is having some tests around probably</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:33 UTC</span>

<span style="font-size: 90%;">And the proper setup for your web server</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:04 UTC</span>

<span style="font-size: 90%;">I think it is a good addition to our plugins roster :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:23 UTC</span>

<span style="font-size: 90%;">And was definitely something that it was out there in v3 (but don't know how useful it was)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:43 UTC</span>

<span style="font-size: 90%;">That's it</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:39:58 UTC</span>

<span style="font-size: 90%;">Oh, ok. I thought there was something to be discussed.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:40:00 UTC</span>

<span style="font-size: 90%;">Thanks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:20 UTC</span>

<span style="font-size: 90%;">Well, the setting</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:41 UTC</span>

<span style="font-size: 90%;">This geoip version is based on adding information for other plugins</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:45 UTC</span>

<span style="font-size: 90%;">`What about to create really GeoIP only plugin which then can be used by other plugins, like IP reputation?`</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:04 UTC</span>

<span style="font-size: 90%;">So the idea is that you will have variables available only</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:41:24 UTC</span>

<span style="font-size: 90%;">And then use that in your rules</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:41:51 UTC</span>

<span style="font-size: 90%;">Sounds like a good idea to me.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:42:45 UTC</span>

<span style="font-size: 90%;">Shall we move on to the next topic?</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:43:27 UTC</span>

<span style="font-size: 90%;">_@airween_, _@ne20002_ can you explain the issue with [https://github.com/coreruleset/coreruleset/issues/3698](https://github.com/coreruleset/coreruleset/issues/3698)?</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:43:49 UTC</span>

<span style="font-size: 90%;">Sure</span>

**airween** <span style="color: grey; font-size: 90%;">18:44:18 UTC</span>

<span style="font-size: 90%;">_@ne20002_ thanks :slightly_smiling_face:</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:44:52 UTC</span>

<span style="font-size: 90%;">A in the description I have a Friendica server. A very small private one.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:45:30 UTC</span>

<span style="font-size: 90%;">With the update to 4.2. I realized a number of denied requests.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:46:22 UTC</span>

<span style="font-size: 90%;">Those are all within the /inbox post request. It's a json with a few fields and can contain nearly anything, e.g. signatures.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:46:58 UTC</span>

<span style="font-size: 90%;">One was a match on 'mkdir' where the signature included mKDiR or something like that.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:47:31 UTC</span>

<span style="font-size: 90%;">I also had fp on strings like 'PowerShell' if it was part of an url.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:47:53 UTC</span>

<span style="font-size: 90%;">In the issue a few examples are listed, including the request body.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:48:11 UTC</span>

<span style="font-size: 90%;">I wonder if those rules shall be part of PL1 or better PL2?</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:48:39 UTC</span>

<span style="font-size: 90%;">Or e.g. looking for ' mkdir ' in PL1 and for 'mkdir' in PL2?</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:19 UTC</span>

<span style="font-size: 90%;">I think the biggest problem is that the compiled regex has many single words, and those match if any of that exists in an ARG as a substring - so that's not an "exact match"</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:31 UTC</span>

<span style="font-size: 90%;">perhaps we should use some boundaries</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:49:31 UTC</span>

<span style="font-size: 90%;">Yes</span>

**airween** <span style="color: grey; font-size: 90%;">18:49:42 UTC</span>

<span style="font-size: 90%;">eg. whitespace</span>

**airween** <span style="color: grey; font-size: 90%;">18:50:28 UTC</span>

<span style="font-size: 90%;">the `mkdir` example above is not this case - there you should create an exclusion</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:50:28 UTC</span>

<span style="font-size: 90%;">Do you feel this is a general problem? To me, on  a cursory look, it seems like a good case for a rule exclusion plugin.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:50:31 UTC</span>

<span style="font-size: 90%;">For a command like mkdir I suggest a test for at least one whitespace before or after. Otherwise it is probably no attak.</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:51:09 UTC</span>

<span style="font-size: 90%;">Unfortunately, that's not how command line injection works :slightly_smiling_face:</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:51:30 UTC</span>

<span style="font-size: 90%;">I thought of having a plugin for Fediverse / ActivityPub servers would be a good idea, Fediverse is growing.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:51:53 UTC</span>

<span style="font-size: 90%;">But simply excluding rules instead of maybe making it better?</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:53:04 UTC</span>

<span style="font-size: 90%;">There is a few other rules I already excluded for /inbox.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:53:42 UTC</span>

<span style="font-size: 90%;">Current version of my exclusions is:</span>

**airween** <span style="color: grey; font-size: 90%;">18:53:43 UTC</span>

<span style="font-size: 90%;">_@ne20002_ - I think you can't avoid to make a plugin for Fediverse :slightly_smiling_face:, sooner or later you will run into many FP's
to others: what if we make a less strict rule with that regex where we use boundaries on PL1, and keep the existing rule but move it to PL2?</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:53:47 UTC</span>

<span style="font-size: 90%;"># Mitigate false positives on calls to /inbox
SecRule REQUEST_URI "@streq /inbox" \
    "id:900300,\
    phase:2,\
    pass,\
    t:none,\
    nolog,\
    ctl:ruleRemoveTargetByTag=OWASP_CRS;ARGS:json.signature.signatureValue,\
    ctl:ruleRemoveTargetByTag=OWASP_CRS;ARGS:json.object.content,\
    ctl:ruleRemoveById=932130,\
    ctl:ruleRemoveById=932370,\
    ctl:ruleRemoveById=932380,\
    ctl:ruleRemoveById=933120"
#    ctl:requestBodyAccess=Off"</span>

**azurit** <span style="color: grey; font-size: 90%;">18:54:07 UTC</span>

<span style="font-size: 90%;">Hi, my Slack app is crashing after upgrade, so this is why i'm not here. :white_frowning_face:</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:54:30 UTC</span>

<span style="font-size: 90%;">I believe a plugin would be great. All (most) Fediverse server share the protocol, so they all would benefit.</span>

**airween** <span style="color: grey; font-size: 90%;">18:55:01 UTC</span>

<span style="font-size: 90%;">_@ne20002_: never use `ctl:requestBodyAccess=Off`, especially on libmodsecurity3</span>

**maxleske** <span style="color: grey; font-size: 90%;">18:55:02 UTC</span>

<span style="font-size: 90%;">You're speaking of "a rule" but mention multiple ones in the issue. Which one are we talking about here?</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:55:17 UTC</span>

<span style="font-size: 90%;">They (software) all do have their own api as well, but the common part is ActivityPub.</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:55:54 UTC</span>

<span style="font-size: 90%;">That's why it is commented. I heard you :wink:</span>

**ne20002** <span style="color: grey; font-size: 90%;">18:56:49 UTC</span>

<span style="font-size: 90%;">Those are what I found until today. They all caused at least on FP on the /inbox post.</span>

**airween** <span style="color: grey; font-size: 90%;">18:58:58 UTC</span>

<span style="font-size: 90%;">I inspected the issue with rule 932235, there I found that "substring" problem:

[https://github.com/coreruleset/coreruleset/issues/3698#issuecomment-2106343444](https://github.com/coreruleset/coreruleset/issues/3698#issuecomment-2106343444)

"See the [regex](https://github.com/coreruleset/coreruleset/blob/main/regex-assembly/932235.ra) and it's [included](https://github.com/coreruleset/coreruleset/blob/main/regex-assembly/include/unix-shell-4andup.ra#L486) source, which has the sub-string `tcsh`." (the argument was "enVTCsH")</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:38 UTC</span>

<span style="font-size: 90%;">yes, we have a couple of open issues with the unix RCE rules. I think we need to tackle those as a group and conceptually decide what we want to do with them.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:00:51 UTC</span>

<span style="font-size: 90%;">The plugin, I think, is pretty much a given.</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:01:23 UTC</span>

<span style="font-size: 90%;">enVTCsH as part of:
,"signatureValue":"SMPaxxkHm6ejaJqS/lAouPJjRtMXmLfX/VBWuu6zTILQu7/gh18Vjlx2dqe/ktBqByQwkbRcdocOCiac6FOEtqvFTJaabUcl+z1NCwx9K9e+541DPYtouwI/6OUTe4BBtOL3eUC31iUosfmlKxgXI+loe7NFXcxc5RMt+Ma3iF9Rtf+QRkg9polMf0w65u/8LxWHI9xRHQsgdw95cJtxy/KnFxDc4zFqkHlBKCBaGHy4DeReGyzNEIheZB8tLyu7HM4zmYTlNfgd0qctARkBbydyVenVTCsHpj/lf2+nq9nNk3AToa5nM9FPet6kATd35ZF9auZQI40qoxb0o1+11g=="}}</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:01:49 UTC</span>

<span style="font-size: 90%;">I would love a plugin.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:02:37 UTC</span>

<span style="font-size: 90%;">Are you both happy with that? I know it's not a solution for the 923* rules.</span>

**airween** <span style="color: grey; font-size: 90%;">19:02:42 UTC</span>

<span style="font-size: 90%;">oh, so was it "env" + "tcsh"? Nice :smile:</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:03:09 UTC</span>

<span style="font-size: 90%;">I believe it is a good way to go.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:04:39 UTC</span>

<span style="font-size: 90%;">Great.</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:05:08 UTC</span>

<span style="font-size: 90%;">The plugin could then also include the content-types ... clean solution. :slightly_smiling_face:</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:05:46 UTC</span>

<span style="font-size: 90%;">What are you referring to?</span>

↳ **ne20002** <span style="color: grey; font-size: 90%;">19:06:57 UTC</span>

<span style="font-size: 90%;">There is a few more tweaks I did for ActivityPub. They should all go into the plugin.</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:08:22 UTC</span>

<span style="font-size: 90%;">So nothing we need to consider in general?</span>

↳ **ne20002** <span style="color: grey; font-size: 90%;">19:09:11 UTC</span>

<span style="font-size: 90%;">No, just for the plugin then.</span>

↳ **ne20002** <span style="color: grey; font-size: 90%;">19:09:44 UTC</span>

<span style="font-size: 90%;">Like this:
 setvar:'tx.allowed_request_content_type=|application/octet-stream| |application/activity+json| |application/ld+json| |application/magic-envelope+xml| |application/x-zot+json| |application/x-www-form-urlencoded| |multipart/form-data| |multipart/related| |text/xml| |application/xml| |application/soap+xml| |application/json|'"</span>

↳ **maxleske** <span style="color: grey; font-size: 90%;">19:10:05 UTC</span>

<span style="font-size: 90%;">I see</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:05:09 UTC</span>

<span style="font-size: 90%;">So, _@azurit_, did you want to add anything to _@fzipitria_'s explanation on the GeoIP plugin?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:05:33 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:06:01 UTC</span>

<span style="font-size: 90%;">It will take a minute as i'm writing uding my phone.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:06:58 UTC</span>

<span style="font-size: 90%;">Current form of geoip plugin was meant to be some kind of a library used by other plugins or custom user rules.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:07:18 UTC</span>

<span style="font-size: 90%;">So plugin does nothing by itself, it's very simple.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:07:45 UTC</span>

<span style="font-size: 90%;">I created it to unify usage of geoip across CRS.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:08:59 UTC</span>

<span style="font-size: 90%;">But dune don't think this is optimal solution and would like from plugin to do at least simple blocking using geoip.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:10:06 UTC</span>

<span style="font-size: 90%;">i.e. to add one more rule which will block request based on another config rule with ISO codes (or something similar).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:28 UTC</span>

<span style="font-size: 90%;">I would say let's have _something_ and then we iterate and enhance</span>

**azurit** <span style="color: grey; font-size: 90%;">19:11:29 UTC</span>

<span style="font-size: 90%;">I, on the other hand, would like to use it in current form and create another, more generic, plugin which will do blocking based on multiple criteria.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:51 UTC</span>

<span style="font-size: 90%;">Oh, so two plugins? Wouldn't that be confusing to users?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:12:42 UTC</span>

<span style="font-size: 90%;">It might be a little confusing, maybe. But as long as the documentation makes the dependency clear, I don't really see an issue.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:13:13 UTC</span>

<span style="font-size: 90%;">I like the idea to have this simple plugin but I'd really like to hear _@dune73_'s concerns first.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:13:19 UTC</span>

<span style="font-size: 90%;">Geoip will be only a 'library' which only be mentioned in docs of other plugins - something like 'to use this plugin you need to activate also geoip plugin'.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">19:14:19 UTC</span>

<span style="font-size: 90%;">The idea is to create a layer to support multiple different installations, right?</span>

↳ **azurit** <span style="color: grey; font-size: 90%;">19:17:13 UTC</span>

<span style="font-size: 90%;">Yes, so everything other (plugins, rules, CRS) will use geoip using the same way i.e. not trying to initialize it X times per request.</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:13:27 UTC</span>

<span style="font-size: 90%;">I'd like more plugins based on context. E.g. for the Nextcloud plugin I would have expected a WebDav plugin as base.</span>

**ne20002** <span style="color: grey; font-size: 90%;">19:13:58 UTC</span>

<span style="font-size: 90%;">So WebDav would be reusable for other context ..</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:14:20 UTC</span>

<span style="font-size: 90%;">That's certainly a good idea, _@ne20002_</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:21 UTC</span>

<span style="font-size: 90%;">So will be geoip.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:14:40 UTC</span>

<span style="font-size: 90%;">That was my thinking.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:15:11 UTC</span>

<span style="font-size: 90%;">Let's give _@dune73_ the chance to voice his opinion in the issue (please ping him, _@azurit_).</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:16:23 UTC</span>

<span style="font-size: 90%;">We skipped over this one _@azurit_, as you were offline: [https://github.com/coreruleset/coreruleset/issues/2751](https://github.com/coreruleset/coreruleset/issues/2751)

Do you still want to discuss it now?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:17:49 UTC</span>

<span style="font-size: 90%;">This is an old one.</span>

**azurit** <span style="color: grey; font-size: 90%;">19:18:06 UTC</span>

<span style="font-size: 90%;">Any thoughts about it?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:18:42 UTC</span>

<span style="font-size: 90%;">I did sime tests, as i stated but i can't guarantee anything.</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:20:25 UTC</span>

<span style="font-size: 90%;">So you're suggestion is to check for gzip magic number to avoid FPs?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:20:59 UTC</span>

<span style="font-size: 90%;">yes</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:21:37 UTC</span>

<span style="font-size: 90%;">Sounds good to me.
Other opinions?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:22:50 UTC</span>

<span style="font-size: 90%;">What about Content-Encoding?</span>

**azurit** <span style="color: grey; font-size: 90%;">19:23:01 UTC</span>

<span style="font-size: 90%;">Can it be trusted?</span>

**maxleske** <span style="color: grey; font-size: 90%;">19:24:45 UTC</span>

