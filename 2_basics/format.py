def prStr():
    s = "num1: {0} num2: {1}".format(100, 200)
    print(s)
    s = "{0:<10} {1:<10} {2:<10}".format("apple", "banana", "grape")
    print(s)
    s = "{0:>10.2f}".format(3.1415926)
    print(s)
    s = "{0:^10.2f}".format(3.1415926)
    print(s)

prStr()