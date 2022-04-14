from abc import ABC, abstractmethod

#
# class InformalEmployeeInterface:
#     """
#     This is an informal interface and should not be instancetiated.
#     """
#     def __init__(self):
#         pass
#
#     def calculate_payroll(self):
#         pass
#
#     def get_generated_payroll_date(self):
#         pass
#
#
# class FormalEmployeeInterface(ABC):
#     """
#     This is an formal interface and can not be instancetiated.
#     """
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def calculate_payroll(self):
#         pass
#
#     @abstractmethod
#     def get_generated_payroll_date(self):
#         pass
#
#
# class EmployeeV1(InformalEmployeeInterface):
#
#     def calculate_payroll(self):
#         return 1200
#
#
# class EmployeeV2(FormalEmployeeInterface):
#
#     def calculate_payroll(self):
#         return 1200


# class Lion:
#     def give_food(self):
#         print("Feeding a lion with raw meat!")
#
#
# class Panda:
#     def feed_animal(self):
#         print("Feeding a panda with some tasty bamboo!")
#
#
# class Snake:
#     def feed_snake(self):
#         print("Feeding a snake with mice!")


# class Animal(ABC):
#     @abstractmethod
#     def feed(self):
#         pass
#
#
# class Lion(Animal):
#     def feed(self):
#         print("Feeding a lion with raw meat!")
#
#
# class Panda(Animal):
#     def feed(self):
#         print("Feeding a panda with some tasty bamboo!")
#
#
# class Snake(Animal):
#     def feed(self):
#         print("Feeding a snake with mice!")

# class Animal(ABC):
#     @abstractmethod
#     def do(self, action): # Renamed it to "do", and it has "action" parameter
#         pass
#
# class Lion(Animal):
#     def do(self, action, time): # It's still mandatory to implement action. "time" is our other parameter
#         print(f"{action} a lion! At {time}")
#
# class Panda(Animal):
#     def do(self, action, time):
#         print(f"{action} a panda! At {time}")
#
# class Snake(Animal):
#     def do(self, action, time):
#         print(f"{action} a snake! At {time}")


class Animal(ABC):
    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def feed(self, time):
        pass


class Lion(Animal):
    @property
    def diet(self):
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}")


class Snake(Animal):
    @property
    def diet(self):
        return ["frog", "rabbit"]

    def feed(self, time):
        print(f"Feeding a snake with {self._food} meat! At {time}")


def main():
    # Informal interface
    # emp = EmployeeV1()
    # print(emp.calculate_payroll())
    # emp2 = InformalEmployeeInterface()
    # print(emp2.get_generated_payroll_date())

    # Formal interface
    # empv2 = EmployeeV2()
    # print(empv2)
    # empv2 = FormalEmployeeInterface()
    # print(empv2.get_generated_payroll_date())

    # Real life example
    # leo = Lion()
    # po = Panda()
    # sam = Snake()
    #
    # leo.give_food()
    # po.feed_animal()
    # sam.feed_snake()

    # the best way will be
    # Put all the animals in a list:
    # zoo = [leo, po, sam]

    # Loop through the animals and feed them
    # for animal in zoo:
    #     # this will fail because there is no feed method in any of those objects.
    #     animal.feed()

    # Required arguments works the same on subclasses than inherit from a parent class.
    # zoo = [Lion(), Panda(), Snake()]
    #
    # for animal in zoo:
    #     # {action} is required by the parent class and {time} is required by the subclass
    #     animal.do(action="feeding", time="10:10 PM")

    # encapsulation with abstract classes
    # leo = Lion()
    # leo.food_eaten = "papa"
    # leo.feed("10:10 AM")
    # adam = Snake()
    # adam.food_eaten = "frog"
    # adam.feed("10:20 AM")


if __name__ == "__main__":
    main()
