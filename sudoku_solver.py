import time

sudoku=[[3,4,1,0],
                [0,2,0,0],
                [0,0,2,0],
                [0,1,4,3]]

def expand_sudoku(sudoku):
    """
    Expands the sudoku substituting the 0s with the possible values
    """
    sudoku_expanded=sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j]==0:
                sudoku_expanded[i][j]=[1,2,3,4]
            else:
                sudoku_expanded[i][j]=[sudoku[i][j]]
    return sudoku_expanded

def check_rows(sudoku_expanded):
    """
    Checks the rows for possible values
    """
    for i in range(len(sudoku_expanded)):
        known_row_values=[]
        for j in range(len(sudoku_expanded)): # Check for known values
            if (len(sudoku_expanded[i][j])==1): #if the value is already known
                known_row_values.append(sudoku_expanded[i][j][0]) #add it to the list of known values
        for j in range(len(sudoku_expanded)): # remove known values from possible values
            if (len(sudoku_expanded[i][j])>1): #if the value is not known
                for k in range(len(known_row_values)):#remove known values
                    try:
                        sudoku_expanded[i][j].remove(known_row_values[k])
                    except:
                        pass
    return sudoku_expanded

def check_columns(sudoku_expanded):
    """
    Checks the columns for possible values
    """
    for i in range(len(sudoku_expanded)):
        known_column_values=[]
        for j in range(len(sudoku_expanded)): # Check for known values
            if (len(sudoku_expanded[j][i])==1): #if the value is already known
                known_column_values.append(sudoku_expanded[j][i][0]) #add it to the list of known values
        for j in range(len(sudoku_expanded)): # remove known values from possible values
            if (len(sudoku_expanded[j][i])>1): #if the value is not known
                for k in range(len(known_column_values)):#remove known values
                    try:
                        #print("removing",known_column_values[k],"from",sudoku_expanded[j][i],"at",i,j)
                        sudoku_expanded[j][i].remove(known_column_values[k])
                        #print("removed",known_column_values[k],"from",sudoku_expanded[j][i],"at",i,j)
                    except:
                        #print(e)
                        pass
    return sudoku_expanded

def check_squares(sudoku_expanded):
    """
    Checks the squares for possible values
    """
    #0,0 0,1 1,0 1,1   0,2 0,3 1,2 1,3   2,0 2,1 3,0 3,1   2,2 2,3 3,2 3,3
    known_square_values=[]
    for square in range(4):
        known_square_values.append([])
        for i in range(0,2):
            for j in range(0,2):
                #print(i+int(square%2)*2,j+int(square/2)*2)
                i2=i+int(square%2)*2
                j2=j+int(square/2)*2
                if(len(sudoku_expanded[i2][j2])==1):
                    known_square_values[square].append(sudoku_expanded[i2][j2][0])
                         
    #print(known_square_values)       
    for square in range(4):
        for i in range(0,2):
            for j in range(0,2):
                #print(i+int(square%2)*2,j+int(square/2)*2)
                i2=i+int(square%2)*2
                j2=j+int(square/2)*2
                if(len(sudoku_expanded[i2][j2])>1):
                    for k in range(len(known_square_values[square])):#remove known values
                        try:
                            #print("removing",known_square_values[square][k],"from",sudoku_expanded[j][i],"at",i,j)
                            sudoku_expanded[i2][j2].remove(known_square_values[square][k])
                        except:
                            pass
    return sudoku_expanded

def check_sudoku(sudoku_expanded):
    """
    Checks the sudoku for possible values
    """
    print_sudoku(sudoku_expanded)
    sudoku_expanded=check_rows(sudoku_expanded)
    print("row")
    print_sudoku(sudoku_expanded)
    print("column")
    sudoku_expanded=check_columns(sudoku_expanded)
    print_sudoku(sudoku_expanded)
    print("squares")
    sudoku_expanded=check_squares(sudoku_expanded)
    print_sudoku(sudoku_expanded)
    return sudoku_expanded

def is_solved(sudoku_expanded):
    """
    Checks if the sudoku is solved
    """
    for i in range(len(sudoku_expanded)):
        for j in range(len(sudoku_expanded)):
            if len(sudoku_expanded[i][j])>1:
                return False
    return True

def print_sudoku(sudoku_expanded):
    """
    Prints the sudoku
    """
    print("Sudoku:")
    for i in range(len(sudoku_expanded)):
        for j in range(len(sudoku_expanded)):
            for k in range(len(sudoku_expanded[i][j])):
                print(sudoku_expanded[i][j][k],end="")
            print("\t",end="")
        print()
    print()


def solve_sudoku(sudoku):
    """
    Solves the sudoku
    """
    sudoku_expanded=expand_sudoku(sudoku)
    #print_sudoku(sudoku)
    while not is_solved(sudoku_expanded):
        sudoku_expanded=check_sudoku(sudoku_expanded)
        time.sleep(1)
    return sudoku_expanded

sudoku_expanded=solve_sudoku(sudoku)


#check_sudoku(expand_sudoku(sudoku))
