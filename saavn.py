import pyautogui                     # for keyboard functionality
from selenium import webdriver       #for browser automation
import time   

music = input('Enter the name of song : ')


url = 'https://www.saavn.com/'

driver = webdriver.Chrome("/path/to/chromedriver")  # Enter the path to your chromedriver

driver.get(url)

music_search = driver.find_element_by_id('search')
music_search.send_keys(music)
time.sleep(2)


pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(1)

song = driver.find_element_by_link_text(f'{music}')
song.click()
time.sleep(1)

driver.find_element_by_class_name('play').click()