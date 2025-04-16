import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r'F:\Huy-Le-Data-Projects-base\Olist_Ecommerce\Cancellation_rate\data')
orders_by_cat = pd.read_csv('orders_by_cat.csv')
cat_w_canceled = pd.read_csv('cat_w_canceled.csv')
del_time = pd.read_csv('dev_cat.csv')
est_del_time = pd.read_csv('cat_exp_del_time.csv')
ccp = pd.read_csv('cat_cancel_price.csv')
#%% cancellation bar chart
tmp = cat_w_canceled.merge(orders_by_cat,on='category_name',how='left')
# print(tmp)

fig, ax1 = plt.subplots(figsize=(18, 8))

sns.barplot(data=tmp, x='category_name', y='num_orders', color='skyblue', ax=ax1)
ax1.set_xlabel('Category', fontsize=12)
ax1.set_ylabel('Number of orders', color='skyblue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='skyblue')
plt.xticks(rotation=90, fontsize=10)

ax2 = ax1.twinx()

sns.lineplot(data=tmp, x='category_name', y='num_orders_canceled', color='tomato', marker='o', linewidth=2, ax=ax2)
ax2.set_ylabel('Number of cancelled orders', color='tomato', fontsize=12)
ax2.tick_params(axis='y', labelcolor='tomato')

plt.title('Number of orders and cancelled orders by category', fontsize=16)

plt.tight_layout()
plt.show()

#%% cancellation and delivery time 
print(np.mean(del_time['delivery_time']))

del_tmp = cat_w_canceled.merge(del_time,on='category_name',how='left')



scat = sns.relplot(x='num_orders_canceled',y='delivery_time',data=del_tmp,kind='scatter',size='delivery_time',hue='delivery_time')
scat.fig.suptitle('Relationship between number of canceled orders and delivery time')
scat.set(xlabel='Orders canceled',ylabel='Delivery time (days)')
plt.show()
# print(del_tmp['num_orders_canceled'].corr(del_tmp['delivery_time']))

#%% estimated delivery time
est_tmp = del_time.merge(est_del_time,on='category_name',how='left')
print(est_tmp.columns)

est_tmp.set_index('category_name')[['delivery_time', 'estimated_delivery_time']].plot(
    kind='bar',
    stacked=True,
    color=['#4CAF50', '#F44336'],
    figsize=(8, 6)
)

# Thêm tiêu đề và nhãn
plt.title('Estimated and real delivery time (days)')
plt.xlabel('Category')
plt.ylabel('Delivery time (days)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()

