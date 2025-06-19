import pandas as pd
import os
def extract(path_csv, path_parquet):
    '''Load files in local computer into Python

    :param path_csv: location of the csv file - if no csv files need loading, pass an empty string
    :param path_parquet: location of the parquet file- if no parquet files need loading, pass an empty string

    :return: a merged DataFrame
    '''
    csv_file = pd.read_csv(path_csv)
    parquet_file = pd.read_parquet(path_parquet, engine='pyarrow')
    raw_data = csv_file.merge(parquet_file, on = 'index')
    return raw_data


def transform(raw_data):
    '''Transform the data and return a clean DataFrame
    
    :param raw_data: DataFrame to be cleaned
    :return: a cleaned DataFrame with columns Store_ID, Month, Dept, IsHoliday, Weekly_Sales, CPI, Unemployment
    '''
    clean_data = raw_data[['Store_ID','Date','Dept','IsHoliday','Weekly_Sales','CPI','Unemployment']]

    # Fill missing values
    clean_data = raw_data.fillna(value={'Date':clean_data['Date'].mode().iloc[0],
                                        'Weekly_Sales':0,
                                        'CPI':0,
                                        'Unemployment':0})

    # Adding column Month
    clean_data['Date'] = pd.to_datetime(clean_data['Date'])
    clean_data['Month'] = clean_data['Date'].dt.month

    # Filter records where Weekly_Sales over 10000
    clean_data = clean_data.loc[clean_data['Weekly_Sales']>10000, :]
    
    return clean_data[['Store_ID','Month','Dept','IsHoliday','Weekly_Sales','CPI','Unemployment']]

def avg_sales(clean_data):
    '''Calculate the average weekly sales of each month
    
    :param: clean_data: a cleaned DataFrame
    :return: a DataFrame with aggregated data
    '''

    agg_data = round(clean_data[['Month','Weekly_Sales']].groupby(by='Month',axis=0).mean().reset_index(),2)
    agg_data.rename(columns={'Weekly_Sales':'Avg_sales'}, inplace=True)
    return agg_data

def load(data_1, data_2, path_1, path_2):
    '''Load the transformed data to csv files
    '''
    data_1.to_csv(path_1, index=False)
    data_2.to_csv(path_2, index=False)

def validation(file_path):
    assert os.path.exists(file_path)