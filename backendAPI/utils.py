import random, string
import constants
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from pytz import timezone, all_timezones
from webargs import ValidationError

fmt = "%Y-%m-%d %H:%M:%S"

def generate_hashedPassword(password):
    return pbkdf2_sha256.hash(password)

def verify_hashedPassword(password, hash):
    return pbkdf2_sha256.verify(password, hash)

def generate_db_error():
    return generate_response(0,"UNKNOWN ERROR OCCURED IN DATABASE")

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_current_utc():
    return datetime.now(timezone('UTC'))


def convert_utc_to_timezone_x(time_utc, timezone_x):
    return time_utc.astimezone(timezone(timezone_x))  

def generateExactMatchPattern(inpStr):
    return "^" + inpStr + "$"

def validate_timezone(timezone_x):
    if not timezone_x in all_timezones:
        raise ValidationError("Invalid Timezone.")

def generate_response(VERDICT="0", PAYLOAD=""):
    return {
        constants.response.VERDICT.name: VERDICT,
        constants.response.PAYLOAD.name: PAYLOAD
    }

def return_first_row(data):
    for unit in data:
        return unit