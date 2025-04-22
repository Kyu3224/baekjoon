def _24313():
    big_o = list(map(int, input().split()))
    const = [int(input()) for _ in range(2)]
    if big_o[0] > const[0]:
        print(0)
    else:
        if big_o[0] * const[1] + big_o[1] > const[0] * const[1]:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    _24313()