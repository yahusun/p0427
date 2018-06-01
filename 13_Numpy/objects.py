import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
print(arr)
print(arr.ndim)
print(arr.shape)

arr2_x = np.arange(5, 100, 20) #5到100，每20一個點
arr2_y = arr2_x ** 1.2 + 1
print(arr2_x)
print(arr2_y)

arr3_x = np.arange(10, 50, 5)
arr3_y = arr3_x * 2 + 5

arr4_x = np.linspace(0, 10, 21) #21是指0開始到10之間有21個點，包含10那個點，所以每一個距離是0.5
arr4_y1 = arr4_x * 2
arr4_y2 = arr4_x * 3
#print(arr4_x)

#plt.plot(arr2, arr2_1, linestyle= '--', marker='o', color='b')
plt.plot(arr4_x, arr4_y1, '-rv', arr4_x, arr4_y2, '--bo') #'-rv'線段的表示方式，r紅色、v三角形
plt.show()