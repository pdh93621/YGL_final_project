import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pyautogui

class StartEndppt:
    def __init__(self,exe_path,ppt_path):
        self.openppt = False
        self.motion = input()
        self.exe_path = exe_path
        self.ppt_path = ppt_path

    def startendppt(self):
        if openppt:
            pyautogui.hotkey('alt', 'f4')
            self.openppt = False
        else:
            batch_ppt = 'start' + ' "'+ self.exe_path + '" ' + self.ppt_path
            os.system(batch_ppt)
            self.openppt = True

class CustomKey:
    def __init__(self):
        self.motion = input()
        self.key = input()
    
    def gesture2command(self):
        pyautogui.press(self.key)

class AddLink:
    def __init__(self, link):
        self.motion = input()
        self.link = link
        self.open_link = False
    
    def startendlink(self):
        if self.open_link:
            self.link_driver.quit()
            self.open_link = False
        else:
            self.open_link = True
            options = Options()

            options.add_argument('--start-maximized')

            self.link_driver = webdriver.Chrome(executable_path="./chromedriver", options = options)
            self.link_driver.implicitly_wait(1)
            self.link_driver.get(self.link)
            #self.link_driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

class AddMedia:
    def __init__(self, media_exe_path, media_path):
        self.motion = input()
        self.media_path = media_path
        self.media_exe_path = media_exe_path
        self.open_media = False

    def startendmedia(self):
        if self.open_media:
            pyautogui.hotkey('alt', 'f4')
            open_media = False
        else:
            batch_media = 'start' + ' "'+ self.media_exe_path + '" ' + self.media_path
            os.system(batch_media)