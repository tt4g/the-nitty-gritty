cmake_minimum_required(VERSION 3.16.3)

project(spdlog-issue-2681 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG        v1.11.0
)
FetchContent_MakeAvailable(spdlog)

if(NOT TARGET spdlog)
    # Stand-alone build
    find_package(spdlog REQUIRED)
endif()

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_compile_options(-Wall -Wextra -pedantic -O3 -Wno-c11-extensions)

add_definitions(-DCROW_ENABLE_SSL)
add_executable(cs main.cpp)
add_library(deviceManager deviceManager.cpp)
target_link_libraries(deviceManager spdlog::spdlog)

target_link_libraries(cs deviceManager pthread rt ssl crypto spdlog::spdlog)

add_custom_command(
  TARGET cs POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:cs> ../../
)
