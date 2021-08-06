import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Gesture2Command:
    gestures = ['K', 'W', 'paper', 'rock', 'scissor', 'W']
    def __init__(self, gesture):
        self.gesture = gesture
    
    def openSlide():
        self.gesture 

    def forwordSlide():
        self.gesture 
    
    def backwordSlide():
        self.gesture

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
        self.gesture
