#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Test module

# Takes user Str in camelCase
# Converts it to  to snake_case

from camel import camelcase_converter


def test_camelcase_converter():
    assert camelcase_converter("camelCase") == ("camel_case")
    assert camelcase_converter("helloWorld") == ("hello_world")
