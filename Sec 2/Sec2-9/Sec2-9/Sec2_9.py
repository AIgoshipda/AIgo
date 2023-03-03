import sys
sys.stdin=open("input.txt", "rt")

# 1부터 6까지의 주사위 3개를 던져 상금을 받는 게임
# 규칙(1) 같은 눈이 3개 나오면 10,000+같은 눈*100원
# 규칙(2) 같은 눈이 2개만 나오면 1,000+같은 눈*100원
# 규칙(3) 모두 다른 눈이 나오면 그 중 가장 큰 눈*100원
# 가장 많은 상금을 받은 사람의 상금 출력

n=int(input())
'''
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))

cnt=[0]*6
def count(a):
    for i in a:
        cnt[i-1]+=1  
    for idx, i in enumerate(cnt):
        if i==3:
            return 10000+(idx+1)*100
        elif i==2:
            return 1000+(idx+1)*100
        elif i==1:
            max=-2147000000
            if idx+1>max:
                max=idx+1
    return max*100

print(max(count(a), count(b), count(c)))
'''
res=0
for i in range(n):
    tmp=input().split()
    #print(tmp) # ['6', '2', '5']
    tmp.sort()
    a, b, c=map(int, tmp)
    #print(a, b, c) # 6 2 5

    # 눈이 모두 같을 경우
    if a==b and b==c:
        money=10000+(a*100)
    # 눈 2개가 같을 경우
    elif a==b or a==c: # 한 눈을 기준으로(a 기준)
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=1000+(c*100)
    if money>res:
        res=money
print(res)