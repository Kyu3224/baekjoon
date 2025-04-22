def _10807():
    total_num = int(input())
    array_num = input().split()
    find_num = int(input())
    cnt = 0
    for i in range(total_num):
        if int(array_num[i]) == find_num:
            cnt += 1
    print(cnt)

def _10809():
    word = input()
    alphabet_list = [-1] * 26
    place = 0
    for letter in word:
        letter_index = ord(letter) - ord('a')
        if alphabet_list[letter_index] < 0:
            alphabet_list[letter_index] = place
        place += 1
    print(*alphabet_list)

def _10810():
    num_bucket, num_iter = map(int, input().split())
    buckets = [0] * num_bucket
    for i in range(num_iter):
        start_idx, end_idx, num_ball = map(int, input().split())
        for j in range(start_idx, end_idx + 1):
            buckets[j - 1] = num_ball
    print(" ".join(map(str, buckets)))

def _10811():
    num_bucket, num_change = map(int, input().split())
    bucket_seq = [i + 1 for i in range(num_bucket)]
    for i in range(num_change):
        start_idx, end_idx = map(int, input().split())
        start_idx -= 1
        bucket_seq[start_idx:end_idx] = bucket_seq[start_idx:end_idx][::-1]
    print(*bucket_seq)

def _10813():
    num_bucket, num_iter = map(int, input().split())
    buckets = [0] * num_bucket
    for i in range(num_bucket):
        buckets[i] = i + 1
    for i in range(num_iter):
        start, end = map(int, input().split())
        temp = buckets[start - 1]
        buckets[start - 1] = buckets[end - 1]
        buckets[end - 1] = temp
    print(" ".join(map(str, buckets)))

def _10814():
    people_list = [list(input().split()) for _ in range(int(input()))]
    people_sorted = []
    age = 1
    while len(people_sorted) < len(people_list):
        peoples = []
        for person in people_list:
            if int(person[0]) == age:
                peoples.append(person)
        people_sorted.extend(peoples)
        age += 1
    for person in people_sorted:
        print(*person)

def _10815():
    num_card = int(input())
    card_list = set(map(int, input().split()))
    num_target_card = int(input())
    target_list = list(map(int, input().split()))
    has_card = [1 if target in card_list else 0 for target in target_list]
    print(*has_card)

def _10816():
    num_card = int(input())
    card_list = {}
    card_input = list(map(int, input().split()))
    for i in range(num_card):
        card = card_input[i]
        if card in card_list:
            card_list[card] += 1
        else:
            card_list[card] = 1
    num_tar = int(input())
    target_input = list(map(int, input().split()))
    sol = []
    for j in range(num_tar):
        card = target_input[j]
        if card in card_list:
            sol.append(card_list[card])
        else:
            sol.append(0)
    print(*sol)

def _10818():
    N = int(input())
    array_num = list(map(int, input().split()))
    array_num.sort()
    print(f"{array_num[0]} {array_num[N - 1]}")

def _10869():
    a, b = map(int, input().split())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)

def _10870():
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    num_input = int(input())
    print(fibonacci(num_input))

def _10871():
    N, X = map(int, input().split())
    array_num = input().split()
    to_print = ""
    for i in range(N):
        if int(array_num[i]) < X:
            to_print += array_num[i] + ' '
    print(to_print)

def _10872():
    num = 1
    for i in range(1, int(input()) + 1):
        num *= i
    print(num)

if __name__ == '__main__':
    _10872()