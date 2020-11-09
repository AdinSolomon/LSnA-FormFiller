
from Field import Field
    
#################################

class InputFormat:
    def __init__(self, filepath: str):
        pass

################################

class InputFile:
    def __init__(self, filepath: str):
        pass
    def is_of_format(self, input_format: InputFormat) -> bool:
        pass
    def get_fields(self) -> [Field]:
        pass
    def verify_fields(self, input_format: InputFormat) -> bool:
        pass
