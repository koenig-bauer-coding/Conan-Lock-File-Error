# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT 

from conan import ConanFile
from conan.tools.cmake import CMake


class ConanLockFileError(ConanFile):
    name = "CoLoFiEr"
    author = "Philipp Jeske <philipp.jeske@koenig-bauer.com>"
    version = "0.1"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared":       [True, False],
        "fPIC":         [True, False]
    }
    default_options = {
        "shared":       False,
        "fPIC":         True
    }
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "liba/**"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "CoLoFiEr"
        self.cpp_info.set_property("cmake_file_name", "CoLoFiEr")
        self.cpp_info.set_property("cmake_find_mode", "both")

        self.cpp_info.components['liba'].names["cmake_find_package"] = 'LibA'
        self.cpp_info.components['liba'].set_property(
            "cmake_target_name", f"CoLoFiEr::LibA")
        self.cpp_info.components['liba'].libs = ['LibA']
