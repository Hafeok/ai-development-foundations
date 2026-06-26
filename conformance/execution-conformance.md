# Execution Contract — Conformance Checklist

A framework conforms to **Pillar Two** when it declares all eight building blocks completely and satisfies the closure contract. The framework may add finer categories, richer verdict vocabularies, or extra guarantees — it **may not omit any of the eight**, because each omission is a point at which autonomy stops being safe.

A conformance claim is an assertion that **a pipeline running under your framework cannot execute at Level 4/5 with any building block undeclared.**

> Source of truth: [`foundations/02-execution-contract.md`](../foundations/02-execution-contract.md). Where this checklist and the foundation differ, the foundation governs.

---

## Section 0 — Premise

- [ ] The framework treats the **environment as the trust boundary** at Levels 4–5: an agent *cannot* exceed its authority, rather than being asked not to.
- [ ] Everything an agent can do is **declared and bounded before execution begins**; nothing undeclared is permitted.

## The actors

### Workers
- [ ] Every agent role that executes work is declared.
- [ ] For each worker, what it is responsible for / permitted / **not** permitted is unambiguous.
- [ ] A worker is a **role, not a model**; permissions are not inherited from "whatever the agent can do."
- [ ] No flow, grant, or verification step references an undeclared worker.

### Verification
- [ ] Who validates each output is declared, with the verifier's authority, conditions, and verdict form.
- [ ] **No output is accepted without a verdict** (Jidoka).
- [ ] It is unambiguous whether each verifier is human, automated, or another agent.
- [ ] A verdict is a **declared artifact with a declared vocabulary** — at minimum *accepted* / *rejected* / *escalate to human* — not a boolean in an exit code.

## The grants

### Capabilities
- [ ] Every category of action is an explicit capability; floor is **read / write / call / spawn**.
- [ ] Each is explicitly granted or withheld per worker; nothing implicit.
- [ ] A worker holds exactly the capabilities its task requires and no more (the floor may be refined, not collapsed).

### Environment
- [ ] The execution boundary and its guarantees are declared: filesystem reach, permitted network destinations, host/peer reachability, what is destroyed when the unit ends.
- [ ] Guarantees are **enforced by construction, not by instruction** to the worker.

### Tools
- [ ] Every invokable tool is declared, scoped to workers/conditions; an undeclared tool is unreachable.
- [ ] Each tool is classified **effect** (side effects, permitted at the take-effect points) or **knowledge** (retrieval).
- [ ] **Knowledge tools do not introduce live, unversioned data mid-execution** — knowledge enters through the frozen input contract with provenance.

### Credentials
- [ ] Every grant is **scoped to the work unit**, short-lived, least-privilege, revoked when the unit ends.
- [ ] A worker holds a **reference** the boundary exchanges for real access, never a standing or broad credential.
- [ ] Which credential / which service / which scope / how long is unambiguous.

## The flows

### Input Contract
- [ ] Each worker's input is declared, **frozen and bounded at execution start**.
- [ ] The worker's behavior is a function of that input alone; nothing needed is acquired through an undeclared channel afterward.

### Output Contract
- [ ] What each worker produces, where it lands, and how it reaches the next worker/verifier is declared.
- [ ] State crosses between workers **only** through the declared output — no hidden side channel.

### Transition Contract
- [ ] For **every** verdict a verifier can produce, the consequence (advance / halt / retry / escalate) is declared.
- [ ] It is declared which consequences may fire **without human involvement** — this set *is* the framework's autonomy level.

## The closure contract

The framework's five-rule mirror of the derivation contract holds:

- [ ] Every capability traces to a task requirement; excess authority is withdrawn (Rule 1 surfaces a decomposition problem, it does not block).
- [ ] Every tool is declared and classified; a mid-execution knowledge tool is a violation.
- [ ] Every credential is work-unit-scoped and time-bounded; standing/broad credentials are flagged.
- [ ] Every output is judged by a declared verifier before acceptance.
- [ ] Every verdict maps to a declared consequence; a dangling verdict is an unfinished decision.

## The seam (only if the framework consumes work from a specification pillar)

The producing pillar owns the interface; an execution framework is a **conforming consumer**, not a co-author of it. If your framework receives frozen work-units:

- [ ] The framework **conforms to** the handoff artifact's shape as defined by the producing side — it does not require the producer to adopt an executor-specific format.
- [ ] The framework resolves **nothing by calling back** into the specification side mid-execution; the received unit is sufficient (this is the Input Contract).
- [ ] The framework's return path is a **declared verdict event** that is self-describing — reconcilable by a consumer that never observed the dispatch.
- [ ] The framework imposes no change on the producer when its own hardware or scheduler changes (the seam versions independently of the executor).

---

## How to declare

Copy [`CONFORMANCE-TEMPLATE.md`](CONFORMANCE-TEMPLATE.md) into your framework's repo, check the boxes you satisfy, and cite where each building block is declared in your framework. Then list your framework in the [registry](../registry/).

State your **autonomy level** explicitly — it follows directly from the shape of your transition contract.
