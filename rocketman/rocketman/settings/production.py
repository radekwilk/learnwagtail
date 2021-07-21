from .base import *
import os

DEBUG = False

# getcwd  - is is to get current working directory
cwd = os.getcwd()

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

try:
    from .local import *
except ImportError:
    pass
