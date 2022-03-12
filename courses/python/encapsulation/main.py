
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.radius})"
#
#     @property
#     def radius(self):
#         """The radius property."""
#         print("Get radius")
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         print("Set radius")
#         self.__radius = value
#
#     @radius.deleter
#     def radius(self):
#         print("Delete radius")
#         del self.__radius
#
#     def __radius_pow_by_value(self, value):
#         return self.__radius ** value
#
#     def radius_pow_by_value(self, value):
#         if isinstance(value, int):
#             return self.__radius_pow_by_value(value)
#         raise ValueError(f"{value} is not type int")


class Employee:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.email = f"{name}.{last_name}@mail.com"

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.last_name})"

    # def __init__(self, name, last_name):
    #     self.__name = name
    #     self.__last_name = last_name
    #     self.__email = f"{name}.{last_name}@mail.com"

    # def __repr__(self):
    #     return f"{self.__class__.__name__}({self.__name}, {self.__last_name})"

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def last_name(self):
    #     return self.__last_name
    #
    # @last_name.setter
    # def last_name(self, value):
    #     self.__last_name = value
    #
    # @property
    # def full_name(self):
    #     return f"{self.__name} {self.__last_name}"
    #
    # @full_name.setter
    # def full_name(self, new_full_name):
    #     self.__name, self.__last_name = new_full_name.split()
    #
    # @property
    # def email(self):
    #     return f"{self.name}.{self.last_name}@mail.com"
    #
    # @email.setter
    # def email(self, new_email):
    #     self.__name, self.__last_name = new_email.split("@")[0].split(".")
    #     self.__email = new_email


def main():
    pass

    # Differences between protected and private methods
    # circle = Circle(25)
    # print(circle.radius_pow_by_value(2))
    # print(circle.__radius_pow_by_value(2))

    # print(circle)

    # Trying to overwrite attrs
    # emp = Employee("juan", "cruz")
    # print(emp.full_name)
    # print(emp.email)
    #
    # emp.name = "Benedito"
    # print(emp.full_name)
    # print(emp.email)
    #
    # emp.full_name = "Benito Camelo"


    # Test with getters and setters
    # emp = Employee("juan", "cruz")
    # print(emp.full_name)
    # print(emp.email)
    #
    # emp.name = "tomas"
    # print(emp.full_name)
    # print(emp.email)
    #
    # emp.last_name = "morales"
    # print(emp.full_name)
    # print(emp.email)


if __name__ == '__main__':
    main()
