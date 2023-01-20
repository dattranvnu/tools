from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


username = "wakamats@oregonstate.edu"
password = "Baneyboo8"
output =''
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 100)
my_file = open("outputs/0-links.txt", "r")
data = my_file.read()
links = data.split(",")
my_file.close()

driver.get("https://www.codecademy.com/login")
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="user_login"]'))).send_keys(username)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="login__user_password"]'))).send_keys(password)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-18luxs6-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
time.sleep(8)
driver.get("https://www.codecademy.com/paths/front-end-engineer-career-path/tracks/fecp-22-introduction-to-front-end-engineer-career-path/modules/fecp-22-getting-started/informationals/fecp-22-welcome-to-front-end-engineer-career-path")

for i in range(40):
    time.sleep(3)
    try:
      header = driver.find_element(By.XPATH, '//span[@class="gamut-yj8jvy-Text e8i0p5k0"] | //h1[@class="gamut-1ewwict-Text e8i0p5k0"] | //div[@class="gamut-haybot-Text e8i0p5k0"]').text
      try:
        div = driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[2]').get_attribute('innerHTML') + driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[4]').get_attribute('innerHTML')
      except:
        pass
      try:
        div = driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[2]').get_attribute('innerHTML') + driver.find_element(By.XPATH, '//div[@class="gamut-1s3gwqq-Box ebnwbv90"]/div[4]').get_attribute('innerHTML')
      except:
        pass
      try:
        div = driver.find_element(By.XPATH, '//div[@class="gamut-1ag67m1-FlexBox e1tc6bzh0"]').get_attribute('innerHTML')
      except:
        pass
      try:
        div = driver.find_element(By.XPATH, '//div[@class="gamut-xvi723-FlexBox e1tc6bzh0"]').get_attribute('innerHTML')
      except:
        pass
      output = output + '\n\n\n\n\n## ' + header + '\n\n\n\n\n' + div + '\n\n\n\n\n'
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="discovery-next"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-vsz6v0-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-dpt7io-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//button[@class="e1w6mdco0 gamut-mq5gnu-ResetElement-createButtonComponent e1bhhzie0"]'))).click()
    except:
        pass
    print((i,len(output)))


f=open("outputs/source.html","w")
f.write(output)
f.close()