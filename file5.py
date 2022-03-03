import csv
file_name=['no','company','car model']
car=[{'no':1,'company':'TATA','car model':'nano'},
{'no':1,'company':'TATA','car model':'nano'},
{'no':2,'company':'BMW','car model':'nx10'},
{'no':3,'company':'Toyota','car model':'nano'},
{'no':4,'company':'jeep','car model':'jeep'}]
with open('s.csv','w') as csvfile:
 writer=csv.DictWriter(csvfile,file_name)
 writer.writeheader()
 writer.writerows(car)
with open('s.csv','r') as csvfile:
    d=csv.reader(csvfile,delimiter='|')
    for r in d:
      print(','.join(r))