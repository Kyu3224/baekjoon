def _2438():
    num_stars = int(input())
    for i in range(1, num_stars + 1):
        stars = ""
        for j in range(i):
            stars += "*"
        print(stars)

def _2439():
    num_stars = int(input())
    for i in range(1, num_stars + 1):
        stars = ""
        for j in range(1, num_stars + 1):
            if j <= num_stars - i:
                stars += " "
            else:
                stars += "*"
        print(stars)

def _2444():
    num_stars = int(input())

    for i in range(2 * num_stars - 1):
        if i < num_stars:
            stars = " " * (num_stars - i - 1) + "*" * (i * 2 + 1)
        else:
            stars = " " * (i - num_stars + 1) + "*" * (4 * num_stars - 2 * i - 3)
        print(stars)

def _2447():
    def make_star(star_array, search_size, row, col):
        if search_size == 1:
            return
        size = search_size // 3
        for i in range(size):
            for j in range(size):
                star_array[row + size + i][col + size + j] = False
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                make_star(star_array, size, row + i * size, col + j * size)

    star_size = int(input())
    star_array = [[True for j in range(star_size)] for i in range(star_size)]
    make_star(star_array, star_size, 0, 0)
    for row in star_array:
        print(''.join('*' if cell else ' ' for cell in row))

def _2480():
    a, b, c = map(int, input().split())
    num_list = [a, b, c]
    num_list.sort()
    if num_list[0] == num_list[-1]:
        price = 10000 + num_list[0] * 1000
    elif num_list[0] == num_list[1] or num_list[1] == num_list[2]:
        price = 1000 + num_list[1] * 100
    else:
        price = num_list[2] * 100
    print(price)

def _2485():
    import math

    num_already = int(input())
    tree_locs = [int(input()) for _ in range(num_already)]
    dist = [(tree_locs[i] - tree_locs[i - 1]) for i in range(1, len(tree_locs))]
    gcd = math.gcd(dist[0], dist[1])
    for i in range(2, len(dist)):
        gcd = math.gcd(gcd, dist[i])
    print((tree_locs[-1] - tree_locs[0]) // gcd - len(tree_locs) + 1)

if __name__ == '__main__':
    _2485()