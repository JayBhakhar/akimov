from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


browser = webdriver.Chrome()
browser.get("https://www.ahdancembet.site/en/")
time.sleep(2)
link = browser.find_element_by_xpath("//a[@class='label']")
link.click()
time.sleep(2)
# webdriver.ActionChains(browser).move_by_offset(500, 500).perform()
# time.sleep(2)
# browser.find_element_by_xpath('//a[@class="breadcrumb-text"]')

element = browser.find_element_by_xpath('//a[@class="breadcrumb-text"]')
actions = ActionChains(browser)
actions.move_to_element(element).perform()


teamname = browser.find_elements_by_xpath("//div/a/span[@data-member-link='true']")
lst = []
for i in teamname:
    lst += [i.text]
fnllst = []
newlst1 = lst[::2]
newlst2 = lst[1::2]
for i in range(len(newlst1)):
    fnllst.append(newlst1[i] + " vs " + newlst2[i])
#print(fnllst)


time = browser.find_elements_by_xpath("//tr/td[@class='date']")
tme = []
for i in time:
    tme += [i.text]
#print(tme)

win1 =  browser.find_elements_by_xpath("//tr/td[@class='price height-column-with-price    first-in-main-row  coupone-width-3']")
                                                        #price height-column-with-price    first-in-main-row  coupone-width-3
                                                        #price height-column-with-price    first-in-main-row  coupone-width-3 price-highlighted
wi1 = []
for i in win1:
    wi1 += [i.text]
# print(wi1)


draw =  browser.find_elements_by_xpath("//tr/td[@class='price height-column-with-price    coupone-width-3']")
dra = []
for i in draw:
    dra += [i.text]
realdra = dra[::2]
win2 = dra[1::2]
#print(realdra)
#print(win2)


df = pd.DataFrame(  {   'Country' : fnllst,
                        'Time' : tme,
                         'Win 1' : wi1,
                         'Draw' : realdra,
                         'Win 2' : win2
                    })
df.to_csv("list6.csv")