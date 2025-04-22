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

def _11050():
    from math import factorial
    n, k = map(int,input().split())
    print(factorial(n)//(factorial(k)*factorial(n-k)))

if __name__ == '__main__':
    _11050()