#!/usr/bin/env python3

import pytest
from lib.ipdb_debugging import plus_two

class TestIpdbDebugging:
    def test_adds_two(self):
        """plus_two() adds 2 to the input argument and returns the sum."""
        assert plus_two(3) == 5


