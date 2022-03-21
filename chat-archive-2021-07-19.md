### Mon, Jul 19th, 2021

**dune73** <span style="color: grey; font-size: 90%;">18:30:33 UTC</span>

<span style="font-size: 90%;">Hello everybody, time for our monthly issue chat. Who's participating today?</span>

**walter** <span style="color: grey; font-size: 90%;">18:30:40 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**airween** <span style="color: grey; font-size: 90%;">18:31:04 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:31:23 UTC</span>

<span style="font-size: 90%;">Good evening</span>

**dune73** <span style="color: grey; font-size: 90%;">18:31:29 UTC</span>

<span style="font-size: 90%;">Hey guys, good see you all!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:50 UTC</span>

<span style="font-size: 90%;">:wave: Hello</span>

**dune73** <span style="color: grey; font-size: 90%;">18:32:08 UTC</span>

<span style="font-size: 90%;">Hello Andrew, so cool to see you again!</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:33:41 UTC</span>

<span style="font-size: 90%;">Hi</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:47 UTC</span>

<span style="font-size: 90%;">Franziska is on holiday, and I do not know where everybody else is. I've seen _@theMiddle_ near a terminal today...</span>

**dune73** <span style="color: grey; font-size: 90%;">18:33:56 UTC</span>

<span style="font-size: 90%;">Hey, _@azurIt_! Welcome.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:35:47 UTC</span>

<span style="font-size: 90%;">I expected us to be fewer people than usual, so I only put 8 issues on the menu. It is at [https://github.com/coreruleset/coreruleset/issues/2141](https://github.com/coreruleset/coreruleset/issues/2141)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:36:40 UTC</span>

<span style="font-size: 90%;">Before we start: I think the first badge of dev-on-duty payments have all been processed. The fees for paypal have been acceptable or what we expected, the ones for bank transfer quite substantial (> 25%).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:37:38 UTC</span>

<span style="font-size: 90%;">Also: From now on, I will try to group the payments so we can do badges of 3 months. Otherwise it's too much work for me. (Getting the first badge of payments was 3-4 hours of work for me alone. The next ones will be easier, but still.)</span>

**dune73** <span style="color: grey; font-size: 90%;">18:38:49 UTC</span>

<span style="font-size: 90%;">The first issue to cover tonight is a complex one. The other ones are easier I suppose. _@fzipitria_ did a large test run with a test script that Wallarm published. He identified a few FPs, but also a few bypasses, that we need to look at.
That issue 1991.</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:40:36 UTC</span>

<span style="font-size: 90%;">If there is lot's of work to do, maybe we should separate it into multiple issues.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:22 UTC</span>

<span style="font-size: 90%;">That would make sense.
If you scroll down to my comment, I have summed it up.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:41:44 UTC</span>

<span style="font-size: 90%;">Do you guys think the FPs at PL1 are something we should tackle?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:05 UTC</span>

<span style="font-size: 90%;">Hi! :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:05 UTC</span>

<span style="font-size: 90%;">It's 4 different rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:42:15 UTC</span>

<span style="font-size: 90%;">Hello _@fzipitria_!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:33 UTC</span>

<span style="font-size: 90%;">Hi all!</span>

**dune73** <span style="color: grey; font-size: 90%;">18:43:42 UTC</span>

<span style="font-size: 90%;">The payloads causing the FPs look more or less natural.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:44:12 UTC</span>

<span style="font-size: 90%;">932100, 932110, 932150 and 942190.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:44:35 UTC</span>

<span style="font-size: 90%;">Yeah, kind of</span>

**dune73** <span style="color: grey; font-size: 90%;">18:45:01 UTC</span>

<span style="font-size: 90%;">What do you propose?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:38 UTC</span>

<span style="font-size: 90%;">Well, they are well crafted, that’s for sure</span>

**theMiddle** <span style="color: grey; font-size: 90%;">18:45:56 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:57 UTC</span>

<span style="font-size: 90%;">We might need to review a bit the RCE ones</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:04 UTC</span>

<span style="font-size: 90%;">But I agree we should create new tickets per rule, at least</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:41 UTC</span>

<span style="font-size: 90%;">Does everybody agree these are FPs that we will attack (vs. FPs we simply ignore until a user walks up).</span>

**dune73** <span style="color: grey; font-size: 90%;">18:48:48 UTC</span>

<span style="font-size: 90%;">?</span>

**azurIt** <span style="color: grey; font-size: 90%;">18:50:26 UTC</span>

<span style="font-size: 90%;">I think we should at least because it is a part of well-know (guessing?) testing suite.</span>

**walter** <span style="color: grey; font-size: 90%;">18:51:26 UTC</span>

<span style="font-size: 90%;">I think “union was a great select” is kind of lame, but as for the other ones, I don’t know how we would tackle these as they are valid UNIX/DOS commands that can leak files in case of unsanitized passing to a shell</span>

**dune73** <span style="color: grey; font-size: 90%;">18:51:27 UTC</span>

<span style="font-size: 90%;">It's not very well known, but Wallarm has released it more or less for us because they somehow like what we do and because their former chief strategy officer Kavya Pearlman is a friend of mine.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:52:27 UTC</span>

<span style="font-size: 90%;">I agree on the union.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:52:30 UTC</span>

<span style="font-size: 90%;">Would seem good to fix FPs related to common words (time, more etc), as I imagine these could be used fairly commonly. I haven't looked at this in detail to understand what anchoring / word boundaries already help protect against FPs</span>

**walter** <span style="color: grey; font-size: 90%;">18:52:44 UTC</span>

<span style="font-size: 90%;">we could, of course, move frequently occurring words such as time and copy to a higher PL but that would open up vulnerabilities again…</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:08 UTC</span>

<span style="font-size: 90%;">time is a peculiar case I think since it only works with other commands, does not it?</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:29 UTC</span>

<span style="font-size: 90%;">And how do you use time in an RCE exactly? (n00b question ...)</span>

**walter** <span style="color: grey; font-size: 90%;">18:53:30 UTC</span>

<span style="font-size: 90%;">yes you can do time ls to do a ls and conveniently display the time it took the computer</span>

**dune73** <span style="color: grey; font-size: 90%;">18:53:57 UTC</span>

<span style="font-size: 90%;">OK, so you do time ls to hide the ls command from RCE detection?</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:17 UTC</span>

<span style="font-size: 90%;">yes! we have ls blocklisted in that rule</span>

**walter** <span style="color: grey; font-size: 90%;">18:54:20 UTC</span>

<span style="font-size: 90%;">or denylisted :smile:</span>

**dune73** <span style="color: grey; font-size: 90%;">18:54:33 UTC</span>

<span style="font-size: 90%;">Blocklisted sounds leggit to me. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:11 UTC</span>

<span style="font-size: 90%;">maybe we could make time work by adding it as a prefix only so that it requires a real unix command after it, to trigger</span>

**walter** <span style="color: grey; font-size: 90%;">18:55:22 UTC</span>

<span style="font-size: 90%;">that would get rid of time.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:55:54 UTC</span>

<span style="font-size: 90%;">I think that would be a good plan, Walter.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:04 UTC</span>

<span style="font-size: 90%;">The problem with time is the covert channel attack</span>

**dune73** <span style="color: grey; font-size: 90%;">18:56:05 UTC</span>

<span style="font-size: 90%;">It's a question whether it's worth the performance, though.</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:07 UTC</span>

<span style="font-size: 90%;">copy, maybe we can make a separate rule for it. I imagine people doing copy password.txt con to output it to the response</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">18:56:10 UTC</span>

<span style="font-size: 90%;">Looks like time can be useful in a few limited scenarios: [https://gtfobins.github.io/gtfobins/time/](https://gtfobins.github.io/gtfobins/time/)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:56 UTC</span>

<span style="font-size: 90%;">And timing commands can be useful for blind injections</span>

**walter** <span style="color: grey; font-size: 90%;">18:56:59 UTC</span>

<span style="font-size: 90%;">it might be worth doing this work. I’ve had to make exclusions for time so I bet probably most people will run into it.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:33 UTC</span>

<span style="font-size: 90%;">OK. So we have a plan here. Then we forget about the Union.</span>

**dune73** <span style="color: grey; font-size: 90%;">18:57:49 UTC</span>

<span style="font-size: 90%;">Copy in a separate rule too, or what is our plan there?</span>

**walter** <span style="color: grey; font-size: 90%;">18:58:18 UTC</span>

<span style="font-size: 90%;">yes, time can become one of the prefixes such as ; and &&. so, time plus a unix command will trigger, not time alone.</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:02 UTC</span>

<span style="font-size: 90%;">maybe we can even make the rule so we have (?:time\s+)? in it.</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:25 UTC</span>

<span style="font-size: 90%;">(and remove it from the wordlist)</span>

**walter** <span style="color: grey; font-size: 90%;">18:59:48 UTC</span>

<span style="font-size: 90%;">that would be even better I think.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:00:08 UTC</span>

<span style="font-size: 90%;">And it would save us a rule!</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:15 UTC</span>

<span style="font-size: 90%;">I guess it would be best to assign it to me as I’ve made this rule :see_no_evil:</span>

**dune73** <span style="color: grey; font-size: 90%;">19:01:41 UTC</span>

<span style="font-size: 90%;">I would not mind doing, that. :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:41 UTC</span>

<span style="font-size: 90%;">I’ve been a bad boy though last month. Been extremely busy and did not finish the issues that were on my plate..</span>

**walter** <span style="color: grey; font-size: 90%;">19:01:56 UTC</span>

<span style="font-size: 90%;">but summer vacation should be better</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:13 UTC</span>

<span style="font-size: 90%;">Same here. But I also spent a full week on the CVE coordination (namely behind the curtain with integrators).</span>

**dune73** <span style="color: grey; font-size: 90%;">19:02:30 UTC</span>

<span style="font-size: 90%;">How about the copy, then?</span>

**walter** <span style="color: grey; font-size: 90%;">19:04:28 UTC</span>

<span style="font-size: 90%;">I’m not a Windows user, but I guess copy can only be used to leak data if it’s copied to CON (standard output). so we could create a separate rule and look for copy\s+.*\s+[cC][oO][nN] …</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:05:09 UTC</span>

<span style="font-size: 90%;">Or by copying file into web accessible directory.</span>

**walter** <span style="color: grey; font-size: 90%;">19:05:47 UTC</span>

<span style="font-size: 90%;">yes, if we want to prevent copying arbitrary files then we have no way to prevent the FP I’m afraid</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:06:14 UTC</span>

<span style="font-size: 90%;">Or potentially to overwrite file (eg an allow list file)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:06:28 UTC</span>

<span style="font-size: 90%;">I was assuming copy was part of an RCE attack and then it's really a copy and then there is little we can do.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:07:08 UTC</span>

<span style="font-size: 90%;">I guess the copy to be useful is almost certainly got to have a path after it</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:21 UTC</span>

<span style="font-size: 90%;">We could prevent a rare occurrence of FPs when copy comes with a single argument only. But that's probably not worth it.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:28 UTC</span>

<span style="font-size: 90%;">Ah, you mean a slash somewhere?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:07:33 UTC</span>

<span style="font-size: 90%;">Yes</span>

**walter** <span style="color: grey; font-size: 90%;">19:07:45 UTC</span>

<span style="font-size: 90%;">that might be a good compromise</span>

**dune73** <span style="color: grey; font-size: 90%;">19:07:54 UTC</span>

<span style="font-size: 90%;">So it's got to be a CON or a slash!?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:08:07 UTC</span>

<span style="font-size: 90%;">\ included</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:08:31 UTC</span>

<span style="font-size: 90%;">we’re talking about windows copy command?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:08:32 UTC</span>

<span style="font-size: 90%;">Copying a file to another file that's already in the same directory your in doesn't seem like it should be very useful in many scenarios... Other than evading specific blocks eg .htaccess</span>

**walter** <span style="color: grey; font-size: 90%;">19:08:59 UTC</span>

<span style="font-size: 90%;">yes!</span>

**walter** <span style="color: grey; font-size: 90%;">19:09:18 UTC</span>

<span style="font-size: 90%;">I like that idea. we could combine it into one rule</span>

**walter** <span style="color: grey; font-size: 90%;">19:10:19 UTC</span>

<span style="font-size: 90%;">or two rules (IIRC we have a separate rule that also looks for Windows commands without the ; prefix, for applications that might pass the whole payload to a shell)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:11:30 UTC</span>

<span style="font-size: 90%;">Me too. This is a decent step forward. And every FP we prevent is one FP less that our users are facing.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:12:03 UTC</span>

<span style="font-size: 90%;">(They'll probably never notice just how much time we spend on making their lives easier.)</span>

**walter** <span style="color: grey; font-size: 90%;">19:12:46 UTC</span>

<span style="font-size: 90%;">OK so we have agreement on this and a plausible way forward!</span>

**walter** <span style="color: grey; font-size: 90%;">19:13:24 UTC</span>

<span style="font-size: 90%;">shall I create a separate issue for it?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:35 UTC</span>

<span style="font-size: 90%;">Please do. Per issue or the 3 together?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:14:46 UTC</span>

<span style="font-size: 90%;">(Assuming we drop Union from the list)</span>

**walter** <span style="color: grey; font-size: 90%;">19:14:56 UTC</span>

<span style="font-size: 90%;">I guess since they will be changing the same rule, it will be easier to do it in one PR.</span>

**walter** <span style="color: grey; font-size: 90%;">19:15:45 UTC</span>

<span style="font-size: 90%;">we don’t have a good plan for more than still, though.</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:14 UTC</span>

<span style="font-size: 90%;">more displays a file, but it accepts multiple arguments.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:15 UTC</span>

<span style="font-size: 90%;">True that.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:16:49 UTC</span>

<span style="font-size: 90%;">Is not there a way to do a privilege escalation with more? I seem to remember there was a technique...</span>

**walter** <span style="color: grey; font-size: 90%;">19:16:56 UTC</span>

<span style="font-size: 90%;">we could check for slashes and dots…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:17:43 UTC</span>

<span style="font-size: 90%;">So we say "more" in the local folder is moot?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:17:55 UTC</span>

<span style="font-size: 90%;">[https://gtfobins.github.io/gtfobins/more/](https://gtfobins.github.io/gtfobins/more/)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:18:53 UTC</span>

<span style="font-size: 90%;">There we go.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:20:43 UTC</span>

<span style="font-size: 90%;">Looks like the prevention of slashes can take us quite far here.</span>

**walter** <span style="color: grey; font-size: 90%;">19:21:17 UTC</span>

<span style="font-size: 90%;">I guess if we look for dots and slashes we can shave off some FP.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:22:02 UTC</span>

<span style="font-size: 90%;">The one case this doesn't protect is reading things like PHP config files with passwords in the same directory. But that might not be easy to detect without creating FPs</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:22:39 UTC</span>

<span style="font-size: 90%;">Hi!!
I'm in Italy and I will not attend our meeting tonight... :wave:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:22:49 UTC</span>

<span style="font-size: 90%;">Sorry, I'm a bit late :wink:</span>

**walter** <span style="color: grey; font-size: 90%;">19:22:50 UTC</span>

<span style="font-size: 90%;">_@franbuehler_ have fun in italy!</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:02 UTC</span>

<span style="font-size: 90%;">Thank you :smiley:</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:23:05 UTC</span>

<span style="font-size: 90%;">wow where? :slightly_smiling_face:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:13 UTC</span>

<span style="font-size: 90%;">Cavallino-Treporti</span>

**dune73** <span style="color: grey; font-size: 90%;">19:23:28 UTC</span>

<span style="font-size: 90%;">Happy holidays, nice to say hello!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:23:42 UTC</span>

<span style="font-size: 90%;">oh nice, near venezia?</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:42 UTC</span>

<span style="font-size: 90%;">Thank you :smiley:</span>

**franbuehler** <span style="color: grey; font-size: 90%;">19:23:47 UTC</span>

<span style="font-size: 90%;">Yes!!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:24:13 UTC</span>

<span style="font-size: 90%;">So who does the issue for "more"?</span>

**walter** <span style="color: grey; font-size: 90%;">19:25:16 UTC</span>

<span style="font-size: 90%;">maybe I come up with something good when working on the other two keywords</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:22 UTC</span>

<span style="font-size: 90%;">OK, thanks. Let's move on then.</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:32 UTC</span>

<span style="font-size: 90%;">there was some more in [#1991](https://github.com/coreruleset/coreruleset/issues/#1991)</span>

**walter** <span style="color: grey; font-size: 90%;">19:26:37 UTC</span>

<span style="font-size: 90%;">the triple-dot was interesting</span>

**dune73** <span style="color: grey; font-size: 90%;">19:26:40 UTC</span>

<span style="font-size: 90%;">Since 1991 also comes with bypasses...</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:07 UTC</span>

<span style="font-size: 90%;">There are a few mail injections that we only catch at PL4 since we do not have any SMTP rules.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:27:10 UTC</span>

<span style="font-size: 90%;">Do we need that?</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:12 UTC</span>

<span style="font-size: 90%;">this is, I guess, interesting if we are in front of an open proxy and we would be abused for making IMAP, POP3 or SMTP connections to other machines (in order for brute force password scanning?)</span>

**walter** <span style="color: grey; font-size: 90%;">19:28:49 UTC</span>

<span style="font-size: 90%;">but I think we solved that already in the default config because we don’t allow CONNECT</span>

**walter** <span style="color: grey; font-size: 90%;">19:29:06 UTC</span>

<span style="font-size: 90%;">(rule 900200)</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:19 UTC</span>

<span style="font-size: 90%;">OK. How about SMTP with regards to data leakages?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:29:32 UTC</span>

<span style="font-size: 90%;">RCE->SMTP?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:31:07 UTC</span>

<span style="font-size: 90%;">I've only skimmed this, but are there some nosql and LDAP injection bypasses too?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:11 UTC</span>

<span style="font-size: 90%;">Yes, but that we catch at PL2 which is good enough IMHO.</span>

**walter** <span style="color: grey; font-size: 90%;">19:32:37 UTC</span>

<span style="font-size: 90%;">could be worthwhile adding more noSQL rules, but I have no experience with that sadly</span>

**dune73** <span style="color: grey; font-size: 90%;">19:32:39 UTC</span>

<span style="font-size: 90%;">I'm wondering about the SMTP stuff only at PL4 and the Windows triple dot ... only at PL3 worries me.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:01 UTC</span>

<span style="font-size: 90%;">OK, so the consensus seems to be that we do not worry about SMTP.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:33:11 UTC</span>

<span style="font-size: 90%;">What about the triple dots then?</span>

**walter** <span style="color: grey; font-size: 90%;">19:33:32 UTC</span>

<span style="font-size: 90%;">yeah that triple dot is interesting, I’ve never come across it… what does it do? it doesn’t seem to do anything special here</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:34:15 UTC</span>

<span style="font-size: 90%;">[https://cwe.mitre.org/data/definitions/32.html](https://cwe.mitre.org/data/definitions/32.html)</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:34:25 UTC</span>

<span style="font-size: 90%;">I reckon triple dots are used pretty commonly ... As a way of breaking up a sentence, and could result in FPs. Probably pretty safe if we required a slash before or after though</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:35:14 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:35:43 UTC</span>

<span style="font-size: 90%;">[https://superuser.com/questions/480122/does-have-meaning-as-a-relative-pathname-edit-no](https://superuser.com/questions/480122/does-have-meaning-as-a-relative-pathname-edit-no)</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:26 UTC</span>

<span style="font-size: 90%;">on Win9x systems (but not NT-based systems), the cd command would treat ... similarly to ..\.. and .... similarly to ..\..\.. and so on.</span>

**walter** <span style="color: grey; font-size: 90%;">19:36:45 UTC</span>

<span style="font-size: 90%;">I think it’s safe to ignore this :blush:</span>

**azurIt** <span style="color: grey; font-size: 90%;">19:36:49 UTC</span>

<span style="font-size: 90%;">Sorry friends, i have to go. Good night!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:36:53 UTC</span>

<span style="font-size: 90%;">That's why the CVEs are so old.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:09 UTC</span>

<span style="font-size: 90%;">Good night _@azurIt_!</span>

**dune73** <span style="color: grey; font-size: 90%;">19:37:45 UTC</span>

<span style="font-size: 90%;">OK, we let this go then.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:38:14 UTC</span>

<span style="font-size: 90%;">So I personally think all the bypasses are of little interest for us and we can close this with new issues for the FPs.</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:13 UTC</span>

<span style="font-size: 90%;">it might still be worth it to create NoSQL rules, but if we don’t have that knowledge, it would be hard for us to make them. we probably would have to learn the most popular query languages from scratch</span>

**walter** <span style="color: grey; font-size: 90%;">19:39:33 UTC</span>

<span style="font-size: 90%;">might still be a useful project for the hacking week though!</span>

**walter** <span style="color: grey; font-size: 90%;">19:40:10 UTC</span>

<span style="font-size: 90%;">I guess a few days would be enough to install a nosql server docker and play with it</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:40:41 UTC</span>

<span style="font-size: 90%;">there’re free labs too to play with nosql injection</span>

**dune73** <span style="color: grey; font-size: 90%;">19:40:42 UTC</span>

<span style="font-size: 90%;">Please write it on a note somewhere. Also time we start to collect ideas for October.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:41:32 UTC</span>

<span style="font-size: 90%;">SANS 2015 Holiday Hack might have some useful info... I think that involved nosql injection</span>

**dune73** <span style="color: grey; font-size: 90%;">19:42:28 UTC</span>

<span style="font-size: 90%;">Good, so we are done with 1991 for tonight.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:43:14 UTC</span>

<span style="font-size: 90%;">That brings us to 2118, where _@theMiddle_ responded to a request by Franziska tonight, so I think she'll probably pick this up when she's back from Italy.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:04 UTC</span>

<span style="font-size: 90%;">2135 is tougher. There are a few rules triggered by "ping pong" when in a payload after a newline.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:13 UTC</span>

<span style="font-size: 90%;">Funny enough, ping pong is worse than Ping Pong.</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:32 UTC</span>

<span style="font-size: 90%;">yes, ping will work on unix as it’s case-sensitive</span>

**walter** <span style="color: grey; font-size: 90%;">19:44:39 UTC</span>

<span style="font-size: 90%;">but Ping will only work on windows</span>

**dune73** <span style="color: grey; font-size: 90%;">19:44:46 UTC</span>

<span style="font-size: 90%;">Ah, of course.</span>

**walter** <span style="color: grey; font-size: 90%;">19:45:42 UTC</span>

<span style="font-size: 90%;">we could similarly write a custom rule for this, to look for a pattern looking like a host (e.g. [example.com](http://example.com) or 1.2.3.4)</span>

**walter** <span style="color: grey; font-size: 90%;">19:46:08 UTC</span>

<span style="font-size: 90%;">and accept that one might ping local machines in the default search domain (with no dot), in exchange for the FP lowering</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:46:58 UTC</span>

<span style="font-size: 90%;">That would solve FPs, while still protecting from an attacker trying to determine if they can reach out to a command and control server.... But won't protect from them trying to enumerate local domain for other hosts</span>

**dune73** <span style="color: grey; font-size: 90%;">19:47:04 UTC</span>

<span style="font-size: 90%;">But that's an additional rule, is not it?</span>

**walter** <span style="color: grey; font-size: 90%;">19:47:05 UTC</span>

<span style="font-size: 90%;">exactly</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:47:46 UTC</span>

<span style="font-size: 90%;">it should include other ipv4 format like long/hex/etc..</span>

**dune73** <span style="color: grey; font-size: 90%;">19:48:12 UTC</span>

<span style="font-size: 90%;">Or several rules as this applies to multiple rules / FPs.</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:19 UTC</span>

<span style="font-size: 90%;">the good news about linux ping is that it really only accepts one argument</span>

**walter** <span style="color: grey; font-size: 90%;">19:48:45 UTC</span>

<span style="font-size: 90%;">but that would still trigger on ping pong :smile:</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:49:39 UTC</span>

<span style="font-size: 90%;">Could rule be written to specifically exclude only certain common usage "ping pong , ping them, ping a"</span>

**walter** <span style="color: grey; font-size: 90%;">19:49:56 UTC</span>

<span style="font-size: 90%;">on Windows sadly ping accepts multiple parameters</span>

**walter** <span style="color: grey; font-size: 90%;">19:50:00 UTC</span>

<span style="font-size: 90%;"></span>

**walter** <span style="color: grey; font-size: 90%;">19:50:52 UTC</span>

<span style="font-size: 90%;">too bad, I thought they stole these utilities from FreeBSD</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:51:14 UTC</span>

<span style="font-size: 90%;">Has Windows ignored everything after the first word though?</span>

**dune73** <span style="color: grey; font-size: 90%;">19:51:16 UTC</span>

<span style="font-size: 90%;">Is it worth it for a rare FP like ping pong?</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:28 UTC</span>

<span style="font-size: 90%;">maybe it’s not worth it…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:51:49 UTC</span>

<span style="font-size: 90%;">def. not imo :)</span>

**walter** <span style="color: grey; font-size: 90%;">19:51:54 UTC</span>

<span style="font-size: 90%;">since it’s a pretty dangerous command too for exploration of the local domain</span>

**walter** <span style="color: grey; font-size: 90%;">19:52:14 UTC</span>

<span style="font-size: 90%;">might be dangerous for us to try to work around it…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:52:54 UTC</span>

<span style="font-size: 90%;">maybe you can check anyway if a local/remote host is alive using other commands</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:01 UTC</span>

<span style="font-size: 90%;">I'd agree on that. People should be advise to write "table tennis".</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:53:10 UTC</span>

<span style="font-size: 90%;">lol</span>

**walter** <span style="color: grey; font-size: 90%;">19:53:23 UTC</span>

<span style="font-size: 90%;">yes we maybe we can write that to the log file</span>

**dune73** <span style="color: grey; font-size: 90%;">19:53:47 UTC</span>

<span style="font-size: 90%;">I'd welcome a PR in this direction.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:03 UTC</span>

<span style="font-size: 90%;">Let's look at 2139.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:39 UTC</span>

<span style="font-size: 90%;">I think the interpretation is right, the ctl statement should move down the chain, but even with it's present location Franziska could not reproduce.</span>

**dune73** <span style="color: grey; font-size: 90%;">19:54:44 UTC</span>

<span style="font-size: 90%;">What do we do?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:55:13 UTC</span>

<span style="font-size: 90%;">btw I would prefer to never include +E to logpart</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:55:39 UTC</span>

<span style="font-size: 90%;">nor request or response body should be included in audit logs</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:03 UTC</span>

<span style="font-size: 90%;">we do it quite often</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:56:14 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">19:56:22 UTC</span>

<span style="font-size: 90%;">but that could be just copypasting…</span>

**dune73** <span style="color: grey; font-size: 90%;">19:56:24 UTC</span>

<span style="font-size: 90%;">That is a valid argument, _@theMiddle_, yet when I want the audit log, which is rare, I want the bodies.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:00 UTC</span>

<span style="font-size: 90%;">hm yes but imo it’s safer if who need the body change the logparts config</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:57:16 UTC</span>

<span style="font-size: 90%;">instead of having it on rules</span>

**dune73** <span style="color: grey; font-size: 90%;">19:57:45 UTC</span>

<span style="font-size: 90%;">I agree on that. I do not really like CRS to manipulate the logging even if it's meaning well.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:57:54 UTC</span>

<span style="font-size: 90%;">I agree _@dune73_ that I want the bodies to debug stuff... But it does make things challenging in GDPR and PCI environments</span>

**dune73** <span style="color: grey; font-size: 90%;">19:58:45 UTC</span>

<span style="font-size: 90%;">So we could get rid of all the logpart stuff for the next release?</span>

**walter** <span style="color: grey; font-size: 90%;">19:59:17 UTC</span>

<span style="font-size: 90%;">it could deal with a good review at least. in some rules it seems to be nonsensical, for instance 920460</span>

**theMiddle** <span style="color: grey; font-size: 90%;">19:59:31 UTC</span>

<span style="font-size: 90%;">would be great</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">19:59:59 UTC</span>

<span style="font-size: 90%;">On the other hand if there was a breach, having the body logged is a really big advantage, as you are then more likely to be and to determine scope of breach</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:00:08 UTC</span>

<span style="font-size: 90%;">I’ve a preprocessing script that removes things like req body and resp body from logs</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:00:27 UTC</span>

<span style="font-size: 90%;">it’s a nightmare</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:06 UTC</span>

<span style="font-size: 90%;">_@Paul Beckett_, yes it is. But then that's the local decision.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:16 UTC</span>

<span style="font-size: 90%;">For the record: we are talking of 140 instances, here...</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:01:44 UTC</span>

<span style="font-size: 90%;">140 rules that adds +E ?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:01:55 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:01:59 UTC</span>

<span style="font-size: 90%;">wow!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:08 UTC</span>

<span style="font-size: 90%;">A ton of request rules trigger the logging of the response body.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:10 UTC</span>

<span style="font-size: 90%;">I think they make no sense in most cases.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:19 UTC</span>

<span style="font-size: 90%;">I guess so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:03:36 UTC</span>

<span style="font-size: 90%;">But then it's a big question and we should probably schedule it for the monthly meeting with more people in the room.</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:37 UTC</span>

<span style="font-size: 90%;">well, at least if you’re in blocking mode, the app never sees the requests</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:44 UTC</span>

<span style="font-size: 90%;">but of course some people run just in logging mode</span>

**walter** <span style="color: grey; font-size: 90%;">20:03:52 UTC</span>

<span style="font-size: 90%;">and THEN it might be interesting to see what the app said</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:04:37 UTC</span>

<span style="font-size: 90%;">Some people could also be running blocking but with threshold higher than an individual rule resulting in blocking.</span>

**walter** <span style="color: grey; font-size: 90%;">20:04:58 UTC</span>

<span style="font-size: 90%;">should we turn it into a crs-setup.conf parameter? seems easy to do</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:12 UTC</span>

<span style="font-size: 90%;">Auditlogparts?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:05:50 UTC</span>

<span style="font-size: 90%;">Like a commented out SecAction that does ctl:auditLogParts=+E?</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:00 UTC</span>

<span style="font-size: 90%;">something like that yeah!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:06:17 UTC</span>

<span style="font-size: 90%;">But is not that lame when there is a SecAuditLogParts directive?</span>

**walter** <span style="color: grey; font-size: 90%;">20:06:44 UTC</span>

<span style="font-size: 90%;">good point :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:13 UTC</span>

<span style="font-size: 90%;">yes</span>

**dune73** <span style="color: grey; font-size: 90%;">20:07:26 UTC</span>

<span style="font-size: 90%;">I propose we schedule that for the August meeting and close this issue.</span>

**walter** <span style="color: grey; font-size: 90%;">20:07:59 UTC</span>

<span style="font-size: 90%;">OK. though you already have me convinced that people should be making this choice for themselves in mod_security2.conf</span>

**dune73** <span style="color: grey; font-size: 90%;">20:08:36 UTC</span>

<span style="font-size: 90%;">Yes, I think that is more in line with our policies. Yet it's a big move and it has to be considered and explained in the release notes.</span>

**walter** <span style="color: grey; font-size: 90%;">20:08:57 UTC</span>

<span style="font-size: 90%;">there could be a case made for leaving the +E in the response rules.</span>

**walter** <span style="color: grey; font-size: 90%;">20:09:07 UTC</span>

<span style="font-size: 90%;">so yes, let’s discuss it with a wider audience</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:12 UTC</span>

<span style="font-size: 90%;">Cool</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:31 UTC</span>

<span style="font-size: 90%;">2140 then.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:09:42 UTC</span>

<span style="font-size: 90%;">100% agree. same thing should be done with logdata, prevent logging cookie string values and something like that :smile: but ok, one step at a time</span>

**dune73** <span style="color: grey; font-size: 90%;">20:09:53 UTC</span>

<span style="font-size: 90%;">We don't seem to detect path traversals with backslashes.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:10:09 UTC</span>

<span style="font-size: 90%;">Thoughts?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:10:46 UTC</span>

<span style="font-size: 90%;">Is this because t:cmdLine is mangling the input?</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:11:05 UTC</span>

<span style="font-size: 90%;">Or I may have misunderstood‥</span>

**walter** <span style="color: grey; font-size: 90%;">20:11:11 UTC</span>

<span style="font-size: 90%;">that’s strange</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:11:51 UTC</span>

<span style="font-size: 90%;">I'd be happy to investigate this one, but I admit I haven't tested it myself, yet</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:15 UTC</span>

<span style="font-size: 90%;">I recently did some work on path traversal rule, did I break it?</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:28 UTC</span>

<span style="font-size: 90%;">I thought we would have tests for this though</span>

**walter** <span style="color: grey; font-size: 90%;">20:12:57 UTC</span>

<span style="font-size: 90%;">930110</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:13:38 UTC</span>

<span style="font-size: 90%;">uhm cmdLine deletes all backslashes actually</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:18 UTC</span>

<span style="font-size: 90%;">do we even need that transformation in this rule?</span>

**walter** <span style="color: grey; font-size: 90%;">20:14:58 UTC</span>

<span style="font-size: 90%;">probably a 1 minute fix, shall i try it</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:24 UTC</span>

<span style="font-size: 90%;">If it's so easy, then it would be a good start for _@xanadu_</span>

**dune73** <span style="color: grey; font-size: 90%;">20:15:46 UTC</span>

<span style="font-size: 90%;">Especially, if you coach him.</span>

**walter** <span style="color: grey; font-size: 90%;">20:16:01 UTC</span>

<span style="font-size: 90%;">agreed! we should get an additional test for the false negative, and then see if the removal of the transformation passes the test</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:17:10 UTC</span>

<span style="font-size: 90%;">That sounds like a good plan</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:28 UTC</span>

<span style="font-size: 90%;">Cool. Thank you guys.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:17:48 UTC</span>

<span style="font-size: 90%;">2142: A potential addition for the WP RE package.</span>

**walter** <span style="color: grey; font-size: 90%;">20:18:51 UTC</span>

<span style="font-size: 90%;">I disagree with the OP’s solution, it seems much too wide…</span>

**walter** <span style="color: grey; font-size: 90%;">20:19:03 UTC</span>

<span style="font-size: 90%;">I thought my provided rule will/should be enough</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:11 UTC</span>

<span style="font-size: 90%;">I completely agree.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:22 UTC</span>

<span style="font-size: 90%;">Can we take your proposal in the RE package?</span>

**walter** <span style="color: grey; font-size: 90%;">20:20:32 UTC</span>

<span style="font-size: 90%;">yes, I don’t see why not!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:20:45 UTC</span>

<span style="font-size: 90%;">Who wants to take this on?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:21:09 UTC</span>

<span style="font-size: 90%;">it’s an easy and quick one, if no other wants I can</span>

**dune73** <span style="color: grey; font-size: 90%;">20:22:30 UTC</span>

<span style="font-size: 90%;">Thank you.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:23:03 UTC</span>

<span style="font-size: 90%;">Are we concerned that endsWith could allow for bypass of those rules?</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:23:41 UTC</span>

<span style="font-size: 90%;">Assuming attacker is trying to get PHP info and can write to arbitrary final path</span>

**dune73** <span style="color: grey; font-size: 90%;">20:24:14 UTC</span>

<span style="font-size: 90%;">What do you think Walter, you're the expert here.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:24:29 UTC</span>

<span style="font-size: 90%;">we can use contains</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:25:09 UTC</span>

<span style="font-size: 90%;">uhm but doesn’t help much</span>

**walter** <span style="color: grey; font-size: 90%;">20:25:25 UTC</span>

<span style="font-size: 90%;">hmmm, I don’t mind so much…</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:25:53 UTC</span>

<span style="font-size: 90%;">It wouldn't affect me as I delete all the exclusion rules, but thinking of users who leave all the exclusion rules in even if they're not relevant to what they are hosting</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:03 UTC</span>

<span style="font-size: 90%;">I think in most cases people would want to attack a specific filename and our requirement that it ends with this string would thwart it</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:25 UTC</span>

<span style="font-size: 90%;">of course there’s the path info problem in vanilla PHP sites…</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:27:48 UTC</span>

<span style="font-size: 90%;">is it a default thing in PHP?</span>

**walter** <span style="color: grey; font-size: 90%;">20:27:50 UTC</span>

<span style="font-size: 90%;">so it’s a valid comment</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:01 UTC</span>

<span style="font-size: 90%;">it’s really a tradeoff</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:15 UTC</span>

<span style="font-size: 90%;">yeah, I think it’s default, at least in Apache with mod_php</span>

**walter** <span style="color: grey; font-size: 90%;">20:28:38 UTC</span>

<span style="font-size: 90%;">you can do index.php/wp-admin/site-health.php</span>

**dune73** <span style="color: grey; font-size: 90%;">20:28:46 UTC</span>

<span style="font-size: 90%;">OK in light of the time progressing, can we postpone this policy question?</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:22 UTC</span>

<span style="font-size: 90%;">can we do regexps on the response?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:29:33 UTC</span>

<span style="font-size: 90%;">I thought was an old default thing. If I’m not wrong this doesn’t work with nginx+fastcgi/php-fpm</span>

**dune73** <span style="color: grey; font-size: 90%;">20:29:40 UTC</span>

<span style="font-size: 90%;">On RESPONSE_BODY?</span>

**walter** <span style="color: grey; font-size: 90%;">20:29:44 UTC</span>

<span style="font-size: 90%;">yes</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:04 UTC</span>

<span style="font-size: 90%;">then we could make a chain that actually ensures this is a WordPress response page, by looking for some known output</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:30:24 UTC</span>

<span style="font-size: 90%;">but in phase:4</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:34 UTC</span>

<span style="font-size: 90%;">oh yeah of course</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:36 UTC</span>

<span style="font-size: 90%;">I’m talking nonsense</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:44 UTC</span>

<span style="font-size: 90%;">or am I?</span>

**walter** <span style="color: grey; font-size: 90%;">20:30:45 UTC</span>

<span style="font-size: 90%;">it might work</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:31:01 UTC</span>

<span style="font-size: 90%;">the blocks occurs on phase:2 or am I wrong?</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:12 UTC</span>

<span style="font-size: 90%;">ah… yes it does of course</span>

**dune73** <span style="color: grey; font-size: 90%;">20:31:29 UTC</span>

<span style="font-size: 90%;">I guess it's getting late... :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:29 UTC</span>

<span style="font-size: 90%;">or, no</span>

**walter** <span style="color: grey; font-size: 90%;">20:31:56 UTC</span>

<span style="font-size: 90%;">it’s a phase 4 rule</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:30 UTC</span>

<span style="font-size: 90%;">anyway! looking for WordPress strings in the output could prevent this from being abused in other apps</span>

**walter** <span style="color: grey; font-size: 90%;">20:32:42 UTC</span>

<span style="font-size: 90%;">I like the idea, could be worth exploring</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:33:05 UTC</span>

<span style="font-size: 90%;">anyway, I save a note for me on the issue to add _@walter_ rule version to WP RE or should we think about it?</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:25 UTC</span>

<span style="font-size: 90%;">if you would like to experiment with it, that would be cool</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:31 UTC</span>

<span style="font-size: 90%;">do you have access to a WordPress panel?</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:33:38 UTC</span>

<span style="font-size: 90%;">yep</span>

**walter** <span style="color: grey; font-size: 90%;">20:33:48 UTC</span>

<span style="font-size: 90%;">ok then you can find a good code snippet in the site health page</span>

**dune73** <span style="color: grey; font-size: 90%;">20:34:57 UTC</span>

<span style="font-size: 90%;">Sounds cool.</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:35:02 UTC</span>

<span style="font-size: 90%;"></span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:35:08 UTC</span>

<span style="font-size: 90%;">I need an upgrade :smile: but ok</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:36:17 UTC</span>

<span style="font-size: 90%;">Could we do beginsWith, and use a user configurable variable to handle cases where the have a prefix before /wp-admin?</span>

**dune73** <span style="color: grey; font-size: 90%;">20:36:59 UTC</span>

<span style="font-size: 90%;">I think beginsWith does not work with variables in the argument.</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:37:14 UTC</span>

<span style="font-size: 90%;">Ah, sorry</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:16 UTC</span>

<span style="font-size: 90%;">that could already be achieved by something like:
SecRule REQUEST_FILENAME "@beginsWith /blog/" \
 "id:1234,phase:1,t:none,nolog,pass,setvar:tx.crs_exclusions_wordpress=1"Maybe we should put this in a FAQ….</span>

**walter** <span style="color: grey; font-size: 90%;">20:38:50 UTC</span>

<span style="font-size: 90%;">I am too lazy to set this for every blog but I think it would work</span>

**dune73** <span style="color: grey; font-size: 90%;">20:39:43 UTC</span>

<span style="font-size: 90%;">Nice one. Never thought about this.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:40:12 UTC</span>

<span style="font-size: 90%;">It's getting really late. I think we call it a day. 1991 has been an intense discussion.</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:23 UTC</span>

<span style="font-size: 90%;">yes thank you, I’m super tired already :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:30 UTC</span>

<span style="font-size: 90%;">but we had some good ideas</span>

**walter** <span style="color: grey; font-size: 90%;">20:40:37 UTC</span>

<span style="font-size: 90%;">it was a productive chat</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:24 UTC</span>

<span style="font-size: 90%;">bye everyone!</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:27 UTC</span>

<span style="font-size: 90%;">Think so too.</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:35 UTC</span>

<span style="font-size: 90%;">Thank you everybody for joining!</span>

**theMiddle** <span style="color: grey; font-size: 90%;">20:42:37 UTC</span>

<span style="font-size: 90%;">good nite all!</span>

**walter** <span style="color: grey; font-size: 90%;">20:42:51 UTC</span>

<span style="font-size: 90%;">I will spend more time on my assigned issues this month :slightly_smiling_face:</span>

**dune73** <span style="color: grey; font-size: 90%;">20:42:54 UTC</span>

<span style="font-size: 90%;">And hope you have some sunny days. Summer just started in Switzerland this weekend!</span>

**walter** <span style="color: grey; font-size: 90%;">20:43:07 UTC</span>

<span style="font-size: 90%;">yes it seems the weather is picking up now!</span>

**Paul Beckett** <span style="color: grey; font-size: 90%;">20:43:39 UTC</span>

<span style="font-size: 90%;">Had a sunny week here in the UK</span>

**xanadu** <span style="color: grey; font-size: 90%;">20:44:01 UTC</span>

<span style="font-size: 90%;">Too sunny. Bring on the Autumn :laughing:</span>

