from time import sleep
from os import getenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv("variables.env")



options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("detach",True)
options.binary_location = "/usr/bin/google-chrome-stable"
driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"),options=options)

def tweet(speed):
    speeds = speed()
    def post():
        driver.get("https://www.x.com")
        try:
            driver.find_element(By.XPATH,
                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[2]/div[4]/a/div').click()
        except:
            driver.find_element(By.XPATH,
                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a').click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))).send_keys(
            getenv("email"),Keys.RETURN)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(
                getenv("password"), Keys.RETURN)
        except:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))).send_keys(
                getenv("user_name"), Keys.RETURN)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(
                getenv("password"), Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div'))).send_keys(
            f" @nayatelpk I paid for 10Mbps DSpeed & 10Mbps USpeed\nI'm getting \nDownload Speed : {speeds[0]} \nUpload Speed : {speeds[1]}", Keys.RETURN)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span').click()
    if speeds[0] < 10 or speeds[1] < 10:
        return post
    else:
        "Speeds are full.."




@tweet
def get_speed():
    global driver
    driver.get("https://www.speedtest.net/")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]'))).click()
    sleep(50)
    download_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    download_speed = download_speed.text
    upload_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    upload_speed = upload_speed.text
    print(download_speed,upload_speed)
    return (float(download_speed),float(upload_speed))

get_speed()