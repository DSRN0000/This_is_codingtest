# 📍 문제 - 부품찾기
# 이진 탐색, 계수 정렬, 집합 자료형 이용.

# 이진 탐색
n = int(input())
ElectronicPartNumbers = list(map(int, input().split()))
m = int(input())
CustomerParts = list(map(int, input().split()))

ElectronicPartNumbers.sort()

def binarySearch (ElectronicPartNumbersList, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if ElectronicPartNumbersList[mid] == target:
            return mid
        elif ElectronicPartNumbersList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in CustomerParts:
    result = binarySearch(ElectronicPartNumbers, i, 0, n - 1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end= ' ')

# # 계수 정렬
# n = int(input())
# array = [0] * 10
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 집합 자료형
# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')