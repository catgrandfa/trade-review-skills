# Trade Review Skills

Five portable AI skills and an optional unified entrypoint for reviewing a trader's own reasoning, plans and execution against their own rules, with traceable evidence.

[中文](README.md) · [Downloads](https://github.com/catgrandfa/trade-review-skills/releases/latest) · [Installation](docs/installation.md) · [Compatibility](docs/compatibility.md)

## One installation, five capabilities

The [trade-review-suite](skills/trade-review-suite/SKILL.md) skill selects the relevant module for each request and includes all references locally. It does not require the five independent skills to be installed.

- [trade-review-suite.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.2/trade-review-suite.zip): `SKILL.md` directly at the ZIP root, with 22 files and no standalone `LICENSE` file.
- [trade-review-suite-folder.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.2/trade-review-suite-folder.zip): identical skill content wrapped in one `trade-review-suite/` folder, for folder-based importers.
- The existing five ZIPs remain available for individual installation. `trade-review-skills-VERSION.zip` is a repository collection for extraction, not a single-skill upload.

For local installation, add `--skill trade-review-suite` to the installer command below. The default still installs the five independent skills. All seven upload ZIPs in 0.3.2 continue to omit the standalone `LICENSE` file. The shared contract and five modules have been updated; MIT metadata is retained. The [SkillHub upload check](docs/skillhub-upload-check.md) covered the 23-file 0.3.0 package. Versions 0.3.1 and 0.3.2 have not been retested on SkillHub; approval and installation remain unverified.

Version 0.3.1 has since been installed and invoked in new WorkBuddy 5.5.6 tasks, and imported from its GitHub release ZIP into ChatGPT's account skill directory for use in a new Work conversation. The [product trial report](docs/product-trials-0.3.1.md) records the exact scope and two behavioral defects; successful installation does not mean every answer passed review.

## Ask your AI to install

Paste this into your current agent:

```text
Install all five skills from https://github.com/catgrandfa/trade-review-skills.
Read the repository's INSTALL.md first, then perform the installation for the current tool rather than only explaining the steps.
Preserve existing customized skills. Report the names, actual destination, and verification results.
If this environment only supports chat or temporary sandbox files, say so and follow the documented alternative; do not claim that reading Markdown is a native installation.
```

The [AI installation entrypoint](INSTALL.md) covers complete skill folders, target selection, file verification, and chat-only fallback. Replace “all five skills” with “the unified trade-review-suite skill” for one entrypoint, or “trade-plan-check” for only that capability.

## Skills

| Skill | Purpose |
| --- | --- |
| `trade-plan-check` | Review a proposed trade for missing conditions and changes from the original plan |
| `trade-execution-review` | Compare reported execution with the plan, separating reasoning, execution and outcome |
| `trade-source-check` | Check whether a quotation preserves its original conditions and limitations |
| `trade-scenario-plan` | Organize user-supplied reasoning into conditional scenarios without inventing trading parameters |
| `trade-rule-cards` | Turn a lesson into a scoped rule card with provenance and adoption status |

Instructions are Chinese-first; each skill tells the agent to follow the user's language. Examples are fictional. The skills do not fetch prices, analyze charts, validate trading signals, connect to brokers, place orders or prove a strategy profitable. User rules are inputs, not universal defaults.

## Start

- Claude/Cowork and WorkBuddy: import one skill ZIP from Releases using the product's custom-skill upload interface.
- ChatGPT: use its Skills interface if available. Otherwise paste a [self-contained text adapter](adapters/plain-chat/trade-plan-check.md), or put [instructions](adapters/chatgpt/instructions.md) in a Project and upload its [knowledge file](adapters/chatgpt/knowledge.md).
- Codex, Claude Code and Cursor: clone this repository and run one of `python3 scripts/install.py --target codex`, `--target claude-code`, or `--target cursor` from the repository root. `--dry-run` previews changes. Python is only needed for maintenance/installation helpers, not skill execution.

Test with fictional input: “My plan was to wait for a pullback. Now I fear missing out and want to enter before defining invalidation. I have not supplied personal rules or market data. Review my plan.”

Expect evidence-based gaps and inconsistencies, not permission to trade. The package follows the Agent Skills format. See the compatibility document for the distinction between documented support, package validation and actual product tests.

## Author experience library

Each skill and text adapter includes an optional [12-lesson author experience library](shared/author-experience.md) with [source notes](shared/author-sources.md), contexts, review questions and boundaries (Chinese). Inclusion does not make a lesson a user's rule. Explicit adoption is respected without repeated confirmation; numeric examples such as risk/reward ratios, loss counts and position proportions remain separate choices. The bundled source description is “根据作者经验” (“based on the author’s experience”). It is independent of personal identities and local projects, and needs no network access at runtime.

The author experience library will continue to be updated and refined. Feedback, suggestions, and requests for additional scenarios are welcome through [Issues](https://github.com/catgrandfa/trade-review-skills/issues).

## Development

Python 3.10+ standard library only:

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

Common instructions are maintained in `shared/`. The suite's modules, templates and examples are generated from the five independent skills; only its routing entrypoint is maintained separately. Text adapters and release assets use the same sources.

[Directory listing material](docs/catalog-listing.md) includes descriptions, use cases, dependencies, licensing, versioned downloads and validation evidence for SkillsMP discovery and SkillCast editorial review. Readiness is not a claim of acceptance or indexing.

Licensed under [MIT](LICENSE). No private journal data or original third-party source materials are distributed. Not affiliated with any agent platform.
