import logging

def setup_logger():
    """
    Configure the application logging
    
    Sets up a properly formatted logger for the application that includes
    timestamps, logger names, and log levels in the output.
    
    Returns:
        logging.Logger: The configured logger instance for the application
    """
    # Configure root logger with basic settings
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    
    # Create and return a specific logger for our application
    logger = logging.getLogger("serverhub")
    
    # Optional: Configure specific loggers differently if needed
    # For example, to reduce verbosity from libraries
    # sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
    # sqlalchemy_logger.setLevel(logging.WARNING)
    
    return logger
