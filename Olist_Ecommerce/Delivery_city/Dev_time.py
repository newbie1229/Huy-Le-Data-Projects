import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'F:\Huy-Le-Data-Projects-base\Olist_Ecommerce\Delivery_city')
delivery = pd.read_csv('Dev_time.csv',index_col='seller_city')

#%% Average delivery time
print(f'The average delivery time is {round(np.mean(delivery["delivery_time_day"]),1)} days')
print()

delivery.loc[delivery['delivery_time_day']<=7,'time_cat'] = 'Less than 1 week'
delivery.loc[(7<delivery['delivery_time_day']) & (delivery['delivery_time_day']<=14),'time_cat'] = 'One to Two weeks'
delivery.loc[(14<delivery['delivery_time_day']) & (delivery['delivery_time_day']<=30),'time_cat'] = 'Two weeks to a month'
delivery.loc[30<delivery['delivery_time_day'],'time_cat'] = 'More than one month'
time_cat_bar = sns.catplot(x='time_cat',data=delivery,kind='count',hue='time_cat')
time_cat_bar.set(xlabel='Delivery Time',ylabel='Number of cities')
time_cat_bar.fig.suptitle('Distribution of Delivery Time Categories')
plt.show()

#%% Fastest delivery time
top_10 = delivery.sort_values('delivery_time_day').head(10)
print(f'The average delivery time of the top 10 cities {top_10["delivery_time_day"].mean()} days')
top_10_bar = sns.catplot(x='seller_city',y='delivery_time_day',data=top_10,kind='bar',palette='Blues')
top_10_bar.fig.suptitle('Cities with shortest delivery time')
top_10_bar.set(xlabel='City',ylabel='Delivery time (days)')
plt.show()

#%% Long delivery time
bot_10 = delivery.sort_values('delivery_time_day',ascending=False).head(10)
print(f'The average delivery time of the bottom 10 cities {bot_10["delivery_time_day"].mean()} days')
bot_10_bar = sns.catplot(x='seller_city',y='delivery_time_day',data=bot_10,kind='bar',palette='PuRd')
bot_10_bar.fig.suptitle('Cities with highest delivery time')
bot_10_bar.set(xlabel='City',ylabel='Delivery time (days)')
plt.show()