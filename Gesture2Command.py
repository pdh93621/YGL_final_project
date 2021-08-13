import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pyautogui
import time

class Gesture2Command:
    gestures = ['K', 'L', 'paper', 'rock', 'scissor', 'W', 'O']
    
    def __init__(self, gesture = None):
        self.gesture = gesture
        self.current_page = -1
        self.ppt_path = os.path.join(os.getcwd(), 'TestPPT')
        #self.total_page = input()
        self.total_page = 4
        #self.ppt_exe_path = input()
        self.ppt_exe_path = "C:\Program Files (x86)\HNC\Office 2018\HOffice100\Bin\HShow.exe"
        #self.media_exe_path = input()
        self.media_exe_path = "C:\Program Files\DAUM\PotPlayer"
        self.ppt = os.path.join(self.ppt_path,os.listdir(self.ppt_path)[0])
        self.open_ppt = False
        self.open_media = False
        self.media_path = os.path.join(os.getcwd(), 'TestMedia')
        self.media = os.path.join(self.media_path, os.listdir(self.media_path)[0])

    def startendSlide(self):
        if self.open_ppt:
            pyautogui.press('esc')
            pyautogui.hotkey('alt', 'f4')
            self.current_page = -1
        else:
            batch_ppt = 'start' + ' "'+ self.ppt_exe_path + '" ' + self.ppt
            os.system(batch_ppt)
            time.sleep(4)
            pyautogui.hotkey('f5')
            self.current_page = 1
            self.open_ppt = True

    def nextSlide(self):
        if self.current_page < self.total_page:
            self.current_page += 1
            pyautogui.hotkey('right')

    def previousSlide(self):
        if self.current_page > 1:
            self.current_page -= 1
            pyautogui.hotkey('left')

    def opencloseYouTube(self):
        if self.open_media:
            self.link_driver.quit()
        else:
            self.open_media = True
            options = Options()

            #전체 화면
            options.add_argument('--start-maximized')

            #pdf 위치
            get_youtube = "https://www.youtube.com/watch?v=X_jfbXA9mUM"

            self.link_driver = webdriver.Chrome(executable_path="./chromedriver", options = options)
            self.link_driver.implicitly_wait(1)
            self.link_driver.get(get_youtube)
            self.link_driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
        
    def opencloseMedia(self):
        if self.open_media:
            self.open_media = False
            pyautogui.hotkey('alt', 'f4')
            
        else:
            self.open_media = True
            batch_media = 'start' + ' "' + self.media_path + '" ' + self.media
            os.system(batch_media)
            time.sleep(1)
            pyautogui.press('enter')

    def gotopage(self, page):
        num = self.current_page - page
        if num >= 0:
            for _ in range(num):
                self.previousSlide()
            
        else:
            for _ in range(-num):
                self.nextSlide()

        self.current_page = page

    def press_key(self):
        pyautogui.press('space')
            
    def activate_command(self,gesture, num = 1):
        self.gesture = gesture
        if self.gesture == Gesture2Command.gestures[0]:
            self.startendSlide()
        elif self.gesture == Gesture2Command.gestures[1]:
            self.nextSlide()
        elif self.gesture == Gesture2Command.gestures[2]:
            self.previousSlide()
        elif self.gesture == Gesture2Command.gestures[3]:
            self.opencloseYouTube()
        elif self.gesture == Gesture2Command.gestures[4]:
            self.opencloseMedia()
        elif self.gesture == Gesture2Command.gestures[5]:
            self.gotopage(num)
        elif self.gesture == Gesture2Command.gestures[6]:
            self.press_key()
