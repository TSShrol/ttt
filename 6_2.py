# Напишіть клас Animal, який при створенні екземпляру надає йому
# атрибут виду тварини species. Клас має містити метод,
# який виводить інформацію про вид тварини,і метод, який виводить
# характерний звук для даного виду тварини.
# Створіть два класи Dog і Cat, які успадковуються від класу Animal
# (є підкласами для Animal). У кожному з підкласів реалізуйте виклик
# конструктора надкласу з передачею йому назви виду тварини.
# Також, у підкласах реалізуйте методи, які перевизначають метод
# надкласу для відтворення характерного звуку для конкретного виду тварини.
# Визначте окрему функцію show_animal_info, яка приймає об’єкт (екземпляр класу)
# як аргумент і викликає його методи show_species і make_sound,
# якщо це тварина, а інакше - виводиться відповідне повідомлення як у вихідних даних.
#
# Вхідні дані:
# Немає
# Вихідні дані:
# I'm an - ordinary animal
# Grrr!
# I'm an - dog
# Woof! Woof!
# I'm an - cat
# Meow!
# Book this is not an animal!

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'person: {self.__name}, {self.__age} '


class Animal:
    def __init__(self, species):
        self.__species = species
        self.__voice = 'Grr-r-r'

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, voice):
        self.__voice = voice

    def infoAnimal(self):
        print("I am - ", self.__species)

    def voiceAnimal(self):
        print(self.__voice)

    def __str__(self):
        return f'This is {self.__species} and its voice {self.__voice} '


class Dog(Animal):
    def __init__(self, person=Person('NoneName', 18)):
        super().__init__("dog")
        self.__voice = "Woof!"
        self.__person = person  # об'єкт

    def voiceAnimal(self):
        print(self.__voice, self.__voice)

    def infoAnimal(self):
        super().infoAnimal()
        print("Owner ", super().species, self.__person)

    def __str__(self):
        return f'This is {super().species} and its voice {self.__voice} '


class Cat(Animal):
    def __init__(self):
        super().__init__("cat")
        self.__voice = "Meow!"

    def voiceAnimal(self):
        print(self.__voice, self.__voice)

    def __str__(self):
        return f'This is {Animal.species(self)} and its voice {self.__voice} '
    # super().species або Animal.species(self) або super(Cat,self).species
    # super().voiceAnimal() - виклик методу базовго класу


animal1 = Animal("ordinary animal")
animal1.infoAnimal()
print(animal1)
dog1 = Dog(Person('Olga',25))
dog1.infoAnimal()
print(dog1)
print(dog1.species)
person=Person('Igor',34)
dog2=Dog(person)
dog2.infoAnimal()

# dog1.voiceAnimal()
# cat=Cat()
# print(Cat.__base__)
# cat.infoAnimal()
# print(cat)
