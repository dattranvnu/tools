import time

from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
wait = WebDriverWait(driver, 100)

soup = BeautifulSoup(open('links.html'), 'html.parser')
dom = etree.HTML(str(soup))

links = [link.get('href') for link in soup.find_all('a')]
links = [f"https://www.codecademy.com{link}" for link in links]

with open("my_file.txt", "w") as file:
    for item in links:
        file.write(item + "\n")

username, password, output = "CMR333221@yahoo.com", "Diamond3", ""

driver.get("https://www.codecademy.com/login")
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="user_login"]'))).send_keys(username)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="login__user_password"]'))).send_keys(password)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-18luxs6-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
time.sleep(8)
i = 0
for link in links:
    contents =''
    instructions =''
    driver.get(link)
    time.sleep(25)
    try:
        # informationals & articles
        contents = driver.find_element(By.XPATH, '//div[@class="gamut-1ag67m1-FlexBox e1tc6bzh0"]').get_attribute("innerHTML")
    except:
        pass
    try:
        # lessons & projects
        learn = driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[2]')
        try:
            instructions = driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[4]')
        except:
            pass
        contents = f'<h1>Learn</h1>\n\n\n{learn.get_attribute("innerHTML")}\n\n\n<h2>Instructions</h1>\n\n\n{instructions.get_attribute("innerHTML")}\n\n\n<h2>Solution</h2>\n\n\n'
    except:
        pass
    # # videos
    # try:
    #   learn = '## ' + driver.find_element(By.XPATH, '//div[@class="gamut-xvi723-FlexBox e1tc6bzh0"]//h1').text
    #   instructions = driver.find_element(By.XPATH, '//main//iframe/..').get_attribute('innerHTML')
    # except:
    #   pass
    # # external_resources
    # try:
    #   learn = '## ' + driver.find_element(By.XPATH, '//div[@class="gamut-1qd5muv-FlexBox-ExternalResourceContainer e1xk5veq0"]//h1').text
    #   instructions = driver.find_element(By.XPATH, '//div[@class="gamut-1qd5muv-FlexBox-ExternalResourceContainer e1xk5veq0"]//*[name(.) !="h1"]').get_attribute('innerHTML')
    # except:
    #   pass
    output = f"{output}\n\n\n\n\n{contents}"
    print(i, link)
    i += 1

f=open("README.txt","w")
f.write(output)
f.close()