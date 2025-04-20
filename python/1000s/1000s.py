def _1010():
    from math import factorial
    for i in range(int(input())):
        n, m = map(int,input().split())
        print(factorial(m) // (factorial(n) * factorial(m - n)))

def _1037():
    _ = int(input())
    nums = sorted(list(map(int, input().split())))
    print(nums[0] * nums[-1])

if __name__ == '__main__':
    # _1010()
    _1037()