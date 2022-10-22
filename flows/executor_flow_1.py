# TODO Multithreading for IO
# TODO Multiprocessing for the actual upload

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

PROCESS_CAP = 10

import logging

CHROME_DRIVER_PATH = "C:\Development/chromedriver.exe"
EXEC_PATH = Service(CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(service=EXEC_PATH)
LOG = logging.basicConfig(level=logging.DEBUG)


def dropdown_selection(box_select_id, choose_option):
    """ID of the box, ID of the selection"""
    dropdown = DRIVER.find_element(By.ID, box_select_id)
    time.sleep(2)
    selected_dropdown = Select(dropdown)
    selected_dropdown.select_by_value(choose_option)


def auto_suggestion_dropdown(xpath, option):
    """XPath of the box, option"""
    DRIVER.find_element(By.XPATH, xpath).click()
    DRIVER.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(option)
    DRIVER.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)


def attach_files(attached_file_id, path_of_file, upload_file):
    """In double quotes:

    Right click on attach file button and copy the ID, Path of file,

        Right click and copy ID of the upload button"""
    DRIVER.find_element(By.XPATH, attached_file_id).send_keys(path_of_file)
    DRIVER.find_element(By.ID, upload_file).click()


def dummy_driver(data_dict):
    print(data_dict)

def driver_flow_1(data_dict):
    DRIVER.get(data_dict['url'])

    # Step 1: Login
    LOG.debug("Login")
    time.sleep(1)
    DRIVER.find_element(By.NAME, "login").click()
    time.sleep(1)
    DRIVER.find_element(By.ID, "j_password").send_keys(data_dict['password'])

    # login button
    DRIVER.find_element(By.ID, "btn-login-submit").click()
    time.sleep(2)

    # Sometimes an authentication message appear, and you must press continue
    # Sometimes not
    auth_pass = DRIVER.find_elements(By.ID, "btn-submit")
    if not auth_pass:
        pass
    else:
        auth_submit = DRIVER.find_element(By.ID, "btn-submit")
        auth_submit.click()
    time.sleep(3)

    # Step 2: New ticket
    LOG.debug("New ticket")
    DRIVER.find_element(By.NAME, "newccticket").click()
    time.sleep(4)
    DRIVER.find_element(By.ID, "next").click()

    # ------------------------------------------------------------------------------
    # Step 3: Filling out the First Page / Στοιχεία Αιτούντος Φορέα

    LOG.debug("Filling out the First Page / Στοιχεία Αιτούντος Φορέα")
    DRIVER.find_element(By.ID, "diak").send_keys(data_dict['distinctive_title'])
    # TODO can anything from the line below be dynamic?
    auto_suggestion_dropdown('''//*[@id="select2-doy-container"]/span''', "Α' ΗΡΑΚΛΕΙΟΥ")
    dropdown_selection("miagro", "0")
    dropdown_selection("eipr", "02")
    dropdown_selection("idio", "0201")
    time.sleep(2)
    DRIVER.find_element(By.ID, "edra").send_keys(data_dict['residence_headquarters'])
    DRIVER.find_element(By.ID, "taxmail").send_keys(data_dict['tax_mail'])
    DRIVER.find_element(By.ID, "thle").send_keys(data_dict['phone_number)'])
    DRIVER.find_element(By.ID, "email").send_keys(data_dict['email'])
    DRIVER.find_element(By.ID, "next").click()

    # -----------------------------------------------------------------------------------------------
    # Step 4: Filling out Second Page / Στοιχεία Νόμιμου Εκπροσώπου
    LOG.debug("Filling out Second Page / Στοιχεία Νόμιμου Εκπροσώπου")

    DRIVER.find_element(By.ID, "epon_noek1").send_keys(data_dict['legal_representative'])
    DRIVER.find_element(By.ID, "afm_noek1").send_keys(data_dict['VAT_number'])

    # TODO can anything from the line below be dynamic?
    auto_suggestion_dropdown('''//*[@id="select2-doy_noek1-container"]''', "Α' ΗΡΑΚΛΕΙΟΥ")

    DRIVER.find_element(By.ID, "edra_noek1").send_keys(data_dict['legal_headquarters'])
    DRIVER.find_element(By.ID, "taxmail_noek1").send_keys(data_dict['legal_taxmail'])
    DRIVER.find_element(By.ID, "thle_noek1").send_keys(data_dict['legal_phone_number'])
    DRIVER.find_element(By.ID, "email_noek1").send_keys(data_dict['legal_email'])
    time.sleep(2)
    DRIVER.find_element(By.ID, "next").click()

    # Step 5:  Filling out Third Page / Στοιχεία Υπεύθυνου Μηχανικού
    LOG.debug("Filling out Third Page / Στοιχεία Υπεύθυνου Μηχανικού")

    DRIVER.find_element(By.ID, "epon_mech1").send_keys(data_dict['engineer_name'])
    DRIVER.find_element(By.ID, "eime1").send_keys(data_dict['engineer_specialty'])
    DRIVER.find_element(By.ID, "afm_mech1").send_keys(data_dict['engineer_VAT'])

    # TODO can anything from the line below be dynamic?
    auto_suggestion_dropdown('''//*[@id="select2-doy_mech1-container"]''', "Α' ΗΡΑΚΛΕΙΟΥ")

    DRIVER.find_element(By.ID, "edra_mech1").send_keys(data_dict['engineer_residence'])
    DRIVER.find_element(By.ID, "taxmail_mech1").send_keys(data_dict['engineer_taxmail'])
    DRIVER.find_element(By.ID, "thle_mech1").send_keys(data_dict['engineer_phone_number'])
    DRIVER.find_element(By.ID, "email_mech1").send_keys(data_dict['engineer_email'])
    DRIVER.find_element(By.ID, "next").click()

    # Step 6: Filling out Fourth Page / Στοιχεία σταθμού
    # TODO are all the same for all clients? if not, check what data we need to pass
    LOG.debug("Filling out Fourth Page / Στοιχεία σταθμού")

    time.sleep(2)
    dropdown_selection("eipa", "01")
    dropdown_selection("adst", "02")
    dropdown_selection("peadst", "02")
    dropdown_selection("eiprs", "01")
    dropdown_selection("texn", "ΦΒ")
    DRIVER.find_element(By.ID, "isxy").send_keys("399.96")
    DRIVER.find_element(By.ID, "maxisxy").send_keys("399.96")
    DRIVER.find_element(By.ID, "next").click()

    # Step 7: Filling out Fifth Page / Στοιχεία θέσης εγκατάστασης Σταθμού
    LOG.debug("Filling out Fourth Page / Στοιχεία σταθμού")

    DRIVER.find_element(By.ID, "thes").send_keys(data_dict['toponym_place'])
    auto_suggestion_dropdown('''//*[@id="select2-klpe-container"]/span''', data_dict['region'])
    auto_suggestion_dropdown('''//*[@id="select2-klno-container"]/span''', data_dict['regional_unity'])
    auto_suggestion_dropdown('''//*[@id="select2-klot-container"]/span''', data_dict['municipality'])
    auto_suggestion_dropdown('''//*[@id="select2-klde-container"]/span''', data_dict['city_section'])
    DRIVER.find_element(By.ID, "taxcode").send_keys(data_dict['postal_code'])
    dropdown_selection("idka", "02")
    dropdown_selection("eipeak", "02")
    dropdown_selection("xwro", "1")
    DRIVER.find_element(By.ID, "next").click()

    # Step 8: Filling out / Δικαιολογητικά
    LOG.debug("Filling out / Δικαιολογητικά")

    for item in data_dict['attachments']:
        # Assumption, the filen_name is a number e.g., 02, 03
        file_name, file_ext = item.split('.')
        attach_files('''//*[@id="file''' + file_name + '''"]''', "/data/" + item, "apupload" + file_name)
        time.sleep(2)

    DRIVER.find_element(By.XPATH, '''//*[@id="next"]''').click()

    # Step 9: Tick boxes
    LOG.debug("Tick boxes")

    DRIVER.find_element(By.XPATH, '''//*[@id="invalidCheck60"]''').click()
    DRIVER.find_element(By.XPATH, '''//*[@id="invalidCheck61"]''').click()
    DRIVER.find_element(By.XPATH, '''//*[@id="invalidCheck62"]''').click()
    DRIVER.find_element(By.XPATH, '''//*[@id="invalidCheck63"]''').click()
    DRIVER.find_element(By.XPATH, '''//*[@id="invalidCheck99"]''').click()

    # next button:
    DRIVER.find_element(By.XPATH, '''//*[@id="next"]''').click()

    # attach_files('''//*[@id="file02"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload02")
    # time.sleep(2)
    # attach_files('''//*[@id="file04"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload04")
    # attach_files('''//*[@id="file05"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload05")
    # time.sleep(2)
    # attach_files('''//*[@id="file06"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload06")
    # time.sleep(2)
    # attach_files('''//*[@id="file07"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload07")
    # time.sleep(2)
    # attach_files('''//*[@id="file09"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload09")
    # attach_files('''//*[@id="file09a"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload09a")
    # time.sleep(2)
    # attach_files('''//*[@id="file10"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload10")
    # time.sleep(2)
    # attach_files('''//*[@id="file12"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload12")
    # time.sleep(2)
    # attach_files('''//*[@id="file13"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload13")
    # time.sleep(2)
    # attach_files('''//*[@id="file16a"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload16a")
    # time.sleep(2)
    # attach_files('''//*[@id="file17"]''', "C:/Users/Spiros/Desktop/Screenshots/unit_decimal.jpg", "apupload17")
# --

# if __name__ == "__main__":
#     # Parse file
#     #
#     number_of_files = os.listdir('.').__len__()
#     for  iteration in range(1,number_of_files):
#         pass
#
#     # both threads completely executed
#     print("Done!")
#
#     # Parse file (TODO can we do a universal file?)
#     # Create python objects
#     # Upload
