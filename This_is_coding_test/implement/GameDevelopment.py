# 📍 문제 - 상하좌우
# 💯 문제해결 팁 : 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx,dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다.

n, m = map(int, input().split())
a, b, direction = map(int, input().split())

map = list([0] * m for _ in range(n)) #방문한 위치를 저장하기 위한 맵 생성. 0으로 초기화. 컴프리헨션 이용

array = list() #사용자 입력으로 맵 정보 받아오기
for _ in range(n):
        array.append(input().split())

#북,동,남,서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): #왼쪽 회전
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = a + dx[direction]
    ny = b + dy[direction]
    if map[nx][ny] == 0 and int(array[nx][ny]) == 0: #가보지 않은 칸 그리고 갈 수 있는 칸 존재하는 경우
        map[nx][ny] = 1
        a = nx
        b = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4: #4방향 모두 가보았거나 바다인 경우
        nx = a - dx[direction]
        ny = b - dy[direction]
        if array[nx][ny] == 0: # 뒤로 이동 가능한 경우
            a = nx
            b = ny
        else:
            break
        turn_time = 0
print(cnt)

