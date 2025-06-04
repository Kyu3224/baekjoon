def _11005():
    num_10, num_type = map(int, input().split())
    num_b = ""
    max_digit = 0
    while True:
        if num_10 >= num_type ** max_digit:
            max_digit += 1
            continue
        else:
            break

    for i in range(max_digit, 0, -1):
        digit = num_10 // num_type ** (i - 1)
        num_10 -= digit * num_type ** (i - 1)
        if digit >= 10:
            num_b += chr(digit - 10 + ord('A'))
        elif digit == 0 and num_b == "":
            continue
        else:
            num_b += str(digit)
    print(num_b)

def _11021():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print(f"Case #{i + 1}: {a + b}")

def _11022():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print(f"Case #{i + 1}: {a} + {b} = {a + b}")

def _11047():
    num_coins, target = map(int, input().split())
    coins = []
    for i in range(num_coins):
        coins.append(int(input()))
    num_coins = 0
    for coin in reversed(coins):
        if target == 0:
            break
        if target // coin == 0:
            continue
        else:
            coin_used = target // coin
            num_coins += coin_used
            target -= coin * coin_used
    print(num_coins)

def _11050():
    from math import factorial
    n, k = map(int,input().split())
    print(factorial(n)//(factorial(k)*factorial(n-k)))

def _11053():
    num_seq = int(input())
    num_list = list(map(int, input().split()))

    dp = [1] * num_seq

    for i in range(1, num_seq):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

def _11054():
    num_seq = int(input())
    num_list = list(map(int, input().split()))

    dp_inc = [1] * num_seq
    dp_dec = [1] * num_seq

    for i in range(1, num_seq):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
            if num_list[num_seq - j - 1] < num_list[num_seq - i - 1]:
                dp_dec[num_seq - i - 1] = max(dp_dec[num_seq - i - 1], dp_dec[num_seq - j - 1] + 1)

    dp_tot = [x + y for x, y in zip(dp_inc, dp_dec)]
    print(max(dp_tot) - 1)


if __name__ == '__main__':
    _11050()