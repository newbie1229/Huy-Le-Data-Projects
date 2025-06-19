from etl_utils.pipeline_utils import extract, transform, avg_sales, load, validation
import os
os.chdir(r'F:\Data Courses\DataCamp\Data Engineer\Data Engineer in Python\Building a Retail Data Pipeline\data')

raw_data = extract('grocery_sales.csv','extra_data.parquet')
clean_data = transform(raw_data)
agg_data = avg_sales(clean_data)
load(clean_data, agg_data, 'clean_data.csv','agg_data.csv')
validation('clean_data.csv')
validation('agg_data.csv')