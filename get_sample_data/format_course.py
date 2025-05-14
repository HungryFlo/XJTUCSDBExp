import json
import csv

# 1. 读入原始 JSON
with open('/Users/floh/LocalDoc/XJTUCSDBExp/get_sample_data/xjtujwc/xjtujwc/course_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 打开 CSV 并写入
with open('courses_extracted.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    # 写表头
    writer.writerow(['C#', 'CNAME', 'PERIOD', 'CREDIT', 'TEACHER'])
    
    # 写每条记录，枚举生成序号
    for idx, item in enumerate(data):
        seq = f"{idx:04d}"                # 0000, 0001, 0002, ...
        writer.writerow([
            seq,
            item.get('course_name', ''),
            item.get('class_hours', ''),
            item.get('credit', ''),
            item.get('teachers', '')
        ])

print("已生成 courses_extracted.csv")
