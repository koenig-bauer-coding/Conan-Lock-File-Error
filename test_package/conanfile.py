# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT 

import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class CoLoFiErTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv", "VirtualRunEnv"
    test_type = "explicit"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(".%sexample" % os.sep)

    def layout(self):
        cmake_layout(self)
