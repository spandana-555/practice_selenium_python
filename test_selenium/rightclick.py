from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
wait = WebDriverWait(driver, 30)
action=ActionChains(driver)
herokuapp=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='hot-spot']")))
#action=ActionChains(driver)
action.context_click(herokuapp).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)