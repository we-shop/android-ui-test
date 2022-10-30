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
from locators.post_locators import *



class SearchPage:
	def search_and_clear_field(self, driver):
		# search request
		switch_to_search_menu = acc_id_click(driver, FOOTER_ITEM_SEARCH)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		make_request_in_search_field = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, "Adidas")
		select_suggested_search_item = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH)

		# verify that we have search result
		first_item_in_search_result_text = el_xpath(driver, FIRST_ITEM_NAME_SEARCH).text

		assert "Adidas".lower() in first_item_in_search_result_text.lower()

		# clear search result
		clear_field = id_click(driver, CLEAR_SEARCH_X_BTN)
		#click_in_search_field = id_click(driver, SEARCH_INPUT_FIELD)
		click_on_search_btn_in_head_bar_again = id_click(driver, SEARCH_BTN_HEAD_BAR)
		#time.sleep(1)

		# asserting recent search name
		recent_search_item_text = el_id(driver, RECENT_SEARCH_ITEM_TEXT).text
		assert recent_search_item_text.lower() == "Adidas".lower()

	def search_product_and_open_detail_page(self, driver):
		# search request
		switch_to_search_menu = acc_id_click(driver, FOOTER_ITEM_SEARCH)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		make_request_in_search_field = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, "Samsung")
		select_suggested_search_item = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH)

		# verify that we have search result
		first_item_in_search_result_text = el_xpath(driver, FIRST_ITEM_NAME_SEARCH).text

		assert "Samsung".lower() in first_item_in_search_result_text.lower()

		# go to product detail page
		first_item_in_search_result_click = xpath_click(driver, FIRST_ITEM_NAME_SEARCH)

		# assert product name on product detail page
		assert "Samsung" in el_id(driver, PRODUCT_NAME_PRICE_BLOCK).text
		

	def search_specific_product_and_open_detail_page(self, driver):
		switch_to_search_menu = acc_id_click(driver, FOOTER_ITEM_SEARCH)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		make_request_in_search_field = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, "Wild dance")
		select_suggested_search_item = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH_ONE_ITEM)
		first_item_in_search_result_click = xpath_click(driver, FIRST_ITEM_NAME_SEARCH)


	def search_extended(self, driver):
		pass

	def search_negative(self, driver):
		pass
