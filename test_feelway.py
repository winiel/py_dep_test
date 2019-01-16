from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options);

listWindow = driver.window_handles;
print(listWindow);
windowMain = listWindow[0];


url = "http://www.feelway.com/login.php";
driver.get(url);
id = driver.find_element_by_name("login_id");
id.send_keys("afrokingdom");
pwd = driver.find_element_by_name("login_password");
pwd.send_keys("taemin1828");
btn_login = driver.find_element_by_css_selector("input[type=image]");
btn_login.click();

Alert(driver).accept();

url = "http://www.feelway.com/sell.php";
driver.get(url);
chk = driver.find_element_by_name("checkbox1");
chk.click()
chk = driver.find_element_by_name("checkbox2");
chk.click()
chk = driver.find_element_by_name("checkbox3");
chk.click()
btn_login = driver.find_element_by_css_selector("input[type=image]");
btn_login.click();


brand = Select(driver.find_element_by_css_selector("form[name=up_form] select[name=brand_no]"));
tmp = brand.select_by_visible_text("A.Testoni");



soupDoc = BeautifulSoup(driver.page_source, 'html.parser');
divPhoto_1 = soupDoc.find("div", {"id" : "g_photo1_div"});
print( "divPhoto_1 - 1 : " +  str(divPhoto_1.get_text) );



btnImgPopup = driver.find_element_by_css_selector("input[value='사진등록하기']");
btnImgPopup.click();

listWindow = driver.window_handles;
windowSub = "";
for row in listWindow :
    if windowMain != row :
        windowSub = row;

print("windowSub : " + windowSub)

driver.switch_to_window(windowSub)

# btnImgClick = driver.find_element_by_css_selector("input[name='g_photo1']");
# btnImgClick.click();


tmp = "/Users/winiel/Documents/test_image/vans_1.jpg";
driver.find_element_by_css_selector("input[name='g_photo1']").send_keys(tmp);


driver.find_element_by_css_selector("input[value='상품사진등록하기']").click();
Alert(driver).accept();

driver.switch_to_window(windowMain)
soupDoc = BeautifulSoup(driver.page_source, 'html.parser');
divPhoto_1 = soupDoc.find("div", {"id" : "g_photo1_div"});
print( "divPhoto_1 - 2 : " +  str(divPhoto_1.get_text) );



print("end");


# url = "http://www.feelway.com/mypage_sell_list_pop.php?brand_no=&keyword=" + bytes('심플', "utf-8");
# driver.get(url);


