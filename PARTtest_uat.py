import pytest
import os

# # LIST OF TESTS
	#done
def test_login_and_logout(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_with_assert(selenium)
	login_model.logout(selenium)

	#done
def test_login_with_incorrect_credentials(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_with_incorrect_creds(selenium)


	# done
def test_search_request_and_clear_field(login_model, debug_model, search_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_and_clear_field(selenium)

	# done 1
def test_add_and_remove_product_from_wishlist(login_model, debug_model, search_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_product_and_open_detail_page(selenium)
	product_page_model.add_product_to_wishlist(selenium)

	# done 1
def test_add_product_to_wishlist_and_check_in_profile(login_model, debug_model, search_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_product_and_open_detail_page(selenium)
	product_page_model.add_product_to_wishlist_and_check_in_profile(selenium)

	# done
def test_open_product_website(debug_model, login_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	product_page_model.open_product_website(selenium)

	# done
def test_add_product_to_post(debug_model, login_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	product_page_model.add_product_to_post(selenium)

	# done
def test_add_product_to_question(debug_model, login_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	product_page_model.add_product_to_question(selenium)

	# done
def test_profile_check_followers_and_followings_count(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.followings_followers_count(selenium)

	# done
def test_profile_follow_unfollow_followers_following_tabs(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.following_count_manipulations_in_profile(selenium)

	# done
def test_profile_follow_few_users_using_search(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.follow_few_users(selenium)


	# done
def test_profile_info_edit(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.edit_profile(selenium)

def QQQtest_profile_deactivate_account_flow(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.deactivate_account_and_login_after(selenium)

	# done 1 bug
@pytest.mark.xfail #marked as should fail, because of bug
def test_profile_info_pages(login_model, debug_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.info_pages_check(selenium)
	profile_model.customer_support_page_check(selenium)

	# done
def test_profile_about_version_check(debug_model, profile_model, selenium):
	debug_model.switch_to_uat_version_check(selenium)
	profile_model.about_version_check(selenium)

	# done 1
def test_post_create_new_product(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.recommend_product(selenium)

	# Done | need to re-debug few times, for sure
def test_post_create_new_product_edit_delete(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.recommend_product(selenium)
	post_model.product_edit_and_deletion(selenium)

	# done 1
def test_self_post_like_and_comment_check(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	post_model.comment_and_like_self_post(selenium)

	# done 1
def test_self_post_comment_edit_and_delete(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.recommend_product(selenium)
	post_model.comment_edit_and_delete_in_self_post(selenium)

def OLDtest_self_post_comment_edit_and_delete_second(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.recommend_product(selenium)
	post_model.comment_edit_and_delete_in_self_post_second(selenium)

	# done
def test_post_create_new_question(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.ask_question(selenium)

def QQQtest_post_create_new_question_edit_delete(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.ask_question(selenium)
	post_model.question_edit_and_deletion(selenium)

	# done | need to add like STATE (NEED TO DISCUSS WITH DANILO)
def test_self_question_like_and_comment_check(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	post_model.comment_and_like_self_question(selenium)

def QQQtest_self_question_comment_edit_and_delete(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.ask_question(selenium)
	post_model.comment_edit_and_delete_in_self_question(selenium)

def OLDtest_self_question_comment_edit_and_delete_second(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	post_model.ask_question(selenium)
	post_model.comment_edit_and_delete_in_self_question_second(selenium)

	# done
def test_inbox_check(debug_model, login_model, inbox_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	inbox_model.inbox_check(selenium)

	# done
def test_inbox_redirect_to_post_and_question_check(debug_model, login_model, inbox_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	inbox_model.inbox_post_and_question_redirects(selenium)

	# done
def test_dashboard_new_account_check(debug_model, login_model, dashboard_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only_new_acc(selenium)
	dashboard_model.new_acc_check(selenium)

	# done | NEED to fix scroll bug
def test_dashboard_existing_account_check(debug_model, login_model, dashboard_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	dashboard_model.existing_acc_check(selenium)

def OLDtest_dashboard_wenews_check(debug_model, login_model, dashboard_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	dashboard_model.wenews_check(selenium)

	# done
def test_walkthough_other_user_posts_and_questions(debug_model, login_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only_new_acc(selenium)
	profile_model.other_user_posts_n_questions(selenium)

# done
def test_like_and_comment_wishlist(debug_model, login_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.wishlist_likes_and_comments(selenium)

	# Done
def test_share_profile_post_and_product(debug_model, login_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.share_profile_post_and_product(selenium)

	# Not done
def Atest_search_products_and_check_terms_and_description(login_model, debug_model, search_model, product_page_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_specific_product_and_open_detail_page(selenium)
	product_page_model.open_description_and_terms(selenium)

	# done
def test_wishlist_create_read_update_delete(debug_model, login_model, profile_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	profile_model.wishlist_crud(selenium)

	# done
def test_home_feed_carousel(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_go_to_profile(selenium)
	post_model.home_feed_carousel(selenium)

	# done
def test_flag_post_content(debug_model, login_model, post_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only_new_acc(selenium)
	post_model.flag_post_content(selenium)

