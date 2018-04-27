#使用check時，如果有用=給值，這樣後面在check的時候不給值就會直接印出預設值

def check(kg, m=1.8, name="girl"):
     b=bmi(kg, m)
     print (name, "BMI", b)
check(60, 1.5, name="Bob")
check(60, 1.5)
