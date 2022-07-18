### Mon, Jul 18th, 2022

**walter** <span style="color: grey; font-size: 90%;">18:30:38 UTC</span>

<span style="font-size: 90%;">I’m sorry but I have to skip today. We have a go-live for a project tomorrow and I have to get some high-prio issues fixed, so I need my concentration…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:30:59 UTC</span>

<span style="font-size: 90%;">Hey hey!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:17 UTC</span>

<span style="font-size: 90%;">Well… sorry to hear that so many heavy weights are out today</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:20 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:31:28 UTC</span>

<span style="font-size: 90%;">Let’s keep the meet short then</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:31:55 UTC</span>

<span style="font-size: 90%;">Hello!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:02 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:32:13 UTC</span>

<span style="font-size: 90%;">hello!</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:32:16 UTC</span>

<span style="font-size: 90%;">How's the weather in Uruguay? :grinning:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:31 UTC</span>

<span style="font-size: 90%;">Cold as hell</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:32:38 UTC</span>

<span style="font-size: 90%;">Which is a conundrum</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:33:23 UTC</span>

<span style="font-size: 90%;">But yeah, at least there is some sun out there</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:33:28 UTC</span>

<span style="font-size: 90%;">he is it super hot in Germany :sweat:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:33:51 UTC</span>

<span style="font-size: 90%;">One of the hottest days in recorded history today in the UK.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:01 UTC</span>

<span style="font-size: 90%;">38?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:34:05 UTC</span>

<span style="font-size: 90%;">Yeah</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:09 UTC</span>

<span style="font-size: 90%;">:scream:</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:34:22 UTC</span>

<span style="font-size: 90%;">Apparently France is bad, too.</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:34:25 UTC</span>

<span style="font-size: 90%;">And Portugal.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:34:49 UTC</span>

<span style="font-size: 90%;">Well, please keep hydrated, people!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:21 UTC</span>

<span style="font-size: 90%;">On the agenda side, I’ve added some issues to cover, but nothing crazy</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:35:50 UTC</span>

<span style="font-size: 90%;">One general comment from my side is that we need to keep updating our lists.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:12 UTC</span>

<span style="font-size: 90%;">The good thing is that there are 5 PRs waiting to be merged for general updates</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:36:27 UTC</span>

<span style="font-size: 90%;">So things keep evolving</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:19 UTC</span>

<span style="font-size: 90%;">And we discovered a nice way to get things like python/php/gcc/etc with versioning in the lists (e.g. python3.10)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:37:39 UTC</span>

<span style="font-size: 90%;">Will be easier to propagate to other places also</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:38:02 UTC</span>

<span style="font-size: 90%;">Max is working on doing some fixes to the regexp-assemble script</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:02 UTC</span>

<span style="font-size: 90%;">And we keep updating/creating issues with the findings from the BB program, so let’s dive into the ones we selected for today</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:39:37 UTC</span>

<span style="font-size: 90%;">First is [#2562](https://github.com/coreruleset/coreruleset/issues/2562)</span>§

**fzipitria** <span style="color: grey; font-size: 90%;">18:40:25 UTC</span>

<span style="font-size: 90%;">_@xanadu_ I understand that we want to have the new variable set, right?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:41:55 UTC</span>

<span style="font-size: 90%;">Yes. So, the rule is to block archives like .xz, .bz2 etc. The question is:
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:15 UTC</span>

<span style="font-size: 90%;">Yeah, something like setvar:'tx.restricted_extensions=%{tx.restricted_extensions} %{tx.restricted_extensions_archives} ?</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:26 UTC</span>

<span style="font-size: 90%;">Yes</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:42:31 UTC</span>

<span style="font-size: 90%;">But at PL2</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:42:44 UTC</span>

<span style="font-size: 90%;">Then maybe it is better to have a new rule</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:43:02 UTC</span>

<span style="font-size: 90%;">I tend to agree. A new rule is simpler and easier to disable if you don't need it or want it.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:26 UTC</span>

<span style="font-size: 90%;">Then we can call it a “sibling” rule and document it properly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:43:50 UTC</span>

<span style="font-size: 90%;">I think it will be easier to manage also</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:38 UTC</span>

<span style="font-size: 90%;">It was mentioned in the issue also, that doing variable initialisation based on PL would be something completely new to the project…</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:44:59 UTC</span>

<span style="font-size: 90%;">So maybe it's based to keep it simple anyway. Especially for integrators.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:45:26 UTC</span>

<span style="font-size: 90%;">Ok. And we should get the .axd back to the list</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:46:13 UTC</span>

<span style="font-size: 90%;">Okay, cool. I'm happy to implement those decisions. I'll get it done before the next meeting.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:16 UTC</span>

<span style="font-size: 90%;">Do you think you can push those changes?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:20 UTC</span>

<span style="font-size: 90%;">Excellent, thanks.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:46:57 UTC</span>

<span style="font-size: 90%;">Next I’ve added [#2621](https://github.com/coreruleset/coreruleset/issues/2621), so everyone can take a look on the remaining</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:14 UTC</span>

<span style="font-size: 90%;">I think I managed to not get all the files needed to update there</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:47:57 UTC</span>

<span style="font-size: 90%;">Also I’ve learned that we have the same pattern in many different files, likes the unix cmds we use in 932100, 932105 and 932150 (and possibly others)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:24 UTC</span>

<span style="font-size: 90%;">Maybe for those a more holistic view will help instead</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:48:52 UTC</span>

<span style="font-size: 90%;">And we can leverage the use of the include functionality that regexp-assembly has now</span>

**xanadu** <span style="color: grey; font-size: 90%;">18:49:06 UTC</span>

<span style="font-size: 90%;">Ooh</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:49:24 UTC</span>

<span style="font-size: 90%;">It is already difficult to maintain one list… but having three with very similar things is a lost cause</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:50:42 UTC</span>

<span style="font-size: 90%;">Anyway, will do a full pass on lists other that the ones in the rules subdirectory</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:51:40 UTC</span>

<span style="font-size: 90%;">We need people to start picking those. _@emphazer_ asked me for advice, and I can take a walk on how my process was for some of the files in a separate meeting, if needed</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:52:10 UTC</span>

<span style="font-size: 90%;">good idea</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:22 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:52:43 UTC</span>

<span style="font-size: 90%;">So i’ll send some dates where people can join and we can go over one</span>

**emphazer** <span style="color: grey; font-size: 90%;">18:53:09 UTC</span>

<span style="font-size: 90%;">this would be very helpful</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:14 UTC</span>

<span style="font-size: 90%;">Next: [#2680](https://github.com/coreruleset/coreruleset/issues/2680)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:53:47 UTC</span>

<span style="font-size: 90%;">i think the last pending plugin we have before v4 is this.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:54:30 UTC</span>

<span style="font-size: 90%;">Was hoping _@studersi_ was around, to see if he has spare cycles :smile: .</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:55:53 UTC</span>

<span style="font-size: 90%;">Being a parallel task that doesn’t need to be tracked with things from the BB, but is needed for v4 would be a thing he might like</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:56:28 UTC</span>

<span style="font-size: 90%;">For the moment, I’ll add a comment to see if he wants to pick this one.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:06 UTC</span>

<span style="font-size: 90%;">For the next one, I’ve added a PR (yes, I know)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:58:14 UTC</span>

<span style="font-size: 90%;">So [#2676](https://github.com/coreruleset/coreruleset/issues/2676).</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:02 UTC</span>

<span style="font-size: 90%;">There are additional ones that we would like people to :eyes: and see if they can be merged</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:20 UTC</span>

<span style="font-size: 90%;">List updates are simpler that BB reviews, so anyone can do those</span>

**fzipitria** <span style="color: grey; font-size: 90%;">18:59:35 UTC</span>

<span style="font-size: 90%;">But we need people to do the review</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:01 UTC</span>

<span style="font-size: 90%;">I can tell you how I normally do this, so if you want to double check</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:27 UTC</span>

<span style="font-size: 90%;">The gh tool is cool helper for this</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:00:53 UTC</span>

<span style="font-size: 90%;">You can use the gh pr checkout 2676, for example</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:02 UTC</span>

<span style="font-size: 90%;">(any PR number will work)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:17 UTC</span>

<span style="font-size: 90%;">That will crate a local branch and get it locally</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:01:39 UTC</span>

<span style="font-size: 90%;">Then one thing I always do is check that the regular expression is updated</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:22 UTC</span>

<span style="font-size: 90%;">./util/regexp-assemble/regexp-assemble.py update 932100 in this case</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:40 UTC</span>

<span style="font-size: 90%;">If there is a difference, files will be changed and you need to comment on the ticket</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:02:53 UTC</span>

<span style="font-size: 90%;">This might be a quick good thing to add on the pipeline :thinking_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:20 UTC</span>

<span style="font-size: 90%;">And then playing with the tests before approval</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:23 UTC</span>

<span style="font-size: 90%;">It's easy to update a .data file and forget to update the pattern in the rule :grimacing:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:03:36 UTC</span>

<span style="font-size: 90%;">A check would be good.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:40 UTC</span>

<span style="font-size: 90%;">Indeed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:03:55 UTC</span>

<span style="font-size: 90%;">Will create a ticket for that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:22 UTC</span>

<span style="font-size: 90%;">Anyway: anyone can help with approvals also, so we keep merging things</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:37 UTC</span>

<span style="font-size: 90%;">We have still way too many PRs open</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:04:50 UTC</span>

<span style="font-size: 90%;">It slows progress, we need rebases, etc</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:15 UTC</span>

<span style="font-size: 90%;">Last one [#2625](https://github.com/coreruleset/coreruleset/issues/2625)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:05:55 UTC</span>

<span style="font-size: 90%;">This is a very specific issue, not coming from the BB</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:30 UTC</span>

<span style="font-size: 90%;">And it is a good candidate that complements our mysql error detection.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:06:58 UTC</span>

<span style="font-size: 90%;">Who wants to dive into it? _@emphazer_ what do you think?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:08:32 UTC</span>

<span style="font-size: 90%;">i have to check</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:08:55 UTC</span>

<span style="font-size: 90%;">Sure, can we assign it to you?</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:09:01 UTC</span>

<span style="font-size: 90%;">sure</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:08 UTC</span>

<span style="font-size: 90%;">Remember you are not alone, and we can interact as you want!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:09:15 UTC</span>

<span style="font-size: 90%;">looks interesting</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:29 UTC</span>

<span style="font-size: 90%;">Indeed!</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:36 UTC</span>

<span style="font-size: 90%;">How are word lists being automated?</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:09:41 UTC</span>

<span style="font-size: 90%;">Is there a standard approach?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:09:57 UTC</span>

<span style="font-size: 90%;">Well, depends a lot on where the lists come from</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:06 UTC</span>

<span style="font-size: 90%;">If they come from GH, then we might</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:10:17 UTC</span>

<span style="font-size: 90%;">Ok.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:10:58 UTC</span>

<span style="font-size: 90%;">The most important part is the documentation itself</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:15 UTC</span>

<span style="font-size: 90%;">For example, this is a semi-automated process that I did for php errors</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:11:28 UTC</span>

<span style="font-size: 90%;"># The contents of this list come from the [PHP source code]([https://github.com](https://github.com):php/php-src).

There are different types of errors that might be thrown. An easy way to discover them is to
get any text that comes from the error handling functions: `zend_error`, `zend_throw_error`, `soap_error0`, etc.
Using the regexp `_error([0-9])?\(` will give you all. And you can see them using:
`grep -h -E -r -o --exclude="*.phpt" '\w+_error([0-9])?\(' * | sort | uniq`

After getting the list, there are two different types of errors: those with literal text, and those that include
print format args like `%s`, `%d`, `%zu`, etc. We sort them in two groups.

The first group is just anything without formatting args. Only text, sorted ascending. Command used:
  - `grep -E -h -r --exclude="*.phpt" '_error([0-9])?\(' * | awk -F\" '{ print $2;} ' | sed -e 's/ \\$/ "/g' | sort | uniq | grep -v '%'`
Post processing might be necessary to adjust strings that can cause false positives, such as
- line is very short
- line is a (partial) common English sentence, like `Can use`, `Attribute`, etc.
- text coming from php unit/regression tests, like 'DROP TABLE IF EXISTS test_bug_71863`

The second group will be the part with format strings. Only text, sorted ascending.
This will need a more careful processing. The format string will appear in the text result,
but it will (of course) be substituted by some variable value. So we need to clean more text here.
The easiest way is to split a line whenever a format string is found. This will shorten the texts but,
then we can sort out the ones we don't want to include more easily.
We also remove:
- text with just one word (likely to be FP), or one word, one space (optional) and one non-word (optional),
  which will match things like `Collect "`, `Method` or `Class `.
Command used:
  - `grep -E -h -r --exclude="*.phpt" '_error([0-9])?\(' * | awk -F\" '/%/ { print $2;} ' | sed -e 's/ \\$/ "/g' -e 's/%[zlp][ud]/\n/g' -e 's/%[a-z]/\n/g'  -e 's/%\.\*s/\n/g' | sort | uniq | grep -E -v '^\w+\s?\W?$' | grep -E -v '^\W+$'

Anything that is too short, or nonsense, we remove.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:12 UTC</span>

<span style="font-size: 90%;">That's useful to know that shell scripts are an acceptable way to do this.</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:12:16 UTC</span>

<span style="font-size: 90%;">Seems like a good idea to me.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:13:13 UTC</span>

<span style="font-size: 90%;">There are more examples</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:14:58 UTC</span>

<span style="font-size: 90%;">Another one:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:01 UTC</span>

<span style="font-size: 90%;"># This list has generic unix shell variables, shells and commands that affect Unix systems.
To generate the list, we get the data from all places first. Strip or add the path to commands so it begins with `bin`.
Sort the file content ascending, and remove duplicate lines.

Data comes from multiple places, listed below.
- Binaries:
  - GTFOBins. Update list using `curl -H "Accept: application/vnd.github.v3+json" [https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins](https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins) | jq '.[].name' | grep '.md' | tr -d '"' | cut -f1 -d.`
- Shell lists:
  - [https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html)
  - [https://en.wikipedia.org/wiki/Unix_shell](https://en.wikipedia.org/wiki/Unix_shell)
  - [https://hyperpolyglot.org/unix-shells](https://hyperpolyglot.org/unix-shells)
- Generic shell variables (Ad-Hoc for now, needs references)
- Generic /etc and /dev files (Ad-Hoc, needs references)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:35 UTC</span>

<span style="font-size: 90%;">There I got the list from GTFOBins with a curl call</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:15:48 UTC</span>

<span style="font-size: 90%;">so it’s easier in the future to update</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:18:19 UTC</span>

<span style="font-size: 90%;">Ok, that’s all what I’ve got in the list for the people that I knew were going to be around</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:18:37 UTC</span>

<span style="font-size: 90%;">this looks very good</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:19:13 UTC</span>

<span style="font-size: 90%;">it would be just sad if the sources change....</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:29 UTC</span>

<span style="font-size: 90%;">Well, that’s why we need to do quarterly checks</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:21:46 UTC</span>

<span style="font-size: 90%;">And this is like anything else: it is our duty to be updated.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:22:05 UTC</span>

<span style="font-size: 90%;">Hopefully the community here can nudge us (and/or help us) with this update</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:22:54 UTC</span>

<span style="font-size: 90%;">There are still things that anyone here can help. For example java code leakages, etc</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:13 UTC</span>

<span style="font-size: 90%;">Even adding a source site in the comments helps us to do the update</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:23:37 UTC</span>

<span style="font-size: 90%;">So we keep encouraging people to help how they can, even it it is not writing rules!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:08 UTC</span>

<span style="font-size: 90%;">I will take notes and create issues for those decisions here.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:31 UTC</span>

<span style="font-size: 90%;">With that, see you next one!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">19:24:39 UTC</span>

<span style="font-size: 90%;">Good night everyone! :wave:</span>

**xanadu** <span style="color: grey; font-size: 90%;">19:24:44 UTC</span>

<span style="font-size: 90%;">Night!</span>

**emphazer** <span style="color: grey; font-size: 90%;">19:25:13 UTC</span>

<span style="font-size: 90%;">good night!</span>

