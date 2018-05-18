# 請讀取輸入, 建立一個 dictionary 記錄班上的同學名字以及他們對應的歲數.
# 寫一個函數 prAge(name), 如果 name 存在 dictionary, 印出名字和歲數, 否則印出 N/A, 例如: prAge('Bob') 印出 Bob 10, prAge('John') 印出 N/A

ages = {}

def prAge(name):
    if ages.get(name):
        print(name, ages.get(name))
    else:
        print("n/a")

def test():
    num = int(input())
    for i in range(0,num):
        line = input()
        tokens = line.strip().split() #tokens後面是被切割好的字串list
        name = tokens[0]
        age = int(tokens[1])
        ages[name] = age
    print(ages)

    num = int(input())
    for i in range(0, num):
        line = input()
        prAge(line)

test()

#要測試的話需要打python3 dict_age.py < input1.txt ，這樣才會讀到那份字典的資料