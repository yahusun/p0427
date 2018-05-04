import sys

def sum_lines():
     for line in sys.stdin:
         line = line.strip()
         print(line)
         tokens = line.split()
         print(tokens)
         print(len(tokens))
#tokens 數字的陣列

         total = 0
         for i in range(0, len(tokens)):
             total += float(tokens[i])
         print(total)

sum_lines()

#變數名稱盡量不要用sum，因為這是python的特殊詞