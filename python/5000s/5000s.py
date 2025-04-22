def _5073():
    while True:
        lines = list(map(int, input().split()))
        if len(set(lines)) == 1:
            if lines[0] == 0:
                break
            else:
                print("Equilateral")
        else:
            if 2 * max(lines) >= sum(lines):
                print("Invalid")
            elif len(set(lines)) == 2:
                print("Isosceles")
            else:
                print("Scalene")

def _5086():
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        if b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        else:
            print("neither")