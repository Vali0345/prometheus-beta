import pytest
import logging
from src.variable_type_logger import log_variable_type

def test_log_variable_type_with_int(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)

    # Test int type
    result = log_variable_type(42)

    # Check logging output
    assert result == int
    assert "Variable type is: <class 'int'>" in caplog.text

def test_log_variable_type_with_str(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)

    # Test string type
    result = log_variable_type("Hello")

    # Check logging output
    assert result == str
    assert "Variable type is: <class 'str'>" in caplog.text

def test_log_variable_type_with_list(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)

    # Test list type
    test_list = [1, 2, 3]
    result = log_variable_type(test_list)

    # Check logging output
    assert result == list
    assert "Variable type is: <class 'list'>" in caplog.text

def test_log_variable_type_with_none(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)

    # Test None type
    result = log_variable_type(None)

    # Check logging output
    assert result == type(None)
    assert "Variable type is: <class 'NoneType'>" in caplog.text

def test_log_variable_type_with_custom_class(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)

    # Custom class for testing
    class TestClass:
        pass

    # Test custom class type
    test_instance = TestClass()
    result = log_variable_type(test_instance)

    # Check logging output
    assert result == TestClass
    assert "Variable type is: <class 'TestClass'>" in caplog.text