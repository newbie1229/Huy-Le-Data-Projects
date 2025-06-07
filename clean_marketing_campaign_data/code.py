import os
os.chdir(r'F:\Data Courses\DataCamp\Data Engineer\Data Engineer in Python\Project - Cleaning Bank Marketing Campaign Data')
import pandas as pd
import numpy as np
data = pd.read_csv('bank_marketing.csv')
# print(data['campaign_outcome'])

#%% client
client = data[['client_id','age','job','marital','education','credit_default','mortgage']]
print(client['mortgage'].unique())
# job
client['job'] = client['job'].str.replace('.','_')
# print(client['job'].head(15))

# education
client['education'] = client['education'].str.replace('.','_')
client.loc[client['education']=='unknown','education'] = np.nan

# credit default
client.loc[client['credit_default']=='yes','credit_default'] = 1
client.loc[client['credit_default'].isin(['no','unknown']),'credit_default'] = 0
client['credit_default'] = client['credit_default'].astype('bool')
# print(client['credit_default'])
# mortgage
client.loc[client['mortgage']=='yes','mortgage'] = 1
client.loc[client['mortgage'].isin(['unknown','no']),'mortgage'] = 0
# print(client['mortgage'].unique())
client['mortgage'] = client['mortgage'].astype('bool')
client.to_csv('client.csv', index=False)

#%% campaign
campaign = data[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']]
campaign.loc[campaign['previous_outcome']=='success','previous_outcome']=1
campaign.loc[campaign['previous_outcome'].isin(['nonexistent','failure']),'previous_outcome']=0
campaign['previous_outcome'] = campaign['previous_outcome'].astype('bool')
# print(campaign['previous_outcome'].unique())

campaign.loc[campaign['campaign_outcome']=='yes','campaign_outcome']=1
campaign.loc[campaign['campaign_outcome']=='no','campaign_outcome']=0
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype('bool')
# print(campaign['campaign_outcome'].unique())

data['year'] = '2022'
mapping = {'may':5,'jun':6,'jul':7,'aug':8,'oct':10,'nov':11,'dec':12,'mar':3,'apr':4,'sep':9}
data['month'] = data['month'].replace(mapping)
campaign['last_contact_date'] = pd.to_datetime(data['year'] + '-' + data['month'].astype('str') + '-' + data['day'].astype('str'))
campaign.to_csv('campaign.csv',index=False)

#%% economics
economics = data[['client_id','cons_price_idx','euribor_three_months']]
economics.to_csv('economics.csv',index=False)