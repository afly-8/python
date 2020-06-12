
from selenium import webdriver
from time import sleep
import random
import datetime
import smtplib
from email.mime.text import MIMEText


# 收件人列表
mail_namelist = ["921335613@qq.com"]
# 发送方信息
mail_user = "*****@qq.com"
# 口令,注意这里是腾讯的授权码，可不是什么 QQ密码或者独立密码！
# http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
mail_pass = "*****"
def send_qq_email(title, conen):
    try:
        msg = MIMEText(str(conen))
        # 设置标题
        msg["Subject"] = title
        # 发件邮箱
        msg["From"] = mail_user
        # 收件邮箱
        msg["To"] = ";".join(mail_namelist)
        # 设置服务器、端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录邮箱
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(mail_user, mail_namelist, msg.as_string())
        s.quit()
        print("邮件发送成功!")
        return True
    except smtplib.SMTPException as err:
        print("邮件发送失败！"+str(err))
        return False


def auto_dk():
    driver = webdriver.Chrome()
    driver.get("https://cas.gfxy.com/lyuapServer/login")
    input_first = driver.find_element_by_id('username')
    input_two = driver.find_element_by_id('password')
    input_first.send_keys('35318418')
    input_two.send_keys('248913')

    driver.find_element_by_name('login').click()
    sleep(5)
    driver.find_element_by_xpath('.//div[@class="el-scrollbar__view"]/li[4]/a').click()
    sleep(8)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(driver.current_url)
    print(driver.current_url)
    wendu = driver.find_element_by_id('DQTW')
    wendu.clear()
    sleep(5)
    wendu_list = ['36.5', '36.3', '36.4', '36.6']
    tem = random.choices(wendu_list)
    wendu.send_keys(tem)
    sleep(5)
    banli = driver.find_element_by_xpath('.//a[@class="submitbtn"]')
    banli.click()
    sleep(0.5)
    send_qq_email("打卡成功咯！", '肖乐已打卡温度为：%s，请打开手机app查看'%tem)
    # 关闭浏览器
    driver.quit()

def main():
    while True:
        nowTime = datetime.datetime.now().strftime('%H:%M:%S')  # 现在
        # 早上打卡
        if nowTime == '00:01:00':
            auto_dk()
        # 中午打卡
        elif nowTime == '12:01:00':
            auto_dk()
        # 晚上打卡
        elif nowTime == '19:01:00':
            auto_dk()
        else:
            print('\r当前时间'+nowTime+',**休眠状态',end='')
main()
