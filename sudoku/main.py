'''import pygame

pygame.font.init()

#pygame.display.set_caption("SUDOKU")
windows_surface=pygame.display.set_mode((500,500))

block_size=500/9

x=0
z=0
value=0'''

default_grid=[
    [0,0,2,4,0,5,8,0,0],
    [0,4,1,8,0,0,0,2,0],
    [6,0,0,0,7,0,0,3,9],
    [2,0,0,0,3,0,0,9,6],
    [0,0,9,6,0,7,1,0,0],
    [1,7,0,0,5,0,0,0,3],
    [9,6,0,0,8,0,0,0,1],
    [0,2,0,0,0,9,5,6,0],
    [0,0,8,3,0,6,9,0,0]
]

'''font1=pygame.font.SysFont("Calibri", 30)
font2=pygame.font.SysFont("Verdana", 20)'''


def solve(grid):
    #print_grid(grid)

    find=find_vacant_cell(grid)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if check_valid_num(grid,num,(row,col)):
            grid[row][col] = num

            if solve(grid):
                return True
            grid[row][col] = 0
    return False


def print_grid(grid):

    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("-----------------------------")

        for j in range(len(grid[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end=" ")


def find_vacant_cell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return(i,j)
    return None


def check_valid_num(grid,num,pos):

    # check row
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[pos[0]][j] == num and pos[1]!=j:
                return False

    # check column
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][pos[1]] == num and pos[0]!=i:
                    return False
    # check square
        #for i in range(len(grid)):
        #for j in range(len(grid[0])):

        row_start=(pos[0]//3)*3
        col_start=(pos[1]//3)*3

        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if grid[i][j] == num and (i,j)!=pos:
                    return False

        return True


print_grid(default_grid)
solve(default_grid)
print("---------------------------------------------------")
print_grid(default_grid)
