# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.15)

project(CoLoFiEr
        VERSION 0.1
        DESCRIPTION "Demo project to show issues with conan lockfiles"
        LANGUAGES CXX)

include(GNUInstallDirs)

add_subdirectory(liba)

