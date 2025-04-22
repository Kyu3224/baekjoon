def _5597():
    list_student = [0] * 30
    for i in range(28):
        num = int(input())
        list_student[num - 1] = 1
    not_submitted = []
    for idx in range(30):
        if list_student[idx] != 1:
            not_submitted.append(idx + 1)
    for i in range(len(not_submitted)):
        print(not_submitted[i])

if __name__ == '__main__':
    _5597()