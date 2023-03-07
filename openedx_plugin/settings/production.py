"""
Common Pluggable Django App settings
"""
#from path import Path as path
import environ
import os

# cast anything that doesn't have to flow via CI
# Note: this is for local development. On K8S these settings
# are injected into the setup. this will only be used if the settings don't
# already exist
env = environ.Env(
    DEBUG=(bool, False),
    BADGR_ISSUER_SLUG=(str, ""),
    BADGR_BASE_URL=(str, "https://api.badgr.io"),
    BADGR_USERNAME=(str, ""),
    BADGR_PASSWORD=(str, ""),
    BADGR_TOKENS_CACHE_KEY=(str, ""),
)

# path to this file.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG")

# Raises Django's ImproperlyConfigured
# exception if any of these params are not in os.environ
_BADGR_ISSUER_SLUG = env("BADGR_ISSUER_SLUG")
_BADGR_BASE_URL = env("BADGR_BASE_URL")
_BADGR_USERNAME = env("BADGR_USERNAME")
_BADGR_PASSWORD = env("BADGR_PASSWORD")
_BADGR_TOKENS_CACHE_KEY = env("BADGR_TOKENS_CACHE_KEY")

# django stuff
from ..waffle import waffle_switches, OVERRIDE_OPENEDX_DJANGO_LOGIN


def plugin_settings(settings):
    """
    Injects local settings into django settings
    """
    settings.BADGR_ISSUER_SLUG = _BADGR_ISSUER_SLUG
    settings.BADGR_BASE_URL = _BADGR_BASE_URL
    settings.BADGR_USERNAME = _BADGR_USERNAME
    settings.BADGR_PASSWORD = _BADGR_PASSWORD
    settings.BADGR_TOKENS_CACHE_KEY = _BADGR_TOKENS_CACHE_KEY

    if waffle_switches[OVERRIDE_OPENEDX_DJANGO_LOGIN]:
        middleware = getattr(settings, "MIDDLEWARE", None)
        if middleware:
            settings.MIDDLEWARE.append("openedx_plugin.middleware.RedirectDjangoAdminMiddleware")
