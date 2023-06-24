list1=[]
size=int(input("Enter the list size:"))


def insert():
    for i in range(0,size+1):
        num=input("Enter input:")
        list1.append(num)
        


def delete():
    del1=int(input("Enter the index where u want to delete:"))
    list1.pop(del1)


def sort():
    list1.sort()


def quite():
    print("program terminated")
    

def display():
    print(list1)

     
while (True):

    print("1.Insert")
    print("2.delete")
    print("3.search")
    print("4.sort")
    print("5.quite")
    print("6.Display")

    choice=int(input("Enter your choice:"))

    if(choice==1):
        insert()
    elif(choice==2):
        delete()
    elif(choice==3):
        search()
    elif(choice==4):
        sort()
    elif(choice==5):
        quite()
    elif(choice==6):
        display()
    else:
        print('invalid input')

   
    
