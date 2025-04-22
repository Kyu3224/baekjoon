def _11650():
    pts = sorted([list(map(int, input().split())) for _ in range(int(input()))])
    for row in pts:
        print(*row)

def _11651():
    pts = [list(map(int, input().split())) for _ in range(int(input()))]
    for i in range(len(pts)):
        pts[i][1], pts[i][0] = pts[i][0], pts[i][1]
    for row in sorted(pts):
        row.reverse()
        print(*row)

def _11653():
    num = int(input())
    while num != 1:
        for i in range(2, int(num) + 1):
            if num % i == 0:
                num /= i
                print(i)
                break

def _11654():
    print(ord(input()))

if __name__ == '__main__':
    _11654()