from crud.entity.Ast import Ast

class Baum:
    def __init__(self, id: int, name: str, ast: Ast):
        self.id = id
        self.name = name
        self.ast = ast