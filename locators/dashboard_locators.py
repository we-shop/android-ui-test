from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR DASHBOARD PAGE MODEL
DASHBOARD_WESHARES_TAB = "WeShares"
DASHBOARD_TRANSACTIONS_TAB = "Transactions"
DASHBOARD_WENEWS_TAB = "WeNews"
DASHBOARD_REFER_N_EARN_TAB = "Refer & Earn"
PRE_LOADER = "com.socialsuperstore:id/progressPanel"

# WESHARES TAB
DASH_WESHARES_EMPTY_STUB_IMG = "com.socialsuperstore:id/emptyImage"
DASH_WESHARES_EMPTY_STUB_TITLE = "com.socialsuperstore:id/emptyTitle"
DASH_WESHARES_EMPTY_STUB_TEXT = "com.socialsuperstore:id/emptyBody"
DASH_WESHARES_BOTTOM_HINT = "com.socialsuperstore:id/bottomHint"

DASH_WESHARES_SUPPORT_LINK = "com.socialsuperstore:id/supportHint"
DASH_WESHARES_LAST_UPDATED = "com.socialsuperstore:id/lastUpdated"
DASH_WESHARES_SHARE_PRICE = "com.socialsuperstore:id/sharePrice"
DASH_WESHARES_YOUR_WESHARE_TOP = "com.socialsuperstore:id/capitalization" 
DASH_WESHARES_YOUR_WESHARE_BOTTOM = "com.socialsuperstore:id/shareCount" #"com.socialsuperstore:id/yourWeshares"
DASH_WESHARES_CHART = "com.socialsuperstore:id/chart"
DASH_WESHARES_BOTTOM_HINT_CLOSE_BTN = "com.socialsuperstore:id/bottomHintCloseIcon"


# TRANSACTIONS TAB
DASH_TRANS_EMPTY_PURCHASES_STUB = "com.socialsuperstore:id/purchasesEmpty"
DASH_TRANS_EMPTY_INFLUENCE_SALES_STUB = "com.socialsuperstore:id/influencedEmpty"
DASH_TRANS_EMPTY_REFERRALS_STUB = "com.socialsuperstore:id/referralsEmpty"
DASH_TRANS_EMPTY_SHARE_BTN = "com.socialsuperstore:id/shareBtn"
DASH_TRANS_SHOW_MORE_PURCHASES = "com.socialsuperstore:id/youPurchasesLoadMore"
DASH_TRANS_SHOW_MORE_PRODUCT_TITLE = "com.socialsuperstore:id/dashboardTransactionTitle"
DASH_TRANS_SHOW_MORE_REFFERALS_USERNAME = "com.socialsuperstore:id/dashboardTransactionDescription"
DASH_TRANS_SHOW_MORE_PRICE = "com.socialsuperstore:id/dashboardTransactionPrice"
DASH_TRANS_SHOW_MORE_SALES = "com.socialsuperstore:id/influencedSalesLoadMore"
DASH_TRANS_SHOW_MORE_REFERRALS = "com.socialsuperstore:id/friendsReferredLoadMore"
DASH_TRANS_SHOW_MORE_REFERRALS_HEADER = "com.socialsuperstore:id/referralsHeader"
DASH_TRANS_SHOW_MORE_REFERRALS_NICK_INPUT = "//*[contains(@resource-id, 'linkInput')]//android.widget.FrameLayout/android.widget.EditText" # "//*[contains(@resource-id, 'linkInput')]//android.widget.EditText"  

# WENEWS TAB
DASH_WENEWS_READ_MORE_BTN = "com.socialsuperstore:id/newsReadMore"
DASH_WENEWS_POST_TITLE = "com.socialsuperstore:id/newsTitle"
DASH_WENEWS_READ_MORE_POST_TITLE = "//androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView[1]" #"//android.view.View/android.view.View/android.widget.TextView[1]"

# REFFER&EARN TAB
DASH_REFER_N_EARN_SHARE_USRN_BTN = "com.socialsuperstore:id/weReferEarnButton"
DASH_REFER_N_EARN_TERMS_LINK = "com.socialsuperstore:id/weReferEarnTerms"