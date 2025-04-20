def _1427():
    num = list(str(int(input())))
    num_list = sorted([int(nums) for nums in num], reverse=True)
    reverse = ''
    for nums in num_list:
        reverse += str(nums)
    print(reverse)

def _1436():
    start_num, idx, num_title = 666, 0, int(input())
    while True:
        if str(start_num).find('666') != -1:
            idx += 1
            if idx == num_title:
                print(start_num)
                break
        start_num += 1

if __name__ == '__main__':
    _1427()