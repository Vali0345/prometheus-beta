import logging
import pytest
import io
import sys
from src.emoji_logger import setup_emoji_logger, log_with_emoji

def test_setup_emoji_logger():
    """Test creating a logger with default settings."""
    logger = setup_emoji_logger()
    assert isinstance(logger, logging.Logger)
    assert logger.name == 'emoji_logger'
    assert logger.level == logging.INFO

def test_log_with_emoji_valid_inputs(caplog):
    """Test logging with various valid inputs."""
    logger = setup_emoji_logger()
    caplog.set_level(logging.INFO)
    
    # Test logging with an emoji
    log_with_emoji(logger, "Hello world", emoji="🌍")
    assert "Hello world" in caplog.text
    assert "🌍" in caplog.text
    
    # Test logging without an emoji
    log_with_emoji(logger, "Test message")
    assert "Test message" in caplog.text

def test_log_with_emoji_different_levels(caplog):
    """Test logging at different levels."""
    logger = setup_emoji_logger()
    
    test_cases = [
        ('debug', logging.DEBUG, "Debug message"),
        ('info', logging.INFO, "Info message"),
        ('warning', logging.WARNING, "Warning message"),
        ('error', logging.ERROR, "Error message"),
        ('critical', logging.CRITICAL, "Critical message")
    ]
    
    for level, log_level, message in test_cases:
        caplog.clear()
        caplog.set_level(log_level)
        log_with_emoji(logger, message, emoji="✨", level=level)
        assert message in caplog.text
        assert "✨" in caplog.text

def test_log_with_emoji_invalid_inputs():
    """Test error handling for invalid inputs."""
    logger = setup_emoji_logger()
    
    # Invalid logger
    with pytest.raises(TypeError, match="First argument must be a logging.Logger instance"):
        log_with_emoji("not a logger", "message")
    
    # Invalid message type
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_emoji(logger, 123)
    
    # Invalid log level
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji(logger, "Message", level="invalid")