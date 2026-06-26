# Specification Framework — Conformance Checklist

A framework conforms to **Pillar One** when it gives its users a concrete, opinionated way to produce specifications that satisfy every requirement below. The framework does not have to use these names or formats — it has to make each requirement *achievable and checkable* in its own terms.

A conformance claim is an assertion that **a spec authored under your framework cannot pass your own process while leaving any of these requirements unmet.**

> Source of truth: [`foundations/01-specification-framework.md`](../foundations/01-specification-framework.md). Where this checklist and the foundation differ, the foundation governs.

---

## Section 0 — Premise

The framework treats a specification as an **LLM input artifact**, not after-the-fact documentation. Specs produced under it are:

- [ ] **Unambiguous** — every term defined, no decision left to inference
- [ ] **Complete at the boundary** — no required input to the next stage is missing
- [ ] **Internally consistent** — contradictions are resolved in the spec, not by the model
- [ ] **Machine-readable** — structured, not free-form prose
- [ ] **Explicitly bounded** — out-of-scope is declared, not assumed

## Section 1 — Layer separation

- [ ] The framework keeps **What**, **How**, and **SPMC** as distinct concerns and does not collapse them.
- [ ] The **What** is ownable and validatable by a customer/product role with no technical knowledge.
- [ ] The **How** is authored by the development team and **derived** from the What — it does not restate it.
- [ ] Each discrete unit of work decomposes into an **SPMC** bundle before a model consumes it.

## Section 2 — What completeness

The framework's What artifact requires, for any project regardless of size:

- [ ] **Identity** — single unique name, used consistently downstream
- [ ] **Purpose** — problem / who has it / why a system is needed, answerable without prior knowledge
- [ ] **Actors** — every interacting person/role/system, with what each may and may not do
- [ ] **Behaviors** — every behavior with initiator, precondition, postcondition, **and unhappy path**
- [ ] **Boundaries** — explicit in-scope and out-of-scope lists; out-of-scope is **non-empty**
- [ ] **Data** — every entity created/read/updated/deleted, with owner and lifecycle
- [ ] **Constraints** — every non-derivable rule, with source and a way to verify it
- [ ] **Acceptance Criteria** — at least one testable criterion per behavior, referencing that behavior
- [ ] **Open Questions** — every known unknown, with owner and what it blocks

## Section 3 — How completeness

The framework's How artifact requires:

- [ ] **What Reference** — identity and version of the What it derives from
- [ ] **Components** — single-responsibility units, dependencies directed and acyclic
- [ ] **Data Model** — a technical representation for every What data entity, no orphan entries
- [ ] **Integrations** — every external system, direction, protocol, contract, **and failure behavior**
- [ ] **Decisions** — every non-derivable choice with question, decision, rationale, rejected alternatives, driving What element
- [ ] **Error Handling** — a declared behavior for every error category
- [ ] **Non-Functional Requirements** — a specific, measurable threshold for every What constraint
- [ ] **Open Questions** — propagated and structured as in the What

## Section 4 — The derivation contract

The framework enforces, or makes auditable, all five rules:

- [ ] Every component traces to ≥1 What behavior or data entity
- [ ] Every data model entry maps to a What data entity
- [ ] Every non-functional requirement maps to a What constraint
- [ ] Every decision traces to a What element that required it
- [ ] Every How element with no What anchor is **flagged as an undeclared product decision** and escalated before proceeding (Rule 5 surfaces a conversation; it does not silently block)

## Section 5 — SPMC

Every worker (every discrete LLM call) under the framework receives all four, none optional:

- [ ] **Schema** — output shape, derived from How interfaces/data model; non-conforming output is rejected
- [ ] Schema pins the **shape language** conformance is decided in; it is recorded alongside the schema
- [ ] **Prompt** — derived from What behaviors/criteria, filtered through How component responsibility
- [ ] **Model** — selected by the complexity *remaining* after the How collapses the decision space
- [ ] Model is pinned as a **binding**, not a name: served precision/quantization and invocation parameters are fixed and recorded, so a change under an unchanged name still counts as a Model-axis change
- [ ] **Context** — assembled from the How, **frozen and bounded** at execution; no mid-execution retrieval
- [ ] **Each axis is pinned to the precision at which it affects output** — no axis is specified by a label that two different behaviors could share (the precondition for attribution)
- [ ] SPMC axes are **independently attributable** so a quality failure points to which axis failed

## Section 6 — Scale discipline

- [ ] The framework applies the **same floor** to a single-page feature as to a large project (same structure, smaller content).
- [ ] A spec missing any required section, or containing placeholder content, is treated as a **draft** and does not proceed to the How layer.

## Section 7 — The seam (only if the framework hands work to an execution pillar)

The producing pillar owns the interface. If your framework emits frozen work-units to any executor:

- [ ] The framework **defines** the handoff artifact's shape (what the unit contains, how it is identified, what return event closes it) — it does not inherit that shape from a specific executor.
- [ ] The unit is **frozen and self-contained** at emit: no element requires a callback into the framework to resolve (mirrors the Execution Contract Input Contract).
- [ ] The interface is declared to **version independently** of the framework, so an executor swap requires no framework change and a framework swap requires no executor change.
- [ ] Any spec-side conformance gate the seam depends on (e.g. a homogeneity or resolution check) runs **before emit**, on the specification side.

---

## How to declare

Copy [`CONFORMANCE-TEMPLATE.md`](CONFORMANCE-TEMPLATE.md) into your framework's repo, check the boxes you satisfy, and cite where in your framework each requirement is met. Then list your framework in the [registry](../registry/).

Partial conformance is legitimate and useful — a framework may cover only the What layer, or only How. Declare exactly what you cover.
