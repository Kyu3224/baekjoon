def _16139():
    # Commented code: code for 50 pts
    import sys
    input = sys.stdin.readline

    S = input().strip()
    Q = int(input())

    prefix = [[0] * 26]
    # prefix = [[0] * (len(S) + 1) for _ in range(26)]

    for i in range(len(S)):
        prefix.append(prefix[-1][:])
        prefix[-1][ord(S[i]) - ord('a')] += 1

    for _ in range(Q):
        ch, l, r = input().split()
        idx = ord(ch) - ord('a')
        print(prefix[int(r) + 1][idx] - prefix[int(l)][idx])

    # for i in range(len(S)):
    #     for j in range(26):
    #         prefix[j][i + 1] = prefix[j][i]
    #     prefix[ord(S[i]) - ord('a')][i + 1] += 1
    #
    # for _ in range(Q):
    #     ch, l, r = input().split()
    #     idx = ord(ch) - ord('a')
    #     print(prefix[idx][int(r) + 1] - prefix[idx][int(l)])

if __name__ == '__main__':
    _16139()