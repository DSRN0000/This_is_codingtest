# 📍 문제 - 숫자 카드 게임
# 🎯 목표 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾자

N, M = map(int, input().split())
min_a = 0
for _ in range(N):
    number = map(int, input().split())
    a = min(number)
    if min_a < a:
        min_a = a
print(min_a)

# # 답안 예시
# N, M = map(int, input().split())
# result = 0
# for i in range(N):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)