from crud.entity.Ast import Ast
from pydantic import BaseModel
from crud.router.BlattModel import BlattModel

class AstModel(BaseModel):
    id: int
    name: str
    blatt: BlattModel

    def to_entity(self) -> Ast:
        return Ast(self.id, self.name, self.blatt.to_entity())