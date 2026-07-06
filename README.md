# AI Development Foundations

**The stable base layer for building software with AI.** Two technology-neutral foundations — one for getting intent into a model correctly, one for letting a model act without losing control — that other people build Specification Frameworks and Execution Frameworks on top of.

> Building software with AI is not one problem. It is two: **getting intent into the machine correctly** (specification) and **letting the machine act without losing control** (execution). These foundations define the minimum each requires, so neither is solved by accident.

This repository holds the two foundations and the process around them. The two-pillars model is the structural idea inside it: two peer foundations, neither containing the other, each built in three layers. Frameworks depend on the foundations; projects depend on frameworks; the foundations depend on nothing below them.

---

## The two foundations

| Pillar | Foundation document | Governs | Governing rule |
|--------|--------------------|---------|----------------|
| **One — Specification** | [Specification Framework](foundations/01-specification-framework.md) | the *input* to AI work | the **derivation contract**: every How traces to a What; every SPMC bundle traces to a How |
| **Two — Execution** | [Execution Contract](foundations/02-execution-contract.md) | the *execution* of AI work | the **closure contract**: every grant traces to a need; every output is verified; every verdict has a consequence |

Read [**The Two Pillars**](foundations/00-two-pillars.md) first — it is the bridge that explains how the pillars relate, why they are independent, and how they carry a team up the autonomy ladder.

The two pillars are **peers**. Neither contains the other, and neither is sufficient alone. A perfect specification fed into an uncontrolled environment produces output no one can trust. A perfectly controlled environment with no specification produces controlled nonsense.

---

## The layer model

Each pillar is a three-layer stack. **Dependencies point downward, toward stability.**

```
ACTUAL IMPLEMENTATIONS    project specs, running pipelines      most volatile
        depends on
FRAMEWORK IMPLEMENTATIONS your methodology / your pipeline      evolves
        depends on
SHARED CONTRACTS          the seam schemas both frameworks use  stable
        depends on
FOUNDATION                this repository                       most stable
```

The **shared contracts** tier holds the concrete schemas that cross the seam between a specification framework and an execution framework — depended on by both, so by the Stable Dependency Principle it sits beneath both and above the foundation it instantiates. It lives in its own repository, [ai-development-contracts](https://github.com/Hafeok/ai-development-contracts).

This repo is the **foundation layer** of both pillars. It defines the standard; it does not prescribe tooling, methodology, or format. Frameworks depend on it. Projects depend on frameworks. The foundation does not churn.

This ordering is not arbitrary — it follows from three design principles that govern the whole repository: the **Stable Dependency Principle**, **Loose Coupling**, and **High Cohesion**. They decide where each concern lives, what may depend on what, and where the boundaries fall. See [The three design principles](foundations/00-two-pillars.md#the-three-design-principles).

---

## Build on this

You are here because you want to author a **Specification Framework**, an **Execution Framework**, or both.

1. **Read the foundation** for the pillar(s) you are building on.
2. **Check your framework against the conformance checklist** — [Specification](conformance/specification-conformance.md) or [Execution](conformance/execution-conformance.md).
3. **Write a conformance statement** using the [template](conformance/CONFORMANCE-TEMPLATE.md) and host it in your own repo.
4. **List your framework** in the [registry](registry/) by opening a PR (see [registry/README.md](registry/README.md)).

Conformance is **self-declared**: you assert it against the checklist, in your own repo, and the registry links to it. There is no gatekeeper sign-off. The checklist is precise enough that a false claim is visible to anyone who reads your framework against it.

---

## Repository layout

```
foundations/   the two foundation documents + the bridge   (normative, CC BY 4.0)
conformance/   checklists + self-declaration template        (normative)
registry/      index of frameworks that build on the pillars (community)
rfcs/          process for proposing changes to a foundation (governance)
```

## Changing a foundation

The foundations are deliberately stable. Material changes go through the [RFC process](rfcs/0000-template.md). The bar is high: a foundation change must justify itself against the stability discipline — everything downstream depends on it not churning.

## License

- **Documentation** (`foundations/`, `conformance/`, `rfcs/`): [CC BY 4.0](LICENSE-DOCS)
- **Code, schemas, and templates**: [Apache-2.0](LICENSE)

See [GOVERNANCE.md](GOVERNANCE.md) for how decisions are made and [CONTRIBUTING.md](CONTRIBUTING.md) to get started.
