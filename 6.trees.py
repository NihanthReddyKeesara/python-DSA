class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
class Tree:
    def __init__(self):
        self.root=None


node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
node7=Node(70)
node8=Node(35)
node9=Node(45)
tr=Tree()
tr.root = node1

node1.r_child=node2
node1.l_child=node3

node2.r_child=node5
node2.l_child=node4

node3.r_child=node7
node3.l_child=node6

if node8.data<node4.data:
    node4.l_child=node8
else:
    node4.r_child=node8

if node9.data>node4.data:
    node4.r_child=node9
else:
    node4.l_child=node9

print(node4.r_child.data)
print(node4.l_child.data)




