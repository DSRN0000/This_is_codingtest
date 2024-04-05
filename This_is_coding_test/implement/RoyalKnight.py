# 📍 문제 - 왕실의 나이트

#수평2수직1 or 수직2수평1 이동가능
current_location = input()
col = int(ord(current_location[0])) - int(ord('a')) + 1 #ord() => 문자에 해당하는 유니코드로 변환. a -> 97
row = int(current_location[1])

direction = [(-2, -1), (-1, -2), (1, -2), (-2, 1), (2, 1), (1, 2), (-1, 2), (2, -1)]

cnt = 0
for d in direction:
    c = col + d[0]
    r = row + d[1]

    if 1 <= c and c <= 8 and 1 <= r and r <= 8:
        cnt += 1
print(cnt)