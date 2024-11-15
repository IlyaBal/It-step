class invalidAgeErro(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Person:
    # def __init__(self):
    def set_age(self, age):
        if age < 0 or age > 120:
            raise invalidAgeErro("не корректно число років")

        self.age = age


try:
    p = Person()
    p.set_age(65)
except invalidAgeErro as e:
    print(e)
