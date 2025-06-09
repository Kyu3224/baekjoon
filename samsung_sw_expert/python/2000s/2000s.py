def _2072():
    T = int(input())
    for test_case in range(1, T + 1):
        nums = list(map(int, input().split()))
        sums = 0
        for num in nums:
            sums = sums if num % 2 == 0 else sums + num
        print(f"#{test_case} {sums}")

if __name__ == '__main__':
    _2072()