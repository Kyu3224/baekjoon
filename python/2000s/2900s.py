def _2903():
    num_step = int(input())
    points_per_side = 2
    for i in range(num_step):
        points_per_side = 2 * points_per_side - 1
    print(points_per_side ** 2)

def _2908():
    a, b = input().split()
    a_reverse = int(a[2] + a[1] + a[0])
    b_reverse = int(b[2] + b[1] + b[0])
    if a_reverse >= b_reverse:
        print(a_reverse)
    else:
        print(b_reverse)

def _2941():
    croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    word = input()
    num_word = 0
    while word != "":
        word_deleted = None
        for chars in croatia_list:
            if word.startswith(chars):
                num_word += 1
                word_deleted = chars
                word = word.removeprefix(chars)
                break
        if not word_deleted:
            if word != "":
                num_word += 1
            word = word.removeprefix(word[0])

    print(num_word)

if __name__ == '__main__':
    _2903()