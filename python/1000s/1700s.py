def _1735():
    import math

    nums = [list(map(int, input().split())) for _ in range(2)]
    results = [nums[0][0] * nums[1][1] + nums[0][1] * nums[1][0], nums[0][1] * nums[1][1]]
    gcd = math.gcd(results[0], results[1])
    results = [results[0] // gcd, results[1] // gcd]
    print(*results)

def _1764():
    num_listen, num_see = map(int, input().split())
    listen_list = {}
    for _ in range(num_listen):
        listen_list[input()] = 'y'

    see_list = {}
    for _ in range(num_see):
        name = input()
        if name in listen_list:
            see_list[name] = 'y'
    print(len(see_list), *sorted(list(see_list.keys())), sep='\n')

if __name__ == '__main__':
    _1735()