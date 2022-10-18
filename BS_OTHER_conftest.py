import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from ui_page_objects.inbox_page_object import InboxPage
from appium import webdriver
from ui_page_objects.functions import *


from dotenv import load_dotenv

load_dotenv()

# Read from file function
def get_data(data):
  return data.split("#")[0]

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
LOGIN_NEW = os.getenv("LOGIN_NEW")
PASSWORD_NEW = os.getenv("PASSWORD_NEW")
LOGIN_INT = os.getenv("LOGIN_INT")
PASSWORD_INT = os.getenv("PASSWORD_INT")
LOGIN_INT_NEW = os.getenv("LOGIN_INT_NEW")
PASSWORD_INT_NEW = os.getenv("PASSWORD_INT_NEW")


prefs = {"download.default_directory": os.getcwd() + "/"}


#caps for Browserstack
# "device" : "Samsung Galaxy S21",
# "os_version" : "11.0"

# {"app_url":"bs://576463a96efb0a64e20d5abe7652b5faa671aba4"}

# /* In your test script, use this "app_url" value to specify the application under test using the "app" capability. During test execution, your app will automatically be installed and launched on the device being tested. */

# caps.setCapability("app", "bs://576463a96efb0a64e20d5abe7652b5faa671aba4")

# BROWSERSTACK_BUILD_NAME # browserstack-build-13
desired_cap = {
  "device" : "Samsung Galaxy A51",
  "os_version" : "10.0",
  "project" : "First Python project2", 
  "build" : 'browserstack-build-13', 
  "name" : 'test-browserstack-build-13',
  "appPackage": "com.socialsuperstore",
  "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
  "app_url":"bs://30685e2517ddd3049429ddb20accdddb77403845",
  "browser" : "Chrome",
  "browserstack.idleTimeout":10,
  "implicit":8000,
  "autoGrantPermissions": True,
  "unicodeKeyboard": True,
  "noReset:": True,
  "resetKeyboard": True }


# BS TEMP BLOCK
username = os.getenv("BROWSERSTACK_USERNAME") # mika_ajI75Z
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY") # 3LEmS9BCLDd6zL4uzufk
build_name = os.getenv("BROWSERSTACK_BUILD_NAME") # browserstack-build-13
#browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
#browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
BROWSERSTACK_BUILD_NAME = os.getenv("BROWSERSTACK_BUILD_NAME")

caps = {
 "device" : "Samsung Galaxy A51",
 "os_version" : "10.0",
 "project" : "First Python project2",
 'browser': 'chrome',
 'browser_version': 'latest',
 'name': 'BStack-Jenkins Sample Test', # test name
 'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
 #'browserstack.local': browserstack_local,
 #'browserstack.localIdentifier': browserstack_local_identifier,
 'browserstack.user': username,
 'browserstack.key': access_key,
 "appPackage": "com.socialsuperstore",
 "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
 "app_url":"bs://30685e2517ddd3049429ddb20accdddb77403845",
 "browserstack.idleTimeout":10,
 "implicit":8000,
 "autoGrantPermissions": True,
 "unicodeKeyboard": True,
 "noReset:": True,
 "resetKeyboard": True 
}

  # "device" : "Samsung Galaxy A51",
  # "os_version" : "10.0",
  # "project" : "First Python project2", 
  # "build" : BROWSERSTACK_BUILD_NAME, 
  # "name" : BROWSERSTACK_BUILD_NAME,
  # "appPackage": "com.socialsuperstore",
  # "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
  # "app_url":"bs://30685e2517ddd3049429ddb20accdddb77403845",
  # "browser" : "Chrome",
  # "browserstack.idleTimeout":10,
  # "implicit":8000,
  # "autoGrantPermissions": True,
  # "unicodeKeyboard": True,
  # "noReset:": True,
  # "resetKeyboard": True }



# Customizing appium driver for Browserstack
# @pytest.fixture(autouse=True)
# def selenium(request):
#     webdriver
#     selenium = webdriver.Remote(
#       command_executor='http://hub-cloud.browserstack.com/wd/hub/',
#       desired_capabilities=caps)

#     yield selenium
#     selenium.quit() # marking test is finished for Browserstack
#     #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
#     clear_data_from_temp_file() # clearing data in temp_data.txt


# Customizing appium driver for Browserstack
@pytest.fixture(autouse=True)
def selenium(request):
    webdriver
    selenium = webdriver.Remote(
      command_executor='https://mika_ajI75Z:3LEmS9BCLDd6zL4uzufk@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)

    yield selenium
    selenium.quit() # marking test is finished for Browserstack
    #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt









# #Customizing appium driver (implicitly waits + app close/kill)
# @pytest.fixture
# def selenium(selenium):
#     #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
#     selenium.implicitly_wait(7)
#     yield selenium
#     #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
#     #selenium.terminate_app('com.socialsuperstore') # put app in background
#     selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
#     clear_data_from_temp_file() # clearing data in temp_data.txt


#FIXTURES PAGE OBJECT
@pytest.fixture()
def login_model(request):
  fixture = LoginPage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture

@pytest.fixture()
def debug_model(request):
  fixture = DebugPage()
  return fixture

@pytest.fixture()
def search_model(request):
  fixture = SearchPage()
  return fixture

@pytest.fixture()
def product_page_model(request):
  fixture = ProductDetailPage()
  return fixture

@pytest.fixture()
def profile_model(request):
  fixture = ProfilePage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture

@pytest.fixture()
def post_model(request):
  fixture = PostPage()
  return fixture

@pytest.fixture()
def inbox_model(request):
  fixture = InboxPage()
  return fixture

@pytest.fixture()
def dashboard_model(request):
  fixture = DashboardPage(LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW)
  return fixture
