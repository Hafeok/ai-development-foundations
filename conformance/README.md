# Conformance

How to claim that your framework builds on AI Development Foundations.

## The model: self-declared

There is no central authority that certifies frameworks. Instead:

1. You check your framework against the relevant checklist.
2. You publish a [conformance statement](CONFORMANCE-TEMPLATE.md) in **your own** repository.
3. You add a one-line entry to the [registry](../registry/) pointing at it.

This works because the checklists are derived line-by-line from the foundation documents' completeness requirements. A statement that claims conformance is **falsifiable**: anyone can read your framework against the checklist and see whether the claim holds. Self-declaration scales; gatekeeping does not.

## Files

| File | Purpose |
|------|---------|
| [`specification-conformance.md`](specification-conformance.md) | Pillar One checklist — What / How / SPMC / derivation |
| [`execution-conformance.md`](execution-conformance.md) | Pillar Two checklist — eight building blocks / closure |
| [`CONFORMANCE-TEMPLATE.md`](CONFORMANCE-TEMPLATE.md) | The statement you copy into your repo |

## Partial conformance is fine

A framework may conform to only one pillar, or only one layer of a pillar (e.g. a What-layer-only methodology). Declare exactly what you cover. A precise partial claim is worth more than a vague total one.
