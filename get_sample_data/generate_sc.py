import csv
import random

# 1. 读入学生列表
with open('students.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    students = [row['S#'] for row in reader]

# 2. 读入所有课程编号
with open('courses_extracted.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    courses = [row['C#'] for row in reader]

# 3. 为每个学生随机选课并生成成绩
with open('student_course_selection.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['S#', 'C#', 'GRADE'])

    for sid in students:
        # 从 courses 中随机选 20 门，不足 20 则从 0000–3685 范围内补随机
        picked = random.sample(courses, min(20, len(courses)))
        if len(picked) < 20:
            all_ids = [f"{i:04d}" for i in range(3686)]
            extras = set(all_ids) - set(picked)
            picked += random.sample(extras, 20 - len(picked))

        for cid in picked:
            grade = random.randint(30, 100)
            writer.writerow([sid, cid, grade])

print("已生成 student_course_selection.csv")
