print("hello  hello")
#跑程式：在終端機打-> python3 檔案名稱
print("yahsuan", sep="s", end="&")
print("get a life, my friend")

print(101%10)
#不需要先設變數，可以直接使用
a=1
b=2
c=a+b-4
print(c)

str1 = "it's not really easy..."
print(str1)
print(len(str1))
#len是字串的長度
print(str1[2])
print(str1[6:8])
print(str1[10:])
print(str1[:6])
print(str1[:])
print(str1[::-1])
#[]是取值，：可以有特殊功能

print("{0} {1}".format(100,200))
print("num1: {0} num2: {1}".format(a, b))
print("{0:10}{1:10}".format(200, 300))
print("{0:<7}{}")
#不懂

s = "Stone Campus"
#這個字串的長度
print(len(s))
#位置6的字母（使用[]）
print(s[6])
# 從位置3到9的子字串"no camp"
print(s[3:10])
