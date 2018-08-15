#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake
import os
import tempfile


class Catch2Conan(ConanFile):
    name = "catch2"
    version = "2.3.0"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"
    homepage = "https://github.com/catchorg/Catch2"
    url = "https://github.com/bincrafters/conan-catch"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "https://github.com/catchorg/Catch2/blob/master/LICENSE.txt"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    header_name = "catch.hpp"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    no_copy_source = True

    def source(self):
        source_url = "https://github.com/catchorg/Catch2"
        tools.download(
            "{0}/releases/download/v{1}/{2}".format(source_url, self.version, self.header_name),
            self.header_name
        )

        # All this to get the LICENSE.txt
        extracted_dir = "Catch2-" + self.version
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        install_dir = tempfile.mkdtemp()
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = install_dir
        cmake.configure()
        cmake.install()
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self.source_subfolder)
        self.copy(pattern=self.header_name, dst=os.path.join("include", self.name))
        self.copy(pattern="*.cmake", dst=".", src=os.path.join(install_dir, "lib", "cmake", "Catch2"))

    def package_id(self):
        self.info.header_only()
