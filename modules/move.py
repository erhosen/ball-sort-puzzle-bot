class Move:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __repr__(self):
        return f'Ball({self})'

    def __str__(self) -> str:
        return f'{self.i} -> {self.j}'
