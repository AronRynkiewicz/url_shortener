import random

available_chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


def new_url_generator():
    new_url = ''.join([random.choice(available_chars) for i in range(8)])
    return new_url
