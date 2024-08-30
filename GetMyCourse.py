from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time
import random
import HduLogin
import json

with open('Config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
def SwitchHandle(wd,title):
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if title in wd.title:
            break
    return wd
def GetCourse(wd):
    for course_id in config['course_id']:
        input_element = wd.find_element(By.XPATH, '//div/input')
        input_element.clear()
        input_element.send_keys(course_id,Keys.ENTER)
        wd.implicitly_wait(10)
        course_class = int(config['course_id'][course_id])
        class_element = ('//*[@id="tab_kklx_01"]','//*[@id="tab_kklx_10"]','//*[@id="tab_kklx_05"]','//*[@id="tab_kklx_09"]')
        element = wd.find_element(By.XPATH, class_element[course_class-1]).click()
        while(1):
            wd.implicitly_wait(10)
            time.sleep(2)
            coures_choose = wd.find_element(By.XPATH,'//td[@class="an"]').text
            if(coures_choose == "退选"):
                print("你已经选上该课程。")
                break
            elif(coures_choose == "选课"):
                wd.find_element(By.XPATH, '//td[@class="an"]').click()
                wd.implicitly_wait(10)
                time.sleep(1)
                request_info = wd.find_element(By.XPATH,'//div[@class="alert alert-modal"]/p').text
                print(request_info)
                ok = wd.find_element(By.ID, 'btn_ok').click()
                if request_info != "对不起，该教学班已无余量，不可选！":
                    sleep_time = random.uniform(1,2)
                    time.sleep(sleep_time)
    return wd

wd = HduLogin.wd
HduLogin.Login(wd)
wd.implicitly_wait(10)
element = wd.find_element(By.XPATH, '//li[@class="dropdown"][3]/a').click()
wd.implicitly_wait(10)
element = wd.find_element(By.XPATH, '//*[@id="cdNav"]/ul/li[3]/ul/li[2]/a').click()
SwitchHandle(wd,"自主选课")
wd = GetCourse(wd)

