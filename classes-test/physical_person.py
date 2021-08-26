from person import Person


class PhysycalPerson(Person):
    last_name: str

    def __init__(self, name: str, national_id: str, last_name: str):
        self.last_name = last_name
        super().__init__(name, national_id)
