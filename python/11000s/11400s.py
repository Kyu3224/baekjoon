def _11478():
    words = list(input())
    word_made = []
    for i in range(1, len(words) + 1):
        for j in range(0, len(words) - i + 1):
            word_made.append(''.join(words[j:j + i]))
    print(len(set(word_made)))

if __name__ == '__main__':
    _11478()