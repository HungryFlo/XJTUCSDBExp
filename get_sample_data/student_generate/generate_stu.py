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

    # 2）分别生成女生宿舍和男生宿舍
    # 女生宿舍：东1、东2、东3、东4、西1、西2、西3、西4
    female_rooms = []
    for p in ("东", "西"):
        for b in range(1, 5):  # 1, 2, 3, 4
            for r in [*range(101,121),
                      *range(201,221),
                      *range(301,321),
                      *range(401,421),
                      *range(501,521),
                      *range(601,621),
                      *range(701,721),
                      *range(801,821)]:
                for _ in range(4):  # 每个房间4个床位
                    female_rooms.append(f"{p}{b}舍{r}")
    
    # 男生宿舍：剩下的所有宿舍
    male_rooms = []
    for p in ("东", "西"):
        for b in range(5, 21):  # 5-20
            for r in [*range(101,121),
                      *range(201,221),
                      *range(301,321),
                      *range(401,421),
                      *range(501,521),
                      *range(601,621),
                      *range(701,721),
                      *range(801,821)]:
                for _ in range(4):  # 每个房间4个床位
                    male_rooms.append(f"{p}{b}舍{r}")
    
    # 打乱宿舍列表
    random.shuffle(female_rooms)
    random.shuffle(male_rooms)

    max_female_count = len(female_rooms)
    max_male_count = len(male_rooms)

    print(f"女生宿舍床位数: {max_female_count}")
    print(f"男生宿舍床位数: {max_male_count}")
    print(f"总床位数: {max_female_count + max_male_count}")

    # 3）创建学号集合来确保唯一性
    used_sids = set()
    
    def generate_unique_sid():
        """生成唯一的学号"""
        while True:
            sid = str(_rand_randint(10_000_000, 99_999_999))
            if sid not in used_sids:
                used_sids.add(sid)
                return sid
    
    headers = ["S#","SNAME","SEX","BDATE","HEIGHT","DORM"]
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        female_count = 0
        male_count = 0
        female_room_index = 0
        male_room_index = 0
        
        for i in range(n):
            # 随机生成性别，但要考虑床位限制
            available_sexes = []
            if female_count < max_female_count:
                available_sexes.append("女")
            if male_count < max_male_count:
                available_sexes.append("男")
            
            # 如果没有可用床位了，跳出循环
            if not available_sexes:
                print(f"床位已满！实际生成 {i} 人，原计划 {n} 人")
                break
            
            # 从可用性别中随机选择
            sex = _rand_choice(available_sexes)
            
            # 生成唯一学号
            sid = generate_unique_sid()
            name = _name_male() if sex=="男" else _name_female()
            
            # 生成随机出生日期
            delta_days = _rand_randint(0, (_end_date - _start_date).days)
            bdate = (_start_date + 
                     timedelta(days=delta_days)
                    ).strftime("%Y-%m-%d")
            height = round(_rand_uniform(150,190), 1)
            
            # 根据性别分配宿舍
            if sex == "女":
                dorm = female_rooms[female_room_index]
                female_room_index += 1
                female_count += 1
            else:  # 男生
                dorm = male_rooms[male_room_index]
                male_room_index += 1
                male_count += 1

            writer.writerow({
                "SID": sid,
                "SNAME": name,
                "SEX": sex,
                "BDATE": bdate,
                "HEIGHT": height,
                "DORM": dorm
            })

    print(f"已写入 {female_count + male_count} 条记录到 {filename}")
    print(f"女生人数: {female_count}")
    print(f"男生人数: {male_count}")
    print(f"女生比例: {female_count/(female_count + male_count)*100:.1f}%")
    print(f"生成了 {len(used_sids)} 个唯一学号")


    print(f"已写入 {n} 条记录到 {filename}")

if __name__ == "__main__":
    generate_and_save()
