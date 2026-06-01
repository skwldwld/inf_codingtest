class Person:
    def __init__(self, name_param): # 생성자
        self.name = name_param
        print("hi", self, self.name) # self: 자기자신의 정보

    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다.")

person_1 = Person("A")
person_1.talk()
person_2 = Person("B")
person_2.talk()