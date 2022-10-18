from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR SEARCH PAGE MODEL
WISHLIST_STAR_BUTTON = "com.socialsuperstore.feature_product_detail:id/saveToWishlistBtn"
ADD_BUTTON_IN_WISHLIST = "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.Button"
BACK_BTN = "Navigate up"
PRODUCT_NAME_TITLE =  "com.socialsuperstore.feature_product_detail:id/productName" #"com.socialsuperstore:id/toolbarText"
POST_HEAD_TITLE_YOUR_PRODUCT = '//*[contains(@resource-id, "com.socialsuperstore:id/toolbar")]/android.widget.TextView'
PRODUCT_NAME_PRICE_BLOCK = "com.socialsuperstore.feature_product_detail:id/productName"
PRODUCT_NAME_POST_CREATION = "com.socialsuperstore.feature_post_editor:id/name"
PRODUCT_NAME_PRODUCTS_TAB_FILLED_IMAGE = "//*[contains(@resource-id, 'com.socialsuperstore.feature_post_editor:id/productImage')]"

PRODUCT_PAGE_SUB_MENU = "com.socialsuperstore.feature_product_detail:id/moreActionsBtn"
PROFILE_FOOTER_ITEM = "com.socialsuperstore:id/action_profile"
WISHLIST_PROFILE_CLICK = "Wishlists"
WISHLIST_FIRST_ITEM_TITLE = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[2]"
WISHLIST_ITEMS_TITLE_LIST = "//*[contains(@resource-id, 'com.socialsuperstore:id/titleText')]" #"//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"
LIST_OF_ITEMS_INSIDE_WISHLIST = "//*[contains(@resource-id, 'com.socialsuperstore:id/productTitle')]"
NAME_OF_WISHLIST_PRODUCT_PAGE = "com.socialsuperstore:id/productTitle" #"com.socialsuperstore:id/titleTextView"
PROGRESS_BAR_WISHLIST = "com.socialsuperstore:id/progress"
BUY_NOW_BTN = "com.socialsuperstore.feature_product_detail:id/stickyBuyBtn"
FOOTER_PRODUCT_PRICE = "com.socialsuperstore.feature_product_detail:id/stickyPrice"
FOOTER_PRODUCT_RETAILER = "com.socialsuperstore.feature_product_detail:id/stickyRetailer"
FEED_PRODUCT_TITLE = "com.socialsuperstore:id/productTitle"


DESCRIPTION_TAB = "Description"
TERMS_TAB = "Terms"
DESCRIPTION_TEXT = "com.socialsuperstore.feature_product_detail:id/descriptionPlainTextView"
TERMS_TEXT = "//androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/androidx.viewpager.widget.ViewPager[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.TextView" #"com.socialsuperstore:id/recycler" #"com.socialsuperstore:id/term"

# "Taking you to" window locators
PRODUCT_MODAL_READ_TERMS_BTN = "com.socialsuperstore:id/readTermsButton"
PRODUCT_MODAL_CONTINUE_BTN = "com.socialsuperstore:id/continueButton"
PRODUCT_MODAL_TITLE_TEXT = "com.socialsuperstore:id/titleText"
TERMS_TEXT_IN_WINDOW = "//androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView" # //androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.TextView

# Wishlist add/remove btn debug XPATH, can be removed in future
#//*[contains(@resource-id, 'com.socialsuperstore:id/saveButton')]//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.Button
#/android.widget.TextView[1]
#/android.widget.Button
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.Button