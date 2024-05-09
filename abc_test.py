from secrets import token_hex
from time import time
from random import random

# print(token_hex(10))
start = time()


def func(pwd):
    with open(pwd, 'a') as f: f.truncate(0)
    while time() - start < 3:
        d = {token_hex(10): random()}
        with open(pwd, 'a') as f: f.writelines(str(d) + '\n')


func('demo.txt')
