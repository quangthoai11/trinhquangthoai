# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:17:10 2024

@author: Student
"""
import random
cau_1= random.randint(20,30)
cau_2= [random.uniform(18,99)**2 for i in range(cau_1)]
print(f"Số lượng phần tử được chọn ngẫu nhiên: {cau_1}")
print("Các giá trị bình phương được chọn ngẫu nhiên:")
for i in cau_2:
    print(f"{i:.2f}")