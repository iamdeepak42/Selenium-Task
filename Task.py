from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://www.ionicpartners.com/')
actions = ActionChains(driver)

blog_link = driver.find_element(By.XPATH, "(//rs-layer-wrap[contains(@class,'rs-parallax-wrap')]//following::a[contains(text(),'Blog')])[1]")
blog_link.click()

# Scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

# Click on Abouut us link to navigate to Blog page
aboutus_link = driver.find_element(By.XPATH, "(//a[contains(text(),'About Us')])[1]")
aboutus_link.click()

# Scroll down to Twitter Icon at bottom
twitter_icon = driver.find_element(By.XPATH, "//a[@href='https://twitter.com/IonicPartners']")
actions.move_to_element(twitter_icon).perform()

# Click on the Twitter Icon
twitter_icon.click()
print(driver.current_url)
