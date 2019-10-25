'''
1. define valid bots list
2. Execute bots based on that
'''

from robots import footlocker, nike, jdsports #,farfetch
import pandas as pd

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

	return price_df
	
def execute_bots_for_website(details):
	price_df = pd.DataFrame()
	email = details['email']
	shoes = details['shoes']
	gender = details['gender']

	if gender == "Male":
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

	return price_df
	
