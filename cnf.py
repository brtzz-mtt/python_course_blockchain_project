import os

DEBUG_MODE = True

BASE_PATH = os.path.dirname(__file__) + '/'

with open(BASE_PATH + 'README.md') as readme_file:
    BASE_TITLE = "EvoCHAIN v" + readme_file.readline().strip()
    for line in readme_file:
        pass
    COPYRIGHT = line
