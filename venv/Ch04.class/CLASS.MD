# 클래스

## 클래스와 객체
```buildoutcfg
* 절차지향 vs 객체지향

    - 절차 지향 프로그래밍 : 기능들을 어떤 순서로 처리할 것인가에 초점을 맞춘다.    
    - 객체 지향 프로그래밍 : 객체가 중심이 되고, 객체를 정의하고 객체간 상호작용에 초점을 맞춘다.
    
✔ 프로그래밍 규모에 따라 절차 지향일지 객체 지향일지 선택할 수 있다.
```

## 여러가지 속성
```buildoutcfg

✔ 예시코드
    def __init__(self, name, hp, shield, demage):
    /*
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
    */ 여기가 인스턴스 속성이 있는 부분이다. 객체마다 모두 다르게 가지고 있다.    
        print(f"[{self.name}] 이(가) 생성되었습니다.")
    # 객체를 출력할 때 호출 되는 메서드
    def __str__(self):
        return f"체력 : {self.hp}, 방어막 : {self.shield}, 공격력 : {self.demage}"
        
- 클래스 안 : self.속성명
- 클래스 밖 : 객체명.속성명

* 모든 객체가 공유하는 속성 

class Unit:
    count = 0 # 모든 객체가 공유하는 속성
    def __init__(self, name, hp, shield, demage):    
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1 # self 붙이는 거 아님
        
- 클래스 밖에서 사용할 때
print(Unit.count)

* 클래스 안에서만 접근 가능한 속성
    def __init__(self, name, hp, shield, demage):    
        self.name = name
        self.__hp = hp # 이렇게 하면 Public 속성으로 변경되므로
        self.shield = shield
        self.demage = demage

- 클래스 밖에서
zealot.__hp = 9999 변경 불가능
```

## 메서드
```buildoutcfg
* 인스턴스 메서드

- hit 메서드 구현
1️⃣ 데미지가 방어막보다 작거나 같으면 방어막만 깎인다.
2️⃣ 데미지가 방어막보다 크고 체력보다 작으면 체력과 방어막이 깎인다.
3️⃣ 데미지가 체력보다 크면 체력을 0으로 만든다.

* 클래스 메서드
    - 클래스 속성에 접근하기 위해서 사용한다.
    - 클래스를 의미하는 cls를 파라미터로 받는다.
    
    class Unit:
        count = 0
        ...
        @classmethod
        def print_count(cls):
            print(f"전체 유닛 개수 : {cls.count}"
            
* 정적 메서드
    - 인스턴스를 만들 필요가 없는 메서드
    - self를 받지 않는다
    - 메서드가 인스턴스 유무와 관계없이 독립적으로 사용될 때
    
    class Math:
        @staticmethod
        def add(x,y):
        return x+y    
        
* 매직 메서드
    - 클래스 안에 정의할 수 있는 스페셜 메서드
    - 특별한 상황에 호출된다.
    - __이름__ 형태로 되어있음.
```

## 상속
```buildoutcfg
* 상속의 개념
    - 클래스들의 공통된 속성과 메서드를 뽑아내서 부모 클래스를 만든다.
    - 이를 자식 클래스에서 상속받아서 사용한다.
    
    ✔ 장점  
    - 코드의 중복을 제거할 수 있다.
    - 유지보수가 편리해진다.
* 추상 클래스 (abstract method)
    - 부모 클래스의 추상 클래스를 자식클래스에선 항상 구현 해야한다.
*
*
```