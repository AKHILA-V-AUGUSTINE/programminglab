list1 = []
n = int(input("enter the integer number"))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
    print(list1)
    result = []
    for i in list1:
        if i > 100:
            result.append("over")
        else:
             result.append(i)
             print(result)