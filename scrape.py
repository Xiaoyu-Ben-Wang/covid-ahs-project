from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

def getCSVs():
    # remove past file
    if os.path.exists("info\\covid19dataexport.csv"):
        os.remove("info\\covid19dataexport.csv")


    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": str(
        Path().absolute())+"\\info\\"}
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)

    URL = 'https://www.alberta.ca/stats/covid-19-alberta-statistics.htm'
    URL2 = 'https://www.alberta.ca/maps/covid-19-status-map.htm#list-of-active-cases-by-region'
    driver.get(URL)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"covid-19-in-alberta\"]/ul/li[9]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"DataTables_Table_0_wrapper\"]/div[5]/button[1]").click()



    driver.get(URL2)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"DataTables_Table_0_wrapper\"]/div[5]/button[1]/span").click()
    driver.quit()
    # delete .tmp files
    directory = os.listdir("info\\")
    for file in directory:
        if file.endswith(".tmp"):
            os.remove(os.path.join("info\\",file))


if __name__ == "__main__":
    getCSVs()
