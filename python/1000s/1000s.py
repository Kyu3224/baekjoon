def _1000():
    a1, a2 = map(int,input().split())
    print(a1 + a2)

def _1001():
    a1, a2 = map(int,input().split())
    print(a1 - a2)

def _1008():
    a, b = map(int, input().split())
    print(a / b)

def _1010():
    from math import factorial
    for i in range(int(input())):
        n, m = map(int,input().split())
        print(factorial(m) // (factorial(n) * factorial(m - n)))

def _1018():
    input_dim = list(map(int, input().split()))
    board_config = [input() for _ in range(input_dim[0])]
    color = {0: "W", 1: "B"}
    min_nums_to_color = 64
    for i in range(input_dim[0] - 7):
        for j in range(input_dim[1] - 7):
            for k in {0, 1}:
                nums_to_color = 0
                # Case when first starts with black
                for row_idx in range(8):
                    for col_idx in range(8):
                        if (row_idx + col_idx) % 2 == 0:
                            if board_config[i + row_idx][j + col_idx] == color[k]:
                                nums_to_color += 1
                        else:
                            if board_config[i + row_idx][j + col_idx] == color[1 - k]:
                                nums_to_color += 1
                if nums_to_color <= min_nums_to_color:
                    min_nums_to_color = nums_to_color
    print(min_nums_to_color)

def _1037():
    _ = int(input())
    nums = sorted(list(map(int, input().split())))
    print(nums[0] * nums[-1])

def _1085():
    x, y, w, h = map(int, input().split())
    print(min(min(x, w - x), min(y, h - y)))

if __name__ == '__main__':
    # _1010()
    _1037()