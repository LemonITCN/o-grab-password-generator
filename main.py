import hmac
import json
import sys

PASSWORD_KEY = '33854053'
PASSWORD_FILE = 'password.lem'
PASSWORD_FIELD = 'secret'


def generate_password_secret(password):
    secret = PASSWORD_KEY.encode('utf-8')
    data = password.encode('utf-8')
    signature = hmac.new(secret, data, digestmod='SHA256').hexdigest()
    with open(PASSWORD_FILE, "w") as dump_f:
        json.dump({PASSWORD_FIELD: signature}, dump_f)


generate_password_secret(sys.argv[1])
