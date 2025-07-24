from abc import ABC
import logging
import logging.config
import inspect
import os
import sys
from food_pantry.settings import LOG_SETTINGS


# Path to the log directory
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')

# If the log directory does not exist, create it
os.makedirs(LOG_DIR, exist_ok=True)


# Logger class for logging actions in the application
# It uses the logging module to log messages to a file and to the console.
class Logger(ABC):  
    def init_log(self, log_name = None):

        # If no logger name is passed, use the class name
        if not log_name:
            if 'pytest' in sys.modules:
                log_name = 'tests'
            else:
                log_name = self.__class__.__name__

        
        # Get the log file name from LOG_SETTINGS or use the default
        
        # Get the specific log file name from settings or use default
        specific_log_file = LOG_SETTINGS.get('log_files', {}).get(log_name, LOG_SETTINGS['log_files']['default'])
        specific_log_path = os.path.join(LOG_DIR, specific_log_file)

        # Path to the shared/general log file
        general_log_path = os.path.join(LOG_DIR, LOG_SETTINGS['log_files']['general'])

        # Create the logging configuration
        # It defines the formatters, handlers, and loggers for the application
        logging_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                },
            },
            'handlers': {
                'specific_file': {
                    'level': LOG_SETTINGS.get('file_log_level'),
                    'class': 'logging.FileHandler',
                    'filename': specific_log_path,
                    'formatter': 'default',
                    'encoding': 'utf-8',
                },
                'general_file': {
                    'level': LOG_SETTINGS['file_log_level'],
                    'class': 'logging.FileHandler',
                    'filename': general_log_path,
                    'formatter': 'default',
                    'encoding': 'utf-8',
                },
                'stdout': {
                    'level': LOG_SETTINGS.get('stdout_log_level'),   
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                },
            },
            'loggers': {
                log_name: {
                    'handlers': ['specific_file', 'general_file', 'stdout'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }

        logging.config.dictConfig(logging_config)
        return logging.getLogger(log_name)

    def __init__(self, log_name=None):
        # Initialize logger with optional custom name
        self.__logger_app = self.init_log(log_name)
    
    def info(self,message):
        self.__logger_app.info(f"{inspect.stack()[1][3]} - {message}")
        
    def warning(self,message):
        self.__logger_app.warning(f"{inspect.stack()[1][3]} - {message}")
    
    def debug(self,message):
        self.__logger_app.debug(f"{inspect.stack()[1][3]} - {message}")
        
    def critical(self,message):
        self.__logger_app.critical(f"{inspect.stack()[1][3]} - {message}")
        
    def error(self,message):
        self.__logger_app.error(f"{inspect.stack()[1][3]} - {message}")
        