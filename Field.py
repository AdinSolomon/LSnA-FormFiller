
class Field:
    def __init__(self, field_name: str, field_coordinates: str, field_value: str):
        self.name =     field_name
        self.coords =   field_coordinates
        self.value =    field_value
    def __str__(self):
        return "Field< "+self.name+ " ("+self.coords+") = "+self.value+" >"
    def __repr__(self):
        return (self.name, self.coords, self.value)
    