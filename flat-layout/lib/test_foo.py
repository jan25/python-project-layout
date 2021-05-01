import lib.foo as lib_foo
import unittest


def test_foo():
    assert lib_foo.name() == "I'm foo"


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(lib_foo.name(), "I'm foo")
