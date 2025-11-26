import pytest
from hello_app import app

def test_fail():
    assert False

def test_math_fail():
    assert 1 + 1 == 3
