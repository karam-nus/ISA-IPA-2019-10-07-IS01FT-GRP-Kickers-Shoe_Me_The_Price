from persistence import db_updates
from statsmodels.tsa.seasonal import seasonal_decompose



def price_trend(df, conn):

    price_hist = db_updates.get_price_data(conn)

    df['trend'] = ''

    for shoe in df['name'].unique():

        shoe_df = price_hist.loc[price_hist['shoe_name'] == shoe]

        shoe_df.sort_values(['website', 'price_date'])

        for com in shoe_df.website.unique():

            shoe_company_df = shoe_df.loc[shoe_df['website'] == com]

            series = shoe_company_df['price'].values

            result = seasonal_decompose(series, model='additive', freq=1)

            delta = []

            result_trend = result.trend

            del_limit = len(result_trend)

            ind = df.index[(df['name'] == shoe) & (
                df['website'] == com)].tolist()

            if del_limit > 15:
                for i in range(del_limit, del_limit - 15, -1):

                    delta.append(result_trend[i-1] - result_trend[i-2])
                    # print(i)

                if np.mean(delta) > 0:

                    trend = 'Upwards'

                else:

                    trend = 'Downwards'

                    df['trend'][ind] = trend

                print(shoe, com, trend)
            else:
                df['trend'][ind] = 'Trend will be shared in upcomming mails'

    return df
