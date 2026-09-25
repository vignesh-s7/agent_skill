# Enterprise Security & Compliance Policy

`agent_skill` is engineered specifically for secure, auditable enterprise environments.

## Security Guarantees

1. **Zero Shell Scripts (`NO_SHELL_SCRIPTS`)**:
   - The repository contains **zero** `.sh`, `.bash`, `.cmd`, or `.bat` execution files.
   - Prevents automated enterprise security scanners (Prisma Cloud, Checkmarx, Snyk, Veracode) from flagging arbitrary shell execution or script injection attack vectors.
2. **Pure Declarative Configurations**:
   - Environment and tooling configurations are distributed strictly as declarative JSON and TOML files (`.settings`, `.json`, `pyproject.toml`).
   - Declarative data can be statically validated against schemas without code execution risks.
3. **Pure Auditable Python Stdlib**:
   - Core configuration and inspection routines use standard Python 3.10+ stdlib only (`json`, `pathlib`, `shutil`).
   - Every routine is fully inspectable via AST and safe for restricted environments.
4. **Third-Party Dependency Boundary**:
   - Zero required runtime pip dependencies for base operation.
   - Optional acceleration providers (`ortools`, `onnxruntime`, `tree-sitter`) are explicitly isolated under `[project.optional-dependencies]`.

## Vulnerability Reporting

If you discover a security issue or vulnerability, please report it responsibly by opening a private security advisory on GitHub or contacting the maintainers directly.
