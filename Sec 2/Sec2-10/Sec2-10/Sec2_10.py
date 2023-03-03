
import sys
sys.stdin=open("input.txt", "rt")

# OX문제로 이루어진 시험에서 연속 정답일 경우 가산점
# 처음 맞은 문제는 1점
# N연속 정답일 때마다 N점

n=int(input())
a=list(map(int, input().split()))

'''
tot=0
cnt=0 # 가중치
for i in range(len(a)):
    if a[i]==1:
        tot+=1
        if i>0 and a[i-1]==1:
            cnt+=1
    if a[i]==0:
        cnt=0 # 0 만나면 초기화
    tot+=cnt
print(tot)
'''
sum=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)