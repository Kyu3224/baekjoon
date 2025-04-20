def _1316():
    num_words = int(input())
    word_list = []
    for i in range(num_words):
        word_list.append(input())

    not_group_word = 0
    for i in range(num_words):
        word = word_list[i]
        word_used = {}
        word_prev = word[0]
        for j in range(len(list(word))):
            if word[j] not in word_used:
                word_used[word[j]] = 1
                word_prev = word[j]
            else:
                if word_prev != word[j] and word[j] in word_used:
                    not_group_word += 1
                    break
    print(num_words - not_group_word)

def _1330():
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")

if __name__ == '__main__':
    _1316()