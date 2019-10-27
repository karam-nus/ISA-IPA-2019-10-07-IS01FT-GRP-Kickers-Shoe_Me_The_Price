from persistence import db_updates
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np



def price_trend(df, conn):
    df.reset_index(inplace=True)
    price_hist = db_updates.get_price_data(conn)
    price_hist.reset_index(inplace=True)

    print('[pp]a')
    df['trend'] = 'Trend will be shared in upcomming mails'
    print('[pp]b')

    for shoe in df['name'].unique():

        shoe_df = price_hist.loc[price_hist['shoe_name'] == shoe]

        shoe_df.sort_values(['website', 'price_date'])

        for com in shoe_df.website.unique():
            
            print(shoe, "company = ", com)
    
            shoe_company_df = shoe_df.loc[shoe_df['website'] == com]
            print('[pp]shoe 1')

            series = shoe_company_df['price'].values
            print('[pp]shoe 2', series)

            if len(series) < 15:
                continue

            result = seasonal_decompose(series, model='additive', freq=1)
            print('[pp]shoe 3')

            delta = []

            result_trend = result.trend
            print('[pp]shoe 4')

            del_limit = len(result_trend)
            print('[pp]shoe 5')

            ind = df.index[(df['name'] == shoe) & (
                df['Company'] == com.lower().capitalize())].tolist()
            print('[pp]',ind)
            #print('[pp]shoe 5')

            if del_limit > 15:
                for i in range(del_limit, del_limit - 15, -1):
                    
                    delta.append(result_trend[i-1] - result_trend[i-2])
                    # print(i)

                if np.mean(delta) > 0:

                    trend = 'Upwards'

                else:

                    trend = 'Downwards'

                    df['trend'][ind] = trend

                #print(shoe, com, trend)
            

    return df
