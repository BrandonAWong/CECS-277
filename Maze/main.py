# Names: Trung Ho & Brandon Wong
# Date: 9/12/2023
# Desc: Python CLI game that reads a txt file and has the player run through a maze.

from check_input import get_int_range

def read_maze() -> list[list[str]]:
    '''
    Opens maze.txt file and returns it as a 2D-list.
    '''
    with open("maze.txt", 'r') as maze:
        return maze.readlines()

def find_start(maze: list[list[str]]) -> list[int]:
    '''
    Returns the starting point of the maze as a list.
    '''
    for row in range(len(maze)):
        if 's' in maze[row]:
              return [row, maze[row].index('s')]

def display_maze(maze: list[list[str]], loc: list[int]) -> None:
    '''
    Prints out the maze
    '''
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            print('X', end='') if [row, col] == loc else print(maze[row][col], end='')

def main() -> None:
    print("-Maze Solver-")
    maze: list[list[str]] = read_maze()
    loc: list[int] = find_start(maze)
    while maze[loc[0]][loc[1]] != 'f':
        display_maze(maze, loc)
        print('\n'
            "1. Go North\n"
            "2. Go South\n"
            "3. Go East\n"
            "4. Go West")
        choice = get_int_range("Enter choice: ", 1, 4)
        if choice == 1 and maze[loc[0]-1][loc[1]] != '*':
            loc[0] -= 1
        elif choice == 2 and maze[loc[0]+1][loc[1]] != '*':
            loc[0] += 1
        elif choice == 3 and maze[loc[0]][loc[1]+1] != '*':
            loc[1] += 1
        elif choice == 4 and maze[loc[0]][loc[1]-1] != '*':
            loc[1] -= 1
        else:
            print("You cannot move there.")
    display_maze(maze, loc)
    print("Congratulations! You solved the maze.")
    return

main()