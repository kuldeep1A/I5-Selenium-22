from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
By = by.By()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
chrome_drive_path = "C:\development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(options=option, executable_path=chrome_drive_path)
driver.get(url="https://profile.w3schools.com/") # Choice any think what you want to go 

email = driver.find_element(By.NAME, "email")
email.send_keys("your email id")
password = driver.find_element(By.NAME, "currentfrom selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
By = by.By()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
chrome_drive_path = "C:\development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(options=option, executable_path=chrome_drive_path)
driver.get(url="https://profile.w3schools.com/") # Choice any think what you want to go 

email = driver.find_element(By.NAME, "email")
email.send_keys("your email id")
password = driver.find_element(By.NAME, "current-password")
password.send_keys("Your password")

submit = driver.find_element(By.CSS_SELECTOR, "button ")
submit.click()


-password")
password.send_keys("Your password")

submit = driver.find_element(By.CSS_SELECTOR, "button ")
submit.click()

