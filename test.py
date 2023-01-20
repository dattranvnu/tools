from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


username = "wakamats@oregonstate.edu"
password = "Baneyboo8"
output =''

my_file = open("0-links.txt", "r")
data = my_file.read()
links = data.split(",\n")
my_file.close()

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 100)

driver.get("https://www.codecademy.com/login")
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="user_login"]'))).send_keys(username)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="login__user_password"]'))).send_keys(password)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-18luxs6-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
time.sleep(8)
i = 0
div = ''
for link in links[0:3]:
    driver.get(link)
    time.sleep(6)
    # informationals & articles
    try:
      header = '## ' + driver.find_element(By.XPATH, '//div[@class="gamut-1ag67m1-FlexBox e1tc6bzh0"]/h1').text
      nodes = driver.find_elements(By.XPATH, '//div[@class="gamut-1ag67m1-FlexBox e1tc6bzh0"]/*[name(.) !="h1"]')
      for node in nodes:
        div = div + node.get_attribute('innerHTML')
    except:
      pass
    output = output + header + '\n\n\n\n\n' + div + '\n\n\n\n\n'
    print(i, link, nodes)
    i += 1



output = "---\noutput:\n  md_document:\n    variant: markdown_github\n---\n\n" + output


f=open("README.Rmd","w")
f.write(output)
f.close()