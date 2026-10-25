# claude-skills

Agent Skills for Claude by Shishir Agrawal. Each skill is a folder under `skills/` with a
`SKILL.md` and whatever scripts or references it needs.

## Skills

| Skill | What it does |
|---|---|
| [sell-my-stuff](skills/sell-my-stuff) | Find what you own from email receipts, price it from sold data, draft eBay and Vinted listings, run a colleague sale page, and handle buyers, postage and order problems (UK). |
| [uk-personal-tax](skills/uk-personal-tax) | Work out whether you need a Self Assessment return, gather the figures from your inbox, compute the tax with a tested calculator, and fill the SA100 box by box. Covers PAYE refunds, leaving the UK, foreign income, crypto, RSUs and Overseas Workday Relief. |
| [india-income-tax](skills/india-income-tax) | File and e-verify an Indian ITR, especially as an NRI abroad: residential status, ITR form and regime, AIS reconciliation, capital gains schedules, DTAA and Form 67, and what to do after a missed deadline. |

## Install

**Claude Code:** each skill is its own plugin, so install only the ones you want:

```
/plugin install sell-my-stuff --marketplace Agrawal-31/claude-skills
/plugin install uk-personal-tax --marketplace Agrawal-31/claude-skills
/plugin install india-income-tax --marketplace Agrawal-31/claude-skills
```

On older versions, add the marketplace once, then install by name:

```
/plugin marketplace add Agrawal-31/claude-skills
/plugin install uk-personal-tax@agrawal-claude-skills
```

**claude.ai:** download a skill folder as a zip and upload it under
Settings → Capabilities → Skills.

Tax skills are guidance, not professional advice; see each skill's `DISCLAIMER.md`.

## License

MIT
