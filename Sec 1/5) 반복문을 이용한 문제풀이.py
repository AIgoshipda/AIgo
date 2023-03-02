'''
반복문을 이용한 문제풀이
    1) 1부터 N까지 홀추 출력하기
    2) 1부터 N까지의 합 구하기
    3) N의 약수 출력하기
'''

n=int(input("숫자 입력 : "))

# 1
for i in range(1, n+1):
    if i%2==1:
        print(i)


# 2
sum=0
for i in range(1, n+1):
    sum+=i  # sum = sum+i
print(sum)

# 3
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ') # 줄바꿈 삭제
