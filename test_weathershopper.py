import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.edge.options import Options as Edge_Options
from selenium.webdriver.common.by import By

url = 'https://weathershopper.pythonanywhere.com/'
def test_run_chrome():
    print("Chrome node started")
    chrome_options = Chrome_Options()
    chrome_options.add_argument('--headless')
    remote_url = 'http://localhost:4444/wd/hub'
    # Create a remote WebDriver instance with the desired options and capabilities
    driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
    driver.get(url)
    temp = driver.find_element((By.XPATH,"//span[@id='temperature']"))
    temperature = int(temp.text.strip().split()[0])
    if temperature < 30:
        driver.find_element(By.XPATH, "//button[text()='Buy moisturizers']").click
    else:
        driver.find_element(By.XPATH, "//button[text()='Buy sunscreens']").click
    price_list = driver.find_elements(By.XPATH, "//div[@class='container']//div//p[2]")
    add_button_list = driver.find_elements(By.XPATH, "//button[contains(text(),'Add')]")
    prices = []
    for price in price_list:
        price_element = price.text
        price_value = re.findall(r'\d+', price_element)
        if price_value:
            prices.append(int(price_value[0]))        
        lowest_prices = sorted(prices)[:2]
    for price, add_btn in zip(prices, add_button_list):
        if price in lowest_prices:
            add_btn.click()




def test_run_firefox():
    print("Firefox node started")
    firefox_options = Firefox_Options()
    firefox_options.add_argument('--headless')
    # Set the URL of the Firefox node in the Selenium Grid
    remote_url = 'http://localhost:4444/wd/hub'
    # Create a remote WebDriver instance with the desired options and capabilities
    driver = webdriver.Remote(command_executor=remote_url,options=firefox_options)
    driver.get(url)
    temp = driver.find_element((By.XPATH,"//span[@id='temperature']"))
    temperature = int(temp.text.strip().split()[0])
    if temperature < 30:
        driver.find_element(By.XPATH, "//button[text()='Buy moisturizers']").click
    else:
        driver.find_element(By.XPATH, "//button[text()='Buy sunscreens']").click
    price_list = driver.find_elements(By.XPATH, "//div[@class='container']//div//p[2]")
    add_button_list = driver.find_elements(By.XPATH, "//button[contains(text(),'Add')]")
    prices = []
    for price in price_list:
        price_element = price.text
        price_value = re.findall(r'\d+', price_element)
        if price_value:
            prices.append(int(price_value[0]))        
        lowest_prices = sorted(prices)[:2]
    for price, add_btn in zip(prices, add_button_list):
        if price in lowest_prices:
            add_btn.click()


def test_run_edge():
    print("Edge node started")
    edge_options = Edge_Options()
    edge_options.add_argument('--headless')
    # Set the URL of the Edge node in the Selenium Grid
    remote_url = 'http://localhost:4444/wd/hub'
    # Create a remote WebDriver instance with the desired options and capabilities
    driver = webdriver.Remote(command_executor = remote_url,options=edge_options)
    driver.get(url)
    temp = driver.find_element((By.XPATH,"//span[@id='temperature']"))
    temperature = int(temp.text.strip().split()[0])
    if temperature < 30:
        driver.find_element(By.XPATH, "//button[text()='Buy moisturizers']").click
    else:
        driver.find_element(By.XPATH, "//button[text()='Buy sunscreens']").click
    price_list = driver.find_elements(By.XPATH, "//div[@class='container']//div//p[2]")
    add_button_list = driver.find_elements(By.XPATH, "//button[contains(text(),'Add')]")
    prices = []
    for price in price_list:
        price_element = price.text
        price_value = re.findall(r'\d+', price_element)
        if price_value:
            prices.append(int(price_value[0]))        
        lowest_prices = sorted(prices)[:2]
    for price, add_btn in zip(prices, add_button_list):
        if price in lowest_prices:
            add_btn.click()