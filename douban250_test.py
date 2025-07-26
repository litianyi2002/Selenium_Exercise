#提取电影标题，中文标题，不包含英文的
#网站地址：https://movie.douban.com/top250
# 要求：
#使用 CSS 选择器提取第一页的所有电影名。
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# wd = webdriver.Chrome()
# wd.get('https://movie.douban.com/top250')
# elements=wd.find_elements(By.CSS_SELECTOR,'#content div.hd span:nth-child(1)')
# for element in elements:
#     print('  ')
#     print(element.text)
# input()


# 提取第一页电影的导演和主演文字描述
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# wd = webdriver.Chrome()
# wd.get('https://movie.douban.com/top250')
# elements=wd.find_elements(By.CSS_SELECTOR,'#content div.bd > p:nth-child(1)')
# #这里只能会把年代信息一并打印，需要split
# # for element in elements:
# #     print('  ')
# #     print(element.text)
# # 遍历所有提取到的 <p> 元素，每个元素对应一部电影的导演/主演信息段
# for p in elements:
#     # 去掉元素文本前后的空格，获取完整的文本内容（包含导演、主演、年份、地区等）
#     full_text = p.text.strip()
#     # 如果包含换行符（即有 <br> 标签），就只取换行符前的内容（导演/主演信息）
#     if '\n' in full_text:
#         main_info = full_text.split('\n')[0]  # 以 \n 拆分，保留第 0 项
#     else:
#         main_info = full_text  # 如果没有 \n，就保留整段文字（极少数情况）
#     # 打印出最终提取的“导演 主演”信息
#     print(main_info)
# input()


#提取第一页电影的评分
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# wd = webdriver.Chrome()
# wd.get('https://movie.douban.com/top250')
# elements=wd.find_elements(By.CSS_SELECTOR,'span[class="rating_num"]')
# for element in elements:
#     print('  ')
#     print(element.text)
# input()


#提取评价人数文本
#使用xpath
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://movie.douban.com/top250")
# time.sleep(3)
#
# # 提取所有“xxx人评价”的 span
# rating_spans = driver.find_elements(By.XPATH, '//span[contains(text(), "人评价")]')
#
# # 打印每个评价人数
# for span in rating_spans:
#     print(span.text)
#
# driver.quit()


#提取引言
from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Chrome()
wd.get('https://movie.douban.com/top250')
elements=wd.find_elements(By.CSS_SELECTOR,'p.quote span')
for element in elements:
    print('  ')
    print(element.text)
input()