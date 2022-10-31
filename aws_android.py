import boto3
import pprint
import re
import requests
import os
import glob
import json


pp = pprint.PrettyPrinter(indent=4)

########################################
# get apps from s3 bucket
########################################
# Local credentials
# ACCESS_KEY = "xtest"
# SECRET_KEY = "xtest"
# SESSION_TOKEN = "xtest"

# AWS credentials
# ACCESS_KEY = os.getenv("ACCESS_KEY_ID")
# SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")
# SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
# REGION = os.getenv("AWS_REGION")

# BS credentials
# BS_USERNAME = os.getenv("BS_USERNAME")
# BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")

# CREDS
credentials = boto3.Session().get_credentials()

ACCESS_KEY = credentials.access_key
SECRET_KEY = credentials.secret_key
SESSION_TOKEN = credentials.token


# AWS boto session init + credentials
session = boto3.Session( 
		 aws_access_key_id=ACCESS_KEY, 
		 aws_secret_access_key=SECRET_KEY,
		 aws_session_token=SESSION_TOKEN)

client = boto3.client(
	's3',
	aws_access_key_id=ACCESS_KEY,
	aws_secret_access_key=SECRET_KEY,
	aws_session_token=SESSION_TOKEN
)


#######################
# generate Json (final action)
#######################
def generate_json(bucket_tags):
	app_link = []

	for i in bucket_tags:
		if "bs_link" in i.get("Key"):
			app_link.append(i.get("Value"))


	desired_cap = {
    "device" : "Samsung Galaxy A51",
    "os_version" : "10.0",
    "project" : "First Python project2",
    "build" : "browserstack-build-android",
    "name": "Android_tests",
    "app_url": app_link[0],
    "appium:resetKeyboard": True,
    "autoGrantPermissions": True,
	"appium:unicodeKeyboard": True,
	"appium:noReset:": False,
	"appium:resetKeyboard": True
	}


	with open(os.getcwd() + '/android_caps.json', 'w', encoding='utf-8') as f:
		json.dump(desired_cap, f, ensure_ascii=False, indent=4)

	print("Successfully updated json caps!")

# Filter all android apps and get latest file path and app id
def android_get_app_path():
	android_lst = []

	s3 = session.resource('s3')
	response_android = s3.Bucket('ss-travis-ci').objects.filter(Prefix='we-shop/Android/')

	for i in response_android:
		if i.key.startswith("we-shop/Android/") and i.key.endswith("/feature_base-qa.aab"):
			if ".1" not in i.key:
				android_lst.append(i.key)

	#we-shop/Android/14208/&showversions=false
	#get_direct = [i.key for i in s3.Bucket('ss-travis-ci').objects.filter(Prefix=sorted(android_lst)[-1])][0] # debug

	# get direct android path, looks like this "we-shop/Android/16143/build.aab"
	get_direct_path_android = sorted(android_lst)[-1]

	# get build id, looks like this "9143"
	getting_id_of_android_build = re.findall("\\d+", get_direct_path_android)[0]

	return get_direct_path_android, getting_id_of_android_build


LATEST_APP_PATH_AND_ID = android_get_app_path()
#print(LATEST_APP_PATH_AND_ID[0])

#print(LATEST_APP_PATH_AND_ID)
#we-shop/Android/14208/&showversions=false


# get tags of file
def get_tag_of_certain_file(path_app_id):
	response = client.get_object_tagging(
		Bucket='ss-travis-ci',
		Key=f"we-shop/Android/{path_app_id}/feature_base-qa.aab", #file_path
	)

	return response['TagSet']

# download certain (according to passed argument) file 
def download_android_app(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'feature_base-qa{new_name}.aab') #'WeShop.ipa')
	print(f"Android app downloaded, version {new_name}!")




# get whole list of downloaded (locally) files
def get_whole_scope_of_files():
	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	return str(glob.glob(os.getcwd() + "/*.aab"))

# getting latest local (downloaded) file
def get_latest_file(all_files):
	#downloading latest build
	#download_android_app(android_get_app_path())

	all_nums = max(re.findall("\\d+", all_files))

	#print(glob.glob(os.getcwd() + "/*.ipa")[0]) # debug
	#return str(glob.glob(os.getcwd() + "/*.ipa")) # debug

	for i in glob.glob(os.getcwd() + "/*.aab"):
		if all_nums in i:
			return i
	else:
		print(f"{SOMETHING_WRONG_WITH_FILE_NAME}")


# uploading downloaded latest app file
def upload_app_to_BS():
	LATEST_FILE_ANDROID = get_latest_file(get_whole_scope_of_files())

	files = {'file': (LATEST_FILE_ANDROID, open(LATEST_FILE_ANDROID, 'rb'))}
	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
				files=files, 
				auth=('mishatt_TZ84Lg', 'fcd9xqWeoVZUgpeZzz5t'))


	return json.loads(response.text)["app_url"]


def check_android_app_tags(path_to_file, tag_set):
	# re-name downloaded file
	app_id_build = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	#client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')


	if len(tag_set) == 0:
		print("Download started!")
		# download app file
		download_android_app(path_to_file)
		uploaded_bs_file_data = upload_app_to_BS()
		
		# update tags	
		response = client.put_object_tagging(
		Bucket="ss-travis-ci",
		Key=f"we-shop/Android/{app_id_build}/feature_base-qa.aab", #file_path
		Tagging={
		'TagSet': [
			{
				'Key': 'android_build_id',
				'Value': app_id_build,
			},
			{
				'Key': 'bs_link',
				'Value': uploaded_bs_file_data,
			},
		  ],
		 } 
	    )

		return [{'Key': 'bs_link', 'Value': uploaded_bs_file_data}, {'Key': 'android_build_id', 'Value': app_id_build}]

	else:
		print("Not needed")
		return get_tag_of_certain_file(app_id_build)


generate_json(check_android_app_tags(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))


#################################
# Debug just download certain app
#################################

#download_android_app("we-shop/Android/14796/feature_base-qa.aab")
