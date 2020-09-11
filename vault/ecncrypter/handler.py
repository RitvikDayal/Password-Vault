import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

def encrypt_obj(key, user, init):
    '''
    key: key for AES
    user: username
    initializer: initialzing vector
    '''
    if init == None:
        init = Random.new().read(AES.block_size).decode('cp1252').encode().decode()
        os.environ[user.upper()+'_IV'] = init
    return AES.new(key, AES.MODE_CBC, init.encode('cp1252'))

def encrypt(en_obj, request):
    '''
    key: key for AES
    request: password that need to be encrypted
    user: username
    init: initialzing vector
    '''
    return en_obj.encrypt(pad(request, AES.block_size))

def decrypt(key, request, user, init):
    '''
    key: key for AES
    request: password that need to be encrypted
    user: username
    init: initialzing vector
    '''
    return unpad(encrypt_obj(key, user, init).decrypt(request), AES.block_size).decode()