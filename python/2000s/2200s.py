def _2231():
    num = int(input())
    has_num = False
    for i in range(1, num):
        num_to_str = list(str(i).split())
        sum_each = 0
        for j in range(len(num_to_str[0])):
            sum_each += int(num_to_str[0][j])
        if sum_each + i == num:
            print(i)
            has_num = True
            break
    if not has_num:
        print(0)

def _2292():
    num_room = int(input())
    num_layer = 0
    if num_room != 1:
        while True:
            if num_room - 6 * num_layer - 1 > 0:
                num_room -= 6 * num_layer
                num_layer += 1
                continue
            else:
                break
    print(num_layer + 1)

if __name__ == '__main__':
    _2231()