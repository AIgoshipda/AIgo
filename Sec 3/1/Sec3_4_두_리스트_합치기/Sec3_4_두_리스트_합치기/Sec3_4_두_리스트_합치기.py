# sort() -> 8log8
# 이미 정렬이 되어있기 때문에 8로 충분함
# a
# p1
# 0 1 2 3
# 1 3 5

# b
# p2
# 0 1 2 3 4 5
# 2 3 6 7 9

# c
# 1 2 3 3 5 6 7 9

# if a[p1]<=b[p2]: c.append(a[p1])
# else: b[p2]
# 이후 하나씩 증가시키기
# 끝까지 갔다면 break
# 남은 부분은 slice를 이용해 뒤로 붙이기

import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

p1=p2=0
c=[]

while p1<n and p2<m: # 둘 중 하나라도 끝까지 갔다면 중지
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n: # p1이 남음
    c=c+a[p1:] # p1부터 끝까지
if p2<m: # p2가 남음
    c=c+b[p2:] # p2부터 끝까지

# print
for x in c:
    print(x, end=' ')