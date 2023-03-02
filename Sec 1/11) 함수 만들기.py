'''
함수 만들기
'''
def add(a, b): # 함수 생성(호출보다 위에 작성)
    c=a+b
    print(c)

add(3, 2)   # 함수 호출
add(5, 7)

def add(a, b):
    c=a+b
    return c # return 후 함수 종료

x=add(3, 2) # return한 값을 저장
print(x)

def add(a, b):
    c=a+b
    d=a-b
    return c, d # 두 개의 값을 return -> 튜플 형태로

print(add(3, 2))

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')

