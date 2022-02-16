# 정규표현식
```buildoutcfg
✔ 장점
* 문자열 추출, 유효성 검사에서 유용하게 쓰일 수 있다.
* 거의 모든 언어에서 지원(범용성이 높다.)

✔ 단점
* 가독성이 좋지 못하다.
* 유지보수가 힘들다.
```

## 정규표현식 사용방법
```buildoutcfg
* Flags
* Character classes
* Anchors
* Escaped Characters


** Expression Flags
- global : 전체 텍스트에서 검색 할 수 있게 함
- multiline : 줄 별로 검색할 수 있게 함 

** Character classes
. : 모든 문자 중 1글자
\w : 알파벳, 숫자, _  모두 가져옴
\W : \w 의 반대 

\d : 숫자만
\D : 숫자가 아닌 것들만

\s : 공백
\S : 공백 빼고 다

[abc] : 모든 a 나 b 나 c 의 해당하는 것을 다 찾음
[^abc] : NOT [abc]

[a-g] : a-g 사이의 문자 한글은 [가-힣]20
[^a-g] : NOT [a-g]
[a-zA-Z0-9]

** Anchors
^abc$ : ^는 문장의 시작 , $는 문자의 끝

\b : 단어의 시작부분인가 끝부분인가
ex ) 시작 : \bapple 
     끝   : apple\b
     
 \B : \b의 반대
 
** Escaped characters
\. : 마침표 자체
\* : * 자체
\\ : 역슬래시 자체
\t : 탭
\n : 
\r :

** Quantifiers(수량자) & Alternation
rab*it : b가 0개 또는 1 이상 
    rait rabit rabbit rabbbit rabbbbit
rab+it : b가 1개 또는 1 이상
    rabit rabbit rabbbit rabbbbit
rab?it : b가 0개 또는 1개
    rait rabit
rab{4}it : b가 4개들어간 것 
    rabbbbit
rab{2,}it : b가 2개 이상인것 
    rabbit rabbbit rabbbbit
rab{1,3}it : b가 1개 ~ 3개 사이
    abit rabbit rabbbit

#.+?, : 비 greed 방식으로 바꿈 : 매치가 최소한으로 일어나는 기준으로 찾음
    #좋아요, #좋아요반사, #팔로우, #맞팔,
    위의 결과가 , 기준으로 나뉜다
#.{3,}?, : # 뒤 글자가 3개 이상인 것
    #좋아요, #좋아요반사, #팔로우,
#.{2,3}?,
    #좋아요, #팔로우, #맞팔,
gray|grey : gray 또는 grey를 찾아라
gr(e|a)y : 위랑 결과 똑같음 
gr[ae]y : 위랑 결과 똑같음

** Groups & Lookaround

#(.+?), : 안에 있는 특정한 것만 뽑고 싶을 때 사용
(.+)\s\1 : 단어가 1개또는 그 이상인 녀석을 그룹지어서 찾고 그뒤에 바로 공백이 있고 
            또 그 단어가 있을때 ( 역참조 )
 
\[(?:특가할인|품절)].* : 특가할인 품절을 그룹에 넣지않고 단순히 찾을 때만 쓰고 싶을 때 ?: 사용
.*(?=-레몬스토어) : -레몬스토어를 단어를 제외하고 전방의 정보를 찾고 싶다.
.*-(?!레몬) : 레몬이 붙어있는 것을 제외한 전방의 정보를 찾고싶다.
.*(?=-(?!레몬).*스토어) : 스토어중 레몬스토어가 아닌 것의 내용만 찾고싶을때(ㅇㅇ 스토어 내용 포함 x)
```

## re 모듈 사용
```buildoutcfg

(regex, 문자열)

* re모듈의 메서드(종류 : 기능, 찾는경우, 없는 경우 )
    - match : 문자열의 처음부터 검색 , match object 1개 반환 , None
    - search : 문자열 전체를 검색  , match object 1개 반환 , None
    - findall : 문자열 전체를 검색 , 문자열리스트, 빈리스트
    - finditer : 문자열 전체를 검색 , match object iterator, None
    - fullmatch : 패턴과 문자열이 남는부분없이 완벽하게 일치, match object 1개 반환 , None
    
    ✔ iter (순서)
* match 객체의 메서드 ( 종류 : 기능, ex )
    - group : 매칭된 문자열을 반환 , people
    - start : 매칭된 문자열의 시작위치, 5
    - end : 매칭된 문자열의 끝 위치, 11
    - span : 매칭된 문자열의 (시작,끝)튜플, (5,11)
```