#-*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
from numpy.random import *
import numpy as np
import scipy.stats as stats
import pandas
import matplotlib.pyplot as plt

normal = randn(1000) # 標準正規分布に従う乱数を1000個生成
comparison = rand(1000) #比較のため乱数を1000個生成

plt.hist(normal, bins=100)
filename="hist.png"
plt.savefig(filename)
plt.show()
