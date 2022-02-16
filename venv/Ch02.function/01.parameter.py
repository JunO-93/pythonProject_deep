# 1. 위치매개변수

def my_func(a, b):
    print(a, b)

my_func(2, 3)

#2. 기본매개변수

def post_info(title, content='내용없음'):
    print(f'제목 : {title}')
    print(f'내용: {content}')

post_info('출석합니다!')

#3. 키워드 매개변수
# 함수 호출 시에 키워드를 붙여서 호출

def post_info(title, content):
    print(f'제목 : {title}')
    print(f'네용 : {content}')

post_info(content='없어요', title='여자친구 만드는 방법')