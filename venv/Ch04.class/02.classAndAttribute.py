class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체바다 다른 값을 가지는 속성

    클래스 속성 : 전체 유닛 개수
    -> 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성
    """
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.__hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f"[{self.name}] 이(가) 생성되었습니다.")
    # 객체를 출력할 때 호출 되는 메서드
    def __str__(self):
        return f"체력 : {self.__hp}, 방어막 : {self.shield}, 공격력 : {self.demage}"

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)


# 인스턴스 속성 수정
probe.demage += 1
print(probe)

# 비공개 속성 접근
probe.__hp = 9999
print(probe)

# 네임 맹글링 (name mangling) --> 비공개 속성 접근을 접근하는 방법
probe._Unit__hp = 9999
print(probe)

# 클래스 속성 출력
print(Unit.count)

#