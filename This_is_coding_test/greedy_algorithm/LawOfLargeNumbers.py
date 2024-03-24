# 📍 문제 - 큰 수의 법칙

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
big_num = max(numbers) #sort를 사용하지 않은 이유 : sort을 사용하면 시간복잡도가 커진다고 생각했다.
numbers.remove(max(numbers))
answer = 0

while  0 < M: #while
    if K < M:
        for _ in range(K):
            answer += big_num
        answer += max(numbers)
        M = M - K - 1
    else:
        answer += big_num
        M = M - 1
print(answer)

# 답안 ---------------------------------------
# 💯 키 포인트 : 반복되는 수열에 대해서 파악하자.
start_time = time.time() # 측정 시작
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)