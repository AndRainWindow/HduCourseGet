from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

login_url = "https://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html?time=1723872035447"

def Login(ID, password):
    #此处使用了Edge浏览器的开发者工具，如果你使用的是Chrome浏览器，可以将webdriver.Edge改为webdriver.Chrome
    wd = webdriver.Edge(service = Service())
    wd.get(login_url)
    element = wd.find_element(By.ID, 'yhm')
    element.send_keys(ID)#输入学号
    element = wd.find_element(By.ID, 'mm')
    element.send_keys(password)#输入密码
    element.send_keys(Keys.ENTER)
    return wd
def SwitchHandle(wd,title):
    for handle in wd.window_handles:
        # 先切换到该窗口
        wd.switch_to.window(handle)
        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if title in wd.title:
            # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
            break
    return wd
#输入你的学号和密码
wd = Login("","")
wd.implicitly_wait(10)
element = wd.find_element(By.XPATH, '//li[@class="dropdown"][3]/a').click()
element = wd.find_element(By.XPATH, '//*[@id="cdNav"]/ul/li[3]/ul/li[2]/a').click()
SwitchHandle(wd,"自主选课")
#输入课程号
#暂时只支持主修课程的选课
while(1):
    wd.implicitly_wait(10)
    input_element = wd.find_element(By.XPATH, '//div/input')
    #输入你想选择的课程的课程号
    input_element.send_keys("(2024-2025-1)-A150347s-03")
    input_element.send_keys(Keys.ENTER)
    getmycourse = wd.find_element(By.XPATH, '//td[@class="an"]').click()
    time.sleep(2)
    wd.refresh()
    time.sleep(1)

input()