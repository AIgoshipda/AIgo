
import sys
sys.stdin=open("input.txt", "rt")

# 에라토스테네스 체
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력

n=int(input())
ch=[0]*(n+1)
cnt=0
'''
for i in range(2, n):
    if ch[i]==0:
        cnt+=1
        for j in range(2, n):
            if j%2==0:
                ch[i]+=1
'''

for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i): # i의 배수씩 증가
            ch[j]=1

print(cnt)