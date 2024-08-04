from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# إعداد Service مع GeckoDriverManager
service = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=service)

# فتح موقع Google
browser.get("https://www.google.com")

# العثور على حقل البحث باستخدام CSS Selector
search_field = browser.find_element(By.CSS_SELECTOR, ".gLFyf")
search_field.send_keys("Front End Developer")

# العثور على زر البحث باستخدام XPath بناءً على `aria-label`
search_button = browser.find_element(By.XPATH, "//input[@aria-label='بحث Google']")
search_field.send_keys(Keys.RETURN) 
search_button.click()