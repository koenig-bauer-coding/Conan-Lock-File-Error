# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.15)


project(PackageTest CXX)

add_executable(example example.cpp)

find_package(CoLoFiEr REQUIRED COMPONENTS LibA)

target_link_libraries(example PRIVATE CoLoFiEr::LibA)