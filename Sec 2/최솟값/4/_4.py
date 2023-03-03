# 최솟값 구하기
arr=[5, 3, 7, 9, 2, 5, 2, 6]
#arrMin=float('inf')
arrMin=arr[0]
for i in range(1, len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i] # 첫 값은 무조건 참
print(arrMin)

# 2
arrMin=float('inf')
for x in arr:
    if x<arrMin:
        arrMin=x
print(arrMin)