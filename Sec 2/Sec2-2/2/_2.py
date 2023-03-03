import sys
sys.stdin=open("input.txt", "rt")

# N개의 숫자로 이루어진 숫자열이 주어지면
# 해당 숫자열 중에서 s번째부터 e번째 까지의 수를
# 오름 차순으로 정렬했을 때 k번째로 나타나는 숫자를 출력하시오

T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split())) # list화
    a=a[s-1:e] # s번째부터 e번째까지
    a.sort()
    print("#%d %d" %(t+1, a[k-1])) # k번째 숫자
