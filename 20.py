startyear = int(input("enter the startyear"))
endyear = int(input("enter the endyear"))


for year in range(startyear,endyear):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
      print ("leap year is :", year)
