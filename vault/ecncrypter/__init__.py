import os
import hashlib

def generator(request):
    return hashlib.sha256(request).digest()