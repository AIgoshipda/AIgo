import abc
from os import abort
import sys
sys.stdin=open('input.txt', 'rt')

# 1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있을 때
# 각 카드의 위치는 카드 위에 적인 숫자와 같이 1부터 20까지로 나타낸다

# 구간 [a, b]가 주어지면 위치 a부터 b까지의 카드를 현재의 역순으로 놓는다

#a, b=map(int, input().split())
#print(a, b)
# a와 b 값 교환
#a, b=b, a
#temp=a
#a=b
#b=temp
#print(a, b)

a=list(range(21))
for _ in range(10): # _를 통해 저장되는 변수가 없이 반복문 실행
    s, e=map(int, input().split())
    # 1 2 3 4 5 6 7 8 9 -> 2 ~ 7 구간 뒤집기
    # 1 7 6 5 4 3 2 8 9 -> (7-2+1)//2 = 3 -> (e-s+1)//2, 짝수와 홀수 상관없이 가능
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i] # 앞쪽은 증가, 뒤쪽은 감소
# 0 제거
a.pop(0) # 0번 인덱스를 pop

for x in a:
    print(x, end=' ')