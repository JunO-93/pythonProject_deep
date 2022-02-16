# 1. 위치 가변 매개변수

def print_fruits(*args):
    print(args)

print_fruits('apple','orange','mango','grape')


# 2. 키워드 가변 매개변수

def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value} ')

comment_info(name='파린이', content='정말 감사합니다!')


# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(*tags,title, content):
    print(f'제목: {title}')
    print(f'내용: {content}')
    print(f'태그: {tags}')

post_info("#파이썬", '#함수', '파이썬 함수 정리!', '다양한 매개변수 정리한다.')
# tags 에서 모든 인자를 가져가 버려서 title, content가 없다는 오류 발생
# 1. 해결방법 : 함수 가변매개변수를 맨 뒤로 넣는다.
# 2. 해결방법 : title 과 content를 키워드 매개변수로 변경한다.
# post_info("#파이썬", '#함수', title = '파이썬 함수 정리!', content = '다양한 매개변수 정리한다.')