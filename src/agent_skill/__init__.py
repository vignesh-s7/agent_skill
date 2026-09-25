"""agent_skill - deterministic utilities, constraint satisfaction, and open-source toolchain adapters.

Enterprise Compliant:
- Zero shell scripts (.sh).
- Statically auditable pure Python standard library.
- Standard declarative configuration dotfiles.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

__version__ = "0.3.0"
__all__ = [
    "available_capabilities",
    "configure_environment",
    "run_hermes_candidate",
    "run_langchain_graph",
    "compact_shell_output",
    "score_build",
    "analyze_code_structure",
]


def available_capabilities() -> dict[str, bool]:
    """Check availability of optional engine libraries."""
    capabilities = {
        "ortools": False,
        "onnxruntime": False,
        "graphify": True,   # stdlib AST fallback available
        "hermes": True,     # stdlib urllib fallback available
        "langchain": False,
        "rtk": True,        # stdlib stream compactor available
        "ponytail": True,   # stdlib BUILD scoring available
    }
    try:
        import ortools  # noqa: F401
        capabilities["ortools"] = True
    except ImportError:
        pass

    try:
        import onnxruntime  # noqa: F401
        capabilities["onnxruntime"] = True
    except ImportError:
        pass

    try:
        import graphify  # noqa: F401
        capabilities["graphify"] = True
    except ImportError:
        pass

    try:
        import langchain_core  # noqa: F401
        capabilities["langchain"] = True
    except ImportError:
        pass

    return capabilities


def configure_environment(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of configure_environment to keep package import clean."""
    from agent_skill.configure import configure_environment as _cfg
    return _cfg(*args, **kwargs)


def run_hermes_candidate(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of run_hermes_candidate."""
    from agent_skill.hermes import run_hermes_candidate as _hermes
    return _hermes(*args, **kwargs)


def run_langchain_graph(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of run_langchain_graph."""
    from agent_skill.langchain_adapter import run_langchain_graph as _langchain
    return _langchain(*args, **kwargs)


def compact_shell_output(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of compact_shell_output (RTK)."""
    from agent_skill.rtk import compact_shell_output as _rtk
    return _rtk(*args, **kwargs)


def score_build(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of score_build (Ponytail)."""
    from agent_skill.ponytail import score_build as _pt
    return _pt(*args, **kwargs)


def analyze_code_structure(*args: Any, **kwargs: Any) -> Any:
    """Lazy import of analyze_code_structure (Graphify)."""
    from agent_skill.graphify_adapter import analyze_code_structure as _ga
    return _ga(*args, **kwargs)
