import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r'F:\Huy-Le-Data-Projects\Netflix_movies')
netflix = pd.read_csv('netflix_data.csv')
print(len(netflix))
# '''1942-2021'''
# print(netflix.columns)

#%% Most common genres
'''Which genre is the most common during this time'''
common_gen = pd.DataFrame(netflix.value_counts('genre')).reset_index()
common_gen['mod_gen'] = common_gen['genre'].where(common_gen['count']>=20,'Other')
print(common_gen)

gen_bar = sns.catplot(x='mod_gen',y='count',data=common_gen,kind='bar',palette='PuRd_r')
gen_bar.fig.suptitle('Most common genres')
gen_bar.set(xlabel='Genre',ylabel='Number of movies')
plt.xticks(rotation=90)
plt.show()

#%% Most productive producers
pro_dir = pd.DataFrame(netflix.value_counts('director')).reset_index()
pro_dir['mod_dir'] = pro_dir['director'].where(pro_dir['count']>=10,'Other')
print(pro_dir)

dir_bar = sns.catplot(x='mod_dir',y='count',data=pro_dir,kind='bar',palette='Blues_r')
dir_bar.fig.suptitle('Most productive directors')
dir_bar.set(xlabel='Director',ylabel='Number of movies')
plt.xticks(rotation=90)
plt.show() 


#%% Decade with the most movies:

netflix['decade'] = netflix['release_year']//10 *10
# print(netflix.head())

top_dec = netflix.groupby('decade',as_index=False)['decade'].value_counts()
print(top_dec)


top_dec_bar = sns.catplot(x='decade',y='count',data=top_dec,kind='bar',palette='rocket')
top_dec_bar.fig.suptitle('Decade with the most movies/shows')
top_dec_bar.set(xlabel='Decade',ylabel='Number of movies/shows')
plt.show()

top_dec_line = sns.relplot(x='decade',y='count',data=top_dec,kind='line',palette='rocket')
top_dec_line.fig.suptitle('Number of movies/show fluctuation by decade')
top_dec_line.set(xlabel='Decade',ylabel='Number of movies/shows')
plt.show()



