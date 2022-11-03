from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
import time
import pytest
import random
import requests
from ui_page_objects.functions import *
from locators.profile_locators import *
from locators.login_locators import *
from locators.search_locators import *
from locators.debug_locators import *
from locators.post_locators import *



class ProfilePage:
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

	def followings_followers_count(self, driver):
		# read count of followers and following
		profile_followers = int(el_id(driver, FOLLOWERS_COUNT).text)
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# going to followers/following and reading real count of followers/following
		click_on_followers_btn = id_click(driver, FOLLOWERS_LABEL_PROFILE)
		total_count_of_existing_followers = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))
		click_on_following_tab = acc_id_click(driver, PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB)
		total_count_of_existing_following = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))


		# assertion of real and readed count of followers/following
		# we unable to see more then 7 items without scroll
		if profile_followers >= 7:
			assert total_count_of_existing_followers >= 7
		else:	
			assert profile_followers == total_count_of_existing_followers

		# cover vision issue (unable to detect hidden items)
		# we unable to see more then 7 items without scroll
		if profile_following >= 7:
			assert total_count_of_existing_following >= 7
		else:	
			assert profile_following == total_count_of_existing_following

	def OLD_edit_profile(self, driver):
		# random data
		RANDOM_FIRST_NAME = rand_letters(7)
		RANDOM_LAST_NAME = rand_letters(7)
		RANDOM_BIO_NAME = rand_letters(12)

		# go to settings > edit
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		click_on_settings_edit_btn = id_click(driver, PROFILE_SETTINGS_EDIT_BTN)

		# temprorary flow is not fully completed [WILL BE FINISHED IN FUTURE > UPLOAD STAGE IS NOT COMPLETED]
		# profie photo change (open > cancel flow)
		click_on_profile_photo_change_btn = id_click(driver, PROFILE_EDIT_PHOTO_CHANGE_ICON)
		click_on_take_photo_in_window = xpath_click(driver, PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO)
		time.sleep(3) #obligatory wait to open phone camera
		driver.back()
		toast_error_msg_get = get_toast_msg(driver)
		expected_message_one = "Sorry, an error occurred while trying to pick up the image. Please try again or pick up a different image."
		expected_message_two = "Media unrecognised. Please select a valid image or video and try again."

		# checking expected error message (2 possible variants)
		assert toast_error_msg_get == expected_message_one or expected_message_two == expected_message_two

		# editing first/last name and bio
		edit_first_name_field = id_keys(driver, PROFILE_EDIT_FIRST_NAME_FIELD, RANDOM_FIRST_NAME)
		edit_last_name_field = id_keys(driver, PROFILE_EDIT_LAST_NAME_FIELD, RANDOM_LAST_NAME)
		edit_bio_name_field = id_keys(driver, PROFILE_EDIT_BIO_FIELD, RANDOM_BIO_NAME)
		click_on_save_changes_btn = id_click(driver, PROFILE_EDIT_SAVE_CHANGES_BTN)
		
		# refresh manupulation to see new profile data
		click_on_back_btn = driver.back() #acc_id_click(driver, BACK_BTN)
		click_on_footer_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_footer_profile_btn = acc_id_click(driver, FOOTER_ITEM_PROFILE)

		# asserting edited first/last name and bio
		read_first_and_last_name_text = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text
		read_bio_text = el_id(driver, PROFILE_BIO).text
		compared_first_and_last_random_names = RANDOM_FIRST_NAME + " " + RANDOM_LAST_NAME

		assert read_first_and_last_name_text == compared_first_and_last_random_names
		assert read_bio_text == RANDOM_BIO_NAME


	def edit_profile(self, driver):
		# random data
		RANDOM_FIRST_NAME = rand_letters(7)
		RANDOM_LAST_NAME = rand_letters(7)
		RANDOM_BIO_NAME = rand_letters(12)

		# go to settings > edit
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		click_on_settings_edit_btn = id_click(driver, PROFILE_SETTINGS_EDIT_BTN)

		# temprorary flow is not fully completed [WILL BE FINISHED IN FUTURE > UPLOAD STAGE IS NOT COMPLETED]
		# profie photo change (open > cancel flow)
		click_on_profile_photo_change_btn = id_click(driver, PROFILE_EDIT_PHOTO_CHANGE_ICON)
		click_on_take_photo_in_window = xpath_click(driver, PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO)
		time.sleep(2.5) #obligatory wait to open phone camera
		driver.back()
		time.sleep(1.5)
		toast_error_msg_get = get_toast_msg(driver)
		expected_message = "Something went wrong trying to select this image."
		#expected_message_one = "Sorry, an error occurred while trying to pick up the image. Please try again or pick up a different image."
		#expected_message_two = "Media unrecognised. Please select a valid image or video and try again."


		# checking expected error message (2 possible variants) 
		# OLD
		#assert toast_error_msg_get == expected_message_one or expected_message_two == expected_message_two
		assert toast_error_msg_get == expected_message

		# editing first/last name
		edit_first_name_field = xpath_keys(driver, PROFILE_EDIT_FIRST_NAME_FIELD, RANDOM_FIRST_NAME)
		edit_last_name_field = xpath_keys(driver, PROFILE_EDIT_LAST_NAME_FIELD, RANDOM_LAST_NAME)

		time.sleep(1.4) # obligatory wait to avoit toast messages
		scroll_down_deep(driver)
		time.sleep(1.2) # obligatory wait, between scrolls
		scroll_down_deep(driver)

		# manipulation with "your interests"
		UNCHECK_BOXES = None
		total_count_of_interests = len(elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES))
		total_count_of_checked_interests = len([i for i in elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES) if i.get_attribute("checked") == "true"])

		if total_count_of_checked_interests >= 5:
			UNCHECK_BOXES = True
			rand_boxes_to_uncheck = random.sample([i for i in elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES) if i.get_attribute("checked") == "true"], 2)
			for i in rand_boxes_to_uncheck:
				i.click()
		elif total_count_of_checked_interests < 3:
			rand_boxes_to_fill = [i for i in elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES) if i.get_attribute("checked") == "false"]
			for i in rand_boxes_to_fill:
				i.click()
		else:
			UNCHECK_BOXES = False
			rand_boxes_to_check	= random.sample([i for i in elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES) if i.get_attribute("checked") == "false"], 2)
			for i in rand_boxes_to_check:
				i.click()

		re_read_count_of_checked_interests = len([i for i in elems_xpath(driver, PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES) if i.get_attribute("checked") == "true"])

		if UNCHECK_BOXES:
			assert total_count_of_checked_interests == re_read_count_of_checked_interests + 2

		elif UNCHECK_BOXES == None:
			total_count_of_checked_interests == total_count_of_interests

		else:
			assert total_count_of_checked_interests == re_read_count_of_checked_interests - 2		
		
		scroll_down_deep(driver)
		time.sleep(1.2) # obligatory wait, between scrolls

		# editing first/last name
		edit_bio_name_field = xpath_keys(driver, PROFILE_EDIT_BIO_FIELD, RANDOM_BIO_NAME)
		scroll_down_deep(driver)
		click_on_save_changes_btn = id_click(driver, PROFILE_EDIT_SAVE_CHANGES_BTN)
		
		# refresh manupulation to see new profile data
		#click_on_back_btn = acc_id_click(driver, BACK_BTN) #not needed anymore (commented from #sep 2022)
		click_on_footer_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_footer_profile_btn = acc_id_click(driver, FOOTER_ITEM_PROFILE)

		# asserting edited first/last name and bio
		read_first_and_last_name_text = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text
		read_bio_text = el_id(driver, PROFILE_BIO).text
		compared_first_and_last_random_names = RANDOM_FIRST_NAME + " " + RANDOM_LAST_NAME

		assert read_first_and_last_name_text == compared_first_and_last_random_names
		assert read_bio_text == RANDOM_BIO_NAME		

	def deactivate_account_and_login_after(self, driver):
		# deactivate account
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		#driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		scroll_down_deep(driver)
		deactivate_acc_click = xpath_click(driver, SETTINGS_DEACTIVATE_ACC)
		deactivate_acc_btn_click = id_click(driver, DEACTIVATE_ACCOUNT_BTN)
		accept_are_you_sure_modal = id_click(driver, DEACTIVATE_ACC_ACCEPT_IN_MODAL)

		# check if user logged out
		already_have_account_btn_click = id_click(driver, ALREADY_HAVE_ACC_LOGIN_SCREEN)
		read_welcome_back_text_on_login_screen = el_id(driver, READ_WELCOME_TEXT_LOGIN_SCREEN).text

		assert read_welcome_back_text_on_login_screen == "Welcome back!"

		# login after deactivation
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile from footer menu (to make sure you are already logged in)
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)	

	def following_count_manipulations_in_profile(self, driver):
		# read count of followers and following
		profile_followers = int(el_id(driver, FOLLOWERS_COUNT).text)
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# going to followers/following and follow for some followers
		click_on_followers_btn = id_click(driver, FOLLOWERS_LABEL_PROFILE)
		find_all_follow_btns = elems_xpath(driver, LIST_OF_ALL_FOLLOW_BTNS)

		follow_count = 0
		follow_clicked = 0
		follow_unclicked = 0

		# calculating available count of actual "follow" buttons
		# checking if user have at least 1 follower
		if profile_followers == 0:
			print("Re-check account, you need to have at least 1 follower")
			print(f"{ERROR}")

		# calculating how many user have "follow" buttons in followers tab
		for btns in find_all_follow_btns:
			if btns.text == "Follow":
				btns.click()
				follow_count +=1
				follow_clicked +=1

		# click conditions, according to "follow" buttons
		if follow_count == 0:
			if profile_followers == 1:
				xpath_click(driver, FIRST_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 1
			elif profile_followers == 2:
				xpath_click(driver, FIRST_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 1
			else:
				xpath_click(driver, SECOND_BTN_IN_FOLLOWERS_TAB)
				xpath_click(driver, THIRD_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 2

		# going back to profile
		driver.back()
		click_on_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		re_reading_followings_count = int(el_id(driver, FOLLOWINGS_COUNT).text)

		#print(re_reading_followings_count)

		# assertions
		if follow_clicked > 0:
			assert re_reading_followings_count == (profile_following + follow_clicked)
		else:
			assert re_reading_followings_count == (profile_following - follow_unclicked)

		
		# going to following to make sure that current count match existing count of following
		click_on_following_btn = id_click(driver, FOLLOWINGS_LABEL_PROFILE)
		time.sleep(0.6) # obligatory wait to avoid miscalculations of following items
		calculate_all_following_btns = len(elems_xpath(driver, LIST_OF_ALL_FOLLOW_BTNS))

		# cover vision issue (unable to detect hidden items)
		if re_reading_followings_count >= 8:
			assert calculate_all_following_btns >= 8
		else:	
			assert calculate_all_following_btns == re_reading_followings_count


	def follow_few_users(self, driver):
		# test users
		USER_1 = "Molosay"
		USER_2 = "Veremeychik"
		follow = 0
		unfollow = 0 

		# read count of following
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# search for user
		switch_to_search_menu = acc_id_click(driver, FOOTER_ITEM_SEARCH)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		make_request_in_search_field = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, USER_1)
		select_suggested_search_item = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH_PROFILE)


		# searching USER_1 and subscribing/unsubscribing
		#search_user_one = id_keys(driver, SEARCH_INPUT_FIELD, USER_1)
		#click_on_suggested_item_in_search = id_click(driver, SEARCH_RESULT_ONE_ITEM_TEXT)
		follow_btn_user_one_text = el_id(driver, FOLLOW_TO_USER_BTN).text

		if follow_btn_user_one_text == "Follow":
			id_click(driver, FOLLOW_TO_USER_BTN)
			follow += 1
		else:
			id_click(driver, FOLLOW_TO_USER_BTN)
			unfollow += 1

		driver.back()
		
		# searching USER_2 and subscribing/unsubscribing
		clear_search_btn_click = id_click(driver, CLEAR_SEARCH_X_BTN)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		search_user_two = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, USER_2) #id_keys(driver, SEARCH_INPUT_FIELD, USER_2) 
		click_on_suggested_item_in_search = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH_PROFILE) #id_click(driver, SEARCH_RESULT_ONE_ITEM_TEXT)
		follow_btn_user_two_text = el_id(driver, FOLLOW_TO_USER_BTN).text

		if follow_btn_user_two_text == "Follow":
			id_click(driver, FOLLOW_TO_USER_BTN)
			follow += 1
		else:
			id_click(driver, FOLLOW_TO_USER_BTN)
			unfollow += 1

		driver.back()

		# going back to profile
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_footer_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		time.sleep(1) # for sure, refresh purpose
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		re_reading_profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# asserting following counter
		# DEBUG PRINTS
		# print(profile_following)
		# print("Follow" + str(follow))
		# print("Unfollow" + str(unfollow))
		# print(re_reading_profile_following)
		assert re_reading_profile_following == ((profile_following + follow) - unfollow)


	def info_pages_check(self, driver):
		# Going to info pages menu
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		click_on_settings_legal_n_terms_menu = xpath_click(driver, SETTINGS_LEGAL_N_TERMS)

		# Terms check
		click_on_menu_terms = xpath_click(driver, MENU_TERMS)
		select_chrome_browser(driver)
		page_url_terms = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_terms == "legal.we.shop/terms-and-conditions"
		driver.back()

		# Privacy policy check
		click_on_menu_privacy_policy = xpath_click(driver, MENU_POLICY)
		select_chrome_browser(driver)
		page_url_privacy_policy = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_privacy_policy == "legal.we.shop/privacy-policy"
		driver.back()

		# Cookie policy check
		click_on_menu_cookies = xpath_click(driver, MENU_COOKIE)
		select_chrome_browser(driver)
		page_url_cookie = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_cookie == "help.we.shop/en/article/cookie-policy-pu4kpj/"
		driver.back()

		# Acknowledgements check
		click_on_menu_acknowledgements = xpath_click(driver, MENU_ACKNOWLEDGEMENTS)
		select_chrome_browser(driver)
		page_url_acknowledgements = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_acknowledgements == "help.we.shop/en/article/acknowledgements-7z42ii/?bust=1629990511519"
		driver.back()

		# Community Guidelines check
		click_on_menu_community_guidelines = xpath_click(driver, MENU_COMMUNITY_GUIDES)
		select_chrome_browser(driver)
		page_url_cummunity_guides = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_cummunity_guides == "help.we.shop/en/article/community-guidelines-m34bm5/"
		driver.back()

	def customer_support_page_check(self, driver):
		# make back, because this test bound with info_pages_check test
		driver.back()

		# Going to info pages menu
		click_on_settings_customer_support = xpath_click(driver, SETTINGS_CUSTOMER_SUPPORT)

		# Customer support check
		select_chrome_browser(driver)
		page_url_terms = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_terms == "help.we.shop/en/"
		driver.back()
	

	def about_version_check(self, driver):
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


		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# handling info block after login
		try:
			id_click(driver, CLOSE_BTN_LOGIN)
		except:
			pass

		# going to profile settings
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)

		# going to settings > about and reading app version
		click_on_about = xpath_click(driver, SETTINGS_ABOUT)
		read_app_version_in_profile_about = el_xpath(driver, APP_VERSION_SETTINGS_ABOUT).text
		read_app_version_from_file = read_data_from_temp_file()[1]

		assert read_app_version_from_file == read_app_version_in_profile_about

	def other_user_posts_n_questions(self, driver):
		# test users
		USER_1 = "@nemesis"
		USER_2 = "Veremeychik"
		follow = 0
		unfollow = 0 


		switch_to_search_menu = acc_id_click(driver, FOOTER_ITEM_SEARCH)
		click_on_search_btn_in_head_bar = id_click(driver, SEARCH_BTN_HEAD_BAR)
		make_request_in_search_field = xpath_keys(driver, COLLAPSED_SEARCH_INPUT_FIELD, USER_1)
		click_on_suggested_item_in_search = xpath_click(driver, SEARCH_RESULT_FOURTH_ITEM)
		#select_suggested_search_item = xpath_click(driver, SELECT_SUGGESTED_ITEM_SEARCH_ONE_ITEM)
		#first_item_in_search_result_click = xpath_click(driver, FIRST_ITEM_NAME_SEARCH)

		
		#search_user_one = id_keys(driver, SEARCH_INPUT_FIELD, USER_1)
		#click_on_suggested_item_in_search = xpath_click(driver, SEARCH_RESULT_SECOND_ITEM)
		read_opened_profile = el_id(driver, PROFILE_USERNAME).text
		assert read_opened_profile == USER_1
		read_profile_first_and_last_name = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text

		# post tab manipulation		
		nested_product_count = None

		try:
			if el_xpath(driver, NESTED_PRODUCTS_COUNT_IN_POST).is_displayed():
				nested_product_count = int(el_xpath(driver, NESTED_PRODUCTS_COUNT_IN_POST).text.split("+")[1]) + 1
		except:
			nested_product_count = False

		
		if nested_product_count != False:
			read_product_post_name = el_xpath(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT).text
			go_to_first_product = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT)
			assert nested_product_count == len(elems_xpath(driver, READ_SINGLE_PRODUCT_LINEAR_LAYOUTS))
		else:
			read_product_post_name = el_xpath(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT_SPECIAL).text
			go_to_first_product = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT)
			

		read_product_name_on_post_page = el_id(driver, POST_PRODUCT_TITLE).text
		read_user_name_in_post = el_id(driver, POST_USERNAME).text
		
		assert read_product_post_name == read_product_name_on_post_page
		assert read_profile_first_and_last_name == read_user_name_in_post

		driver.back()

		# question tab manipulation
		switch_to_question_tab = acc_id_click(driver, PROFILE_QUESTIONS_TAB)
		##############################################################################
		# NEED TO ADD CHECK FOR COUNT OF PRODUCT IN QUESTION, WHEN WILL BE IMPLEMENTED
		##############################################################################
		click_on_first_question = xpath_click(driver, FIRST_QUESTION_IN_QUEST_TAB)
		read_username_in_question = el_id(driver, POST_USERNAME).text

		assert el_id(driver, QUESTION_REPLY_LABEL).is_displayed()
		assert read_profile_first_and_last_name == read_username_in_question
		
	def wishlist_likes_and_comments(self, driver):
		got_to_wishlists_tab = acc_id_click(driver, PROFILE_WISHLIST_TAB)
		click_on_first_wishlist_in_grid = xpath_click(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)

		# manipulation with likes
		assert el_xpath(driver, PROFILE_FIRST_ITEM_TEXT_INSIDE_WISHLIST).is_displayed()

		time.sleep(0.5)
		read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		final_count_of_likes = 0

		if read_likes_in_wishlist == 0:
			click_on_like_btn = id_click(driver, LIKES_IN_POST)
			re_read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
			assert re_read_likes_in_wishlist == read_likes_in_wishlist + 1
			final_count_of_likes = read_likes_in_wishlist + 1
		elif read_likes_in_wishlist == 1:
			click_on_like_btn = id_click(driver, LIKES_IN_POST)
			re_read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0]) # added text.split(" ")[0]
			if re_read_likes_in_wishlist == 0:
				click_on_like_btn = id_click(driver, LIKES_IN_POST)
				re_re_read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
				assert re_re_read_likes_in_wishlist == 1
				final_count_of_likes = 1
			else:
				assert re_read_likes_in_wishlist == 2
				final_count_of_likes = 2

		else:
			click_on_like_btn = id_click(driver, LIKES_IN_POST)		
			re_read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])

			if re_read_likes_in_wishlist == read_likes_in_wishlist - 1:
				click_on_like_btn = id_click(driver, LIKES_IN_POST)
				re_re_read_likes_in_wishlist = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
				assert re_re_read_likes_in_wishlist == read_likes_in_wishlist
				final_count_of_likes = re_re_read_likes_in_wishlist
			else:
				assert re_read_likes_in_wishlist == read_likes_in_wishlist + 1
				final_count_of_likes = read_likes_in_wishlist + 1

			
		
		# manipulation with comments
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])				

		
		go_to_wishlist_comments = id_click(driver, GO_TO_COMMENTS_BTN)

		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for post")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		driver.back()
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])
		read_again_likes_count = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		
		
		# WILL BE UNCOMMENTED AFTER BUG FIX
		#asserting comments and likes (because of often bug in past)
		print(read_comments_count)
		print(re_read_comments_count)
		print(final_count_of_likes)
		print(read_again_likes_count)
		assert re_read_comments_count == read_comments_count + 1

		assert read_again_likes_count == final_count_of_likes

	def share_profile_post_and_product(self, driver):
		current_env = read_data_from_temp_file()[0]
		current_usr = read_data_from_temp_file()[1]

		# clicking share profile button and getting data from clipboard
		click_on_profile_share_btn = id_click(driver, PROFILE_SHARE_BUTTON)
		click_on_copy_btn = id_click(driver, SHARE_WINDOW_COPY_BTN)
		
		get_profile_text_from_clipboard = driver.get_clipboard_text()
		
		assert len(get_profile_text_from_clipboard.split("/")) == 4
		
		#assert current_env in get_profile_text_from_clipboard # not in use, because of short links implementation

		# send request to get username in URL
		req = requests.get(get_profile_text_from_clipboard)
		response_text = req.text

		assert current_usr in response_text

		# go to post in profile and check share functionality
		click_on_first_product_in_posts_tab = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT)
		click_on_share_post_btn = id_click(driver, PROFILE_POST_SHARE_BUTTON)
		click_on_copy_btn = id_click(driver, SHARE_WINDOW_COPY_BTN)

		get_post_text_from_clipboard = driver.get_clipboard_text()

		assert len(get_post_text_from_clipboard.split("/")) == 4

		# go to product and check share functionality
		click_on_product_in_post = id_click(driver, POST_PRODUCT_TITLE)
		click_on_share_product_btn = id_click(driver, PRODUCT_SHARE_BUTTON)
		click_on_copy_btn = id_click(driver, SHARE_WINDOW_COPY_BTN)

		get_product_text_from_clipboard = driver.get_clipboard_text()

		assert len(get_product_text_from_clipboard.split("/")) == 4


	def wishlist_crud(self, driver):
		RANDOM_WISHLIST_NAME = "New wishlist " + rand_letters(7)
		RANDOM_EDITED_WISHLIST_NAME = "Edited wishlist " + rand_letters(7)

		# creating new wishlist
		go_to_wishlist_tab = acc_id_click(driver, PROFILE_WISHLIST_TAB)
		wait_wishlist_items = el_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)
		scroll_on_feed_page(driver)

		click_plus_icon = id_click(driver, ADD_NEW_WISHLIST_ITEM_PLUS_ICON)

		enter_wishlist_name = id_keys(driver, ADD_NEW_WISHLIST_INPUT_NAME, RANDOM_WISHLIST_NAME)
		save_new_wishlist = id_click(driver, ADD_NEW_WISHLIST_SAVE_BUTTON)

		time.sleep(1) #obligatory wait after wishlist creation

		switch_to_post_tab = acc_id_click(driver, PROFILE_POSTS_TAB) # purpose: refresh wishlist items
		switch_back_to_wishlists_tab = acc_id_click(driver, PROFILE_WISHLIST_TAB)

		read_created_wishlist_name = [i.text for i in elems_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)]
		read_all_hide_icons_count = len(driver.find_elements(By.ID, WISHLIST_GRID_HIDE_ICON))

		assert RANDOM_WISHLIST_NAME in read_created_wishlist_name
		assert read_all_hide_icons_count == 0 # should be 0

		# try/except block to avoid unknown java error
		try:
			go_to_created_wishlist = [i.click() for i in elems_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID) if i.text == RANDOM_WISHLIST_NAME]
		except:
			pass

		wait_plus_icon = el_id(driver, ADD_NEW_WISHLIST_ITEM_PLUS_ICON)

		# edit created wishlist
		open_sub_menu = id_click(driver, ADD_NEW_WISHLIST_MORE_BUTTON)
		click_on_sub_menu_edit_item = xpath_click(driver, WISHLIST_SUB_MENU_EDIT)

		clear_wishlist_field = el_id(driver, WISHLIST_EDIT_NAME_INPUT).clear()
		edit_wishlist_name =id_keys(driver, WISHLIST_EDIT_NAME_INPUT, RANDOM_EDITED_WISHLIST_NAME)
		make_wishlist_not_public = id_click(driver, WISHLIST_EDIT_IS_PUBLIC_SWITCHER)
		save_edited_changes = id_click(driver, WISHLIST_EDIT_SAVE_BUTTON)

		wait_plus_icon_after_edit = el_id(driver, ADD_NEW_WISHLIST_ITEM_PLUS_ICON)
		time.sleep(2.2) # obligatory wait (for update edited name in toolbar)

		read_edited_wishlist_name_in_toolbar = el_xpath(driver, WISHLIST_NAME_TOOLBAR_TEXT).text
		assert read_edited_wishlist_name_in_toolbar == RANDOM_EDITED_WISHLIST_NAME

		driver.back()

		# check edit changes in grid
		wait_wishlist_items = el_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)
		time.sleep(2) # obligatory wait (for update edited name + hide icon in grid)

		assert el_id(driver, WISHLIST_GRID_HIDE_ICON).is_displayed()

		# delete created wishlist
		go_to_edited_wishlist = xpath_click(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)
		open_sub_menu = id_click(driver, ADD_NEW_WISHLIST_MORE_BUTTON)
		click_on_sub_menu_delete_item = xpath_click(driver, WISHLIST_SUB_MENU_DELETE)

		click_yes_in_modal_window = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)
		wait_wishlist_items = el_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)

		time.sleep(2) # obligatory wait to see refreshed grid

		read_all_wishlist_names = [i.text for i in elems_xpath(driver, PROFILE_FIRST_ITEM_IN_WISHLIST_GRID)]
		assert RANDOM_EDITED_WISHLIST_NAME not in read_all_wishlist_names
