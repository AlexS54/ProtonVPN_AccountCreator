from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
def check0_exists_by_id(id):                #Functions used to stall the program until a certain element loads
    try:
        driver0.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check0_exists_by_xpath(id):
    try:
        driver0.find_element_by_xpath(id)
    except NoSuchElementException:
        return False
    return True

def check1_exists_by_xpath(id):
    try:
        driver1.find_element_by_xpath(id)
    except NoSuchElementException:
        return False
    return True

driver0 = webdriver.Chrome()
driver0.get("https://temp-mail.org/en/")                            #Open the temp-mail tab
ok=True
while(not(check0_exists_by_id("mail")) or ok):                      #In case the page doesn't load or only partially loads a refresh is performed.                        
    driver0.refresh()
    time.sleep(5)
    adress=driver0.find_element_by_id("mail").get_property("value")
    if(adress!=""): ok=False
    else: ok=True
while(True):                                                        #Wait for the adress to show up and replace the "Loading..."    
    time.sleep(1)
    mailadress = driver0.find_element_by_id("mail").get_property("value")
    if(mailadress!="Loading" and mailadress!="Loading." and mailadress!="Loading.." and mailadress!="Loading..."): break
username=[]                                                          
for letter in mailadress:                                          #The username is the email adress without everything that comes after '@'.
    if letter=='@':
        break
    username+=letter
driver1=webdriver.Chrome()
driver1.get("https://account.protonvpn.com/signup")                #Open a new window with the ProtonVPN signup page.
time.sleep(2)
while(not(check1_exists_by_xpath("/html/body/div[1]/main/main/div/div[4]/div[1]/div[3]/button"))):      #Making sure again that the page is fully loaded.
    driver1.refresh()
    time.sleep(3)
driver1.find_element_by_xpath("/html/body/div[1]/main/main/div/div[4]/div[1]/div[3]/button").click()    
driver1.find_element_by_xpath("//*[@id='username']").send_keys(username)    #Input the details.
driver1.find_element_by_name("password").send_keys("kjkszpj0")          
driver1.find_element_by_id("passwordConfirmation").send_keys("kjkszpj0")
driver1.find_element_by_id("email").send_keys(mailadress)
driver1.find_element_by_xpath("/html/body/div[1]/main/main/div/div[2]/div/div[1]/form/div[3]/div/button").click()
time.sleep(2)
driver1.find_element_by_xpath("/html/body/div[1]/main/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div[2]/button").click()
while(not(check0_exists_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/ul/li[2]/div[2]/span/a"))): time.sleep(1)   #Wait for the email with the code to arrive...
time.sleep(1)
driver0.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/ul/li[2]/div[2]/span/a").click()
while(not(check0_exists_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/p/code"))): time.sleep(1)
code=driver0.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/p/code").text
driver1.find_element_by_id("code").send_keys(code)      #Input code.
driver1.find_element_by_xpath("/html/body/div[1]/main/main/div/div[2]/div/div[1]/div[2]/form/div/div/div[2]/button").click() #Finalize
driver0.close()