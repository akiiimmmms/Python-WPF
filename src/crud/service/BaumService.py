from crud.service import NotFoundException
from crud.repository.BaumRepository import BaumRepository
from crud.entity.Baum import Baum

class BaumService:
    def __init__(self, baum_repository: BaumRepository):
        self.baum_repository = baum_repository

    def add(self, baum: Baum) -> None:
        self.baum_repository.add(baum)

    def get_by_id(self, id: int) -> Baum:
        baum = self.baum_repository.get(id)
        if baum is None:
            raise NotFoundException(id)
        return baum

    def update_by_id(self, id: int, baum: Baum) -> None:
        baum = self.baum_repository.get(id)
        if baum is None:
            raise NotFoundException(id)
        self.baum_repository.update(baum)

    def delete_by_id(self, id: int) -> None:
        baum = self.baum_repository.get(id)
        if baum is None:
            raise NotFoundException(id)
        self.baum_repository.delete(id)

    def get_all(self) -> list[Baum]:
        return self.baum_repository.get_all()