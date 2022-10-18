from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.profile_locators import *
from locators.login_locators import *
from locators.search_locators import *
from locators.debug_locators import *
from locators.inbox_locators import *
from locators.product_detail_locators import *
from appium.webdriver.common.mobileby import By

class InboxPage:
	# def __init__(self, LOGIN_URL, LOGIN, PASSWORD):
	# 	self.LOGIN_URL = LOGIN_URL
	# 	self.LOGIN = LOGIN
	# 	self.PASSWORD = PASSWORD

	def inbox_check(self, driver):
		# checking inbox page
		is_inbox_messages = None
		go_to_inbox_click = acc_id_click(driver, FOOTER_ITEM_INBOX)
		#getting_all_inbox_message_titles = elems_id(driver, ALL_INBOX_TITLES)
		try:
			el_id_short_wait(driver, ALL_INBOX_TITLES)
			check_msgs = elems_id(driver, ALL_INBOX_TITLES)
			getting_all_inbox_message_titles = [i.text for i in check_msgs]
			is_inbox_messages = True
		except:
			# checking stun "No activity here, yet" in case when activity list is empty
			assert "No activity here, yet" in el_id(driver, NO_CONTENT_TEXT).text

		# if is_inbox_messages:
		# 	print(getting_all_inbox_message_titles)
		

	def inbox_post_and_question_redirects(self, driver):
		# checking inbox page
		is_inbox_messages = None
		go_to_inbox_click = acc_id_click(driver, FOOTER_ITEM_INBOX)
		#getting_all_inbox_message_titles = elems_id(driver, ALL_INBOX_TITLES)
		try:
			el_id_short_wait(driver, ALL_INBOX_TITLES)
			check_msgs = elems_id(driver, ALL_INBOX_TITLES)
			getting_all_inbox_message_titles = [i.text for i in check_msgs]
			is_inbox_messages = True
		except:
			# checking stun "No activity here, yet" in case when activity list is empty
			assert "No activity here, yet" in el_id(driver, NO_CONTENT_TEXT).text


		print(getting_all_inbox_message_titles)
		have_post_like = None
		have_question_like = None
		
		if is_inbox_messages:
			for i in elems_id(driver, ALL_INBOX_TITLES):
				if "liked your post" in i.text:
					i.click()
					have_post_like = True
					break
			else:
				pass

		print(have_post_like)
		if have_post_like:
			try:
				assert el_xpath(driver, POST_HEAD_TITLE_YOUR_PRODUCT).text == "Your post"
				driver.back()
			except:
				pass

		#time.sleep(3)

		if is_inbox_messages:	
			for i in elems_id(driver, ALL_INBOX_TITLES):
				if "liked your question" in i.text:
					i.click()
					have_question_like = True
					break
			else:
				pass		

		if have_question_like:
			try:
				assert el_xpath(driver, POST_HEAD_TITLE_YOUR_PRODUCT).text == "Your question"
				driver.back()
			except:
				pass

		
		

		
		
		
		
		