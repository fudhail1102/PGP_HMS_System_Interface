import csv
import ApartmentStructure as AS
HashTable={}
with open("OwnerData.csv", "r+") as f:
    reader = csv.reader(f)
    for i in reader:
        HashTable[(i[6],i[7])]=[x for x in AS.ProvidentGreenPark.get_house() if (x.get_username(),x.get_password())==(i[6],i[7]) ][0]