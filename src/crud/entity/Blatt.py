from crud.entity.Ast import Ast
class Blatt:
    def __init__(self, id: int, farbe: str, ast: Ast):
        self.id = id
        self.farbe = farbe
        self.ast = ast
