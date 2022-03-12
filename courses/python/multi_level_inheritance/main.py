

class Person:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.name} {self.last_name}"


class Employee(Person):

    def __init__(self, name, last_name, age, salary, squad):
        super().__init__(name, last_name, age)
        self.salary = salary
        self.squad = squad

    def get_full_name(self):
        return f"The name is {self.name} {self.last_name}"


class Developer(Employee):

    def __init__(self, name, last_name, age, salary, squad, programing_lang):
        super().__init__(name, last_name, age, salary, squad)
        self.programing_lang = programing_lang


def main():
    d = {
        "name": "juan",
        "last_name": "perez",
        "age": 21,
        "squad": "cloud",
        "salary": 55000,
        "programing_lang": "python"
    }

    per = Person("david", "sanchez", 29)
    emp = Employee("pedro", "sanchez", 33, 28000, "marketing")
    dev = Developer(**d)

    print(per.get_full_name())
    print(emp.get_full_name())
    print(dev.get_full_name())

    # print(help(dev))


if __name__ == '__main__':
    main()
