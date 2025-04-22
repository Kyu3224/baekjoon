def _9506():
    while True:
        num = int(input())
        if num == -1:
            break
        num_list = []
        for i in range(1, num):
            if num % i == 0:
                num_list.append(i)
        if sum(num_list) == num:
            print(f"{num} = ", end="")
            print(*num_list, sep=" + ")
        else:
            print(f"{num} is NOT perfect.")

if __name__ == "__main__":
    _9506()