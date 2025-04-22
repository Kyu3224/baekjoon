def _11718():
    while True:
        try:
            word = input()
            if word == '':
                break
            print(word)
        except EOFError:  # EOF 입력 시 안전하게 종료
            break

def _11720():
    num = int(input())
    nums = input()
    sums = 0
    for i in range(num):
        sums += int(nums[i])
    print(sums)

if __name__ == '__main__':
    _11720()