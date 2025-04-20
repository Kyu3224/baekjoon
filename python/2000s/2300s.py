def _2346():
    from collections import deque
    n = int(input())
    move_vals = list(map(int, input().split()))
    balloons = deque((i + 1, move_vals[i]) for i in range(n))
    result = []
    while balloons:
        idx, move = balloons.popleft()
        result.append(idx)
        if balloons:
            if move > 0:
                balloons.rotate(-(move - 1))
            else:
                balloons.rotate(-move)

    print(*result)

if __name__ == '__main__':
    _2346()