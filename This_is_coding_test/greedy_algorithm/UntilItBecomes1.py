# 📍 문제 - 1이 될 때까지
# 🎯 목표 : 최대한 많이 나누기

n, k = map(int, input().split())
cnt = 0
while(2 <= n):
    if n % k == 0:
        n = n / k
        cnt += 1
    else:
        n = n - 1
        cnt += 1
print(cnt)

# #답안예시
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     # (n == k로 나누어떨어지는 수)가 될때까지 1씩 빼기
#     target = (n//k) * k
#     result += (n - target)
#     n = target
#
#     # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     result += 1
#     #k로 나누기
#     n //= k
#
# #마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)