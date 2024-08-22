from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time
import random
import pyautogui

#开发时插入xpath拓展用
login_url = "https://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html?time=1723872035447"
options = webdriver.EdgeOptions()
#options.add_extension(r'C:\Users\Westreet\AppData\Local\Microsoft\Edge\User Data\Default\Extensions\hgimnogjllphhhkhlmebbmlgjoejdpjl\2.0.2_0.crx')
options.add_experimental_option("detach", True)
wd = webdriver.Edge(options=options)
def Login(wd):
    wd.get(login_url)
    ID = input("请输入你的学号：")
    element = wd.find_element(By.ID, 'yhm')
    element.send_keys(ID)#输入学号
    password = input("请输入你的密码：")
    #password = pyautogui.password('请输入你的密码: ')
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
def GetCourse(wd):
    wd.implicitly_wait(10)
    input_element = wd.find_element(By.XPATH, '//div/input')
    course_id = input("请输入你想选择的课程的课程号：")
    input_element.send_keys(course_id,Keys.ENTER)
    wd.implicitly_wait(10)
    course_class = eval(input("你想选择的课程是哪一种(1是主修课程，2为通识选修课,3为体育分项,4是特殊课程)："))
    class_element = ('//*[@id="tab_kklx_01"]','//*[@id="tab_kklx_10"]','//*[@id="tab_kklx_05"]','//*[@id="tab_kklx_09"]')
    element = wd.find_element(By.XPATH, class_element[course_class-1]).click()
    while(1):
        time.sleep(3)
        coures_choose = wd.find_element(By.XPATH,'//td[@class="an"]').text
        if(coures_choose == "退选"):
            print("你已经选上该课程。")
            break
        elif(coures_choose == "选课"):
            wd.find_element(By.XPATH, '//td[@class="an"]').click()
            wd.implicitly_wait(10)
            request_info = wd.find_element(By.XPATH,'//div[@class="alert alert-modal"]/p').text
            print(request_info)
            ok = wd.find_element(By.ID, 'btn_ok').click()
            if request_info != "对不起，该教学班已无余量，不可选！":
                sleep_time = random.randint(0.1,0.5)
                time.sleep(sleep_time)
                break
    return wd


wd = Login(wd)
wd.implicitly_wait(10)
try:
    element = wd.find_element(By.XPATH, '//li[@class="dropdown"][3]/a').click()
except:
    print("登录失败，请检查你的学号和密码是否正确。")
    wd = Login(wd)
    element = wd.find_element(By.XPATH, '//li[@class="dropdown"][3]/a').click()
wd.implicitly_wait(10)
element = wd.find_element(By.XPATH, '//*[@id="cdNav"]/ul/li[3]/ul/li[2]/a').click()
SwitchHandle(wd,"自主选课")
wd = GetCourse(wd)

