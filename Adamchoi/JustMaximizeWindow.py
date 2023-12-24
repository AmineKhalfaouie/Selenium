from selenium import webdriver

web = "https://www.audible.com/search"
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()
