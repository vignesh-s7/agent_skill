# agent_skill

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

A lightweight utility collection and runtime toolchain bundling deterministic ML, constraint satisfaction, and abstract syntax tree (AST) code analysis capabilities for autonomous agent environments.

## Features

- **AST Code Analysis & Knowledge Graphs**: Integration helpers for tree-sitter based AST parsing and deterministic code structure analysis.
- **Operations Research & Scheduling**: Standard helpers for linear optimization and constraint solving powered by Google OR-Tools.
- **Embedded Neural Inference**: Portable cross-platform CPU runtime evaluation via Microsoft ONNX Runtime.
- **Pure Dependency Isolation**: Packaged for continuous integration (CI) workflows, reproducible testing, and containerized evaluation.

## Installation

```bash
pip install agent_skill
```

Or install specific optional providers:

```bash
pip install "agent_skill[all]"
```

## Quick Start

```python
import agent_skill

# Inspect available deterministic capability modules
print(agent_skill.available_capabilities())
```

## Third-Party Notices & Licenses

This project bundles and interfaces with several industry-standard open-source libraries:
- **Google OR-Tools**: Licensed under the Apache License, Version 2.0. Copyright Google LLC.
- **Microsoft ONNX Runtime**: Licensed under the MIT License. Copyright Microsoft Corporation.
- **Graphify / Tree-Sitter**: Licensed under the MIT License.

Detailed attributions, licenses, and notices are documented in [NOTICE](NOTICE) and [LICENSE](LICENSE).

## Contributing

Contributions are welcome under the Apache-2.0 license. Please submit issues or pull requests to the repository.

## License

Distributed under the Apache 2.0 License. See [LICENSE](LICENSE) for more information.
