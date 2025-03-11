import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

class LogCapture:
    def __init__(self):
        self.captured = []

    def write(self, message):
        self.captured.append(message)

    def getvalue(self):
        return ''.join(self.captured)

def test_log_variable_type_with_int():
    # Capture log output
    log_capture = LogCapture()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test int type
    result = log_variable_type(42)
    log_output = log_capture.getvalue().strip()

    assert result == int
    assert "Variable type is: <class 'int'>" in log_output

def test_log_variable_type_with_str():
    # Capture log output
    log_capture = LogCapture()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test string type
    result = log_variable_type("Hello")
    log_output = log_capture.getvalue().strip()

    assert result == str
    assert "Variable type is: <class 'str'>" in log_output

def test_log_variable_type_with_list():
    # Capture log output
    log_capture = LogCapture()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test list type
    test_list = [1, 2, 3]
    result = log_variable_type(test_list)
    log_output = log_capture.getvalue().strip()

    assert result == list
    assert "Variable type is: <class 'list'>" in log_output

def test_log_variable_type_with_none():
    # Capture log output
    log_capture = LogCapture()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test None type
    result = log_variable_type(None)
    log_output = log_capture.getvalue().strip()

    assert result == type(None)
    assert "Variable type is: <class 'NoneType'>" in log_output

def test_log_variable_type_with_custom_class():
    # Custom class for testing
    class TestClass:
        pass

    # Capture log output
    log_capture = LogCapture()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test custom class type
    test_instance = TestClass()
    result = log_variable_type(test_instance)
    log_output = log_capture.getvalue().strip()

    assert result == TestClass
    assert "Variable type is: <class 'TestClass'>" in log_output