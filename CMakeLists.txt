cmake_minimum_required(VERSION 3.15)
project(python_vs_cpp LANGUAGES CXX)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

pybind11_add_module(
    cpp_speed_test
    cpp/src/loop_speed.cpp
    cpp/src/bindings.cpp
)

target_include_directories(cpp_speed_test PRIVATE cpp/include)

# Install the compiled module to the python_vs_cpp/loop_clocking package directory
install(TARGETS cpp_speed_test LIBRARY DESTINATION python_vs_cpp/loop_clocking)
