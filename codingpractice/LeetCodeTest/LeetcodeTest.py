import LeetCode
import pytest

class test_increment():
    def test_increment(self):
        assert LeetCode.increment(3) == 4
    def test_descrement(self):
        assert LeetCode.decrement(3) == 4
        