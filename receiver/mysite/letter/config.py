from dotenv import load_dotenv
import os


# Enviornment variables
load_dotenv()

ENV = os.environ

EMAIL = ENV['EMAIL']
PASSWORD = ENV['PASSWORD']

NAME = ENV['NAME']
BIRTH = ENV['BIRTH']
ENTER_DATE = ENV['ENTER_DATE']
UNIT_NAME = ENV['UNIT_NAME']

# Others
SUCCESS_DIRECTORY = '/letters/'
FAILED_DIRECTORY = '/letters/failed/'

RECENT_LETTERS = 10
