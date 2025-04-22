def _19532():
    coef = list(map(int, input().split()))
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if coef[0] * i + coef[1] * j == coef[2] and coef[3] * i + coef[4] * j == coef[5]:
                print(i, j)

if __name__ == '__main__':
    _19532()