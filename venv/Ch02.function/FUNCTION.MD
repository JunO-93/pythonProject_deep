# 함수 중급파트

## 파라미터
```buildoutcfg
* 다양한 매개변수 (*args, **kwargs)
* 람다함수
* map 함수
* filter 함수

- 위치 매개변수 (positional parameter)
    * 가장 기본적인 매개변수
    * 함수를 호출할 떄 순서대로 데이터를 넘겨줘야 한다.
    * 다른 매개변수와 함꼐 쓸 때는 항상 맨 앞에 써야한다.
    
    ✔ 함수정의
    def my_func(a,b):
        print(a,b)
        
    ✔ 함수호출
    my_func(1, 2)
    
- 기본 매개변수 (default parameter)
    * 매개변수의 기본적인 값
    * 함수를 정의할 떄 매개변수의 기본 값을 지정할 수 있다.
    
   ✔ 함수정의 
   def post_info(title, content ='내용없음'):
       print('제목:',title)
       print('내용:', content)
       
   ✔ 함수호출    
   post_info("출석합니다!")
   
   출력 
   제목 : 출석합니다!
   내용 : 내용없음
   
- 키워드 매개변수(keyword parameter)
    * 함수 호출 시에 키워드를 붙여 호출한다.
    * 매개변수의 순서를 지키지 않아도 된다.
    
   ✔ 함수정의 
   def post_info(title, content):
   print('제목:',title)
   print('내용:', content)
   
   ✔ 함수호출   
   post_info(content='없어요', title='여자친구 만드는 방법')
   
   출력
   제목 : 여자친구 만드는 방법
   내용 : 없어요
   
```

## 파라미터 2
```buildoutcfg
* 위치 가변 매개변수 (positilnal variable length parameter)
    - 가변 매개변수 = 개수가 정해지지 않은 매개변수
    - 매개변수 앞에 *가 붙는다. (튜플형)
    
    ✔ 함수정의
    def print_fruits(*args):
        for arg in args:
            print(arg)
    ✔ 함수호출
    print_fruits('apple', 'orange', 'mango')
    
    출력
    apple
    
    orange
    
    mango
    
* 키워드 가변 매개변수 (keyword variable length parameter)
    - 매개변수 앞에 **가 붙는다. (딕셔너리형)
    
    ✔ 함수정의
    def comment_info(**kwargs):
        for key, value in kwargs.items():
            print(f'{key} : {value}')
    ✔ 함수출력
    comment_info(name:'파린이',content='정말 감사합니다.!')
    
    출력
    name : 파린잉
    content : 정말 감사합니다!    
```

## 람다함수
```buildoutcfg
* 이름을 지을 필요도 없을 간단한 형태의 함수
* 다른 함수의 인자(argument)로 넣을 수 있다.
* 코드가 간결해 지고, 메모리가 절약된다.

✔ 기존 함수 정의 방법

    def 함수이름(매개변수):
        return 결과
    
    def minus_one(a):
        return a-1

✔ 람다 함수 정의 방법

    lambda 매개변수 : 결과
    
    lambda a:a-1

✔ 기존 함수 호출 방법

    >>> minus_one(10)
    9

✔ 람다 함수 호출 방법
    
    1. 
    >>> (lambda a:a-1)(10)
    9
    
    2.
    >>> minus_one=lambda a:a-1
    >>> minus_one(10)
    9

✔ 기존 함수 정의방법 (if문)
     def is_positive_number(a):
        if a>0:
            return True
        else:
            return False

✔ 람다 함수 정의방법 (if문)
    lambda a: True if a > else False
    
✔ 기존 함수 호출 방법 (if문)

    >>> is_positive_number(-2)
    False

✔ 람다 함수 호출 방법 (if문)
    >>> (lambda a:True if a >0 else False)(-2)
    False
```

## Map & filter
```buildoutcfg
* map 함수 사용 방법( + 람다 함수)

    map(함수, 순서가있는자료형)
    ✔ 예시 : 숫자로 바꿔주는 함수
    map(int,['3','4','5','6'])
    1. ['3','4','5','6'] 은 int 함수를 거치게 되고
    2. map object로 만들어낸다 (3, 4, 5, 6)
        
    ✔ map object 를 리스트로 바로 변환 
    list(map(int,['3','4','5','6']))
    
    1) 리스트의 모든 요소의 공백 제거(for문 사용)
    items = [' 로지텍마우스 ',' 앱솔키보드 ']
    for i in range(len(items)):
        items[i]=items[i].strip()
        
    2) map을 사용했을 때
    def strip_all(x):
        return x.strip()
    items = [' 로지텍마우스 ',' 앱솔키보드 ']
    items=list(map(strip_all,items))
    
    3) 함수 이름까지 붙이기 귀찮을 때
    items = [' 로지텍마우스 ',' 앱솔키보드 ']
    items = list(map(lambda x : x.strip(),items))
    
* filter 함수 사용 방법 ( + 람다 함수)

    filter(함수,순서가있는자료형
    def func(x):
        return x < 0
    filter(func, [-3,-2,0,5,7])
    
    1. [-3,-2,0,5,7] 는 func을 거치게 되고
    2. func 의 return 조건에 해당하는 값만 filter object로 뽑아준다
    3. list(filter(func, [-3, -2, 0, 5, 7])) 로 바로 리스트화 가능 
    
    ✔ 예시 : 리스트에 길이가 3이하인 문자들만 필터링
    1) for문 사용했을 때
    animals = ['cat','tiger','dog','bird','monkey']    
    result = []
    
    for i in animals:
    if len(i) <=3:
        result.append(i)
        
    2) filter 사용했을 때
    animals = ['cat','tiger','dog','bird','monkey']    
    def word_check(x):
        return len(x) <=3
    result = list(filter(word_check,animals)) 
    
    3) 람다함수 사용했을 때
    animals = ['cat','tiger','dog','bird','monkey']
    result = list(filter(lambda x : len(x) <=3,animals))    
```
