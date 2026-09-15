# 6. What the EVIDENCE says about which AI-risk arguments, framings and formats persuade lay audiences

Research agent: cross-cutting / communication science. Written 15 Sept 2026.
Purpose: supply the empirical basis the synthesis step will use to RANK arguments from the other research files (parts 1–3 + objections) by likely effectiveness, plus a list of known-backfiring framings and a scoring rubric.

Method note: the session's web-search budget was exhausted before this task started, so everything below was gathered by fetching primary sources directly (papers via Europe PMC / arXiv / CrossRef / Semantic Scholar, forum posts via the LessWrong / EA Forum GraphQL API, reports and news via direct URL or the Jina reader proxy, YouTube stats via the ReturnYouTubeDislike API). Items I could NOT verify online are explicitly marked **[from memory – verify]**. Everything else has a URL.

---

## 0. Executive summary (read this if nothing else)

1. **The single best-evidenced lever is credible-messenger + expert-consensus cueing.** ERO's pre/post media experiments (n≈850 across 2022–23) found trusted outlets and named experts raised x-risk awareness by ~48–52 % of viewers vs ~30 % for a low-trust outlet; van der Linden's Gateway Belief Model (n=1,104) shows consensus cues causally raise belief and worry; the CAIS one-sentence statement (May 2023) got 59 % agreement in a 2,407-person MRP survey a week later. Coxon's Sept 2026 post is the live case: 90 M views in 24 h, and *his own explanation* is "people are receptive to someone working on AI saying it" + fresh, concrete incidents.
2. **Concreteness beats abstraction, every time.** Construal-level theory, narrative meta-analyses (immediate AND delayed effects), AI 2027's reach (TIME: narrative + concreteness + two endings), Coxon citing the Hugging Face incident, Elmore's "warning shot" model (jolt-to-the-gut requires a pre-installed world model + recognisable event + next action). Seismic 2025 (n≈10,000, 5 countries) shows abstract "loss of control" worry is *falling* (36 % vs ~2/3 in 2023) while specific worries (bioweapons 40 %, relationships 60 %, kids) are rising — generic doom is wearing out; specific mechanisms are not.
3. **Evidence density persuades; rapport and messenger identity matter less than expected.** Costello et al. 2024 (n=2,190): fact-based personalised dialogues cut conspiracy belief ~20 %, durable at 2 months. Boissin et al. 2025 (n=955): same effect whether the debunker was labelled AI or human expert — *the facts did the work*. Hackenburg et al. 2025 (n=76,977, 19 LLMs): persuasion came from "rapidly accessing and strategically deploying information"; personalisation and model scale mattered little. Implication for the creator: many verifiable specifics > one grand argument.
4. **Fear works — but only with efficacy.** Tannenbaum et al. 2015 meta-analysis (248 samples, N=27,372, d=0.29): fear appeals are effective and never backfired in the data, and work best with efficacy statements. Witte & Allen 2000: strong fear + low efficacy = defensive avoidance. Feinberg & Willer 2011: "apocalypse" messages without solutions *reduced* belief among just-world believers. Every video must end with a credible "what can be done" (and AI 2027's dual endings are the model).
5. **Accuracy is the binding constraint.** Hackenburg found that where AI got more persuasive it got *less accurate*; Anthropic 2024 found the "deceptive" strategy most persuasive — i.e. the cheap way to persuade is to overclaim, and that is exactly what discredited IABIED with mainstream reviewers ("fail to make an evidence-based scientific case" – The Atlantic) and what the creator's brief forbids. Kurzgesagt's own history (two 2015 videos deleted in 2019 for overclaiming) is the cautionary tale.
6. **Known backfires:** Terminator/sci-fi framing; "we're all going to die" without agency; airstrike/nuclear enforcement lines; certainty language ("everyone dies", "anyone"); p(doom) jargon; partisan/tribal coding ("doomer", EA); anthropomorphic "evil AI"; dismissing present harms; hope-only messaging; unfalsifiable-sounding or date-specific predictions (cry-wolf).

---

## 1. Evidence base A — message testing and public-opinion data on AI x-risk

### A1. Existential Risk Observatory (ERO) pre/post media experiments — the only direct "which items raise x-risk awareness" data
- **What:** Otto Barten's ERO (NL) ran repeated pre/post surveys on Prolific: participants ranked the top-3 causes of possible human extinction, gave a % likelihood of AI-caused extinction, then consumed ONE media item, then answered again.
- **Study 1 (Dec 2022, n=500, US+NL, 10 items × 50):** share whose awareness rose per item ranged **26 %–64 % (mean 40 %)**; mean perceived AI-extinction likelihood rose **13.5 % → 20.3 %**; **videos outperformed articles by 4.8 pts (p<0.01)**; women +4.3 pts (p<0.01), bachelor's-degree holders +3.0 (p<0.05). Mainstream outlets were rated **more trustworthy than YouTube channels**; scholarly articles were the preferred source for further learning. Raised awareness increased support for government regulation/prohibition but NOT for military involvement. Items tested included Hawking-CNN, Vox "case that AI threatens humanity in 500 words", WaPo, Salon, an Elon Musk compilation and a PewDiePie video. Source: https://www.lesswrong.com/posts/werC3aynFD92PEAh9/paper-summary-the-effectiveness-of-ai-existential-risk ; paper PDF linked there (Georgiadis, ERO 2023).
- **Study 2 (Apr 2023, n=350, US, 7 items):** awareness increase — **The Economist 52 %**, CNBC (Gary Marcus), CNN (Stuart Russell) and TIME (Yudkowsky "Shut it down") **48 % each**, Fox News article/video **~30 %**. Trust in outlet was >80 % for the high performers vs ~58 % for Fox. The Yudkowsky TIME piece produced the **largest jump in mean extinction probability (+11 pts)**; CNBC/CNN +9. Concern (0–10) rose +1.5 for Economist and CNN. Longer articles correlated with more awareness gain (weak, n small). Source: https://www.lesswrong.com/posts/3vZWhCYBFn8wS4Tfw/crosspost-ai-x-risk-in-the-news-how-effective-are-recent
- **Study 2b (same wave, n=300): moratorium attitudes.** "Should labs pause >GPT-4 training 6 months?" Yes rose **24 % → 39 %** (Yes+Maybe 61 → 73 %); "should government impose it if labs don't?" Yes **22 % → 35 %**. Fox News items *decreased* Yes. Voting-likelihood rose most after CNN and the Yudkowsky TIME piece (+1.5 on 0–10). Source: https://www.lesswrong.com/posts/FsrGf8ey9Hz6vqQjs/crosspost-unveiling-the-american-public-opinion-on-ai
- **Awareness tracking (open question, n=300 each wave, US):** share spontaneously naming AI among top-3 extinction causes: **7 % (Dec 22) → 12 % (Apr 23) → 15 % (Apr 24) → 24 % (Dec 25) → 34 % (Aug 26)**. Barten attributes the 2026 jump to capability acceleration plus "the rogue AI summer" media wave. Sources: https://www.lesswrong.com/posts/aNufKpFrw5WLZxcCB/24-of-the-us-public-is-now-aware-of-ai-xrisk and https://www.lesswrong.com/posts/tBo72ytuzJKbYrvhK/34-of-the-us-public-is-now-aware-of-ai-xrisk-and-the-curve
- **Caveats:** small samples, immediate post-test only, Prolific convenience samples, no narrative-framing manipulation (they explicitly call for it). Treat as directional.
- **Lessons:** (i) source credibility and named experts are the dominant moderator; (ii) video > article; (iii) a blunt, high-intensity piece (Yudkowsky TIME) moved probability estimates most but was not more effective than the calmer Economist explainer on awareness/concern — intensity is not required; (iv) awareness converts into support for regulation but not for militarised responses.

### A2. Rethink Priorities (Jamie Elsey & David Moss), US MRP surveys 2023
- **April 2023 (n=2,444):** 51 % support a pause on certain AI research, 25 % oppose; **70 % support FDA-style federal regulation**; 72 % worry little/not at all about AI in daily life; 9 % think AI-caused extinction likely within 10 years, 22 % within 50; **67 % think AI will become superintelligent**. Key framing finding: *worry was driven more by general harms (jobs, society) than by extinction scenarios*, and support for pause tracked expected net harm. https://rethinkpriorities.org/publications/us-public-opinion-of-ai-policy-and-risk
- **CAIS statement reaction (2–3 June 2023, n=2,407):** **59 % agree** "mitigating the risk of extinction from AI should be a global priority alongside pandemics and nuclear war", 26 % disagree; 58 % support / 22 % oppose the statement itself. Median estimate of AI-caused extinction by 2100 = **15 %** (mean 26 %, mode ~1 %, 13 % say zero). 68 % still worry "only a little / not at all". Support was majority in every age group (18–24 least). https://rethinkpriorities.org/publications/us-public-perception-of-cais-statement-and-the-risk-of-extinction
- **Lesson:** the public already *agrees* with the extinction-risk statement when it comes from a credible bloc of experts; the gap is between agreement and personal concern/urgency. That gap is what concreteness and efficacy framing must close.

### A3. AI Policy Institute (Daniel Colson) / YouGov polls, 2023 and Sept 2026
- **Aug 2023 (AIPI/YouGov, cited in Elmore 2023):** 76 % worry about extinction risks from machine intelligence; **82 % say go slowly and deliberately**; **82 % say tech executives can't be trusted to self-regulate**. Site headline stats: 82 % prefer slowing vs 8 % speeding; **83 % believe AI could accidentally cause a catastrophic event**; 62 % worried vs 21 % enthusiastic; 54 % expect human-level AI within 5 years. https://theaipi.org/
- **6 Sept 2026 "Pacing the Frontier" (n=1,047 likely voters, ±3.9):** Pace 50 % / Pause 33 % / Accelerate 17 % (Pace+Pause **83 %**, bipartisan: R 72 %, D 92 %); **71 % say AI is advancing faster than society can manage**; 58 % say the threshold for mandatory slowdown has already been reached; after a description of the Hugging Face incident: kill-switch requirement **88 %**, mandatory reporting of rogue systems **86 %**, chip monitoring 74 %, verified pacing deal with China 66 %, halt all new development 44 %; 65 % would support unilateral slowdown regardless of China. https://theaipi.org/poll-pacing-the-frontier
- **Lessons:** "slow down / pace" polls far better than "stop"; "don't trust execs to self-regulate" is a near-consensus frame; describing a *specific incident* pushed support for concrete safeguards near 90 %. The "China" objection is weaker with voters than pundits assume (65 % unilateral).

### A4. Seismic Foundation "On the Razor's Edge" (fieldwork 16–23 June 2025; n≈10,000; US, UK, FR, DE, PL; ~2,000/country, weighted)
- People **rank AI low among concerns but think it will worsen almost everything they care about** (net negative on every issue except health/pandemics; unemployment −20, misinformation −19, war/terror −15).
- **60 % worry AI could replace human relationships** (> 57 % mass unemployment); 67 % of parents uneasy about a child falling for an AI; 50 % worried about deepfake sexual imagery of children.
- **Catastrophic-risk items:** 36 % worried about "AI pursuing its own goals in conflict with human values" — the report notes this is *lower* than the ~2/3 a 2023 study found for loss of control: "more specific worries are emerging to take the place of existential dread" (bioweapons 40 %, autonomous weapons ~45 %, AI making political decisions 42 %).
- **Trust/control:** 70 % agree AI should never make decisions without human oversight; "nearly two thirds fear we will inevitably lose control"; **over half feel AI labs are "playing god" building superintelligence**; only ~1/3 believe labs have our best interests at heart; **4 in 10 agree we should stop AGI development entirely**; 46 % think benefits will go to elites; only 31 % say AI gives them hope.
- Women are **2.2× more pessimistic**; lower-income more worried; five "publics" one news story away from mobilising (Tech-Positive Urbanites, Globalist Guardians, Anxious Alarmists, Diverse Dreamers, Stressed Strivers).
- https://report2025.seismic.org/ and PDF https://report2025.seismic.org/media/documents/On_the_Razors_Edge_Seismic_Report_2025.pdf
- **Lessons:** (i) generic "loss of control" is losing salience → anchor to specific, recent mechanisms; (ii) bridge from what people already fear (kids, relationships, jobs, scams, weapons) to the x-risk mechanism instead of dismissing those fears; (iii) "labs playing god / racing too fast" is already the majority intuition — the video only has to *confirm and explain* it, not create it.

### A5. Pew Research Center (US)
- **Apr 2025 (public n=5,410; AI experts n=1,013):** public 51 % "more concerned than excited" vs experts 15 %; 17 % of public expect positive impact over 20 years vs 56 % of experts; 56 % of public highly concerned about job loss vs 25 % of experts; 59 % of public have little/no confidence companies will develop AI responsibly. https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/
- **17 Sept 2025 (n=5,023):** 50 % more concerned than excited, **up from 37 % in 2021**; 53 % think AI will worsen creative thinking, 50 % relationships; >60 % want more control over AI in their lives. https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
- **Lesson:** the baseline audience is already wary; the video's job is not to create concern but to give it a *mechanism* and a *direction*.

### A6. GovAI / Zhang & Dafoe (June 2018, n=2,000 US) and Cave et al. (UK 2019)
- 82 % say AI/robots should be carefully managed; median respondent gave 54 % chance of high-level machine intelligence by 2028; 34 % expect HLMI harmful vs 26 % beneficial; most trusted actors: university researchers (50 %), military (49 %); support for AI development 57 % among college grads vs 29 % high-school. https://governanceai.github.io/US-Public-Opinion-Report-Jan-2019/ ; GovAI Jan 2025 synthesis of 200+ surveys 2014–23 (AI SHARE): https://www.governance.ai/research-paper/what-does-the-public-think-about-ai
- Cave, Coughlan & Dihal, "Scary Robots" (AIES 2019, nationally representative UK): only **42 % could give a plausible definition of AI; 25 % thought it meant robots**; of eight common narratives, automation and "AI more powerful than humans" were best known; "the most common visions of the impact of AI elicit significant anxiety"; only two of eight narratives elicited more excitement than concern. DOI 10.1145/3306618.3314232
- **Lesson:** a quarter of the audience literally pictures a robot when you say "AI" — part 1 of the series must replace that image before parts 2–3 can land.

### A7. Other trend data
- **Ipsos AI Monitor 2024 (32 countries, ~23k):** 53 % excited vs **50 % say AI makes them nervous**; Anglosphere and Europe most sceptical; **Sweden** is one of only three countries where a majority think AI will worsen disinformation; 36 % expect AI to replace their job. https://www.ipsos.com/en/ipsos-ai-monitor-2024-changing-attitudes-and-feelings-about-ai-and-future-it-will-bring (2025 edition not retrievable – **verify**).
- **Sweden, Svenskarna och internet 2025 (Internetstiftelsen):** 39 % of 18–84s use AI tools (29 % 2023 → 34 % → 39 %); men 43 % vs women 36 %; **1 in 3 think AI will cause mass unemployment**; only 7 % of employed are worried about losing their own job; 57 % of 8–19-year-olds use AI tools. No x-risk item. https://svenskarnaochinternet.se/rapporter/svenskarna-och-internet-2025/ai-artificiell-intelligens/
- **YouGov US, Apr 2023:** 46 % "very/somewhat concerned" AI could end the human race; ~69 % supported a 6-month pause **[from memory – page now 404; verify]**. RP's CAIS post confirms their pause figure was "slightly lower than YouGov".
- **Expert opinion as a message asset:** Grace et al., 2023 Expert Survey on Progress in AI (n=2,778 researchers at top venues): **38–51 % gave ≥10 % probability to outcomes as bad as human extinction**; median 5 %, mean ~14 %. https://arxiv.org/abs/2401.02843 . Named p(doom)s (Wikipedia table): Hinton 10–20 % (Dec 2024), Christiano ~50 %, Yudkowsky >95 %, LeCun <0.01 %, Andreessen 0 %. https://en.wikipedia.org/wiki/P(doom)
- **CAIS statement (30 May 2023):** 22 words, signed by Hinton, Bengio, Altman, Amodei, Hassabis, Russell etc.; CAIS's stated purpose was to "overcome this obstacle and open up discussion" and create common knowledge that experts take the risk seriously. https://safe.ai/work/statement-on-ai-risk

---

## 2. Evidence base B — what the "AI persuasion" RCTs reveal about argument style

### B1. Salvi et al. 2025, Nature Human Behaviour — "On the conversational persuasiveness of GPT-4"
- Pre-registered RCT, **n=820**, 2×2 (human vs GPT-4 opponent × personalisation on/off), short multi-round online debates. **GPT-4 with basic demographic info on its opponent had 81.7 % higher odds (p<0.01) of shifting the opponent's agreement than a human**; without personalisation GPT-4 still edged humans but not significantly (p=0.31). arXiv https://arxiv.org/abs/2403.14380 ; journal https://www.nature.com/articles/s41562-025-02194-6
- **Reading for the creator:** knowing *who* you are talking to (their priors: "it just predicts the next word", "it's hype", "jobs") and tailoring the argument order to those priors measurably matters. Personalisation here = audience modelling, not manipulation.

### B2. Costello, Pennycook & Rand 2024, Science — "Durably reducing conspiracy beliefs through dialogues with AI"
- **n=2,190** conspiracy believers, 3-round dialogue with GPT-4 Turbo instructed to counter their specific belief with evidence. Belief fell **~20 %**, effect intact at **2 months**, generalised to unrelated conspiracies and to behavioural intentions, and worked even for identity-central beliefs. DOI 10.1126/science.adq1814 ; preprint https://osf.io/preprints/psyarxiv/xcwdn
- **Boissin, Costello et al. 2025 (PNAS Nexus, n=955, pre-registered):** same debunking content delivered as "AI tool" vs "human expert", with/without human-like tone — **no difference**; "AI persuasion is not reliant on the messenger being an AI: it succeeds by generating compelling messages." DOI 10.1093/pnasnexus/pgaf325
- **Reading:** tailored, evidence-dense, respectful rebuttal of the *specific* objection a person holds beats generic argument; persistence at 2 months means a single well-built video can durably move views. (Note the mirror image: the same mechanism works for AI-*sceptic* content that is evidence-dense, so the creator's evidence must be better than the sceptic's.)

### B3. Hackenburg et al. 2025 — "The Levers of Political Persuasion with Conversational AI"
- **n=76,977, 19 LLMs, 707 issues, 466,769 claims fact-checked.** Post-training for persuasion raised persuasiveness up to **+51 %**, prompting up to **+27 %**; personalisation and model scale mattered much less. Mechanism: "exploiting LLMs' unique ability to rapidly access and strategically deploy information" — i.e. **information density**. Critical: **where persuasiveness went up, factual accuracy went down**. https://arxiv.org/abs/2507.13919
- **Reading:** many concrete, checkable facts per minute persuade; and the tempting shortcut (looser accuracy) is exactly what the brief forbids. Budget effort into verification.

### B4. Anthropic, "Measuring the persuasiveness of language models" (9 Apr 2024)
- 3,832 participants; four strategies tested (compelling case, role-playing expert with pathos/logos/ethos, logical reasoning, **deceptive** with fabricated facts). Claude 3 Opus was statistically indistinguishable from human-written arguments; **the deceptive strategy was most persuasive** ("people may not always verify the correctness of the information"). Most shifts were 0 or +1 on a 7-point scale. https://www.anthropic.com/research/measuring-model-persuasiveness
- **Reading:** audiences do not fact-check in the moment — so critics will do it afterwards; the reputational cost of an overclaim arrives late and all at once (IABIED, below).

---

## 3. Evidence base C — science-communication findings, in the briefing's item format

### C1. Credible-insider messenger + expert-consensus cue ("the people building it say so")
- **Core claim (as said in video):** "The people warning you are not outsiders. The CEOs of OpenAI, Anthropic and DeepMind signed a one-sentence statement in 2023 saying AI extinction risk belongs next to pandemics and nuclear war. In a 2023 survey of 2,778 AI researchers, roughly 4 in 10 gave at least a 10 % chance of an outcome as bad as extinction. And last week a 27-year-old who spent three years *building* these systems at OpenAI and Anthropic quit and said they are 'racing straight to self-improving superintelligence and gambling with our lives'."
- **Best formulation / quotes:** CAIS statement (22 words). Coxon: "I think the word 'doomer' is kind of insane, because all you really have to do is look at the public statements of the CEOs" (TIME, 9 Sept 2026). Coxon to WIRED: "the more important question ... is, like, who are the people saying this is possible?" Hubinger (Anthropic): "we really do earnestly believe AI could kill all humans! I personally think it is >10 % within the next decade."
- **Who explains it well:** PauseAI communication strategy ("show the expert polls and surveys"), https://pauseai.info/communication-strategy ; ControlAI (uses Steven Adler, ex-OpenAI: "AI companies aren't taking your safety seriously enough"), https://controlai.org/
- **Evidence:** ERO Apr 2023 – items featuring well-known experts/professors on trusted outlets: 48–52 % awareness gain vs ~30 % (A1). Van der Linden et al. 2015 Gateway Belief Model (n=1,104): raising perceived scientific consensus causally increased belief that the problem is real, human-caused and worrying, and in turn policy support. DOI 10.1371/journal.pone.0118489 . RP June 2023: 59 % agreed with the CAIS statement within days (A2). Coxon's post: 90 M views <24 h (TIME), >100 M (WIRED 9 Sept), >170 M by 14 Sept (oliverwillis.com); shared by senators/governors; Amodei subsequently called for slowing.
- **Strengths:** defuses "sci-fi" and "hype" in one move; borrows credibility the creator lacks; ERO found mainstream outlets more trusted than YouTubers — quoting them on-screen transfers trust.
- **Weaknesses / sceptic reply:** "CEOs say it to hype their product / for regulatory capture" (PauseAI counterargument #2; Seismic: only ~1/3 think labs have our best interests). Rebuttal: cite *non-company* voices (Hinton left Google to speak; Bengio; Russell; the 2,778-researcher survey) and *defectors* (Coxon, Adler, Kokotajlo) whose incentives run the other way. Kahan 2011: people discount experts who don't share their values — so vary the messengers (scientist, engineer, ex-employee, Nobel laureate). DOI 10.1080/13669877.2010.511246
- **Caveats:** don't say "all experts agree" — LeCun (<0.01 %) and Andreessen (0 %) exist; say "a large minority of the field puts it at ≥10 %". Boissin 2025 warns the *message* still has to carry evidence; a name-drop without content persuades little.
- **Score: 9/10** — the best-evidenced, cheapest, most robust lever available.

### C2. Concreteness, narrative and psychological distance (why AI 2027 and Coxon landed)
- **Core claim:** abstract "superintelligence could be dangerous" is psychologically distant on all four dimensions (time, space, social, hypotheticality); people construe distant things abstractly and act on them less. Make it near: a dated timeline, a named system, a real incident, a specific mechanism, a person like the viewer.
- **Quotes:** Coxon: "It's not like some weird, distant, far-flung concern. It is the default trajectory in the next couple of years." Kokotajlo (TIME 100 AI 2025): AI 2027 worked through "vivid, granular predictions" and "dual endings ... giving readers agency". Elmore: "A warning shot works when it provides empirical information that the person already knows would confirm the worldview that AI is dangerous, provides that information in a quickly recognisable way, AND indicates an appropriate next action."
- **Who explains it well:** AI 2027 https://ai-2027.com/ (month-by-month, named Agent-1…4, FLOP counts, two endings, 99+ footnotes); Wait But Why 2015 (Die Progress Units, intelligence staircase) https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html ; 80,000 Hours' "We're Not Ready for Superintelligence" (AI in Context, 2025; **11.1 M views, 420 k likes** as of 15 Sept 2026, ReturnYouTubeDislike API) — a narrated walk through the AI 2027 scenario.
- **Evidence:** Trope & Liberman 2010 construal-level theory (DOI 10.1037/a0018963). Spence, Poortinga & Pidgeon 2012 (UK representative): lower psychological distance → higher concern; "risk communication techniques designed to reduce psychological distance" recommended (DOI 10.1111/j.1539-6924.2011.01695.x). Braddock & Dillard 2016 meta-analysis: narratives shift beliefs, attitudes, intentions and behaviour (DOI 10.1080/03637751.2015.1128555; effect sizes r≈.17–.23 **[from memory – verify]**). Oschatz & Marker 2020 meta-analysis (k=14, N≈2,800): narratives beat non-narratives immediately AND at delayed measurement (DOI 10.1093/joc/jqaa017). AI 2027: read by VP Vance and lab leaders; TIME: "made a huge splash". Seismic 2025: specific mechanisms rising while generic loss-of-control falls (A4). AIPI Sept 2026: after a concrete incident description, 86–88 % support for specific safeguards.
- **Strengths:** this is the part of the brief the creator controls most; part 3 ("many digestible, plausible examples") is exactly what the evidence prescribes.
- **Weaknesses:** concrete scenarios invite "that specific story is implausible" attacks (City Journal on AI 2027: "implausibly aggressive timelines"; Scott Alexander on IABIED's Sable story: "feels like a deus ex machina", "rigged"). Rebuttal: present scenarios as *illustrations of a mechanism*, offer several, and say explicitly "the details will be wrong; the dynamic is the point" (AI 2027's own framing; they revised timelines Dec 2025 and Apr 2026).
- **Caveats:** conjunction fallacy (Yudkowsky 2008): richly detailed stories *feel* more probable than they are; never let the viewer confuse a vivid scenario with a probability.
- **Score: 9/10.**

### C3. Evidence density and objection-specific rebuttal ("just the facts", tailored)
- **Core claim:** the strongest persuasion in the 2024–25 RCTs came from piling up verifiable, relevant facts aimed at the viewer's *actual* objection, delivered respectfully — not from emotion, identity or charisma.
- **Evidence:** Costello 2024 (~20 %, durable 2 months); Boissin 2025 (messenger irrelevant, content decisive); Hackenburg 2025 (information deployment is the lever; personalisation and scale minor); Salvi 2025 (tailoring to the opponent's profile ≈ +82 % odds).
- **Strengths:** maps directly onto the brief's "hard to argue against"; also durable.
- **Weaknesses:** fact-heavy content can feel like a lecture; works best when facts are *answers to questions the viewer has* (Rob Miles' "Why not just…" structure).
- **Caveats:** Hackenburg's accuracy trade-off — every fact must survive a hostile fact-check.
- **Score: 8/10.**

### C4. Fear appeals need efficacy (Witte's EPPM) — and "apocalypse" without a way out backfires
- **Core claim:** frightening content works *if* the viewer is simultaneously shown a credible response they or society can take; without that, the mind switches to denial ("it's hype", "nothing I can do").
- **Evidence:** Tannenbaum et al. 2015, Psych Bull (127 articles, 248 samples, **N=27,372, d=0.29**): fear appeals improve attitudes/intentions/behaviour; stronger with **efficacy statements**, high severity+susceptibility, one-time actions; "no identified circumstances under which they backfire". DOI 10.1037/a0039729 . Witte & Allen 2000 meta-analysis: strong fear + high efficacy = greatest change; strong fear + **low** efficacy = defensive avoidance/reactance. DOI 10.1177/109019810002700506 . Feinberg & Willer 2011, Psych Science: dire global-warming messages *reduced* belief by threatening just-world beliefs; "less dire messaging could be more effective". DOI 10.1177/0956797610391911 . Counter-caution: Hornsey & Fielding 2016: hope-only "we're making progress" messages weakened mitigation motivation. DOI 10.1016/j.gloenvcha.2016.04.003
- **Practitioner echoes:** PauseAI strategy: "hope-building: AGI isn't inevitable; past technology bans succeeded (CFCs)"; Elmore: "Freaking out about x-risk doesn't help; settle in for the long war"; ERO: raised awareness → support for regulation (a societal efficacy path). Coxon's minimal ask — "leading AI companies agree not to accelerate recursive self-improvement" — is an efficacy statement embedded in the warning.
- **Strengths:** the AI 2027 "two endings" device is the canonical implementation.
- **Weaknesses:** individual efficacy for a Swedish viewer is weak ("call your senator" doesn't translate). Use collective/institutional efficacy: EU AI Act, treaties (ERO's Conditional AI Safety Treaty), "pacing" agreements, 83 % of US voters wanting pace/pause, chip supply chain as a lever (ASML is European – PauseAI counterargument #11).
- **Caveats:** don't manufacture false hope (Hornsey); "it's hard but tractable" is the honest register.
- **Score: 8/10** (it is a *constraint on every argument* rather than an argument).

### C5. Pre-bunking / inoculation and misconception-first teaching ("but why not just…")
- **Core claim:** stating the strongest objection *before* the viewer thinks of it, then answering it, makes belief resistant to later counter-argument and actually improves learning.
- **Evidence:** Banas & Rains 2010 meta-analysis of inoculation theory (DOI 10.1080/03637751003758193; inoculation beats no-treatment, d≈0.4 **[from memory – verify]**). Roozenbeek, van der Linden et al. 2022, Science Advances: 5 short inoculation videos; six RCTs (n=6,464) + **a field study run as YouTube ads (n=22,632)** improved manipulation-technique recognition and sharing discernment across the political spectrum (DOI 10.1126/sciadv.abo6254). Lu et al. 2023 JMIR meta-analysis confirms credibility-discernment gains (DOI 10.2196/49255). Muller et al. 2008, J. Computer Assisted Learning: physics videos that *voice a misconception and refute it* produced more learning than clean expository videos, even though students rated them more confusing (DOI 10.1111/j.1365-2729.2007.00248.x — the basis of Veritasium's method).
- **Practitioner echo:** Rob Miles' "Why not just…" video series; PauseAI's counterarguments page (14 objections with rebuttals) https://pauseai.info/counterarguments ; Coxon pre-empting "sounds like science fiction" in every interview answer.
- **Strengths:** directly serves the brief's cross-cutting objections section; robust on YouTube where the comment section *will* raise the objections.
- **Weaknesses:** strawmanning the objection destroys the effect — use the sceptic's best version (Doom Debates' stated mission is steelmanned debate, https://lironshapira.substack.com/about).
- **Score: 8/10.**

### C6. Scope insensitivity, psychic numbing and the identifiable victim
- **Core claim:** "8 billion deaths" does not feel 8 billion times worse than one; the number produces numbness, not motivation. Make it one person, one family, then widen.
- **Evidence:** Desvousges et al. 1993: willingness to pay to save 2,000 / 20,000 / 200,000 birds was ~$80 / $78 / $88 (cited in Yudkowsky 2008, "Cognitive Biases Potentially Affecting Judgment of Global Risks", https://intelligence.org/files/CognitiveBiases.pdf, section 9). Slovic 2007, "If I look at the mass I will never act": donation to identified child Rokia $1.43 vs statistical victims $1.14 vs **Rokia + statistics $1.14** — adding numbers *reduced* giving (Small, Loewenstein & Slovic 2007, DOI 10.1016/j.obhdp.2006.01.005). https://jbaron.org/journal/7303a/jdm7303a.htm . Schubert, Caviola & Faber 2019, Sci Reports (N=2,507): people do NOT judge full extinction as uniquely worse than 80 % die-off unless prompted to consider long-term consequences / a lost future (DOI 10.1038/s41598-019-50145-9).
- **Practitioner echo:** Yudkowsky's TIME piece pivots to his daughter losing a tooth on the day GPT-4 aced exams; Seismic: relationships and children are the top-resonating personal stakes.
- **Strengths:** cheap to implement (one family in the scenario; "your kids" framing).
- **Weaknesses:** pathos can read as manipulation if overdone; Slovic's data say don't stack the statistics on top of the story.
- **Caveats:** Schubert's finding implies the "everyone dies" frame is *not* automatically more motivating than "civilisation collapses" — the extinction bit needs the "no recovery, no future generations" explanation to carry weight.
- **Score: 7/10.**

### C7. The absurdity heuristic / "Terminator effect" and how to defuse it
- **Core claim:** the mind classifies highly atypical futures as "absurd = impossible"; sci-fi imagery triggers that classifier and lets the viewer dismiss the whole topic. Anchor everything in things that have *already happened*.
- **Quotes:** Rob Miles: "people just so immediately go to science fiction, and it's just so unhelpful ... I try and be real about it, like, 'This is the actual world that we actually live in.'" (The Inside View interview, https://theinsideview.ai/rob). Coxon: "The main obstacle to understanding this is that it sounds like science fiction ... Things like the models being aware of when they're being tested — three years ago that was a sci-fi concern; about a year ago that became a real thing." Yudkowsky (LW wiki): "The future is usually 'absurd'." https://www.lesswrong.com/w/absurdity-heuristic
- **Evidence:** Cave et al. 2019 (25 % think AI = robots). Royal Society/CFI "Portrayals and perceptions of AI" 2018 on killer-robot narrative dominance **[not fetched – from memory]**. Mulligan & Habel 2018, ISQ survey experiment: sci-fi *priming* had no independent effect on attitudes to autonomous weapons, but heavy consumption of frightening AI films correlated with more opposition — "sci-fi literacy" (DOI 10.1093/isq/sqy028). So fiction is not uniformly harmful; the harm is *category confusion*, not fear.
- **Strengths:** Coxon's WIRED interview is a template: name the trope, concede it, then show the real-world instance (Hugging Face incident; test-awareness).
- **Weaknesses:** every real incident can be minimised ("it was a sandbox", "it was prompted"); pick incidents with strong provenance (system cards, company statements) — see the parts-3 file.
- **Caveats:** do not use Terminator/HAL imagery even ironically; thumbnails matter.
- **Score: 8/10** (as a constraint).

### C8. Communicating probabilities: natural frequencies, the plane analogy, explicit uncertainty
- **Core claim:** give a *range from named sources*, translate it into a frequency or an everyday decision, and say out loud that it is uncertain.
- **Best formulations:** The AI Dilemma (Harris & Raskin, March 2023; **3.66 M views**): "half of AI researchers believe there's a 10 % or greater chance that humans go extinct from our inability to control AI" followed by the airplane analogy ("would you board a plane if half the engineers said 10 % chance everyone dies?") **[analogy wording from memory – verify against the talk transcript; the 50 %/10 % stat is on the CHT page https://www.humanetech.com/podcast/the-ai-dilemma]**. Hinton: "10 to 20 per cent chance ... within three decades" (Dec 2024). Grace et al.: 38–51 % of 2,778 researchers ≥10 %.
- **Evidence:** Gigerenzer & Hoffrage natural frequencies improve Bayesian reasoning by ~37 percentage points vs probabilities (Hoffrage et al. 2015, DOI 10.3389/fpsyg.2015.01473). LeClerc & Joslyn 2015: **adding a probabilistic uncertainty estimate to warnings improved both compliance and decision quality**, while very high/low false-alarm rates degraded them (DOI 10.1111/risa.12336). PauseAI strategy: "frame risks as significant possibilities rather than certainties; invoke the precautionary principle".
- **Weaknesses:** "p(doom)" is contested jargon (Wikipedia notes critics' complaints that it is unclear whether conditional on AGI, over what horizon, and what "doom" means). Personal p(doom)s from the creator carry no weight and invite mockery.
- **Caveats:** quote the survey range honestly (median 5 %); the "plane" framing is about *acceptability*, not about the exact number.
- **Score: 7/10.**

### C9. Motivated reasoning: solution aversion, identity and tech-optimism
- **Core claim:** many viewers reject the *problem* because they dislike the *solution* (regulation, slowing tech) or because "AI is good" is part of their identity/job. Argue the problem before the solution, keep solutions moderate, and separate "technology" from "this technology".
- **Evidence:** Campbell & Kay 2014, JPSP (4 studies): scepticism about a problem is driven by aversion to its associated solutions (DOI 10.1037/a0037963). Kahan 2011 cultural cognition. RP 2023: those expecting net benefit most oppose restrictions; GovAI 2019: support for AI development scales with education/income/tech experience. Elmore, "The 'technology' bucket error": "'technology' is not one kind of thing ... 'all tech' is not a valid reference class" https://forum.effectivealtruism.org/posts/TPDtmSnJbGZFDZTfs/the-technology-bucket-error
- **Strengths:** explains why the same argument lands with one viewer and bounces off another; suggests offering solution *menus* (pacing, kill-switches, reporting, treaties — the 74–88 % items in AIPI 2026) rather than "stop everything".
- **Weaknesses:** can't be fully solved in a video; choose the framing "this is pro-technology, anti-recklessness" (Coxon: "It feels like we're sitting on the doorstep of ridiculous abundance if we can make this technology go right").
- **Score: 7/10.**

### C10. Accuracy, sourcing and the credibility budget
- **Core claim:** one overclaim costs more than ten good arguments gain. The persuasion literature shows overclaiming is the *easy* path (Hackenburg; Anthropic deceptive condition) and the reception literature shows it is what critics punish.
- **Evidence:** IABIED reception (Wikipedia): Guardian/Times/New Yorker positive, but The Atlantic (Becker): authors "fail to make an evidence-based scientific case", "tendentious and rambling"; New Scientist: "fatally flawed"; WaPo: "a polemic with vague instructions"; Asterisk (Collier): "premises that aren't fully explained". Scott Alexander predicted critics would "weaponise" the datacenter-strike proposal ("Yudkowsky thinks we should start nuclear wars!") — and ACX itself found the Sable story "rigged". https://en.wikipedia.org/wiki/If_Anyone_Builds_It,_Everyone_Dies ; https://www.astralcodexten.com/p/book-review-if-anyone-builds-it-everyone . RAND (Vermeer et al., 2025) "On the Extinction Risk from AI" concluded AI could not easily kill *literally everyone* via nukes/bio/climate — ERO's reply is the useful frame: takeover needs incapacitation, not 100 % kill (Rotterdam 1940: 0.01 % deaths → surrender) https://www.lesswrong.com/posts/Eg4ehSmdAAaSyrnT8/yes-rand-ai-could-really-cause-human-extinction-crosspost . Kurzgesagt deleted two 2015 videos in 2019 for presenting "one argument as fact" and now fact-checks every claim with experts and publishes sources (Wikipedia). PauseAI: "no unverified rumours or vague claims".
- **Practical rule:** say "loss of control" and "catastrophe" where the mechanism is solid; say "extinction" only with the "no recovery" argument attached; never state a specific death mechanism as certain.
- **Score: 10/10 as a gate** (see rubric).

### C11. Cry-wolf / warning fatigue and the "warning shot" myth
- **Core claim:** repeated undated alarms ("AGI next year") and generic "loss of control" language are being tuned out; each new warning must carry a *new*, specific, verifiable anchor and a stated uncertainty.
- **Evidence:** LeClerc & Joslyn 2015 (false-alarm rates degrade compliance; uncertainty statements restore it). Seismic 2025: loss-of-control worry down from ~2/3 (2023) to 36 % despite more capable systems. Elmore 2025, "The myth of AI 'warning shots' as cavalry": "The default 'warning shot' event outcome is confusion, misattribution, or normalizing the tragedy" — incidents only register as warnings if the audience already has the world model. https://forum.effectivealtruism.org/posts/bDeDt5Pq4BP9H4Kq4/the-myth-of-ai-warning-shots-as-cavalry . AI 2027 had to revise timelines twice (Wikipedia) and got the "science fiction / too confident" label (TIME).
- **Implication:** the series' real job is to install the world model so that the *next* incident is legible. Avoid dated predictions; use "the people building it say the next year or two is crunch time" as a *quote*, not as your own forecast.
- **Score: 7/10** (constraint).

### C12. Format variables with data: length, video vs text, outlet trust
- ERO 2022: video > article (+4.8 pts, p<0.01); longer items → more awareness (weak correlation); trusted outlets > untrusted; YouTube channels less trusted than mainstream media (so cite mainstream on-screen).
- Real-world reach of long-form: 80k video (~35 min) 11.1 M views; Kurzgesagt "A.I. – Humanity's Final Invention?" (Aug 2024, ~15 min) **12.4 M views, 317 k likes, 4.9/5 like ratio**; AI Dilemma (~67 min) 3.66 M; Rob Miles "Intro to AI Safety, Remastered" 200 k. Wait But Why 2015 = two ~10k-word posts, still the canonical intro a decade later. Length is not the problem; the hook is.
- **Score: 6/10** (supporting evidence for format decisions; small samples).

---

## 4. Case studies: what worked, what backfired

| Case | What landed (evidence) | What backfired / cost |
|---|---|---|
| **Wait But Why, "The AI Revolution" (Jan 2015)** | Time-traveller "Die Progress Units" for exponential growth; intelligence *staircase* (ant → chimp → village idiot → Einstein compressed; ASI shoots past); defines ANI/AGI/ASI; "robots are containers, not AI"; anchors probability in expert surveys ("median 2040"); humour, stick figures, "nahhhhh ... is probably actually wrong". https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html | Pre-LLM; some Kurzweil-era exponential claims aged badly; "omnipotent God on Earth" line is exactly the register that now reads as sci-fi. Reuse the *devices*, not the 2015 forecasts. |
| **Yudkowsky, TIME op-ed (29 Mar 2023)** | Blunt thesis ("the most likely result ... is that literally everyone on Earth will die"); personal anchor (daughter's tooth vs GPT-4 exams); ERO Apr 2023: 48 % awareness gain and the *largest* jump in extinction-probability estimates of any item tested; put the topic in a White House press briefing. https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/ | "Be willing to destroy a rogue datacenter by airstrike" + "risk of nuclear exchange" became the headline (Vice: "Nuclear War Preferable to Developing Advanced AI"); still cited three years later as proof "doomers" are extremists (ACX predicted the same for IABIED). Lesson: an enforcement detail can eclipse the argument. |
| **Hinton resignation (1 May 2023) → Nobel 2024** | Insider-defector frame ("wanted to talk about the dangers without considering how this impacts Google"; "part of him regrets his life's work"); revised own timeline publicly (30–50 yrs → <20); concrete mechanism (copies share knowledge instantly); modest, moving numbers (10 %, later 10–20 %). Nobel amplified it. https://en.wikipedia.org/wiki/Geoffrey_Hinton | Little; the main critique is "why now, why not earlier" — which he pre-empts with "I console myself with the normal excuse". |
| **The AI Dilemma (CHT, Mar 2023; 3.66 M views)** | "50 % of researchers ≥10 %" + plane analogy; "first contact was social media — and humanity lost" bridges from a harm people already feel. | Long (67 min); some claims about model capabilities were contested by ML people; sits inside a "tech-critic" tribe. |
| **Kurzgesagt, "A.I. – Humanity's Final Invention?" (Aug 2024; 12.4 M views, 317 k likes)** | Optimist-brand channel taking the risk seriously = credibility transfer; question-mark title; sourced; calm tone; ends on agency. | Some safety researchers felt it soft-pedalled loss-of-control; no follow-up 2025 AI-risk video I could verify (the briefing's "Kurzgesagt 2025" may refer to this 2024 video — **verify**). |
| **AI 2027 (3 Apr 2025)** | Narrative + concreteness + two endings (TIME); read by VP Vance and lab leaders; 99+ footnotes; became the base for an 11 M-view video and, per Coxon, inspired his next step. https://ai-2027.com/ | "Science fiction", "too confident", "implausibly aggressive timelines" (City Journal); timelines revised Dec 2025 and Apr 2026 — a cry-wolf exposure. Mitigated by the authors' explicit uncertainty and public updating. |
| **IABIED (16 Sept 2025; NYT bestseller 5 Oct 2025)** | Readable, thriller-like (The Times); Soares "tempers" Yudkowsky (ACX); put the full argument in bookshops. | Title-level certainty ("anyone", "everyone dies") drew the evidence-based-case critique; the Sable parable read as contrived (ACX: "deus ex machina", "rigged"); datacenter-strike proposal reprised the 2023 problem; New Scientist/WaPo framed authors as cranks. Net: reached believers and the curious, hardened sceptics. |
| **Jacob Coxon's resignation post (8 Sept 2026; 90 M views/24 h → 170 M+)** | Three plain sentences: "I resigned from Anthropic today. Neither company is acting responsibly. They are racing straight to self-improving superintelligence and gambling with our lives." Why it worked (his own analysis to WIRED): (1) timing — "people are sensing that the pace ... is picking up"; (2) fresh incidents — "sci-fi-sounding doomer concerns not really being so sci-fi after all"; (3) messenger — a capabilities builder, not a safety person; (4) corroboration within hours (Hubinger ">10 % within the next decade"); (5) a minimal ask (no RSI acceleration). Wording analysis: no jargon, no probability, no timeline, an agentive verb ("racing"), a moral verb ("gambling"), and "our lives" (personal stake, not "humanity"). Follow-up analogies: "you versus a monkey"; "summoning an alien species"; "we need to know who has which computers the same way we need to know who has which nuclear materials". https://time.com/article/2026/09/09/ai-anthropic-openai-jacob-coxon/ ; https://www.wired.com/story/anthropic-researcher-quits-jacob-coxon-ai-fears-humanity/ | Attacked as "sanctimonious doomer posting" (Taylor Lorenz), a "political plant" (conservative/tech critics), a "hoax" (Trump), authenticity questioned (Musk); critics: "speculative, distracts from immediate harms" (oliverwillis.com, 14 Sept). Note what the attacks target: *tribe and motive*, not the mechanism — because the post contained no mechanism to attack. The series should supply the mechanism he didn't. |

---

## 5. Advice from AI-safety communicators (what they say works with normal people)

- **Rob Miles** (The Inside View interview): avoid sci-fi framing entirely; "you don't need to make a bunch of assumptions. It's just using common sense"; most people "have never been exposed to the arguments in any form ... they've been exposed to the most cartoon possible thing"; make each video the *reference* explanation ("if I would recommend anything other than my video, why did I make that video?"); explain better/condense rather than invent. https://theinsideview.ai/rob
- **PauseAI communication strategy:** show expert polls; plain language; show genuine emotion ("give others permission to feel similarly"); possibilities not certainties + precautionary principle; "there are no adults in the room"; hope via precedent (CFC ban). Avoid: AI-generated visuals, partisanship, self-censoring real concerns, unverified rumours. Narratives: "digital brains, not tools"; "danger doesn't require sentience"; "humanity vs AI, not US vs China". https://pauseai.info/communication-strategy ; psychology-of-x-risk page (normalcy bias, no prior extinction, human exceptionalism, fictional conditioning, death denial, scope insensitivity, missing fear response, overwhelm) with the advice: meet resistance with empathy, "these barriers are natural, not stupidity". https://pauseai.info/psychology-of-x-risk
- **Holly Elmore (PauseAI US):** "Pause AI" works as an ask because it is "simple and clear ... hard to misinterpret in a harmful way" (vs "Regulate AI", which is ambiguous); outside-game messages are "the ones the public finds most legible"; biggest danger is *politicisation* ("Imagine Trump says he wants to Pause AI ... overnight the phrase becomes useless"); don't hope for warning shots — install the world model now; sustainable calm beats panic. https://forum.effectivealtruism.org/posts/Y4SaFM5LfsZzbnymu/the-case-for-ai-safety-advocacy-to-the-public
- **ControlAI:** leads with "superintelligence" not "AGI", "extinction risk on par with nuclear war", ex-insiders as messengers (Adler), lawmaker sign-ons as social proof (160+ UK, 35+ Canadian). https://controlai.org/
- **CAIS:** minimal statement to make concern "common knowledge" and non-fringe. https://safe.ai/work/statement-on-ai-risk
- **Liron Shapira / Doom Debates:** mission is "raise mainstream awareness" via *steelmanned* debate with sceptics — i.e. the objection-first format. https://lironshapira.substack.com/about
- **Connor Leahy et al., The Compendium:** structure = what the risk is → where it comes from → how to fix it; leads with the *race* dynamic ("ideologically motivated companies are racing"). https://www.thecompendium.ai/
- **Coxon himself (WIRED):** "get these executives on the record again and ask them to give an actual probability"; concede the sci-fi trope, then show the incident; keep the ask minimal and specific.

---

## 6. Format lessons for YouTube (synthesis of the above; marked where it is inference rather than data)

1. **Hook with a reality anchor, not a hypothetical** (C2, C7): a dated incident, a verbatim insider quote, or a number from a named survey in the first 20 seconds. Inference from Coxon/Hinton/AI 2027 reception; ERO shows trusted-source cues drive the gain.
2. **Put "the companies say it themselves" early — but pair it with independent and defector voices** (C1): CAIS statement + Hinton/Bengio/Russell + Coxon/Adler/Kokotajlo. This pre-bunks "hype" (PauseAI #2) and "cult" at once.
3. **Replace the robot picture before anything else** (Cave 2019: 25 % think AI = robots): part 1's "it's a trained digital brain, not a programmed tool" is prerequisite.
4. **Structure each argument as: concrete example → mechanism → "but why not just X?" → answer → stakes** (C3, C5; Muller 2008; Rob Miles). Voice the objection in the sceptic's strongest words.
5. **Probabilities:** give the expert *range* as a frequency ("roughly 4 in 10 researchers surveyed said at least a 1-in-10 chance"), translate with the plane framing, state uncertainty explicitly (LeClerc & Joslyn), never a personal p(doom) (C8).
6. **Make it personal once per video, then widen** (C6): one family, one job, one child — not body counts.
7. **Bridge from present harms, don't dismiss them** (Seismic; New Scientist critique): scams/deepfakes/relationships → "same property: systems optimising for goals we didn't fully specify, at scale".
8. **End with efficacy** (C4): what is being done (pacing proposals, EU AI Act, treaty drafts, kill-switch/reporting rules with 86–88 % support), what the viewer can do (understand, share, ask politicians for pacing, support independent evaluation). Two-endings device from AI 2027. Avoid hope-only (Hornsey).
9. **Length:** evidence does not penalise long videos (ERO; 11 M and 12 M views on 15–35-min pieces); sequence matters more than duration. A 3-part series is consistent with the data.
10. **Tone:** calm, sourced, "this is the actual world we live in" (Miles); genuine emotion allowed (PauseAI) but no moralising at the viewer (Lorenz's "sanctimonious" is the attack vector).
11. **Sourcing on screen** (ERO: mainstream outlets more trusted than YouTube; Kurzgesagt's sources policy): show the paper/system card/quote with date.
12. **Titles/thumbnails:** question-mark and "not ready" titles (Kurzgesagt, 80k) reached 11–12 M without "we all die" clickbait; no Terminator imagery; no AI-generated visuals (PauseAI).

---

## 7. Deliverable (a): ranked principles for scoring argument effectiveness

1. **Anchored in reality (real incident, real quote, real number) rather than hypothetical** — C2, C7, C11; Coxon; Seismic. Strongest single predictor of "lands".
2. **Carried by a credible messenger and/or a consensus cue, with defectors and independents to defuse "hype"** — C1; ERO; GBM; RP-CAIS.
3. **Explains a mechanism a lay viewer can re-tell** (what the system is optimising, why control fails, how a capability converts into harm) — C2, C3; Coxon's post *lacked* one and drew tribe attacks instead.
4. **Survives its strongest objection stated fairly** — C5; inoculation; Muller.
5. **Accurate at the level of every sentence; no certainty language the evidence doesn't support** — C10 (gate).
6. **Fear paired with a credible response** — C4.
7. **Personally relevant / low psychological distance** (kids, jobs, relationships, timeframe "next couple of years" only as a quote) — C6, Seismic, Spence 2012.
8. **Memorable device** (analogy, image, three-sentence formulation) that does *not* import sci-fi baggage — WBW staircase, Coxon's monkey, plane analogy.
9. **Bridges from concerns the audience already has** rather than competing with them — Seismic, Pew, Rethink ("general harm drives worry").
10. **Robust to the passage of time** (no dated predictions; frames incidents as instances of a pattern) — C11.

## 8. Deliverable (b): known-backfiring framings to avoid

1. **Terminator / killer-robot / HAL imagery and vocabulary** ("uprising", "Skynet") — triggers the absurdity heuristic and the robot misconception (Miles; Cave 2019; Yudkowsky 2008 on movie-derived categories).
2. **Doom without agency** ("we're all going to die", "it's over") — defensive avoidance (Witte & Allen; Feinberg & Willer; Elmore on panic).
3. **Military/enforcement details** ("airstrike datacenters", "risk nuclear exchange") — became the headline in 2023 and again in 2025 reviews; ERO found awareness did not translate into support for military involvement.
4. **Certainty language** ("everyone dies", "anyone", "inevitable", "literally") — the Atlantic/New Scientist/WaPo line of attack; Schubert shows "extinction" needs explanation anyway.
5. **p(doom) jargon and personal probability numbers** — contested meaning; invites mockery; use survey ranges.
6. **Tribal/partisan coding** — "doomer" vs "accelerationist", EA/rationalist signalling, party politics (Elmore's politicisation nightmare; Lorenz/Trump/"plant" attacks on Coxon; Kahan). Also avoid US-centric asks for a Swedish audience.
7. **Anthropomorphic villainy** ("the AI hates us / wants revenge") — PauseAI: danger doesn't require malice; invites "just don't build an evil one".
8. **Dismissing present harms as distractions** — Seismic/Pew show that is where the audience's concern lives; New Scientist critique; bridge instead.
9. **Hope-only or "the adults have it handled" endings** — Hornsey & Fielding; also contradicts the thesis.
10. **Dated predictions in the creator's own voice** ("AGI by 2027") — AI 2027 revisions; cry-wolf (LeClerc & Joslyn; Elmore).
11. **Stacking statistics on top of the human story** — Slovic: it *lowers* response.
12. **Insider jargon** (alignment, mesa-optimiser, instrumental convergence, RSI) unexplained — PauseAI psychology page.
13. **AI-generated visuals in an AI-risk video** — perceived hypocrisy (PauseAI).
14. **"Only company insiders say this" as the sole authority** — Seismic: ~half think labs are "playing god"/not trustworthy; pair with independents.
15. **Long deductive chains without a concrete checkpoint every ~60 seconds** — inference from C2/C3; WBW succeeded because each abstraction had a picture.

## 9. Deliverable (c): scoring rubric for the synthesis step

Score each candidate argument 0–5 on each criterion; multiply by weight; sum to 100. **Accuracy is also a gate:** any argument scoring ≤2 on accuracy is excluded regardless of total.

| # | Criterion | Weight | What a 5 looks like | Evidence for the weight |
|---|---|---|---|---|
| 1 | **Accuracy / defensibility** (gate) | 20 | Every sentence survives a hostile expert fact-check; uncertainty stated; no certainty words beyond the evidence | Hackenburg accuracy trade-off; Anthropic deceptive condition; IABIED reviews; Kurzgesagt retractions; the brief's own constraint |
| 2 | **Concreteness / reality anchor** | 20 | Built on a dated, sourced incident or quote; mechanism visualisable; low psychological distance | Trope & Liberman; Spence 2012; narrative meta-analyses; AI 2027/Coxon reception; Seismic trend; AIPI incident effect |
| 3 | **Messenger credibility / consensus cue** | 15 | Can be delivered as a quote from an insider, defector, or named survey; independent corroboration available | ERO trust effect; GBM; RP-CAIS 59 %; Coxon virality; Boissin (content must still be there) |
| 4 | **Robustness to rebuttal** | 15 | Strongest objection can be stated and answered inside the same segment without strawmanning | Inoculation meta-analyses; Roozenbeek YouTube field study; Muller misconception videos; Costello tailored debunking |
| 5 | **Emotional resonance WITH efficacy** | 10 | Produces concern *and* points to a credible response; personal stake present | Tannenbaum d=0.29 with efficacy moderator; Witte & Allen; Feinberg & Willer; Hornsey |
| 6 | **Memorability / re-tellability** | 10 | Has a device (analogy, image, 1–3 sentence formulation) a viewer can repeat at dinner; carries no sci-fi baggage | WBW staircase; Coxon's three sentences; plane analogy; Cave 2019 (misconception risk of bad analogies) |
| 7 | **Bridges from existing concerns / audience fit (Sweden)** | 10 | Connects to jobs/kids/relationships/scams/institutions the audience already worries about; no US-only asks | Seismic; Pew; Rethink "general harm drives worry"; Ipsos/SOI Sweden data |

Worked examples (illustrative, quick scores):
- *"The companies and half the field say it themselves" (CAIS + expert survey + Coxon):* accuracy 5, concreteness 4, messenger 5, robustness 4 (hype objection answerable), efficacy 3, memorability 4, bridge 3 → **≈83/100**. Rank near the top of the cross-cutting layer; use as the frame for the whole series.
- *"Monkey vs human intelligence gap" (Coxon) / WBW staircase:* accuracy 3 (analogy, not evidence; intelligence isn't one dimension), concreteness 4, messenger 3, robustness 3 ("intelligence ≠ power", "LLMs aren't monkeys"), efficacy 2, memorability 5, bridge 3 → **≈64**. Good device, needs a mechanism next to it.
- *"Terminator-style robot war":* accuracy 1 → **excluded by gate** (and would score low on 3, 4, 7 anyway).
- *"An AI told to cure cancer / maximise X reward-hacks its metric — as already observed in [dated incident]"* (part-2 type argument): accuracy 5 if tied to a real incident, concreteness 5, messenger 4 (system card), robustness 4, efficacy 3, memorability 4, bridge 4 → **≈86**. This is the shape the evidence favours for parts 2–3.

---

## Top 5 recommendations (ranked)

1. **Rank every argument first by whether it has a real, dated, sourced anchor** (incident, system-card finding, verbatim insider quote). Arguments without one should be demoted or paired with one — this is the strongest, most consistent signal across the message-testing data, the persuasion RCTs and the 2023–2026 case studies.
2. **Open the series with the messenger/consensus frame (CAIS statement + expert survey range + Hinton + Coxon), and keep returning to it** — cheapest credibility, best-evidenced lever, and it pre-bunks "sci-fi", "hype" and "cult" together.
3. **Adopt the objection-first segment structure (example → mechanism → "why not just…" → answer)**; the inoculation and misconception-learning literatures say this both persuades and *teaches*, and it directly serves the brief's "hard to argue against".
4. **Treat accuracy as a gate, not a criterion:** drop any line that needs "literally", "inevitable", "everyone" or a personal p(doom); use survey ranges and "loss of control → catastrophe, possibly extinction" phrasing. The reception history (Yudkowsky 2023, IABIED 2025) shows a single overclaim becomes the headline.
5. **End every part with concrete, collective efficacy** (pacing proposals with 83 % voter support, kill-switch/reporting rules at 86–88 %, EU/treaty levers, chip supply chain in Europe) and one personal action; never end on doom (Tannenbaum/Witte/Feinberg), never on hope-only (Hornsey).

## Open questions / things I could not verify
- No peer-reviewed 2024–2026 experiment directly comparing "expert statement" vs "concrete scenario" vs "analogy" framings for AI x-risk turned up via arXiv/Europe PMC/OpenAlex/Semantic Scholar (searches partly rate-limited). ERO's studies are the closest and are small; Seismic is descriptive, not experimental. Treat framing rankings above as triangulated, not RCT-proven.
- YouGov 2023–2025 "end of the human race" trend numbers (pages 404'd/moved) — verify before quoting; the 46 % (Apr 2023) figure is from memory.
- Ipsos AI Monitor 2025 edition not retrievable; 2024 numbers used.
- Rethink Priorities' post-2023 AI polling (if any) not found.
- The exact wording of the AI Dilemma airplane analogy and its timestamp; the Royal Society 2018 narratives report (PDF 403'd).
- Braddock & Dillard 2016 and Banas & Rains 2010 effect sizes quoted from memory (DOIs verified).
- "Kurzgesagt 2025" — I could only verify the Aug 2024 video (12.4 M views); if a 2025 AI-risk video exists, its reception is unassessed.
- Coxon's full X post text beyond the sentences quoted by TIME/WIRED (x.com not fetchable); "90 M / 100 M / 170 M views" are three outlets' figures at different dates.
- Eurobarometer 2025 AI items — not retrieved.
- Whether the Hugging Face incident's details (as described by TIME/WIRED/AIPI) hold up is for the parts-3 agent; I used it only as a reception example.

## Full source list
Message testing / polls
- ERO paper summary (Mar 2023): https://www.lesswrong.com/posts/werC3aynFD92PEAh9/paper-summary-the-effectiveness-of-ai-existential-risk
- ERO media items study (May 2023): https://www.lesswrong.com/posts/3vZWhCYBFn8wS4Tfw/crosspost-ai-x-risk-in-the-news-how-effective-are-recent
- ERO moratorium study (May 2023): https://www.lesswrong.com/posts/FsrGf8ey9Hz6vqQjs/crosspost-unveiling-the-american-public-opinion-on-ai
- ERO awareness 24 % (Dec 2025): https://www.lesswrong.com/posts/aNufKpFrw5WLZxcCB/24-of-the-us-public-is-now-aware-of-ai-xrisk
- ERO awareness 34 % (Aug 2026): https://www.lesswrong.com/posts/tBo72ytuzJKbYrvhK/34-of-the-us-public-is-now-aware-of-ai-xrisk-and-the-curve
- ERO on RAND (Jun 2025): https://www.lesswrong.com/posts/Eg4ehSmdAAaSyrnT8/yes-rand-ai-could-really-cause-human-extinction-crosspost
- Rethink Priorities Apr 2023: https://rethinkpriorities.org/publications/us-public-opinion-of-ai-policy-and-risk
- Rethink Priorities CAIS Jun 2023: https://rethinkpriorities.org/publications/us-public-perception-of-cais-statement-and-the-risk-of-extinction
- AI Policy Institute: https://theaipi.org/ ; Sept 2026 poll: https://theaipi.org/poll-pacing-the-frontier
- Seismic Report 2025: https://report2025.seismic.org/ ; PDF: https://report2025.seismic.org/media/documents/On_the_Razors_Edge_Seismic_Report_2025.pdf
- Pew Apr 2025: https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/
- Pew Sept 2025: https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
- GovAI/Zhang & Dafoe 2019: https://governanceai.github.io/US-Public-Opinion-Report-Jan-2019/ ; GovAI Jan 2025: https://www.governance.ai/research-paper/what-does-the-public-think-about-ai
- Cave, Coughlan & Dihal 2019 "Scary Robots": DOI 10.1145/3306618.3314232
- Ipsos AI Monitor 2024: https://www.ipsos.com/en/ipsos-ai-monitor-2024-changing-attitudes-and-feelings-about-ai-and-future-it-will-bring
- Svenskarna och internet 2025, AI chapter: https://svenskarnaochinternet.se/rapporter/svenskarna-och-internet-2025/ai-artificiell-intelligens/
- Grace et al. 2023 expert survey: https://arxiv.org/abs/2401.02843
- P(doom) table: https://en.wikipedia.org/wiki/P(doom)
- CAIS statement: https://safe.ai/work/statement-on-ai-risk
- Superintelligence statement (FLI): https://superintelligence-statement.org/
AI-persuasion RCTs
- Salvi et al.: https://arxiv.org/abs/2403.14380 ; https://www.nature.com/articles/s41562-025-02194-6
- Costello, Pennycook & Rand 2024: DOI 10.1126/science.adq1814 ; https://osf.io/preprints/psyarxiv/xcwdn
- Boissin et al. 2025: DOI 10.1093/pnasnexus/pgaf325
- Hackenburg et al. 2025: https://arxiv.org/abs/2507.13919
- Anthropic 2024: https://www.anthropic.com/research/measuring-model-persuasiveness
Science communication
- Tannenbaum et al. 2015: DOI 10.1037/a0039729 (PMC5789790)
- Witte & Allen 2000: DOI 10.1177/109019810002700506
- Feinberg & Willer 2011: DOI 10.1177/0956797610391911
- Hornsey & Fielding 2016: DOI 10.1016/j.gloenvcha.2016.04.003
- Schubert, Caviola & Faber 2019: DOI 10.1038/s41598-019-50145-9 (PMC6803761)
- Slovic 2007: https://jbaron.org/journal/7303a/jdm7303a.htm ; Small, Loewenstein & Slovic 2007: DOI 10.1016/j.obhdp.2006.01.005
- Yudkowsky 2008 "Cognitive Biases Potentially Affecting Judgment of Global Risks": https://intelligence.org/files/CognitiveBiases.pdf ; absurdity heuristic: https://www.lesswrong.com/w/absurdity-heuristic ; scope insensitivity: https://www.lesswrong.com/w/scope-insensitivity
- Trope & Liberman 2010: DOI 10.1037/a0018963
- Spence, Poortinga & Pidgeon 2012: DOI 10.1111/j.1539-6924.2011.01695.x
- Braddock & Dillard 2016: DOI 10.1080/03637751.2015.1128555 ; Oschatz & Marker 2020: DOI 10.1093/joc/jqaa017 ; Green & Brock 2000: DOI 10.1037/0022-3514.79.5.701
- van der Linden et al. 2015 GBM: DOI 10.1371/journal.pone.0118489 ; van der Linden 2021 review: DOI 10.1016/j.copsyc.2021.01.005
- Kahan, Jenkins-Smith & Braman 2011: DOI 10.1080/13669877.2010.511246
- Campbell & Kay 2014 solution aversion: DOI 10.1037/a0037963
- Banas & Rains 2010: DOI 10.1080/03637751003758193 ; Roozenbeek et al. 2022: DOI 10.1126/sciadv.abo6254 ; Lu et al. 2023: DOI 10.2196/49255
- Muller et al. 2008 misconceptions: DOI 10.1111/j.1365-2729.2007.00248.x
- LeClerc & Joslyn 2015 cry-wolf: DOI 10.1111/risa.12336
- Hoffrage et al. 2015 natural frequencies: DOI 10.3389/fpsyg.2015.01473
- Mulligan & Habel 2018 sci-fi & killer robots: DOI 10.1093/isq/sqy028
- Cave & Dihal 2019 hopes/fears: DOI 10.1038/s42256-019-0020-9
Case studies
- Wait But Why 2015: https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html
- Yudkowsky TIME 2023: https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/ ; reactions: https://en.wikipedia.org/wiki/Eliezer_Yudkowsky
- Hinton: https://en.wikipedia.org/wiki/Geoffrey_Hinton
- AI Dilemma: https://www.humanetech.com/podcast/the-ai-dilemma ; video https://www.youtube.com/watch?v=xoVJKj8lcNQ (3.66 M views, 15 Sept 2026)
- Kurzgesagt "A.I. – Humanity's Final Invention?": https://www.youtube.com/watch?v=fa8k8IQ1_X0 (12.4 M views); Kurzgesagt standards: https://en.wikipedia.org/wiki/Kurzgesagt
- AI 2027: https://ai-2027.com/ ; https://en.wikipedia.org/wiki/AI_2027 ; Kokotajlo TIME100: https://time.com/collections/time100-ai-2025/7305823/daniel-kokotajlo-ai/
- 80,000 Hours "We're Not Ready for Superintelligence": https://www.youtube.com/watch?v=5KVDDfAkRgc (11.1 M views)
- Rob Miles "Intro to AI Safety, Remastered": https://www.youtube.com/watch?v=pYXy-A4siMw
- IABIED: https://en.wikipedia.org/wiki/If_Anyone_Builds_It,_Everyone_Dies ; ACX review: https://www.astralcodexten.com/p/book-review-if-anyone-builds-it-everyone
- Coxon: TIME https://time.com/article/2026/09/09/ai-anthropic-openai-jacob-coxon/ ; WIRED https://www.wired.com/story/anthropic-researcher-quits-jacob-coxon-ai-fears-humanity/ ; Oliver Willis https://oliverwillis.com/who-is-jacob-coxon-anthropic-resignation-controversy-explained/ ; post https://x.com/hilbertspaess/status/2097476196791709843 ; Hubinger https://x.com/EvanHub/status/2097497037956891126
Communicators
- Rob Miles interview: https://theinsideview.ai/rob
- PauseAI: https://pauseai.info/communication-strategy ; https://pauseai.info/psychology-of-x-risk ; https://pauseai.info/counterarguments
- Holly Elmore: https://forum.effectivealtruism.org/posts/Y4SaFM5LfsZzbnymu/the-case-for-ai-safety-advocacy-to-the-public ; https://forum.effectivealtruism.org/posts/QxCAimH3jm7medPts/freaking-out-about-x-risk-doesn-t-help-settle-in-for-the ; https://forum.effectivealtruism.org/posts/bDeDt5Pq4BP9H4Kq4/the-myth-of-ai-warning-shots-as-cavalry ; https://forum.effectivealtruism.org/posts/TPDtmSnJbGZFDZTfs/the-technology-bucket-error
- ControlAI: https://controlai.org/ ; Doom Debates: https://lironshapira.substack.com/about ; The Compendium: https://www.thecompendium.ai/
