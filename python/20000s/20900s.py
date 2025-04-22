def _20920():
    import sys
    from collections import defaultdict
    num_words, word_size = map(int, input().split())
    words = defaultdict(int)
    for _ in range(num_words):
        word = sys.stdin.readline().strip()
        if len(word) < word_size:
            continue
        words[word] += 1

    words_gathered = defaultdict(list)
    words_in_value = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for word, count in words_in_value:
        words_gathered[count].append(word)

    for idx in range(max(words_gathered.keys()), min(words_gathered.keys()) - 1, -1):
        word_list = sorted(words_gathered[idx], key=lambda x: (-len(x), x))
        for word in word_list:
            print(word)

if __name__ == '__main__':
    _20920()