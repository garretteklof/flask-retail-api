import json
import os

with open('config/config.json') as f:
    config = json.load(f)

_APP_SECRET_ = os.urandom(24)
#_JWT_SECRET_KEY_ = config['JWT_SECRET_KEY']
