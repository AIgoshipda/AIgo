import sys
sys.stdin=open('input.txt', 'rt')

# N개의 수로 된 수열 A[1], A[2], ..., A[N]이 있다
# 이 수열의 i번째 수부터 j번째 수까지의 합
# A[i]+A[i+j]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램

# a개 중 부분합이 b가 되는 경우의 수
# a
#lt rt
# 0 1 2 3 4 5 6 7 
# 1 2 1 3 1 1 1 2
# tot : lt ~ rt 인덱스 직전까지 연속 부분 합
# tot=a[0] -> 처음
# tot < m -> rt 증가 -> rt+1
# tot = m -> cnt+1 -> rt-rt값, lt+1
# tot > m -> 
# lt와 rt는 같을 순 있어도 lt가 rt보다 클 순 없다
# rt=n일 경우 break
# 마지막 자료가 n보다 클 때 lt=rt=0

n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else: # rt=n
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else: # tot>m
        tot-=a[lt]
        lt+=1
print(cnt)
