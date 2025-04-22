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