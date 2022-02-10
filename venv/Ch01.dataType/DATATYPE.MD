# 자료형 심화

## 01. 문자열 다루기 (메서드 학습)
```buildoutcfg
* 소문자를 대문자로 변경하는 방법
    - .upper()
    
* 대문자를 소문자로 변경하는 방법
    - .lower()
    
* 문자열 바꾸는 방법
    - .replace("바꿀문자","바뀔문자")
    
* 문자열 위치 찾는 방법 ( 찾은 문자열의 인덱스를 반환 )
    - .find("찾을문자열")    
    
* 문자열 개수 세는 방법
    - .count("cat")
    
* 문자열 분리하는 방법
    - .split()
    
* 문자열 연결하는 방법
    - .join(['연결할','문자열'])
    
* 공백 삭제하는 방법
    - .lstrip() #왼쪽 공백 삭제
    - .rstrip() #오른쪽 공백 삭제
    - .strip()  #양쪽 공백 삭제
```

## 02. 문자열 포맷팅
```buildoutcfg
1. format 메서드

    (1). 값을 넣을 때
    '{인덱스}'.format(데이터)
    
    >>> 'Hello {0}.format('startcoding')
    'Hello startcoding'
    
    (2). 값을 여러개 넣을 때
    >>> 'Hello {0} {1} {2}.format('apple','pineapple','pen')
    'Hello aplle pineapple pen'
    
    (3). 인덱스 생략 방법
    >>> 'Hello {} {} {}.format('apple','pineapple','pen')
    'Hello aplle pineapple pen'
    
2. f-string
    name1 = 'apple'
    name2 = 'pineapple'
    name3 = 'pen'
    
    >>> msg = f'{name1} {name2} {name3}'
    'apple pineapple pen'
```

## 03.List 자료형
```buildoutcfg
1. 리스트 데이터 추가방법
    - .append(추가할 데이터(리스트도 가능))
    
2. 리스트 데이터 삭제하는 방법
    - .pop()
    
3. 리스트 데이터 삭제하는 방법(인덱스 사용)
    - .pop(없앨 위치의 인덱스)
    
4. 리스트 데이터 삭제하는 방법(데이터 사용)
    - .remove("삭제할 데이터의 내용")
    
5. 리스트의 특정 값의 인덱스 구하는 방법
    - .index('구하려는 데이터')
    
6. 리스트 안에서 특정 값의 개수를 구하는 방법
    - .count('구하려는 데이터')

7. 리스트 안에서 모든 요소 삭제 하는 방법
    - .clear()
    
8. 리스트 정렬하기
    - .sort()
    
9. enumerate : for in 반복문 사용할 때 인덱스를 같이 출력하는 방법

numbers = [5, 2, 8, 1, 10]
for index, number in enumerate(numbers):
    print(index, number)
```

## 04. 리스트 내포
```buildoutcfg
* 리스트를 for 문, if 문등을 지정하여 리스트를 간편하게 만드는 방법
1️⃣ 1번째로 for 문
2️⃣ 2번째로 if 문
3️⃣ 3번째로 표현식
4️⃣ 4번째로 리스트

✔ [표현식 for 변수 in 순회가능한 데이터]
    >>> nums = [i for i in range(5)]
    >>> print(nums)
    [0,1,2,3,4]
    
    >>> nums = [100,200,300]
    >>> double_nums = [i*2 for i in nums]
    print(double_nums)
    [200,400,600]
    
✔ [표현식 for 변수 in 순회가능한 데이터 if 조건식]
    >>> nums = [i for i in range(10) if i % 2 ==0]
    >>> print(nums)
    [0,2,4,6,8]
    
    >>>nums=[100,200,300,400,500]
    >>>double_nums=[i*2 for i in nums if i >= 300]
    print(double_nums)
    [600,800,1000]
```

