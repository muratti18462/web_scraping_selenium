from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "Downloads\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)

def selenium_to_html(input):
    temp=input.get_attribute('innerHTML')
    return temp

def load_page(pageNumber):
    browser.get("https://www.bosch-home.com.tr/urun-listesi/buzdolaplari-derin-dondurucular/?pageNumber="+str(pageNumber))

products=[]
pageNumber=1

while True:
    load_page(pageNumber)

    if len(browser.find_elements_by_xpath("//span[@class='fragment normal std-header-2']"))==0:
        break
    
    header2=browser.find_elements_by_xpath("//span[@class='fragment normal std-header-2']")
    header6=browser.find_elements_by_xpath("//span[@class='fragment normal std-header-6']")
    number=browser.find_elements_by_xpath("//span[@class='text number']") # 0-1/2-3/4-5/...
    items=browser.find_elements_by_xpath("//div[@class='item']")

    serie_prdct=0
    size_prdct=0
    info_prdct=0
    
    for prdct in range(len(header2)):
        products.append([])

        products[-1].append(selenium_to_html(header2[prdct]))
        products[-1].append(selenium_to_html(header6[prdct]))
        products[-1].append(selenium_to_html(number[2*prdct]))
    
    pageNumber+=1
    time.sleep(1)
    
browser.quit()

print("\nNumber of total product: "+str(len(products))+"\n")

for i in range(len(products)):
    print(products[i])

input("\nPress enter to exit...")
