from medicus.settings.development import *

DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET')

assert DEBUG == False
assert SECRET_KEY