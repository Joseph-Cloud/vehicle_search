from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def load_manufacturers():
    dict = {}

    file = open("manufacturers.txt")
    for make in file.readlines:
        dict[make] = 0
    
    return dict


url = "https://carsandbids.com"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument("--incognito")
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
driver.implicitly_wait(10)

driver.get(url)
elements = driver.find_elements(By.CLASS_NAME, "auction-item")

for elem in elements:
    print(elem.text)