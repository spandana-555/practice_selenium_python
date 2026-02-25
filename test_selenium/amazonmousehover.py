from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 30)
amazon=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='nav-tools']//a[contains(@aria-label,'Choose a language')]")))
action=ActionChains(driver)
action.move_to_element(amazon).perform()
time.sleep(5)
