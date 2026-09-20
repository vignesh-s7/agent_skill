"""agent_skill - deterministic utilities, constraint satisfaction, and code analysis helpers."""

__version__ = "0.1.0"


def available_capabilities() -> dict[str, bool]:
    """Check availability of optional engine libraries."""
    capabilities = {
        "ortools": False,
        "onnxruntime": False,
        "graphify": False,
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

    return capabilities
