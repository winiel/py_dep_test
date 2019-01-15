from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time;

from datetime import date, datetime;


today = datetime.now().isoformat();

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options);

url = "http://sandbox.www.pylun.com";
driver.get(url);

driver.find_element_by_css_selector("input[placeholder=ID]").send_keys("pylun");
driver.find_element_by_css_selector("input[placeholder=Password]").send_keys("password");
driver.find_element_by_css_selector("button[type=submit]").click();
time.sleep(1);
print(driver.page_source);
print("=====================")
print("=====================")
print("=====================")

url = "http://sandbox.www.pylun.com/config/market";
driver.get(url);
print(driver.page_source);
print("=====================")
print("=====================")
print("=====================")

time.sleep(2);
btn = driver.find_element_by_css_selector("button[ng-click='btnReg()']");
# btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '등록')]']")));
# btn = WebDriverWait(driver, 3).until((EC.presence_of_element_located, "button[ng-click='btnReg()']"));
btn.click();
time.sleep(1);
driver.find_element_by_css_selector("input[placeholder='마켓 이름을 입력해주세요.']").send_keys(today);
driver.find_element_by_css_selector("button[ng-click='btnSave()']").click();
print("end");