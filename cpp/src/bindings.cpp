#include <pybind11/pybind11.h>
#include "loop_speed.hpp"

namespace py = pybind11;

PYBIND11_MODULE(cpp_speed_test, m) {
    m.doc() = "time a c++ loop"; 
    m.def("run_speed_test", &run_speed_test, "Run C++ speed test for N loops");
}
