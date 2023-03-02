'''
문자열과 내장함수
'''
msg="It is Time"

# 대문자
print(msg.upper()) # 출력만
print(msg)
print()

# 소문자
print(msg.lower())
print(msg)
print()

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))    # 문자열 인덱스 번호 출력
print(tmp.count('T'))   # count
print(msg)

# slice
print(msg[:2])  # It
print(msg[3:5]) # is
print(len(msg)) # len
print()

# 응용
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg: # msg 문자열 하나씩 접근
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): # 대문자면 True
        print(x, end=' ')
print()

for x in msg:
    if x.islower(): # 소문자면 True
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳이면 True(공백 제거)
        print(x, end=' ')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # ascii number 출력
print()

tmp='az'
for x in tmp:
    print(ord(x))
print()

tmp=65
print(chr(tmp)) # ascii number -> 문자
