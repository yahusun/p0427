#list:  stud = [20045, 33048, 84203]
#sets和dict很像，都是{}，但是dict有一個字和對應的值，sets就只有字用,隔開
zooA = {'elephant', 'tiger', 'lion', 'giraffe', 'leopard', 'antelop'}
zooB = {'lion', 'cheetah', 'giraffe', 'zebra', 'wildebeest', 'elephant'}

print("zoo A:", zooA)
print("zoo B:", zooB)
print("zoo A and zoo B:", zooA & zooB) #共同有的
print("zoo A or zoo B:", zooA | zooB) #A和B有的
print("zoo A - zoo B:", zooA - zooB) #
print("zoo A xor zoo B:", zooA ^ zooB) #