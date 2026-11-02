# Local Agentic Code Navigator (Powered by Gemma 4)

An edge-optimized Software Engineering (SWE) agent framework engineered for **The Gemma 4 Developer Agent Competition (Paper Track)**.

This repository demonstrates autonomous codebase inspection, isolated bug localisation, and self-validating patch synthesis using quantized Gemma 4 checkpoints running purely on local hardware.

---

## Architecture Overview

Current developer-agent implementations depend heavily on commercial frontier APIs with vast context allowances. This project investigates the efficiency ceiling of localized, token-bounded agent loops.
─────────────────────────┐
                │   Issue / Task Prompt   │
                └────────────┬────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ Gemma 4 ReAct Engine (Quantized / Edge-Optimized)           │
│                                                             │
│   [Thought] -> Reason through stack trace & directory tree  │
│   [Action]  -> Dispatch granular file / test tool calls     │
└──────────────┬───────────────────────────────▲──────────────┘
│                               │
▼                               │
┌─────────────────────────────┐                │
│ Tool Execution Sandbox      │                │
│  - Directory Scanners       │                │
│  - AST & Line-Range Slicers ├────────────────┘
│  - Target Patch Applier     │   Observation State
│  - Automated Test Runners   │
└─────────────────────────────┘


### Core Design Principles

1. **Context Economy:** Instead of ingesting full files, the agent queries specific line ranges and structural AST slices to protect the model's active context window.
2. **Deterministic Tool Schema:** Rigid JSON-based action invocation minimises token consumption during the ReAct reasoning step.
3. **Execution Guardrails:** Candidate code modifications are immediately validated against local test harnesses, generating immediate feedback for automated regression checks.

---

## Project Structure

```text
├── agent/
│   ├── __init__.py          # Module exports
│   ├── core.py             # Agent state machine and turn controller
│   ├── prompts.py          # Structured system instructions & tool signatures
│   └── tools.py            # Local file manipulators and execution subprocesses
├── benchmarks/
│   └── mock_swe_task.py    # Self-contained task verification scenario
├── run_agent.py            # CLI entry point to trigger the agent loop
├── requirements.txt        # Runtime dependencies
└── README.md               # Architecture documentation
