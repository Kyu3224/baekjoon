def _15996():
    n, a = map(int, input().split())
    if n <= 1:
        print(0)
    else:
        count = 0
        div = a
        while div <= n:
            count += n // div
            div *= a
        print(count)

if __name__ == '__main__':
    _15996()