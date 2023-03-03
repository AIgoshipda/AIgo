from os import terminal_size
import sys
sys.stdin=open("input.txt", "rt")

# N개의 자연수가 입력되면 각 자연수를 뒤집은 후
# 그 뒤집은 수가 소수이면 출력하는 프로그램
# def reverse(x)와 def isPrime(x) 사용

def reverse(x):
    res=0
    while x>0: # 0이면 break
        t=x%10 # x의 1의 자리 숫자
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):# 1과 자신을 제외한 다른 숫자 -> 2부터 -> 절반까지
        if x%i==0:
            return False
    else:
        return True

n=int(input())
a=list(map(int, input().split()))
for x in a: # list 각 숫자에 접근
    tmp=reverse(x)
    if isPrime(tmp): # True면 출력
        print(tmp, end=' ')
