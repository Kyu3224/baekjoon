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

def _11659():
    import sys
    _input = sys.stdin.readline

    n, num_sum = map(int, _input().split())
    items = list(map(int, _input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + items[i - 1]

    for _ in range(num_sum):
        start_idx, end_idx = map(int, _input().split())
        result = prefix_sum[end_idx] - prefix_sum[start_idx - 1]
        print(result)


def _11660():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().strip().split())
    main_table = [[0] * (n + 1) for i in range(n + 1)]
    sum_table = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        main_table[i][1:] = list(map(int, input().strip().split()))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum_table[i][j] = main_table[i][j] + sum_table[i][j - 1] + sum_table[i - 1][j] - sum_table[i - 1][j - 1]
    for i in range(m):
        x1, y1, x2, y2 = map(int, input().strip().split())
        print(sum_table[x2][y2] - sum_table[x2][y1 - 1] - sum_table[x1 - 1][y2] + sum_table[x1 - 1][y1 - 1])


if __name__ == '__main__':
    _11654()