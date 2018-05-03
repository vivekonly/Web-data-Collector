from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import re
import csv

driver = webdriver.Chrome()

def get_match_link_lists(link):
    driver.get(link)

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,'//*[@id="main-content"]/div/div/section/div[2]/div/div[8]/div[2]'))
    )

    block = driver.find_element_by_class_name("js-list")
    if bool(block):
        print("block found searching for link")
        result_links = block.find_elements_by_class_name("result__button--mc")
        list = []
        for link in result_links:
            list.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
    return list

def batmat_data(list):
    with open("batmans.csv", "a") as bat:
        writer = csv.writer(bat, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list)
        bat.close()


def bowler_data(datas):
    with open("bowlers.csv", "a") as bat:
        writer = csv.writer(bat, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(datas)
        bat.close()

def get_scoreboards(link):
    driver.get(link)

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="scorecardContent"]/div[2]'))
    )

    scoreboards = driver.find_elements_by_class_name("teamScorecard")
    if bool(scoreboards):
        print("found scoreboard's collecting data")
        for scoreboard in scoreboards:
            teamHeader = scoreboard.find_element_by_class_name("teamHeader").text
            batsmen = scoreboard.find_element_by_class_name("batsmen")
            bowlers = scoreboard.find_element_by_class_name("bowlers")
            m_date = scoreboard.find_element_by_xpath('/html/body/div[2]/div[1]/section[2]/header/h1/span').text

            bat_row = batsmen.find_elements_by_tag_name("tr")
            for row in bat_row:
                tds = row.find_elements_by_tag_name("td")
                status = 0
                list = []
                list.append(teamHeader)
                list.append(m_date)
                list.append("B")
                for td in tds:
                    if bool(re.search("EXTRAS", td.text, re.I)):
                        print("table data complited")
                        status = 1
                        break
                    list.append(td.text)
                if status == 1:
                    break
                batmat_data(list)

            bow_row = bowlers.find_elements_by_tag_name("tr")
            for row in bow_row:
                tds = row.find_elements_by_tag_name("td")
                status = 0
                list = []
                list.append(teamHeader)
                list.append(m_date)
                list.append("W")
                for td in tds:
                    if bool(re.search("EXTRAS", td.text)):
                        print("table data complited")
                        status = 1
                        break
                    if bool(td.text):
                        list.append(td.text)
                    else:
                        list.append(" ")
                if status == 1:
                    break
                bowler_data(list)

