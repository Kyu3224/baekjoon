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

def _1463():
    num = int(input())
    memo = [0] * 1000001
    for i in range(2, num + 1):
        if i % 6 == 0:
            value = min(memo[i // 2], memo[i // 3], memo[i - 1])
        elif i % 2 == 0:
            value = min(memo[i // 2], memo[i - 1])
        elif i % 3 == 0:
            value = min(memo[i // 3], memo[i - 1])
        else:
            value = memo[i - 1]
        memo[i] = value + 1
    print(memo[num])

if __name__ == '__main__':
    _1427()