
import sys
sys.stdin=open("input.txt", "rt")

# N개의 자연수가 입력되면 각 자연수의 자릿수 합을 구하고,
# 그 합이 최대인 자연수를 출력하는 프로그램
# 합을 구하는 함수는 def digit_sum(x)를 사용해 작성

n=int(input())
a=list(map(int, input().split()))

# 이중 for문을 통해 각 자리의 숫자를 이중 리스트에 저장하고자 했음
# 이중 리스트 저장 과정에서 막힘

# 1
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10 # 나머지
        x=x//10 # 몫
    return sum

for x in a: # list 원소 접근
    tot=digit_sum(x) # 각 자리수의 합
    max=-2147000000
    if tot>max:
        max=tot
        res=x
print(res)

# 2
def digit_sum2(x):
    sum=0
    for i in str(x): # 문자열에 하나씩 접근
        sum+=int(i) # 정수화
    return(sum)

max=-2147000000
for x in a: # list 원소 접근
    tot=digit_sum2(x) # 각 자리수의 합
    if tot>max:
        max=tot
        res=x
print(res)