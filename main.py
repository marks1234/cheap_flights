from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the desired URL
driver.get("https://fly.airbaltic.com/en/fb/availability?p=bti&l=en&departure=2023-11-11&originCode=TLL&originType=A&destinCode=LON&destinType=C&numAdt=1&numChd=0&numInf=0&numYth=0&tripType=oneway")

# Wait until the desired element is loaded.
price_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/section/div/div/div[2]/div[1]/div[1]/section/div[2]/div[2]/p/strong/span'))
)

# Extract and print the price

price_main = price_element.text  # 90
# price_sup = price_element.find_element(By.TAG_NAME, 'sup').text  # 99
# final_price = f"{price_main}.{price_sup}€"
print(price_main[:-3] + "," + price_main[-3:])  # Outputs: 90.99€


# Close the browser session
driver.quit()
