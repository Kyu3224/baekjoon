def _27433():
    def factorial(n):
        if n > 1:
            return n * factorial(n - 1)
        else:
            return 1

    input_num = int(input())
    print(factorial(input_num))

if __name__ == '__main__':
    _27433()