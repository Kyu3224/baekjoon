def _9461():
    def dp(n, _memo):
        if n not in _memo:
            _memo[n] = dp(n - 1, _memo) + dp(n - 5, _memo)
        return _memo[n]

    memo = {}

    num_input = int(input())
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2
    for i in range(num_input):
        num = int(input())
        print(dp(num, memo))

def _9498():
    score = int(input())
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

if __name__ == "__main__":
    _9498()