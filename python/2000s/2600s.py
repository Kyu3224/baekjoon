def _2630():
    def recur_div(size, arr, counter):
        total_value = 0
        for row in arr:
            total_value += sum(row)
        if total_value == 0:
            counter['n_white'] += 1
        elif total_value == size ** 2:
            counter['n_blue'] += 1
        else:
            half = size // 2
            recur_div(half, [row[:half] for row in arr[:half]], counter)
            recur_div(half, [row[:half] for row in arr[half:]], counter)
            recur_div(half, [row[half:] for row in arr[:half]], counter)
            recur_div(half, [row[half:] for row in arr[half:]], counter)

    import sys
    from collections import defaultdict
    _input = lambda: sys.stdin.readline().strip()
    num_input = int(_input())
    board_array = [list(map(int, _input().split())) for i in range(num_input)]
    counter = defaultdict(int)
    recur_div(num_input, board_array, counter)
    print(counter['n_white'], counter['n_blue'], sep="\n")

def _2657():
    num = int(input())
    for i in range(num):
        a, b = input().split()
        word = ""
        for j in range(len(b)):
            word += b[j] * int(a)
        print(word)

if __name__ == '__main__':
    _2657()