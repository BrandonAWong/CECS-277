class Rectangle():
    '''
    A rectangle with coordinates and a height and width which can be moved around
    '''
    def __init__(self, w: int, h: int):
        '''
        Constructor of the rectangle
        Contains: coordiantes and dimensions
        '''
        self.x = self.y = 0
        self.w = w
        self.h = h

    def get_cords(self) -> tuple[int, int]:
        '''
        Returns the coordinates of the rectangle
        '''
        return (self.x, self.y)
    
    def get_dimensions(self) -> tuple[int, int]:
        '''
        Returns the dimensions of the rectangle
        '''
        return (self.w, self.h)
    
    def move_up(self) -> None:
        '''
        Moves the rectangle up
        '''
        self.y -= 1
    
    def move_down(self) -> None:
        '''
        Moves the rectangle down
        '''
        self.y += 1
    
    def move_left(self) -> None:
        '''
        Moves the rectangle left
        '''
        self.x -= 1

    def move_right(self) -> None:
        '''
        Moves the rectangle down
        '''
        self.x += 1