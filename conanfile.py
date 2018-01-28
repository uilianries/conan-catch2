#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class Catch2Conan(ConanFile):
    name = "catch2"
    version = "2.1.1"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"
    url = "https://github.com/bincrafters/conan-catch"
    license = "BSL-1.0"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    header_name = "catch.hpp"

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
        self.copy(pattern="LICENSE.txt", src=self.source_subfolder)
        self.copy(pattern=self.header_name, dst="include")

    def package_id(self):
        self.info.header_only()
        