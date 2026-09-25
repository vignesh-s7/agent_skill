# agent_skill

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![Enterprise Ready](https://img.shields.io/badge/Enterprise-Zero_Shell_Scripts-green.svg)](SECURITY.md)

A lightweight utility collection and runtime toolchain bundling deterministic ML, constraint satisfaction, open-source agent runners, stream compaction, and abstract syntax tree (AST) code analysis capabilities for autonomous agent environments.

## Features

- **Input Interception & Output Compaction (RTK)**: Intercepts verbose shell command outputs (e.g., git logs, build traces, test outputs), collapses streams down to essential errors and summaries, and constraints model generation with terse registers to save tokens on return trips.
- **Minimum-Build Ladder (Ponytail)**: Automated B.U.I.L.D scoring evaluator (Borrow, Upgrade, Innovate, Later, Drop) enforcing pre-build reuse discipline.
- **AST Code Analysis & Knowledge Graphs (Graphify)**: Integration helpers for tree-sitter and Python AST parsing with deterministic structure graphs.
- **Agent Reasoning & Candidate Prototyping (Hermes)**: Pure Python candidate adapter powered by NousResearch Hermes Agent patterns.
- **Workflow & Graph Execution (LangChain)**: Adapter helpers for LangChain and LangGraph stateful runtimes.
- **Declarative Assistant Skills**: Pre-packaged, zero-shell prompt configurations (`caveman`, `ui-ux-pro-max`, `ponytail`, `rtk`) in `dotfiles/skills/`.
- **Operations Research & Scheduling**: Standard helpers for linear optimization and constraint solving powered by Google OR-Tools.
- **Embedded Neural Inference**: Portable cross-platform CPU runtime evaluation via Microsoft ONNX Runtime.
- **Enterprise-Grade Declarative Settings**: Zero shell scripts (`.sh`). Environment dotfiles and MCP connections are configured purely via declarative JSON and standard Python.
- **Pure Dependency Isolation**: Packaged for continuous integration (CI) workflows, reproducible testing, and containerized evaluation.

## Installation

```bash
pip install agent_skill
```

Or install specific optional providers:

```bash
pip install "agent_skill[all]"
# Or specific feature sets:
pip install "agent_skill[hermes]"
pip install "agent_skill[langchain]"
```

## Quick Start

### 1. Inspect Engine Capabilities
```python
import agent_skill

# Inspect available deterministic capability modules
print(agent_skill.available_capabilities())
```

### 2. Stream & Shell Output Compaction (RTK)
```python
from agent_skill import compact_shell_output

raw_git_log = "..." # Long verbose terminal stream
compacted = compact_shell_output(raw_git_log, max_lines=20)
print(compacted["compacted_text"])
print("Reduction ratio:", compacted["reduction_ratio"])
```

### 3. Pre-Build Clearance Scoring (Ponytail)
```python
from agent_skill import score_build

# Score proposal: value (1-5), effort (1-5)
score = score_build(value=5, effort=1)
print(f"Action: {score['action']} | Proceed: {score['proceed']}")
# -> Action: BORROW | Proceed: True
```

### 4. AST Structure Analysis (Graphify)
```python
from agent_skill import analyze_code_structure

ast_graph = analyze_code_structure("class Engine:\n    def run(self): pass")
print("Classes:", ast_graph["classes"])
print("Functions:", ast_graph["functions"])
```

### 5. Candidate Reasoning (Hermes)
```python
from agent_skill import run_hermes_candidate

result = run_hermes_candidate("Analyze algorithmic complexity of quicksort")
print("Status:", result["status"])
print("Receipt:", result["receipt"])
```

### 6. Configure Enterprise Environment (Zero Shell Scripts)
To automatically configure standard declarative MCP and assistant settings (`~/.gemini/config/mcp_config.json`, `~/.claude/settings.json`) in pure Python:

```bash
python3 -m agent_skill.configure
# Or if installed via pip:
# agent-skill-setup
```

## Enterprise Security & Declarative Settings

This package complies with strict corporate security policies:
- **No Arbitrary Shell Scripts**: Zero `.sh`, `.bash`, or untrusted command scripts that trigger enterprise firewall or SecOps warnings.
- **Declarative Settings**: Pre-packaged templates in `dotfiles/` for Model Context Protocol (MCP) and agentic toolchains.
- **Auditable Pure Python**: All setup and inspection routines are written in auditable Python standard library. See [SECURITY.md](SECURITY.md) for full compliance details.

## Third-Party Notices & Licenses

This project bundles and interfaces with several industry-standard open-source libraries:
- **RTK (RunTime Kit)**: Licensed under the MIT License.
- **Dietrich Gebert Ponytail**: Licensed under the MIT License.
- **Graphify / Tree-Sitter**: Licensed under the MIT License.
- **NousResearch Hermes Agent**: Licensed under the MIT License.
- **Julius Brussee Caveman**: Licensed under the MIT License.
- **LangChain**: Licensed under the MIT License.
- **UI/UX Pro Max**: Licensed under the MIT License.
- **Google OR-Tools**: Licensed under the Apache License, Version 2.0. Copyright Google LLC.
- **Microsoft ONNX Runtime**: Licensed under the MIT License. Copyright Microsoft Corporation.

Detailed attributions, licenses, and notices are documented in [NOTICE](NOTICE) and [LICENSE](LICENSE).

## Contributing

Contributions are welcome under the Apache-2.0 license. Please submit issues or pull requests to the repository.

## License

Distributed under the Apache 2.0 License. See [LICENSE](LICENSE) for more information.
