# Registry

Frameworks that build on AI Development Foundations. Each entry links to a framework hosted in **its own repository**, along with that framework's self-declared conformance statement.

This registry is an **index, not a host.** Frameworks live wherever their authors keep them; this repo just points to them and records what they claim to conform to.

## Listed frameworks

<!-- Keep this table sorted by pillar, then name. Add your row in the same PR that adds your entry to frameworks.yaml. -->

| Framework | Pillar | Layers / blocks | Conformance statement | Maintainer |
|-----------|--------|-----------------|------------------------|------------|
| _(example)_ Decision-Driven Design | Specification | What · How · SPMC | _link_ | — |
| _(example)_ Assembly Line Protocol | Execution | all 8 blocks | _link_ | — |

> The example rows are illustrative placeholders drawn from the foundation documents. Replace or remove them once real adoptions land.

## How to add your framework

1. Publish a [conformance statement](../conformance/CONFORMANCE-TEMPLATE.md) in your framework's repo.
2. Fork this repo.
3. Add an entry to [`frameworks.yaml`](frameworks.yaml) following the schema in that file.
4. Add a matching row to the table above.
5. Open a PR using the **"Register a framework"** template.

A maintainer will check that:

- the linked repo exists and is public,
- a conformance statement is present at the linked URL,
- the declared pillar/layers match what the statement actually claims (not whether the claim is *true* — that is the author's assertion and the reader's to verify).

Listing is **not** an endorsement or a certification of correctness. It records a self-declared claim and makes it discoverable.

## Removal

Open a PR or issue if a listed framework's repo is gone, its statement has been removed, or its entry is materially inaccurate.
