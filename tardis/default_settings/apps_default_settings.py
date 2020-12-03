import sys
import importlib
from django.conf import settings


this_module = sys.modules[__name__]


for app in settings.INSTALLED_APPS:
    if app.startswith("tardis.apps"):
        try:
            app_module = importlib.import_module("%s.default_settings" % app)
            # print("Loading default settings for %s" % app)
            for setting in dir(app_module):
                if setting.isupper():
                    # print(" - %s" % setting)
                    setattr(this_module, setting, getattr(app_module, setting))
        except Exception as e:
            # print("Can't load default settings for %s due to:\n%s" % (app, str(e)))
            pass
