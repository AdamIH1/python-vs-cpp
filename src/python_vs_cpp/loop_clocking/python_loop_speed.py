import time

def run_speed_test_python(loops: int) -> float:
    """
    Run a Python speed test for the given number of loops.

    Args:
        loops: Number of loop iterations

    Returns:
        Elapsed time in milliseconds
    """
    if loops < 1:
        raise ValueError(f"loops must be >= 1, got {loops}")

    start = time.perf_counter()

    x = 0
    for _ in range(loops):
        x += 1

    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    return elapsed_ms
