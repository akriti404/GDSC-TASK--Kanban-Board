def addTasks():
    global todo,count
    bno=int(input("Enter Kanban Board number: "))
    if(bno<count):
        while(True):
            global i
            task=input("\nEnter task: ")
            todo[bno].append(task)
            cin=input("Do you want to add more tasks(y/n)").lower()
            if(cin=='n'):break
        print(todo,prog,done)
    else:
        print("Invalid Board Number")

def moveTasks():
    global j,k,count
    j=k=0
    if(bno<count):
        bno=int(input("Enter Kanban Board number: "))
        print("Enter the from_status, to_status and position of task\n")
        from_status=input().lower()
        to_status=input().lower()
        pos=int(input())
        global todo,prog,done
        if(from_status=='to do' and to_status=='in progress'):
            prog[bno].append(todo[bno].pop(pos - 1))
            j+=1
        elif(from_status=='in progress' and to_status=='done'):
            done[bno].append(prog[bno].pop(pos - 1))
            k+=1
        print(todo,prog,done)
    else:
        print("Invalid Board Number")

def deleteTasks(bno,from_status,pos):
    global count
    if(bno<count):
        if(from_status=='to do'): 
            todo[bno].pop(pos-1)
        elif(from_status=='in progress'): 
            prog[bno].pop(pos-1)
        else: 
            done[bno].pop(pos-1)
        print(todo,prog,done)
    else:
        print("Invalid Board Number")

def view():
    global count
    if(bno<count):
        bno=int(input("Enter Kanban Board number: "))
        print("TO DO\tIN PROGRESS\tDONE")
        print(todo[bno],"\t",prog[bno],"\t",done[bno],"\n")
    else:
        print("Invalid Board Number")

todo=[[]]
prog=[[]]
done=[[]]
count=0
while(True):
    print("\nMENU:")
    print("0.Create a Kanban Board")
    print("1.Add Tasks")
    print("2.Move Tasks")
    print("3.Delete Tasks")
    print("4.View Board")
    print("5.Exit\n")
    choice=int(input())
    if(choice==0):
        count+=1
    if(choice==1):
        addTasks()
    elif(choice==2):
        moveTasks()
        c=input("Do you want to move more tasks? (y/n)").lower()
        if(c=='y'):
            moveTasks()
        else:
            continue
    elif(choice==3):
        bno=int(input("Enter Kanban Board number: "))
        FROM=input("Enter from_status")
        position=int(input("Enter position of task"))
        deleteTasks(bno,FROM,position)
        c=input("Do you want to delete more tasks? (y/n)").lower()
        if(c=='y'):
            FROM=input("Enter from_status: ")
            position=int(input("Enter position of task: "))
            deleteTasks(bno,FROM,position)
        else:
            continue
    elif(choice==4):
        view()
    else:
        break  