'''
람다 함수
'''
def plus_one(x):
    return x+1

print(plus_one(1))

# 람다 함수
plus_two=lambda x:x+2
print(plus_two(1))

# 내장함수의 인자로 많이 사용
a=[1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))

# sort 함수의 인자로 많이 사용
