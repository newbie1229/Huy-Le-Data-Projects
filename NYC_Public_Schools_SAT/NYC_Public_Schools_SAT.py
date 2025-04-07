import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('notebook')
os.chdir(r'F:\Huy-Le-Data-Projects-base\NYC_Public_Schools_SAT')
schools = pd.read_csv('schools.csv')
# print(schools.columns)
# print(len(schools))
'''
Index(['school_name', 'borough', 'building_code', 'average_math',
       'average_reading', 'average_writing', 'percent_tested'],
      dtype='object')
'''

#%% Top 10 schools with best math results and avg math score
print(np.mean(schools['average_math']))
best_math = schools.sort_values('average_math',ascending=False)[['school_name','average_math']].head(10)
print(best_math['school_name'])

best_math_bar = sns.catplot(x='average_math',y='school_name',data=best_math,kind='bar',palette='PuRd_r',aspect=5)
best_math_bar.fig.suptitle('Best Schools based on Math score')
best_math_bar.set(xlabel='Math Score',ylabel='School Name')
plt.tight_layout()
plt.show()


#%% Top 10 schools with best reading results and avg reading score
print(np.mean(schools['average_reading']))
best_reading = schools.sort_values('average_reading',ascending=False)[['school_name','average_reading']].head(10)
print(best_reading['school_name'])

best_reading_bar = sns.catplot(x='average_reading',y='school_name',data=best_reading,kind='bar',palette='PuRd_r',aspect=5)
best_reading_bar.fig.suptitle('Best Schools based on Reading score')
best_reading_bar.set(xlabel='Reading Score',ylabel='School Name')
plt.tight_layout()
plt.show()

#%% Top 10 schools with best writing results and avg writing score
print(np.mean(schools['average_writing']))
best_wri = schools.sort_values('average_writing',ascending=False)[['school_name','average_writing']].head(10)
print(best_wri['school_name'])

best_wri_bar = sns.catplot(x='average_writing',y='school_name',data=best_wri,kind='bar',palette='PuRd_r',aspect=5)
best_wri_bar.fig.suptitle('Best Schools based on Writing score')
best_wri_bar.set(xlabel='Writing Score',ylabel='School Name')
plt.tight_layout()
plt.show()

#%% Find the top 10 schools with best SAT scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools.sort_values('total_SAT', ascending=False)[['school_name','total_SAT']].head(10)
# print(schools['total_SAT'].mean())
# print(top_10_schools)

# top_10_bar = sns.catplot(x='total_SAT',y='school_name',data=top_10_schools,kind='bar',palette='Blues_r',aspect=5)
# top_10_bar.fig.suptitle('Top 10 schools with highest SAT scores')
# top_10_bar.set(xlabel='Score',ylabel='School Name')
# plt.tight_layout()
# plt.show()

#%% total_SAT distribution

plt.hist(schools['total_SAT'])
plt.show()
plt.title('SAT score distribution')
plt.xlabel('SAT score')
plt.ylabel('Number of schools')

#%% Which borough has the largest std in the combined SAT score
borough_SAT_std = schools.groupby('borough')['total_SAT'].std()
schools['std_SAT'] = round(schools['borough'].map(borough_SAT_std),2)
largest_std = schools.sort_values('std_SAT', ascending=False)[['borough','std_SAT']]
largest_std = largest_std.drop_duplicates(subset='borough')

std = sns.catplot(x='borough',y='std_SAT',data=largest_std,kind='bar',palette='PuRd_r')
std.fig.suptitle('Standard deviation in SAT score by borough')
std.set(xlabel='Borough',y='SAT score STD')
plt.xticks(rotation=90)
plt.show()
