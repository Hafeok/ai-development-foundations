---
rfc: 0000
title: <descriptive title>
status: draft   # draft | proposed | accepted | rejected | withdrawn | superseded
pillar: <specification | execution | both | process>
author: <name / handle>
created: YYYY-MM-DD
supersedes: <rfc number, or none>
---

# RFC 0000 — <title>

## Summary

One paragraph. What does this change, in plain terms?

## Motivation

What problem in a **foundation document** does this solve? Foundation changes carry a high burden: everything downstream depends on the foundation not churning. A change that belongs in a *framework* rather than the foundation should be made in that framework, not here. State explicitly why this must live at the foundation layer.

## Affected foundation text

Quote the exact section(s) of `foundations/` this RFC alters. Link by file and heading.

## Proposal

The precise change. If it edits normative text, show the before/after. If it adds a requirement, state its completeness criterion in the same style as the existing requirements (a requirement is met when ___, not merely present).

## Impact on conformance

- Does this change the [conformance checklists](../conformance/)? Show the checklist edits.
- Does it invalidate existing self-declared conformance statements? If so, how should already-listed frameworks migrate, and over what window?

## Stability justification

The foundations are the most stable layer by design. Argue that this change is worth the churn it imposes downstream — or that it imposes none. An RFC that cannot make this argument should not be a foundation RFC.

## Alternatives considered

What else was considered, and why was it rejected? Include "do nothing."

## Open questions

Unresolved points that reviewers should weigh in on.
