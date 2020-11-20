from .prod import *  # noqa
from .prod import LOGGING

DEBUG = True

# add db logging to dev settings
LOGGING["loggers"]["django.db"] = {
    "level": "INFO",
    "handlers": ["console"],
    "propagate": True,
}
