
board = [[7,8,9],[4,5,6],[1,2,3]]

def print_board():
    print("------")
    print("OOOOOO")
    print("XXXXXX")
    print("~~~~~~")
    for i in range(0,2):
        row = board[i]
        print(f'{str(row[0])}|{str(row[1])}|{str(row[2])}') 
    row = board[2]
    print(f'{str(row[0])}|{str(row[1])}|{str(row[2])}')

def check_marked(x,y):
    try:
        int(board[x][y])
    except Exception:
        raise ValueError("That Cell is already Marked!")

def set_cell(x,y,marker):
    try:
        marked = check_marked(x,y)
        board[x][y] = marker
    except Exception as e:
        return -2
    return 2

def check_choice(choice):
    try:
        choice = int(choice)
    except ValueError:
        raise ValueError("Non-integer input not accepted!")
    if choice > 9 or choice < 1:
        raise ValueError("Value out of range!")
    return(choice)

def get_cell(choice):
    if choice<4:
        return (2,choice-1)
    elif choice<7:
        return(1,choice-4)
    else:
        return(0,choice-7)

def check_winner():
    for i in board:
        if all(j==i[0] for j in i):
            #print("cross")
            return True    
        
    for i in range(0,3):
        column = []
        for j in range(0,3):
            column.append(board[j][i])
        if all(k==column[0] for k in column):
            return True
    
    diag = []
    diag.append(board[0][0])
    diag.append(board[1][1])
    diag.append(board[2][2])
    if all(k==diag[0] for k in diag):
        return True
    
    diag[0]=board[0][2]
    diag[2]=board[2][0]
    if all(k==diag[0] for k in diag):
        return True

def check_full():
    for i in board:
        if all(isinstance(j, str) for j in i):
            pass
        else:
            return False
    return True
        

def get_choice(marker):
    choice = input("Choose a cell to mark: ")
    try:
        choice = check_choice(choice)
        cell = get_cell(choice)
        status = set_cell(cell[0],cell[1],marker)
        if check_winner():
            return 1
        elif check_full():
            return -1
        else:
            return status

    except Exception as e:
        print(e)

over = False
marker = "O"
status = 2
while not over:
    if status == 2:
        if marker == "X":
            marker = "O"
        else:
            marker = "X"
    print_board()
    status = get_choice(marker)
    if status == 1:
        over = True
    elif status == -1:
        over = True
        marker = "CAT"
    

print_board()   
print(f'{marker} Wins!')
