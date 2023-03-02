'''
변수명 정하기
    1) 영문과 숫자, _로 이루어진다
    2) 대소문자를 구분한다
    3) 문자나, _로 시작한다
    4) 특수문자를 사용하면 안된다(&, % 등)
    5) 키워드를 사용하면 안된다(if, for 등)
'''

a=1
A=2
A1=3
# 2b=4 -> error
_2b=4
print(a, A, A1, _2b)

a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b=10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a=123453312312423432524647679730
print(a, type(a)) # int
a=12.12315342573
print(a, type(a)) # float:8byte까지
a='student'
print(a, type(a)) # str

# 출력방식
print("number")
a, b, c=1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ') # sep:구분자
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')

