import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pyautogui
import time

class Gesture2Command:
    gestures = ['K', 'L', 'paper', 'rock', 'scissor', 'W']
    
    def __init__(self, gesture = None):
        self.gesture = gesture
        self.current_page = -1
        self.ppt_path = os.path.join(os.getcwd(), 'TestPPT')
        #self.total_page = input()
        self.total_page = 4
        #self.exe_path = input()
        self.exe_path = "C:\Program Files (x86)\HNC\Office 2018\HOffice100\Bin\HShow.exe"
        self.ppt = os.path.join(self.ppt_path,os.listdir(self.ppt_path)[0])
        self.open_ppt = False

    def openFirstSlide(self):
        if self.open_ppt == False:
            os.system(f'start "{self.exe_path}" "{self.ppt}"')
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

    def openYouTube(self):
        options = Options()

        #전체 화면
        options.add_argument('--start-maximized')

        #pdf 위치
        get_youtube = "https://www.youtube.com/watch?v=X_jfbXA9mUM"

        self.link_driver = webdriver.Chrome(executable_path="./chromedriver", options = options)
        self.link_driver.implicitly_wait(1)
        self.link_driver.get(get_youtube)
        self.link_driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
    
    def closeYouTube(self):
        self.link_driver.quit()

    def endSlide(self):
        if self.open_ppt == True:
            self.open_ppt = False
            pyautogui.press('esc')
            pyautogui.hotkey('alt', 'f4')
            
    def activate_command(self,gesture):
        self.gesture = gesture
        if self.gesture == Gesture2Command.gestures[0]:
            self.openFirstSlide()
        elif self.gesture == Gesture2Command.gestures[1]:
            self.nextSlide()
        elif self.gesture == Gesture2Command.gestures[2]:
            self.previousSlide()
        elif self.gesture == Gesture2Command.gestures[3]:
            self.openYouTube()
        elif self.gesture == Gesture2Command.gestures[4]:
            self.closeYouTube()
        elif self.gesture == Gesture2Command.gestures[5]:
            self.endSlide()
