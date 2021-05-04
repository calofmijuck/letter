import os

from dotenv import load_dotenv

DOTENV_PATH = "/env/.env"

# Enviornment variables
load_dotenv(dotenv_path=DOTENV_PATH)

ENV = os.environ

EMAIL = ENV['EMAIL']
PASSWORD = ENV['PASSWORD']

NAME = ENV['NAME']
BIRTH = ENV['BIRTH']
ENTER_DATE = ENV['ENTER_DATE']
UNIT_NAME = ENV['UNIT_NAME']
