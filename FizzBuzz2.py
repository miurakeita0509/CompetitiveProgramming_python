def onetone(n):
    return(n//3, n//5, n//15)

def rangemultiple(lef,rig):
    a = onetone(rig)
    b = onetone(lef - 1)
    return(a[0]-b[0], a[1]-b[1], a[2]-b[2])

print('onetone')
print(onetone(10))

print('rangemultiple')
print(rangemultiple(1,10))

def calc_len_n(n):
    lef = 1
    rig = 9
    ret = 0
    for i in range(20):
        if lef > n:
            break
        if rig > n:
            rig = n
        tup = rangemultiple(lef,rig)
        num = rig - lef + 1
        three = tup[0] - tup[2]
        five = tup[1] - tup[2]
        both = tup[2]
        ret += (i+1) * (num - three - five - both)
        ret += (three + five + both * 2) * 4

        lef *= 10
        rig = lef * 10 - 1
    return ret
    
s = int(input())

start = 0
end = 10 ** 18

while(abs(start - end) > 1):
#    print(start,end)
    middle = start + end
    middle //= 2
    h = calc_len_n(middle)
#    print(middle,h)
    if h < s:
        start = middle
    else:
        end = middle

print(start,end)
s -= calc_len_n(start)

a = ''

for i in range(end, end + 20):
    t = str(i)
    if i% 15 == 0:
        t = 'FizzBuzz'
    elif i % 3 == 0:
        t = 'Fizz'
    elif i % 5 == 0:
        t = 'Buzz'
    a += t

print(a[s-1:s+19])
