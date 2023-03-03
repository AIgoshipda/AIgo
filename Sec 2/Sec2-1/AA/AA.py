
import sys
sys.stdin=open("input.txt", "rt")

# K번째 약수
# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다
# 두 개의 자연수 N과 K가 주어졌을 때, 
# N의 약수등 중 K번째로 작은 수를 출력하는 프로그램을 작성해라
# K번째 약수가 없다면 -1 출력

n, k = map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
# for문이 정상적으로 끝났을 경우 -> K번째 약수를 찾지 못했을 경우
else: print(-1) 