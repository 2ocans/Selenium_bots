import time
import random
from selenium import webdriver

driver = webdriver.Chrome('D:\Webdrivers\chromedriver.exe') #location of your drivers here.

videos = [
#Put your Videos here



]

sleep_time = 0

for i in range(100):
    print("botting for {} times".format(i))
    random_video = random.randint(0,8)
    driver.get(videos[random_video])
    time.sleep(sleep_time) 
    sleep_time = random.randint(10, 20)
    time.sleep(5)
    
     
driver.quit()

#This is a simple template, you will need a proxy for this bot to work, otherwise it will not work.
