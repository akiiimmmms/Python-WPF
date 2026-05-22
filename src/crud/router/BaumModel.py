from crud.entity.Baum import Baum
from pydantic import BaseModel
from crud.router.AstModel import AstModel

class BaumModel(BaseModel):
    name: str
    ast: AstModel

    def to_entity(self) -> Baum:
        return Baum(name = self.name, ast = self.ast.to_entity())