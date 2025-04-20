import sys
import operator
from collections import defaultdict
n, m = map(int,input().split())
num_words = defaultdict(lambda: [0, 0])
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < m:
        continue
    num_words[word][0] += 1
    if num_words[word][0] == 1:
        num_words[word][1] += len(word)
list_sorted_freq = sorted(num_words.items(), key=operator.itemgetter(1), reverse= True)
