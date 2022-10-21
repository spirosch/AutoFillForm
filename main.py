from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

username = "test"
password = "test"
# First Page resources
distinctive_title = "test"
residence_headquarters = "test"
tax_mail = "test"
phone_number = "test"
email = "test"

# Second Page resources
legal_representative = "test"
VAT_number = "test"
legal_headquarters = "test"
legal_taxmail = "test"
legal_phone_number = "test"
legal_email = "test"

# Third Page resources
engineer_name = "test"
engineer_specialty = "test"
engineer_VAT = "test"
engineer_residence = "test"
engineer_taxmail = "test"
engineer_phone_number = "test"
engineer_email = "test"

# Fifth Page resources
toponym_place = "test"
postal_code = "test"
region = "ΝΟΤΙΟΥ ΑΙΓΑΙΟΥ"
regional_unity = "ΘΗΡΑΣ"
municipality = "ΣΙΚΙΝΟΥ"
city_section = "ΣΙΚΙΝΟΥ"



def dropdown_selection(box_select_id, choose_option):
    """ID of the box, ID of the selection"""
    dropdown = driver.find_element(By.ID, box_select_id)
    time.sleep(2)
    selected_dropdown = Select(dropdown)
    selected_dropdown.select_by_value(choose_option)


# right click on box (before left click) and inspect element,
# right click on highlighted code and copy --> XPath (not full XPath)
def auto_suggestion_dropdown(xpath, option):
    """XPath of the box, option"""
    driver.find_element(By.XPATH, xpath).click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(option)
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)


def attach_files(attached_file_id, path_of_file, upload_file):
    """In double quotes:

    Right click on attach file button and copy the ID, Path of file,

        Right click and copy ID of the upload button"""
    driver.find_element(By.XPATH, attached_file_id).send_keys(path_of_file)
    driver.find_element(By.ID, upload_file).click()


chrome_driver_path = "C:\Development/chromedriver.exe"
executable_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=executable_path)

driver.get("https://apps.deddie.gr/apewebportal-ws/index.html")
driver.find_element(By.NAME, "login").click()

# autofill user and password and login
time.sleep(1)
driver.find_element(By.ID, "v").send_keys(username)
driver.find_element(By.ID, "j_password").send_keys(password)
# login button
driver.find_element(By.ID, "btn-login-submit").click()
time.sleep(2)

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

# This page sometimes takes time to load, adjust the below time.sleep
time.sleep(4)
driver.find_element(By.ID, "next").click()

# Filling out the First Page / Στοιχεία Αιτούντος Φορέα
driver.find_element(By.ID, "diak").send_keys(distinctive_title)
auto_suggestion_dropdown('''//*[@id="select2-doy-container"]/span''', "Α' ΗΡΑΚΛΕΙΟΥ")
dropdown_selection("miagro", "0")
dropdown_selection("eipr", "02")
dropdown_selection("idio", "0201")
time.sleep(2)
driver.find_element(By.ID, "edra").send_keys(residence_headquarters)
driver.find_element(By.ID, "taxmail").send_keys(tax_mail)
driver.find_element(By.ID, "thle").send_keys(phone_number)
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "next").click()

# Filling out Second Page / Στοιχεία Νόμιμου Εκπροσώπου
driver.find_element(By.ID, "epon_noek1").send_keys(legal_representative)
driver.find_element(By.ID, "afm_noek1").send_keys(VAT_number)

auto_suggestion_dropdown('''//*[@id="select2-doy_noek1-container"]''', "Α' ΗΡΑΚΛΕΙΟΥ")
# # Auto Suggestion Dropdown / Επιλέξτε ΔΟΥ
# driver.find_element(By.XPATH, '''//*[@id="select2-doy_noek1-container"]''').click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Α' ΗΡΑΚΛΕΙΟΥ")
# driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
# time.sleep(3)
# # End Auto Suggestion Dropdown

driver.find_element(By.ID, "edra_noek1").send_keys(legal_headquarters)
driver.find_element(By.ID, "taxmail_noek1").send_keys(legal_taxmail)
driver.find_element(By.ID, "thle_noek1").send_keys(legal_phone_number)
driver.find_element(By.ID, "email_noek1").send_keys(legal_email)
time.sleep(2)
driver.find_element(By.ID, "next").click()

# Filling out Third Page / Στοιχεία Υπεύθυνου Μηχανικού
driver.find_element(By.ID, "epon_mech1").send_keys(engineer_name)
driver.find_element(By.ID, "eime1").send_keys(engineer_specialty)
driver.find_element(By.ID, "afm_mech1").send_keys(engineer_VAT)
auto_suggestion_dropdown('''//*[@id="select2-doy_mech1-container"]''', "Α' ΗΡΑΚΛΕΙΟΥ")
driver.find_element(By.ID, "edra_mech1").send_keys(engineer_residence)
driver.find_element(By.ID, "taxmail_mech1").send_keys(engineer_taxmail)
driver.find_element(By.ID, "thle_mech1").send_keys(engineer_phone_number)
driver.find_element(By.ID, "email_mech1").send_keys(engineer_email)
driver.find_element(By.ID, "next").click()

# Filling out Fourth Page / Στοιχεία σταθμού
time.sleep(2)
dropdown_selection("eipa", "01")
dropdown_selection("adst", "02")
dropdown_selection("peadst", "02")
dropdown_selection("eiprs", "01")
dropdown_selection("texn", "ΦΒ")
driver.find_element(By.ID, "isxy").send_keys("399.96")
driver.find_element(By.ID, "maxisxy").send_keys("399.96")
driver.find_element(By.ID, "next").click()

# Filling out Fifth Page / Στοιχεία θέσης εγκατάστασης Σταθμού
driver.find_element(By.ID, "thes").send_keys(toponym_place)
auto_suggestion_dropdown('''//*[@id="select2-klpe-container"]/span''', region)
auto_suggestion_dropdown('''//*[@id="select2-klno-container"]/span''', regional_unity)
auto_suggestion_dropdown('''//*[@id="select2-klot-container"]/span''', municipality)
auto_suggestion_dropdown('''//*[@id="select2-klde-container"]/span''', city_section)
driver.find_element(By.ID, "taxcode").send_keys(postal_code)
dropdown_selection("idka", "02")
dropdown_selection("eipeak", "02")
dropdown_selection("xwro", "1")
driver.find_element(By.ID, "next").click()

# Sixth Page Filling out / Δικαιολογητικά
attach_files('''//*[@id="file02"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload02")
time.sleep(2)
attach_files('''//*[@id="file04"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload04")
attach_files('''//*[@id="file05"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload05")
time.sleep(2)
attach_files('''//*[@id="file06"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload06")
time.sleep(2)
attach_files('''//*[@id="file07"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload07")
time.sleep(2)
attach_files('''//*[@id="file09"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload09")
attach_files('''//*[@id="file09a"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload09a")
time.sleep(2)
attach_files('''//*[@id="file10"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload10")
time.sleep(2)
attach_files('''//*[@id="file12"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload12")
time.sleep(2)
attach_files('''//*[@id="file13"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload13")
time.sleep(2)
attach_files('''//*[@id="file16a"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload16a")
time.sleep(2)
attach_files('''//*[@id="file17"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload17")
driver.find_element(By.XPATH, '''//*[@id="next"]''').click()

# Seventh Page / Tick Boxes
driver.find_element(By.XPATH, '''//*[@id="invalidCheck60"]''').click()
driver.find_element(By.XPATH, '''//*[@id="invalidCheck61"]''').click()
driver.find_element(By.XPATH, '''//*[@id="invalidCheck62"]''').click()
driver.find_element(By.XPATH, '''//*[@id="invalidCheck63"]''').click()
driver.find_element(By.XPATH, '''//*[@id="invalidCheck99"]''').click()
# next button:
driver.find_element(By.XPATH, '''//*[@id="next"]''').click()

# Eighth Page / Submit the Form
# driver.find_element(By.XPATH, '''//*[@id="submit-all"]''').click()

