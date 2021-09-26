import os
from modules.logger import Logger

DEBUG_MODE = True

BASE_PATH = os.path.dirname(__file__) + '/'

with open(BASE_PATH + 'log.md') as log_file:
    VERSION = log_file.readline().strip()

with open(BASE_PATH + 'README.md') as readme_file:
    BASE_TITLE = readme_file.readline().strip() + " v" + VERSION
    for line in readme_file:
        pass
    COPYRIGHT = line

LOGGER = Logger('./app.log', False)
