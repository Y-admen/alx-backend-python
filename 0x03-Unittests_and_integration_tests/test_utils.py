#!/usr/bin/env python3
" Parameterize a unit test"
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    "TestAccessNestedMap"
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b", 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        "test access nested map"
        self.assertequal(access_nested_map(nested_map, path, expected))

    @parameterized.expand([({}, ("a",), "a"),
                           ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_excep_msg):
        "test access nested map exception"
        with self.assertRaise(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], expected_excep_msg)
