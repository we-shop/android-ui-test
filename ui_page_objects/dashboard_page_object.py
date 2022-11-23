from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from datetime import datetime
from ui_page_objects.functions import *
from locators.search_locators import *
from locators.product_detail_locators import *
from locators.dashboard_locators import *
from locators.profile_locators import *


class DashboardPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		self.LOGIN_NEW = LOGIN_NEW
		self.PASSWORD_NEW = PASSWORD_NEW
		self.LOGIN_INT = LOGIN_INT
		self.PASSWORD_INT = PASSWORD_INT
		self.LOGIN_INT_NEW = LOGIN_INT_NEW
		self.PASSWORD_INT_NEW = PASSWORD_INT_NEW


	def wenews_check(self, driver):
		# open dashboard > wenews
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)
		go_to_wenews_tab = acc_id_click(driver, DASHBOARD_WENEWS_TAB)

		# open first news item
		read_first_post_title = el_id(driver, DASH_WENEWS_POST_TITLE).text
		first_news_item_read_more_click = id_click(driver, DASH_WENEWS_READ_MORE_BTN)
		read_post_title_inside = el_xpath(driver, DASH_WENEWS_READ_MORE_POST_TITLE).text

		# check that title from preview is the same as inside post
		assert len(read_first_post_title) - len(read_post_title_inside) < 2


	def new_acc_check(self, driver):
		# open dashboard > weshares
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)

		# check weshares tab stubs for new account
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_IMG).is_displayed()
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_TITLE).is_displayed()
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_TEXT).is_displayed()
		assert el_id(driver, DASH_WESHARES_BOTTOM_HINT).is_displayed()
		 
		# check transactions tab stubs for new account
		go_to_transactions_tab = acc_id_click(driver, DASHBOARD_TRANSACTIONS_TAB)
		assert el_id(driver, DASH_TRANS_EMPTY_PURCHASES_STUB).is_displayed()
		assert el_id(driver, DASH_TRANS_EMPTY_INFLUENCE_SALES_STUB).is_displayed()
		assert el_id(driver, DASH_TRANS_EMPTY_REFERRALS_STUB).is_displayed()
		#assert el_id(driver, DASH_TRANS_EMPTY_SHARE_BTN).is_displayed() # not needed in latest build (oct 2022)


	def existing_acc_check(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")
		
		CURRENT_DATE = datetime.today().strftime('%d.%m.%y')

		# open dashboard
		click_on_profile_footer_item = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)

		# check weshares tab
		# OLD
		#weshares_chart = el_id(driver, DASH_WESHARES_CHART)
		#assert weshares_chart.is_displayed()

		close_bottom_hint_message = id_click(driver, DASH_WESHARES_BOTTOM_HINT_CLOSE_BTN)

		last_updated = el_id(driver, DASH_WESHARES_LAST_UPDATED).text.split(", ")[1]
		assert last_updated == CURRENT_DATE
		
		share_price = round_two_dots(el_id(driver, DASH_WESHARES_SHARE_PRICE).text) #float(el_id(driver, DASH_WESHARES_SHARE_PRICE).text.split("£")[1].replace(",", "."))
		assert share_price > 0

		your_weshare_top = round_two_dots(el_id(driver, DASH_WESHARES_YOUR_WESHARE_TOP).text) #float(el_id(driver, DASH_WESHARES_YOUR_WESHARE_TOP).text.split("£")[1].replace(",", "."))
		print(your_weshare_top)
		#assert your_weshare_top > 100

		your_weshare_bottom = float(el_id(driver, DASH_WESHARES_YOUR_WESHARE_BOTTOM).text)
		print(your_weshare_bottom)
		#assert your_weshare_bottom > 100

		# NEED TO FIX SCROLL BUG
		# support URL check
		#click_on_support_link = id_click(driver, DASH_WESHARES_SUPPORT_LINK)
		#select_chrome_browser(driver)
		#page_url_support = el_id(driver, BROWSER_URL_BAR).text
		#assert page_url_support == "help.we.shop/en/"
		#driver.back()

		# switch to transactions tab
		click_on_transactions_tab = acc_id_click(driver, DASHBOARD_TRANSACTIONS_TAB)

		# check purchases
		click_on_show_more_purchases = id_click(driver, DASH_TRANS_SHOW_MORE_PURCHASES)
		time.sleep(1)
		#id_until_gone_short(driver, PRE_LOADER)

		error = False

		try:
			read_possible_error = get_toast_msg_short(driver)
			error = True 
		except:
			pass 

		if error:
			print(read_possible_error)
			print(F"{ERROR_IN_TOAST}")
		else:
			pass

		purchased_product_title = len(el_id(driver, DASH_TRANS_SHOW_MORE_PRODUCT_TITLE).text)
		purchased_product_price = round_two_dots(el_id(driver, DASH_TRANS_SHOW_MORE_PRICE).text) #float(el_id(driver, DASH_TRANS_SHOW_MORE_PRICE).text.split("£")[1].replace(",", "."))

		assert purchased_product_title > 3
		assert purchased_product_price > 0
		driver.back()

		# check influenced sales
		click_on_show_more_sales = id_click(driver, DASH_TRANS_SHOW_MORE_SALES)
		id_until_gone_short(driver, PRE_LOADER)
		influenced_sales_product_title = len(el_id(driver, DASH_TRANS_SHOW_MORE_PRODUCT_TITLE).text)
		influenced_sales_price = round_two_dots(el_id(driver, DASH_TRANS_SHOW_MORE_PRICE).text) #float(el_id(driver, DASH_TRANS_SHOW_MORE_PRICE).text.split("£")[1].replace(",", "."))

		assert influenced_sales_product_title > 3
		assert influenced_sales_price > 0
		driver.back()

		# check refferals
		click_on_show_more_referrals = id_click(driver, DASH_TRANS_SHOW_MORE_REFERRALS)
		id_until_gone_short(driver, PRE_LOADER)

		read_my_invited_referral_name = len(el_id(driver, DASH_TRANS_SHOW_MORE_PRODUCT_TITLE).text)
		read_my_invited_referral_username = el_id(driver, DASH_TRANS_SHOW_MORE_REFFERALS_USERNAME).text

		# OLD
		#read_referral_header_title = el_id(driver, DASH_TRANS_SHOW_MORE_REFERRALS_HEADER).text
		#read_link_in_share_input = el_xpath(driver, DASH_TRANS_SHOW_MORE_REFERRALS_NICK_INPUT).text.split("@")[1]
		#assert read_referral_header_title == "Invite your friends"
		#assert read_link_in_share_input == USERNAME

		assert read_my_invited_referral_name > 5
		assert "@" in read_my_invited_referral_username
		assert len(read_my_invited_referral_username) > 4

		driver.back()

		# reffer and earn tab
		go_to_refer_n_earn_tab = acc_id_click(driver, DASHBOARD_REFER_N_EARN_TAB)
		wait_for_share_username_btn = el_id(driver, DASH_REFER_N_EARN_SHARE_USRN_BTN)
		wait_for_terms_link = el_id(driver, DASH_REFER_N_EARN_TERMS_LINK)


