# Governance

## What this project governs

This project maintains **three foundation documents** and the process around them. It does **not** govern the frameworks built on top — those are sovereign in their own repos. The registry indexes them; it does not control them.

## Roles

- **Maintainers** — merge PRs, steward the RFC process, curate the registry. Listed in [`MAINTAINERS.md`](MAINTAINERS.md).
- **Contributors** — anyone opening issues, PRs, or RFCs.
- **Framework authors** — maintainers of frameworks listed in the registry; they self-govern their frameworks.

## Decision types

| Change | How it's decided |
|--------|------------------|
| Typos, links, formatting, non-normative clarifications | Single maintainer approval |
| Registry additions/edits | Single maintainer approval (checks existence + statement presence, not claim truth) |
| Conformance checklist edits that don't change meaning | Single maintainer approval |
| **Foundation text / requirement changes** | [RFC](rfcs/), maintainer consensus, minimum review window |
| Governance / license / process changes | RFC, maintainer consensus |

## The stability mandate

Maintainers are biased toward **not** changing the foundations. The whole value of a foundation layer is that frameworks and projects can rely on it not moving. The default answer to a foundation-change RFC is "can this live in a framework instead?" A change ships only when it cannot.

## Foundation change review window

A `proposed` foundation RFC stays open for a **minimum of 14 days** before acceptance, to give downstream framework authors time to weigh in on migration impact.

## Versioning

The foundations are versioned together with semantic tags:

- **MAJOR** — a change that can invalidate existing conformance claims
- **MINOR** — a backward-compatible addition (e.g. a clarified requirement that nothing previously conforming fails)
- **PATCH** — editorial, non-normative

Conformance statements cite the foundation version they were checked against, so a MAJOR bump never silently breaks a listed framework — it just marks it as checked against an older version until the author re-verifies.

## Disputes

Disagreements are resolved on the relevant PR/issue thread by maintainer consensus. There is no private channel; governance happens in the open.
