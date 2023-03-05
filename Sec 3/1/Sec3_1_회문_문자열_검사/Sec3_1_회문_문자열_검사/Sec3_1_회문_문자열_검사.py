import sys
sys.stdin=open('input.txt', 'rt')

# N개의 문자열 데이터를 입력받아
# 앞에서 읽을 때나 뒤에서 읽을 때나 같으면 YES
# 회문 문자열이 아니면 NO 출력
# 회문을 검사할 때 대소문자 구문X

n=int(input())

'''
# Case 1
for i in range(n):
    s=input()
    # 소문자 -> 대문자
    s=s.upper()
    # 비교를 위한 문자열 길이
    size=len(s)
    for j in range(size//2):
        # l e v e l
        # 0 1 2 3 4
        # 0과 4/1과 3 비교
        # 5//2 = 2번 비교
        # s[j]!=s[-1-j] => 중요 ! ! !
        if s[j]!=s[-1-j]: # 회문이 아닐 경우
            print("#%d NO" %(i+1)) # case i
            break
    else: # 정상 종료가 되지 않았다면 = 회문
        print("#%d YES" %(i+1))
'''

# Case 2
# 가급적 Case 1처럼 직접 코딩 할 것
for i in range(n):
    s=input()
    s=s.upper()
    #print(s[::-1]) # reverse code
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else: # 회문이 아닌 경우
        print("#%d NO" %(i+1))
