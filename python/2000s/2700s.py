def _2720():
    num_test_case = int(input())
    coin_type = [25, 10, 5, 1]
    test_cases = []
    for i in range(num_test_case):
        money_to_return = int(input())
        result = []
        for j in range(len(coin_type)):
            coins_to_give = 0
            while True:
                if coin_type[j] * (coins_to_give + 1) <= money_to_return:
                    coins_to_give += 1
                    continue
                else:
                    break
            result.append(coins_to_give)
            money_to_return -= coin_type[j] * coins_to_give
        test_cases.append(result)

    for row in test_cases:
        print(*row)

def _2738():
    row, col = map(int, input().split())
    num_mat = 2
    mat_tot = []
    for num in range(num_mat):
        mat = []
        for i in range(row):
            mat.append(list(map(int, input().split())))
        mat_tot.append(mat)

    mat_sum = []
    for i in range(row):
        for j in range(col):
            mat_sum.append(mat_tot[0][i][j] + mat_tot[1][i][j])
    for i in range(row):
        print(*mat_sum[col * i:col * i + col])

def _2739():
    number = int(input())
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")

def _2743():
    print(len(input()))

def _2745():
    num_b, num_type = input().split()
    num_type = int(num_type)
    num_10 = 0
    for i in range(len(num_b), 0, -1):
        if not num_b[i - 1].isdigit():
            multi = (ord(num_b[i - 1]) - ord('A') + 10)
        else:
            multi = int(num_b[i - 1])
        num_10 += multi * num_type ** abs(len(num_b) - i)
    print(num_10)

def _2750():
    num_elements = int(input())
    elements = [int(input()) for _ in range(num_elements)]
    elements.sort()
    print(*elements, sep="\n")

def _2751():
    from collections import deque
    import sys

    def merge_sort(arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        left = deque(merge_sort(arr[:mid]))
        right = deque(merge_sort(arr[mid:]))

        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.popleft())
            else:
                merged.append(right.popleft())
        merged.extend(left)
        merged.extend(right)
        return merged

    num = int(input())
    num_list = [int(sys.stdin.readline()) for _ in range(num)]
    print(*merge_sort(num_list), sep='\n')

def _2753():
    year = int(input())
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("1")
        else:
            print("0")
    else:
        print("0")

def _2798():
    num_card, target_num = map(int, input().split())
    card_list = list(map(int, input().split()))
    num_sum = 0
    for i in range(num_card):
        for j in range(i + 1, num_card):
            for k in range(j + 1, num_card):
                sum_card = card_list[i] + card_list[j] + card_list[k]
                if num_sum <= sum_card <= target_num:
                    num_sum = sum_card
    print(num_sum)
    
if __name__ == '__main__':
    _2798()