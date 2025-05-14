import scrapy
import json


class CoursesSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["ehall.xjtu.edu.cn"]

    # 不使用 start_urls，而是使用 start_requests 方法
    def start_requests(self):
        url = "https://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/modules/qxkcb/qxfbkccx.do"

        # 设置请求头
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://ehall.xjtu.edu.cn',
            'Referer': 'https://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/*default/index.do?amp_sec_version_=1&gid_=ZEFkQmRralVOdmRmSHpWL3dMR3NrTkRvbTM2ZXQydVg4RGI3VDF5cllmWkVGaFgxeDNvOGwrdkNPbjBVL1BNRk43T0E1ekVjUVUzdFdKdEtUeWlub1E9PQ&EMAP_LANG=zh&THEME=cherry',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
            'X-Requested-With': 'XMLHttpRequest',
        }

        # 设置 Cookie，这里需要填入您自己的有效 Cookie
        cookies = {
            'EMAP_LANG': 'zh',
            '_WEU': 'lMAnrz9v_MtpDKhjtPicV28ar3C_9rrnSPto06PTYmJGCVCrW7e08XdZpGN7vXePdWRWQUGvw4a2Yml668fwJS*03oeEZLMoUcVxL9Ai_m7lSdce1IdYXiO781udNDb6hEgXyjIruuUHrC938dZbC6cmk80KANG45uHtAtin9WYthQlRb5T2WradV2tphb7Y',
            'THEME': 'cherry',
            'JSESSIONID': '5hrPMzstLEbD - sj6qK2YXF4xPbDg_TiETSuKM04alfmrYNjk3j4B!-656819764',
            'amp.locale': 'undefined',
            'route': 'ab22dc972e174017d573ee90262bcc96',
            'CASTGC': 'plXj2hpTFptwjb0yWXiaOcOFpxYOtGreIrx4mws9xLnpHfr3TlXLNw==',
            'MOD_AMP_AUTH': 'MOD_AMP_d83f939b-5b49-4bda-8170-b10c8ae95673',
            'asessionid': '0d72fab4-b040-48f0-9302-e6637c8cc826',
            'CASTGC': 'TGT-2613947-EkZDccBzXg1QOzsJ5AqVghrRnJkStJAxfpiQvsXqbtWqnvNaJT-gdscas01'
        }

        # 表单数据，根据您提供的信息填写
        form_data = {
            'querySetting': '[{"name":"XXXQDM","caption":"学校校区","linkOpt":"AND","builderList":"cbl_String","builder":"equal","value":"1","value_display":"兴庆校区"},[{"name":"XNXQDM","value":"2024-2025-2","linkOpt":"and","builder":"equal"},[{"name":"RWZTDM","value":"1","linkOpt":"and","builder":"equal"},{"name":"RWZTDM","linkOpt":"or","builder":"isNull"}]],{"name":"*order","value":"+KKDWDM,+KCH,+KXH","linkOpt":"AND","builder":"m_value_equal"}]',
            '*order': '+KKDWDM,+KCH,+KXH',
            'pageSize': '10',
            'pageNumber': '1'
        }

        # 发送 POST 请求
        yield scrapy.FormRequest(
            url=url,
            headers=headers,
            # cookies=cookies,
            formdata=form_data,
            meta={'pageNumber': 1, 'pageSize': 10},
            callback=self.parse
        )
    
    def parse(self, response):
        try:
            # 尝试解析 JSON 响应
            data = json.loads(response.text)
            self.logger.info("成功获取数据")
            
            # 处理数据
            if 'datas' in data and 'qxfbkccx' in data['datas']:
                courses = data['datas']['qxfbkccx']['rows']
                for course in courses:
                    # 提取课程信息
                    course_item = {
                        'course_code': course.get('KCH', ''),  # 课程号
                        'course_name': course.get('KCM', ''),  # 课程名称
                        'credit': course.get('XF', ''),  # 学分
                        'teachers': course.get('SKJS', ''),  # 授课教师
                        'department': course.get('KKDWDM_DISPLAY', ''),  # 开课单位
                        'semester': course.get('XNXQDM', ''),  # 学年学期
                        'campus': course.get('XXXQDM_DISPLAY', ''),  # 校区
                        'class_hours': course.get('XS', ''),  # 总学时
                        'theory_hours': course.get('TLXS', ''),  # 理论学时
                        'practice_hours': course.get('SJXS', ''),  # 实践学时
                        'class_capacity': course.get('KRL', ''),  # 课容量
                        'enrolled_students': course.get('XKZRS', ''),  # 选课总人数
                        'male_students': course.get('NSXKRS', ''),  # 男生选课人数
                        'female_students': course.get('NVSXKRS', ''),  # 女生选课人数
                        'course_type': course.get('XGXKLBDM_DISPLAY', ''),  # 课程类型
                        'class_time_location': course.get('YPSJDD', ''),  # 上课时间地点
                        'class_id': course.get('JXBID', ''),  # 教学班ID
                        'classroom': course.get('JASDM', '')  # 教室代码
                    }
                    yield course_item
                
                # 获取分页信息
                ext_params = data['datas']['qxfbkccx'].get('extParams', {})
                total_page = ext_params.get('totalPage', 0)
                current_page = int(response.meta.get('pageNumber', 1))
                
                self.logger.info(f"当前页: {current_page}, 总页数: {total_page}")
                
                # 爬取下一页
                if current_page < total_page:
                    next_page = current_page + 1
                    self.logger.info(f"准备爬取第 {next_page} 页")
                    
                    form_data = {
                        'querySetting': '[{"name":"XXXQDM","caption":"学校校区","linkOpt":"AND","builderList":"cbl_String","builder":"equal","value":"1","value_display":"兴庆校区"},[{"name":"XNXQDM","value":"2024-2025-2","linkOpt":"and","builder":"equal"},[{"name":"RWZTDM","value":"1","linkOpt":"and","builder":"equal"},{"name":"RWZTDM","linkOpt":"or","builder":"isNull"}]],{"name":"*order","value":"+KKDWDM,+KCH,+KXH","linkOpt":"AND","builder":"m_value_equal"}]',
                        '*order': '+KKDWDM,+KCH,+KXH',
                        'pageSize': '10',
                        'pageNumber': str(next_page)
                    }
                    
                    yield scrapy.FormRequest(
                        url=response.url,
                        headers=response.request.headers,
                        cookies=response.request.cookies,
                        formdata=form_data,
                        callback=self.parse,
                        meta={'pageNumber': next_page, 'pageSize': 10}
                    )
            else:
                self.logger.warning("返回数据格式不符合预期")
                self.logger.debug(f"返回数据: {data}")
                
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 解析失败: {e}")
            self.logger.debug(f"响应内容: {response.text[:200]}")
        except Exception as e:
            self.logger.error(f"处理数据时发生错误: {e}")