"""
Unit and regression test for the markplotlib package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import markplotlib


def test_markplotlib_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", markplotlib.__name__)
    assert "markplotlib" in sys.modules


# Assert that a certain exception is raised
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
