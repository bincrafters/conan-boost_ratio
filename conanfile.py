#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostRatioConan(base.BoostBaseConan):
    name = "boost_ratio"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_ratio"
    lib_short_names = ["ratio"]
    header_only_libs = ["ratio"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_mpl",
        "boost_rational",
        "boost_static_assert",
        "boost_type_traits"
    ]
