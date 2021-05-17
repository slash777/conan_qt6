cmake_minimum_required(VERSION 3.1.0)

set(CMAKE_CXX_STANDARD 17)

project(test_package)

if(NOT EXISTS "${PROJECT_BINARY_DIR}/conan.cmake")
      message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
      file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.15/conan.cmake"
                    "${PROJECT_BINARY_DIR}/conan.cmake" STATUS status)
      list (GET status 0 download_failed)
      if(${download_failed})
          message(FATAL_ERROR "... Downloading conan.cmake failed. Working with cached version. ${PROJECT_BINARY_DIR}")
      endif(${download_failed})
endif(NOT EXISTS "${PROJECT_BINARY_DIR}/conan.cmake")
include(${PROJECT_BINARY_DIR}/conan.cmake)

conan_cmake_run(CONANFILE conanfile.py
               BASIC_SETUP
               NO_OUTPUT_DIRS
               CMAKE_TARGETS
               KEEP_RPATHS
               BUILD missing
               BUILD_TYPE ${CMAKE_BUILD_TYPE}
               PROFILE_AUTO build_type compiler.version)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

find_package(Qt6 REQUIRED CONFIG)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

add_executable(${PROJECT_NAME} test_package.cpp greeter.h example.qrc)
# Must compile with "-fPIC" since Qt was built with -reduce-relocations.
target_compile_options(${PROJECT_NAME} PRIVATE -fPIC)

target_link_libraries(${PROJECT_NAME} Qt6::Core)
