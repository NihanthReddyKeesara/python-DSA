class BST:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            return
        if self.key == data:
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
          if self.key < data:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
    def pre_order(self):
        print(self.key,end="-->")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
    def in_order(self):
      if self.l_child:
        self.l_child.in_order()
      print(self.key,end="-->")
      if self.r_child:
        self.r_child.in_order()
    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key,end="-->")

    def delete(self,data):
      if self.key is None:
        print("Tree is Empty") 
      else:
        if data<self.key:
          if self.l_child:
            self.l_child = self.l_child.delete(data)
          else:
            print("Given Node is Not Present in the tree")
        elif data>self.key:
          if self.r_child:
             self.r_child = self.r_child.delete(data)
          else:
            print("Given Node is Not Present in the tree")
        else:
          if self.l_child is None:
            temp=self.r_child
            self=None
            return temp
          if self.r_child is None:
            temp=self.l_child
            self=None
            return temp
          node=self.r_child
          while node.l_child:
            node=node.l_child
          self.key=node.key
          self.r_child = self.r_child.delete(node.key)
      return self
root=BST(45)
root.insert_node(30)
root.insert_node(25)
root.insert_node(50)
root.insert_node(31)
root.insert_node(49)
root.insert_node(51)
root.insert_node(24)
root.insert_node(26)
x=root.pre_order()
print("")
root.in_order()
print("")
root.post_order()
print("")
root.delete(49)
print(" ")
root.post_order()
print("")
