---
rfc: 0002
title: Each SPMC axis must be pinned to the precision at which it affects output
status: accepted
pillar: specification
author: Hafeok
created: 2026-06-26
supersedes: none
---

# RFC 0002 — Each SPMC axis must be pinned to the precision at which it affects output

## Summary

Strengthens the SPMC definition: an axis is completely specified only when every property that affects output is fixed. A label that two different behaviors could share is not a binding — it is a confound. Adds the general principle and tightens the Schema and Model axis definitions, which were specifiable by a bare label (a shape with no shape language; a model with no served precision or invocation parameters).

## Motivation

The foundation already claims SPMC supports per-axis attribution: a quality change can be assigned to exactly one of Schema / Prompt / Model / Context. That claim is only true if each axis is pinned tightly enough that an unrecorded change underneath a stable label is impossible. Two axes failed that bar as written:

- **Schema** said "the shape output must conform to" but not the shape language conformance is decided in. The same intent in two shape languages admits and rejects different output — so "Schema unchanged" did not guarantee conformance behavior unchanged.
- **Model** said it is "the concrete, capability-tagged model" selected by remaining complexity, but a model *name* does not fix served precision/quantization or invocation parameters. Two endpoints with the same name at different quantization produce different output — so "Model unchanged" did not guarantee generation behavior unchanged.

Context already met the bar (frozen, bounded, content-hashed bundle), and needs no change. The fix is to name the general property both gaps are instances of, so future axes and future frameworks are held to it rather than patched case by case.

## Affected foundation text

`foundations/01-specification-framework.md`, section **SPMC: From Specification to Execution**:
- the **Schema** axis paragraph
- the **Model** axis paragraph
- a new subsection **"Each axis is pinned to the precision at which it affects output"** after the four axis definitions, before "SPMC as a quality diagnostic"

## Proposal

1. **General principle:** an axis is completely specified only when everything that changes the output is fixed. Test — *if two things can carry the same label and produce different output, the label is not a binding and the axis is underspecified.* Pin to the level at which output stops varying. This precision is the precondition for the per-axis attribution the diagnostic relies on.
2. **Schema** is the output shape **plus its pinned shape language**; conformance is undefined without it, and the shape language is recorded alongside the schema.
3. **Model** is pinned as a **binding**, not a name: served precision/quantization and invocation parameters (temperature, top-p, output limits, seed where honored) are fixed and recorded. A change of binding under an unchanged name is still a Model-axis change and resets the baseline.

The foundation text is kept abstract — it names *served precision* and *invocation parameters* without enumerating a framework's specific binding fields, and names *shape language* without privileging any one formalism. Framework implementations supply the concrete field lists.

## Impact on conformance

`conformance/specification-conformance.md`, Section 5 (SPMC), gains three items:
- Schema pins and records its shape language.
- Model is pinned as a binding (served precision + invocation parameters), not a name.
- Each axis is pinned to the precision at which it affects output — no axis specified by a label two behaviors could share.

No execution-side checklist change. Existing self-declared statements that already pin model bindings and shape languages remain conforming; statements that pinned only names now have a named gap to close, which is the intended effect.

## Stability justification

Additive and clarifying. It does not change the four axes, their ownership, or their derivation — it states the precision the attribution claim always silently required. A framework already doing reproducible attribution (pinning quantization, sampling, and shape language) is unaffected. Under the governance versioning policy this is a **MINOR** change.

## Alternatives considered

- **Leave SPMC as-is; treat binding precision as framework-specific.** Rejected: the attribution guarantee is a *foundation* claim, so the precision it depends on must be foundation-level too, or the guarantee is unbacked.
- **Enumerate concrete binding fields in the foundation** (provider, model ID, fp16/Q4, temperature, …). Rejected: that is framework instantiation and would couple the foundation to today's serving landscape. The foundation names the property; frameworks name the fields.
- **Split Model into two axes (identity vs invocation).** Rejected: both are Model-axis changes for attribution (both reset the baseline). The identity/invocation distinction is a useful framework-level refinement of *how* to sweep them, not a fifth axis.

## Open questions

None blocking. The identity-versus-invocation cut (cheap A/B within one identity vs an identity swap that crosses the cost and capability ladders) is a framework concern; decision-cli specifies it in its entity reference and ADRs. The foundation deliberately stops at "both are Model-axis changes."
