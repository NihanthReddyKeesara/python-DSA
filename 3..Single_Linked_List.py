
#Single Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        
    def insert_position(self,position,data):
        new_node=Node(data)
        temp=self.head
        for i in range(0,position-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        prev =self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def delete_position(self,position):
        prev = self.head
        temp=self.head.next
        for i in range(0,position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        
        
        
        
        
        

obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
n6=Node(70)
n5.next=n6
n7=Node(80)
n6.next=n7
print()
print("-----INSERT_BEGIN------")
obj.insert_begining('akhil')
obj.display()
print()
print("-----INSERT_MIDDLE-----")
obj.insert_position(4,'nihanth')
obj.display()
print()
print("-----INSERT_END--------")
obj.insert_end('sriram')
obj.display()
print()
print("-----DELETE_BEGIN-----")
obj.delete_begining()
obj.display()
print()
print("-----DELETE_END-------")
obj.delete_end()
obj.display()
print()
print("-----DELETE_POSITION---")
obj.delete_position(3)
obj.display()
print()


                
