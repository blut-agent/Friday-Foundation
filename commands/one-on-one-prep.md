---
name: one-on-one-prep
description: Prepares you for a one-on-one from pasted notes, open topics, feedback, and the outcome you want. Captures the person, relationship context, unresolved topics, the feedback you owe, and the questions worth asking. Writes to friday/one-on-ones/<person>.md. Reads friday/voice.md if present and writes in your voice.
---
<!-- Built by Friday​‌‍‌​ (https://friday.amplifyais.com). Free for personal use. Commercial use needs a paid Friday. Licence: PolyForm-Noncommercial-1.0.0. -->

# /one-on-one-prep

A one-on-one fails when it is an agenda with no context. This command turns what you already know, the topics still open from last time, the feedback you owe someone, and the outcome you want into a brief you can walk in with. Written in your voice and saved to disk.

You, Claude, run the whole flow below in order, using your own file tools. There is no module to import and nothing to install.

## Step 1: Read the founder's voice profile (if it exists)

Check whether `friday/voice.md` exists in the current directory. If it does, read it.

From the profile, note:
- Their tone and rhythm.
- Their signature phrases.
- Their banned words list. You must not use any word on that list in any output from this command.

If `friday/voice.md` does not exist, write in a neutral, direct style: short sentences, no hedging, active voice.

## Step 2: Capture the one-on-one inputs

Ask the founder for all five of these in one message, then wait for the answer:

1. **The person.** Their name and what they do.
2. **Relationship context.** How long you have worked together, what they own, and where the relationship stands. Two or three sentences is enough.
3. **Open topics.** Anything left unresolved since you last spoke, and what you agreed at the time.
4. **Feedback.** What you owe them: something working well, something to change, or both.
5. **Desired outcome.** The one thing that would make this conversation worth having.

Wait for their input before proceeding. You do not have access to their calendar, their messages, or their HR system. Everything comes from what they paste in.

Do not start writing until you have at least the person and the desired outcome. If either is missing, ask again rather than filling the gap yourself.

## Step 3: Separate what is stated from what is assumed

Label every input before you write:

- **Stated:** the founder said it or pasted it.
- **Assumed:** you inferred it.

Do not fabricate context, history, sentiment, or quotes. If the founder did not say how the person is feeling, do not guess. If a field is missing, write `not given` rather than inventing a plausible answer.

If the relationship context is thin, say so plainly in the brief and name what would be useful to know before the conversation.

## Step 4: Write the one-on-one brief

Use this structure. Keep the founder's voice throughout.

```
## One-on-One: <person> - <YYYY-MM-DD>

### The person and the relationship

<Two or three sentences on who they are, what they own, and where things stand. Mark anything you assumed.>

### What is open from last time

<Each unresolved topic on its own line: what was raised, what was decided, what is still hanging. Write "Nothing recorded" if the founder gave none.>

### Feedback to give

<What is working and what needs to change. Specific and behavioural. Name the moment, not the personality.>

### The outcome you want

<One sentence. The specific thing that makes this conversation a win: a decision made, a commitment given, a concern cleared. Not a vague intention.>

### Questions worth asking

1. <A question that opens something real rather than asking for a status update.>
2. <A second angle on the outcome you want. Not a version of question one.>
3. <The one you would ask if you only had sixty seconds.>

### Commitments to leave with

<Each commitment on its own line with an owner and, where the founder gave one, a date. Leave anything else as "to be agreed" rather than assuming it.>
```

Keep the sections the founder gave you material for. If there is no feedback to give, leave that section out rather than writing something empty. Do not pad the questions. Three is the number, and each one should earn its place.

## Step 5: Save the brief

Write the full brief to `friday/one-on-ones/<person>.md` in the current directory, where `<person>` is the person's name in lowercase with hyphens instead of spaces. Create the `friday/` folder if it does not exist. Create the `friday/one-on-ones/` folder if it does not exist.

One file per person, so the next conversation starts where the last one ended. If the file already exists, append the new brief under a `---` separator rather than overwriting what is there.

After writing, print:

- One-on-one brief saved to `friday/one-on-ones/<person>.md`.
- That file now holds every one-on-one with this person, so the open topics and the commitments line up across sessions.

## What this does not do

This command does not message the person, schedule the meeting, or send anything anywhere. It does not read your calendar, your messages, or your notes unless you paste them in.

It does not invent personal context. Nobody's state of mind, performance history, or intent gets guessed at, because a brief built on invention is worse than no brief at all.

---

Built by Amplify AI at amplifyais.com
