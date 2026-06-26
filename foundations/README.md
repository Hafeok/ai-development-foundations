# Foundations

The normative core of AI Development Foundations. These three documents are the **most stable layer** — everything in any conforming framework or project traces back to them. They are technology-neutral and tool-agnostic by design.

Read in this order:

1. **[The Two Pillars](00-two-pillars.md)** — the bridge. How the two pillars relate, why they are independent, and how they map to the autonomy ladder. Start here.
2. **[Specification Framework](01-specification-framework.md)** — Pillar One. What any specification must contain (What / How / SPMC) for an LLM to produce correct, complete, verifiable output. Governed by the **derivation contract**.
3. **[Execution Contract](02-execution-contract.md)** — Pillar Two. What any execution environment must declare and guarantee (eight building blocks) for an agent to act autonomously without exceeding its authority. Governed by the **closure contract**.

## Status

These documents are **normative**. A framework that claims to build on a pillar must satisfy every completeness requirement in that pillar's foundation. The [conformance checklists](../conformance/) restate those requirements as a checkable list.

## Changing these documents

Changes go through the [RFC process](../rfcs/). The stability discipline is the whole point: a framework can evolve its format without disturbing the foundation beneath it, and a project can switch frameworks entirely without either foundation changing. Volatility is contained upward, never pushed down.

## License

These documents are licensed [CC BY 4.0](../LICENSE-DOCS). You may build on, adapt, and redistribute them with attribution.
