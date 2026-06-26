---
rfc: 0001
title: The seam between the pillars is owned by the producing pillar
status: accepted
pillar: both
author: Hafeok
created: 2026-06-26
supersedes: none
---

# RFC 0001 — The seam between the pillars is owned by the producing pillar

## Summary

Adds a foundation-level rule for the interface between a specification-pillar implementation and an execution-pillar implementation: the side that freezes and hands over the work-unit owns the shape of that handoff (**producer-owns**). Ownership is directional (specification authors and stewards the contract) but not containing (the contract versions independently of any single framework, so swaps on either side do not rewrite it).

## Motivation

The Two Pillars foundation already requires that framework implementations be swappable without disturbing the other pillar. It did not say *who owns the contract* that makes the swap mechanical. Without that, two failure modes are possible: an executor dictates the work-unit format (binding the spec side to one executor), or the contract is treated as jointly owned (no single steward, so it drifts). Both defeat swappability.

The resolution is forced by the frozen-input discipline already in both foundations: a work-unit is a function of its declared input alone, and the side that *produces* that frozen input is the side that declares its form. The consumer cannot own the shape of something it must receive without modification. This belongs at the foundation layer because it governs the relationship *between* the pillars, which no single framework can declare on its own.

## Affected foundation text

`foundations/00-two-pillars.md` — new section **"Who owns the seam between the pillars"**, inserted after "Why the pillars are independent" (it qualifies independence: peers, but the seam is not jointly owned).

## Proposal

Add the section stating:

1. Work crosses as a single frozen, bounded artifact the specification side assembles and hands over.
2. **Producer-owns:** the side that freezes defines the artifact's shape; execution conforms rather than negotiates.
3. Ownership is **directional, not containing** — the specification *pillar* stewards the contract, but it is not an artifact of any one Specification *Framework*, so it versions on its own axis. Neither a framework swap nor an executor swap rewrites it.
4. Practical test: swap executor → spec side unchanged; swap spec tool → executor unchanged.

The completeness criterion: a conforming pair satisfies this rule when the producing side defines the handoff shape, the consuming side conforms to it without callback, and the interface is declared to version independently of both implementations.

## Impact on conformance

Both checklists gain a conditional "seam" section, applicable only when a framework participates in a cross-pillar handoff:

- `conformance/specification-conformance.md` — new **Section 7**: the producing framework defines the handoff shape, freezes it self-contained, versions it independently, and runs seam-dependent gates before emit.
- `conformance/execution-conformance.md` — new **The seam** section: the consuming framework conforms to the producer-defined shape, resolves nothing by callback, returns a self-describing verdict event, and imposes no producer change on executor-side changes.

No existing self-declared statement is invalidated: the sections are conditional ("only if the framework hands work to / consumes work from the other pillar"). A single-pillar framework checks nothing new.

## Stability justification

This is additive. It names a rule the foundation already implied and that working implementations (the Work-Unit Interface between product-cli and the Spark substrate) already embody. It removes ambiguity rather than changing a requirement, so nothing previously conforming becomes non-conforming. Under the governance versioning policy this is a **MINOR** change.

## Alternatives considered

- **Jointly owned, specification authors canonical version.** Rejected: "jointly owned" leaves no single steward and invites drift; the directional rule is cleaner and matches the freeze discipline.
- **Split ownership — specification owns outbound (WorkUnit), execution owns inbound (VerdictEvent).** Rejected: the verdict event is still produced *against* the frozen bundle the spec side defined (it echoes `bundle-hash`, `unit-ref`, lineage). Splitting ownership would let the two halves of one contract version independently and drift apart. One producer, one steward, one contract.
- **Do nothing.** Rejected: the swappability promise is unenforceable without naming who owns the seam.

## Open questions

None blocking. A future RFC may generalize "producer-owns" to any artifact crossing a role or pillar boundary, not only the work-unit seam — but that generalization is not required now.
