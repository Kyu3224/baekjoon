def _10718():
    print("강한친구 대한육군\n강한친구 대한육군")

def _10773():
    import sys
    _input = sys.stdin.readline
    num = int(_input().strip())
    num_list = []
    for _ in range(num):
        num_new = int(_input().strip())
        if num_new == 0:
            num_list.pop(-1)
        else:
            num_list.append(num_new)
    print(sum(num_list))

def _10798():
    words = []
    for i in range(5):
        words.append(list(input().split()))

    max_iter = max([len(words[i][0]) for i in range(5)])
    word_vertical = ""
    for col in range(max_iter):
        for row in range(5):
            if len(words[row][0]) > col:
                word_vertical += words[row][0][col]
    print(word_vertical)

if __name__ == '__main__':
    _10773()