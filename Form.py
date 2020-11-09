
from Field import Field

#################################

class FormFormat:
    def __init__(self):
        pass
    def get_fields(self) -> [Field]:
        pass
    def populate(self, fields: [Field]) -> FormFile:
        # Creates a FormFile using fields
        pass

#################################

class FormFile:
    def __init__(self):
        pass
    def save(self, filepath: str):
        pass