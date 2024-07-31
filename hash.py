import csv
class Flatdetail:
    def __init__(self, name, phonenum, status,bhk):
        self.name = name
        self.phonenum = phonenum
        self.status = status
        self.bhk = bhk

    def __str__(self):
        return f"Name: {self.name}, Phone number: {self.phonenum}, Status: {self.status},bhk detail: {self.bhk}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table1 = [None] * size
        self.table2 = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _probe(self, index, attempt):
        return (index + attempt) % self.size
    
    def insert1(self, key, value):
        index = self._hash_function(key)
        attempt=0
        if self.table1[index] is not None:
            attempt += 1
            index = self._probe(index, attempt)
        self.table1[index] = []
        self.table1[index].append(value)

    def insert2(self, key, value):
        index = self._hash_function(key)
        if self.table2[index] is None:
            self.table2[index] = []
        self.table2[index].append(value)

    def get_keys1(self):
        keys1={}
        for item in self.table1:
            if item is not None:
                for val in item:
                    if val.bhk=='1':
                        keys1[val.name]=val.phonenum
        return keys1
    
    def get_keys2(self):
        keys2={}
        for item in self.table1:
            if item is not None:
                for val in item:
                    if val.bhk=='2':
                        keys2[val.name]=val.phonenum
        return keys2
    
    def get_keys3(self):
        keys3={}
        for item in self.table1:
            if item is not None:
                for val in item:
                    if val.bhk=='3':
                        keys3[val.name]=val.phonenum
        return keys3
    
    def get_keys4(self):
        keys4 = {}
        for item in self.table2:
            if item is not None:
                for val in item:
                    keys4[val.name]=(val.phonenum,val.bhk)
        return keys4
