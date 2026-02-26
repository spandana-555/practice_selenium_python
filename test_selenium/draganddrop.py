from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
action=ActionChains(driver)
driver.maximize_window()
driver.get("https://demoqa.com/droppable")
source=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='draggable']")))
target=wait.until(EC.visibility_of_element_located((By.XPATH," //p[text()='Drop Here']")))
time.sleep(5)
action.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)
