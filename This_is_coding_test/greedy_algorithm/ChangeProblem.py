# 📍 문제 - 거스름돈 문제

# 🎯 목표 : 가장 큰 화폐 단위부터 돈을 거슬러 주자.

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n //coin
    n %= coin

print(count)