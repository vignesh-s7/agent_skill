"""agent_skill.configure - Pure Python declarative environment configurator.

Enterprise Safe:
- Zero shell script (.sh / .bash) execution.
- Statically auditable Python 3.10+ standard library only (json, pathlib, shutil).
- Safely configures user dotfiles (~/.gemini/config/mcp_config.json, ~/.claude/settings.json).
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Dict


def detect_node_binary() -> str:
    """Locate the node runtime binary using Python's standard path lookup."""
    node_path = shutil.which("node")
    if node_path:
        return node_path

    # Common fallbacks in developer containers and cloud shells
    home = Path.home()
    candidates = [
        home / "nvm" / "current" / "bin" / "node",
        Path("/usr/local/bin/node"),
        Path("/usr/bin/node"),
    ]
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    return "node"


def detect_skills_directory() -> str:
    """Locate companion skills repository directory."""
    home = Path.home()
    candidates = [
        home / "skills",
        Path("/workspaces/skills"),
        home / "Core" / "Skills-Bundle",
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return str(candidate)

    return str(home / "skills")


def configure_environment(target_home: Path | None = None) -> Dict[str, Any]:
    """Declaratively write standard MCP and assistant configuration dotfiles."""
    home = target_home or Path.home()
    node_bin = detect_node_binary()
    skills_dir = detect_skills_directory()

    gemini_dir = home / ".gemini" / "config"
    claude_dir = home / ".claude"

    gemini_dir.mkdir(parents=True, exist_ok=True)
    claude_dir.mkdir(parents=True, exist_ok=True)

    node_parent = str(Path(node_bin).parent)
    system_path = f"{node_parent}:/usr/local/bin:/usr/bin:/bin"

    # 1. Gemini / AGY MCP Configuration
    gemini_mcp = {
        "mcpServers": {
            "Skills-MCP-L": {
                "command": node_bin,
                "args": [f"{skills_dir}/server/dist/stdio.js"],
                "env": {
                    "PATH": system_path,
                },
            }
        }
    }
    gemini_config_path = gemini_dir / "mcp_config.json"
    with open(gemini_config_path, "w", encoding="utf-8") as f:
        json.dump(gemini_mcp, f, indent=2)

    # 2. Claude / Cline Configuration
    claude_settings = {
        "mcpServers": {
            "Skills-MCP-L": {
                "command": node_bin,
                "args": [f"{skills_dir}/server/dist/stdio.js"],
            }
        }
    }
    claude_config_path = claude_dir / "settings.json"
    with open(claude_config_path, "w", encoding="utf-8") as f:
        json.dump(claude_settings, f, indent=2)

    return {
        "status": "CONFIGURED",
        "gemini_mcp": str(gemini_config_path),
        "claude_settings": str(claude_config_path),
        "node_binary": node_bin,
        "skills_directory": skills_dir,
    }


def main() -> int:
    """CLI entry point: python -m agent_skill.configure"""
    result = configure_environment()
    print("==> Open Garden Environment Configured (Pure Python, Zero Shell):")
    print(f"  [✓] Gemini MCP:     {result['gemini_mcp']}")
    print(f"  [✓] Claude Config:  {result['claude_settings']}")
    print(f"  [i] Node Binary:    {result['node_binary']}")
    print(f"  [i] Skills Path:    {result['skills_directory']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
