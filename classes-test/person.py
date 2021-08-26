class Person:
    name: str = ""
    national_id: str = ""

    def __init__(self, name: str, national_id: str):
        self.name = name
        self.national_id = national_id

    def __str__(self):
        return f"{self.name} - {type(self)}"
