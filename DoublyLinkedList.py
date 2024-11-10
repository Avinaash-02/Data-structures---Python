class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class doubly_linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.value=value
        self.length=1
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True

    def get(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next

        new_node.prev=before
        new_node.next=after
        after.next=new_node
        before.prev=new_node
        self.length+=1
        return True
my_DLL=doubly_linked_list(4)
my_DLL.append(4)
my_DLL.append(5)
my_DLL.append(6)
my_DLL.append(8)
my_DLL.append(9)
my_DLL.insert(2,32)
my_DLL.print_list()
