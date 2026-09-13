---
name: launch-retro
description: Compare the results of a launch with friday/gtm-plan.md or friday/product-hunt-launch.md and turn the gap into wins, misses, lessons, unresolved questions, and one next experiment. Works from a pasted recap when neither plan file exists, compares expected with actual without inventing a metric, and writes friday/launch-retro.md. Reads friday/voice.md if present and writes in your voice.
---
<!-- Built by Friday​‌‍‌​ (https://friday.amplifyais.com). Free for personal use. Commercial use needs a paid Friday. Licence: PolyForm-Noncommercial-1.0.0. -->

# /launch-retro

A launch plan is a stack of assumptions with dates attached. This command compares what you expected with what actually happened, then turns the gap into lessons and one next experiment. It reads the plan you launched from when that file exists, works from a pasted recap when it does not, and never replaces a missing number with a plausible one.

You, Claude, run the whole flow below in order, using your own file tools. There is no module to import and nothing to install.

## Step 1: Read the founder's voice profile (if it exists)

Check whether `friday/voice.md` exists in the current directory. If it does, read it and write all output in the founder's voice.

If `friday/voice.md` does not exist, write in a direct, plain style: short sentences, active voice, no hedging.

## Step 2: Find the launch plan

Look for the plan this launch ran from, in this order:

1. `friday/gtm-plan.md`, written by `/go-to-market`.
2. `friday/product-hunt-launch.md`, written by `/product-hunt-launch`.

Read whichever you find and lift out the launch's expectations: the targets, the launch date or window, the channels, the budget, and what the plan said success would look like. Keep each expectation attached to the file it came from, so the retro can say where a promise was written down.

Three cases, all workable:

- **One plan file exists.** Use it. Do not ask for the same information again.
- **Both exist.** Use both. Name the file each expectation came from when the two disagree, because a plan that contradicted itself is itself a lesson.
- **Neither plan file exists.** Do not stop and do not stall. Ask:

> Paste the plan or the promise you launched with: the targets, the date or window, the channels, and what you expected to happen. A few bullets is enough. If you never wrote one down, tell me what you remember expecting and say so, and I will mark every expectation as recalled rather than documented.

If the founder never wrote a plan, run the whole retro anyway and label those expectations `recalled`. A retro against remembered expectations is still worth more than no retro, as long as the file says which is which.

## Step 3: Get the actual results

Ask in one batch, before writing anything:

> What actually happened, and where did you see it? Give me the numbers you have with the window they cover (visits, signups, replies, orders, revenue, retention, whatever this launch was supposed to move), plus anything you watched that has no number attached.

Rules for this step:

- **Partial data is fine.** A launch with three known numbers and five gaps is a normal retro.
- **A missing number is written as `not measured`.** Never estimate, never interpolate, never carry a number over from the plan and present it as a result.
- **A remembered number is labelled `recalled`,** with the source named if there is one (a screenshot, a dashboard, a Stripe email).
- **No result is inferred from a feeling.** "Traffic felt strong" is not a result. Ask what the person saw that made it feel that way, and write that instead.

Wait for the results before comparing anything. Do not work from what the plan expected.

## Step 4: Compare expected and actual

Put every expectation next to its result, in one table. One row per expectation, no row left out because the result is embarrassing or absent.

| Expectation | Where it was written | Actual | Source and window | Verdict |
|---|---|---|---|---|
| <target from the plan> | <friday/gtm-plan.md, friday/product-hunt-launch.md, or recalled> | <number, or "not measured"> | <where the number came from and the dates it covers> | hit / missed / unclear |

The verdict column is deliberately narrow:

- **hit** means the actual met or beat the expectation, measured over a window that matches it.
- **missed** means the actual fell short over a comparable window.
- **unclear** means the result cannot be compared, usually because the number is missing or the windows do not line up. Say which of the two it is. Do not force a verdict to fill the column.

If the plan contained no numeric target, compare the qualitative claim instead ("we expected Product Hunt to carry the first hundred users") and say plainly that the comparison is directional rather than measured.

## Step 5: Wins, misses, and lessons

From the table, write three short sections in the founder's voice.

**Wins.** What worked, with the evidence beside it. A win with no evidence behind it is a claim, not a win, so either attach the number or say it is a judgement call.

**Misses.** What did not land, described as an outcome rather than a personality flaw. Name the assumption that failed, not the person who wrote it. If a miss was caused by something outside the founder's control, say so separately from the misses they can act on.

**Lessons.** Each lesson must point at the row of the table that produced it. A lesson that could have been written before the launch is not a lesson, it is a platitude, and it does not belong in this section.

## Step 6: Unresolved questions and one next experiment

**Unresolved questions.** What the retro still cannot answer: the missing numbers, the channel with no attribution, the result too early to read. Each one gets the smallest concrete way to answer it next time.

**One next experiment.** Exactly one. Name the change, the number it is meant to move, the window it runs over, and what result would make the founder keep it or drop it. If two experiments look equally promising, pick the cheaper one to run and list the other under Unresolved questions, so the file stays a decision rather than a wish list.

Do not turn this section into a full growth plan. That is `/go-to-market`'s job, and a second plan started inside a retro is how the first one gets abandoned.

## Step 7: Write the retro

Write the result to `friday/launch-retro.md`. Create the `friday/` folder if it does not exist.

If the file does not exist, create it with this structure:

```markdown
# Launch Retro: <product or launch name>

**Launch window:** <YYYY-MM-DD to YYYY-MM-DD, or "not stated">
**Plan source:** <friday/gtm-plan.md, friday/product-hunt-launch.md, a paste, or "no plan written">
**Results source:** <dashboard, email, founder recall, or "partial">
**Last updated:** <YYYY-MM-DD>

## What we expected, and what happened

| Expectation | Where it was written | Actual | Source and window | Verdict |
|---|---|---|---|---|
| <target> | <plan file or recalled> | <number or "not measured"> | <source and dates> | hit / missed / unclear |

## Wins

- <What worked. Evidence: <number or observation>.>

## Misses

- <What did not land. The assumption that failed: <assumption>. Evidence: <number or observation>.>

## Lessons

- <The lesson. Table row it came from: <expectation>.>

## Unresolved questions

- <Question the retro cannot answer yet. Cheapest way to answer it: <step>.>

## The one next experiment

- **Change:** <what changes>
- **Number it should move:** <metric>
- **Runs for:** <window>
- **Keep it if:** <result that means keep>
- **Drop it if:** <result that means drop>

## Where the data is thin

<Name the windows, channels, or metrics with no reliable number, and what to instrument before the next launch.>
```

If `friday/launch-retro.md` already exists, add the new retro at the top, immediately after the `# Launch Retro: <name>` heading it starts with, so the newest launch sits first. Keep earlier retros intact. Never overwrite the file wholesale, and never delete an older retro because its assumptions now read badly.

Write the prose sections in the founder's voice. The table keeps its own plain language: numbers, sources, and windows are evidence, so leave them as they are whatever the voice profile says. If the profile lists banned words, do not use any of them in the sections you write.

After writing, print:

> Launch retro saved to `friday/launch-retro.md`. The one next experiment is the only thing to schedule. Everything else here is context for the launch after it.

## What this does not do

This command does not connect to an analytics tool, does not pull numbers from any platform, and does not send anything anywhere. It does not score the launch out of ten, does not forecast the next one, and does not rewrite the plan that failed. It reads the plan you launched with, compares it with the results you give it, holds every claim to what those two actually contain, and writes the retro to your own disk.

## What this builds toward

Run after every launch, `friday/launch-retro.md` becomes the record of what your plans promised against what they delivered. The assumptions that keep missing stop being repeated, the wins that nobody noticed get written down while they are still true, and each launch starts from the last one's evidence instead of its enthusiasm.

The full stack is Friday at friday.amplifyais.com. Nine specialists, running against your real inbox, calendar, and tasks every morning before you are up.

---

Built by Amplify AI at amplifyais.com
