from House import House
from Trees import *
import csv

ProvidentGreenPark_Rent_1 = Apartment("ProvidentGreenPark")

with open("OwnerData.csv", "r+") as f:
    reader = csv.reader(f)
    x = list(reader)
    currentblock=None
    
    for i in x:
        if i[-1]=="Rent" and i[3]=="1":
            if currentblock==None:
                currentblock = Block(i[1][0])
                ProvidentGreenPark_Rent_1.addblock(currentblock)
                currentwing = Wing(int(i[1][1]),currentblock)
                currentblock.addwing(currentwing)
            temp = House(int(i[2][3:]), int(i[3]), int(i[4]), i[-2], i[1][:1], int(i[1][1:]), i[5], int(i[-3]), i[-5], i[-4],i[-1])
            if i[1][0] == currentblock.RootNode.data:
                if int(i[1][1]) == currentwing.head.data:
                    currentwing.addhouse(temp)
                else:
                    currentwing = Wing(int(i[1][1]),currentblock)
                    currentblock.addwing(currentwing)
                    currentwing.addhouse(temp)
            else:
                currentblock = Block(i[1][0])
                ProvidentGreenPark_Rent_1.addblock(currentblock)
                currentwing = Wing(int(i[1][1]),currentblock)
                currentblock.addwing(currentwing)
                currentwing.addhouse(temp)