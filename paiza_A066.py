# https://paiza.jp/challenges/558/show


def calculate_max_consecutive_work_days(n, work_periods):
    # 100,000 日までの配列を用意し、全て 0 で初期化
    days = [0] * 100001

    # 各仕事の期間を配列にマーク
    for start, end in work_periods:
        for day in range(start, end + 1):
            days[day] = 1

    # 連続出勤日数を計算
    max_consecutive_days = 0
    current_streak = 0
    for day in days:
        if day == 1:
            current_streak += 1
            max_consecutive_days = max(max_consecutive_days, current_streak)
        else:
            current_streak = 0

    return max_consecutive_days


def main():
    n = int(input())
    work_periods = []

    for _ in range(n):
        start, end = map(int, input().split())  # 各行から開始日と終了日を読み込む
        work_periods.append((start, end))

    print(calculate_max_consecutive_work_days(n, work_periods))


if __name__ == "__main__":
    main()
