import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# start process
fr = open("number.txt", "r")    # อ่านค่าประวัติ
v_lotto = list([])  # keep lotto
for i in fr.readlines():
    v_lotto.append(int(i[:-1]))

v_lotto.reverse()

##@@ demo
# result = []
# for i in range(len(v_lotto)-1):
#     single_value = v_lotto[i] - v_lotto[i+1]
#     if single_value < 0:
#         single_value *= (-1)
#     result.append(single_value)

# v_lotto = result

# for i in v_lotto:
#     print(i)
##@@ demo

lotto = np.array(v_lotto)  # แปลงเป็นประเภท array
number = np.arange(len(lotto))  # แปลงเป็นประเภท array
lotto = lotto.reshape(-1, 1)
number = number.reshape(-1, 1)

# 476
x_train, x_test = number[:390], number[390:]  # แยกข้อมูลสำหรับ train & test
y_train, y_test = lotto[:390], lotto[390:]   # แยกข้อมูลสำหรับ train & test

# model train
model = LinearRegression()
model.fit(number, lotto)

##@@ demo
# predit demo
from sklearn.metrics import accuracy_score
y_predit = model.predict([[len(lotto)+1]])
print(int(y_predit))
##@@ demo

# import math
# for i in range(len(y_predit)):
#     y_predit[i][0] = math.ceil(y_predit[i][0])

# print("accuracy_score=",accuracy_score(y_test, y_predit)*100)
# print(len(v_lotto))
# predit
# point = len(lotto) + 1
# y_predit = model.predict([[point]])

# print("Number [", point, "] = ", y_predit)

# input("done")