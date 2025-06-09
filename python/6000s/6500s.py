def _6549():
    def max_middle_area(heights, mid):
        left = mid - 1
        right = mid
        min_height = min(heights[left], heights[right])
        max_area = min_height * 2

        n = len(heights)
        while True:
            if left > 0 and (right == n - 1 or heights[left - 1] >= heights[right + 1]):
                left -= 1
                min_height = min(min_height, heights[left])
            elif right < n - 1:
                right += 1
                min_height = min(min_height, heights[right])
            else:
                break
            width = right - left + 1
            max_area = max(max_area, min_height * width)

        return max_area

    def max_area(num_input, heights):
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 2:
            return max(min(heights) * 2, max(heights))
        else:
            half = num_input // 2
            area_left = max_area(half, heights[:half])
            area_right = max_area(num_input - half, heights[half:])
            area_middle = max_middle_area(heights, half)
            return max(area_left, area_right, area_middle)

    import sys
    _input = lambda: sys.stdin.readline().strip()
    while True:
        nums = list(map(int, _input().split()))
        if nums[0] == 0:
            break
        else:
            n_input = nums.pop(0)
            print(max_area(n_input, nums))

if __name__ == '__main__':
    _6549()