#include "loop_speed.hpp"
#include <chrono>

double run_speed_test(std::size_t loops) {
    auto start = std::chrono::high_resolution_clock::now();
    volatile std::size_t x = 0; 
    for (std::size_t i = 0; i < loops; i++) {
        x++; 
    }
    auto end = std::chrono::high_resolution_clock::now();
    return std::chrono::duration<double, std::milli>(end - start).count();
}
