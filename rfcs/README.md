# RFCs

The RFC process is how the **foundation documents** change. It exists to keep the foundations stable: a change here ripples through every conforming framework and project, so the bar is deliberately high.

## When you need an RFC

| You want to… | Use |
|--------------|-----|
| Change normative text in `foundations/` | **RFC** (this process) |
| Add or alter a completeness requirement / building block | **RFC** |
| Change a conformance checklist's *meaning* | **RFC** (the checklist tracks the foundation) |
| Fix a typo, broken link, or clarify without changing meaning | a normal PR |
| List your framework | the [registry](../registry/), not an RFC |
| Build a new framework on the pillars | nothing here — just build it and declare conformance |

Most contributions are **not** RFCs. You almost never need to change the foundation to build on it; that is the point of the layer model.

## Process

1. **Draft.** Copy [`0000-template.md`](0000-template.md) to `rfcs/0000-my-title.md` (keep `0000` until assigned). Open a PR.
2. **Discussion.** The PR is the discussion thread. Status is `draft`.
3. **Proposed.** When the author considers it ready, they set status to `proposed` and request maintainer review.
4. **Decision.** Maintainers accept, reject, or request changes per [GOVERNANCE.md](../GOVERNANCE.md). On acceptance, the RFC gets its number and is merged with status `accepted`; the foundation edit lands in the same or a follow-up PR.
5. **Superseding.** A later RFC may supersede an accepted one; the old RFC stays in the tree with status `superseded` and a forward pointer.

Accepted RFCs are never deleted — they are the changelog of the foundations' reasoning.

## Index

<!-- Add accepted/proposed RFCs here, newest last. -->

| RFC | Title | Pillar | Status |
|-----|-------|--------|--------|
| [0001](0001-seam-ownership.md) | The seam between the pillars is owned by the producing pillar | both | accepted |
| [0002](0002-spmc-axis-precision.md) | Each SPMC axis must be pinned to the precision at which it affects output | specification | accepted |
| [0003](0003-design-principles.md) | The three design principles governing the foundation | both | accepted |
| [0004](0004-seam-pattern.md) | The seam pattern — new domains add seams, not pillars | both | accepted |
