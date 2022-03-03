
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

num = int(input("enter a number"))
if num < 0:
     print("factorial cannot be negative")
elif num == 0:
     print("factorial is 1")
else:
        print("factorial", num, "is", factorial(num))





