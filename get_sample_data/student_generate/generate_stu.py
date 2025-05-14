from faker import Faker
import random
from datetime import date, timedelta
import csv

fake = Faker("zh_CN")

def generate_and_save(n=5000, filename="students.csv"):
    # 1）把频繁访问的变量／函数绑定到局部
    _rand_choice   = random.choice
    _rand_randint  = random.randint
    _rand_uniform  = random.uniform
    _name_male     = fake.name_male
    _name_female   = fake.name_female
    _date_between  = fake.date_between_dates
    _start_date    = date(2000, 1, 1)
    _end_date      = date(2006, 12, 31)

    # 2）预生成宿舍列表并打乱
    rooms = [f"{p}{b}舍{r}" 
             for p in ("东","西")
             for b in range(1,21)
             for r in [*range(101,121),
                       *range(201,221),
                       *range(301,321),
                       *range(401,421),
                       *range(501,521),
                       *range(601,621),
                       *range(701,721),
                       *range(801,821)]
             for _ in range(4)]
    random.shuffle(rooms)

    headers = ["S#","SNAME","SEX","BDATE","HEIGHT","DORM"]
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for i in range(n):
            sex = _rand_choice(["男","女"])
            sid = str(_rand_randint(10_000_000, 99_999_999))
            name = _name_male() if sex=="男" else _name_female()
            # 生成随机出生日期
            delta_days = _rand_randint(0, (_end_date - _start_date).days)
            bdate = (_start_date + 
                     timedelta(days=delta_days)
                    ).strftime("%Y-%m-%d")
            height = round(_rand_uniform(150,190), 1)
            dorm   = rooms[i]  # 已预打乱、可直接取

            writer.writerow({
                "SID": sid,
                "SNAME": name,
                "SEX": sex,
                "BDATE": bdate,
                "HEIGHT": height,
                "DORM": dorm
            })

    print(f"已写入 {n} 条记录到 {filename}")

if __name__ == "__main__":
    generate_and_save()
