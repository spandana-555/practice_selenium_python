from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
action=ActionChains(driver)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
doubleclick=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Double-Click Me To See Alert']")))
action.double_click(doubleclick).perform()
alert=driver.switch_to.alert
alert.accept()
time.sleep(15)
