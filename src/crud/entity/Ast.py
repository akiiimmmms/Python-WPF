from crud.entity import Blatt
class Ast:
    def __init__(self, id: int, eigenschaft: str, blatt: Blatt):
        self.id = id
        self.eigenschaft = eigenschaft
        self.blatt = blatt
    