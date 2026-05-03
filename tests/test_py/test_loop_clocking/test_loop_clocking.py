import pytest
from python_vs_cpp_speed.loop_clocking import (
    run_speed_test_python
)

from python_vs_cpp_speed.loop_clocking import (
    run_speed_test_cpp
)

@pytest.fixture
def python_speed_result():
    """Run the Python speed test once and share the result across tests."""
    return run_speed_test_python(loops=1000)

@pytest.fixture
def cpp_speed_result():
    """Run the C++ speed test once and share the result across tests."""
    return run_speed_test_cpp(loops=1000)

def test_returns_float_py(python_speed_result):
    assert isinstance(python_speed_result, float)

def test_returns_non_negative_py(python_speed_result):
    assert python_speed_result >= 0.0

def test_returns_float_cpp(cpp_speed_result):
    assert isinstance(cpp_speed_result, float)

def test_returns_non_negative_cpp(cpp_speed_result):
    assert cpp_speed_result >= 0.0

def test_more_loops_not_faster_high_count_py():
    small = run_speed_test_python(loops=1000)
    large = run_speed_test_python(loops=100000)
    assert large >= small

def test_more_loops_not_faster_high_count_cpp():
    small = run_speed_test_cpp(loops=1000)
    large = run_speed_test_cpp(loops=100000)
    assert large >= small

def test_invalid_input_py():
    with pytest.raises(ValueError):
        run_speed_test_python(loops=0)

def test_invalid_input_cpp():
    with pytest.raises(ValueError):
        run_speed_test_cpp(loops=0)
