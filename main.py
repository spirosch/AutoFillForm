from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

username = "test"
password = "test"

chrome_driver_path = "C:\Development/chromedriver.exe"
executable_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=executable_path)

driver.get("https://apps.deddie.gr/apewebportal-ws/index.html")
login = driver.find_element(By.NAME, "login")
login.click()
driver.find_element(By.ID, "v").send_keys(username)
driver.find_element(By.ID, "j_password").send_keys(password)
gsis_login = driver.find_element(By.ID, "btn-login-submit")
gsis_login.click()
auth_submit = driver.find_element(By.ID, "btn-submit")
auth_submit.click()