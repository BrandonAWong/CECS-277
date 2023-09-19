# Names: Trung Ho & Brandon Wong
# Date: 9/19/2023
# Desc: Utilizing classes to create a rectangle and move it along a grid in a CLI program


from rectangle import Rectangle
from check_input import get_int_range


def display_grid(grid: list[list[str]]) -> None:
    '''
    Prints out the grid and triangle
    '''
    [print(' '.join(row)) for row in grid]

def reset_grid(grid: list[list[str]]) -> None:
    '''
    Turns grid into all '.'s
    '''
    grid[:] = [['.' for _ in range(20)] for _ in range(20)]

def place_rect(grid: list[list[str]], rect: Rectangle) -> None:
    '''
    Places the rectangle into the 2D array as '*'s
    '''
    x, y = rect.get_cords()
    w, h = rect.get_dimensions()
    for i in range(h):
        for j in range(w):
            grid[y+i][x+j] = '*'

def main() -> None:
    width: int = get_int_range("Enter a rectangle width (1-5): ", 1, 5)
    height: int = get_int_range("Enter a rectangle height (1-5): ", 1, 5)
    rect: Rectangle = Rectangle(width, height)
    grid: list[list[str]] = []
    while True:
        reset_grid(grid)
        place_rect(grid, rect)
        display_grid(grid)
        choice = get_int_range("Enter Direction:\n"
                               "1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n",
                               1, 5)
        if choice == 1 and rect.y > 0:
            rect.move_up()
        elif choice == 2 and rect.y+height < 20:
            rect.move_down()
        elif choice == 3 and rect.x > 0:
            rect.move_left()
        elif choice == 4 and rect.x+width < 20:
            rect.move_right()
        elif choice == 5:
            break
        else:
            print("Unable to move there.")


main()