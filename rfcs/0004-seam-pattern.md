---
rfc: 0004
title: The seam pattern — new domains add seams, not pillars
status: accepted
pillar: both
author: Hafeok
created: 2026-07-05
supersedes: none
---

# RFC 0004 — The seam pattern: new domains add seams, not pillars

## Summary

Generalizes RFC 0001. The discipline first defined for the specification⟷execution seam (frozen artifact out by value; self-describing event back; producer knows no consumer; producer-owns authorship; contracts-tier housing; optional consumer self-description for pre-flight matching) is named as a **pattern** with multiple instances. A new consumer domain — interface building, flow compilation, or others — adds a **seam instance at a contracts tier**, never a third pillar.

## Motivation

A Reification Contract (specification ⟷ interface: UIIntent out, ReificationReport back) arrived following the seam discipline exactly, but its draft placed itself "at the foundation" and coined an "interface pillar." Both moves were wrong in instructive ways: concrete contracts live at contracts tiers, not in the foundation (settled in RFC 0003's resolution); and the pillars are defined by the two fundamental problems, not by the number of consuming domains. Without a stated pattern, every new seam re-litigates placement and tempts pillar inflation. With it, a new seam is a recognized application.

## Affected foundation text

`foundations/00-two-pillars.md` — new section **"The seam pattern"** after "Who owns the seam between the pillars."

## Proposal

State the five properties of a conforming seam (frozen-by-value outbound; self-describing event inbound; producer-blind-to-consumer; producer-owns with optional consumer capability manifest; contracts-tier housing) and the corollary: **frameworks multiply, seams multiply, the pillar count does not.** A specification framework is the hub with one published socket per seam.

## Impact on conformance

None retroactive. The Build-seam checklists in ai-development-contracts already satisfy the pattern. Future seam instances (e.g. the Reification Contract) declare conformance in their own contracts-tier repos against this pattern.

## Stability justification

Additive naming of a discipline two working instances already follow (Build seam; flows-contracts' Decision seam). MINOR.

## Alternatives considered

- **A third "interface pillar."** Rejected: pillars map to fundamental problems, of which there remain two; interface building is a consuming domain. Pillar inflation would also break the naming and the bridge document's core argument.
- **Leave the pattern implicit.** Rejected: the Reification draft demonstrated the failure mode (self-placement in the foundation, pillar coinage) within one document of the pattern going unstated.

## Open questions

Whether the pattern's optional consumer self-description (capability manifest) should be mandatory for all seams is left to each instance; the Build seam made it normative, the Reification seam may adopt an analog when pre-flight matching matters there.
