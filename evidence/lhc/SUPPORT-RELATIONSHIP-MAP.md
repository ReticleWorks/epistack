# LHC Micro-Black-Hole Safety Case — Warrant Map

**Status: corpus-grounded analytic artifact.** This document reports what six primary and peer-reviewed sources state, and what a direct reading of their bylines and acknowledgments shows about authorship. It is not a `judgment_panel` output, not a consensus score, and not a probability estimate. Every material statement below is labeled as **direct support**, **inference**, **methodological criticism**, or **not established**, with a source id and line/section reference. Author: Sonnet 5 (Claude Code), acting as an independent evidence auditor — not the corpus collector, and not the author of either FLF proposal draft.

**Research question (from `canonical-manifest.json`):** Does the CERN safety case for excluding dangerous micro-black-hole production rest on independent, jointly sufficient physical assumptions, or on a chain with a theoretically derived (not directly experimentally confirmed) weak link?

**Prior proposal framing under test** (FLF-PROPOSAL-2-warrantgraph-voicefix-2026-06-24.md, line 60): *"The likely bottleneck is Hawking radiation: theoretically derived and supported by multiple independent physical arguments, but not directly observed... It should present it as the weakest warrant in an otherwise strong chain."* This map tests, rather than assumes, that framing. Neither proposal draft is edited here.

---

## 1. Source roster

| id | Title | Authors | Year | Role in corpus |
|---|---|---|---|---|
| src-0001 | Review of the Safety of LHC Collisions | Ellis, Giudice, **Mangano**, Tkachev, Wiedemann (LSAG) | 2008 | Primary official safety case |
| src-0002 | Astrophysical implications of hypothetical stable TeV-scale black holes | Giddings, **Mangano** | 2008 | Astrophysical fallback argument |
| src-0003 | Study of Potentially Dangerous Events during Heavy-Ion Collisions at the LHC | Blaizot, Iliopoulos, Madsen, Ross, Sonderegger, Specht | 2003 | Predecessor safety report |
| src-0004 | Extra dimensions, gravitons, and tiny black holes | CERN (institutional, unsigned) | undated | Public-facing background |
| src-0005 | Probing the Improbable | Ord, Hillerbrand, Sandberg | 2010 | Methodological critique, uses LHC as worked example |
| src-0006 | A Critical Look at Risk Assessments for Global Catastrophes | Kent | 2004 | Methodological critique, RHIC strangelets (pre-LSAG) |

---

## 2. Does the safety case include a stable-black-hole fallback, or is Hawking radiation a bare single point of failure?

**Finding: direct support for a fallback existing.** The safety case is not structured as Hawking radiation alone with no backup. src-0001 states the conditional explicitly:

> "Theoretically, it is expected that microscopic black holes would indeed decay via Hawking radiation... If, nevertheless, some hypothetical microscopic black holes should be stable, we review arguments showing that they would be unable to accrete matter in a manner dangerous for the Earth [2]." (src-0001, lines 151–155)

src-0002 is written explicitly as that fallback test:

> "For that reason, this paper will test the hypothesis that the statements of this subsection are false, by investigating possible consequences of hypothetical black holes that do not undergo Hawking decay." (src-0002, line 371)

src-0005, a methodological source independent of the CERN authors, characterizes the same structure as a deliberate multi-layer argument:

> "...it uses a multiple bounds argument. It first shows that rapid black hole decay is a robust consequence of several different physical theories (A1). Second it discusses the likely incompatibility between non-evaporating black holes and mechanisms for neutralising black holes... (A2)... The third part... models how multidimensional and ordinary black holes would interact with matter [with white dwarfs/neutron stars] (A3)." (src-0005, lines 614–640)

> "While each of these arguments have weaknesses the force of the total argument (A1,A2,A3) is significantly stronger by the combination of them. Essentially the paper acts as three sequential arguments, each partly filling in the grey area... left by the previous." (src-0005, lines 642–644)

**Refinement of the prior proposal's framing (inference, corpus-supported):** The proposal's language — "a chain... Hawking radiation [as] the weakest warrant" — implies a single linear AND-chain where every link, including Hawking radiation, must hold for the safety conclusion to stand. The corpus shows a branching, conditional structure instead: if Hawking radiation holds, the case is closed; if it fails, two further independent-of-Hawking-radiation conditions (charge neutralization, then astrophysical accretion bounds) must *also* fail before danger follows. src-0001 makes the nesting explicit for the charge step:

> "The standard neutralization process due to the quantum creation of particle-antiparticle pairs near the horizon – the Schwinger mechanism – relies on principles very similar to those at the basis of Hawking radiation, and would likely not operate if the latter was suppressed. Thus, combining the hypotheses that black holes are simultaneously neutral and stable and accrete matter requires some further deviation from basic physical laws." (src-0001, lines 388–394)

src-0002 states the same point about the same dependency (line 200): "There is therefore no concrete framework where neutralization occurs without Hawking decay taking place as well." This means the fallback layer is not fully decoupled from Hawking radiation either — a black hole stable *and* neutral simultaneously requires a further, physically unmotivated departure from known quantum mechanics before the astrophysical fallback even becomes the operative argument. The "bottleneck" is better described as: Hawking radiation failing does not by itself create danger; danger requires Hawking radiation to fail *and* neutralization to fail *and* (per src-0002's own conclusion, §9) the compactification scale to sit in a narrow, fine-tuned range. **What the corpus does not establish:** any quantitative probability for this compound failure, from any source. src-0001, src-0002, and src-0004 all state qualitative or order-of-magnitude conclusions ("no basis," "no risk of any significance") without an explicit joint probability figure for the full conditional chain.

**Not established / silence:** The 2003 predecessor report (src-0003) does not contain this fallback for black holes. Its black-hole section (§3, lines 555–786) argues safety purely from Hawking-type thermal decay-rate formulas (ΓD vs. ΓA) and a brief note that only "extremal" charged-quantum-number-carrying black holes are stable, with "no source of matter capable of causing the extremal black hole to grow" (src-0003, lines 764–766). It does not discuss cosmic-ray production of black holes on white dwarfs or neutron stars anywhere in its gravitational-effects section; that astrophysical-constraint method appears in the 2003 report only for strangelets (§2.2.2, lines 342–397). The supplied materials do not establish why the astrophysical black-hole fallback is absent from the 2003 report — whether because the concern (a stable-black-hole loophole distinct from Hawking failure) had not yet been raised in the literature, or for some other reason. What is established is that the fallback is a 2008 addition, prompted (per src-0002, line 371 and its introduction, lines 176–187) by Dimopoulos & Landsberg's 2001 suggestion that colliders could test Hawking radiation, which "raise[d] a possible question about stability."

---

## 3. Is the fallback genuinely independent of the LSAG report, or does it share authors/sources?

**This was tested, not assumed. Finding: the fallback is not independent by ordinary standards of scientific independence (separate research group, no shared authorship, no acknowledged advisory relationship).**

**Direct support — shared authorship.** src-0001's byline (line 27): "John Ellis, Gian Giudice, Michelangelo Mangano, Igor Tkachev and Urs Wiedemann." src-0002's byline (line 34, e-mail lines 67–69): "Steven B. Giddings... and Michelangelo L. Mangano." Michelangelo Mangano is a co-author of both the primary safety report and the fallback paper it relies on.

**Direct support — the fallback paper's own acknowledgments name the other four LSAG authors.** src-0002's acknowledgments (lines 2538–2544): "We are grateful to many colleagues who helped us in the course of the nine months of this project, providing valuable guidance and advice... Among these: J. Arons, **J. Ellis**, M. Fairbairn, **G. Giudice**, G. Horowitz, D. Ida, Y. Kanti, G. Landsberg, D. Marolf, J. March-Russell, K.-Y. Oda, S. Park, J. Polchinski, T. Rizzo, S. Rychkov, M. Salaris, M. Srednicki, N. Toro, **I. Tkachev**, M. Vietri, U. Wiedemann and T. Wiseman." All four of the remaining LSAG co-authors (Ellis, Giudice, Tkachev, Wiedemann) are individually named as having provided guidance on the fallback paper.

**Direct support — the primary report imports the fallback paper as its own source, rather than citing an outside, unaffiliated derivation.** src-0001 does not re-derive the accretion bound; it points to src-0002 for it: "This is discussed in full detail in [2], where several accretion scenarios... have been used to set conservative, worst-case-scenario limits to the black hole growth rates" (src-0001, lines 402–406). Reference [2] in src-0001's bibliography (line 1022) is: "S.B. Giddings and M.L. Mangano, CERN-PH-TH/2008-025, arXiv:0806.3381" — src-0002 itself.

**Inference (supported, not directly stated by any source):** Because one author is common to both papers and the other four primary-report authors are named as consulted advisors on the fallback paper, the fallback does not meet a standard test of independent verification (a separate team, unaware of or not consulted by the first team, reaching the same conclusion by a different route). It reads as an internal elaboration by an overlapping subset of the same CERN theory-division collaboration, not a second, disinterested check.

**Partial counterpoint (direct support, narrower claim):** the underlying astrophysical *inputs* to src-0002 — as distinct from its authorship — draw on named external specialists outside the LSAG circle: "We would particularly like to thank O. Blaes for a number of important discussions on Bondi and Eddington accretion, K. Shen and G. Schmidt for guidance on white dwarf structure and populations, and L. Bildsten both for many crucial discussions and for supplying information about neutron-star binary systems" (src-0002, lines 2547–2550); Bildsten and Shen are also cited as private communications for specific data points (src-0002, references [47] and [116]). So the compact-object astrophysics (ages, structure, binary populations) that anchors the fallback's empirical bound is sourced from specialists outside the particle-theory group, even though the argument connecting that astrophysics to LHC black-hole safety was written by an author of the primary report and reviewed by its other four authors. **What the corpus does not establish:** whether Blaes, Shen, Schmidt, or Bildsten reviewed or endorsed the safety conclusion itself, as opposed to supplying astrophysical facts and discussion on request; the acknowledgment records consultation, not independent verification of the argument's use of that data.

**Not established:** No source in this corpus discusses or critiques this authorship overlap. The independence question above is answered from the primary documents' bylines and acknowledgments directly (bibliographic/documentary evidence), not from any secondary source's stated opinion on independence.

---

## 4. Cosmic-ray / accretion-modeling fallback: content and scope

**Direct support.** src-0002's entire subject is accretion modeling for two contexts: (a) a hypothetical stable black hole trapped inside the Earth, and (b) black holes produced by cosmic rays striking white dwarfs and neutron stars. Its summary: "if the radius of crossover from higher-dimensional gravity to four-dimensional gravity is less than about 200 Å, the natural lifetime of the solar system is too short to allow significant growth of stable black holes... In contrast, in a scenario where the crossover radius exceeds the 200 Å scale, accretion times could be shorter than the solar time scale. In this case, however, examination of the latter dense-star scenario then produces an argument that, given observational data setting the lifetimes of such objects at a billion years or more, such stable black holes cannot in fact exist for a crossover radius greater than ≃ 15Å." (src-0002, lines 232–240)

Its dimension-by-dimension summary (§9, lines 2437–2482) makes each branch's empirical anchor explicit: for D=5 and D=6, white dwarf survival over billions of years rules out the scenario; for D=7, massive white dwarf survival over hundreds of millions of years does; for D≥8, neutron star survival over ~10 million years does. The paper's own conclusion states three conditions that would all have to hold simultaneously for the paper's bounds to even be relevant (TeV-scale gravity correct; Hawking radiation wrong; a neutralization mechanism exists without Hawking decay), and states that even then, the astrophysical bound requires the compactification scale to be fine-tuned into a narrow window (src-0002, lines 2487–2523).

**Direct support — this fallback is absent from CERN's public-facing explanation.** src-0004, CERN's own institutional science-outreach page on this topic, states only: "If micro black holes do appear in the collisions created by the LHC, they would disintegrate rapidly, in around 10-27 seconds." (src-0004, line 28) It does not mention Hawking radiation's unconfirmed status, the stable-black-hole hypothesis, the neutralization argument, or the astrophysical fallback at all. **Inference:** the multi-layer conditional structure documented in §§2–4 above exists in the technical literature (src-0001, src-0002) but is not conveyed in CERN's general-public messaging, which presents rapid decay as the unqualified account.

---

## 5. Methodological criticism — and its limits

**Methodological criticism (src-0005), not evidence of danger.** Ord, Hillerbrand, and Sandberg argue that any safety report gives P(disaster | argument is sound), not P(disaster), and that unless the probability of the argument itself being flawed is shown to be extremely small, the true risk estimate could be materially higher than the report's headline number. Applied to the LHC black-hole case specifically:

> "However, our analysis implies that the current safety report should not be the final word in the safety assessment of the LHC. To proceed with the LHC on the arguments of the most recent safety report alone, we would require further work on estimating P(¬A), P(X|¬A)..." (src-0005, lines 729–732)

This is a critique of confidence-methodology completeness — it calls for further work on argument-failure probability, not a claim that the LHC is or was dangerous. **The corpus does not establish, and src-0005 does not claim, that the LHC posed or poses actual danger; it claims the *published confidence level* is not by itself a complete risk assessment.** src-0005 explicitly frames its own paper as subject to the same caveat about itself (lines 768–780) and does not revise its own estimate to suggest elevated real-world risk.

**Methodological criticism (src-0006), narrower scope than the black-hole question.** Kent (2004) predates the 2008 LSAG report and the Hawking-radiation/stable-black-hole debate entirely; its subject is the RHIC/ALICE "killer strangelet" risk-bound-versus-expectation-value framing, not black holes. It is included in this corpus (per `canonical-manifest.json`) as background that "directly frames the LSAG-era debate" methodologically, not as direct testimony on the black-hole warrant chain. Its own final section makes the same distinction this map is instructed to preserve:

> "The particular artificial extinction risk considered in this paper is hypothetical, and there are good arguments to suggest that the actual risk is small or zero." (src-0006, lines 623–624)

Kent's paper argues that risk-bound framing (e.g., "safe to run for 500 million years") systematically understates cost when converted to expectation value, and that the empirical bounds and theoretical arguments in the RHIC/ALICE debate are not independent of each other because "the empirical bounds still rely on theoretical assumptions" (src-0006, footnote 9, lines 362–365) — a structurally similar point to the authorship-dependency finding in §3 above, though Kent makes it about *assumption* dependency for strangelets, not *authorship* dependency for black holes.

**What neither methodological source establishes:** neither src-0005 nor src-0006 concludes that the LHC (or RHIC) was or is actually dangerous, that the probability of catastrophe is non-negligible, or that operation should have been halted. Both explicitly confine their claims to the reliability and completeness of the confidence-reporting method. Reading either as evidence the LHC was dangerous would misstate their scope.

---

## 6. Summary answer to the research question

The safety case for excluding dangerous micro-black-hole production does not rest on Hawking radiation alone with no backup (direct support, §2). It has an explicit conditional fallback for the case where Hawking radiation fails, gated by a further neutralization condition, gated in turn by an astrophysical accretion bound anchored in observed compact-object lifetimes (direct support, §2, §4). That fallback is not authorially independent of the primary report: one author (Mangano) is common to both, and the primary report's other four authors are named as consulted advisors on the fallback paper, which the primary report then cites as its own source rather than as outside verification (direct support, §3). The astrophysical *data* feeding the fallback draws on outside specialists in white-dwarf and neutron-star astrophysics (direct support, §3). Peer-reviewed methodological criticism exists and is substantive, but it targets the completeness of the confidence-reporting method, not the underlying physics, and neither critique concludes the LHC was dangerous (methodological criticism, §5; not established, §5).

The prior proposal's framing — a single linear chain with Hawking radiation as its weakest, unconfirmed link — is partially confirmed (Hawking radiation is indeed theoretically derived and not directly observed, per src-0001 line 348 and src-0002 lines 319–323) and partially refined by this corpus: the actual structure is a branching fallback tree, not a bare chain, and its second-tier robustness depends on shared personnel with the primary report rather than on fully independent verification — a dependency the prior proposal draft does not mention and this corpus does not resolve either way as a matter of danger, only as a matter of documentary record.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
