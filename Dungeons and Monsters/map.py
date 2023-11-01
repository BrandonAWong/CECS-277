class Map:
    _instance = None
    _initialized = False

    def __new__(cls): 
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Map._initialized:
            with open("map.txt", "r") as f:
                self._map: list[list[chr]] = [[c for c in row] for row in f.readlines()]
            self._revealed: list[list[bool]] = [[False for _ in row] for row in self._map]
            Map._initialized = True

    def __getitem__(self, row: int) -> list[chr]:
        return self._map[row]

    def __len__(self):
        '''Returns number of rows in the map'''
        return len(self._map)

    def show_map(self, loc: list[int]) -> str:
        '''
        Returns the map as a string and displays revelead locations.
        Unrevealed locations will be denoted with an "x".
        '''
        mapped: list[list[str]] = [[self[i][j] if self._revealed[i][j] or self[i][j] == "\n" else "x" for j in range(len(self[i]))] for i in range(len(self))]
        mapped[loc[0]][loc[1]] = "*"
        return "".join([" ".join(row) for row in mapped])
    
    def reveal(self, loc: list[int]) -> None:
        '''Sets input location as seen'''
        self._revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc: list[int]) -> None:
        '''Sets last position seen by Hero to "n"'''
        self[loc[0]][loc[1]] = "n"