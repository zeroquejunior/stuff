from typing import List
from person import Person
from physical_person import PhysycalPerson
from company import Company


class PersonService:
    __persons: list[Person] = []

    def list_person(self) -> list[Person]:
        ze = PhysycalPerson("Ze", "123912309", "Roque")
        tiago = PhysycalPerson("Tiago", "1231231", "Framesqui")
        random_shopping = Company(
            "Random Shopping", "12893891238912389/0001-12", "123901293210"
        )
        winerfy = Company("Winerfy", "9182389123/0001-12", "asdasdas")
        self.__persons.extend([ze, tiago, random_shopping, winerfy])

        for person in self.__persons:
            person.peida()


PersonService().list_person()
