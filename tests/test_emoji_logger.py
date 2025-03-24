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
        ('debug', logging.DEBUG, "Debug message", "Should show debug with debug level"),
        ('info', logging.INFO, "Info message", "Should show info with info level"),
        ('warning', logging.WARNING, "Warning message", "Should show warning with warning level"),
        ('error', logging.ERROR, "Error message", "Should show error with error level"),
        ('critical', logging.CRITICAL, "Critical message", "Should show critical with critical level")
    ]
    
    for level, log_level, message, description in test_cases:
        # Reset logger and set its level
        logger = setup_emoji_logger()
        logger.setLevel(log_level)
        
        # Clear previous log records
        caplog.clear()
        caplog.set_level(log_level)
        
        # Log the message
        log_with_emoji(logger, message, emoji="✨", level=level)
        
        # Different expectations for different log levels
        if log_level == logging.DEBUG:
            # Use setLevel to correctly capture debug messages
            assert message in caplog.text, f"{description} failed"
        else:
            assert message in caplog.text, f"{description} failed"

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