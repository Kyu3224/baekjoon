def _14215():
    sticks = list(map(int, input().split()))
    max_length = max(sticks)
    while max_length >= sum(sticks) - max(sticks):
        max_length -= 1
    print(sum(sticks) - max(sticks) + max_length)

if __name__ == '__main__':
    _14215()