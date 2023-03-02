'''
리스트와 내장함수(2)
'''
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

# 리스트 요소 접근하기1
for i in range(len(a)):
    print(a[i], end=' ')
print()

# 리스트 요소 접근하기2
for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2==1:  # 홀수만 출력
        print(x, end=' ') 
print()

for x in enumerate(a): # 인덱스 번호까지 -> 튜플 형태로
    print(x)

b=[1, 2, 3, 4, 5]
print(b[0])
b[0]=7
print(b[0]) # 리스트는 수정 가능

b=(1, 2, 3, 4, 5) 
print(b[0])
# b[0]=7 튜플은 수정 불가능

# index, value 출력하기1
for x in enumerate(a):
    print(x[0], x[1]) # (index, value)
print()

# index, value 출력하기2
for index, value in enumerate(a):
    print(index, value)
print()

# all, any
if all(60>x for x in a): # all : 모두 참이면 True
    print("YES")
else:
    print("NO")

if any(15>x for x in a): # any : 하나라도 참이면 True
    print("YES")
else:
    print("NO")
