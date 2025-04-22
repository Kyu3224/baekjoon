def _14425():
    counts = list(map(int, input().split()))
    ref_set = set([input() for _ in range(counts[0])])
    ref_tar = list([input() for _ in range(counts[1])])
    print(sum(1 for word in ref_tar if word in ref_set))

if __name__ == '__main__':
    _14425()