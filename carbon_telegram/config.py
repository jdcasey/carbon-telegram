import yaml
import getpass
import subprocess
import os
import sys

CONFIG_PATH = '/etc/carbon-telegram.yml'

TOKEN = 'token'

class Config(object):
    def __init__(self, data):
        self.token = data[TOKEN]

def load(config_file=None):
    config_path = config_file or CONFIG_PATH
    data = None

    with open(config_path) as f:
        data = yaml.safe_load(f)

    return Config(data)
