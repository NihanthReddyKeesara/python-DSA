#Doubly linked list

class Node:
    def __init__(self,data):
        self.previous=None
        self.data=data
        self.next=None
        
'''node1=Node(10)
print(node1.previous)
print(node1.data)
print(node1)
print(node1.next)'''

class DoublyLinkedList:
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
         self.head.prev=new_node
         self.head=new_node
         self.head.prev=None

    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        new_node.prev=temp.next
        
    def insert_position(self,position,data):
        new_node=Node(data)
        temp=self.head
        for i in range(0,position-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        new_node.prev=temp.next

    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    def delete_end(self):
        prev =self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

    def delete_position(self,position):
        prev = self.head
        temp=self.head.next
        for i in range(1,position-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
        
        


ob=DoublyLinkedList()
#print(ob)
node1=Node(20)
ob.head=node1
#print(ob.head)
node2=Node(30)
ob.head.next=node2
ob.head.prev=node1
#print(ob.head.data)
#print(ob.head.next)
node3=Node(40)
node2.next=node3
node3.prev=node2
#print(node2.data)
#print(node3.data)
#print(node2)
#print(node3.prev)
node4=Node(50)
node3.next=node4
node4.prev=node3
#print(node4.data)
node5=Node(60)
node4.next=node5
node5.prev=node4
#print(node5.data)
node6=Node(70)
node5.next=node6
node6.prev=node5
print()
print("-----INSERT_BEGIN------")
ob.insert_begining('akhil')
ob.display()
print()
print("-----INSERT_MIDDLE-----")
ob.insert_position(4,'nihanth')
ob.display()
print()
print("-----INSERT_END--------")
ob.insert_end('sriram')
ob.display()
print()
print("-----DELETE_BEGIN-----")
ob.delete_begining()
ob.display()
print()
print("-----DELETE_POSITION---")
ob.delete_position(1)
ob.display()
print()
print("-----DELETE_END-------")
ob.delete_end()
ob.display()
print()


   



