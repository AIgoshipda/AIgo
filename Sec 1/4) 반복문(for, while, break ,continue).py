'''
반복문(for, while)
'''
a=range(10)
print(list(a))
a=range(1, 11)
print(list(a))

for i in range(1, 10):
    print(i, 'hello')

print('\n')

for i in range(10, 0, -2):
    print(i, 'hello')

print('\n')

i=1
while i<=10:
    print(i)
    i=i+1 # 1 -> 10

print('\n')

i=10
while i>=1:
    print(i)
    i=i-1 # 10 -> 1

print('\n')

i=1
while True: # 무한루프
    print(i)
    if i==5:
        break # 5일 때 while문 탈출
    i+=1

print('\n')

for i in range(1, 11):
    if i%2==0:
        continue # 짝수 제외
    print(i)

print('\n')

for i in range(1, 11):
    print(i)
    if i>15:
        break
else:
    print(11) # for문이 정상적으로 종료 됐을 경우 출력(break 됐을 때 X)
    
