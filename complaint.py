from ctypes import py_object

class priority_queue_node:

    def __init__(self,item=None,pr=None):
        self._item=item
        self._priority=pr
        self._next=None

class linked_priority_queue:

    def __init__(self):
        self._front=None

    def isEmpty(self):
        return self._front==None
    
    def queue(self,value,pr):
        if self.isEmpty():
            self._front=priority_queue_node(value,pr)
            return 1
        else:
            if self._front._priority < pr:
                newNode=priority_queue_node(value,pr)
                newNode._next=self._front
                self._front=newNode
                return 1
            else:
                temp=self._front
                while temp._next:
                    if pr >= temp._next._priority:
                        break
                    temp = temp._next
                newNode=priority_queue_node(value,pr)
                newNode._next = temp._next
                temp._next = newNode
                return 1
    
    def dequeue(self):
        if self.isEmpty():
            return
        self._front=self._front._next
        return 1
    
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self._front._item
    
    def traverse(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            temp=self._front
            while temp:
                print(temp._item, end=' ')
                temp=temp._next

    def __str__(self):
        res='['
        temp=self._front
        while temp:
            res+=str(temp._item)+','
            temp=temp._next
        res+=']'
        return res
