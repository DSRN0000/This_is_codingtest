# 📍 문제 - 성적이 낮은 순서로 학생 출력하기
# 파이썬 기본 정렬 라이브러리 사용. key 파라미터 lambda 사용

n = int(input())
li = list()
for _ in range(n):
    data = input().split()
    li.append((data[0], int(data[1])))

li = sorted(li, key=lambda x: x[1]) #value 값을 기준으로 정렬한다.

for i in li:
    print(i[0], end=' ')