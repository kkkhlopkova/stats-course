# -*- coding: utf-8 -*-
"""
Вышмат ДЗ 2

Хлопкова Ксения

Максимально лаконичный код, который осуществляет построение ядерной оценки плотности (KDE) для заданной выборки.
"""

sample = [1, 3, 4, 4, 4, 4, 6, 8, 9, 12, 13, 13, 15, 16, 19, 20, 20, 20]
sample.sort()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# создаем математическую функцию
f_hat = gaussian_kde(sample)

# создаем график
x = np.linspace(0, 20, 200)
plt.plot(x, f_hat(x))

