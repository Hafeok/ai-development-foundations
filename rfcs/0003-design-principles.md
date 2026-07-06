---
rfc: 0003
title: The three design principles governing the foundation
status: accepted
pillar: both
author: Hafeok
created: 2026-06-26
supersedes: none
---

# RFC 0003 — The three design principles governing the foundation

## Summary

Names the three principles that govern the whole repository and everything built on it: the **Stable Dependency Principle**, **Loose Coupling**, and **High Cohesion**. These were operating implicitly — the layer model, pillar independence, and the seam are all consequences of them — but were never stated as the governing rationale. Stating them makes future structural decisions derivable rather than ad hoc, and in particular makes explicit a conclusion the Stable Dependency Principle forces: a contract shared by two frameworks must live on a layer beneath both, not inside either.

## Motivation

The repository already embodies these principles but only by example. That has two costs. First, a reader sees the *results* (three layers, downward dependencies, a narrow seam, separated pillars) without the single rationale that produces them, so the structure looks like a set of separate choices rather than one coherent stance. Second, future decisions have no stated test to settle them — including the immediate open question of where shared seam schemas live. Naming the three principles gives every future structural question a way to be answered by derivation from the foundation rather than by assertion.

A specific gap motivated this RFC: the question of housing the shared work-unit schemas. An early framing ("the producing framework publishes them") would have placed a shared, depended-upon artifact inside one dependent — which the Stable Dependency Principle forbids, because the other framework would then depend on the first, binding their lifecycles. The principle resolves it cleanly: a shared contract is more stable than both dependents and must sit beneath both. Without the principle stated, that error is easy to make; with it stated, the error is visible.

## Affected foundation text

`foundations/00-two-pillars.md` — new section **"The three design principles"**, inserted after "The problem both pillars solve" and before "Pillar one: specification" (the principles are the lens the rest of the document is read through). Minor tie-in edit to "The shape of the whole" attributing the downward-dependency ordering to the named principle.

## Proposal

State three principles, each naming what it governs:

1. **Stable Dependency Principle** — dependencies point toward stability; the volatile depends on the stable, never the reverse. Orders the layers and serves as a diagnostic (a stable thing forced to change by a volatile one is a mis-pointed dependency). Direct consequence: an artifact shared by two parties must be more stable than both and therefore sit on a layer beneath both, versioning independently — it cannot be housed inside one dependent.
2. **Loose Coupling** — parts interact across a boundary through the narrowest possible declared surface, shared as data not as a live connection. The seam is the worked example (two schemas, two emit-points, freeze-as-decoupling).
3. **High Cohesion** — each part owns exactly one concern wholly; things that change together live together, things that change for different reasons live apart. The test for whether a boundary is correctly placed.

And state how they compose: cohesion decides where boundaries fall, loose coupling decides how the parts interact, the stable dependency principle decides which way dependencies point.

The relationship to **producer-owns** (RFC 0001) is stated explicitly to prevent a conflict: authorship of a contract's shape is directional (the producing pillar writes it); the contract's position in the dependency graph is downward (beneath both dependents). One says who writes it; the other says where it sits. They do not compete.

## Impact on conformance

No checklist change in this RFC. The principles are the rationale layer; the checkable requirements they justify already exist (layer separation, the seam sections, axis attribution). A future RFC that designs the shared-contracts layer will add conformance items; this RFC establishes the principle that such a layer must exist beneath both framework layers.

## Stability justification

Purely additive and explanatory. It introduces no new requirement and invalidates no existing conformance claim — it names the reasons behind requirements already in force. Under the governance versioning policy this is a **MINOR** change.

## Alternatives considered

- **Leave the principles implicit.** Rejected: the shared-contracts question showed that an unstated principle gets violated by plausible-sounding framings. The principles earn their place by settling exactly that kind of question.
- **State only the Stable Dependency Principle** (the one with the immediate consequence). Rejected: the three are a set. Coupling and cohesion answer "where is the boundary and how narrow is it," which the dependency principle alone does not; stating one invites mis-applying it without the other two.
- **Put the principles in a separate `principles.md` foundation doc.** Rejected for now: they are short and they govern how the bridge document's own structure (layers, seam, independence) is to be read, so they belong in the bridge. If they grow, extraction is a later, mechanical move.

## Open questions

The shared-contracts layer itself is **not** designed here (deferred by scope). This RFC establishes only that, by the Stable Dependency Principle, such shared schemas must be more stable than both framework layers and must not be housed inside either.

*Resolved after this RFC:* the contracts layer is its own **distinct tier between the foundation and the frameworks** — it depends on the foundation (it instantiates the seam the foundation defines) and both frameworks depend on it (they share its schemas). "Beneath both frameworks" and "above the foundation" describe the same tier from two directions; there is no contradiction. The contracts layer lives in a separate repository at that tier, governed by its own RFC process, and is stewarded per producer-owns. Its structure is specified there, not here.
