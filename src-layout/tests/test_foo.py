from lib import foo
import pytest
import unittest


def test_foo():
    assert foo.name() == "I'm foo!"


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo.name(), "I'm foo!")
