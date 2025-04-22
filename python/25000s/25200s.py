def _25206():
    credit_map = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
                  'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
                  'F': 0.0}
    num_course = 20
    course_info = []
    for i in range(num_course):
        course_info.append(input().split(" ")[1:])
    total_score = total_course = 0
    for j in range(num_course):
        if course_info[j][1] == 'P':
            continue
        total_score += credit_map[course_info[j][1]] * float(course_info[j][0])
        total_course += float(course_info[j][0])
    print(f"{total_score / total_course:.6f}")

if __name__ == '__main__':
    _25206()