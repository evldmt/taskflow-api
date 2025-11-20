from decouple import config

if config('DEBUG', default=True, cast=bool):
    from .dev import *
else:
    from .prod import *