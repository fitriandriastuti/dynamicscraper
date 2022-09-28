# import os
# #buat mengatasi error baca folder app
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# from app import master
#
# prov = master.get_prov()
#
# # @pepo____________________________________________________________________________
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
#
# # from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import expected_conditions
#
# print(prov)
# total_prov = range(len(prov))
# record_i = 0
# record_j = 0
#
# for i in range(len(prov)):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     driver.get("http://emispendis.kemenag.go.id/pdpontrenv2/Sebaran/Pp")
#
#     actions = ActionChains(driver)
#
#     time.sleep(5)
#
#     find_thn_semester = driver.find_element(By.ID, "thn_semester")
#     select_thn_semester = Select(find_thn_semester)
#     select_thn_semester.select_by_visible_text('2021-2022 / Genap')
#
#     time.sleep(5)
#
#     find_TBLDATA_length = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
#     select_TBLDATA_length = Select(find_TBLDATA_length)
#     select_TBLDATA_length.select_by_visible_text('100')
#
#     time.sleep(5)
#
#     print(prov[i])
#     kode_prov = prov[i]['prov']
#     nama_prov = prov[i]['nama']
#     prov_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'"+nama_prov+"')]//a[@href]")
#     # action.click(prov_act).perform()
#     # ActionChains(driver).click(prov_act).perform()
#     # ActionChains(driver).move_to_element(prov_act).perform()
#     # driver.execute_script('window.scrollTo(0, 200)')
#     # driver.execute_script('arguments[0].scrollIntoView();', prov_act)
#     # action.move_to_element(prov_act).click(prov_act).perform()
#     driver.execute_script('arguments[0].scrollIntoView();', prov_act)
#     # actions.move_to_element(prov_act).click().perform()
#     actions.click(on_element=prov_act).perform()
#
#     kab = master.get_kab(kode_prov)
#
#     print('pepo')
#     print(kab)
#
#     time.sleep(5)
#
#     for j in range(len(kab)):
#         print(kab[j])
#         kode_prov_ = kab[j]['prov']
#         kode_kab = kab[j]['kab']
#         nama_kab = kab[j]['nama']
#         print(kode_prov_, kode_kab, nama_kab)
#
#         time.sleep(5)
#
#         find_TBLDATA_length_kab = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
#         select_TBLDATA_length_kab = Select(find_TBLDATA_length_kab)
#         select_TBLDATA_length_kab.select_by_visible_text('100')
#
#         kab_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'"+nama_kab+"')]//a[@href]")
#         # action.click(kab_act).perform()
#         # ActionChains(driver).click(kab_act).perform()
#         # driver.execute_script("arguments[0].scrollIntoView()", kab_act)
#         # ActionChains(driver).move_to_element(kab_act).perform()
#         # # time.sleep(3)
#         # driver.execute_script('arguments[0].scrollIntoView();', kab_act)
#         # ActionChains(driver).click(kab_act).perform()
#         # driver.execute_script('window.scrollTo(0, 200)')
#         # driver.execute_script('arguments[0].scrollIntoView();', kab_act)
#         # action.move_to_element(kab_act).click(kab_act).perform()
#         # driver.execute_script("arguments[0].scrollIntoView(**{block: 'center', inline: 'center'}**)", kab_act)
#         # actions.move_to_element(kab_act).click().perform()
#         driver.execute_script('arguments[0].scrollIntoView();', kab_act)
#         actions.click(on_element=kab_act).perform()
#
#         time.sleep(5)
#
#         kec = master.get_kec(kode_prov_, kode_kab)
#
#         print(kec)
#
#         for d_kec in kec:
#             time.sleep(5)
#
#             find_TBLDATA_length_kec = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
#             select_TBLDATA_length_kec = Select(find_TBLDATA_length_kec)
#             select_TBLDATA_length_kec.select_by_visible_text('100')
#
#             time.sleep(5)
#
#             print(d_kec['nama'])
#             kec_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'" + str(d_kec['nama']) + "')]//a[@href]")
#             # action.click(kec_act).perform()
#             # ActionChains(driver).click(kec_act).perform()
#             # driver.execute_script("arguments[0].scrollIntoView()", kec_act)
#             # time.sleep(3)
#             # ActionChains(driver).move_to_element(kec_act).perform()
#             # driver.execute_script('arguments[0].scrollIntoView();', kec_act)
#             # ActionChains(driver).click(kec_act).perform()
#             # driver.execute_script('window.scrollTo(0, 200)')
#             # driver.execute_script('arguments[0].scrollIntoView();', kec_act)
#             # action.move_to_element(kec_act).click(kec_act).perform()
#             # driver.execute_script("arguments[0].scrollIntoView(**{block: 'center', inline: 'center'}**)", kec_act)
#             # actions.move_to_element(kec_act).click().perform()
#             driver.execute_script('arguments[0].scrollIntoView();', kec_act)
#             actions.click(on_element=kec_act).perform()
#
#             time.sleep(5)
#
#             find_TBLDATA_length_lembaga = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
#             select_TBLDATA_length_lembaga = Select(find_TBLDATA_length_lembaga)
#             select_TBLDATA_length_lembaga.select_by_visible_text('100')
#
#             data_tabel = driver.find_element(By.XPATH, "//table[@id='TBLDATA']")
#             print(data_tabel.text)
#
#             #backlembaga
#             backlembaga = driver.find_element(By.XPATH, "//button[contains(@onclick,'kembali')]")
#             # action.click(backlembaga).perform()
#             # ActionChains(driver).click(backlembaga).perform()
#             # driver.execute_script("arguments[0].scrollIntoView()", backlembaga)
#             # time.sleep(3)
#             # ActionChains(driver).move_to_element(backlembaga).perform()
#             # time.sleep(3)
#             # driver.execute_script('arguments[0].scrollIntoView();', backlembaga)
#             # ActionChains(driver).click(backlembaga).perform()
#             # driver.execute_script("arguments[0].scrollIntoView(**{block: 'center', inline: 'center'}**)", backlembaga)
#             # actions.move_to_element(backlembaga).click().perform()
#             driver.execute_script('arguments[0].scrollIntoView();', backlembaga)
#             actions.click(on_element=backlembaga).perform()
#
#             time.sleep(5)
#
#         record_j = record_j + 1
#         print(record_j)
#
#     driver.quit()

import os
#buat mengatasi error baca folder app
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import master

prov = master.get_prov()

# @pepo____________________________________________________________________________


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(ChromeDriverManager().install())

actions = ActionChains(driver)

driver.maximize_window()
driver.get("http://emispendis.kemenag.go.id/pdpontrenv2/Sebaran/Pp")

find_thn_semester = driver.find_element(By.ID, "thn_semester")
select_thn_semester = Select(find_thn_semester)
select_thn_semester.select_by_visible_text('2021-2022 / Genap')

time.sleep(20)

find_TBLDATA_length = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
actions.move_to_element(find_TBLDATA_length)
# driver.execute_script("arguments[0].scrollIntoView();", find_TBLDATA_length)
select_TBLDATA_length = Select(find_TBLDATA_length)
select_TBLDATA_length.select_by_visible_text('100')

time.sleep(5)

for i in range(len(prov)):
    print(prov[i]['nama'])
    nama_prov = prov[i]['nama']
    kode_prov = prov[i]['prov']
    # kab
    prov_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'"+nama_prov+"')]//a[@href]")
    # driver.execute_script("arguments[0].scrollIntoView();", prov_act)
    actions.move_to_element(prov_act)
    actions.click(prov_act).perform()
    # prov_act.click()

    kab = master.get_kab(kode_prov)

    # print(kab)

    time.sleep(5)

    for j in range(len(kab)):
        print(kab[j]['nama'])
        nama_kab = kab[j]['nama']
        kode_kab = kab[j]['kab']
        print('nama_kab pepo: ', nama_kab)
        time.sleep(5)

        print('pilih dropdown')
        find_TBLDATA_length_kab = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
        # driver.execute_script("arguments[0].scrollIntoView();", find_TBLDATA_length_kab)
        actions.move_to_element(find_TBLDATA_length_kab)
        select_TBLDATA_length_kab = Select(find_TBLDATA_length_kab)
        select_TBLDATA_length_kab.select_by_visible_text('100')

        time.sleep(5)

        kab_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'"+nama_kab+"')]//a[@href]")
        # driver.execute_script("arguments[0].scrollIntoView();", kab_act)
        # ActionChains(driver).click(kab_act).perform()
        # kab_act.click()
        print('klik scroll ke nama kab')

        # actions.move_to_element_with_offset(kab_act, 0, 100)

        # actions.move_to_element(kab_act)

        # time.sleep(5)  # wait for scrolling
        # print('klik scroll ke nama kab bawahnya lagi')
        # driver.execute_script("window.scrollBy(0,100)", "")
        # driver.execute_script("window.scrollTo(0, 200)")  # scroll down a bit
        #
        # time.sleep(5)  # wait for scrolling

        # first move to the element
        driver.execute_script("return arguments[0].scrollIntoView(true);", kab_act)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-500)", "")

        time.sleep(5)

        # then scroll by x, y values, in this case 10 pixels up
        # actions.execute_script("window.scrollBy(0, -10);")
        # driver.execute_script("window.scrollBy(0, 200);")
        # driver.execute_script("window.scrollBy(0, 5);")

        # time.sleep(5)

        print('klik nama kab: ', nama_kab)
        # actions = ActionChains(driver)
        kab_act_ = driver.find_element(By.XPATH,"//table[@id='TBLDATA']//tbody//tr//td[contains(.,'" + nama_kab + "')]//a[@href]")
        # actions.click(kab_act_).perform()
        kab_act_.click()

        time.sleep(5)

        kec = master.get_kec(kode_prov, kode_kab)

        # print(kec)
        time.sleep(5)

        for d_kec in kec:

            find_TBLDATA_length_kec = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
            # driver.execute_script("arguments[0].scrollIntoView();", find_TBLDATA_length_kec)
            actions.move_to_element(find_TBLDATA_length_kec)
            select_TBLDATA_length_kec = Select(find_TBLDATA_length_kec)
            select_TBLDATA_length_kec.select_by_visible_text('100')

            time.sleep(5)

            print(d_kec['nama'])
            kec_act = driver.find_element(By.XPATH, "//table[@id='TBLDATA']//tbody//tr//td[contains(.,'" + str(d_kec['nama']) + "')]//a[@href]")
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            # ActionChains(driver).click(kec_act).perform()
            # kec_act.click()
            actions.move_to_element(kec_act)
            time.sleep(5)
            # actions.click(kec_act).perform()
            kec_act.click()

            time.sleep(5)

            find_TBLDATA_length_lembaga = driver.find_element(By.XPATH, "//select[@name='TBLDATA_length']")
            # driver.execute_script("arguments[0].scrollIntoView();", find_TBLDATA_length_lembaga)
            actions.move_to_element(find_TBLDATA_length_lembaga)
            select_TBLDATA_length_lembaga = Select(find_TBLDATA_length_lembaga)
            select_TBLDATA_length_lembaga.select_by_visible_text('100')

            data_tabel = driver.find_element(By.XPATH, "//table[@id='TBLDATA']")
            print(data_tabel.text)

            #backlembaga
            backlembaga = driver.find_element(By.XPATH, "//button[contains(@onclick,'kembali')]")
            # ActionChains(driver).click(backlembaga).perform()
            actions.move_to_element(backlembaga)
            time.sleep(5)
            # actions.click(backlembaga).perform()
            backlembaga.click()

            time.sleep(5)

        driver.quit()

# time.sleep(5)
#
# driver.quit()

























