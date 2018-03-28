#-*- coding: utf-8 -*-
import base64
import chilkat
from Crypto.Cipher import DES3
import hashlib


class DecodeJson(object):

    def __init__(self,source_str):
        self.source_str = source_str

    def decodeData(self):
        #解码key固定值
        secret_key = "JadK34ZtQDI0lP7cSupU0DKP"
        #base64解码，服务器返回的message进行了base64编码
        message = base64.decodestring(self.source_str)
        #DES3解码，解码模式是ECB
        des3 = DES3.new(secret_key, DES3.MODE_ECB)
        json_data = des3.decrypt(message)
        return json_data

if __name__=='__main__':
    pass
    '''source_str = "C9yFmGfUJyJ/vTXaKfJx3c+cRNlU3zoiZDmEkPRmmoLHp0zZNGNOqTj6t+3MOYCCk3lh2dynORmTOUFKa7a4mN4i4hGA+2k0yDTX151G+skUhaSVpX1" \
    "RfpYIyVQGy2cAPBxAAuk5fXDcgfy/ZI72R9iWB6WK7QUj5ypS4MT9TkFAnOSQgnyENKByKFd0cKVjCNy6hB7SP/3q7B08d2UHekvTkcRmwuQO1FI9xNqYf" \
    "qXp3ihIgwEZc13nmJEthnGW00JEkLN6xq5R+pfV3LdZqmK4KF1G+RDe57gbrk9Nkv7kkILg8peX2Au5wCwtFqOy93cDULDaQyvmUFnsSAFRfOU+7J9CwqQt" \
    "d8hiH8YEGhfmUFnsSAFRfKUK0uhwSSWJH+nLyxA5emQuMXCrA6VLFsmbugV7jVJ/23Enh3NMmsxulmkVm0oQqCUyxm5whO8vYAytyaRh4e/7cvOxZa2wrVri4T" \
    "k39ZeqqyOXHTSxUNHj/E6L5yI4OC8oaF0kLyy5k+HkdC10sBCbql19yfS5HyO2gpqb8rLA61pkFXdZNGw+FAVrvj9cJPf4D7Z/RYBpu7kaySzsbAVHqbjSwXR4Kq" \
    "yiTdBDV8Gt+CdtOftkusbiyZNPPWqYV0qLbe+oID9wjmgLjQi5sp+p4QI8zVTG9TXIk2qbJL/kaxCeEN5PcBUIMYPhO1P0kctYcvCTtNpMC5fA09fHiH5wUCP0r/" \
    "XPnQXStmEt3cUvZUZVy6hs9Q8M3e0joMHvvZ/YdZWv6hluabOccyxihace8+yV+TsB61Y6UF0hPzLsYoVu31H+dDZnFFkwj+7n8qUK0uhwSSWJH+nLyxA5emQuMXCr" \
    "A6VLFntZ0f0g7JFCAMz7rduGTIOTQ0ukekHVBA/Z6giTXu1eUpVTAHROTeFrapkbgHdEBEEhzM1KFsczOsTBEbYhjz4DXPNe57DssWm1BhFOermV"

    message = base64.decodestring(source_str)

    secret_key = "JadK34ZtQDI0lP7cSupU0DKP"

    des3 = DES3.new(secret_key,DES3.MODE_ECB)
    res2 = des3.decrypt(message)
    print res2'''