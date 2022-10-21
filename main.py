from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

username = "user6861242892"
password = "6228550"
# First Page resources
distinctive_title = "ΒΙΓΛΑ ΕΝΕΡΓΕΙΑΚΗ ΜΟΝΟΠΡΟΣΩΠΗ ΙΚΕ"
residence_headquarters = "ΧΑΡΑΣΟΣ ΔΗΜΟΣ ΧΕΡΣΟΝΗΣΟΥ"
tax_mail = "Λ.ΠΑΠΑΝΑΣΤΑΣΙΟΥ 23Α, ΗΡΑΚΛΕΙΟ ΚΡΗΤΗΣ, Τ.Κ 71306"
phone_number = "6952652565"
email = "boulbasisdim@gmail.com"

# Second Page resources
legal_representative = "ΜΠΟΥΛΜΠΑΣΗΣ ΔΗΜΗΤΡΙΟΣ"
VAT_number = "141374588"
legal_headquarters = "ΜΝΗΣΙΚΛΗ 41 71305 ΗΡΑΚΛΕΙΟ"
legal_taxmail = "Λ.ΠΑΠΑΝΑΣΤΑΣΙΟΥ 23Α, ΗΡΑΚΛΕΙΟ ΚΡΗΤΗΣ, Τ.Κ 71306"
legal_phone_number = "2810244114"
legal_email = "boulbasisdim@gmail.com"
# Third Page resources
engineer_name = "ΚΩΝΣΤΑΝΤΙΝΟΣ ΣΥΡΙΓΩΝΑΚΗΣ"
engineer_specialty = "ΗΛΕΚΤΡΟΛΟΓΟΣ ΜΗΧΑΝΙΚΟΣ"
engineer_VAT = "116656649"
engineer_residence = "ΗΡΑΚΛΕΙΟ ΚΡΗΤΗΣ"
engineer_taxmail = "Λ.ΠΑΠΑΝΑΣΤΑΣΙΟΥ 23Α, ΗΡΑΚΛΕΙΟ ΚΡΗΤΗΣ, Τ.Κ 71306"
engineer_phone_number = "2815103020"
engineer_email = "info@palsengineering.com"

# Fifth Page resources
toponym_place = "ΒΙΓΛΑ"
postal_code = "70014"


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
auto_suggestion_dropdown('''//*[@id="select2-klpe-container"]/span''', "ΚΡΗΤΗΣ")
auto_suggestion_dropdown('''//*[@id="select2-klno-container"]/span''', "ΗΡΑΚΛΕΙΟΥ")
auto_suggestion_dropdown('''//*[@id="select2-klot-container"]/span''', "ΧΕΡΣΟΝΗΣΟΥ")
auto_suggestion_dropdown('''//*[@id="select2-klde-container"]/span''', "ΓΟΥΒΩΝ")
driver.find_element(By.ID, "taxcode").send_keys(postal_code)
dropdown_selection("idka", "02")
dropdown_selection("eipeak", "02")
dropdown_selection("xwro", "1")
driver.find_element(By.ID, "next").click()
