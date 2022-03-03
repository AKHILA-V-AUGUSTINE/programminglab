str1=input("enter the word")
print("original word",str1)
new=str1[0]
a=str1.replace(new,"$")
new=new+a[1:]
print("replace word",new)
