# n = 떡의 개수 , m = 요청받은 떡 길이
n, m = list(map(int, input().split()))
# 떡의 개별 높이 정보
riceCakes = list(map(int, input().split()))

start = 0
end = max(riceCakes)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in riceCakes:
        if i > mid:
            total += i - mid #떡이 잘린 경우 total에 저장
    if total < m: #요청 길이보다 작을 때
        end = mid - 1 #end값 수정
    else: #떡의 양 충분할 경우 덜 자르기
        result = mid #떡 길이 저장
        start = mid + 1
print(result)