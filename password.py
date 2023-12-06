import random
import string

class Password:
    def __init__(PASS, charsets):
        PASS.charsets = charsets
        
    def generate(PASS, length):
        password = []
        for charset in PASS.charsets:
            password.append(random.choice(charset))
        while len(password) < length:
            charset = random.choice(PASS.charsets)
            password.append(random.choice(charset))
        random.shuffle(password)
        return ''.join(password)
