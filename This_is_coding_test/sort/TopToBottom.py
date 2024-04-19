# 📍 문제 - 위에서 아래로
# 파이썬 기본 정렬 라이브러리 사용

n = int(input())
li = list(input() for _ in range(n))
li = sorted(li, reverse = True)

for i in li:
    print(i, end= ' ')