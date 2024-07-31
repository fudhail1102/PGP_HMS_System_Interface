from House import House
from Trees import *
import csv

ProvidentGreenPark_RentSale = Apartment("ProvidentGreenPark")

with open("OwnerData.csv", "r+") as f:
    reader = csv.reader(f)
    x = list(reader)
    currentblock = Block(x[0][1][0])
    ProvidentGreenPark_RentSale.addblock(currentblock)
    currentwing = Wing(int(x[0][1][1]),currentblock)
    currentblock.addwing(currentwing)
    for i in x:
        if i[-1]=="Occupied":
            continue
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
            ProvidentGreenPark_RentSale.addblock(currentblock)
            currentwing = Wing(int(i[1][1]),currentblock)
            currentblock.addwing(currentwing)
            currentwing.addhouse(temp)