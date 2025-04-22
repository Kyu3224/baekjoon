def _25304():
    price_tot = int(input())
    num_tot = int(input())
    sum_tot = 0
    for i in range(num_tot):
        num_each, price_each = map(int, input().split())
        sum_tot += num_each * price_each

    if sum_tot == price_tot:
        print("Yes")
    else:
        print("No")

def _25305():
    num_student, cut_line = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    print(score_list[cut_line - 1])

def _25314():
    num = int(input())
    to_print = ""
    for i in range(num // 4):
        if i == (num // 4) - 1:
            to_print += "long int"
        else:
            to_print += "long "
    print(to_print)

if __name__ == "__main__":
    _25314()