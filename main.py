from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

username = "test"
password = "test"
distinctive_title = "test"

chrome_driver_path = "C:\Development/chromedriver.exe"
executable_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=executable_path)


driver.get("https://apps.deddie.gr/apewebportal-ws/index.html")
driver.find_element(By.NAME, "login").click()

# autofill user and password and login
driver.find_element(By.ID, "v").send_keys(username)
driver.find_element(By.ID, "j_password").send_keys(password)
# login button
driver.find_element(By.ID, "btn-login-submit").click()

# Sometimes an authentication message appear, and you must press continue
# Sometimes not
auth_pass = driver.find_elements(By.ID, "btn-submit")
if not auth_pass:
    pass
else:
    auth_submit = driver.find_element(By.ID, "btn-submit")
    auth_submit.click()

time.sleep(3)
# new ticket
driver.find_element(By.NAME, "newccticket").click()
time.sleep(7)
driver.find_element(By.ID, "next").click()

# Filling out the First Page
driver.find_element(By.ID, "diak").send_keys(distinctive_title)