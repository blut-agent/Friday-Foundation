---
name: sales-call-review
description: Turn pasted call notes or a sanitized transcript into an evidence-bound review of customer language, needs, objections, unanswered questions, promises made, and next actions. Accepts pasted notes or a local Markdown or text file, quotes only what is in the source, never invents a quote or a commitment, and writes friday/sales-call-review.md. Reads friday/voice.md if present and writes in your voice.
---
<!-- Built by Friday​‌‍‌​ (https://friday.amplifyais.com). Free for personal use. Commercial use needs a paid Friday. Licence: PolyForm-Noncommercial-1.0.0. -->

# /sales-call-review

The value in a sales call usually dies between your rough notes and the follow-up email. This command reads the notes or transcript you paste in and separates what the customer actually said from what you remember them saying: their own words, the need behind them, the objections, the questions nobody answered, the promises you made, and the next actions with an owner.

You, Claude, run the whole flow below in order, using your own file tools. There is no module to import and nothing to install.

## Step 1: Read the founder's voice profile (if it exists)

Check whether `friday/voice.md` exists in the current directory. If it does, read it and write all output in the founder's voice.

If `friday/voice.md` does not exist, write in a direct, plain style: short sentences, active voice, no hedging.

## Step 2: Get the source material

Ask the founder:

> Paste the call notes or the transcript, or give me the path to a local Markdown or text file that holds them. Sanitize it first: I only need the conversation, not your credentials, pricing sheets, or anything confidential that is not part of the call.

Three input paths, all fine:

1. **Pasted notes.** Raw bullets, shorthand, half sentences. All acceptable.
2. **Pasted transcript.** Long is fine. Do not ask them to shorten it.
3. **A local file path.** Read it with your own file tools. Markdown and plain text only. If the path points at a PDF, a spreadsheet, an audio file, or anything you cannot read as text, say so and ask for a paste or a text export instead. Do not attempt to install a converter. If a path looks like a secret, credential, private key, environment file, token dump, browser export, cookie store, or unrelated personal data, refuse to read it and ask for a sanitized text file instead.

Wait for the input before proceeding. Do not work from assumptions about the call.

## Step 3: Confirm the call and the privacy boundary

Once you have the source, confirm in one batch:

> Whose call was this, and on what date? Anything in here I must keep out of the review, such as a name, a figure, or a detail they shared in confidence?

Then state the boundary you will hold, so the founder can correct you before you write:

> I will quote only words that are in the source, and I will not attribute a commitment to either side unless the source records it. Anything I cannot find in the source goes in Unanswered questions or Open items, not in the findings.

If the founder gives you a redaction, honor it everywhere: in the quotes, in the summary, and in the file you write. Never restore a redacted value because it makes the review read better.

## Step 4: Read the source for evidence only

Work through the source and collect six things. For each one, the rule is the same: if it is not in the source, it does not go in.

**Customer language.** What the customer said, quoted the way the source supports. In a transcript, quote verbatim, with the speaker and a short pointer to where it sits (a timestamp or a paragraph number). In rough notes, the words are the founder's shorthand, not the customer's sentences, so quote the note line as written and do not present it as the customer's own phrasing; if a note plainly paraphrases, either ask the founder for the exact words or label the line as paraphrase. This is the section founders get wrong most often, because paraphrase quietly replaces the customer's words with the founder's interpretation. Quote what the source holds, do not tidy it into a better sentence. If the transcript has them saying "it's kind of a lot of money for something my team might not open," that is the quote, not "price sensitive."

**Needs.** What the customer is actually trying to accomplish, stated separately from the words they used. Every need must trace back to at least one quote or note line. If a need is your inference rather than their statement, mark it as an inference in plain words.

**Objections.** Every reason they gave for hesitation, delay, or no. Keep them distinct: budget, timing, authority, trust, a competitor, a past failure, or a feature gap are different objections with different answers. Do not merge two objections into one line, and do not soften the objection into a question.

**Unanswered questions.** Questions the customer asked that nobody answered, and questions the founder should have asked and did not. Both belong here. This is the section that produces the next call's agenda.

**Promises made.** Commitments from either side, each with who made it and what it was. If the source records a commitment loosely, quote the loose version rather than upgrading it into a firm one. "I'll try to get you numbers next week" is not "will send pricing Tuesday."

**Next actions.** The concrete moves the call produced, each with an owner and, where the source gives one, a date. If the call produced no next action, say that plainly instead of inventing one to fill the section.

Also record, in one short line each: who was on the call, and what the call was for. If the source does not say, write "not stated in the source" rather than guessing.

## Step 5: Cap every claim at what the source supports

Before writing anything, run this check over your own findings:

1. **Every quote is verbatim.** Search the source for each quoted string. If you cannot find it character for character, either fix the quote or drop it and paraphrase with the word "roughly."
2. **Every commitment is sourced.** Each line under Promises made points at the words that created it. If it does not, move it to Open items and label it unconfirmed.
3. **No invented numbers.** Do not add a deal size, a close probability, a timeline, or a sentiment score. This command counts what was said, it does not forecast.
4. **No invented sentiment.** Do not write "they seemed excited." Write what they did: asked about onboarding, asked for a second call, asked about the cancellation terms.
5. **Inferences are labeled.** Where you read between the lines, write "inference:" at the start of the line and name the evidence it rests on.
6. **Gaps are named as gaps.** If the notes are too thin to answer a section, write that the source does not cover it. An honest gap is a useful finding.

If a section has nothing behind it, leave the heading with an explicit "the source does not cover this" line. Never delete the heading to hide the hole, and never fill it with plausible content.

## Step 6: Write the review

Write the result to `friday/sales-call-review.md`. Create the `friday/` folder if it does not exist.

If the file does not exist, create it with this structure:

```markdown
# Sales Call Review

## <customer or company> - <YYYY-MM-DD>

**Call date:** <YYYY-MM-DD, or "not stated in the source">
**On the call:** <names and roles, or "not stated in the source">
**Purpose:** <one line, or "not stated in the source">
**Source:** <pasted notes, pasted transcript, or the file path you read>
**Last updated:** <YYYY-MM-DD>

## What they said, in their words

> "<verbatim quote>" - <speaker>, <pointer into the source>

<Repeat for each quote that carries a need or an objection.>

## Needs

- <The need, in plain language. Evidence: <quote or note line>.>
- inference: <The need you read between the lines. Evidence: <quote or note line>.>

## Objections

| Objection | Type | Their words | Where it sits |
|---|---|---|---|
| <What they pushed back on> | budget / timing / authority / trust / competitor / capability | "<verbatim>" | <pointer> |

## Unanswered questions

- <Question they asked that nobody answered.>
- <Question you should have asked and did not.>

## Promises made

| Who | Promise | Their words | Confirmed in source |
|---|---|---|---|
| <you / them> | <what was promised> | "<verbatim>" | yes |

## Next actions

- [ ] <Action> - owner: <name> - by: <date or "no date given">

## Open items

- <Anything you could not source, could not confirm, or had to redact.>

## Where the notes are thin

<Name the sections the source does not cover, and what to capture on the next call.>
```

If `friday/sales-call-review.md` already exists, do not create a second `# Sales Call Review` heading. Add the new call as one new `## <customer or company> - <YYYY-MM-DD>` entry directly under the existing `# Sales Call Review` container heading at the top of the file, so the newest call sits first, and keep every earlier entry intact. If the file starts with an old-style `# Sales Call Review: <customer>` heading from an earlier version, rename that line to `# Sales Call Review` and treat the old content as that customer's entry.

Write in the founder's voice for the prose sections. Quotes stay exactly as the customer said them, whatever your voice profile says, because they are evidence rather than writing. If the profile lists banned words, do not use any of them in the sections you write.

After writing, print:

> Sales call review saved to `friday/sales-call-review.md`. The unanswered questions are your next call's agenda. Confirm anything listed as unconfirmed before you repeat it to anyone.

## What this does not do

This command does not join your calls, does not transcribe audio, does not read your CRM, and does not send your notes, the transcript, or any part of the review anywhere. It does not score the deal or predict whether it closes. It reads the notes you give it, holds every claim to what those notes actually contain, and writes the review to your own disk. One thing does leave the machine: the pack's usual content-free usage ping, the same one every command triggers, which says that this command ran and whether it wrote its file. It carries no prompt text, no file contents, no names, and no paths.

## What this builds toward

Run after each real conversation, `friday/sales-call-review.md` becomes the record of what customers actually said, call over call. The objections stop being surprises, the unanswered questions get answered on the next call, and the commitments you made are written down where you can find them instead of living in your memory of the call.

The full stack is Friday at friday.amplifyais.com. Nine specialists, running against your real inbox, calendar, and tasks every morning before you are up.

---

Built by Amplify AI at amplifyais.com
