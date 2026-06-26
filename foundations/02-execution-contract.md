# Execution Contract

> A definition of what an agent execution environment must declare and guarantee before autonomous work runs — who acts, where, with what permissions, and who validates the result.

---

## Where this document sits

Autonomous AI development has two foundations, not one. They are peers. Neither contains the other.

```
        PILLAR ONE                          PILLAR TWO
   (what goes into work)               (how work is executed)

┌──────────────────────────┐      ┌──────────────────────────┐
│   Actual implementations │      │   Actual implementations │
│   project specs, bundles │      │   running pipelines      │
└────────────┬─────────────┘      └────────────┬─────────────┘
             │ depends on                       │ depends on
             ▼                                  ▼
┌──────────────────────────┐      ┌──────────────────────────┐
│  Framework implementations│     │  Framework implementations│
│  e.g. Decision-Driven     │     │  e.g. Assembly Line       │
│  Design                   │     │  Protocol (ALP)           │
└────────────┬─────────────┘      └────────────┬─────────────┘
             │ depends on                       │ depends on
             ▼                                  ▼
┌──────────────────────────┐      ┌──────────────────────────┐
│  SPECIFICATION FRAMEWORK │      │   EXECUTION CONTRACT      │
│  What / How / SPMC       │      │   Workers, capabilities,  │
│  completeness criteria   │      │   environment, tools,     │
│                          │      │   credentials, verifying  │
│  Most stable             │      │   Most stable             │
│                          │      │   — this document         │
└──────────────────────────┘      └──────────────────────────┘
```

The Specification Framework answers: **what must a specification contain so that an LLM can produce correct output?** It governs the *input* to AI work.

This document — the Execution Contract — answers a different question: **what must an execution environment declare and guarantee so that an agent can act autonomously without exceeding its authority, and so that no output is accepted without validation?** It governs the *execution* of AI work.

The two are symmetric and complementary. A perfect specification fed into an uncontrolled environment produces output no one can trust. A perfectly controlled environment with no specification produces controlled nonsense. Autonomous development needs both pillars standing.

This document is the foundation of the second pillar. Framework implementations — like the Assembly Line Protocol — depend on it. Actual pipelines depend on a framework implementation. Stability flows downward; volatility is contained at the top.

---

## Premise: At high autonomy, the environment is the trust boundary

There is an autonomy ladder for AI-assisted development. Each rung removes a category of per-action human involvement.

```
Level 3 — Spec-driven development
          A human writes the specification; the agent executes against it.
          A human reviews the output before it is used.
          → Governed by the Specification Framework.

Level 4 — Supervised autonomy
          Agents execute multi-step pipelines. Humans review at gates,
          not at every action. Most actions complete without inspection.

Level 5 — Full autonomy
          Agents dispatch and orchestrate other agents. Human involvement
          is the exception, not the rule. The pipeline is the backstop.
```

At Level 3, a human inspects each unit of output before it is trusted. The human is the verification backstop, and the environment can be loose, because a person stands between the agent and any consequence.

At Levels 4 and 5, that is no longer true. **No human inspects each action before it happens.** Actions take effect — files are written, services are called, other agents are spawned — without anyone watching that specific action. The human reviews a verdict at a gate, or reviews nothing at all.

This changes what must carry the trust. If no human is watching the action, then the only thing standing between an agent and an unauthorised consequence is the environment itself. The environment must be constructed so that the agent **cannot** exceed its authority — not so that it is asked not to.

This is the load-bearing idea of this document:

> At Levels 4 and 5, the execution environment is the trust boundary. Everything an agent can do must be declared and bounded before execution begins. Nothing undeclared is permitted. Every output is validated before it is accepted. These are not features of a good pipeline — they are the conditions under which autonomy is safe at all.

A framework that does not declare its building blocks completely is not running at Level 4 or 5. It is running unsupervised, which is a different and more dangerous thing.

---

## Intellectual lineage: this is Lean, applied to agents

The problem this document addresses is not new. It is the problem every high-volume production line solved in the twentieth century: how do you run a line at high autonomy, with minimal per-action human inspection, without producing defects at scale?

The Toyota Production System answered it structurally — by building quality and authority into the line itself rather than inspecting them in afterward. The correspondences to autonomous agent execution are exact, not decorative:

- **Jidoka** (autonomation — "automation with a human touch"): a machine stops itself the instant it detects a defect, rather than producing scrap. This is the verification contract. No action is accepted without validation; a defective result halts the line rather than flowing downstream.

- **Andon** (the cord any worker can pull to stop the line and escalate): this is the transition contract and its gates. A verdict either advances the work or pulls the cord.

- **Standardized work**: every station has a defined, bounded procedure declared before it runs. This is the capability, tool, and credential declaration. A worker's permitted surface is specified in advance, never discovered at runtime.

- **Poka-yoke** (mistake-proofing): the line is built so the wrong action is *impossible*, not merely detected after the fact. This is the environment as trust boundary — least-privilege credentials and isolation mean the agent *cannot* exceed authority.

- **Muda** (elimination of waste): a worker is granted exactly the capability the task requires and no more. Excess capability is waste, and waste is risk.

Lean is the evidence that this works. Fifty years of production data show that high autonomy without defects is achieved by structural constraint, not by exhortation or after-the-fact inspection. This document applies that settled result to agent pipelines.

You do not need to know the Toyota Production System to use this document — just as you do not need to know Decision-Driven Design to write a specification. Lean is the *why it works*. The building-block requirements below are the *what you must declare*.

---

## The building blocks a framework must declare

A compliant execution framework must declare eight building blocks. Each declaration has a completeness requirement: the condition under which that declaration has done its job. A declaration is not complete because it has content. It is complete when it satisfies its requirement.

The eight fall into three groups:

- **The actors** — who acts, and who judges: Workers, Verification
- **The grants** — what a worker is permitted, and where: Capabilities, Environment, Tools, Credentials
- **The flows** — what comes in, what goes out, and how work moves: Input Contract, Output Contract, Transition Contract

---

### Workers

**Completeness requirement:** Every agent role that executes work in the framework is declared. For each worker it is unambiguous what it is responsible for, what it is permitted to do, and what it is not permitted to do. No flow, capability grant, or verification step references a worker that is not declared here.

A worker is a role, not a model. The same model may fill different worker roles in different stations, and each role carries its own bounded authority. A worker whose permissions are inherited from "whatever the agent can do" is not a declared worker — it is an unsupervised process.

---

### Capabilities

**Completeness requirement:** Every category of action a worker may take is declared as an explicit capability. The categories — at minimum **read**, **write**, **call**, and **spawn** — are each either granted to a worker or withheld from it. A worker holds exactly the capabilities its task requires and no others. No capability is implicit, and no action outside a declared capability is possible.

- **read** — the worker may observe declared inputs and state
- **write** — the worker may produce declared outputs and mutate declared state
- **call** — the worker may invoke declared tools or external services
- **spawn** — the worker may dispatch other workers

The four categories are the floor. A framework may declare finer-grained capabilities, but it may not collapse the floor — a worker that can write must say so, a worker that can spawn must say so. The capability surface is the structural expression of least privilege: it must rise no higher than the task demands. When a worker requires broad capability, that is a signal the work has not been decomposed far enough upstream.

---

### Environment

**Completeness requirement:** The execution boundary every worker operates within is declared, along with what the environment guarantees. It is unambiguous what a worker has access to, what it is structurally prevented from accessing, and what isolation properties hold. The environment guarantees are enforced by construction, not by instruction to the worker.

The environment is where the trust boundary lives. A compliant declaration states, at minimum: what filesystem the worker can reach, what network destinations are permitted, whether the worker can reach the host or other workers, and what is destroyed when the work unit ends. An environment that relies on the worker choosing not to access something it technically can access has not declared a boundary — it has declared a hope.

---

### Tools

**Completeness requirement:** Every tool a worker may invoke is declared, classified, and scoped. For each tool it is clear which workers may call it and under what conditions. A tool not declared here is not available to any worker. Each tool is classified by its relationship to the work unit:

- **Effect tools** — tools that produce side effects in the world (writing files, calling services, mutating external state). Effect tools are permitted during execution, at the points where the work unit is meant to take effect.
- **Knowledge tools** — tools that retrieve information into the work unit (lookups, searches, retrieval). Knowledge tools must not introduce live, unversioned information into a work unit mid-execution. Knowledge enters through the frozen input contract, with provenance, not through an uncontrolled call during execution.

The distinction matters because it preserves the property that a worker is a function of its declared inputs. An effect tool changes the world and is auditable as such. A knowledge tool that pulls live data mid-execution makes the worker's behaviour depend on something that was never declared and cannot be reproduced. Classify every tool; permit effect tools where they belong; keep knowledge acquisition at the input boundary.

---

### Credentials

**Completeness requirement:** How a worker is granted access to external systems is declared, and every grant is scoped to the work unit, not to the worker's identity. Credentials are short-lived, least-privilege, and revoked when the work unit ends. A worker never holds a standing or broad credential. It is unambiguous which credential a worker can obtain, for which service, at which scope, and for how long.

The principle is that the worker holds no real credential at all — it holds a reference, scoped to its current work unit, that the boundary exchanges for real access only for permitted destinations. The authority derives from the work the worker is doing, not from who or what the worker is. A framework that injects a standing credential into a worker has granted authority that outlives and exceeds the task, which is precisely what Level 4 and 5 autonomy cannot tolerate.

---

### Input Contract

**Completeness requirement:** What every worker receives as its input is declared, and that input is frozen and bounded at the moment execution begins. It is unambiguous what a worker is handed, where that input comes from, and that the worker's behaviour is a function of that input alone. Nothing the worker needs is acquired through an undeclared channel after execution starts.

This is the execution-side counterpart to the specification. The Specification Framework defines what a complete specification contains; the input contract defines that the worker receives a frozen, bounded version of it — that the bundle handed to the worker does not change underneath it, and does not contain references the worker must resolve through uncontrolled means. A worker operating on a live, mutable, or unbounded input is not reproducible and not auditable.

---

### Output Contract

**Completeness requirement:** What every worker produces is declared, along with where the output lands and how it becomes available to the next worker or to verification. The output has a declared shape and a declared destination. State passed between workers crosses this boundary explicitly — there is no hidden channel through which workers share state.

Output is the artifact that crosses the boundary between workers. It is the only legitimate way state moves from one work unit to the next. A framework where workers share state through some side channel — a mutable store no one declared, an environment they both happen to see — has an undeclared flow, which is the execution-side equivalent of an undeclared product decision. Everything that moves between workers moves through the declared output contract.

---

### Verification

**Completeness requirement:** Who validates each output is declared, along with the authority that verifier holds, the conditions under which validation occurs, and the form a verdict takes. No output is accepted without a verdict. It is unambiguous whether the verifier is a human, an automated check, or another agent, and what each kind of verdict permits or forbids downstream.

This is Jidoka. No action without validation. A worker's output is not trusted because the worker produced it — it is trusted because a declared verifier, with declared authority, produced a verdict accepting it. The verifier may be automated for some verdict classes and human for others; the framework must declare which. An output that flows downstream without a verdict has bypassed the only quality gate the line has.

A verdict is not a boolean buried in an exit code. It is a declared artifact with a declared vocabulary — at minimum, a clear distinction between *accepted*, *rejected*, and *escalate to human*. The verdict is what the next building block acts upon.

---

### Transition Contract

**Completeness requirement:** How a verdict becomes a consequence is declared. For every verdict a verifier can produce, it is unambiguous what happens next — advance, halt, retry, or escalate — and which of those consequences a worker or agent may trigger without human involvement. The autonomy level of the framework lives here: it is the declared set of verdict-to-consequence bindings that may proceed without a human.

This is the andon cord. A verdict with no declared consequence dangles exactly as a How element with no What anchor dangles — it is an unfinished decision. The transition contract binds every possible verdict to a defined outcome, and in doing so it *is* the framework's autonomy level: a framework where every non-accepted verdict escalates to a human is operating at Level 4; a framework where agents may advance work on a broader range of verdicts without human involvement is operating at Level 5. The autonomy level is not a setting — it is the shape of this contract.

---

## The Closure Contract

The eight building blocks form a closed system. The test of a compliant framework is closure: a unit of work can be traced end to end, and nothing dangles.

Trace a unit of work:

> A **worker** is dispatched into an **environment**, holding declared **capabilities**, able to invoke declared **tools** using work-unit-scoped **credentials**. It receives a frozen **input**, does its work, and produces a declared **output**. A declared **verifier** judges that output and issues a verdict. The **transition contract** binds that verdict to a consequence, which may dispatch the next worker.

Every reference resolves. Every grant traces to a need. Every output is verified. Every verdict has a consequence. This is the execution-side mirror of the Specification Framework's derivation contract, and it has the same five-rule shape:

1. Every capability a worker holds traces to a requirement of its task. A capability with no task that needs it is excess authority and must be withdrawn.
2. Every tool a worker can call is declared and classified as effect or knowledge. An undeclared tool is unreachable; a knowledge tool that fires mid-execution is a violation of the input contract.
3. Every credential a worker can obtain is scoped to the work unit and time-bounded. A standing or broad credential is flagged and must be replaced with a scoped grant.
4. Every output is judged by a declared verifier before it is accepted. An output that flows downstream without a verdict is flagged.
5. Every verdict a verifier can produce maps to a declared consequence in the transition contract. A verdict with no consequence is an unfinished decision and must be resolved before the framework runs autonomously.

Rule 1 does not block work — it surfaces a decomposition problem. A worker that needs broad capability is telling you the work was not constrained enough upstream. The same funnel principle that governs specification applies here: constraint density rises toward the action, and the capability required falls correspondingly.

---

## Completeness is not optional at autonomy scale

A framework may declare more than these eight blocks. It may add finer capability categories, richer verdict vocabularies, additional environment guarantees. It may not omit any of the eight.

The reason is the premise. Below this floor, the environment is no longer the trust boundary — and at Level 4 and 5 there is no other backstop. A framework missing a verification declaration accepts unvalidated output. A framework missing a capability declaration permits undeclared actions. A framework missing a credential scope grants authority that outlives the task. Each omission is not a missing feature; it is a point at which autonomy stops being safe.

A framework that declares all eight blocks completely can run autonomously because every action is bounded before it happens and every result is validated before it is accepted. A framework that does not is not running at a lower level of rigour — it is running unsupervised, which the autonomy ladder does not contain.

---

*This document defines the minimum a framework must declare to support autonomous agent execution at Levels 4 and 5. It is the foundation of the execution pillar, peer to the Specification Framework. Framework implementations — such as the Assembly Line Protocol — depend on it. No required building block may be omitted regardless of framework, tooling, or autonomy level, because the building blocks are the conditions under which autonomy is safe.*
