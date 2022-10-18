from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR LOGIN PAGE MODEL
ALREADY_HAVE_ACC_LINK = "com.socialsuperstore:id/signInBtn"
LOG_FIELD = "com.socialsuperstore.feature_native_auth:id/loginEditText"
PASS_FIELD = "com.socialsuperstore.feature_native_auth:id/passwordEditText"
SIGN_IN_BTN = "com.socialsuperstore.feature_native_auth:id/continueButton"
PROFILE_FOOTER_MENU = "Profile"
SETTINGS_BTN_PROFILE = "com.socialsuperstore:id/settings" # old: com.socialsuperstore:id/settingsBtn
PROFILE_FIRST_N_LAST_NAMES = "com.socialsuperstore:id/nameTextView"
PROFILE_USERNAME = "com.socialsuperstore:id/usernameTextView"

SIGN_OUT_BTN = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[3]/android.view.ViewGroup[2]/android.widget.TextView"
ACCEPT_MODAL_BTN_LOGOUT = "com.socialsuperstore:id/positiveButton"
LOGIN_SCREEN_TITLE = "com.socialsuperstore:id/body"
APP_VERSION_LOGIN_SCREEN = "com.socialsuperstore:id/version"
CLOSE_BTN_LOGIN = "com.socialsuperstore:id/discoverCloseBtn"