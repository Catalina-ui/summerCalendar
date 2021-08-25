import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyocr
import pyocr.builders
pyocr.tesseract.TESSERACT_CMD = r''

driver_path = './chromedriver'
window = (535,570)

driver = webdriver.Chrome(driver_path)
driver.set_window_size(*window)
target_url = ''
driver.get(target_url)

driver.execute_script("window.scrollTo(124,127);")
time.sleep(10)

#スタートボタンの座標
start_x = 256
start_y = 256

#スタートボタンをクリック
actions = ActionChains(driver)
actions.move_by_offset(start_x,start_y)
actions.click()
actions.perform()

#画面遷移時間
time.sleep(3)

#難易度選択の座標移動
move_y = 60

#難易度選択
actions = ActionChains(driver)
actions.move_by_offset(0,move_y)
actions.click()
actions.perform()
time.sleep(2)

#ゲームスタート
target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

tool = pyocr.get_available_tools()[0]

#入力開始
start = time.time()
while time.time() - start < 90.0:
    fname = "sample.png"
    driver.save_screenshot(fname)

    im = Image.open(fname).crop((0,230,500,254))
    text = tool.image_to_string(im,lang = 'eng',builder = pyocr.builders.TextBuilder())
    print(text)


input("何か入力してください")
driver.close()
driver.quit()
