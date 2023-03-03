from io import RawIOBase
import sys
from typing import Reversible
sys.stdin=open("input.txt", "rt")

# 1부터 100 사이의 자연수가 적힌 카드 N장(중복 가능)
# 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록
# 기록한 값 중 K번째로 큰 수를 출력해라(중복은 건너뜀)

n, k=map(int, input().split())
a=list(map(int, input().split()))

# 중복 제거 위해 set 사용
res=set()

# 1 2 3 4 5
# 1 2 3, 1 2 4, 1 2 5
# 1 3 4, 1 3 5
# 1 4 5 ...
for i in range(n): # list 0번부터
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])
