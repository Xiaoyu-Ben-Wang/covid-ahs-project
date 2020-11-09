from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

def getCSV():
    # remove past file
    if os.path.exists("info\\covid19dataexport.csv"):
        os.remove("info\\covid19dataexport.csv")


    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": str(
        Path().absolute())+"\\info\\"}
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)

    URL = 'https://www.alberta.ca/stats/covid-19-alberta-statistics.htm'
    driver.get(URL)
    time.sleep(5)
    driver.find_element(
        By.XPATH, "//*[@id=\"covid-19-in-alberta\"]/ul/li[9]/a").click()
    time.sleep(3)
    driver.find_element(
        By.XPATH, "//*[@id=\"DataTables_Table_0_wrapper\"]/div[5]/button[1]").click()
    driver.find_element(
        By.XPATH, "//*[@id=\"DataTables_Table_0_wrapper\"]/div[5]/button[1]").click()
    driver.quit()
    # delete .tmp files
    directory = os.listdir("info\\")
    for file in directory:
        if file.endswith(".tmp"):
            os.remove(os.path.join("info\\",file))

if __name__ == "__main__":
    getCSV()
