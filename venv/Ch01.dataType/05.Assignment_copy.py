# 리스트 할당 방식

x = [1,2,3,4,5]
y = x

y[2]=0
print(x)
print(y)
# 주소값 호출
print(id(x))
print(id(y))


# 리스트 카피

x1 = [1,2,3,4,5]
y1 = x1.copy()
print(x1)
print(y1)
# 주소값 호출
print(id(x1))
print(id(y1))

# 다차원 리스트 복사 방식

x2=[[1,2],[3,4,5]]
import copy
y2=copy.deepcopy(x2)

z2=x2.copy()
print(x2)
print(y2)

# 주소값 호출
print(id(x2))
print(id(y2))
