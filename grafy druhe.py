# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:06:14 2022

@author: sch39270
"""
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("default")
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

x_indexes = np.arange(len(ages_x))
width = 0.25




plt.bar(x_indexes + width, js_dev_y, width = width, color = "#f702df", label = "Javascript devs")

plt.bar(x_indexes, py_dev_y, width = width, color = "#02f716", label = "Python devs")

plt.bar(x_indexes - width, dev_y, width = width, linestyle = "--", color = "#2302f7", label = "All devs")


plt.xticks(ticks = x_indexes, labels = ages_x)
plt.xlabel("Věk")
plt.ylabel("Medián mezd")
plt.title("Medián platů dle věku")


plt.savefig("obr_z_kodu.png")
plt.grid(color = "lightgray")
plt.legend()
plt.show()

