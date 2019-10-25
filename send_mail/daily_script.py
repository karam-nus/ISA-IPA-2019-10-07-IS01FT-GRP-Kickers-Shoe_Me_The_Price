import pandas as pd
import persistance as p
from robots import bot_controller


def daily_updates(conn):

	data = p.db_updates.get_customer_data(conn)

	bot_controller.execute_bots_for_daily(details)

