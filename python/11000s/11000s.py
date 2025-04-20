def _11050():
    from math import factorial
    n, k = map(int,input().split())
    print(factorial(n)//(factorial(k)*factorial(n-k)))

if __name__ == '__main__':
    _11050()