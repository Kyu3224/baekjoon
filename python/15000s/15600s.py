def _15649():
    def permute(n, m, path):
        if len(path) == m:
            print(*path)
            return

        for i in range(1, n + 1):
            if i not in path:
                permute(n, m, path + [i])

    n, m = map(int, input().split())
    permute(n, m, [])

def _15650():
    def comb(n, m, path):
        if len(path) == m:
            print(*path)
            return

        for i in range(1, n + 1):
            if i not in path:
                if not path:
                    comb(n, m, path + [i])
                else:
                    if i > path[-1]:
                        comb(n, m, path + [i])

    n, m = map(int, input().split())
    comb(n, m, [])

def _15651():
    def permute_all(n, m, path):
        if len(path) == m:
            print(*path)
            return

        for i in range(1, n + 1):
            permute_all(n, m, path + [i])

    n, m = map(int, input().split())
    permute_all(n, m, [])

def _15652():
    def permute_ascend(n, m, path):
        if len(path) == m:
            print(*path)
            return

        for i in range(1, n + 1):
            if not path:
                permute_ascend(n, m, path + [i])
            else:
                if path[-1] <= i:
                    permute_ascend(n, m, path + [i])

    n, m = map(int, input().split())
    permute_ascend(n, m, [])

if __name__ == '__main__':
    _15649()