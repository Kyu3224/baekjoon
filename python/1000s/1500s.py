def _1541():
    words = input()
    word_split = words.split('-')
    word_processed = [0] * len(word_split)
    for idx, word in enumerate(word_split):
        if word.isdigit():
            word_processed[idx] = int(word)
        else:
            sum_word = word.split('+')
            for _word in sum_word:
                word_processed[idx] += int(_word)
    word_sum = word_processed[0]
    for idx in range(1, len(word_processed)):
        word_sum -= word_processed[idx]
    print(word_sum)


def _1546():
    num = int(input())
    score_list = list(map(int, input().split()))
    score_list.sort()
    max_score = max(score_list)
    sum_score_before = 0
    for i in range(num):
        sum_score_before += score_list[i]
    sum_score_after = sum_score_before * 100 / (max_score * num)
    print(sum_score_after)

if __name__ == '__main__':
    _1546()