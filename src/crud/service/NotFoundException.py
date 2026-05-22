class NotFoundException(Exception):
    def __init__(self, id: int):
        self.id = id
        super().__init__(f"Baum mit ID {id} nicht gefunden")