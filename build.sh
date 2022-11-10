#!/bin/bash

# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT 

# Create packages without lockfiles
conan create . pj/testing -pr:h default -pr:b default -s build_type=Release
conan create . pj/testing -pr:h default -pr:b default -s build_type=Debug

# Create base lock
conan lock create conanfile.py --user=pj --channel=testing --lockfile-out=locks/deps_base.lock --base

# Create lock file per configuration
conan lock create conanfile.py --user=pj --channel=testing --lockfile=locks/deps_base.lock -pr:h default -pr:b default --lockfile-out=locks/deps_debug.lock -s build_type=Debug 
conan lock create conanfile.py --user=pj --channel=testing --lockfile=locks/deps_base.lock -pr:h default -pr:b default --lockfile-out=locks/deps_release.lock -s build_type=Release

# Try to create package with lock file
conan create . pj/testing --lockfile=locks/deps_debug.lock