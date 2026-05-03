import pytest

from python_vs_cpp_speed.api import compare_loop_speed

@pytest.fixture
def loop_result():
    """Pre-computed result dict shared across tests
    that just inspect the output.
    """
    return compare_loop_speed(num_loops=1000, verbose=False)

def test_returns_dict(loop_result):
    assert isinstance(loop_result, dict)

def test_return_dict_has_expected_keys(loop_result):
    assert set(loop_result.keys()) == {"python_ms", "cpp_ms", "speedup"}

def test_all_values_non_negative(loop_result):
    assert loop_result["python_ms"] >= 0.0
    assert loop_result["cpp_ms"] >= 0.0
    assert loop_result["speedup"] >= 0.0

def test_speedup_calculation(loop_result):
    expected_speedup = loop_result["python_ms"] / loop_result["cpp_ms"]
    assert loop_result["speedup"] == pytest.approx(expected_speedup, rel=1e-3)
