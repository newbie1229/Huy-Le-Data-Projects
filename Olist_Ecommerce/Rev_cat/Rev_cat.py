import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'F:\Huy-Le-Data-Projects-base\Olist_Ecommerce\Rev_cat')
revenue = pd.read_csv('Rev_cat.csv',index_col='category_name')

#%% Average revenue
print(f'Average revenue: {round(revenue["revenue"].mean(),2)}')

#%% Top categories
top_10 = revenue.sort_values('revenue',ascending=False).head(10)
print(f'Average revenue of the top 10 categories: {round(top_10["revenue"].mean(),2)}')  
# top_10 = top_10.sort_values('revenue',ascending=True)
top_10_bar = sns.catplot(x='revenue',y='category_name',data=top_10,kind='bar',palette='Blues_r',aspect=5)
top_10_bar.set(xlabel='Revenue (RBL)',ylabel='Category')
top_10_bar.fig.suptitle('Categories with highest revenue')
# plt.xticks(rotation=90)
# plt.tight_layout()
plt.show()

#%% Bottom categories
bot_10 = revenue.sort_values('revenue',ascending=True).head(10)
print(f'Average revenue of the bottom 10 categories: {round(bot_10["revenue"].mean(),2)}')
bot_10_bar = sns.catplot(x='revenue',y='category_name',data=bot_10,kind='bar',palette='PuRd',aspect=5)
bot_10_bar.set(xlabel='Revenue (RBL)',ylabel='Category')
bot_10_bar.fig.suptitle('Categories with lowest revenue')
# plt.xticks(rotation=90)
plt.show()