import numpy as np
'''
mat1 = np.zeros((3,4)) #3*4的矩陣
print(mat1)
print(mat1.ndim)
print(mat1.shape)

mat2 = np.ones((2,3)) * 2
mat2_2 = mat2 * 2
mat2_3 = mat2 * mat2_2

print(mat2)
print(mat2_2)
print(mat2_3)

#對角矩陣
mat3 = np.eye(3,4)
print(mat3)

#真的矩陣運算
#print(np.matmul(mat2, mat3))

'''

#亂數矩陣
import matplotlib.pyplot as plt

arr_x = np.arange(10)
a = np.random.rand(10)                 # uniform in [0, 1]，不會等於1
b = np.random.randint(5, 10, 10)      # uniform in [5, 10] with 10 elements
plt.plot(arr_x, a, '-r^', arr_x, b, '--go')
plt.show()
