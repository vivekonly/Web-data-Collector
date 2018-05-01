from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from Ipl_Data import func_opration

driver = webdriver.Chrome()
list = ["team", "date", "player", "dismissal", "runs", "balls", "strikeRate", "fours", "sixes"]
func_opration.batmat_data(list)
del list
driver.get("https://www.iplt20.com/results")
WebDriverWait(driver,10).until(
    EC.visibility_of_all_elements_located((By.XPATH,"//*[@id='main-content']/div/div/section/div[2]/div/div[1]/div[2]/a[1]"))
)
# print(driver.find_element_by_class_name("js-list"))
result_buttons = driver.find_element_by_xpath('//*[@id="main-content"]/div/div/section')
with open("page.html","w") as fl:
    fl.write(str(result_buttons.get_attribute("innerHTML")))

tab = result_buttons.find_elements_by_class_name("js-match")
result_buttons = []
for t in tab:
    link = t.find_element_by_tag_name("a").get_attribute("href")
    result_buttons.append(link)
for rs in result_buttons:
    link = rs
    print(link)
    if bool(re.search("tab=scorecard", link))==False:
        continue
    print("link: "+ link)
    driver.get(link)

#   wait for connenct to load
    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//*[@id='scorecardContent']/div[1]/div[1]/div[2]/table"))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='scorecardContent']/div[1]/div[1]/div[1]/div"))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='scorecardContent']/div[1]/div[3]/div[1]/table"))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/section[2]/header/h1/span"))
    )
#     access team scorecard's
    team_card = driver.find_elements_by_class_name("teamScorecard")
    for team in team_card:
        print(team.find_element_by_class_name("teamHeader").text)
        team_name = team.find_element_by_class_name("teamHeader").text
#         accesing batman detail
        match_date = team.find_element_by_xpath("/html/body/div[2]/div[1]/section[2]/header/h1/span").text
        batman = team.find_element_by_class_name("batsmen")
        batman_rows = batman.find_elements_by_tag_name("tr")
        for row in batman_rows:
            list = []
            ths = row.find_elements_by_tag_name("th")
            for th in ths:
                list.append(th.text)
            tds = row.find_elements_by_tag_name("td")
            for td in tds:
                print(" data: "+td.text)
                list.append(td.text)
            func_opration.batmat_data(list)


        bowler = team.find_element_by_class_name("bowlers")
        bowler_row = bowler.find_elements_by_tag_name("tr")
        for row in bowler_row:
            list = []
            ths = row.find_elements_by_tag_name("th")
            for th in ths:
                list.append(th.text)
            tds = row.find_elements_by_tag_name("td")
            for td in tds:
                list.append(td.text)

            func_opration.bowler_data(list)

    print("loop end ")






