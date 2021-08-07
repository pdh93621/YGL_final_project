import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import cv2

class Gesture2Command:
    gestures = ['K', 'W', 'paper', 'rock', 'scissor', 'W']
    
    def __init__(self, gesture):
        self.gesture = gesture
        self.current_page = -1
        self.ppt_path = 'C:/Users/User/Service/TestPPT' 
        self.total_page = self.choosePPT()
        self.all_ppt = [cv2.imread(ppt_path + '/' + i) for i in self.ppt_list]

    def choosePPT():
        self.ppt_list = os.listdir(self.ppt_path)
        return len(self.ppt_list)

    def openFirstSlide():
        self.current_page = 0

    def nextSlide():
        if self.current_page < len(self.total_page) - 1:
            self.current_page += 1

    def previousSlide():
        if self.current_page > 1:
            self.current_page -= 1

    def openYouTube():
        options = Options()

        #전체 화면
        options.add_argument('--start-maximized')

        #pdf 위치
        get_youtube = "https://www.youtube.com/watch?v=X_jfbXA9mUM"

        driver = webdriver.Chrome(executable_path="./chromedriver", options = options)
        driver.implicitly_wait(1)
        driver.get(get_youtube)
        driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
    
    def closeYouTube():
        driver.quit()

    def endSlide():
        cv2.destroyAllWindows()
    
    def activate_command():
        if self.gesture == gestures[0]:
            self.openFirstSlide()
        elif self.gesture == gestures[1]:
            self.nextSlide()
        elif self.gesture == gestures[2]:
            self.previousSlide()

        cv2.imshow('myppt', self.all_ppt[self.current_page])
        
        # if self.gesture == gestures[3]:
        #     self.openYouTube()
        # elif self.gesture == gestures[4]:
        #     self.closeYouTube()
