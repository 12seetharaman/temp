def avg(lst):
    return sum(lst)/len(lst)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    for student in student_marks:
        print(f'{student} : {avg(student_marks[student]):.2f}')