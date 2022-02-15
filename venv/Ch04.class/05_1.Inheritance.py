# 추상클래스
# abc 라는걸 import 하고 부모클래스에 metaclass = ABCMeta를 추가
# 부모클래스에 abstractmethod 를 정의 
from abc import *

class Item(metaclass=ABCMeta):
    """
    속성 : 이름
    메서드 : 줍기, 버리기
    """
    def __init__(self,name):
        self.name= name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    @abstractmethod
    def use(self):
        pass


class Weapon(Item):
    """
    속성 : 공격력
    메서드 : 줍기, 버리기
    """

    def __init__(self,name, demage):
        super().__init__(name)
        self.demage = demage

    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.")

class HealingItem(Item):
    """
    속성 : 회복량
    메서드 : 사용하기
    """
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 사용합니다. {self.recovery_amount}만큼 회복되었습니다.")


m16 = Weapon("m16", 110)
bandage = HealingItem("붕대",20)

m16.use()
bandage.use()