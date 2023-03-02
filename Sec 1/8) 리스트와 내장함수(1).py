'''
리스트와 내장함수(1)
'''

import random as r

a=[]
print(a)

b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[0])

b=list(range(1, 11))
print(b)

c=a+b
print(c)

print(a)
a.append(6)     # append(맨 뒤에 6 추가)
a.insert(3, 7)  # insert(index 3에 7 추가)
print(a)
a.pop()         # 마지막 index pop
print(a)
a.pop(3)        # index 3 pop
print(a)
a.remove(4)     # 4 제거
print(a)
print(a.index(5))  # index() : 5의 index 출력 = 3

a=list(range(1, 11))
print(a)
print(sum(a))   # sum
print(max(a))   # max
print(min(a))   # min
print(min(7, 3, 5))

print(a)
r.shuffle(a) # 무작위
print(a)
a.sort()    # sort(오름차순)
print(a)
a.sort(reverse=True)    # 내림차순
print(a)
a.sort()    # 다시 오름차순
print(a)
a.clear()   # clear
print(a)
