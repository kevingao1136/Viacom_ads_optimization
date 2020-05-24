# Import Libraries
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.cluster import KMeans

# Import the CPM data
cpm = pd.read_csv('data/cpm_estimates-15Apr19.csv')

# test

# Preprocess the CPM data for predictive modeling
def clean_cpm_modeling(data=cpm):

    '''
    1. Convert the age_max column to 'int' datatype by replacing '65+' with 65
    2. Impute missing CPM with median
    3. Extract time features such as year and month into dataset
    4. Reduce dataset to only have predictor features
    '''

    data['age_max'].replace({'65+':'65'},inplace=True)
    data['age_max'] = data['age_max'].astype('int')
    data['cpm'].replace({0:np.nan},inplace=True)
    data['cpm'].fillna(value=data['cpm'].median(),inplace=True)

    # Extract time features
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data.date.dt.year
    data['month'] = data.date.dt.month
    data['day'] = data.date.dt.day
    data['dayofyear'] = data.date.dt.dayofyear
    data['weekofyear'] = data.date.dt.week
    data = data[['age_min','age_max','female','male','year','month','day','dayofyear','weekofyear','cpm']]

    return data

# Define input_cols as input variables for both cpm data and page_level imputation data
cpm = clean_cpm_modeling()
input_cols = cpm.drop('cpm',axis=1).columns

# Create a Random Forest model
X, y = cpm[input_cols], cpm['cpm']
rfr = RandomForestRegressor(n_estimators = 50)
rfr.fit(X,y)

# Run cross validations
scores = cross_val_score(rfr, X, y, cv=5, scoring='r2')
print('cross validation scores are:', scores)

# Import the page level data for age gender unique
files = [i for i in os.listdir('data') if 'csv' in i and 'sample' not in i and i.startswith('page')]

# Concatenate all the imported data from the iteration
page_level = pd.DataFrame()
for file in files:
    temp = pd.read_csv('data/'+file)
    page_level = pd.concat([page_level,temp])

# Filter the page level data to only include those with demographic features
page_demo = page_level[page_level['name'] == 'page_impressions_by_age_gender_unique'].copy()
page_demo['date'] = pd.to_datetime(page_demo['date'])

# Reduce the page_level data to have hIDs that have demographic features for later pipelining
print(f'page_demo has {page_demo.hID.nunique()} unique hIDs')
print(f'page_level has {page_level.hID.nunique()} unique hIDs')
page_level = page_level[page_level.hID.isin(page_demo.hID.unique())]

# Prepare the data for the predictions
def clean_page_demo(data=page_demo):

    '''
    1. Extract the demographic information such as age and gender
    2. Extract time features such as year and month
    3. Match the feature to the random forest model inputs
    '''
    data['age_group'] = [i[2:] for i in data['metric']]
    data['age_group'].replace({'65+':'65-85'},inplace=True)
    data['age_min'] = [i[:2] for i in data['age_group']]
    data['age_max'] = [i[-2:] for i in data['age_group']]
    data['female'] = [1 if i[0] == 'F' or i[0] == 'U' else 0 for i in data['metric']]
    data['male'] = [1 if i[0] == 'M' or i[0] == 'U' else 0 for i in data['metric']]
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['dayofyear'] = data['date'].dt.dayofyear
    data['weekofyear'] = data['date'].dt.weekofyear

    return data

page_demo = clean_page_demo()

# Impute page_demo with CPM
page_demo['CPM'] = rfr.predict(page_demo[input_cols])
page_demo = page_demo[['date','metric','value','hID','CPM']]


# Prepare pivot table for clustering
page_pivot = page_level.pivot_table(index=['hID'],columns='name',values='value')
page_pivot.fillna(0,inplace=True)

# Cluster the page level data for further insights
kmeans = KMeans(n_clusters=3, random_state=42)
page_pivot['cluster'] = kmeans.fit_predict(page_pivot)
page_pivot['cluster'] = [i+1 for i in page_pivot.cluster]
cluster1 = page_pivot[page_pivot.cluster == 1]
cluster2 = page_pivot[page_pivot.cluster == 2]
cluster3 = page_pivot[page_pivot.cluster == 3]
print("Cluster 1 has",len(cluster1),"hIDs")
print("Cluster 2 has",len(cluster2),"hIDs")
print("Cluster 3 has",len(cluster3),"hIDs")

# The first data output to Tableau Dashboard
# Mean values by clusters
cluster_avg = pd.concat([pd.DataFrame(cluster1.mean()).T, pd.DataFrame(cluster2.mean()).T, pd.DataFrame(cluster3.mean()).T])
cluster_avg.index = ['cluster1','cluster2','cluster3']
cluster_avg.drop('cluster',axis=1,inplace=True)
cluster_avg.reset_index(inplace=True)
cluster_avg.rename({'index':'cluster'},axis=1,inplace=True)
#cluster_avg.to_csv('tableau_data/cluster_avg.csv')


# The second data output to Tableau Dashboard
# page conversions
page_conversion = pd.DataFrame()
page_conversion['Impressions to CTA'] = page_pivot['page_cta_clicks_logged_in_total']/page_pivot['page_impressions']
page_conversion['Impressions to Views'] = page_pivot['page_views']/page_pivot['page_impressions']
page_conversion['Views to CTA'] = page_pivot['page_cta_clicks_logged_in_total']/page_pivot['page_views']
#page_conversion.to_csv('tableau_data/page_conversion.csv')

# 3. The third data output to Tableau Dashboard
# page_demo.to_csv('tableau_data/page_demo.csv')
