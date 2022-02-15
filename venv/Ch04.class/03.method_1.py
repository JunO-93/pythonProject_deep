class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체바다 다른 값을 가지는 속성
    """
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f"[{self.name}] 이(가) 생성되었습니다.")
    # 객체를 출력할 때 호출 되는 메서드
    def __str__(self): # 매직 메서드 = 던더 메서드
        return f"체력 : {self.hp}, 방어막 : {self.shield}, 공격력 : {self.demage}"
    # 인스턴스 메서드 [즉각적인(메모리상에 객체가 실체한다) 메서드]
    # 인스턴스 메서드 속성에 접근할 수 있는 메서드
    def hit(self, demage):
        if self.shield >= demage:
            self.shield = self.shield - demage

        elif self.shield < demage:
            temp = demage - self.shield
            self.hp = self.hp - temp
            self.shield = 0

            if self.hp <=0:
                self.hp = 0
    #클래스 메서드( class method )
    #클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]개")

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)


# print(probe)
# probe.hit(12)
# print(probe)
#
# probe.hit(12)
# print(probe)
#
# probe.hit(12)
# print(probe)
#
# probe.hit(12)
# print(probe)

Unit.print_count()

print(dir(probe))


