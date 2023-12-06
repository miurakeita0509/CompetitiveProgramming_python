#定義
VALUE = 20

def tupple(n):
    return (n//3, n//5, n//15)

def range_num(a,b):
    taihi = tupple(a-1)
    taihi2 = tupple(b)
    return (taihi2[0] - taihi[0], taihi2[1] - taihi[1], taihi2[2] - taihi[2],)

print(tupple(100))
print(range_num(1,100))

n = int(input())

