ages = {}
ages['bob'] = 9
ages['alice'] = 18



#把一大傳上下各以'''分隔時，那一串就先不會被計算

ages['bob']              # 9
print(ages['bob'])
# print(ages.bob)，在Python裡面不可以直接用.去取字典的值
print(ages.get('bob'))
#使用get去找東西的時候，若找不到有錯誤時他會跟你說找不到，而不會出現errow
#  print(ages.get.(John, "N/A")) #或是找不到回傳某值

'''
ages.bob                 # error: 'dict' object has no attribute 'bob'
ages.get('bob')          # 9
ages['john']             # KeyError: 'john'
ages.get('john')         # None
ages.get('john', 'N/A')  # 'N/A'
len(ages)                # 2
list(ages)               # ['bob', 'alice'], order may differ
'bob' in ages            # True
'john' in ages           # False
'''


