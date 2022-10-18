from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development/chromedriver.exe"
executable_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=executable_path)

driver.get("https://apps.deddie.gr/apewebportal-ws/index.html")
login = driver.find_element(By.NAME, "login")
login.click()