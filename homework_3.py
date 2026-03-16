class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education
    def introduce(self):
        edu = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. У меня {edu} высшее образование.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group_name}. У меня {edu} высшее образование.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. У меня {edu} высшее образование.")


classmate_1 = Classmate("Арген", "12.03.2001", "студент", True, "11A")
friend_1 = Friend("Максим", "27.05.2003", "студент", True, "баскетбол")
classmate_1.introduce()
friend_1.introduce()