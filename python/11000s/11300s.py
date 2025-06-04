def _11382():
    a, b, c = map(int, input().split())
    print(a + b + c)

def _11399():
    num_input = int(input())
    person_list = list(map(int, input().split()))
    list_sorted = sorted(person_list)
    time_need = 0
    total_time = 0
    for i in range(num_input):
        time_need = list_sorted[i] + time_need
        total_time += time_need
    print(total_time)

if __name__ == '__main__':
    _11382()