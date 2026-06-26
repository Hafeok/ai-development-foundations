# Specification Framework

> A definition of what a specification is, what it must contain, and how the What, How, and SPMC layers form a complete chain from customer intent to LLM execution.

---

---

## Where this document sits

Spec-driven development has three layers. Each layer depends on the one below it. The lower the layer, the more stable it is.

```
┌─────────────────────────────────────────────────────────┐
│              ACTUAL IMPLEMENTATIONS                     │
│                                                         │
│  Project A, Project B, Product X                        │
│  Concrete specs, SPMC bundles, generated artifacts      │
│                                                         │
│  Most volatile — changes with every project             │
└────────────────────────┬────────────────────────────────┘
                         │ depends on
                         ▼
┌─────────────────────────────────────────────────────────┐
│            FRAMEWORK IMPLEMENTATIONS                    │
│                                                         │
│  Decision-Driven Design, or any methodology that        │
│  implements the spec framework pattern                  │
│                                                         │
│  Moderately stable — evolves but does not change daily  │
└────────────────────────┬────────────────────────────────┘
                         │ depends on
                         ▼
┌─────────────────────────────────────────────────────────┐
│           SPECIFICATION FRAMEWORK DEFINITION            │
│                                                         │
│  What / How / SPMC — the universal pattern              │
│  Completeness criteria. Derivation contract.            │
│                                                         │
│  Most stable — this document                            │
└─────────────────────────────────────────────────────────┘
```

This document is the foundation layer. It defines the standard every framework implementation must satisfy and every actual implementation must trace back to. It does not prescribe tooling, methodology, or format. It defines the minimum that any approach must meet to support LLM-assisted development correctly.

Framework implementations — like Decision-Driven Design — depend on this document. They define how to satisfy its requirements in a specific, opinionated way. Actual project implementations depend on a framework implementation. They never depend on this document directly — they inherit its requirements through the framework they have adopted.

This means the document changes rarely. When a framework implementation evolves, this document does not need to change. When a project changes scope, neither this document nor the framework implementation needs to change. Stability flows downward. Volatility is contained at the top.

---

## Your path to spec-driven development

This document is the entry point. The path from here to a working spec-driven practice follows three steps, in order.

```
START HERE — read this document
Read the Specification Framework Definition.
Understand What, How, and SPMC.
Understand what completeness means and why it matters.
Understand the derivation contract.
     │
     ▼
CHOOSE A FRAMEWORK IMPLEMENTATION
Find a framework that covers both What and How —
or find one for the What layer and one for the How layer —
or author your own against the completeness criteria.
The framework is your methodology. It tells you how to
produce specs that meet the standard.
     │
     ▼
FIND THE TOOLING FOR THAT FRAMEWORK
Find the implementation tools that support your chosen
framework — scaffolds, CLI tools, templates, PR enforcement.
The tooling operationalises the methodology.
     │
     ▼
YOU ARE READY FOR SPEC-DRIVEN DEVELOPMENT
```

No step can be skipped. Tooling without a framework produces scaffolds with no grounding. A framework without this foundation produces methodology that cannot explain why its requirements exist. This document is why.

## Premise: Specs are LLM input artifacts

A specification is not documentation written after the fact. It is not a narrative for a human reader to interpret loosely. It is a **structured artifact that an LLM will consume to produce correct, complete, verifiable output**.

This distinction changes everything about what a spec must be.

When a human reads an ambiguous requirement, they fill the gaps with judgment, experience, and informal conversation. An LLM fills the same gaps with probability — drawing on its training distribution, not your system's context, your customer's intent, or your team's tacit knowledge. The output will be confident and coherent. It may also be completely wrong in ways that are invisible until late.

**The spec is the only channel through which your intent reaches the model.** What is not in the spec does not exist for the model. What is ambiguous in the spec will be resolved by the model in a way you did not specify. What contradicts itself in the spec will produce output that appears to satisfy one side while silently violating the other.

This means a spec must be:

- **Unambiguous** — every term defined, every condition explicit, no decisions left to inference
- **Complete at its boundary** — no required input to the next stage is missing
- **Internally consistent** — no contradictions; if two requirements conflict, the conflict is resolved in the spec, not by the model
- **Machine-readable** — structured, not free-form prose the model must interpret
- **Explicitly bounded** — what is out of scope is declared, not assumed

A spec that fails any of these properties is not a spec. It is a prompt for the model to make undeclared product decisions on your behalf.

---

## Two Layers

Every system has three distinct specification concerns. They require different knowledge, different conversations, and different authors. They must not be collapsed.

```
┌─────────────────────────────────────────────────────────┐
│                    WHAT SPECIFICATION                   │
│                                                         │
│  What the system does. For whom. Under what conditions. │
│  What success looks like. What is out of scope.         │
│                                                         │
│  Owner: Customer + Product                              │
│  Validator: Customer signs off                          │
└────────────────────────┬────────────────────────────────┘
                         │
                         │  shapes and constrains
                         │  (every How element must
                         │   trace to a What element)
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    HOW SPECIFICATION                    │
│                                                         │
│  How the system is built. Components. Data model.       │
│  Integrations. Decisions. Constraints.                  │
│                                                         │
│  Owner: Development Team                                │
│  Validator: Senior Developer / Architect reviews        │
└────────────────────────┬────────────────────────────────┘
                         │
                         │  decomposes into
                         │  (one SPMC bundle per
                         │   discrete work unit)
                         ▼
┌─────────────────────────────────────────────────────────┐
│                        S P M C                          │
│                                                         │
│  Schema   — the shape output must conform to            │
│  Prompt   — derived from behaviors and criteria         │
│  Model    — capability required by remaining complexity │
│  Context  — the information the model is given          │
│                                                         │
│  Owner: Development Team                                │
│  Validator: Output verified against Schema              │
└────────────────────────┬────────────────────────────────┘
                         │
                         │  consumed by
                         ▼
                    LLM execution
```

The arrows are not cosmetic. **The What shapes the How. The How decomposes into SPMC. Nothing at a lower layer exists independently of the layer above it.**

Any How element without a corresponding What element is an undeclared product decision — made silently, inside an implementation decision, invisible to the customer and unreviewed by product. This is where most tribal knowledge lives.

Any SPMC bundle without a corresponding How element is an undeclared technical decision — a worker operating without grounded constraints, free to fill gaps with model judgment rather than specified intent.

---

## The What Specification

The What Specification defines what the system does from the outside. A customer with no technical knowledge should be able to read it and confirm or reject it. A developer with no business knowledge should be able to read it and know exactly what they are building — without asking questions.

Each section below states what is required for that section to be considered complete. A section is not complete because it has content. It is complete when it satisfies its requirement.

---

### Identity

**Completeness requirement:** The system has a single, unique name that is used consistently across all downstream artifacts. No two systems share a name. No artifact refers to this system by any other label.

The name is the anchor all other artifacts point to. Ambiguity here propagates into every downstream reference.

---

### Purpose

**Completeness requirement:** Any person — technical or non-technical — can read this section and answer three questions without consulting any other document: What problem does this system solve? Who has that problem? Why does a system need to exist to solve it?

If the answer to any of those three questions requires inference or prior knowledge, the section is incomplete.

---

### Actors

**Completeness requirement:** Every person, role, or external system that interacts with this system is named and described. For each actor, it is unambiguous what they are permitted to do and what they are not permitted to do. No behavior elsewhere in the spec introduces an actor not declared here.

An actor appearing in a behavior without being declared here is an undeclared stakeholder. The model cannot resolve their permissions or constraints.

---

### Behaviors

**Completeness requirement:** Every distinct thing the system does is listed. For each behavior: it is clear which actor initiates it, what must be true before it can occur, what is guaranteed to be true after it completes, and what happens when it cannot complete normally. No behavior is described only by its happy path.

The unhappy path is not optional. It is half the behavior. A behavior with no exception condition tells the model it never fails — which is never true.

---

### Boundaries

**Completeness requirement:** There is an explicit list of what this system is responsible for and an explicit list of what it is not. Both lists are present. The out-of-scope list is not empty.

An empty out-of-scope list is a signal that boundaries have not been thought through, not that the system has no boundaries. The model uses the out-of-scope list to decline implementing things the customer did not ask for. Without it, scope expands to fill whatever the model considers reasonable.

---

### Data

**Completeness requirement:** Every piece of information the system creates, reads, updates, or deletes is named and described. For each data entity it is clear who owns it, what it represents, and when it ceases to exist. No behavior references data that is not declared here.

Data that appears in a behavior but not in this section is undeclared state. The model will invent a representation for it.

---

### Constraints

**Completeness requirement:** Every rule the system must obey that is not derivable from the behaviors is declared. Each constraint states what it requires, where it comes from, and how you would confirm it is satisfied. A constraint that cannot be verified is not a constraint — it is a wish.

Constraints include but are not limited to: regulatory requirements, security rules, performance thresholds, business policies, and integration mandates from external systems.

---

### Acceptance Criteria

**Completeness requirement:** For every behavior declared in the spec, there is at least one criterion that states the specific, testable condition under which that behavior is considered correctly implemented. Each criterion references the behavior it validates. A criterion that cannot be tested is not a criterion.

Acceptance criteria are the customer's sign-off surface. They are what the customer is agreeing to when they approve the What Spec. Vague criteria produce disputes at delivery.

---

### Open Questions

**Completeness requirement:** Every known unknown is listed. Each open question names what needs to be resolved, who is responsible for resolving it, and which behaviors or constraints it blocks. An empty list is acceptable only when all prior sections are demonstrably complete.

An empty open questions list on a first draft is a warning sign. It means either the spec is unusually complete or open questions are being treated as implementation details. The model cannot distinguish between these cases.

---

## The How Specification

The How Specification defines how the system is built. It is authored by the development team, derived from the What Specification, and consumed by the LLM to produce code. It does not restate the What. It resolves the What into technical decisions.

Every section in the How must be traceable to the What. If a How element has no What anchor, it is an undeclared product decision embedded in a technical artifact — and it must be surfaced and resolved, not silently carried forward.

---

### What Reference

**Completeness requirement:** The identity and version of the What Specification this How Spec is derived from is stated. A How Spec with no What reference is an implementation document in search of requirements. It cannot be reviewed against customer intent and it cannot be audited when output is incorrect.

---

### Components

**Completeness requirement:** The system is decomposed into discrete units, each with a single stated responsibility. For each component it is clear what it is solely responsible for, which behaviors or data from the What Spec it serves, what it depends on, and how other components interact with it. No component's responsibility requires "and" — if it does, it must be split.

The dependency structure between components must be directed and acyclic. A cycle is an unresolved design decision, not a valid architecture.

---

### Data Model

**Completeness requirement:** Every data entity declared in the What Spec has a corresponding technical representation here. For each entity it is clear where and how it is stored, what its schema is, and how schema changes are managed. No data model entry exists without a corresponding What Spec data entity.

A data model entry with no What Spec counterpart is an undeclared data concern. It means the system stores or manages something the customer did not know about and did not approve.

---

### Integrations

**Completeness requirement:** Every external system this system communicates with is declared. For each integration it is clear which direction data flows, what protocol is used, what the contract at the boundary is, and what this system does when the integration is unavailable. An integration without a defined failure behavior is incomplete.

---

### Decisions

**Completeness requirement:** Every architectural or design choice that cannot be directly derived from the What Spec is documented. For each decision it is clear what question was being resolved, what was decided, why that choice was made over the alternatives, what alternatives were considered and rejected, and which What Spec element drove the need for this decision.

A decision without documented rationale gives the model no basis for making consistent implementation choices within its intent. The model will fill the reasoning gap with its own judgment.

---

### Error Handling

**Completeness requirement:** The system's overall approach to errors is stated. Every category of error the system can encounter has a declared behavior. It is clear what is logged, at what level, and what conditions trigger external alerts. No error category is left to implementation judgment.

---

### Non-Functional Requirements

**Completeness requirement:** Every constraint declared in the What Spec has a corresponding technical implementation stated here. For each non-functional requirement the threshold is specific and measurable — not "fast" but "p95 response time under 200ms at 100 concurrent users." A threshold that cannot be tested against is not a requirement.

No constraint from the What Spec may be absent here. A constraint with no implementation plan is a promise the system cannot verify it keeps.

---

### Open Questions

**Completeness requirement:** Same standard as the What Spec. Every technical unknown that must be resolved before implementation can begin is listed. Any unresolved open question from the What Spec is propagated here with the same structure until it is resolved.

---

## The Derivation Contract

The relationship between What and How is a derivation constraint, not just a sequence. The What does not inform the How — it constrains it. Every How element is either derived from a What element or it is an undeclared decision that must be made explicit.

This is the audit surface. When an LLM produces incorrect output, the first question is: was the spec complete enough for this decision to have been made correctly? The derivation trace answers that question. Without it, a wrong output cannot be diagnosed — you cannot separate "the spec was wrong" from "the model failed on a complete spec."

### The five derivation rules

1. Every component traces to at least one behavior or data entity in the What Spec.
2. Every data model entry maps to a What Spec data entity.
3. Every non-functional requirement maps to a What Spec constraint.
4. Every decision traces to a What Spec element that required it.
5. Any How element with no What anchor is flagged as an undeclared product decision and requires explicit escalation before proceeding.

Rule 5 does not block work. It surfaces a conversation. Sometimes the right answer is "this is a pure technical decision with no product dimension" — and that is valid, but it must be declared, not assumed.

---

## SPMC: From Specification to Execution

The How Specification defines what must be built. SPMC defines how a discrete unit of that work is handed to a model for execution. Every worker — every discrete LLM call — requires all four elements. None is optional.

**Schema** defines the shape the output must conform to, together with the **shape language** that shape is expressed in — the formalism in which conformance is decided (for example a schema-validation language, a type declaration, or a constraint language). "Conform" is undefined without it: the same intent expressed in two different shape languages admits and rejects different output. Schema is derived from the component interface declarations and data model in the How Spec. The model is not asked to decide what form its output takes — that decision was made upstream and encoded in the schema. Output that does not conform to the schema is rejected regardless of how coherent it appears.

**Prompt** is the instruction surface. It is derived directly from the behaviors and acceptance criteria in the What Spec, filtered through the component responsibility in the How Spec. The prompt does not restate the full spec — it states exactly what this worker is responsible for producing, bounded by the decisions already made upstream. A prompt that asks the model to make decisions that should have been made in the How Spec is an incomplete How Spec, not a prompt problem.

**Model** is selected based on the complexity that remains after the How Spec has collapsed the decision space. A complete, well-scoped How Spec with fine-grained component decomposition leaves a worker with a narrow, well-bounded task — which requires less model capability. When a worker requires a large, expensive model, the signal is that the How Spec has not decomposed far enough. Capability requirement is a consequence of spec completeness, not a fixed property of the task.

A model *name* is not a complete specification of this axis. What is pinned is the **binding**: every property of the served model and its invocation that affects output. This includes the model's identity (provider/endpoint, version or revision, and the precision the weights are served at — two endpoints carrying the same model name but serving different quantizations are different bindings and not interchangeable) and the invocation parameters it is called with (such as temperature, top-p, output limits, and seed where honored). The binding, not the name, is what is recorded for attribution; a change of binding under an unchanged name is still a Model-axis change and resets the quality baseline accordingly.

**Context** is the information the model is given to execute the prompt against the schema. It is assembled from the How Spec: the relevant component's dependencies, the data model entries it operates on, the decisions that constrain its behavior, the integration contracts it must respect. Context is bounded and frozen at the moment of execution. The model does not retrieve additional information mid-execution — everything it needs is in the bundle.

### Each axis is pinned to the precision at which it affects output

An axis is completely specified only when everything that changes the output is fixed. A label that does not determine the output is not a specification of the axis — it is a pointer to a family of possible behaviors, and the model will land on one of them in a way the spec did not choose.

This is why naming is not enough on any axis. A schema without its shape language does not decide conformance. A model name without its served precision and invocation parameters does not decide what is generated. The test for each axis is the same: *if two things can carry this same label and produce different output, the label is not yet a binding, and the axis is underspecified.* Pin to the level at which output stops varying.

The same test makes the diagnostic below trustworthy. SPMC attribution can only assign a quality change to one axis if each axis was pinned tightly enough that an unrecorded change could not have caused the shift. An axis specified by a loose label is a confound: when output changes, you cannot tell whether the axis changed underneath the label or another axis is at fault. Precision on every axis is the precondition for the attribution that follows.

### SPMC as a quality diagnostic

The four elements are independently versioned and independently attributable. When output quality drops, SPMC identifies which axis failed:

- Wrong output shape → Schema was underspecified
- Wrong behavior → Prompt did not accurately reflect the What Spec
- Inconsistent reasoning → Model capability was insufficient for remaining complexity
- Missing information → Context bundle was incomplete

Without SPMC attribution, a quality failure produces a single question: "why did the model get this wrong?" With SPMC attribution, it produces four specific, auditable questions — each with a clear owner and a clear fix.

### SPMC is not DDD

SPMC is a universal pattern for structuring LLM execution. Decision-Driven Design is one framework that implements it — using feature specs as the What layer, ADRs as the How layer's decision artifact, and prepared bundles as the SPMC assembly mechanism. But any team using this specification framework can apply SPMC directly, regardless of whether they adopt DDD, without adopting any additional tooling or methodology.

The specification framework produces the inputs SPMC requires. SPMC produces the execution unit the model consumes. The chain is complete.

---

## Working with Customers

The What Specification is a shared artifact. You author it collaboratively with the customer. They own its correctness. You own its completeness.

This reframes the discovery conversation:

> "Our first phase is to write the What Specification together. It defines what the system does — completely, from your perspective. We do not start building until you have read it and confirmed it is correct. Once you sign off, we write the How Specification — that is our domain, and you do not need to review it. But everything we build will be traceable to what you approved."

This gives the customer a clear contract: they are responsible for the What being correct; you are responsible for the How being derived from the What. Disagreements about the outcome are resolved by reading the What Spec, not by renegotiating scope in production.

When gathering inputs for the What Spec, the conversation follows the section order:

- Start with **Purpose** — get the problem statement in one sentence before anything else
- Establish **Actors** — who uses this, in what roles, what are they allowed to do
- Walk through **Behaviors** — what happens step by step, including every unhappy path
- Set **Boundaries** — explicitly ask what this system is not responsible for
- Surface **Constraints** — regulatory, security, performance, business rules
- Agree on **Acceptance Criteria** — how will you know it is done and correct
- Close by listing every **Open Question** before leaving the room

The open questions list is the most important output of a discovery session. Leaving a session with an empty open questions list on a first draft means questions are being suppressed, not that none exist.

---

## Completeness is not optional at project scale

Not every project has the same scope. The section requirements above are the floor. A smaller project does not get a smaller floor — it gets the same floor with smaller content.

A single-page feature still requires a stated purpose, declared actors, explicit behaviors with unhappy paths, a data section, an out-of-scope declaration, and at least one testable acceptance criterion per behavior.

The discipline scales down. The structure does not.

A spec with any required section absent or containing placeholder content is a draft. Drafts do not proceed to the How layer. How Specs derived from drafts produce implementations that cannot be audited, cannot be traced to customer intent, and cannot be diagnosed when they fail.

---

*This document defines the minimum requirements for specifications used in LLM-assisted development. The three-layer stack — What, How, SPMC — is the universal pattern. Teams may extend any layer with additional sections. No required section may be omitted regardless of project size, customer preference, or implementation framework.*
