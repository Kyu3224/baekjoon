def _14888():
    import sys
    input = sys.stdin.readline

    def calculate_value(nums, num_ops, idx, value, value_set):
        if idx == len(nums):
            value_set.add(value)
            return
        prev_value = value
        for i in range(4):
            if num_ops[i] > 0:
                num_ops[i] -= 1
                if i == 0:
                    value = prev_value + nums[idx]
                elif i == 1:
                    value = prev_value - nums[idx]
                elif i == 2:
                    value = prev_value * nums[idx]
                elif i == 3:
                    if prev_value < 0:
                        value = - (abs(prev_value) // nums[idx])
                    else:
                        value = prev_value // nums[idx]
                calculate_value(nums, num_ops, idx + 1, value, value_set)
                value = prev_value
                num_ops[i] += 1

    num_input = int(input())
    nums = list(map(int, input().split()))
    # Order: +, -, *, //
    num_operator = list(map(int, input().split()))
    value_set = set()
    calculate_value(nums, num_operator, 1, nums[0], value_set)
    print(max(value_set), min(value_set), sep="\n")

def _14889():
    def calculate_team(peoples, person_idx, team_a, team_b, diff):
        if len(team_a) + len(team_b) == len(peoples):
            diff.add(calculate_value(peoples, team_a, team_b))
            return

        for i in range(2):
            if i == 0 and len(team_a) < len(peoples) // 2:
                team_a.add(person_idx)
                calculate_team(peoples, person_idx + 1, team_a, team_b, diff)
                team_a.remove(person_idx)
            if i == 1 and len(team_b) < len(peoples) // 2:
                team_b.add(person_idx)
                calculate_team(peoples, person_idx + 1, team_a, team_b, diff)
                team_b.remove(person_idx)

    def calculate_value(peoples, team_a, team_b):
        def team_value(team):
            team = list(team)
            total = 0
            n = len(team)
            for i in range(n):
                for j in range(i + 1, n):
                    total += peoples[team[i] - 1][team[j] - 1]
                    total += peoples[team[j] - 1][team[i] - 1]
            return total

        return abs(team_value(team_a) - team_value(team_b))

    num_people = int(input())
    people_set = [list(map(int, input().split())) for i in range(num_people)]
    # w.l.o.g person 1 always belongs to first team
    team_a_set = set()
    team_b_set = set()
    diff_set = set()
    team_a_set.add(1)
    calculate_team(people_set, 2, team_a_set, team_b_set, diff_set)
    print(min(diff_set))

if __name__ == '__main__':
    _14888()