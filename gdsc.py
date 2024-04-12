def KanbanBoard():
    bno=int(input("Enter Board Number: "))
    def addTasks():
        global todo,count
        if(bno<=count):
            while(True):
                global i
                task=input("\nEnter task: ")
                todo[bno-1].append(task)
                cin=input("Do you want to add more tasks(y/n)").lower()
                if(cin=='n'):break
            print(todo[bno-1],"\t",prog[bno-1],"\t",done[bno-1],"\n")
        else:
            print("Invalid Board Number")

    def moveTasks():
        global j,k,count
        j=k=0
        if(bno<=count):
            print("Enter the from_status, to_status and position of task\n")
            from_status=input().lower()
            to_status=input().lower()
            pos=int(input())
            global todo,prog,done
            if(from_status=='to do' and to_status=='in progress'):
                prog[bno-1].append(todo[bno-1].pop(pos - 1))
                j+=1
            elif(from_status=='in progress' and to_status=='done'):
                done[bno-1].append(prog[bno-1].pop(pos - 1))
                k+=1
            print(todo[bno-1],"\t",prog[bno-1],"\t",done[bno-1],"\n")
        else:
            print("Invalid Board Number")

    def deleteTasks(bno,from_status,pos):
        global count
        if(bno<=count):
            if(from_status=='to do'): 
                todo[bno-1].pop(pos-1)
            elif(from_status=='in progress'): 
                prog[bno-1].pop(pos-1)
            else: 
                done[bno-1].pop(pos-1)
            print(todo[bno-1],"\t",prog[bno-1],"\t",done[bno-1],"\n")
        else:
            print("Invalid Board Number")

    def view():
        global count
        if(bno<=count):
            print("TO DO\tIN PROGRESS\tDONE")
            print(todo[bno-1],"\t",prog[bno-1],"\t",done[bno-1],"\n")
        else:
            print("Invalid Board Number") 

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

todo=[]
prog=[]
done=[]
count=1
bno=1
while True:
    c=input("Do you want to create a new board? (y/n)").lower()
    if(c=='y'):
        KanbanBoard()
        count+=1
    else:
        c1=input("Do you want to work on existing board?(y/n)").lower()
        if(c1=='y'):
            KanbanBoard()
        else:
            print("Thank you, exiting...")
            break