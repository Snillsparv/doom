# SYNTHESIS / JUDGE BRIEFING (read BRIEFING.md and SCHEMA.md first)

You are the JUDGE and SYNTHESIZER for one part of the series. Researchers have proposed arguments; a red
team attacked them; the researchers responded (see the "## RESPONSE TO RED TEAM" sections at the end of
each research file). Your job: decide what survives, rank it, and write the final SWEDISH data for the
browsable page, following SCHEMA.md exactly.

## Inputs (read ALL in full before writing anything)
- The research files for your part (with their red-team responses appended)
- The red-team file for your part (debate/redteam_partN.md)
- research/4_skeptic_objections.md — the relevant sections for your part
- research/6_message_effectiveness.md — the rubric, principles and the backfire list (apply them)
- research/5_swedish_context.md — use its glossary for Swedish terminology (if the file exists)

## Rules of judgment
1. Accuracy is a GATE. If the red team showed a claim is wrong and the researcher conceded, it is out or
   corrected. If they disagree, side with whoever has the primary source; if unresolved, keep the claim
   only with an explicit caveat in `caveats` ("Osäkert: …") and lower `korrekt`.
2. Prefer real, dated, sourced anchors (lab disclosures, system cards, peer-reviewed papers, verified
   incidents) over deductive chains. The 2026 incidents (OpenAI/Hugging Face July 2026; Anthropic's
   three-company breach July 2026; Coxon Sept 2026) are the freshest anchors — use them where they fit,
   with the disputes stated honestly.
3. Apply the backfire list: no Terminator/robot imagery, no "paperclips" as a headline, no certainty words
   ("kommer", "oundvikligt", "alla dör" as fact), no personal p(doom), no fixed dates as our own forecast,
   no doom without agency. Present probabilities as ranges from named sources.
4. Every answer needs a `script`: 30–60 seconds of spoken Swedish a YouTuber could actually say, with
   one concrete image. Write like a good Swedish science communicator (tänk Vetenskapens värld / Kurzgesagt
   på svenska): korta meningar, du-tilltal, inga anglicismer där svenska ord finns.
5. `pros`/`cons` must be specific to the item (not generic). `cons` = what a smart skeptic says. `rebuttal`
   = how to answer it in 1–3 sentences. `caveats` = exactly what NOT to overclaim, with the true version.
6. `debate_note`: one or two sentences summarizing the red-team attack and outcome for this item, so the
   creator sees it was stress-tested (e.g. "Rödlaget invände att … ; researchern medgav … ; behåller med
   tillägget …").
7. `explainers`: 1–4 links to people who explain THIS point well (videos with timestamps where known).
   `sources`: 2–6 primary sources with URLs. Only URLs that appear in the research files or that you verified.
8. Cross-references: if an item belongs mainly to another question, include a short `ref` entry (see SCHEMA).
9. Scores: use the rubric in SCHEMA.md honestly. The overall `score` = 0.25*konkret + 0.25*robust +
   0.15*minnesvard + 0.20*trovardig + 0.15*korrekt, one decimal. Do not inflate; a spread of roughly
   5.5–9.3 across a part is expected. Sort answers by score descending within each question.
10. Questions: 5–7 per part, phrased exactly as a curious Swedish viewer would ask them (du-form, no jargon).
    Use the red team's proposed structure as a starting point but improve it. Each question gets 4–9 answers.
11. `recommended_spine`: 6–10 steps of a recommended video dramaturgy for this part, drawing on the
    message-effectiveness file (hook → concrete example → mechanism → "men kan man inte bara…" → stakes →
    efficacy/what viewers can do).

## Output mechanics (IMPORTANT — avoid one giant write)
Write ONE JSON file per question to the folder named in your task, e.g. `final/del1/q1.json`, `q2.json`, …
each containing a single question object per SCHEMA.md ({"id","question","why","answers":[…]}).
Then write `final/del1/meta.json` with {"id","title","subtitle","intro","recommended_spine"}.
After writing, VALIDATE every file with `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <file>`
and fix any error. Use IDs: questions d1q1…; answers d1q1a1… (d2/d3 for parts 2/3).
Return to the orchestrator a ~12-line summary: the question list, the #1 answer per question with its score,
what you dropped from the research and why, and any remaining accuracy worries.
