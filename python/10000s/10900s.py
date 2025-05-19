def _10926():
    id = input()
    print(id + "??!")

def _10950():
    iter_num = int(input())
    for i in range(iter_num):
        a, b = map(int, input().split())
        print(a + b)

def _10951():
    import sys
    while True:
        try:
            a, b = map(int, sys.stdin.readline().split())
        except:
            break
        print(a + b)

def _10952():
    import sys
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == b == 0:
            break
        print(a + b)

def _10986():
    from collections import defaultdict
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    num_sum = [0] * (n + 1)
    mod_dict = defaultdict(int)
    cnt = 0
    for i in range(n):
        num_sum[i + 1] = nums[i] + num_sum[i]
    for i in range(n + 1):
        num_sum[i] = num_sum[i] % m
        mod_dict[num_sum[i]] += 1
    for key in mod_dict.keys():
        cnt += mod_dict[key] * (mod_dict[key] - 1) // 2
    print(cnt)

def _10988():
    word = input()
    is_sym = True
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            is_sym = False
    print(1 if is_sym else 0)

def _10989():
    import sys

    num = int(input())
    count_array = 10001 * [0]

    for i in range(num):
        count_array[int(sys.stdin.readline())] += 1

    for j in range(1, 10001):
        if count_array[j] != 0:
            for k in range(count_array[j]):
                print(j)

def _10998():
    a, b = map(int, input().split())
    print(a * b)