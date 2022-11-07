import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os
from datetime import datetime

# getting current date
cur_date = datetime.today().strftime('%d-%m-%Y')


recipients_list = ["abavabaraba@gmail.com", "mike_zone@ukr.net"]
GMAIL_ACC_KEY = os.getenv("GMAIL_ACC_KEY")

def email_sender(recipient):
	# travis link
	travis_ci_build_link = os.getenv("TRAVIS_BUILD_WEB_URL")

	subject = f"Travis CI report | Android automation tests | {cur_date}"
	body = f"Travis CI build link: {travis_ci_build_link}"
	sender_email = "abavabaraba@gmail.com"
	receiver_email = recipient #"abavabaraba@gmail.com", "mike_zone@ukr.net" #"abavabaraba@gmail.com"
	password = GMAIL_ACC_KEY #input("Type your password and press enter:")

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	filename = os.getcwd() + "/report.html"  # report to send (should be in root folder)

	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
		# Add file as application/octet-stream
		# Email client can usually download this automatically as attachment
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename= {filename}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)

# send report email(s)
if len(recipients_list) > 0:
	for i in recipients_list:
		email_sender(i)
		time.sleep(0.5)

else:
	print(f"{ERORR} RECIPIENT LIST IS EMPTY!")

