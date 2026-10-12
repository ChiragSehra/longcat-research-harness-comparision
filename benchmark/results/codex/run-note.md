# Codex benchmark run note

- **Brief:** `benchmark/political-realignment-2024-india.md`.
- **Model:** `gpt-6.1-sol`.
- **Reasoning effort:** `medium`.
- **Model/effort provenance:** the brief and the project results register identify this native Codex run as GPT-6.1 Sol / medium. No model substitution, delegated agents, or extra model pass was requested or used. The active tool interface does not independently attest the serving model; a lookup of this thread in the local state database returned no row. The global Codex default names a different model and therefore was not treated as evidence of this invocation's model. These distinctions are recorded rather than claiming independent runtime verification.
- **Harness:** native ChatGPT-authenticated Codex CLI, as identified by the project register; thread `01a12e97-4f96-7ae2-be7a-bef606de8135`.
- **Start, Asia/Kolkata:** **2026-10-12 11:00:31.533472 +05:30**. This is the earliest harness timestamp available, from the existing stderr entry; first explicit clock observation was 11:00:41 +05:30. It is not an independently observed process-launch timestamp.
- **End, Asia/Kolkata:** **2026-10-12 11:14:51 +05:30**, artifact finalisation timestamp.
- **Corresponding UTC interval:** 2026-10-12 05:30:31.533472 UTC to 2026-10-12 05:44:51 UTC.
- **Observed elapsed time:** 859.467 seconds, approximately 14.32 minutes, measured from the earliest harness timestamp to artifact finalisation.
- **Evidence cutoff:** 2026-10-11 23:59:59 Asia/Kolkata (2026-10-11 18:29:59 UTC).
- **Memo length:** **1,957 words**, counting whitespace-separated visible Markdown text; stripping citation URL targets produces the same count.
- **Citation coverage:** 49 direct URL citations to 33 distinct cited URLs. The trail maps 32 claim groups and calculations.
- **Research archive:** 34 web requests with the verbatim returned text. One initial discovery request precedes this separate archive; its execution is in the native event log. All final cited sources have supporting returned text in the archive. It is not a collection of complete website HTML or complete binary PDFs.

## Research steps

1. Read the brief, searched for applicable AGENTS.md files, recorded time, inspected existing output/log files, and recorded pre-existing repository changes. No additional project AGENTS.md was found in the directory search.
2. Searched for ECI 2024 national statistics and subsequent election outcomes. Tried direct ECI portals, ECI statistical-report indexes and static atlas pages. Used accessible official CEO Kerala results and complete search-index text from the official Assam/Tamil Nadu result portals.
3. Retrieved Lokniti national election tables, the original weighted 2024 post-poll questionnaire/tabulations and study metadata. Compared national vote shares, party contest counts, social-group evidence and the implications of changing alliance definitions.
4. Reviewed party-authored manifestos, the July 2024 government Budget speech and official 2025/2026 caste-enumeration announcements. Distinguished campaign promises and policy announcements from implemented benefits or spending.
5. Checked the 2024 Haryana, Maharashtra and Jharkhand tests, 2025 Delhi and Bihar, and 2026 Assam, Bengal, Kerala and Tamil Nadu. Reconciled Bengal's 207-seat preliminary complete-count tally for 293 constituencies with its later 208-seat completed election after Falta.
6. Reviewed named analyses by Milan Vaishnav and Caroline Mallory; Lokniti researchers including Suhas Palshikar and Rajeshwari Deshpande; Debraj Ray's original Bengal sensitivity analysis; and Pratul Sharma's account of parliamentary realignment. Attributed expert judgments rather than treating them as official election facts.
7. Searched parliamentary/government records and PRS legislative trackers. Checked April 2025 Waqf passage, April 2026 delimitation-amendment defeat, the July–August 2026 Monsoon Session, June 2026 reported Trinamool MP movements, September policy reporting and the September 29 delimitation debate. A rolling PRS homepage's October 22 notice was beyond the cutoff and excluded.
8. Calculated seat losses, valid-vote percentage-point changes, the Maharashtra three-party total and formation-time coalition withdrawal scenarios. Kept survey support, official election outcomes, elite movements and interpretation separate.
9. Wrote the memo, raw web archive, source inventory and claim/source map. Verified both JSON files, word range, required uncertainty section, evidence-table presence, every memo URL's inventory entry and every cited source's occurrence in its indexed archive calls. Completed this note without modifying the benchmark brief, results register, competing outputs or other repository files.

## Source-access limitations and unresolved questions

- Multiple direct ECI result-page opens returned internal errors, while statistical-report index/atlas pages sometimes exposed only one line. An inferred static 2024 statistical-PDF path also failed; it was not used as evidence.
- The official Assam and Tamil Nadu portal totals were available through search retrieval despite direct-open failures. Kerala's CEO published an accessible final successful-candidate summary. The run did not independently reaggregate all constituency Form-20 records.
- ECI was prioritised; where extraction failed, final ECI results reported by a government broadcaster, ADR, AP or attributed newspapers were used with direct links. Search results from Wikipedia, anonymous websites and Reddit were discovery leads; no Wikipedia or Reddit URL is cited in the final memo.
- The original AP Bihar page reopened unsuccessfully. The final memo cites the accessible CityNews syndication of Rajesh Roy's AP report, with the same named author and final tally.
- BJP's own manifesto PDF failed direct access. A mirror of the party-authored manifesto at Supreme Court Observer was inspected; this is document provenance through a mirror, not an independent adjudication of party claims.
- Shell-based urllib downloading failed with DNS resolution errors, so no downloaded source binaries are claimed. Web-tool extraction, returned search text and find locators supply the stored evidence.
- Lokniti weighted responses are survey estimates, not electoral caste counts or a voter panel. Some tabulations have internal anomalies outside the questions used; the memo uses identified questions and published methods and avoids unsupported causal coefficients.
- 2019 BJP shares of 37.36% and 37.70% occur in different presentations. The memo uses the government table explicitly labelled percentage of total valid votes: 37.70%, matched to the 2024 published valid-vote series of 36.56%. Congress's 2019 52-seat baseline is also in that government table.
- Alliance grouping differs between the narrower Lokniti constituency-level electoral grouping and the broader NDA/INDIA totals in contemporary accounts. The memo does not equate these definitions or sum overlapping party totals.
- Final Bengal election results differ from early tallies because Falta voted later. A secondary Assam widget contradicted the official portal, so the official 82-seat BJP figure was preferred.
- No certified 11 October 2026 parliamentary roster, Speaker's final recognition decision for every reported merger, or independently assembled division transcript was obtained. June MP movements are reported claims/announcements; coalition arithmetic is explicitly formation-time arithmetic. PRS and the public broadcaster establish specific legislative episodes.
- PRS generic bill-list search snippets were inconsistent about the 131st amendment's status. The dated April defeat and the Monsoon Session table were used; the memo does not assert a universal current status for every later delimitation proposal.
- Source pages were retrieved on 12 October, but cited events/publications fall before the cutoff. This is a bounded search and assessment, not a guarantee that every relevant development through the cutoff was discovered.

## Files written and logs preserved

**Authored by this run:**

1. `benchmark/results/codex/report.md` — final decision memo.
2. `benchmark/results/codex/run-note.md` — this note.
3. `benchmark/results/codex/claim-source-trail.md` — factual claim map, locators, calculations, discrepancies and reproduction instructions.
4. `benchmark/results/codex/sources.json` — 33 cited URLs and their one-based research-log call indexes.
5. `benchmark/results/codex/research-log.json` — 34 original web request payloads and returned response texts, including failures.

**Existing harness-owned logs preserved without direct editing:**

- `benchmark/results/codex/run.jsonl` — native events, automatically appended by the launcher.
- `benchmark/results/codex/run.stderr` — launcher diagnostics.

No unrelated files were authored or modified. Existing unrelated parent-repository changes were left untouched. The project results register was read only to establish run metadata; competitor reports and source trails were not read. No private source pack, human outline or second model evaluation was introduced.

