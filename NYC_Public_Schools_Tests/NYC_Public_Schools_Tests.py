import os 
import pandas as pd
os.chdir(r'F:\Huy-Le-Data-Projects\NYC_Public_Schools_Tests')
schools = pd.read_csv('schools.csv')

if __name__ == '__main__':
    # Find the schools with best math results
    math_tmp = schools[schools['average_math']>=800*0.8][['school_name','average_math']]
    best_math_schools = math_tmp.sort_values('average_math', ascending=False)
    print('Schools with best math results')
    print(best_math_schools)
    
    # Find the top 10 schools with best SAT scores
    schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
    top_10_schools = schools.sort_values('total_SAT', ascending=False)[['school_name','total_SAT']].head(10)
    print()
    print('Top 10 performing schools based on total SAT scores')
    print(top_10_schools)
    # get the first 10 rows: head(10) or .iloc[:10]
    
    # Which borough has the largest std in the combined SAT score
    schools['num_schools'] = schools['borough'].map(schools['borough'].value_counts())
    # must use map, since groupby will create a Series hence column num_schools will have NaN values
    borough_avg_sat = schools.groupby('borough')['total_SAT'].mean()
    schools['average_SAT'] = round(schools['borough'].map(borough_avg_sat),2)
    # map a Series into a DataFrame
    borough_SAT_std = schools.groupby('borough')['total_SAT'].std()
    schools['std_SAT'] = round(schools['borough'].map(borough_SAT_std),2)
    largest_std_dev = schools.sort_values('std_SAT', ascending=False)[['borough','num_schools','average_SAT','std_SAT']].head(1)
    print()
    print('The borough with the largest standard deviation in the combined SAT score')
    print(largest_std_dev)
    
'''
Key takeaway: can't create a new column using groupby, since groupby returns
a Series
Must use map instead 
'''