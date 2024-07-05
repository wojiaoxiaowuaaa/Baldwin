import numpy as np
import random
import matplotlib.pyplot as plt

position = 0

walk = [position]

steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

# 根据前100个随机漫步值生成的折线图
plt.plot(walk[:100])
plt.show()
