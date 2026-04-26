// #include <gtest/gtest.h>
// #include "loop_speed.hpp"
 
// // --- basic return value tests ---
 
// TEST(LoopSpeedTest, ReturnsNonNegative) {
//     double result = run_speed_test(1000);
//     EXPECT_GE(result, 0.0);
// }
 
// TEST(LoopSpeedTest, ZeroLoopsReturnsNonNegative) {
//     double result = run_speed_test(0);
//     EXPECT_GE(result, 0.0);
// }
 
// TEST(LoopSpeedTest, OneLoopReturnsNonNegative) {
//     double result = run_speed_test(1);
//     EXPECT_GE(result, 0.0);
// }
 
// TEST(LoopSpeedTest, LargeLoopCountReturnsPositive) {
//     double result = run_speed_test(1'000'000);
//     EXPECT_GT(result, 0.0);
// }
 
// // --- ordering test ---
 
// TEST(LoopSpeedTest, MoreLoopsNotFaster) {
//     double small = run_speed_test(1'000);
//     double large = run_speed_test(1'000'000);
//     EXPECT_GE(large, small);
// }
 
// int main(int argc, char **argv) {
//     ::testing::InitGoogleTest(&argc, argv);
//     return RUN_ALL_TESTS();
// }
