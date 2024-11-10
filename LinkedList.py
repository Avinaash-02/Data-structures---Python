class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.value=new_node
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
            self.head=new_node
        self.length+=1
        return True
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        prev=self.head
        while(temp.next):
            prev=temp
            temp=temp.next

        self.tail=prev
        self.tail.next=None
        self.length-=1

        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    def insert(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

sll=LinkedList(4)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.print_list()
