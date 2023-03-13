
import sys
sys.stdin=open('input.txt', 'rt')

# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출해서
# 순서대로 자연수를 만들고 만들어진 자연수와 자연수의 약수 개수를 출력

s=input()
res=0
#result = []
for i in s:
    # isdecimal : 0~9
    # isdigit : 숫자
    if i.isdigit():
        res=res*10+int(i) # int화 -> 첫 자리의 0은 무시가 된다
print(res)

cnt=0
for i in range(1, res+1):
    if res%i==0: # 나눠떨어진다면 약수
        cnt+=1
print(cnt)