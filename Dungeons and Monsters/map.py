class Map:
    _instance = None
    _initialized = False

    def __new__(cls, *args): 
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, ):
        if not Map._initialized:
            with open("map.txt", "r") as f:
                self._map: list[list[chr]] = f.readlines()
            self._revealed: list[list[bool]] = [[False for _ in row] for row in self._map]
            Map._initialized = True

    def __getitem__(self, row: int) -> list[chr]:
        return self._map[row]