import logging
import sys

def setup_emoji_logger(name='emoji_logger', log_level=logging.INFO):
    """
    Set up a logger that supports emoji and symbol logging.
    
    Args:
        name (str, optional): Name of the logger. Defaults to 'emoji_logger'.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        logging.Logger: Configured logger that supports emoji and symbol logging.
    """
    # Create a logger
    logger = logging.getLogger(name)
    
    # Prevent duplicate handlers
    if not logger.handlers:
        logger.setLevel(log_level)
        
        # Create console handler and set level
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        
        # Create formatter that supports Unicode characters
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Add formatter to console handler
        console_handler.setFormatter(formatter)
        
        # Add console handler to logger
        logger.addHandler(console_handler)
    
    return logger

def log_with_emoji(logger, message, emoji=None, level='info'):
    """
    Log a message with an optional emoji.
    
    Args:
        logger (logging.Logger): Logger to use for logging.
        message (str): Message to log.
        emoji (str, optional): Emoji or symbol to prepend to the message. Defaults to None.
        level (str, optional): Logging level. Defaults to 'info'.
    
    Raises:
        ValueError: If an invalid logging level is provided.
        TypeError: If logger is not a valid logger or message is not a string.
    """
    # Validate inputs
    if not isinstance(logger, logging.Logger):
        raise TypeError("First argument must be a logging.Logger instance")
    
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Prepare the log message
    full_message = f"{emoji + ' ' if emoji else ''}{message}"
    
    # Select logging method based on level
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    if level not in log_levels:
        raise ValueError(f"Invalid log level. Choose from {list(log_levels.keys())}")
    
    # Log the message
    log_levels[level](full_message)