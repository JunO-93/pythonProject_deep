# 기존함수
def minus_on(a):
    return a-1
# 람다함수
lambda a:a-1

#람다함수 호출 방법
#1. 함수 자체 호출하는 방법

print((lambda a:a-1)(10))

#2. 변수에 담아서 호출

minus_one_2 = lambda a:a-1
print(minus_one_2(100))

# 람다 함수에서 if 문 사용
# 기존함수
def is_postive_number(a):
    if a > 0:
        return True
    else:
        return False
# 람다함수
lambda a: True if a > 0 else False

#람다함수 호출 방법
#1.
print((lambda a: True if a > 0 else False)(-2))
#2.
is_postive_number = lambda a: True if a > 0 else False
print(is_postive_number(-2))
