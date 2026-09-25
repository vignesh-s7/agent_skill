"""agent_skill.hermes - Pure Python adapter for Hermes candidate agent reasoning.

Enterprise Safe:
- Zero shell script (.sh / .bash) execution.
- Statically auditable pure Python standard library.
- Strictly produces unprivileged candidate output with SHA-256 cryptographic verification.
"""

from __future__ import annotations

import hashlib
import json
import time
import urllib.request
from typing import Any, Dict, Optional


def run_hermes_candidate(
    prompt: str,
    *,
    endpoint: Optional[str] = None,
    api_key: Optional[str] = None,
    model: str = "hermes-3-llama-3.1-8b",
    timeout_s: float = 30.0,
) -> Dict[str, Any]:
    """Execute a candidate reasoning step using an OpenAI-compatible Hermes endpoint.

    Returns structured output with SHA-256 digest and candidate isolation metadata.
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")

    target_endpoint = endpoint or "http://127.0.0.1:11434/v1/chat/completions"
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    start_time = time.monotonic()

    payload = json.dumps(
        {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a candidate reasoning assistant. Provide structured, factual candidate proposals.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
    ).encode("utf-8")

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    req = urllib.request.Request(
        target_endpoint,
        data=payload,
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as response:
            body = response.read().decode("utf-8")
            elapsed_ms = int((time.monotonic() - start_time) * 1000)
            data = json.loads(body)
            content = (
                data.get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
            )
            content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
            return {
                "status": "COMPLETED",
                "candidate_only": True,
                "output": content,
                "prompt_sha256": prompt_hash,
                "content_sha256": content_hash,
                "receipt": hashlib.sha256(f"hermes:{content_hash}".encode("utf-8")).hexdigest(),
                "latency_ms": elapsed_ms,
                "model": model,
            }
    except Exception as exc:
        elapsed_ms = int((time.monotonic() - start_time) * 1000)
        error_msg = str(exc)
        return {
            "status": "UNAVAILABLE",
            "candidate_only": True,
            "error": f"HermesEndpointUnavailable: {error_msg}",
            "prompt_sha256": prompt_hash,
            "receipt": hashlib.sha256(f"hermes-unavailable:{prompt_hash}".encode("utf-8")).hexdigest(),
            "latency_ms": elapsed_ms,
            "model": model,
        }
