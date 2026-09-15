# OUTPUT SCHEMA FOR SYNTHESIS (final Swedish data)

Each synthesis agent writes ONE JSON file (UTF-8, valid JSON, no comments, no trailing commas).
ALL user-facing text must be in SWEDISH (natural, clear, spoken-style Swedish suitable for a YouTube creator;
keep English technical terms in parentheses the first time when useful, e.g. "belöningshackning (reward hacking)").
URLs and proper names stay as they are. Quotes from English sources: give the Swedish translation and keep the
original English in `original` where the exact wording matters.

```json
{
  "id": "del1",
  "title": "Hur AI fungerar",
  "subtitle": "…en rad…",
  "intro": "2–4 meningar om vad den här delen ska åstadkomma hos tittaren.",
  "recommended_spine": [
    "Steg 1 i en rekommenderad dramaturgi för videon (en mening)",
    "Steg 2 …"
  ],
  "questions": [
    {
      "id": "d1q1",
      "question": "Hur kan något som bara förutsäger nästa ord vara intelligent?",
      "why": "1–2 meningar: varför tittaren ställer frågan / vilken missuppfattning som ligger bakom.",
      "answers": [
        {
          "id": "d1q1a1",
          "title": "Kort minnesvärt namn (t.ex. 'Deckargåtan: för att gissa nästa ord måste du veta vem mördaren är')",
          "type": "argument | analogi | evidens | exempel | citat | scenario",
          "score": 8.7,
          "scores": {
            "konkret": 9, "robust": 8, "minnesvard": 9, "trovardig": 8, "korrekt": 9
          },
          "core": "Kärnan i 2–5 meningar, som man skulle säga det i videon.",
          "script": "Ett förslag på formulering på talad svenska, 30–60 sekunder. Gärna med en konkret bild.",
          "pros": ["Fördel 1", "Fördel 2"],
          "cons": ["Nackdel / vad en skeptiker säger 1", "…"],
          "caveats": ["Det här får du INTE överdriva: …"],
          "rebuttal": "Hur du bemöter den vanligaste invändningen mot just detta (1–3 meningar). Kan vara tom sträng.",
          "explainers": [
            {"name": "Rob Miles – Instrumental Convergence (YouTube, 2018)", "url": "https://…", "note": "Vad som är värt att låna (en mening)"}
          ],
          "sources": [
            {"title": "Titel på källa (år)", "url": "https://…", "note": "valfritt: vad källan visar"}
          ],
          "quote": {"text": "Översatt citat", "original": "Original English quote", "who": "Vem, roll, år"},
          "debate_note": "Valfritt: vad rödlaget invände och hur det landade (1–2 meningar). Visar att argumentet är stresstestat."
        }
      ]
    }
  ]
}
```

## Scoring rubric (used for `scores` and the overall `score`)
Score each 1–10, then `score` = weighted mean rounded to one decimal:
- konkret (25%): konkret och greppbart för en lekman utan förkunskaper; ger en bild i huvudet.
- robust (25%): svårt att säga emot; överlever den bästa skeptikerinvändningen.
- minnesvard (15%): fastnar; går att återberätta för en kompis.
- trovardig (20%): stöds av trovärdiga budbärare/källor (labbens egna rapporter, Nobelpristagare, primärkällor) – inte bara "doomers".
- korrekt (15%): sant och inte överdrivet; en faktakoll skulle inte hitta något.

Answers within a question MUST be sorted by `score` descending. Aim for 4–9 answers per question.
Avoid duplicates across questions: if the same argument fits two questions, put the full version under the best
question and a short cross-reference version (with `"ref": "d1q1a1"`) under the other.
