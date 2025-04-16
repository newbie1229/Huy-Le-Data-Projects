import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'F:\Huy-Le-Data-Projects-base\Olist_Ecommerce\Reviews\data')
rating = pd.read_csv('pro_reviews.csv')
revenue = pd.read_csv('Rev_cat.csv')
delivery = pd.read_csv('dev_cat.csv')
freight = pd.read_csv('cat_freight.csv')
answer = pd.read_csv('cat_answer.csv')
# print(answer)

#%% Overview
# Average rating
print(np.mean(rating['average_rating']))

# rating distribution
plt.hist(rating['average_rating'])
plt.title('Rating distribution')
plt.xlabel('Rating')
plt.ylabel('Number of categories')
plt.show()


#%% Top categories with highest rating
top_rating = rating.sort_values('average_rating',ascending=False).head(5)
print(top_rating)

top_bar = sns.catplot(x='category_name',y='average_rating',data=top_rating,kind='bar',hue='average_rating',palette='flare')
top_bar.fig.suptitle('Categories with highest rating')
top_bar.set(xlabel='Category Name',ylabel='Rating')

#%% categories with low rating
bot_rating = rating.sort_values('average_rating').head(5)
print(bot_rating)

top_bar = sns.catplot(x='category_name',y='average_rating',data=bot_rating,kind='bar',hue='average_rating',palette='crest')
top_bar.fig.suptitle('Categories with lowest rating')
top_bar.set(xlabel='Category Name',ylabel='Rating')

#%% rating and delivery time
rating_delivery = rating.merge(delivery,on='category_name')
print(rating_delivery['delivery_time'].corr(rating_delivery['average_rating']))

rat_del_scat = sns.relplot(x='average_rating',y='delivery_time',data=rating_delivery,kind='scatter',hue='average_rating')
rat_del_scat.fig.suptitle('Relationship between rating and delivery time')
rat_del_scat.set(xlabel='Rating',ylabel='Delivery time (days)')

#%% rating and revenue
rating_revenue = rating.merge(revenue,on='category_name')
print(rating_revenue['average_rating'].corr(rating_revenue['revenue']))

rat_rev_scat = sns.relplot(x='average_rating',y='revenue',data=rating_revenue,kind='scatter',hue='average_rating')
rat_rev_scat.fig.suptitle('Relationship between rating and revenue')
rat_rev_scat.set(xlabel='Rating',ylabel='Revenue (RBL)')

#%% rating and freight value
rating_freight = rating.merge(freight,on='category_name')
print(rating_freight['average_rating'].corr(rating_freight['shipping_cost']))

rat_fre_scat = sns.relplot(x='average_rating',y='shipping_cost',data=rating_freight,kind='scatter',hue='average_rating')
rat_fre_scat.fig.suptitle('Relationship between rating and shipping cost')
rat_fre_scat.set(xlabel='Rating',ylabel='Shipping cost (RBL)')

#%% rating and answer time
rating_answer = rating.merge(answer,on='category_name')
# print(rating_answer)
print(rating_answer['average_rating'].corr(rating_answer['answer_time']))

rat_ans_scat = sns.relplot(x='average_rating',y='answer_time',data=rating_answer,kind='scatter',hue='average_rating')
rat_ans_scat.fig.suptitle('Relationship between rating and answer time')
rat_ans_scat.set(xlabel='Rating',ylabel='Answer time (days)')

print(rating_answer[rating_answer['answer_time']>9])
