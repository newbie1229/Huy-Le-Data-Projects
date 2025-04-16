import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'F:\Huy-Le-Data-Projects-base\Olist_Ecommerce\Customer_behavior\data')
month = pd.read_csv('purchase_month.csv')
month = pd.DataFrame(month.value_counts('purchase_month')).reset_index()
delivery_time = pd.read_csv('delivery_time_by_month.csv')
daypart = pd.read_csv('part_otd.csv')
# print(daypart)

#%% convert month name
convert = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
    } 

for i in range(1,13):
    month.loc[i-1,'month'] = convert[month.loc[i-1,'purchase_month']]
    delivery_time.loc[i-1,'month'] = convert[delivery_time.loc[i-1,'purchase_month']]

month = month.sort_values('purchase_month')
print(month)

delivery_time = delivery_time.sort_values('purchase_month')
print(delivery_time)
#%% puchase line
line = sns.relplot(x='month',y='count',data=month,kind='line')
line.fig.suptitle('Purchase fluctuation')
line.set(xlabel='Month',ylabel='Number of purchases')
plt.show()

# delivery time by month line
time = sns.relplot(x='month',y='delivery_time',data=delivery_time,kind='line',palette='crest')
time.fig.suptitle('Delivery time by month')
time.set(xlabel='Month',ylabel='Delivery time (days)')
plt.show()


#%% month with most purchases
common_month = month.sort_values('count',ascending=False).head(5)
common_month = common_month.sort_values('purchase_month')
print(common_month)

cm_bar = sns.catplot(x='month',y='count',data=common_month,kind='bar',palette='flare')
cm_bar.fig.suptitle('Months with most purchases')
cm_bar.set(xlabel='Month',ylabel='Number of purchases')
plt.show()

#%% active part of the day
custom_order = ['Morning', 'Noon', 'Afternoon', 'Evening', 'Midnight']

daypart['part_otd'] = pd.Categorical(daypart['part_otd'], categories=custom_order, ordered=True)
daypart = daypart.sort_values('part_otd')

daybar = sns.catplot(x='part_otd',y='count',data=daypart,kind='bar',palette='crest')
daybar.fig.suptitle('Active parts of the day')
daybar.set(xlabel='Part of the day',ylabel='Number of orders')
plt.show()
