# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=ja


class Dictionary:
    def __init__(self):
        self.test = set()

    def insert(self, data: str) -> None:
        self.test.add(data)

    def find(self, data: str) -> bool:
        return data in self.test


if __name__ == "__main__":
    n = int(input())
    dictionary = Dictionary()

    for _ in range(n):
        command = input().split()
        if command[0] == "insert":
            dictionary.insert(command[1])
        elif command[0] == "find":
            result = dictionary.find(command[1])
            print("yes" if result else "no")
