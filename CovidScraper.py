# Sharon Lu
# CovidScraper.py
# Figure out when Giant Website shows available covid vaccination times

import requests
from bs4 import BeautifulSoup
import smtplib
import time

appointment_found = 0

URL = 'https://covidinfo.reportsonline.com/covidinfo/GiantFood.html?queueittoken=e_giantfoodcovid19~q_c8c57978-5716-454c-8b2e-cf3059454bc7~ts_1613069589~ce_true~rt_safetynet~h_42e88d5b2fe7779b2324cd29320bbe3ca8f6a5bb98ec141434b3220c93825470'

headers = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

def check_site():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser') #parses data from webpage
	
	try:
		title = soup.find(id="Content").get_text()
		if(title.strip() != "There are currently no COVID-19 vaccine appointments available. Please check back later. We appreciate your patience as we open as many appointments as possible. Thank you."):
			send_mail()
			return 1
		else:
			return 0
	except AttributeError:
		print("Attribute Error")

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls() #encrypts connection
	server.ehlo()
	server.login('sharonlu4@gmail.com', 'kngqpvnhxqeqqetl')
	subject = 'Vaccine appointments available!'
	body = 'Check Giant link https://covidinfo.reportsonline.com/covidinfo/GiantFood.html?queueittoken=e_giantfoodcovid19~q_c8c57978-5716-454c-8b2e-cf3059454bc7~ts_1613069589~ce_true~rt_safetynet~h_42e88d5b2fe7779b2324cd29320bbe3ca8f6a5bb98ec141434b3220c93825470'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'sharonlu4@gmail.com',
		'sharon.lu@bia-boeing.com', # Put receiver email here
		msg
	)
	print('An email has been sent!')

	server.quit()

while(appointment_found == 0):
	appointment_found = check_site()
	time.sleep(1) #in seconds


