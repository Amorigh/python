# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:34:38 2022

@author: sch39270
"""

#student = {"name": "John","age": 25, "courses": ["Math", "CompSci"]}


"""
student = {"name": "John","age": 25, "courses": ["Math", "CompSci"]}
print(student["name"])

s_student = ["John", 25, "Math a CompSci"]
print(s_student[1])
"""
"""
student["age"] = 37
print(student)
"""
"""
student["Hobby"] = ["Gauching"]
student["Team"] = "Gryffindor"
print(student)

#for hodnota in student:
 #   print(hodnota)

for klic, hodnota in student.items():
     print(klic, hodnota)

#for hodnota in student.values():
 #   print(hodnota)

#for klic in student.keys():
 #   print(klic)    
"""
keys = ["Martin", "Karel", "Pavel"]
values = ["AJ", "NJ", "FJ"]
data = dict(zip(keys, values))
print(data)
