cmake_minimum_required(VERSION 3.16.3)

project(spdlog-issue-2681 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_compile_options(-Wall -Wextra -pedantic -O3 -Wno-c11-extensions)

find_library(SPDLOG_LIB spdlog)

add_definitions(-DCROW_ENABLE_SSL)
add_executable(cs main.cpp)
add_library(deviceManager deviceManager.cpp)
target_link_libraries(deviceManager)

target_link_libraries(cs deviceManager pthread spdlog fmt)

add_custom_command(
  TARGET cs POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:cs> ../../
)
