lst=[]
def push_element():

    if len(lst)==n:
        print("Stack is full")
    else:
        element=input('enter the element for stack:')
        lst.append(element)
        print(lst)


def pop_element():

    if not lst:
        print("stack is empty, add the element")
    else:
        e=lst.pop()
        print(e,"removed")
        print(lst)

def display():
    print(lst)
    
    


n=int(input("Enter the size of stack:"))
while True:
    print('select the operatio 1.push 2.pop 3.quit 4.display')
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    elif choice==4:
        display()
    else:
        print("Enter the valid choice")
