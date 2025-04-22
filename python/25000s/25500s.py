def _25501():
    import sys
    def recursion(s, l, r, cnt):
        cnt+=1
        if l >= r: return 1, cnt
        elif s[l] != s[r]: return 0, cnt
        else: return recursion(s, l+1, r-1, cnt)

    def isPalindrome(s):
        return recursion(s, 0, len(s)-1, 0)

    num_test = int(input())

    for i in range(num_test):
        words = sys.stdin.readline().strip()
        print(*isPalindrome(words))

if __name__ == '__main__':
    _25501()