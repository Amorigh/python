# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:15:16 2022

@author: sch39270
"""

from matplotlib import pyplot as plt
x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]
plt.scatter(x_values,y_values)
other_x = [1, 2, 3, 4]
other_y = [1, 2, 3, 4]

plt.title("graf")
plt.plot(other_x, other_y)

plt.show()