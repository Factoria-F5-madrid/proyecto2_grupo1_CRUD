from abc import ABC
import logging
import inspect
from food_pantry.settings import LOG_SETTINGS

class Logger(ABC):  
    def init_log(self, log_name = None):
        if not log_name:
            log_name = self.__class__.__name__ 
        
        logging_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                },
            },
            'handlers': {
                'file': {
                    'level': LOG_SETTINGS.get('file_log_level'),
                    'class': 'logging.FileHandler',
                    'filename': LOG_SETTINGS.get('file_name') + '.log',
                    'formatter': 'default',
                },
                'stdout': {
                    'level': LOG_SETTINGS.get('stdout_log_level'),   
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                },
            },
            'loggers': {
                log_name: {
                    'handlers': ['file', 'stdout'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }

        logging.config.dictConfig(logging_config)
        return logging.getLogger(log_name)

    def __init__(self):
        self.__logger_app = self.init_log()
    
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
        
