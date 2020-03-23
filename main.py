import hmac
import json

PASSWORD_KEY = '33854053'
PASSWORD_FILE = 'password.lem'
PASSWORD_FIELD = 'secret'


def generate_password_secret(password):
    secret = PASSWORD_KEY.encode('utf-8')
    data = password.encode('utf-8')
    signature = hmac.new(secret, data, digestmod='SHA256').hexdigest()
    with open(PASSWORD_FILE, "w") as dump_f:
        json.dump({PASSWORD_FIELD: signature}, dump_f)


generate_password_secret(input('请输入密码（输入后按回车键生成密钥文件）:'))
print('密码文件生成成功：', PASSWORD_FILE)
