'''
1. define valid bots list
2. Execute bots based on that
'''

from robots import footlocker, nike, jdsports  # ,farfetch
import pandas as pd
from send_mail import mail_body_template as mbt
from send_mail import push_mail as pm
from send_mail import price_prediction as pp

'''
Input params -
Output -
'''


def execute_bots_for_mail(mail_list, conn):

    for item in mail_list:
        shoes = item['shoe_names']
        email = item['subscriber_id']
        price_df = pd.DataFrame()
        for shoe in shoes.split(','):

            for gender in [" men"]:  # , " women"]:

                #details = footlocker.get_shoe(shoe, gender, email)
                #price_df = price_df.append(details)

                # details = jdsports.get_shoe(shoe, gender, email)
                # price_df = price_df.append(details)

                # details = robots.farfetch.get_shoe(email, shoe, gender = gender)
                # price_df = price_df.append(details)

                if "nike" in shoe.lower():

                    details = nike.get_shoe(shoe, gender, email)
                    # print('[bot-controller]',details)
                    price_df = price_df.append(details)

        # get prediction for each shoe
        price_df = price_df[price_df['name'] != "NA"]

        if len(price_df) != 0:

            price_df_final = pp.price_trend(price_df, conn)
        # print('[bot-controller]','after price_df assignment')
            mail_body = mbt.mail_template(price_df_final)
        # print('[bot-controller] mailbody ready')
        else:
            mail_body = '''Sorry, We couldn't find any shoes matching your request.
            Please send us a mail at shoemetheprice@gmail.com with the shoe name and gender in the subject.
            Example subject - [M] Nike Air Max 1

            Thank You
            ShoeMeThePrice'''

    # NEED TO CALL SEND MAIL WITH mail_body AS ARGUMENT
        service = pm.connect_gmail_send()
        message = pm.create_message(email, shoes, mail_body)
        pm.send_message(service, message)

    return price_df


def execute_bots_for_daily(details, conn):

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

            details = footlocker.get_shoe(email, shoe, gender=gender)
            price_df = price_df.append(details)

            details = jdsports.get_shoe(email, shoe, gender=gender)
            price_df = price_df.append(details)

            # details = robots.farfetch.get_shoe(email, shoe, gender = gender)
            # price_df = price_df.append(details)

            if "nike" in shoe.lower():
                details = nike.get_shoe(email, shoe, gender=gender)
                price_df = price_df.append(details)

        # get prediction for each shoe

        price_df = price_df[price_df['name'] != "NA"]

        if len(price_df) != 0:

            price_df_final = pp.price_trend(price_df, conn)
        # print('[bot-controller]','after price_df assignment')
            mail_body = mbt.mail_template(price_df_final)
        # print('[bot-controller] mailbody ready')
        else:
            mail_body = '''Sorry, We couldn't find any shoes matching your request.
            Please send us a mail at shoemetheprice@gmail.com with the shoe name and gender in the subject.
            Example subject - [M] Nike Air Max 1

            Thank You
            ShoeMeThePrice'''

    # NEED TO CALL SEND MAIL WITH mail_body AS ARGUMENT
        service = pm.connect_gmail_send()
        message = pm.create_message(email, shoes, mail_body)
        pm.send_message(service, message)
    return price_df
