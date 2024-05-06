import os

res = os.listdir('.')

res = [i for i in res if os.path.isfile(i)]

for i in res:
    print(i)