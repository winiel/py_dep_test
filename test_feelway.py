from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

import os

projectPath = (os.path.dirname(os.path.realpath(__file__)) );


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options);

listWindow = driver.window_handles;
print(listWindow);
windowMain = listWindow[0];

# 로그인 (s)
url = "http://www.feelway.com/login.php";
driver.get(url);

driver.find_element_by_name("login_id").send_keys("afrokingdom");
driver.find_element_by_name("login_password").send_keys("taemin1828");
driver.find_element_by_css_selector("input[type=image]").click();


Alert(driver).accept();
# 로그인 (e)


# 상품 등록 약관 동의 (s)
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
# 상품 등록 약관 동의 (e)


# 상품 등록  (s)
##  판매자 보상각서
driver.find_element_by_name("bosang_text").send_keys("2배보상하겠음");


##  브랜드
Select(driver.find_element_by_css_selector("form[name=up_form] select[name=brand_no]")).select_by_visible_text("PRADA")



##  새상품 / 중고품
driver.find_element_by_xpath("//input[@name='new_product'][@value=2]").click();
Alert(driver).accept();

##  상품 종류
### 대분류
Select(driver.find_element_by_css_selector("form[name=up_form] select[name=cate_no]")).select_by_visible_text("가방/핸드백");

### 소분류
Select(driver.find_element_by_css_selector("form[name=up_form] select[name=sub_cate_no]")).select_by_visible_text("크로스백");



##  상품명
driver.find_element_by_name("g_name").send_keys("[테스트]프라다 사피아노 심플 체인백");


##  검색어추가
driver.find_element_by_name("g_name_add_key").send_keys("프라다,프라다체인,핸드폰백");

##  원산지(제조국)
driver.find_element_by_name("g_origin").send_keys("이탈리아");

##  사이즈
driver.find_element_by_name("g_size").send_keys("W18.5cm x H10cm");

## 제품소재
driver.find_element_by_name("material").send_keys("100% 소가죽,사피아노");

## 색상
driver.find_element_by_name("color").send_keys("블랙");

## 제조사/수입사
driver.find_element_by_name("company").send_keys("프라다");

## 취급(사용/세탁)시 주의사항
driver.find_element_by_name("notice").send_keys("없음");

##품질보증기준
driver.find_element_by_name("standard_guarantee").send_keys("더스트백,개런티카드,정품택");

## A/S책임자
driver.find_element_by_name("as_manager_phone").send_keys("01068152820");

## 제조연원/사용기한
driver.find_element_by_name("date_period").send_keys("2017.11");





##  상품사진 (s)


###  사진촬영여부
driver.find_element_by_xpath("//input[@name='real_photo'][@value=1]").click();

###  사진등록하기 (s)

btnImgPopup = driver.find_element_by_css_selector("input[value='사진등록하기']");
btnImgPopup.click();

listWindow = driver.window_handles;
windowSub = "";
for row in listWindow :
    if windowMain != row :
        windowSub = row;

print("windowSub : " + windowSub)

driver.switch_to_window(windowSub)

####  사진등록하기 - window (s)
img_1 = projectPath + "/test_img/prada_1.jpg";
img_2 = projectPath + "/test_img/prada_2.jpg";

driver.find_element_by_css_selector("input[name='g_photo1']").send_keys(img_1);
driver.find_element_by_css_selector("input[name='g_photo2']").send_keys(img_2);


driver.find_element_by_css_selector("input[value='상품사진등록하기']").click();
Alert(driver).accept();
####  사진등록하기 - window (e)

driver.switch_to_window(windowMain)
###  사진등록하기 (e)
##  상품사진 (e)


##  기타정보 (s)

### 흠(스크래치 정보)
driver.find_element_by_name("g_scrach").send_keys("없음 [새상품]");

### 보증서(구매영수증) 유무
driver.find_element_by_xpath("//input[@name='part1'][@value=1]").click();

### 부속품
#### 택
driver.find_element_by_xpath("//input[@name='part2'][@value=1]").click();
#### 게런티 카드
driver.find_element_by_xpath("//input[@name='part3'][@value=1]").click();
#### 케이스
driver.find_element_by_xpath("//input[@name='part5'][@value=1]").click();

### 기타 부속품
driver.find_element_by_name("part_text").send_keys("체인");

##  기타정보 (e)


##  판매가격 (s)
### 판매가격 - 희망가격
driver.find_element_by_name("g_price").send_keys("630000");
### 판매가격 - 가격할인
# driver.find_element_by_name("g_price_kor").send_keys("01068152820");

### 신용카드 결제허용
driver.find_element_by_xpath("//input[@name='card'][@value=1]").click();

### 배송 - 국내배송
driver.find_element_by_xpath("//input[@name='sending_nation'][@value=1]").click();

### 배송 - 배송방법
Select(driver.find_element_by_css_selector("form[name=up_form] select[name=sending_method]")).select_by_visible_text("택배");

##  판매가격 (e)


##  판매자 정보 (s)
driver.find_element_by_name("phone").send_keys("01068152820");
##  판매자 정보 (e)


##  상품소개 (s)
gIntro = "" \
         "PRODUCT INFO\n\r" \
         "\n\r" \
         "● MATERIA  & SIZE ●\n\r" \
         "100% CALFSKIN\n\r" \
         "W18.5cm x H10cm x D3cm\n\r" \
         "체인 높이 53cm\n\r" \
         "\n\r" \
         "● MADE ●\n\r" \
         "MADE IN ITALY\n\r" \
         "\n\r" \
         "● COLOR ●\n\r" \
         "NERO (Black)\n\r" \
         "\n\r" \
         "P R A D A\n\r" \
         "♥ 이태리 명품 프라다 입고 완료 ♥\n\r" \
         "\n\r" \
         "이번 모델은 깔끔하고 심플한 모델이예요. \n\r" \
         "라운드 타입으로 손에 잡히는 그립감두 좋구요\n\r" \
         "골드 체인 스트랩이 고급스러움을 더해줘서\n\r" \
         "데일리로 사용하기 좋으실거예요.\n\r" \
         "\n\r" \
         "프라다의 시그니처 사피아노 소재로 되어 있어서\n\r" \
         "생활 스크래치에도 민감하지 않구요\n\r" \
         "여행 다니실때나, 데일리로 강력추천 드립니다.\n\r" \
         "\n\r" ;
driver.find_element_by_name("g_intro").send_keys(gIntro);
##  상품소개 (e)

## 버튼 - 상품 등록하기
driver.find_element_by_xpath("//input[@type='image'][@src='http://icon.feelway.com/feel_image_02/btn29.gif']").click();

# 상품 등록  (e)

#종료
# driver.quit();

Alert(driver).accept();

print("end");


# url = "http://www.feelway.com/mypage_sell_list_pop.php?brand_no=&keyword=" + bytes('심플', "utf-8");
# driver.get(url);


