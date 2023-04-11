import random


def random_str(n):
    return (''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()-_=+'))
                    for _ in range(n)]))
