import numpy as np
'''
def table (m,n):
    arr=[]
    for i in range(0,m):
        arr.append([1,2,3])
    return np.array(arr)
'''
def test():
    arr = [
        [1,2,3],
        [4,5,6]
    ]
    print(arr)
    nparr = np.array(arr)
    print(nparr.ndim)
    print(nparr.shape)

def table(m,n):
    arr = []
    for i in range(1,m+1):
        sub = []
        for j in range(1,n+1):
            sub.append(i*j)
        arr.append(sub)
    return arr

def test2():
    nparr = table(4,5)
    print(nparr)


test()