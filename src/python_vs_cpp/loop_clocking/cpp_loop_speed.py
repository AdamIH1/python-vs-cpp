from .cpp_speed_test import run_speed_test as _run_speed_test_cpp

def run_speed_test_cpp(loops: int) -> float:
    """
    Run a C++ speed test for the given number of loops.

    Args:
        loops: Number of loop iterations

    Returns:
        Elapsed time in milliseconds
    """
    if loops < 1:
        raise ValueError(f"loops must be >= 1, got {loops}")

    elapsed_ms = _run_speed_test_cpp(loops)

    return elapsed_ms
