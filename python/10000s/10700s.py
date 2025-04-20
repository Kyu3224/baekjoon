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

if __name__ == '__main__':
    _10773()