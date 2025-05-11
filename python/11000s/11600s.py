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

if __name__ == '__main__':
    _11654()