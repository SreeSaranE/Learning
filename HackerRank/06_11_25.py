if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_marks)
    sum: int = 0
    for i, j  in student_marks.items():
        if i == query_name:
            for k in j:
                sum = sum+k
    print(f"{sum/3:.2f}")