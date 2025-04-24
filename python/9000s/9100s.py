def _9184():
    import sys
    input = sys.stdin.readline

    def calc_val(num):
        a, b, c = num[0], num[1], num[2]
        key = f"{a}_{b}_{c}"
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if key not in memo:
            if a > 20 or b > 20 or c > 20:
                memo[key] = calc_val([20, 20, 20])
            elif a < b < c:
                memo[key] = (calc_val([a, b, c - 1]) +
                             calc_val([a, b - 1, c - 1]) -
                             calc_val([a, b - 1, c]))
            else:
                memo[key] = (calc_val([a - 1, b, c]) +
                             calc_val([a - 1, b - 1, c]) +
                             calc_val([a - 1, b, c - 1]) -
                             calc_val([a - 1, b - 1, c - 1]))
        return memo[key]

    memo = {}

    while True:
        nums = list(map(int, input().split()))
        if nums == [-1, -1, -1]:
            break

        print(f"w({', '.join(map(str, nums))}) = {calc_val(nums)}")

if __name__ == '__main__':
    _9184()