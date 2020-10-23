import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.grailed.com/sold/dT_PqBRw1g")
time.sleep(15)

python_button = driver.find_element_by_xpath("/html/body/div[10]/div/div/a")
python_button.click()

listings = driver.find_element_by_xpath("//*[@id=\"shop\"]/div/div/div[2]/div[1]/div[1]/div/span")
listings = listings.text
listings = int(listings.split(" ")[0].replace(",", ""))

scroll_number = int(round((listings/40) + 1))

for i in range(0, int(round(scroll_number))):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

results = driver.find_elements_by_class_name("feed-item")
print(len(results))

columns = ["Item", "Price", "Date"]
df_alyx = pd.DataFrame(columns=columns)

names = driver.find_elements_by_class_name("listing-title")
names = [name.text for name in names]
df_alyx["Item"] = names

prices = driver.find_elements_by_class_name("listing-price")
prices = [price.text for price in prices]
df_alyx["Price"] = prices

dates = driver.find_elements_by_class_name("date-ago")
clean_dates = []
for date in dates:
    datetext = date.text
    if "(" not in datetext:
        clean_dates.append(datetext)
df_alyx["Date"] = clean_dates


print(df_alyx.head())
df_alyx.to_csv("gosha.csv")
driver.quit()


