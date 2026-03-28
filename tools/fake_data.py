from faker import Faker
import random


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        self.faker = faker


    def full_name(self) -> str:
        return f"{self.faker.first_name()} {self.faker.last_name()}"


    def email(self) -> str:
        return self.faker.email()


    def password(self) -> str:
        return self.faker.password()


    def random_choice(self) -> str:
        return random.choice(["Yes", "No", "Undecided"])






# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())
