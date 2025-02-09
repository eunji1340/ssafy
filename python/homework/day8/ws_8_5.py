class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        super().__init__()

class Cat(Animal):
    sound = '야옹'

    def __init__(self):
        super().__init__()

class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

print(Pet())