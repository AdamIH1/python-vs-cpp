# python-vs-cpp-speed

[![Unit Tests Linter](https://github.com/AdamIH1/python-vs-cpp-speed/actions/workflows/unit_test_linter.yml/badge.svg?branch=main&label=Unit%20Tests)](https://github.com/AdamIH1/python-vs-cpp-speed/actions/workflows/unit_test_linter.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


#

A Python package that benchmarks pure Python vs C++ loop performance using **Pybind11**.

> **Disclaimer:** This repository is primarily for learning and templating purposes, demonstrating PyPI package development, Pybind11 bindings, and GitHub Actions workflows.

---

## 🔧 Features

- ⚡ **C++ Speed Test**: Measure loop execution time via a compiled Pybind11 extension.
- 🐍 **Python Speed Test**: Equivalent pure Python benchmark for direct comparison.
- 📊 **Side-by-side Comparison**: Returns Python time, C++ time, and speedup multiplier.

---

## 📦 Installation

```bash
pip install python-vs-cpp-speed
```

> Requires Python ≥ 3.9. Prebuilt wheels available for Windows, macOS, and Linux.  
> Building from source requires `cmake >= 3.15` and a C++17 compiler.

---

## 🚀 Quickstart

```python
import python_vs_cpp_speed as pvc

results = pvc.compare_loop_speed(num_loops=1_000_000)
```

**Output:**
```
--- Python Version ---
Completed 1000000 loops in 42.3121 ms
--- C++ Version ---
Completed 1000000 loops in 0.6234 ms
--- Comparison ---
Python: 42.3121 ms
C++:    0.6234 ms
C++ is 67.88x faster
```

---

## 🧪 API Reference

### `compare_loop_speed`

```python
from python_vs_cpp_speed import compare_loop_speed

compare_loop_speed(
    num_loops: Optional[int] = None,
    verbose: bool = True
) -> dict
```

Runs both Python and C++ loop benchmarks and returns a results dictionary.

- `num_loops`: Number of loop iterations. If `None`, prompts for user input.
- `verbose`: If `True`, prints progress and results to stdout.

Returns:
```python
{
    "python_ms": float,   # Python loop time in milliseconds
    "cpp_ms":    float,   # C++ loop time in milliseconds
    "speedup":   float    # python_ms / cpp_ms
}
```

> `num_loops` must be >= 1.

---

## 🏗️ Building from Source

```bash
git clone https://github.com/AdamIH1/python-vs-cpp-speed.git
cd python-vs-cpp-speed
pip install .
```

Requirements: `cmake >= 3.15`, `pybind11 >= 2.11`, a C++17-compatible compiler.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 Contributing

Contributions welcome! Feel free to open issues or submit PRs on [GitHub](https://github.com/AdamIH1/python-vs-cpp-speed/tree/main).
