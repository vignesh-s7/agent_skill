"""agent_skill.rtk - Pure Python input interception and stream compaction for AI agent environments.

Origin: https://github.com/rtk-ai/rtk

Features:
- Intercepts shell command outputs (e.g. git log, build traces, test outputs).
- Collapses text streams down to essential errors, summaries, and status signals.
- Constrains verbose output before returning to LLM context, saving input tokens.
- Zero shell script execution; statically auditable pure Python standard library.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional


def compact_shell_output(
    raw_output: str,
    *,
    max_lines: int = 50,
    max_chars: int = 4000,
    focus_errors: bool = True,
) -> Dict[str, Any]:
    """Collapse verbose shell output down to essential lines, errors, and summaries."""
    if not raw_output or not isinstance(raw_output, str):
        return {
            "compacted_text": "",
            "raw_length": 0,
            "compacted_length": 0,
            "reduction_ratio": 0.0,
            "receipt": hashlib.sha256(b"").hexdigest(),
        }

    raw_len = len(raw_output)
    lines = raw_output.splitlines()
    total_lines = len(lines)

    if total_lines <= max_lines and raw_len <= max_chars:
        return {
            "compacted_text": raw_output.strip(),
            "raw_length": raw_len,
            "compacted_length": raw_len,
            "reduction_ratio": 1.0,
            "total_lines": total_lines,
            "compacted_lines": total_lines,
            "receipt": hashlib.sha256(raw_output.encode("utf-8")).hexdigest(),
        }

    error_patterns = [
        re.compile(r"(error|fail|exception|fatal|traceback|warning)", re.IGNORECASE),
        re.compile(r"^\s*at\s+.*:\d+"),  # stack traces
        re.compile(r"FAILED\s+\(.*\)|FAIL:"),  # test failures
    ]

    critical_lines: List[str] = []
    normal_lines: List[str] = []

    for idx, line in enumerate(lines):
        clean = line.strip()
        if not clean:
            continue
        if focus_errors and any(p.search(clean) for p in error_patterns):
            critical_lines.append(f"[L{idx+1}] {clean}")
        else:
            normal_lines.append(clean)

    selected: List[str] = []
    # Always keep first few lines for context
    head_count = min(5, len(lines))
    selected.extend([f"[L{i+1}] {lines[i].strip()}" for i in range(head_count) if lines[i].strip()])

    # Add error/critical lines
    if critical_lines:
        selected.append(f"... [RTK: Filtered {len(critical_lines)} critical/error lines] ...")
        selected.extend(critical_lines[: max_lines - head_count - 5])

    # Keep tail for final status/exit summary
    tail_count = min(5, len(lines))
    selected.append(f"... [RTK: Collapsed {total_lines - head_count - tail_count} intermediate lines] ...")
    selected.extend([f"[L{total_lines - tail_count + i + 1}] {lines[total_lines - tail_count + i].strip()}" for i in range(tail_count) if lines[total_lines - tail_count + i].strip()])

    compacted = "\n".join(selected)
    if len(compacted) > max_chars:
        compacted = compacted[:max_chars] + f"\n... [RTK: Truncated to {max_chars} chars] ..."

    compacted_len = len(compacted)
    ratio = round(compacted_len / raw_len, 3) if raw_len > 0 else 1.0

    return {
        "compacted_text": compacted,
        "raw_length": raw_len,
        "compacted_length": compacted_len,
        "reduction_ratio": ratio,
        "total_lines": total_lines,
        "compacted_lines": len(selected),
        "receipt": hashlib.sha256(compacted.encode("utf-8")).hexdigest(),
    }
