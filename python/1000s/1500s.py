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