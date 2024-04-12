def KanbanBoard(board_num):
    global todo, prog, done

    def addTasks():
        global board_num
        if board_num <= len(todo):
            while True:
                task = input("\nEnter task: ")
                priority = input("Enter priority (high/medium/low): ").lower()
                todo[board_num - 1].append((task, priority))
                cin = input("Do you want to add more tasks(y/n)").lower()
                if cin == 'n':
                    break
            print(todo[board_num - 1], "\t", prog[board_num - 1], "\t", done[board_num - 1], "\n")
        else:
            print("Invalid Board Number")

    def moveTasks():
        global board_num
        if board_num <= len(todo):
            print("Enter the from_status, to_status and position of task\n")
            from_status = input().lower()
            to_status = input().lower()
            pos = int(input())
            if from_status == 'to do' and to_status == 'in progress':
                if len(todo[board_num - 1]) > 0:
                    prog[board_num - 1].append(todo[board_num - 1].pop(pos - 1))
            elif from_status == 'in progress' and to_status == 'done':
                if len(prog[board_num - 1]) > 0:
                    done[board_num - 1].append(prog[board_num - 1].pop(pos - 1))
            print(todo[board_num - 1], "\t", prog[board_num - 1], "\t", done[board_num - 1], "\n")
        else:
            print("Invalid Board Number")

    def deleteTasks(from_status, pos):
        global board_num
        if board_num <= len(todo):
            if from_status == 'to do':
                if len(todo[board_num - 1]) > 0:
                    todo[board_num - 1].pop(pos - 1)
            elif from_status == 'in progress':
                if len(prog[board_num - 1]) > 0:
                    prog[board_num - 1].pop(pos - 1)
            else:
                if len(done[board_num - 1]) > 0:
                    done[board_num - 1].pop(pos - 1)
            print(todo[board_num - 1], "\t", prog[board_num - 1], "\t", done[board_num - 1], "\n")
        else:
            print("Invalid Board Number")

    def view():
        global board_num
        if board_num <= len(todo):
            sorted_todo = sorted(todo[board_num - 1], key=lambda x: ('high', 'medium', 'low').index(x[1]))
            print("TO DO\tIN PROGRESS\tDONE")
            print(sorted_todo, "\t", prog[board_num - 1], "\t", done[board_num - 1], "\n")
        else:
            print("Invalid Board Number")

    while True:
        print("\nMENU:")
        print("1.Add Tasks")
        print("2.Move Tasks")
        print("3.Delete Tasks")
        print("4.View Board")
        print("5.Change Board")
        print("6.Exit\n")
        choice = int(input())
        if choice == 1:
            addTasks()
        elif choice == 2:
            moveTasks()
            c = input("Do you want to move more tasks? (y/n)").lower()
            if c == 'y':
                moveTasks()
            else:
                continue
        elif choice == 3:
            FROM = input("Enter from_status")
            position = int(input("Enter position of task"))
            deleteTasks(FROM, position)
            c = input("Do you want to delete more tasks? (y/n)").lower()
            if c == 'y':
                FROM = input("Enter from_status: ")
                position = int(input("Enter position of task: "))
                deleteTasks(FROM, position)
            else:
                continue
        elif choice == 4:
            view()
        elif choice == 5:
            new_board_num = int(input("Enter Board Number: "))
            if new_board_num > 0 and new_board_num <= len(todo):
                board_num = new_board_num
                print("Switched to Board", board_num)
            else:
                print("Invalid Board Number")
        else:
            break

todo = [[]]
prog = [[]]
done = [[]]

while True:
    c = input("Do you want to create a new board? (y/n)").lower()
    if c == 'y':
        todo.append([])
        prog.append([])
        done.append([])
    else:
        c1 = input("Enter 'y' to continue and 'n' to exit").lower()
        if c1 == 'y':
            board_num = int(input("Enter Board Number: "))
            if board_num > 0 and board_num <= len(todo):
                KanbanBoard(board_num)
            else:
                print("Invalid Board Number")
        else:
            print("Thank you, exiting...")
            break

