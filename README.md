# GDSC-TASK--Kanban-Board
def addTasks():
    global todo
    while(True):
        global i
        task=input("\nEnter task: ")
        todo.append(task)
        cin=input("Do you want to add more tasks(y/n)").lower()
        if(cin=='n'):break
    print(todo,prog,done)

def moveTasks():
    global j,k
    j=k=0
    print("Enter the from_status, to_status and position of task\n")
    from_status=input().lower()
    to_status=input().lower()
    pos=int(input())
    global todo,prog,done
    if(from_status=='to do' and to_status=='in progress'):
        prog.append(todo.pop(pos - 1))
        j+=1
    elif(from_status=='in progress' and to_status=='done'):
        done.append(prog.pop(pos - 1))
        k+=1
    print(todo,prog,done)

def deleteTasks(from_status,pos):
    if(from_status=='to do'): 
        todo.pop(pos-1)
    elif(from_status=='in progress'): 
        prog.pop(pos-1)
    else: 
        done.pop(pos-1)
    print(todo,prog,done)

def view():
    print("TO DO\tIN PROGRESS\tDONE")
    print(todo,"\t",prog,"\t",done,"\n")

todo=[]
prog=[]
done=[]
while(True):
    print("\nMENU:")
    print("1.Add Tasks")
    print("2.Move Tasks")
    print("3.Delete Tasks")
    print("4.View Board")
    print("5.Exit\n")
    choice=int(input())
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
        FROM=input("Enter from_status")
        position=int(input("Enter position of task"))
        deleteTasks(FROM,position)
        c=input("Do you want to delete more tasks? (y/n)").lower()
        if(c=='y'):
            FROM=input("Enter from_status: ")
            position=int(input("Enter position of task: "))
            deleteTasks(FROM,position)
        else:
            continue
    elif(choice==4):
        view()
    else:
        break


    
