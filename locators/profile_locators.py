from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR PROFILE PAGE MODEL
FOLLOWERS_COUNT = "com.socialsuperstore:id/profileFollowersCount"
FOLLOWINGS_COUNT = "com.socialsuperstore:id/profileFollowingCount"
FOLLOWERS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowersTitle"
FOLLOWINGS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowingTitle"
WISHLIST_LABEL_PROFILE = "com.socialsuperstore:id/profileWishlistsTitle"
PROFILE_FIRST_AND_LAST_NAME = "com.socialsuperstore:id/nameTextView"
PROFILE_USERNAME = "com.socialsuperstore:id/usernameTextView"
PROFILE_BIO = "com.socialsuperstore:id/userDescriptionTextView"
PROFILE_SETTINGS_BTN = "com.socialsuperstore:id/settings" # old: com.socialsuperstore:id/settingsBtn
PROFILE_SETTINGS_EDIT_BTN = "com.socialsuperstore.feature_settings:id/editProfileBtn"
FOOTER_ITEM_HOME = "Your feed"
FOOTER_ITEM_DASHBOARD = "Dashboard"
PLUS_BUTTON = "//android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton"
FOOTER_ITEM_NEW_POST = "New post"
FOOTER_ITEM_INBOX = "Inbox"
FOOTER_ITEM_PROFILE = "Profile"
FOOTER_ITEM_SEARCH = "Shop now"
PROFILE_POSTS_TAB = "Posts"
PROFILE_WISHLIST_TAB = "Wishlists"
SEARCH_BTN_HEAD_BAR = "com.socialsuperstore:id/searchInput" #"com.socialsuperstore:id/searchView" #"com.socialsuperstore:id/search"
ADD_NEW_WISHLIST_ITEM_PLUS_ICON = "com.socialsuperstore:id/plusIcon"
ADD_NEW_WISHLIST_INPUT_NAME = "com.socialsuperstore:id/wishlistTitleEditText"
ADD_NEW_WISHLIST_SAVE_BUTTON = "com.socialsuperstore:id/saveButton"
ADD_NEW_WISHLIST_MORE_BUTTON = "com.socialsuperstore:id/menuActionActions"
WISHLIST_SUB_MENU_DELETE = "(//*[contains(@resource-id, 'actionText')])[1]"
WISHLIST_SUB_MENU_EDIT = "(//*[contains(@resource-id, 'actionText')])[2]"
WISHLIST_SUB_MENU_CANCEL = "(//*[contains(@resource-id, 'actionText')])[3]"
WISHLIST_EDIT_NAME_INPUT = "com.socialsuperstore:id/collectionTitleEditText"
WISHLIST_EDIT_IS_PUBLIC_SWITCHER = "com.socialsuperstore:id/collectionPublicCheckBox"
WISHLIST_EDIT_SAVE_BUTTON = "com.socialsuperstore:id/submitButton"
WISHLIST_NAME_TOOLBAR_TEXT = "//*[contains(@resource-id, 'toolbar')]/android.widget.TextView"
WISHLIST_GRID_HIDE_ICON = "com.socialsuperstore:id/lockIcon"

PROFILE_SHARE_BUTTON = "com.socialsuperstore:id/shareButton"
PROFILE_POST_SHARE_BUTTON = "com.socialsuperstore:id/interactionsShareBtn"
PRODUCT_SHARE_BUTTON = "com.socialsuperstore:id/shareAction"
SHARE_WINDOW_COPY_BTN = "android:id/sem_chooser_chip_button1"
PROFILE_FIRST_ITEM_IN_POSTS_TAB = "(//*[contains(@resource-id, 'cardView')]//androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView)[1]"
PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT = "(//*[contains(@resource-id, 'cardView')]//androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView)[1]"
PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT_SPECIAL = "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[1]"
PROFILE_FIRST_ITEM_IN_WISHLIST_GRID = "//*[contains(@resource-id, 'titleText')]"
PROFILE_FIRST_ITEM_TEXT_INSIDE_WISHLIST = "//*[contains(@resource-id, 'toolbar')]/android.widget.TextView" #"com.socialsuperstore:id/productTitle" #"com.socialsuperstore:id/titleTextView"
NESTED_PRODUCTS_COUNT_IN_POST = "(//*[contains(@resource-id, 'postProductCount')])[1]"
POST_PRODUCT_TITLE = "com.socialsuperstore:id/productTitle"
PROFILE_QUESTIONS_TAB = "Questions"
FIRST_QUESTION_IN_QUEST_TAB = "//*[contains(@resource-id, 'cardView')]/android.view.ViewGroup"
PROFILE_FOLLOWERS_TAB_FOLLOWERS_TAB = "Followers"
PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB = "Following"
PROFILE_FOLLOWERS_TAB_ALL_ITEMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.CompoundButton"
PROFILE_EDIT_PHOTO_CHANGE_ICON = "com.socialsuperstore.feature_settings:id/changePhotoBtn" #"com.socialsuperstore.feature_settings:id/pickImageEmptyCamera"
PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO = "//androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]"
PROFILE_EDIT_PHOTO_CHANGE_PICK_PHOTO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[2]"
PROFILE_EDIT_FIRST_NAME_FIELD = "//*[contains(@resource-id, 'firstNameInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/firstNameInput"
PROFILE_EDIT_LAST_NAME_FIELD =  "//*[contains(@resource-id, 'lastNameInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/lastNameInput"
PROFILE_EDIT_BIO_FIELD = "//*[contains(@resource-id, 'bioInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/bioInput"
PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES = "//*[contains(@resource-id, 'checkbox')]"
PROFILE_EDIT_SAVE_CHANGES_BTN = "com.socialsuperstore.feature_settings:id/saveBtn" #"com.socialsuperstore.feature_settings:id/saveChangesButton"
PROFILE_SETTINGS_FULL_NAME_TEXT = "com.socialsuperstore.feature_settings:id/userFullNameTextView"
PROFILE_SETTINGS_USERNAME_TEXT = "com.socialsuperstore.feature_settings:id/userNickNameTextView"
BACK_BTN = "Navigate up"

# SETTINGS MENU ITEMS
SETTINGS_MANAGE_YOUR_CREDS = '//*[contains(@text, "Manage your credentials")]'
SETTINGS_NOTIFICATION_N_COMMUNICATION = '//*[contains(@text, "Notifications & communication")]'
SETTINGS_SOCIAL_CONNECT = '//*[contains(@text, "Connect your social media")]'

SETTINGS_LEGAL_N_TERMS = '//*[contains(@text, "Legal & terms")]'
SETTINGS_CUSTOMER_SUPPORT = '//*[contains(@text, "Customer support")]'
SETTINGS_BLOCKED_PEOPLE = '//*[contains(@text, "Blocked people")]'
SETTINGS_ABOUT = '//*[contains(@text, "About")]'
SETTINGS_DEBUG_INFO = '//*[contains(@text, "Debug information")]'

SETTINGS_DEACTIVATE_ACC = '//*[contains(@text, "Deactivate your account")]'
SETTINGS_SIGN_OUT = '//*[contains(@text, "Sign out")]'

# DEACTIVATE ACC
DEACTIVATE_ACCOUNT_BTN = "com.socialsuperstore.feature_settings:id/deactivateAccountButton"
DEACTIVATE_ACC_ACCEPT_IN_MODAL = "com.socialsuperstore:id/deactivateAccountButton"
ALREADY_HAVE_ACC_LOGIN_SCREEN = "com.socialsuperstore:id/signInBtn"
READ_WELCOME_TEXT_LOGIN_SCREEN = "com.socialsuperstore.feature_native_auth:id/loginTitle"

# FOLLOWERS/FOLLOWING TABS
LIST_OF_ALL_FOLLOW_BTNS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.CompoundButton"
FIRST_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.CompoundButton"
SECOND_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.CompoundButton"
THIRD_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.CompoundButton"

# OTHER USER PROFILE VIEW
FOLLOW_TO_USER_BTN = "com.socialsuperstore:id/followButton"

# WESHOP INFO PAGES
MENU_TERMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]"
MENU_POLICY = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]"
MENU_COOKIE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]"
MENU_ACKNOWLEDGEMENTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]"
MENU_COMMUNITY_GUIDES = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]"
TERMS_PAGE_TEXT_TITLE = "weshop-terms-of-service"
PRIVACY_POLICY_TITLE = "privacy-policy"
COOKIE_POLICY_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
ACKNOWLEDGEMENTS_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
COMMUNITY_GUIDELINES_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
BROWSER_URL_BAR = "com.android.chrome:id/url_bar"

# SETINGS > ABOUT
APP_VERSION_SETTINGS_ABOUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]"

#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[2]