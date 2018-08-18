project(test_package)
cmake_minimum_required(VERSION 3.0.2)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Catch2 2.3.0 REQUIRED CONFIG)

include(ParseAndAddCatchTests)
include(Catch)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)

catch_discover_tests(${PROJECT_NAME})
