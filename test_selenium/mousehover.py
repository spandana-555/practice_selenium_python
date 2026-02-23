from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
actions = ActionChains(driver)
driver.get("https://the-internet.herokuapp.com/hovers")
image=driver.find_element(By.XPATH,"(//img[@alt='User Avatar'])[1]")
actions.move_to_element(image).perform()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@class='figcaption']//h5)[1]")
time.sleep(5)

