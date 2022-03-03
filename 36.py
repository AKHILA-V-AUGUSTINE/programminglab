def factor(num):
    print("number is",num)
    for i in range(1,num+1):
        if num % i==0:
            print(i)
        i = i+1

num = int(input("enter a number"))
factor(num)

