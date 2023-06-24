lst=[]

def enqueue():
    if len(lst)==size:
        element=input("Enter the element into queue:")
        lst.append(element)
        print(lst)

def dequeue():
    if not lst:
        print("Queue is empty ,add element")
    else:
        #lst.pop()  
        print(lst)

def display():
    print(lst)
    


size=int(input())
while True:

    print("Enter your choice 1.enqueue 2.dequeue 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct choice")
        
    
