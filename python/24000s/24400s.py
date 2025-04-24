def _24416():
    def fibonacci_dp(n):
        cnt = 0
        f = [1, 1]
        for i in range(2, n):
            cnt += 1
            f.append(f[i - 1] + f[i - 2])
        return f[n - 1], cnt

    print(*fibonacci_dp(int(input())))

if __name__ == '__main__':
    _24416()