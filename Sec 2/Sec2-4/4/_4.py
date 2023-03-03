from os import TMP_MAX, X_OK
import sys
sys.stdin=open("input.txt", "rt")

# N명의 수학성적으로 평균(소수 첫째자리 반올림)을 구하고
# 평균에 가장 가까운 학생은 몇 번째 학생인지 구하시오
# 중복일 경우 성적이 높은 학생의 번호 출력
# 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호 출력

n=int(input())
a=list(map(int, input().split()))

# round -> roud_half_even
ave=round(sum(a+0.5)/n)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave) # tmp가 가장 작은 학생이 평균에 가장 가까운 학생
    if tmp<min:
        min=tmp
        score=x 
        res=idx+1
    elif tmp==min: # 중복
        if x>score:
            score=x # score에 저장된 이전 값과 비교해서 저장
            res=idx+1
print(ave, res)
