# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


import scrapy

class CourseItem(scrapy.Item):
    course_code = scrapy.Field()  # 课程号 KCH
    course_name = scrapy.Field()  # 课程名称 KCM
    credit = scrapy.Field()       # 学分 XF
    teachers = scrapy.Field()     # 授课教师 SKJS
    department = scrapy.Field()   # 开课单位 KKDWDM_DISPLAY
    semester = scrapy.Field()     # 学年学期 XNXQDM
    campus = scrapy.Field()       # 校区 XXXQDM_DISPLAY
    class_hours = scrapy.Field()  # 总学时 XS
    theory_hours = scrapy.Field() # 理论学时 TLXS
    practice_hours = scrapy.Field() # 实践学时 SJXS
    class_capacity = scrapy.Field() # 课容量 KRL
    enrolled_students = scrapy.Field() # 选课总人数 XKZRS
    male_students = scrapy.Field() # 男生选课人数 NSXKRS
    female_students = scrapy.Field() # 女生选课人数 NVSXKRS
    course_type = scrapy.Field()  # 课程类型 XGXKLBDM_DISPLAY
    class_time_location = scrapy.Field() # 上课时间地点 YPSJDD
    class_id = scrapy.Field()     # 教学班ID JXBID
    classroom = scrapy.Field()    # 教室代码 JASDM
