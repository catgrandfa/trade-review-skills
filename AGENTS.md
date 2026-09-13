# Project instructions

This is an open-source, Chinese-first collection of five portable decision-review skills. It reviews user-supplied trading reasoning and execution; it has no market-data engine, brokerage integration, or automatic trading.

- Keep the five skills independently installable. Common reference sources live in `shared/`; `python3 scripts/build.py` copies them into every skill and generates text adapters and ZIPs. Do not hand-edit generated copies.
- Preserve the distinction between reported facts, opinions, plans, executions, and AI interpretations. Cite supplied evidence and use “unknown” when it is missing. User rules are configurable; no personal author's discipline is a universal default.
- All examples and behavioral evaluations must be synthetic. Do not import personal journals, account information, private paths, or original third-party source materials. Describe the approved 12-lesson reference library only as “根据作者经验”; do not identify individuals, accounts, external publications, or local projects as its source. Preserve its scope and optional numeric parameters, and never treat inclusion as a user's adoption. Use neutral author/source wording in examples and filenames as well. This attribution wording applies to the bundled library only; preserve evidence attribution for materials supplied by the skill user.
- Runtime skills are Markdown-only and require no API, network, Python, or sibling repository. Build and installation helpers use Python 3.10+ standard library only.
- Run `python3 scripts/build.py`, `python3 scripts/validate.py`, `python3 -m unittest discover -s tests -v`, and `git diff --check` after relevant changes. Structural checks do not prove trading effectiveness or platform end-to-end compatibility.
- Before publishing material changes to decision behavior, use an independent agent to exercise the affected skills on isolated synthetic cases. Keep the request blind to expected answers; review the actual output and record evidence honestly.
- Keep platform support claims tied to official documentation and distinguish package checks, behavioral trials, and actual product installation tests. Never imply installation into a user's account without evidence.
- Keep changes focused; version release notes and use explicit release assets. Never stage files outside this repository.
