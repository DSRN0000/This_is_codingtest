# 📍 문제 - 두 배열의 원소 교체
# 파이썬 기본 정렬 라이브러리 사용. key 파라미터 lambda 사용

n, k = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())

a = sorted(a)
b = sorted(b, reverse = True) #내림차순 정렬

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))