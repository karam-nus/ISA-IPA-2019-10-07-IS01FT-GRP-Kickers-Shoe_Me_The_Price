'''
1. define valid bots list
2. Execute bots based on that
'''

from robots import footlocker, nike, jdsports #,farfetch
import pandas as pd
from send_mail import mail_body_template as mbt
nike_list = []

'''
Input params -
Output -
'''
def execute_bots_for_mail(mail_list):

	price_df = pd.DataFrame()

	for item in mail_list:
		shoes = item['shoe_names']
		email = item['subscriber_id']

		for shoe in shoes.split(','):

			for gender in [" men", " women"]:
					
					
				details = footlocker.get_shoe(shoe, gender, email)
				price_df = price_df.append(details)
				
				details = jdsports.get_shoe(shoe, gender, email)
				price_df = price_df.append(details)

				# details = robots.farfetch.get_shoe(email, shoe, gender = gender)
				# price_df = price_df.append(details)

				if "nike" in shoe.lower():

					details = nike.get_shoe(shoe, gender, email)
					price_df = price_df.append(details)

	mail_body = mbt.mail_template(price_df)				
	
	##### NEED TO CALL SEND MAIL WITH mail_body AS ARGUMENT
	
	return price_df
	
def execute_bots_for_daily(details):
	
	price_df = pd.DataFrame()

	for i in range(0, len(data)):
		email = details['email'][i]
		shoes = details['shoes'][i]
		gender = details['gender'][i]

		if gender == "M":
			gender = ' men'
		else:
			gender = ' women'


		for shoe in shoes.split(','):

			details = footlocker.get_shoe(email, shoe, gender = gender)
			price_df = price_df.append(details)
			
			details = jdsports.get_shoe(email, shoe, gender = gender)
			price_df = price_df.append(details)

			# details = robots.farfetch.get_shoe(email, shoe, gender = gender)
			# price_df = price_df.append(details)

			if "nike" in shoe.lower():
				details = nike.get_shoe(email, shoe, gender = gender)
				price_df = price_df.append(details)

		mail_body = mbt.mail_template(price_df)
	##### NEED TO CALL SEND MAIL WITH mail_body AS ARGUMENT

	return price_df
	
