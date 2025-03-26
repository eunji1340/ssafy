class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        Myth.increase_myth()

    @classmethod
    def increase_myth(cls):
        cls.type_of_myth += 1

    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')


Dangun = Myth('dangun')
Greek = Myth('greek & rome')

print(Dangun.name)
print(Greek.name)
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description()
