def _2657():
    num = int(input())
    for i in range(num):
        a, b = input().split()
        word = ""
        for j in range(len(b)):
            word += b[j] * int(a)
        print(word)

if __name__ == '__main__':
    _2657()