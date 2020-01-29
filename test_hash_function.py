from hash_function import hash_function
import pytest

def test_string_input():
    assert(hash_function("Hello", 5)) < 5

def test_int_input():
    assert(hash_function(188, 5)) < 5
