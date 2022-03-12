
class Person:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_full_description(self):
        return f"{self.name} {self.last_name}"


class Athlete:

    def __init__(self, sport, teacher):
        self.sport = sport
        self.teacher = teacher

    def get_full_description(self):
        return f"{self.sport} - {self.teacher}"


class Student(Person, Athlete):

    def __init__(self, name, last_name, age, sport, teacher, student_id):
        # super(Person).__init__(name, last_name, age)
        # super(Athlete).__init__(sport, teacher)
        Person.__init__(self, name, last_name, age)
        Athlete.__init__(self, sport, teacher)
        self.student_id = student_id

    def get_full_description(self):
        return


    # def get_full_description(self):
    #     return Athlete.get_full_description(self)


class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')

def main():

    per = Person("david", "sanchez", 29)
    athle = Athlete("tennis", "rick")
    stu = Student("Edison", "Thomas", 22, "baseball", "Morgan", 23567)

    print(stu.get_full_description())
    # print(help(stu))

    # print(help(dev))


if __name__ == '__main__':
    main()
