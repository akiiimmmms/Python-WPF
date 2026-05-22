from crud.entity.Baum import Baum

class BaumRepository:
    def __init__(self):
        self.baeume: list[Baum] = []

    def add(self, baum: Baum) -> None:
        self.baeume.append(baum)

    def get(self, id: int) -> Baum | None:
        for baum in self.baeume:
            if baum.id == id:
                return baum
        return None

    def update(self, baum: Baum) -> None:
        for baum in self.baeume:
            if baum.id == baum.id:
                baum = baum
                return
    
    def delete(self, id: int) -> None:
        for baum in self.baeume:
            if baum.id == id:
                self.baeume.remove(baum)
                return