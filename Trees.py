from abc import ABC, abstractmethod
from House import House

class Tree(ABC):

    @abstractmethod
    def root(self):
        pass
    
    @abstractmethod
    def parent(self, pos):
        pass
    
    @abstractmethod
    def __len__(self):
        pass

    def isroot(self, pos):
        return pos == self.root()
    
    def isleaf(self, pos):
        return self.childquantity(pos) == 0
    
    def NodeDepth(self, pos):
        if self.isroot(pos):
            return 0
        return 1 + self.NodeDepth(self.parent(pos))

    def NodeHeight(self, pos):
        if self.isleaf(pos):
            return 0
        return 1 + max(self.NodeHeight(child) for child in self.children(pos))
    
    def is_empty(self):
        return len(self) == 0 
    
    def Height(self, pos=None):
        if pos is None:
            if self.is_empty():
                return -1  # By convention, height of an empty tree is -1
            pos = self.root()
        return self._heightN(pos) 

class Node:
    def __init__(self, data=None,parentblock=None):
        self.data = data
        self.next = None
        self.prev = None
        self.parent=parentblock

class Wing:
    def __init__(self, wingno: int,parentblock):
        self.head = Node(wingno,parentblock)
        self.tail = None
        self.size = 0
        self.block=parentblock

    def is_empty(self):
        return self.head.next is None

    def addhouse(self, house: House):
        new_house = Node(house,self.block)
        if self.is_empty():
            self.head.next = new_house
            new_house.prev = self.head
            self.tail = new_house
        else:
            new_house.prev = self.tail
            self.tail.next = new_house
            self.tail = new_house
        self.size += 1

    def delete(self, data):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return
        current = self.head.next
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next
        print(f"Item {data} not found in the list.")
        self.size -= 1

    def search(self, data):
        if self.is_empty():
            print("List is empty. Nothing to search.")
            return
        current = self.head.next
        while current:
            if current.data == data:
                return current
            current = current.next
        return -1

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.head.data)
    
    def traverse(self):
        pos = self.head.next
        while pos is not None:
            yield pos.data.get_all_details()
            pos = pos.next

    def traverseHouse(self):
        pos = self.head.next
        while pos is not None:
            yield pos.data
            pos = pos.next
class Block(Tree):

    class BlockNode:
        def __init__(self, ele, prnt=None, child=None, sibling=None):
            self.data = ele
            self.Parent = prnt
            self.child = child
            self.sibling = sibling

    def __init__(self, blockname: str):
        self.RootNode = self.BlockNode(blockname)
        self.size = 0

    def addwing(self, wing):
        NewWing = self.BlockNode(wing, self.RootNode)
        if self.RootNode.child is None:
            self.RootNode.child = NewWing
        else:
            pos = self.RootNode.child
            while pos.sibling is not None:
                pos = pos.sibling
            pos.sibling = NewWing
        self.size += 1

    def root(self):
        return self.RootNode

    def parent(self, pos):
        return pos.Parent

    def __len__(self):
        return self.size

    def housequantity(self):
        current = self.RootNode.child
        houses = 0
        while current is not None:
            houses += len(current.data)
            current = current.sibling
        return houses

    def houseinfo(self):
        current = self.RootNode.child
        while current is not None:
            print("Wing Number:", current.data.head.data)
            for i in current.data.traverse():
                print(i)
            current = current.sibling
        if current is None:
            pass
    
    def get_children_wings(self):
        children_wings = []
        current = self.RootNode.child
        while current is not None:
            children_wings.append(current.data)
            current = current.sibling
        return children_wings

class Apartment():
    def __init__(self,name):
        self.Name=name
        self.__blocks=[]
    
    def addblock(self,block:Block):
        self.__blocks.append(block)
    
    def blockinfo(self,block):
        if isinstance(block,Block):
            target=self.__blocks[self.__blocks.index(block)]
            print("Block : ",target.RootNode.data)
            print("Number of Wings in the block : ",len(target))
            target.houseinfo()
        else:
            for i in self.__blocks:
                if i.RootNode.data==block:
                    return i
        
    def get_blocks(self):
        return self.__blocks
    
    def get_house(self):
        for i in self.__blocks:
            for j in i.get_children_wings():
                for k in j.traverseHouse():
                    yield k