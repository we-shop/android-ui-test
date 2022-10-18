from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.debug_locators import *
from locators.login_locators import *

class DebugPage:
	def switch_to_uat(self, driver):
		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_uat_click = xpath_click(driver, UAT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		#assert toast_msg_env_config == "Webapp configuration switched to uat"

		#change_api_to_uat_click = xpath_click(driver, UAT_API_RADIO_BTN)
		#toast_msg_api_config = get_toast_msg(driver)
		
		# asserting toast api config message
		#assert toast_msg_api_config == "API configuration switched to uat"
		assert toast_msg_env_config == "API configuration switched to uat"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)
		create_temp_file_and_write_data("uat")


	def switch_to_int(self, driver):
		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_int_click = xpath_click(driver, INT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		assert toast_msg_env_config == "Webapp configuration switched to int"

		change_api_to_int_click = xpath_click(driver, INT_API_RADIO_BTN)
		toast_msg_api_config = get_toast_msg(driver)

		# asserting toast api config message
		assert toast_msg_api_config == "API configuration switched to int"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)
		create_temp_file_and_write_data("int")

	def switch_to_uat_version_check(self, driver):
		# read version
		read_app_version = el_id(driver, APP_VERSION_LOGIN_SCREEN).text

		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_uat_click = xpath_click(driver, UAT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		#assert toast_msg_env_config == "Webapp configuration switched to uat"

		#change_api_to_int_click = xpath_click(driver, UAT_API_RADIO_BTN)
		#toast_msg_api_config = get_toast_msg(driver)

		# asserting toast api config message
		#assert toast_msg_api_config == "API configuration switched to uat"
		assert toast_msg_env_config == "API configuration switched to uat"


		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)
		create_temp_file_and_write_data("uat")
		update_temp_file(read_app_version)

	def switch_to_int_version_check(self, driver):
		# read version
		read_app_version = el_id(driver, APP_VERSION_LOGIN_SCREEN).text

		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_int_click = xpath_click(driver, INT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		assert toast_msg_env_config == "Webapp configuration switched to int"

		change_api_to_int_click = xpath_click(driver, INT_API_RADIO_BTN)
		toast_msg_api_config = get_toast_msg(driver)

		# asserting toast api config message
		assert toast_msg_api_config == "API configuration switched to int"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)
		create_temp_file_and_write_data("int")
		update_temp_file(read_app_version)
