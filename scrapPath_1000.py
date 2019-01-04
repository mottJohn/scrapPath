import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os, zipfile

dir_name = r"C:\Users\CHA82870\Desktop\pathConc_1-1000"

options = webdriver.ChromeOptions() 
prefs = {'download.default_directory' : dir_name,
"download.prompt_for_download": False, "download.directory_upgrade": True, "safebrowsing.enabled": True}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://path.epd.gov.hk/")


for i in range(568,1001): #5476
    grid = '//*[@id="page"]/map/area[{}]'.format(i)
    print(grid)
    grid_xPath = driver.find_element_by_xpath(grid).click()

    form_2010 = driver.find_element_by_xpath('//*[@id="2010Met"]').click()

    form_conc = driver.find_element_by_xpath('//*[@id="2020Conc"]').click()

    form_level = driver.find_element_by_xpath('//*[@id="Level1"]').click()

    download = driver.find_element_by_xpath('/html/body/div[2]/div[11]/div/button/span').click()

    #time.sleep(2)

    driver.refresh()

    extension = ".zip"

    os.chdir(dir_name) # change directory from working dir to dir with files

    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name)


#//*[@id="page"]/map/area[1509]