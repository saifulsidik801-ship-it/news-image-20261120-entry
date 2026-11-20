# news-image-20261120 — TOP 10 STUDY (live board, checked 2026-11-20 ~11:14–11:17 WIB, 2,087 entries)

Scores: #1 kho22 99.1144% | #2 tommyy-ai 98.9671% | #3 rizky-nugraha 98.9427% | #4 siriusjack 98.9188% | #5 gentle-condor-77-2 98.9178% | #6 fauzinfau4 98.9158% | #7 andyku 98.7997% | #8 beru 98.7907% | #9 brisk-falcon-88 98.7835% | #10 febridewa 98.7748%. All provisional (12 matches each). Images: top20/top1.webp–top10.webp.

## Universal pattern (10/10)
- HUGE serif date "Friday 20 November 2026" as the dominant headline.
- Numbers row under the date: 4–6 big stats (300,000 evacuated · $97.17 Anthropic close · 118 Phillips century · 51–48 Senate · $120bn COP31 · 99 GTA VI Metacritic).
- World map "WHERE IT HAPPENED" with numbered red pins matching the lead stories (solid, dotted, or dark styles).
- Numbered LEAD stories with small original illustrations + kicker (CITY · TOPIC) + 2–3 line summary.
- Long numbered "ALSO ON FRIDAY 20 NOVEMBER — N MORE STORIES" / "IN BRIEF" list.
- Sources line: "Sources: Reuters, AP, AFP, BBC..." + the claim "Every story here happened, or was first reported, on Friday 20 November 2026."
- Region bar with story counts per region (e.g. EUROPE 7 · THE AMERICAS 9 · ASIA-PACIFIC 9).

## DATE CHECK box (9/10 — only #9 lacks it)
Red box at the bottom listing what was LEFT OUT because first reported BEFORE Friday. The judge rewards date accuracy. Recurring exclusions across top entries: the Trump–Xi–Putin trilateral meeting itself (19 Nov), ICJ Myanmar genocide ruling (19 Nov), Anthropic's $83 IPO pricing / Nasdaq debut (19 Nov), GTA VI launch + $1.84bn estimate (19 Nov), Voyager 1 one-light-day (18 Nov), Van Gogh $190.4m sale (18 Nov), Fiji drought declaration (18 Nov), Houthi strike on Riyadh PIF Tower (17–18 Nov), Kerch Bridge span falls (17–18 Nov).

## Story counts
#1: 36 | #2: 39 | #3: 22 | #4: 36 | #5: 50 | #6: 16 | #7: 48 | #8: 46 | #9: 28 | #10: 50. Median ~37. Even the thinnest (#6, 16 stories) still carries map + DATE CHECK + numbers row + a "FRIDAY BY THE HOURS" timeline strip.

## Gap vs OUR entry (commit b220740) — and a DATE PROBLEM
- Ours: 5 lead stories + ALSO TODAY strip with 6 items = ~11 stories total. No map, no DATE CHECK, no numbers row, no region bar, no sources line, no per-story source attributions.
- WORSE: our LEAD story (Trump/Xi/Putin three-way summit) is a THURSDAY story — top 1/6/7/10 DATE CHECKs explicitly exclude the trilateral meeting itself from Friday news. Our Myanmar verdict (19 Nov), Anthropic IPO pricing (19 Nov) and Voyager 1 (18 Nov) are also pre-Friday by the same standard. The judge would penalise these as date errors.
- Correct Friday-first leads (what top entries lead with): Cyclone Akvan landfall near Gopalpur ~noon IST (300,000 evacuated), COP31 final day in Antalya (draft cut 144→80 paragraphs, fossil fuels dropped), Anthropic FIRST CLOSE $97.17 +17% (not the $83 pricing), Wall Street falls (Dow −1,101 below 50,000), Nicholls 146* / Phillips 118 cricket, Trump defers Iran decision to 2027, Houthi missile hits Riyadh KAFD tower, Fiji drought disaster, South Korea court clears ex-PM Han.

## Rebuild spec (for the next builder)
Follow #1 kho22's layout (36 stories): huge serif date + red italic sub-headline + numbers row (6 stats) + region bar + 3 big illustrated leads (Akvan / COP31 / Anthropic close) + 10 smaller numbered leads with illustrations + world map with pins + "ALSO ON FRIDAY — 23 MORE STORIES" numbered list + red DATE CHECK box + sources line. Every story must be Friday-first-reported; verify each date against the DATE CHECK exclusions above. 1024×1024, cream paper background, black serif headlines, red accents. Deadline Sat 22 Nov 07:00 WIB.
