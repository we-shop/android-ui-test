import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from ui_page_objects.inbox_page_object import InboxPage
from ui_page_objects.dashboard_page_object import DashboardPage
from appium import webdriver
from ui_page_objects.functions import *
from dotenv import load_dotenv
import json


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

# BS CREDENTIALS
BS_LOGIN = os.getenv("BS_LOGIN")
BS_SECRET = os.getenv("BS_SECRET")

prefs = {"download.default_directory": os.getcwd() + "/"}


# fetching capabilities
json_f = open(os.getcwd() + '/android_caps.json') # travis CI
#json_f = open('android_caps.json') # local
desired_cap = json.load(json_f)
json_f.close()


# getting test result block
def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')        

# # Customizing appium driver for Browserstack
@pytest.fixture(autouse=True)
def selenium(request):
    #webdriver
    selenium = webdriver.Remote(
      command_executor=f'https://{BS_LOGIN}:{BS_SECRET}@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)

    get_session_id = selenium.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
    #print(get_session_id)
    yield selenium
    #print(get_session_id)
    print("#####")
    #print(session.results)

    print("#####")
    #x = "passed!"
    #selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "fqw"}}'.format(x))
    #print(type(get_session_id))
    selenium.quit() # marking test is finished for Browserstack
    #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt


# can be taken from caps.json
# desired_caps_local = {
#   "platformName": "Android",
#   "deviceName": "3647375352373098", #"21f050e03a027ece",
#   "platformVersion": "10",
#   "appPackage": "com.socialsuperstore",
#   "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",
#   "autoGrantPermissions": True,
#   "unicodeKeyboard": True,
#   "noReset:": False,
#   "resetKeyboard": True
# }


# # LOCAL (SHOULD BE COMMENTED, WHEN BS USED)
# @pytest.fixture
# def selenium(selenium):
#     #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
#     #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_cap)
#     #desired_cap
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
