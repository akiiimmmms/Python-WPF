from crud.entity.Ast import Ast

class Baum:
    def __init__(self, name: str, ast: Ast, id: int | None = None):
        self.id = id
        self.name = name
        self.ast = ast
    
    def set(self, **attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)


    