# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0554

list = []

for i in range(4):
    time = int(input())
    list.append(time)
a = sum(list)

print(a // 60)
print(a % 60)
