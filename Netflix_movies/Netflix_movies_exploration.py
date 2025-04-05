import numpy as np
import pandas as pd
import os
os.chdir(r'F:\Data Projects')
netflix_df = pd.read_csv('netflix_data.csv')

if __name__ == '__main__':
    # find the most frequent movie duration
    mask = np.logical_and(netflix_df['release_year']>=1990, netflix_df['release_year']<=1999)
    duration = netflix_df[mask]['duration'].value_counts().idxmax()
    print(f'The most frequent movie duration in the 1990s is {duration}')
    
    # find the number of short action movies, whose duration <90 minutes
    filter1 = np.logical_and(mask, np.logical_and(netflix_df['type']=='Movie', netflix_df['genre']=='Action'))
    short_action_movie = netflix_df[np.logical_and(filter1, netflix_df['duration']<90)]
    short_movie_count = len(short_action_movie)
    print(f'The number of short movies is {short_movie_count}')