def _15552():
    import sys

    num_sum = int(input())

    for i in range(num_sum):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

if __name__ == '__main__':
    _15552()