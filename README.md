1) You need to have Python at least 3.8+

2) Required Python packages:
Appium-Python-Client==2.0.0
pytest==6.2.5
pytest-base-url==1.4.2
pytest-forked==1.3.0
pytest-html==3.1.1
pytest-metadata==1.11.0
pytest-selenium==2.0.1
pytest-variables==1.9.0
pytest-xdist==2.4.0
requests==2.26.0
selenium==4.0.0
python-dotenv==0.19.2

3) For local launch you need to have latest "Appium Server Gui" that can be downloaded here:
https://appium.io

Note that "Appium Server Gui" also require Java installation.

4) Also, you need to have real device on service, like Browserstack to execute tests on some hardware.

5) Launch line:
pytest test_uat.py