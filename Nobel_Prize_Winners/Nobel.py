import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'F:\Huy-Le-Data-Projects\Nobel_Prize_Winners')
nobel = pd.read_csv('nobel.csv')

#%%
top_gender = nobel.value_counts('sex')
# print(top_gender)
top_category = nobel.value_counts('category')
# print(top_category)
top_category = pd.DataFrame(top_category).reset_index()
top_category_bar = sns.catplot(x='category',y='count',data=top_category,kind='bar',palette='PuRd')
top_category_bar.fig.suptitle('Number of Nobel Prize Winners by category')
top_category_bar.set(xlabel='Category',ylabel='Number of Nobel Prize Winners')
plt.xticks(rotation=90)
plt.show()

#%%
top_country = nobel.value_counts('birth_country')
print(top_country)
# print(len(top_country))
top_country = pd.DataFrame(top_country)
top_country = top_country.reset_index()
top_country.loc[top_country['count']>10,'new_birth_country'] = top_country['birth_country']
top_country.loc[top_country['count']<=10,'new_birth_country'] = 'Other'


top_country_bar = sns.catplot(x='new_birth_country',y='count',data=top_country,kind='bar',palette='Blues_r')
top_country_bar.fig.suptitle('Countries with highest number of Nobel Prize Winners')
top_country_bar.set(xlabel='Country',ylabel='Number of Nobel Prize Winners')
plt.xticks(rotation=90)
plt.show()

#%%
tmp = nobel[nobel['sex']=='Female'].sort_values('year').loc[:,['full_name','category','year']].head(1)
first_woman_name = tmp['full_name'].values[0]
# values[0] to get the value without the index
print(first_woman_name)
first_woman_category = tmp['category'].values[0]
print(first_woman_category)
first_woman_year = tmp['year'].values[0]
print(first_woman_year)



#%%
nobel['decade'] = nobel['year']//10 *10
nobel.loc[nobel['sex']=='Female','is_female']=1
nobel.loc[nobel['sex']!='Female','is_female']=0
tmp = nobel.loc[:,['decade','is_female']]
f_ratio = tmp.groupby(['decade'],as_index=False)['is_female'].mean()
# as_index=False to return a DataFrame, not a Series
print(f_ratio.sort_values('is_female',ascending=False).head(1)['decade'].values[0])

f_ratio_line = sns.relplot(x='decade',y='is_female',data=f_ratio,kind='line',ci=None)
f_ratio_line.fig.suptitle('Ratio of female winners by decade')
f_ratio_line.set(xlabel='Decade',ylabel='Female winners ratio')
plt.show()



#%%

tmp = nobel.value_counts('full_name')
repeat_list = list(tmp.loc[tmp>1].index)
print(nobel[nobel['full_name'].isin(repeat_list)].loc[:,['full_name','category','year']])

print(len(repeat_list))
# print(repeat_list)






