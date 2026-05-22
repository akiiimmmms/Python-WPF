from crud.entity.Baum import Baum
from crud.repository.db import baeume

class BaumRepository:
    def __init__(self):
        # Nutze die Mock-Datenbank
        self.baeume: list[Baum] = baeume

    def add(self, baum: Baum) -> None:
        self.baeume.append(baum)

    def get(self, id: int) -> Baum | None:
        for baum in self.baeume:
            if baum.id == id:
                return baum
        return None

    def update(self, updated_baum: Baum) -> None:
        for i, baum in enumerate(self.baeume):
            if baum.id == updated_baum.id:
                self.baeume[i] = updated_baum
                return
    
    def delete(self, id: int) -> None:
        for baum in self.baeume:
            if baum.id == id:
                self.baeume.remove(baum)
                return

    def get_all(self) -> list[Baum]:
        return self.baeume