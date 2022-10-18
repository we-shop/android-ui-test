import pytest
import os
import multiprocessing


# LIST OF TESTS
def test_login_and_logout(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	print(multiprocessing.cpu_count())
	login_model.login_with_assert(selenium)
	login_model.logout(selenium)

def atest_login_with_incorrect_credentials(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_with_incorrect_creds(selenium)

def atest_search_request_and_clear_field(login_model, debug_model, search_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_and_clear_field(selenium)

def atest_add_and_remove_product_from_wishlist(login_model, debug_model, search_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_product_and_open_detail_page(selenium)
	product_page_model.add_product_to_wishlist(selenium)

