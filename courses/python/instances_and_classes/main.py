import datetime

from constants import WORK_DAYS


class Employee:
    status = "WORKING"

    # def __init__(self, data):
    #     self.name = data.get("name")
    #     self.last_name = data.get("last_name")
    #     self.age = data.get("age")

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # def __str__(self):
    #     return f"{self.name} - {self.last_name}"

    def __repr__(self):
        return f"Employee({self.name}, {self.last_name}, {self.age})"

    # def __init__(self, name, last_name, age, registration_date=None):
    #     self.name = name
    #     self.last_name = last_name
    #     self.age = age
    #     if registration_date:
    #         self.registration_date = registration_date

    # def __init__(self, name, last_name, age, *args, **kwargs):
    #     self.name = name
    #     self.last_name = last_name
    #     self.age = age

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    @property
    def full_name(self):
        return self.get_full_name()

    @staticmethod
    def is_workday():
        return datetime.datetime.now().weekday() in WORK_DAYS

    @staticmethod
    def is_daily_time():
        current_time = datetime.datetime.now().time()
        time_daily_start = datetime.time(hour=10)
        time_daily_end = datetime.time(hour=10, minute=30)
        return time_daily_start <= current_time <= time_daily_end

    @classmethod
    def change_status(cls, status):
        cls.status = status

    @classmethod
    def from_string_person(cls, string_person):
        name, last_name, age = string_person.split('-')
        return cls(name, last_name, age)

    @classmethod
    def from_year_of_birth(cls, name, last_name, birth_date, date_format="%Y-%m-%d"):
        birth_year = datetime.datetime.strptime(birth_date, date_format).year
        age = datetime.datetime.now().year - birth_year
        return cls(name, last_name, age)


def main():
    data_dict = {
        "name": "juan",
        "last_name": "sombrero",
        "age": 25
    }
    data_tuple = ("juan", "sombrero", 25)
    data_list = ["juan", "sombrero", 25]

    extra_data = {"manager": "mark", "department": "multi-cloud", "role": "cloud developer"}

    # UNPACKING
    # Case Scenario 1 - passing params as dict to class.__init__()
    # emp = Employee(data_dict)

    # Case Scenario 2 - passing params unpacking dict with ** to class.__init__()
    emp = Employee(**data_dict)
    #
    # # Case Scenario 3 - passing params unpacking tuple with * to class.__init__()
    # emp = Employee(*data_tuple)
    #
    # # Case Scenario 4 - passing params unpacking list with * to class.__init__()
    # emp = Employee(*data_list)

    # ARGS / KWARGS
    # emp = Employee("pepe", "suarez", 44, data_tuple)

    # ALTERNATIVES CONSTRUCTORS
    # instance of a class using a classmethod
    # emp = Employee.from_string_person("juan-gomez-33")
    # emp2 = Employee.from_year_of_birth("alberto", "fuentes", "19-06-1988", "%d-%m-%Y")

    # CHANGING CLASS STATE VS CHANGING INSTANCE STATE
    # classmethod access only to the class state and not to the instance state
    # Employee.get_full_name()  # should fail, it does not have access to the object method or attr
    # Employee.is_daily_time()  # should work, it have access to the static methods
    # Employee.change_status("SICK_LEAVE")  # should work, it have access to the class state(methods of attrs)
    # emp = Employee("mario", "felix", 19)
    # print(emp.status)

    # instance methods have access to the class and object state
    emp = Employee("maria", "pereida", 26)

    print(emp.age)  # access to attr
    print(emp.get_full_name())  # access to instance method
    print(emp.is_workday())  # access to static method
    print(emp.change_status("PTO"))  # access to class method
    print(emp.status)

    print(emp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

