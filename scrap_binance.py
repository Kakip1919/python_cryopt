from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from time import sleep
import csv

array_crypt = []
array = []


def scraping_method():
    url = 'https://www.binance.com/ja/markets'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(
        executable_path=r"C:\Users\OW_KAKUTA\PycharmProjects\crypto_display_alert_gui\chromedriver\chromedriver.exe")
    driver.get(url)
    print(driver.current_url)

    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/a/div/div").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#tabContainer > div.css-72ldqd > div.css-qbmpwo > div > div.css-1iivwa2 > div:nth-child(2) > "
                        "div "
                        "> svg").click()
    i = 0
    while i <= 4:
        xpath = "/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/div[3]/div/button[{}]".format(2 + i)

        rtn_crypto_name = driver.find_elements(By.CLASS_NAME, "css-17wnpgm")
        rtn_currency = driver.find_elements(By.CLASS_NAME, "css-iognj9")
        driver.find_element(By.XPATH, xpath).click()
        i += 1
        for rtn_crypto_names in rtn_crypto_name:
            array_crypt.append(rtn_crypto_names.text)

        for rtn_currencies in rtn_currency:
            array_currencies = rtn_currencies.text

        if len(array_crypt) is 100:
            return array_crypt


array_crypt_data = scraping_method()
# 上記のメソッドで取得した通貨の配列をｃｓｖに書き込み
with open('crypto_writer_row.csv', 'w', newline="") as f:
    for i in array_crypt_data:
        array = [[i+"/USDT"]]
        writer = csv.writer(f)
        print(array)
        writer.writerows(array)
