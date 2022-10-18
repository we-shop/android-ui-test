#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import string
import random
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
import pytest
from locators.product_detail_locators import PRODUCT_MODAL_CONTINUE_BTN
from appium.webdriver.common.touch_action import TouchAction


# FUCTIONS FOR MOBILE
def id_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, locator))).click()
	except:
		print(f"Element to click by ID: {locator} is not found!")
		pytest.fail("Element to click by ID error")

def xpath_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.XPATH, locator))).click()
	except:
		print(f"Element to click by XPATH: {locator} is not found!")
		print(f"{ERROR}")

def acc_id_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, locator))).click()
	except:
		print(f"Element to click by ACCESSIBILITY ID: {locator} is not found!")
		print(f"{ERROR}")

def el_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		return driver.find_element(By.ID, locator)
	except:
		print(f"Element to find by ID: {locator} is not found!")
		print(f"{ERROR}")

def el_xpath(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		return driver.find_element(MobileBy.XPATH, locator)
	except:
		print(f"Element to find by XPATH: {locator} is not found!")
		print(f"{ERROR}")


def el_xpath_short_wait_with_fail(driver, locator):
	WebDriverWait(driver, 2).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
	return driver.find_element(MobileBy.XPATH, locator)

def el_id_short_wait(driver, locator):
	try:
		WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, locator)))
		#return driver.find_element(By.ID, locator)
	except:
		#print(f"Element to find by ID (short wait): {locator} is not found!")
		print(f"{ERROR}")	

def el_xpath_short_wait(driver, locator):
	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		#return driver.find_element(By.ID, locator)
	except:
		#print(f"Element to find by ID (short wait): {locator} is not found!")
		print(f"{ERROR}")			

def el_acc_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator)))
		return driver.find_element(MobileBy.ACCESSIBILITY_ID, locator)
	except:
		print(f"Element to find by ACCESSIBILITY ID: {locator} is not found!")
		print(f"{ERROR}")

def elems_xpath(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		return driver.find_elements(MobileBy.XPATH, locator)
	except:
		print(f"Elements to find by XPATH: {locator} is not found!")
		print(f"{ERROR}")

def elems_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		return driver.find_elements(By.ID, locator)
	except:
		print(f"Elements to find by ID: {locator} is not found!")
		print(f"{ERROR}")		

def id_until_gone(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, locator)))
	except:
		print(f"Elements by ID: {locator} is not gone!")
		print(f"{ERROR}")

def id_until_gone_short(driver, locator):
	try:
		WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.ID, locator)))
	except:
		print(f"Elements by ID: {locator} is not gone!")
		print(f"{ERROR}")					

def id_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by ID: {locator} is not found!")

def xpath_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by XPATH: {locator} is not found!")

def acc_id_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by ACCESSIBILITY ID: {locator} is not found!")

def get_toast_msg(driver):
	toast_locator = "/hierarchy/android.widget.Toast"
	
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, toast_locator)))
	time.sleep(0.8) # obligatory wait, needed for script pause, between reading of 2 or more toast messages.
	return driver.find_element(MobileBy.XPATH, toast_locator).text


def get_toast_msg_short(driver):
	toast_locator = "/hierarchy/android.widget.Toast"
	
	WebDriverWait(driver, 3).until(EC.presence_of_element_located((MobileBy.XPATH, toast_locator)))
	time.sleep(0.8) # obligatory wait, needed for script pause, between reading of 2 or more toast messages.
	return driver.find_element(MobileBy.XPATH, toast_locator).text


# random letters
def rand_letters(count):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(count))

# NOT IN USE NOW
def click_few_times(locator, clicks):
	if clicks == 1:
		locator.click()
	else:
		for i in range(clicks):
			locator.click()
			time.sleep(0.3)



# returns found element by xpath using js
def js_by_xpath(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	selenium.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0])", locator)
	return elem

# check if checkbox is active (returns True or False)
def js_by_xpath_cbox_status(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	driver.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0]).checked", locator)
	return elem

# check if button is active (returns True or False)
def js_by_xpath_button_status(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	driver.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0]).disabled", locator)
	return elem


def send_enter_key_adb(driver):
	driver.execute_script('mobile: shell', {'command': 'input keyevent', 'args':'KEYCODE_ENTER'}) # send Enter key example (using adb)

def get_correct_text_by_id(driver, locator, text):
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))

	seconds = 5

	while seconds > 0:
		el = driver.find_element(By.ID, locator).text
		if str(text) in el:
			break
		else:
			seconds -=1

	if seconds == 0:
		pytest.fail('Text not found!')


# FILE MANIPUPATION FUNCTIONS
def create_temp_file_and_write_data(data):
	file = open("temp_data.txt", "w+")
	file.write(str(data)+"\n")
	file.close()

def update_temp_file(data):
	with open("temp_data.txt", "a") as f:
		f.write(f"{str(data)}\n")

def read_data_from_temp_file():
	file = open("temp_data.txt", "r")
	return file.read().splitlines()

def clear_data_from_temp_file():
	file = open("temp_data.txt", "w+")
	file.close()


# Solve browser choice
def select_chrome_browser(driver):
	try:
		WebDriverWait(driver, 2.5).until(EC.presence_of_element_located((By.ID, "android:id/icon")))
		all_browsers = driver.find_elements(MobileBy.XPATH, "//android.widget.TextView")
		chrome_click = [i.click() for i in all_browsers if i.text == "Chrome"]
		
		# then click on Just once button
		click_on_just_once_btn = id_click(driver, "android:id/button_once")
		#click_on_always_btn = id_click(driver, "android:id/button_always")
	except:
		pass

# Passing "Taking you to" window function
def taking_you_to_win(driver):
	try:
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, PRODUCT_MODAL_CONTINUE_BTN))).click()
	except:
		print("Taking you to window is not displayed")
		print(f"Expected window is not displayed: {ERROR}")


# Long press function
def long_click_id(driver, locator):
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
	element = driver.find_element(By.ID, locator)
	actions = TouchAction(driver)
	actions.long_press(element)
	actions.perform()

def long_click_xpath(driver, locator):
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
	element = driver.find_element(MobileBy.XPATH, locator)
	actions = TouchAction(driver)
	actions.long_press(element)
	actions.perform()


def scroll_down_slowly(driver):
	driver.swipe(470, 1400, 470, 950, 330)

def scroll_down_deep(driver):
	driver.swipe(470, 1400, 470, 150, 230)

def scroll_on_feed_page(driver):
	time.sleep(2)
	action = TouchAction(driver)
	action.press(x=867, y=1574).wait(1000).move_to(x=867, y=344).release().perform()
	time.sleep(0.3)

def scroll_on_feed_page_more(driver):
	time.sleep(2)
	action = TouchAction(driver)
	action.press(x=537, y=1574).wait(1000).move_to(x=537, y=560).release().perform()
	time.sleep(0.3)	

def scroll_up_on_feed_page(driver):
	time.sleep(2)
	action = TouchAction(driver)
	action.press(x=867, y=1874).wait(1000).move_to(x=867, y=2455).release().perform()
	time.sleep(0.3)	

def horisontal_carousel_swipe(driver):
	time.sleep(2)
	action = TouchAction(driver)
	action.press(x=950, y=1240).wait(1000).move_to(x=280, y=1240).release().perform()
	time.sleep(0.3)

def scroll_down_dashboard(driver):
	driver.swipe(768, 1423, 768, 1657, 330)

def scroll_down_main(driver):
	driver.execute_script('mobile: scrollGesture', {
		'left': 100, 'top': 100, 'width': 200, 'height': 200,
		'direction': 'down',
		'percent': 3.0
	})	


def move_to_element(elem, driver):
	actions = ActionChains(driver)
	actions.move_to_element(elem)
	actions.perform()


def ascroll_into_view(element, driver):
	driver.execute_script("return arguments[0].scrollIntoView();", element)


def scroll_into_view(element, driver):
	driver.execute_script("mobile: scroll", {"direction": 'up', 'element': element})


def round_two_dots(data):
	data_convert = data.split("£")[1].replace(",", ".")
	count_of_dots = 0

	for i in data_convert:
		if i == ".":
			count_of_dots +=1
	
	if count_of_dots == 2:
		second_part_of_number = "." + data_convert.split(".")[2]
		return float(data_convert.replace(second_part_of_number, ""))
	else:
		return float(data_convert)

# element = driver.find_element_by_id("my-id")

# actions = ActionChains(driver)
# actions.move_to_element(element).perform()