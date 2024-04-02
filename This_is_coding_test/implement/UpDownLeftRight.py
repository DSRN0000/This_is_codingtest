# 📍 문제 - 상하좌우

n = int(input())
direction = input().split()
a, b = 1, 1
for i in direction: #하나씩 모든 경우의 수를 다 작성한것은 가독성과 유지보수가 좋지 않을 듯 하다.
    if i == 'L':
        b = b - 1
        if b == 0:
            b = b + 1

    if i == 'R':
        b = b + 1
        if n < b:
            b = b - 1

    if i == 'U':
        a = a - 1
        if a == 0:
            a = a + 1

    if i == 'D':
        a = a + 1
        if n < a:
            a = a - 1
print(a, b)

# #답안예시
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dx[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
# print(x, y)