from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

import time;

from datetime import date, datetime;


today = datetime.now().isoformat();

options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options);

url = "http://sandbox.www.pylun.com";
driver.get(url);

driver.find_element_by_css_selector("input[placeholder=ID]").send_keys("pylun");
driver.find_element_by_css_selector("input[placeholder=Password]").send_keys("password");
driver.find_element_by_css_selector("button[type=submit]").click();
time.sleep(1);

url = "http://sandbox.www.pylun.com/config/market";
driver.get(url);
driver.find_element_by_xpath("//button[contains(text(), '등록')]").click();
time.sleep(1);
driver.find_element_by_css_selector("input[placeholder='마켓 이름을 입력해주세요.']").send_keys(today);
driver.find_element_by_xpath("//button[contains(text(), '저장')]").click();