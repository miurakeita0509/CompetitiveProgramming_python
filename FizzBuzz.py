from math import *
#定義
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


def calc_fizzbuzz(n):
    if(n % 15 == 0):
        return 8
    elif(n % 3 == 0):
        return 4
    elif(n % 5 == 0):
        return 4
    else:
        return keta(n)


def keta(n):
    return int(log10(n)) + 1


#def calc_str_length(index: number) -> number:
def calc_str_length(index):
    # fizz buzz における、index番目の文字数を返す関数
    length = 0
    length = calc_fizzbuzz(index)
    
    #ここで試行中
    return length


# 二分探索をする関数を定義 調査中
def binary_search(n):
    # 探索範囲
    left = 0
    right = 10 ** 18
    
    # 探索範囲を狭めていく
    while right - left  > 1:
        # 探索範囲の中央
        mid = (left + right) // 2
        length = calc_str_length(mid)
        if length < n:
            left = mid
        else :
            right = mid
    return False


def main():
    #n入力
    n = int(input())
    ans = ''

    a = 0
    a = calc_str_length(n)

    for i in range(a, a + VALUE):
        ans = ans + str(calc_fizzbuzz(i))

    print(ans[n - 1 : n + VALUE])


if __name__ == '__main__':
    main()
