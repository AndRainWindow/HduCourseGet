from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os

login_url = "https://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html?time=1723872035447"
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") # 开启无界面模式
wd = webdriver.Edge(options=options)
with open('Config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

def Login(wd):
    wd.get(login_url)
    #ID = input("请输入你的学号：")
    ID = config['login']['ID']
    element = wd.find_element(By.ID, 'yhm')
    element.send_keys(ID)#输入学号
    #password = input("请输入你的密码：")
    #password = pyautogui.password('请输入你的密码: ')
    password = config['login']['password']
    element = wd.find_element(By.ID, 'mm')
    element.send_keys(password)#输入密码
    element.send_keys(Keys.ENTER)
    return wd

#Login(wd)