# area of a square
a=int(input("enter the sides of a square"))
area=lambda c:a*a
print("area of square is:",area(a))

# area of a rectangle
l=int(input("enter the length"))
b=int(input("enter the breadth"))
x=l*b
arearect=lambda r:x
print("area of rectangle is:",arearect(x))

#area of triangle
base=int(input("enter the base length"))
h=int(input("enter the height"))
triarea =1/2*base*h
triangle=lambda t:triarea
print("area of a triangle is:",triangle(triarea))

