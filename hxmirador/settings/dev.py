from .prod import *

DEBUG = True

HXLTI_ENFORCE_SSL = False

# add db logging to dev settings
LOGGING['loggers']['django.db'] = {
    'level': 'INFO',
    'handlers': ['console'],
    'propagate': True
}


