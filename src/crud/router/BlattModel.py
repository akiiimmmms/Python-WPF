from crud.entity.Blatt import Blatt
from pydantic import BaseModel

class BlattModel(BaseModel):
    id: int
    farbe: str

    def to_entity(self) -> Blatt:
        return Blatt(self.id, self.farbe)
    
