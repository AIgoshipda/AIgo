
import sys
sys.stdin=open("input.txt", "rt")

# K��° ���
# � �ڿ��� p�� q�� ���� ��, ���� p�� q�� �������� �� �������� 0�̸� q�� p�� ����̴�
# �� ���� �ڿ��� N�� K�� �־����� ��, 
# N�� ����� �� K��°�� ���� ���� ����ϴ� ���α׷��� �ۼ��ض�
# K��° ����� ���ٸ� -1 ���

n, k = map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
# for���� ���������� ������ ��� -> K��° ����� ã�� ������ ���
else: print(-1) 