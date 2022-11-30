from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.post_locators import *
from locators.profile_locators import *
from locators.product_detail_locators import *
from appium.webdriver.extensions.android.nativekey import AndroidKey


from appium.webdriver.common.touch_action import TouchAction

class PostPage:
	def recommend_product(self, driver):
		# generating random id for product title/caption
		PRODUCT_ID = str(random.randint(1000, 10000000))

		# product creation step 1 (search)
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		plus_button_click = xpath_click(driver, PLUS_BUTTON)
		click_on_footer_new_post_btn = id_click(driver, REC_PRODUCT_PLUS_MENU)
		add_first_product_click = xpath_click(driver, ADD_FIRST_PRODUCT_PLUS_INPUT)
		search_product_for_post = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Samsung")
		driver.keyevent(66) # additional execution: send_enter_key_adb(driver)
		fill_radio_btn_product_one = xpath_click(driver, SEARCH_RESULT_PRODUCT_ONE)
		fill_radio_btn_product_two = xpath_click(driver, SEARCH_RESULT_PRODUCT_TWO)
		fill_radio_btn_product_three = xpath_click(driver, SEARCH_RESULT_PRODUCT_THREE)
		done_btn_search_product_result_click = id_click(driver, STEP_BTN_ADD_PRODUCT)
		acc_id_click(driver, PRODUCT_ADD_FOOTER_ITEM_MEDIA)

		# media step
		click_use_product_image = id_click(driver, MEDIA_IMAGE_FROM_PRODUCT)
		next_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# caption step and publish
		enter_text_to_caption_input_field = id_keys(driver, CAPTION_INPUT_FIELD, f"Test caption for new product number {PRODUCT_ID}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# check if product created (checking title/caption in feed)
		wait_element = el_id(driver, POST_TIME_AGO_TEXT)
		scroll_on_feed_page(driver)
		#get_correct_text_by_id(driver, FEED_POST_DESCRIPTION, PRODUCT_ID)

	def product_edit_and_deletion(self, driver):
		# starting from opened feed
		read_post_title = el_id(driver, FEED_POST_DESCRIPTION).text.split(" ")[-1]
		read_count_of_linear_carousel_items = len(elems_xpath(driver, READ_ALL_PRODUCT_LINEAR_LAYOUTS))

		scroll_up_on_feed_page(driver)
		scroll_up_on_feed_page(driver)
		open_sub_menu_of_post = id_click(driver, POST_DOTS_SUB_MENU)
		edit_post_sub_menu_click = elems_id(driver, POST_SUB_MENU_ACTION_ITEMS_ID)[0].click()

		# edit post part
		remove_selection_first_product = xpath_click(driver, PRODUCT_EDIT_FIRST_CHECKBOX)
		click_on_next_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)
		click_on_next_btn_again = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# final step
		caption_input_edit = id_keys(driver, CAPTION_INPUT_FIELD, f"edited {read_post_title}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# verify post data after edit
		wait_element = el_id(driver, POST_TIME_AGO_TEXT)
		scroll_on_feed_page(driver)
		re_read_count_of_linear_carousel_items = len(elems_xpath(driver, READ_ALL_PRODUCT_LINEAR_LAYOUTS))
		re_read_post_title = el_id(driver, FEED_POST_DESCRIPTION).text

		#print(read_count_of_linear_carousel_items)
		#print(re_read_count_of_linear_carousel_items)

		assert re_read_count_of_linear_carousel_items == read_count_of_linear_carousel_items - 1
		assert re_read_post_title == f"edited {read_post_title}"

		# delete part
		scroll_up_on_feed_page(driver)
		scroll_up_on_feed_page(driver)
		re_open_sub_menu_of_post = id_click(driver, POST_DOTS_SUB_MENU)
		delete_post_sub_menu_click = elems_id(driver, POST_SUB_MENU_ACTION_ITEMS_ID)[1].click()
		accept_deletion_in_modal = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)

		# verify that post was deleted
		read_toast_msg = get_toast_msg(driver)
		scroll_on_feed_page(driver)
		re_re_read_post_title = el_id(driver, FEED_POST_DESCRIPTION).text

		assert read_toast_msg == "Your post has been deleted"
		assert re_re_read_post_title != f"edited {read_post_title}"


	def ask_question(self, driver):
		# generating random id for question title
		QUESTION_ID = str(random.randint(1000, 10000000))

		# question creation step 1 (question title)
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		plus_button_click = xpath_click(driver, PLUS_BUTTON)
		click_on_footer_new_question_btn = id_click(driver, ASK_QUESTION_PLUS_MENU)
		fill_question_text = id_keys(driver, QUESTION_TEXT_STEP_ONE, f"Test question number {QUESTION_ID}")
		click_next_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 2
		bread_crumbs_text_step_2 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_2 == "2"

		# question creation step 2 (customize background)
		popular_designs_click = id_click(driver, QUESTION_UPLOAD_FROM_DESIGNS)
		all_backgrounds = elems_xpath(driver, CUSTOM_BACKGROUND_ITEMS)
		random_background_click = all_backgrounds[random.randint(0, 5)].click()
		save_btn_background_lst_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		all_texts = elems_xpath(driver, ALL_TEXT_STYLES)
		random_text_style_click = all_texts[random.randint(0, 5)].click()
		switch_to_text_colour_tab = acc_id_click(driver, BACKGROUND_TEXT_COLOUR_TAB)
		all_text_clrs = elems_xpath(driver, ALL_TEXT_COLOURS)
		random_clrs_click = all_text_clrs[random.randint(0, 8)].click()

		done_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)
		next_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 3
		bread_crumbs_text_step_3 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_3 == "3"
	
		# question creation step 3 (add product)
		click_in_srch_field = id_click(driver, SEARCH_PRODUCT_POST_CREATION) # probably temporary step, because of bug
		search_product_for_question = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Xiaomi")
		driver.keyevent(66) # additional execution: send_enter_key_adb(driver)
		fill_radio_btn_product_one = xpath_click(driver, SEARCH_RESULT_PRODUCT_ONE)
		fill_radio_btn_product_two = xpath_click(driver, SEARCH_RESULT_PRODUCT_TWO)
		fill_radio_btn_product_three = xpath_click(driver, SEARCH_RESULT_PRODUCT_THREE)
		click_done_step_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)
		next_btn_step_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 4
		bread_crumbs_text_step_4 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_4 == "4"

		# question creation step 4 (add caption and publish)
		enter_text_to_caption_input_field = id_keys(driver, CAPTION_INPUT_FIELD, f"Test caption for question number {QUESTION_ID}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# check if question created (checking title/caption in feed)
		wait_element = el_id(driver, POST_TIME_AGO_TEXT)
		#scroll_on_feed_page(driver)
		scroll_on_feed_page_more(driver)
		get_correct_text_by_id(driver, FEED_POST_DESCRIPTION, QUESTION_ID)

	def question_edit_and_deletion(self, driver):
		# starting from opened feed
		print("Started 00")
		read_question_title = el_id(driver, FEED_POST_DESCRIPTION).text.split(" ")[-1]
		read_count_of_linear_carousel_items = len(elems_xpath(driver, READ_ALL_PRODUCT_LINEAR_LAYOUTS))

		#scroll_up_on_feed_page(driver)
		scroll_up_on_feed_page(driver)

		## not obligatory
		#elem_sub_menu_of_question = el_id(driver, POST_DOTS_SUB_MENU)
		#scroll_into_view(elem_sub_menu_of_question, driver)
		#move_to_element(elem_sub_menu_of_question, driver)
		
		open_sub_menu_of_question = id_click(driver, POST_DOTS_SUB_MENU)
		edit_question_sub_menu_click = elems_id(driver, POST_SUB_MENU_ACTION_ITEMS_ID)[0].click()

		# edit question part
		edit_question_banner_text = id_keys(driver, QUESTION_TEXT_STEP_ONE, f"Edited question {read_question_title}")
		click_on_next_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# verify that edited text visible on next step
		get_edited_question_banner_text = el_id(driver, QUESTION_TEXT_MEDIA_TAB).text
		assert get_edited_question_banner_text == f"Edited question {read_question_title}"
		click_on_next_btn_again = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# next step
		remove_selection_first_product = xpath_click(driver, PRODUCT_EDIT_FIRST_CHECKBOX)
		click_step_further = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# next step
		caption_input_edit = id_keys(driver, CAPTION_INPUT_FIELD, f"edited {read_question_title}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# verify question data after edit
		wait_for_plust_button = el_xpath(driver, PLUS_BUTTON)
		#time.sleep(1)
		scroll_up_on_feed_page(driver)
		scroll_on_feed_page_more(driver)
		#scroll_on_feed_page(driver)
		#scroll_on_feed_page(driver)
		#time.sleep(1)
		print("Passed 1")
		re_read_count_of_linear_carousel_items = len(elems_xpath(driver, READ_ALL_PRODUCT_LINEAR_LAYOUTS))
		re_read_question_title = el_id(driver, FEED_POST_DESCRIPTION).text

		print(read_count_of_linear_carousel_items)
		print(re_read_count_of_linear_carousel_items)
		assert re_read_count_of_linear_carousel_items == read_count_of_linear_carousel_items - 1
		assert re_read_question_title == f"edited {read_question_title}"

		# delete part
		scroll_up_on_feed_page(driver)
		scroll_up_on_feed_page(driver)
		print("Passed 2")
		re_open_sub_menu_of_question = id_click(driver, POST_DOTS_SUB_MENU)
		delete_post_sub_menu_click = elems_id(driver, POST_SUB_MENU_ACTION_ITEMS_ID)[1].click()
		accept_deletion_in_modal = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)

		# verify that question was deleted
		#go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE) # refresh purpose
		#go_to_feed = acc_id_click(driver, FOOTER_ITEM_HOME) # refresh purpose

		read_toast_msg = get_toast_msg(driver)
		# new scroll here
		#scroll_on_feed_page(driver)
		#scroll_on_feed_page(driver)
		scroll_on_feed_page_more(driver)
		
		re_re_read_question_title = el_id(driver, FEED_POST_DESCRIPTION).text

		assert read_toast_msg == "Your post has been deleted"
		assert re_re_read_question_title != f"edited {read_question_title}"
		

	def comment_and_like_self_post(self, driver):
		# manipulation with likes
		click_on_first_posts_in_profile = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)

		# checking likes real count (cover case, when like already clicked)
		read_likes_count = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		click_on_like_btn = id_click(driver, LIKES_IN_POST)
		time.sleep(0.5)
		read_likes_count_2 = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])


		already_clicked = None

		if read_likes_count_2 > read_likes_count:
			read_likes_count_final = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		else:
			click_on_like_btn_again = id_click(driver, LIKES_IN_POST)
			time.sleep(0.5)
			read_likes_count_final = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
			already_clicked = True

		if already_clicked:
			assert read_likes_count_final == read_likes_count
		else:
			read_likes_count_final == read_likes_count +1

		# manipulation with comments
		# check if comment exist
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		click_on_comments_btn = id_click(driver, GO_TO_COMMENTS_BTN)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for post")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		driver.back()
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1

	def comment_edit_and_delete_in_self_post(self, driver):
		# generating random id for question title
		EDITED_COMMENT = "Edited comment " + str(random.randint(1000, 10000000))

		# go to profile
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		el_xpath_short_wait(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)
		click_on_first_posts_in_profile = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)

		# manipulation with comments
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])
			print(read_comments_count)
			print(f"{EXISTING_COMMENTS_IN_NEW_POST}")

		click_on_comments_btn = id_click(driver, GO_TO_COMMENTS_BTN)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for post")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		
		driver.back()
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1, pytest.fail("Wrong comments count!")

		# re-enter to comments, then edit
		click_on_comments_btn_edit_flow = id_click(driver, GO_TO_COMMENTS_BTN)
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_edit_comment_btn = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		edit_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, EDITED_COMMENT)
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window

		read_edited_comment_text = el_id(driver, COMMENT_TEXT_ID).text
		assert read_edited_comment_text == EDITED_COMMENT

		# delete comment block
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_delete_comment_btn = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)

		# asserting that stub "Be the first to comment" is displayed
		read_no_comments_stub = el_id(driver, NO_COMMENTS_STUB).text
		assert "Be the first to comment on" in read_no_comments_stub

		# checking comments count again (after deletion)
		driver.back()
		re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_read_comments_count_after_deletion = 0
		else:
			re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count_after_deletion == re_read_comments_count - 1


	def comment_edit_and_delete_in_self_post_second(self, driver):
		# generating random id for question title
		EDITED_COMMENT = "Edited comment " + str(random.randint(1000, 10000000))

		# go to profile
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		el_xpath_short_wait(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)
		click_on_first_posts_in_profile = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)

		# manipulation with comments
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])
			#print(read_comments_count)
			#print(f"{EXISTING_COMMENTS_IN_NEW_POST}")

		click_on_comments_btn = id_click(driver, GO_TO_COMMENTS_BTN)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for post")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		
		scroll_down_slowly(driver)
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1, pytest.fail("Wrong comments count!")

		# re-enter to comments, then edit
		#click_on_comments_btn_edit_flow = id_click(driver, COMMENTS_IN_POST)
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_edit_comment_btn = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		edit_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, EDITED_COMMENT)
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window

		scroll_down_slowly(driver)
		read_edited_comment_text = el_id(driver, COMMENT_TEXT_ID).text
		assert read_edited_comment_text == EDITED_COMMENT

		# delete comment block
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_delete_comment_btn = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		scroll_down_slowly(driver)

		# asserting that stub "Be the first to comment" is displayed
		read_no_comments_stub = el_id(driver, NO_COMMENTS_STUB).text
		assert "Be the first to comment on" in read_no_comments_stub

		# check count of comments right after deletion (comments page)
		re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_read_comments_count_after_deletion = 0
		else:
			re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count_after_deletion == re_read_comments_count - 1

		# checking comments count again (after deletion)
		driver.back()
		re_re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_re_read_comments_count_after_deletion = 0
		else:
			re_re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_re_read_comments_count_after_deletion == re_read_comments_count - 1


	def comment_and_like_self_question(self, driver):
		switching_to_question_tab = acc_id_click(driver, PROFILE_QUESTIONS_TAB)
		# manipulation with likes
		click_on_first_question_in_profile = xpath_click(driver, FIRST_QUESTION_IN_QUEST_TAB)

		# checking likes real count (cover case, when like already clicked)
		read_likes_count = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		click_on_like_btn = id_click(driver, LIKES_IN_POST)
		time.sleep(0.5)
		read_likes_count_2 = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])


		already_clicked = None

		if read_likes_count_2 > read_likes_count:
			read_likes_count_final = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
		else:
			click_on_like_btn_again = id_click(driver, LIKES_IN_POST)
			time.sleep(0.5)
			read_likes_count_final = int(el_id(driver, LIKES_IN_POST).text.split(" ")[0])
			already_clicked = True

		if already_clicked:
			assert read_likes_count_final == read_likes_count
		else:
			read_likes_count_final == read_likes_count + 1

		# manipulation with comments
		# check if comment exist
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		click_on_comments_btn = id_click(driver, COMMENTS_IN_POST)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for question")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		
		# handle modal window
		click_continue_without_product = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)

		# continue comment check section
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		driver.back()
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1


	def comment_edit_and_delete_in_self_question(self, driver):
		# generating random id for question title
		EDITED_COMMENT = "Edited comment " + str(random.randint(1000, 10000000))

		# go to profile
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		click_on_question_tab = acc_id_click(driver, PROFILE_QUESTIONS_TAB) 
		el_xpath_short_wait(driver, FIRST_QUESTION_IN_QUEST_TAB)
		click_on_first_question_in_profile = xpath_click(driver, FIRST_QUESTION_IN_QUEST_TAB)

		# manipulation with comments
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])
			print(read_comments_count)
			print(f"{EXISTING_COMMENTS_IN_NEW_QUESTION}")

		click_on_comments_btn = id_click(driver, GO_TO_COMMENTS_BTN)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for question")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		
		# handle modal window
		click_continue_without_product = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window

		# check comments count after creation
		driver.back()
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1, pytest.fail("Wrong comments count!")

		# re-enter to comments, then edit
		click_on_comments_btn_edit_flow = id_click(driver, GO_TO_COMMENTS_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window

		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_edit_comment_btn = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		edit_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, EDITED_COMMENT)
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window

		read_edited_comment_text = el_id(driver, COMMENT_TEXT_ID).text

		assert read_edited_comment_text == EDITED_COMMENT

		# delete comment block
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_delete_comment_btn = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)

		# asserting that stub "Be the first to comment" is displayed
		read_no_comments_stub = el_id(driver, NO_COMMENTS_STUB).text
		assert "Be the first to comment on" in read_no_comments_stub

		# checking comments count again (after deletion)
		driver.back()
		re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_read_comments_count_after_deletion = 0
		else:
			re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count_after_deletion == re_read_comments_count - 1

	def comment_edit_and_delete_in_self_question_second(self, driver):
		# generating random id for question title
		EDITED_COMMENT = "Edited comment " + str(random.randint(1000, 10000000))

		# go to profile
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		click_on_question_tab = acc_id_click(driver, PROFILE_QUESTIONS_TAB) 
		el_xpath_short_wait(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)
		click_on_first_question_in_profile = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POSTS_TAB)

		# manipulation with comments
		read_comments_count = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			read_comments_count = 0
		else:
			read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])
			#print(read_comments_count)
			#print(f"{EXISTING_COMMENTS_IN_NEW_QUESTION}")

		click_on_comments_btn = id_click(driver, GO_TO_COMMENTS_BTN)
		type_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, "self test comment for question")
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		
		# handle modal window
		click_continue_without_product = id_click(driver, CONTINUE_WITHOUT_PRODUCT_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		scroll_down_slowly(driver)

		# check comments count after creation
		re_read_comments_count = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count == read_comments_count + 1, pytest.fail("Wrong comments count!")

		# re-enter to comments, then edit
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_edit_comment_btn = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		edit_test_comment = id_keys(driver, COMMENTS_INPUT_TEXT_FIELD, EDITED_COMMENT)
		click_on_send_comments_btn = id_click(driver, COMMENTS_SEND_BTN)
		time.sleep(1.1) # obligatory wait to avoid warning modal window
		scroll_down_slowly(driver)

		read_edited_comment_text = el_id(driver, COMMENT_TEXT_ID).text

		assert read_edited_comment_text == EDITED_COMMENT

		# delete comment block
		long_click_id(driver, COMMENT_TEXT_ID)
		click_on_delete_comment_btn = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		scroll_down_slowly(driver)

		# asserting that stub "Be the first to comment" is displayed
		read_no_comments_stub = el_id(driver, NO_COMMENTS_STUB).text
		assert "Be the first to comment on" in read_no_comments_stub

		# check count of comments right after deletion (comments page)
		re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_read_comments_count_after_deletion = 0
		else:
			re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_read_comments_count_after_deletion == re_read_comments_count - 1

		# checking comments count again (after deletion)
		driver.back()
		re_re_read_comments_count_after_deletion = None

		if el_id(driver, COMMENTS_IN_POST).text == "Add a comment":
			re_re_read_comments_count_after_deletion = 0
		else:
			re_re_read_comments_count_after_deletion = int(el_id(driver, COMMENTS_IN_POST).text.split(" ")[0])

		assert re_re_read_comments_count_after_deletion == re_read_comments_count - 1		


	def home_feed_carousel(self, driver):
		current_env = read_data_from_temp_file()[0]

		# go to feed
		go_to_feed = acc_id_click(driver, FOOTER_ITEM_HOME)

		# manipulation with carousel
		is_carousel = True

		# carousel checks
		### scroll_on_feed_page(driver)
		#time.sleep(2)
		el_xpath(driver, FEED_SLIDE_HEADLINE)
		time.sleep(0.3)
		scope_carousel_before_swipe = [i.text for i in elems_xpath(driver, FEED_SLIDE_HEADLINE)]
		read_text_in_first_carousel_item = el_xpath(driver, FEED_SLIDE_HEADLINE).text
		assert len(read_text_in_first_carousel_item) > 5

		horisontal_carousel_swipe(driver)

		scope_carousel_after_swipe = [b.text for b in elems_xpath(driver, FEED_SLIDE_HEADLINE)]


		assert scope_carousel_before_swipe != scope_carousel_after_swipe # items in carousel is different, because of swipe 
		assert scope_carousel_before_swipe[1] == scope_carousel_after_swipe[0] # after scroll 1 item will have intersection

		#print(scope_carousel_before_swipe)
		#print(scope_carousel_after_swipe)


		# Temprorary commented, because of varios combinations of functionality
		# this test part was replaced with above block, but probably in future in will be uncommented and re-worked
		# while is_carousel:
		# 	try:
		# 		wait_carousel = el_xpath_short_wait_with_fail(driver, FEED_SLIDE_HEADLINE)
		# 		is_carousel = True
		# 	except:
		# 		is_carousel = False

		# 	if is_carousel:
		# 		read_text_in_first_carousel_item = el_xpath(driver, FEED_SLIDE_HEADLINE).text
		# 		assert len(read_text_in_first_carousel_item) > 5

		# 		# going to site and check URL
		# 		click_on_carousel_item = xpath_click(driver, FEED_SLIDE_HEADLINE)
		# 		select_chrome_browser(driver)
		# 		page_url_terms = el_id(driver, BROWSER_URL_BAR).text

		# 		assert current_env in page_url_terms
		# 		assert "search?query=" in page_url_terms
		# 		driver.back()

	def flag_post_content(self, driver):
		# can be implemented for main account
		go_to_profile = acc_id_click(driver, FOOTER_ITEM_PROFILE)
		get_first_and_last_name_profile = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text

		go_to_feed_page = acc_id_click(driver, FOOTER_ITEM_HOME)
		el_id(driver, POST_USERNAME) # wait purpose
		time.sleep(0.4)

		not_self_post = True

		while not_self_post:
			if get_first_and_last_name_profile not in el_id(driver, POST_USERNAME).text:
				not_self_post = False
			else:
				scroll_on_feed_page(driver)
				#time.sleep(0.6)
				#scroll_on_feed_page(driver)
				try:
					el_id(driver, POST_USERNAME)
				except:
					scroll_on_feed_page(driver)
					scroll_on_feed_page(driver)

		open_sub_menu_of_post = id_click(driver, POST_DOTS_SUB_MENU)
		select_flag_content = xpath_click(driver, POST_DOTS_SUB_MENU_EDIT_POST)
		wait_list_of_flags = el_id(driver, POST_DOTS_SUB_MENU_FLAG_CONTENT_ITEMS)
		read_all_flag_reasons = elems_id(driver, POST_DOTS_SUB_MENU_FLAG_CONTENT_ITEMS)
		#print([i.text for i in read_all_flag_reasons])
		select_random_flag_reason = read_all_flag_reasons[random.randint(0, len(read_all_flag_reasons))].click()
		read_success_message_title = el_id(driver, POST_FLAG_CONTENT_SUCCESS_WIN_TITLE).text

		assert read_success_message_title == "Thanks for letting us know"
		click_on_done_btn = id_click(driver, POST_FLAG_CONTENT_SUCCESS_WIN_DONE_BTN)
		
