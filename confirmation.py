from math import *

# 定義
VALUE = 20

def convert_fizzbuzz_str(i):
    if(i % 15 == 0):
        return 'FizzBuzz'
    elif(i % 3 == 0):
        return 'Fizz'
    elif(i % 5 == 0):
        return 'Buzz'
    else:
        return str(i)

def calc_str_length(index):
    # fizz buzz における、index番目の文字数を返す関数
    length = 0
    for i in range(1, index + 1):
        length += len(convert_fizzbuzz_str(i))
    return length

def main():
    # n入力
    n = int(input())
    ans = ''

    left = 1
    right = 10**18

    while left < right:
        mid = (left + right) // 2
        length = calc_str_length(mid)
        if length < n:
            left = mid + 1
        else:
            right = mid

    for i in range(left, left + VALUE):
        ans += convert_fizzbuzz_str(i)

    print(ans[n - 1 : n - 1 + VALUE])

if __name__ == '__main__':
    main()