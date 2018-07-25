from .prod import *

# add db logging to dev settings
LOGGING['loggers']['django.db'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': True
}


