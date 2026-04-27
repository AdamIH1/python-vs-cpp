from typing import Optional

from ..loop_clocking.python_loop_speed import run_speed_test_python
from ..loop_clocking.cpp_loop_speed import run_speed_test_cpp

def compare_loop_speed(num_loops: Optional[int] = None, verbose: bool = True):
    """
    Run a loop speed comparison between Python and C++.

    Args:
        num_loops: Number of loops to run. If not provided, the user will
            be prompted to enter a value interactively.
        verbose: If True, prints progress and results. If False, runs silently.
    """
    if num_loops is None:
        num_loops = int(input("Enter number of loops: "))

    # Run Python version
    if verbose:
        print("--- Python Version ---")
    py_time = run_speed_test_python(num_loops)
    if verbose:
        print(f"Completed {num_loops} loops in {py_time:.4f} ms")

    # Run C++ version
    if verbose:
        print("---C++ Version ---")
    cpp_time = run_speed_test_cpp(num_loops)
    if verbose:
        print(f"Completed {num_loops} loops in {cpp_time:.4f} ms")

    # Show comparison
    speedup = py_time / cpp_time if cpp_time > 0 else 0

    if verbose:
        print("---Comparison ---")
        print(f"Python: {py_time:.4f} ms")
        print(f"C++:    {cpp_time:.4f} ms")
        print(f"C++ is {speedup:.2f}x faster")

    return {'python_ms': py_time, 'cpp_ms': cpp_time, 'speedup': speedup}
