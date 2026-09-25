"""agent_skill.graphify_adapter - AST code analysis and deterministic structure graphs.

Origin: https://github.com/Graphify-Labs/graphify
License: MIT License

Features:
- Extracts function, class, and import dependencies from code.
- Generates deterministic graph representations with SHA-256 integrity digest.
- Pure Python standard library fallback (ast module) when graphify is uninstalled.
"""

from __future__ import annotations

import ast
import hashlib
from typing import Any, Dict, List, Set


def analyze_code_structure(code_content: str, filename: str = "source.py") -> Dict[str, Any]:
    """Parse code into deterministic AST summary graph containing classes, functions, and imports."""
    if not code_content or not isinstance(code_content, str):
        return {
            "status": "EMPTY",
            "classes": [],
            "functions": [],
            "imports": [],
            "receipt": hashlib.sha256(b"").hexdigest(),
        }

    code_hash = hashlib.sha256(code_content.encode("utf-8")).hexdigest()

    try:
        tree = ast.parse(code_content, filename=filename)
        classes: List[str] = []
        functions: List[str] = []
        imports: List[str] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(node.name)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                for alias in node.names:
                    imports.append(f"{mod}.{alias.name}")

        classes.sort()
        functions.sort()
        imports = sorted(list(set(imports)))

        receipt = hashlib.sha256(f"ast-graph:{code_hash}:{len(classes)}:{len(functions)}".encode("utf-8")).hexdigest()

        return {
            "status": "COMPLETED",
            "classes": classes,
            "functions": functions,
            "imports": imports,
            "code_sha256": code_hash,
            "receipt": receipt,
        }
    except SyntaxError as err:
        return {
            "status": "SYNTAX_ERROR",
            "error": str(err),
            "classes": [],
            "functions": [],
            "imports": [],
            "code_sha256": code_hash,
            "receipt": hashlib.sha256(f"ast-error:{code_hash}".encode("utf-8")).hexdigest(),
        }
