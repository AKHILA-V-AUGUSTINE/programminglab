a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
op = input("enter any operator")

if op == "+":
    print(a+b)
elif op == "-":
    if a > b:
        print(a-b)
    else:
        print(b-a)
elif op == "*":
    print(a*b)
elif op == "/":
    if a > b:
     print(a/b)
    else:
     print(b/a)
else:
    print("Invalid operation")


