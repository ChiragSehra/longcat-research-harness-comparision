# Claim/source trail

The memo is the decision artifact. This file maps its factual claims to sources and records analytical choices. Source IDs resolve in the inventory below and in `sources.json`. `research-log.json` preserves 34 web requests and the response text actually returned, including failures; call numbers are one-based array positions. Calls within parallel batches are listed in request order, not response-completion order. The harness-owned `run.jsonl` and `run.stderr` remain intact.

All research was retrieved on **12 October 2026, Asia/Kolkata**. The evidence cutoff is **11 October 2026, 23:59:59 Asia/Kolkata**, equivalent to **11 October 2026, 18:29:59 UTC**. Retrieval after the cutoff is permitted; post-cutoff events are not evidence. Crawl dates were never used as event dates.

## Claims and locators

| Claim | Status | Sources and locator | Treatment |
| --- | --- | --- | --- |
| C01 BJP 303 → 240; Congress 52 → 99 | Election facts | S01 national-party table, S02 printed p. 9, S03 PDF pp. 1–2 | Seats are election outcomes, not October 2026 membership. |
| C02 BJP valid-vote share 37.70% → 36.56%; Congress 2024 21.19% | Published election statistics | S01 column explicitly labelled total valid votes; S02 BJP comparison; S03 party rows | Do not mix 37.36% (a different 2019 denominator) with this valid-vote comparison. |
| C03 BJP decline 1.14 pp; 63 seats/20.8%; 32 below majority | Author calculations | C01–C02; 37.70 − 36.56 = 1.14; 303 − 240 = 63; 63/303 × 100 = 20.792%; 272 − 240 = 32 | Percentage points distinguish vote decline from relative seat decline. |
| C04 BJP contested 441; Congress 328 | Election compilation | S03 PDF pp. 1–2 | These are contested-seat counts, not support in constituencies where no candidate stood. |
| C05 UP SP 37, INC 6, BJP 33; SP–INC combined 43 | ECI results reported by newspaper | S04 final constituency report | Direct ECI UP page failed extraction; newspaper full winner list used transparently. |
| C06 TDP 16, JD(U) 12, formation NDA 293 | Election/coalition facts | S03 PDF p. 1, S14 printed pp. 1–2 | NDA grouping is date-specific; Lokniti uses a narrower electoral grouping in some tables. Do not silently equate grouping definitions. |
| C07 Both partners removed → 265; either removed → 277 or 281 | Arithmetic scenario | 293 − 16 − 12 = 265; 293 − 16 = 277; 293 − 12 = 281 | Stylised formation-time scenario; no claim of an October floor count or member behaviour. |
| C08 Haryana BJP 48/90 | Final election result, secondary | S05 October 8, 2024 full list | No extrapolation to national voting. |
| C09 Maharashtra BJP 132, SHS 57, NCP 41; total 230 | Final results, government broadcaster | S06 November 24, 2024 | Total calculated by summation. These are the named three partners, not every NDA-supported winner. |
| C10 Jharkhand JMM 34, Congress 16 | Final results, government broadcaster | S06 | Regional counterevidence; this is not the entire INDIA alliance tally. |
| C11 Delhi BJP 48, AAP 22 | ECI-derived table | S07 performance-of-parties table | ADR document reproduces election results alongside expenditure disclosures. Distinguish 45.82% valid votes from 45.56% including NOTA; neither percentage is used in memo. |
| C12 Bihar NDA 202/243; BJP 89, JD(U) 85 | ECI results reported by AP | S08 Rajesh Roy, November 14, 2025 | Original AP URL inaccessible on reopening; accessible verbatim AP syndication used. |
| C13 Assam BJP 82/126 | Official results portal, search-index text | S09 party totals, last updated May 5, 2026 | Direct open failed; subsequent search returned complete party totals with zero leads. A secondary embedded widget showed 79 and was rejected in favour of ECI. |
| C14 Tamil Nadu TVK 108, DMK 59, BJP 1 / 234 | Official results portal, search-index text | S10 party totals, last updated May 5, 2026 | TVK 108 is below 118 majority; do not call it an outright majority. |
| C15 Kerala INC 63, BJP 3 / 140 | Official successful-candidate summary | S11 final party-wise summary | Party totals, not a reconstructed alliance total. |
| C16 Bengal initial 207/293 → completed 208/294 | ADR initial tally; final reporting | S15 final-party-position table; S12 May 24, 2026 Falta result | Initial ECI portal and ADR tally predate Falta. No claim that 208 remains current membership after resignations/byelections. |
| C17 BJP remains system-defining despite setback | Named expert interpretation | S16 Vaishnav and Mallory, September 26, 2024 | Attributed expert judgment; later results independently used to test it. |
| C18 UP non-Jatav SC NDA support 48% → 29%; Brahmin 82% → 79%; Muslim SP–INC 92% | Survey estimates, expert synthesis | S14 printed pp. 27–28, figure 17 and following paragraph | BJP-led alliance versus BJP alone distinguished. Figure's caste categories are not national estimates. |
| C19 INC promised caste census/reservation amendment; government approved caste enumeration | Party commitments and official announcement | S17 social justice items 1–2; S18 April 30, 2025; S19 April 25, 2026 | Promises and decisions are verified; electoral causation and implementation success are not. |
| C20 Unemployment 23.1%, inflation 23.8%, Ram Mandir 22.4% | Weighted national survey tabulation | S20 Q11a–Q11b, PDF pp. 7–9 | Correct denominators and wording: most liked/disliked government work, not reasons for voting. |
| C21 Ration continuation/senior health coverage | Party manifesto commitments | S21 “Free Ration for the Next 5 Years” and senior citizen section | Original BJP-hosted PDF failed; identical party-authored document obtained from Supreme Court Observer mirror. Benefits delivery is not inferred from promise. |
| C22 Maharashtra women advantage 3 pp; farmers supported incumbent despite distress; welfare associations mixed | Named survey analyses | S22 PDF pp. 2–3, Deshpande and farmer analysis | Contributions differ within compilation; no causal welfare coefficient or nationally fixed women/farmer bloc claimed. |
| C23 Jharkhand identity/Adivasi mobilisation, limited Hindutva rewards | Named expert interpretation | S23 Suhas Palshikar analysis, PDF p. 2 | State-specific interpretation, not a universal tribal vote estimate. |
| C24 Andhra ₹15,000 crore arrangement and Bihar support | Budget announcements | S24 speech paras. 30–36, printed pp. 7–8 | Facilitated multilateral finance is not an unconditional ₹15,000 crore grant or verified spend. |
| C25 Waqf amendment passed April 2025 | Legislative event | S25 minority-affairs section | Passage only; no claim that every provision subsequently operated unchanged. |
| C26 April 2026 constitutional amendment failed, 298–230 | Legislative event, official public broadcaster | S26 April 18, 2026; S13 law-and-justice section | April episode, not a blanket claim that every later delimitation measure failed. PRS generic bill lists had inconsistent snippets; dated episode preferred. |
| C27 Monsoon 2026 12 Bills passed, simultaneous-elections amendment in committee | Legislative tracker | S27 July 20–August 13, 2026, government-Bills table/pending Bills | This tracker cites parliamentary Bills and bulletins; direct official division reconstruction not obtained. |
| C28 September southern-representation disagreement | Dated report | S28 September 29, 2026 | Used only for the fact of disagreement; not its constitutional merits. Stay within the source's 25-word derivation allowance. |
| C29 20 TMC MPs claimed NDA support; announced NCPI merger | Attributed contemporary reports | S29 June 8, 2026 PTI; S30 June 14, 2026 | Statements distinguished from legally settled membership; no uncertified updated NDA total. |
| C30 MPs do not automatically supply new voters/organisation | Named interpretation | S31 Pratul Sharma, June 19, 2026 | Parliamentary and electoral realignment distinguished. |
| C31 Survey n=19,663, 23 states, 191 constituencies | Research-method metadata | S32 2024 post-poll row | No individual longitudinal follow-up established. |
| C32 Deletion counterfactual needs extreme assumptions to reverse Bengal majority | Original expert sensitivity analysis | S33 Debraj Ray, May 10, 2026, especially pp. 1–3 and conclusion | Conditional model result, not adjudication of electoral-roll fairness. |

## Reproduction and adjudication notes

1. Open `report.md`; match every direct URL to the source inventory. Search its URL and relevant claim text in `research-log.json`. Original request payloads allow the same search/open/find steps to be rerun.
2. Retain source authorship, publication date, election date and retrieval date separately. ECI result portals explicitly distinguish displayed counting results from final Form-20 records. This run did not download and reaggregate all Form-20 records.
3. Primary-source priorities: official ECI/CEO tables, government statistical tables, budget and Cabinet publications, party-authored manifestos. Use Lokniti for survey research, PRS for legislative tracking and named expert papers for interpretation. Use attributed news reports when official extraction fails.
4. Preserve contradictions rather than average them: 2019 denominators; alliance membership definitions; early counts versus complete Bengal election; conflicting Assam secondary widgets; election-time seats versus current MPs; welfare correlations versus causal claims.
5. The September 2026 PRS monthly review and late political searches were checked for material developments. A rolling PRS homepage included an October 22 notice beyond the cutoff; it was not evidence. The September monthly review's unrelated economic measures were not added merely to make the memo appear current.
6. Technical limits: direct shell downloading failed DNS; some official web pages returned internal errors or a single line, although indexed results exposed their tables. The archive is the tool's retrieved text, not a claim to have preserved every webpage's full HTML/PDF or the search engine's underlying index.
7. The initial discovery search preceded the separate JSON archive; the native harness log preserves that execution. The archive later reacquired supporting Bihar reporting via AP syndication. No private source pack, competitor memo, external outline, delegated agent or extra model review was used.
8. Analytical inference is signposted throughout the memo. The conclusion is a qualitative decision under uncertainty, without invented probabilities or a claim that one national election identifies a new equilibrium.

## Source inventory

- **S01** — [2019 government statistical table](https://static.pib.gov.in/WriteReadData/userfiles/GE2024/files/basic-html/page67.html); research-log calls 31, 32.
- **S02** — [2024 government summary](https://newindiasamachar.pib.gov.in/WriteReadData/Magazine/2024/Jun/M202406161.pdf); research-log calls 12.
- **S03** — [Lokniti election tables](https://www.lokniti.org/media/PDF-upload/1755059632_52889800_party_performance.pdf); research-log calls 6, 7, 11.
- **S04** — [Constituency results](https://indianexpress.com/elections/2024-uttar-pradesh-lok-sabha-election-results-full-list-of-winners-on-all-80-seats-of-uttar-pradesh-9365613/); research-log calls 29.
- **S05** — [Haryana results](https://indianexpress.com/elections/haryana-elections-results-full-list-of-winners-9607858/); research-log calls 7.
- **S06** — [public broadcaster’s final summary](https://newsonair.gov.in/bjp-led-mahayuti-alliance-sweeps-assembly-elections-in-maharashtra-jmm-led-india-bloc-retains-power-in-jharkhand/); research-log calls 7.
- **S07** — [ADR’s ECI-derived Delhi table](https://www.adrindia.org/sites/default/files/English_Analysis_of_Funds_Collected_Expenditure_Incurred_Political_Parties_Delhi_Election_2025.pdf); research-log calls 23, 30.
- **S08** — [Bihar results](https://halifax.citynews.ca/2025/11/14/modis-coalition-leads-in-a-key-indian-state-election/); research-log calls 34.
- **S09** — [ECI Assam](https://results.eci.gov.in/ResultAcGenMay2026/partywiseresult-S03.htm); research-log calls 2, 9.
- **S10** — [ECI Tamil Nadu](https://results.eci.gov.in/ResultAcGenMay2026/partywiseresult-S22.htm); research-log calls 2, 3, 10, 15.
- **S11** — [CEO Kerala final candidates](https://www.ceo.kerala.gov.in/ceokerala/pdf/govt_orders/legislative-assembly-2026/statistical-report/2-List_of_Successful_Candidates_1778164525.pdf); research-log calls 3.
- **S12** — [Falta final report](https://www.newindianexpress.com/states/west-bengal/2026/May/24/counting-underway-for-falta-assembly-repoll-in-bengal-bjp-takes-commanding-lead-after-five-round); research-log calls 28.
- **S13** — [PRS April review](https://prsindia.org/policy/monthly-policy-review/april-2026); research-log calls 4, 20.
- **S14** — [contemporary NDA total, printed pages 1–2](https://assets.carnegieendowment.org/static/files/Vaishnav%20Mallory%20-%20Reassessing%204th%20Party%20System.pdf); research-log calls 16, 20, 23, 24, 32.
- **S15** — [ADR initial Bengal tally](https://www.adrindia.org/sites/default/files/West_Bengal_Assembly_Elections_2026_Criminal_and_Financial_background_details_of_Winning_Candidates_FinalVer_Eng_0.pdf); research-log calls 3.
- **S16** — [Carnegie paper](https://carnegieendowment.org/research/2024/09/india-election-bjp-party-politics); research-log calls 14, 17, 22.
- **S17** — [Congress manifesto](https://manifesto.inc.in/en/equity/); research-log calls 5.
- **S18** — [Cabinet announcement](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2125526&lang=1&reg=1); research-log calls 2.
- **S19** — [2026 census backgrounder](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255461&lang=1&reg=3); research-log calls 2.
- **S20** — [Survey, questions 11a–11b](https://lokniti.org/media/PDF-upload/1718435207_67606300_download_report.pdf); research-log calls 1, 2, 3, 5, 14, 24.
- **S21** — [BJP manifesto document](https://www.scobserver.in/wp-content/uploads/2024/04/2024-BJP-Election-Manifest-English.pdf); research-log calls 5, 30, 32.
- **S22** — [Lokniti’s original newspaper compilation, PDF pages 2–3](https://lokniti.org/media/upload_files/Lokniti-CSDS%20Maharashtra.pdf); research-log calls 14, 25, 30.
- **S23** — [Lokniti Jharkhand analysis](https://lokniti.org/media/upload_files/Jharkhand%20Articles%20%281%29.pdf); research-log calls 16, 30.
- **S24** — [Budget speech, paragraphs 30–36](https://www.indiabudget.gov.in/budget2024-25/doc/Budget_Speech.pdf); research-log calls 7, 11.
- **S25** — [PRS April 2025 review](https://prsindia.org/policy/monthly-policy-review/april-2025); research-log calls 19.
- **S26** — [public broadcaster’s division report](https://newsonair.gov.in/hi/131st-constitutional-amendment-bill-not-passed-lok-sabha-vote-count/); research-log calls 20.
- **S27** — [PRS session wrap](https://prsindia.org/sessiontrack/monsoon-session-2026/session-wrap); research-log calls 21, 22.
- **S28** — [September 29 debate](https://www.indiatoday.in/india/story/delimitation-federalism-debate-south-parties-warn-on-voice-bjp-backs-process-3005847-2026-09-29); research-log calls 20.
- **S29** — [PTI account](https://theprint.in/india/after-assembly-revolt-tmc-split-reaches-lok-sabha-as-20-mps-form-separate-bloc-back-nda/2954472/); research-log calls 21.
- **S30** — [merger announcement](https://www.ndtv.com/india-news/trinamool-rebel-bloc-to-merge-with-nationalist-citizens-party-kakoli-ghosh-11635562/); research-log calls 21.
- **S31** — [Sharma analysis](https://www.theweek.in/voices/columns/pratul-sharma/2026/06/19/anti-defection-law-tenth-schedule-coalition-politics-parliament-monsoon-session.html); research-log calls 20, 21.
- **S32** — [Study metadata](https://www.lokniti.org/national-election-studies); research-log calls 1, 2, 3, 6, 14.
- **S33** — [Ray’s original paper](https://debrajray.com/wp-content/uploads/2026/05/SIR2026.pdf); research-log calls 3, 4, 5, 6, 11.

