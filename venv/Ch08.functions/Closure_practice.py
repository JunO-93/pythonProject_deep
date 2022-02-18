#1. 내부함수
#함수 안에 또다른 함수를 정의할 수 있다.

# def outer(name):
#     def inner():
#         print(name, "안녕하세요 이너함수입니다.")
#     return inner
#
# func = outer("startcoding") #아우터함수는 이시점에 종료가 되었음, 이너함수는 어디서 나온걸까? 클로저라는 공간에 name이란 데이터가 들어가 있어서 가능하다.
# func()

# 2. 클로저
# 함수가 종료되어도 자원을 사용할 수 있는 함수

# ** 클로저가 될 조건
# 1) 내부함수 여야 한다.
# 2) 외부 함수의 변수를 참조해야 한다.
# 3) 외부 함수가 내부 함수를 반환해야 한다.

def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요!")
        print("나이: ", age)
        print("성별: ", gender)
    return inner

closure = greeting('나미', 27, 'female')
closure()

# print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)


# 왜 쓰는가?
# 전역변수를 사용해서 대체는 가능하다. 
# 그러나 전역변수 사용을 최소화 하는 것이 좋다. ( 네이밍문제, 스코프 문제 )
# 제네레이터 데코레이터를 이해하기 위해 알아야하는 개념