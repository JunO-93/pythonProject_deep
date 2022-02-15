# Unit 클래스
class unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    """

    # 생성자 (constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f"[{self.name}] 이(가) 생성되었습니다.")
    # 객체를 출력할 때 호출 되는 메서드
    def __str__(self):
        return f"체력 : {self.hp}, 방어막 : {self.shield}, 공격력 : {self.demage}"

# 프로브 객체를 생성
probe = unit("프로브", 20, 20, 5)
print(probe.__str__())
# 질럿 객체를 생성
zealot = unit("질럿", 100, 60, 16)
print(zealot.__str__())
# 드라군 객체를 생성
dragoon = unit("드라군", 100, 80, 20)
print(dragoon.__str__())