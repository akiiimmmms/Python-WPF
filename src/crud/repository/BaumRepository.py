from crud.entity.Baum import Baum
from crud.repository.db import baeume
from loguru import logger

class BaumRepository:
    def __init__(self):
        self.baeume: list[Baum] = baeume

    def add(self, baum: Baum) -> int:
        baum.set(id = len(self.baeume) + 1)
        logger.info(f"Tree with ID {baum.id} added.")
        self.baeume.append(baum)
        return baum.id

    def get(self, id: int) -> Baum | None:
        logger.info(f"Get baum by id: {id}")
        for baum in self.baeume:
            if baum.id == id:
                return baum
        return None

    def update(self, updated_baum: Baum) -> None:
        logger.info(f"Update baum by id: {updated_baum}")
        for i, baum in enumerate(self.baeume):
            if baum.id == updated_baum.id:
                self.baeume[i] = updated_baum
                return
    
    def delete(self, id: int) -> None:
        logger.info(f"Delete baum by id: {id}")
        for baum in self.baeume:
            if baum.id == id:
                self.baeume.remove(baum)
                return

    def get_all(self) -> list[Baum]:
        logger.info("Get all baeume")
        return self.baeume