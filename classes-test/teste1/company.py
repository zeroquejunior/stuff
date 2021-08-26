from person import Person


class Company(Person):
    state_subscription: str

    def __init__(self, name: str, national_id: str, state_subscription: str):
        self.state_subscription = state_subscription
        super().__init__(name, national_id)

    def peida(self):
        print("Empresa não peida")
