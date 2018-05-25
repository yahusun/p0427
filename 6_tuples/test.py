#用小花好把資料放在一起，和list的用法有點像，都是使用（），但是裡面放的不是同一個類型的，但是是和某物相關的

book1 = ("#010", "stone programming", 330)
(id1, title1, price1) = book1

book2 = ("#020", "stone flowers", 1000)
(id2, title2, price2) = book1

print(book1)
print(book1[0], book1[1], book2[2])
print(id1, title1, price1)

arr = [100, 200, 300]
for (idx, val) in enumerate(arr):
    print(idx, val)