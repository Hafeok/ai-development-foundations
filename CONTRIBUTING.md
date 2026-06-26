# Contributing

Thanks for helping build AI Development Foundations. There are four distinct ways to contribute — pick the one that matches what you're doing.

## 1. Build a framework on the pillars

You don't need our permission, and you don't need to touch this repo to start. Read the [foundations](foundations/), build your Specification or Execution framework in your own repo, then:

1. Publish a [conformance statement](conformance/CONFORMANCE-TEMPLATE.md).
2. [List it in the registry](registry/) via PR.

This is the main thing this repo exists to enable.

## 2. List or update a framework in the registry

Edit [`registry/frameworks.yaml`](registry/frameworks.yaml) and the table in [`registry/README.md`](registry/README.md) in the same PR. Use the **"Register a framework"** issue/PR template. See the registry README for what maintainers check.

## 3. Improve the docs without changing meaning

Typos, broken links, clearer phrasing that doesn't alter a requirement — open a normal PR. No RFC needed.

## 4. Change a foundation

Any change to normative text or a completeness requirement goes through the [RFC process](rfcs/). Read [`rfcs/README.md`](rfcs/README.md) first. Expect a high bar and a review window — the foundations are meant to be stable.

---

## Ground rules

- **Match the house style** of the foundations: terse, declarative, no hedging. A requirement is stated as the condition under which it is *met*, not merely present.
- **Don't push volatility downward.** If a thing can live in a framework instead of the foundation, it should.
- **Be precise about conformance.** Partial and honest beats total and vague.

## Licensing of contributions

By contributing you agree your contributions are licensed under the repo's terms: [CC BY 4.0](LICENSE-DOCS) for documentation, [Apache-2.0](LICENSE) for code/templates. See [DCO](#developer-certificate-of-origin).

### Developer Certificate of Origin

Sign off commits with `git commit -s` to certify you have the right to submit them under these licenses.
