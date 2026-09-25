"""agent_skill.langchain_adapter - Pure Python adapter for LangChain and LangGraph runtimes.

Enterprise Safe:
- Zero shell script execution.
- Statically auditable pure Python standard library.
- Safely runs LangChain/LangGraph flows in containerized or host environments.
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Callable, Dict, Optional


def run_langchain_graph(
    graph_callable: Callable[[Dict[str, Any]], Dict[str, Any]],
    initial_state: Dict[str, Any],
    *,
    timeout_s: float = 60.0,
) -> Dict[str, Any]:
    """Execute a callable LangGraph graph or LangChain chain and capture cryptographic receipt."""
    if not callable(graph_callable):
        raise ValueError("graph_callable must be a callable object")

    start_time = time.monotonic()
    state_str = json.dumps(initial_state, sort_keys=True, default=str)
    input_hash = hashlib.sha256(state_str.encode("utf-8")).hexdigest()

    try:
        result_state = graph_callable(initial_state)
        elapsed_ms = int((time.monotonic() - start_time) * 1000)
        res_str = json.dumps(result_state, sort_keys=True, default=str)
        output_hash = hashlib.sha256(res_str.encode("utf-8")).hexdigest()

        return {
            "status": "COMPLETED",
            "candidate_only": True,
            "result": result_state,
            "input_sha256": input_hash,
            "output_sha256": output_hash,
            "receipt": hashlib.sha256(f"langchain:{output_hash}".encode("utf-8")).hexdigest(),
            "latency_ms": elapsed_ms,
        }
    except Exception as exc:
        elapsed_ms = int((time.monotonic() - start_time) * 1000)
        return {
            "status": "ERROR",
            "candidate_only": True,
            "error": f"LangChainExecutionError: {exc}",
            "input_sha256": input_hash,
            "receipt": hashlib.sha256(f"langchain-error:{input_hash}".encode("utf-8")).hexdigest(),
            "latency_ms": elapsed_ms,
        }
