def _1110():
    num = int(input())
    cnt = 0
    num_after = num
    while True:
        if cnt and num_after == num:
            print(cnt)
            break
        if num_after < 10:
            num_after = 11 * num_after
        else:
            num_after = (num_after % 10) * 10 + (num_after // 10 + num_after % 10) % 10
        cnt += 1

def _1149():
    import sys
    input = sys.stdin.readline

    num_house = int(input())
    prev = list(map(int, input().split()))
    new = prev
    for i in range(num_house - 1):
        new = list(map(int, input().split()))
        new[0] += min(prev[1], prev[2])
        new[1] += min(prev[0], prev[2])
        new[2] += min(prev[0], prev[1])
        prev = new
    print(min(new))

def _1152():
    print(len(input().split()))

def _1157():
    word = input()
    word_count = {}
    for i in range(len(word)):
        if word[i].upper() in word_count.keys():
            word_count[word[i].upper()] += 1
        else:
            word_count[word[i].upper()] = 1
    max_keys = [k for k, v in word_count.items() if v == max(word_count.values())]
    print("?" if len(max_keys) > 1 else max_keys[0])

def _1181():
    words = [input() for _ in range(int(input()))]
    words = list(set(words))
    words_in_size = []
    word_size = 1
    while len(words_in_size) < len(words):
        word_set = []
        for word in words:
            if len(word) == word_size:
                word_set.append(word)
        words_in_size += sorted(word_set)
        word_size += 1
    print(*words_in_size, sep='\n')

def _1193():
    input_num = int(input())
    dummy = input_num
    iteration = 1
    while dummy > 0:
        dummy -= iteration
        iteration += 1
    idx = input_num - int((iteration - 1) * (iteration - 2) / 2)
    if (iteration - 1) % 2 == 0:
        print(f"{idx}/{iteration - idx}")
    else:
        print(f"{iteration - idx}/{idx}")

if __name__ == '__main__':
    _1152()