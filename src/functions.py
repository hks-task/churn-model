from datetime import timedelta
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


def getWeeklyDates(df, break_point):

    df['order_date'] = pd.to_datetime(df['order_date'])
    three_day = df[df['order_date'] >= break_point - timedelta(days=3)]
    one_week = df[df['order_date'] >= break_point - timedelta(days=7)]
    two_week = df[df['order_date'] >= break_point - timedelta(days=14)]
    four_week = df[df['order_date'] >= break_point - timedelta(days=28)]
    twelve_week = df[df['order_date'] >= break_point - timedelta(days=84)]
    twenty_four_week = df[df['order_date'] >= break_point - timedelta(days=168)]
    all_week = df
    return three_day, one_week, two_week, four_week, twelve_week, twenty_four_week,all_week


def transform_data(df):

    labelencoder = LabelEncoder()

    for i in ['restaurant_id', 'city_id', 'payment_id', 'platform_id', 'transmission_id']:
        df[i] = labelencoder.fit_transform(df[i])

    return df


def feature_engineering(df, break_point):
    df['customer_order_rank'] = df['customer_order_rank'].fillna(method='ffill')

    df['date'] = pd.to_datetime(df['order_date'])
    df['recency'] = (break_point - df['date']) / np.timedelta64(1, 'D')
    df['first_order_date'] = df.groupby(['customer_id'])['date'].transform('first')
    df['age_of_user'] = (break_point - df['first_order_date']) / np.timedelta64(1, 'D')

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['week'] = df['date'].dt.week
    df['day'] = df['date'].dt.day
    df['dayofweek'] = df['date'].dt.dayofweek
    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(np.int8)

    df['demand'] = 1

    df['order_date_shift'] = df.groupby('customer_id')['date'].shift()
    df['date_diff'] = (df['date'] - df['order_date_shift']) / np.timedelta64(1, 'D')

    col = ['demand', 'is_failed', 'voucher_amount', 'delivery_fee', 'amount_paid', 'date_diff']
    three_day, one_week, two_week, four_week, twelve_week, twenty_four_week, all_week = getWeeklyDates(df, break_point)
    three_day = three_day.groupby('customer_id')[col].mean().add_prefix('three_day_').reset_index()
    one_week = one_week.groupby('customer_id')[col].mean().add_prefix('one_week_').reset_index()
    two_week = two_week.groupby('customer_id')[col].mean().add_prefix('two_week_').reset_index()
    four_week = four_week.groupby('customer_id')[col].mean().add_prefix('four_week_').reset_index()
    twelve_week = twelve_week.groupby('customer_id')[col].mean().add_prefix('twelve_week_').reset_index()
    twenty_four_week = twenty_four_week.groupby('customer_id')[col].mean().add_prefix('twenty_four_week_').reset_index()
    all_week = all_week.groupby('customer_id')[col].mean().add_prefix('all_week_').reset_index()

    df = df.groupby('customer_id').last().reset_index()
    df = df.merge(three_day, how='left').merge(one_week, how='left').merge(two_week, how='left').merge(four_week,
                                                                                                       'left').merge(
        twelve_week, 'left').merge(twenty_four_week, 'left').merge(all_week, 'left').reset_index()

    return df