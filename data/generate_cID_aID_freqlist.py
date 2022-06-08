import pandas as pd
import sys
import time

t0 = time.time()

trans_data2018fall = pd.read_csv('finalproj/data/transactions_train/transactions_train_2018fall.csv', dtype = {'article_id': str})
trans_data2018fall['article_id'] = trans_data2018fall['article_id'].apply(lambda x: x.zfill(10))
print(len(trans_data2018fall.index))
trans_data2019fall = pd.read_csv('finalproj/data/transactions_train/transactions_train_2019fall.csv', dtype = {'article_id': str})
trans_data2019fall['article_id'] = trans_data2019fall['article_id'].apply(lambda x: x.zfill(10))
print(len(trans_data2019fall.index))
trans_data2020summer = pd.read_csv('finalproj/data/transactions_train/transactions_train_2020summer.csv', dtype = {'article_id': str})
trans_data2020summer['article_id'] = trans_data2020summer['article_id'].apply(lambda x: x.zfill(10))
print(len(trans_data2020summer.index))
dfs = [trans_data2018fall, trans_data2019fall, trans_data2020summer]
trans_data = pd.concat(dfs)
print(len(trans_data.index))

customer_totalfreq = trans_data.groupby(['customer_id'])['article_id'].count().reset_index(name='totalfreq')
# print(customer_totalfreq.head(10))

trans_data_freq = trans_data.groupby(['customer_id', 'article_id'])['article_id'].count().reset_index(name='freq')
# print(trans_data_freq.head(10))
trans_data_freq['merged'] = trans_data_freq.apply(lambda row: {'article_id': row['article_id'], 'freq': row['freq']}, axis=1) # wrap single dict in a single element list, now would be treated as an entry rather than iterable?!
# print(trans_data_freq['merged'].head(10))
# print(trans_data_freq['merged'][0])
# print(type(trans_data_freq['merged'][0]))
# print(type(trans_data_freq['merged'])) # pandasSeries !!!!!!!!!!!!!

df = trans_data_freq.groupby('customer_id')['merged'].apply(list).reset_index(name='article_id_freqlist')
# print(df['article_id_freqlist'].head(10))
# print(df['article_id_freqlist'][0][0])
# print(type(df['article_id_freqlist'][0][0]))
# print(type(df['article_id_freqlist'])) # pandasSeries !!!!!!!!!!!!!
df['article_id_freqlist'] = df['article_id_freqlist'].astype('object')
df['totalfreq'] = customer_totalfreq['totalfreq']
print(df.head(10))

df.to_csv('finalproj/data/custID_artID_freqlist_FALL.csv')

print(f'totaltime={time.time-t0}')

sys.exit()






#################################################################################################################


trans_data = pd.read_csv('finalproj/data/transactions_train/transactions_train_2018fall.csv', dtype = {'article_id': str})
trans_data['article_id'] = trans_data['article_id'].apply(lambda x: x.zfill(10))
# print(trans_data.head())


customer_totalfreq = trans_data.groupby(['customer_id'])['article_id'].count().reset_index(name='totalfreq')
# print(customer_totalfreq.head(10))

trans_data_freq = trans_data.groupby(['customer_id', 'article_id'])['article_id'].count().reset_index(name='freq')
# print(trans_data_freq.head(10))
trans_data_freq['merged'] = trans_data_freq.apply(lambda row: {'article_id': row['article_id'], 'freq': row['freq']}, axis=1) # wrap single dict in a single element list, now would be treated as an entry rather than iterable?!
# print(trans_data_freq['merged'].head(10))
# print(trans_data_freq['merged'][0])
# print(type(trans_data_freq['merged'][0]))
# print(type(trans_data_freq['merged'])) # pandasSeries !!!!!!!!!!!!!

df = trans_data_freq.groupby('customer_id')['merged'].apply(list).reset_index(name='article_id_freqlist')
# print(df['article_id_freqlist'].head(10))
# print(df['article_id_freqlist'][0][0])
# print(type(df['article_id_freqlist'][0][0]))
# print(type(df['article_id_freqlist'])) # pandasSeries !!!!!!!!!!!!!
df['article_id_freqlist'] = df['article_id_freqlist'].astype('object')
df['totalfreq'] = customer_totalfreq['totalfreq']
print(df.head(10))

df.to_csv('finalproj/data/custID_artID_freqlist_2018fall.csv')


#################################################################################################################

trans_data = pd.read_csv('finalproj/data/transactions_train/transactions_train_2019fall.csv', dtype = {'article_id': str})
trans_data['article_id'] = trans_data['article_id'].apply(lambda x: x.zfill(10))
# print(trans_data.head())


customer_totalfreq = trans_data.groupby(['customer_id'])['article_id'].count().reset_index(name='totalfreq')
# print(customer_totalfreq.head(10))

trans_data_freq = trans_data.groupby(['customer_id', 'article_id'])['article_id'].count().reset_index(name='freq')
# print(trans_data_freq.head(10))
trans_data_freq['merged'] = trans_data_freq.apply(lambda row: {'article_id': row['article_id'], 'freq': row['freq']}, axis=1)
# print(trans_data_freq.head(10))

df = trans_data_freq.groupby('customer_id')['merged'].apply(list).reset_index(name='article_id_freqlist')
df['article_id_freqlist'] = df['article_id_freqlist'].astype('object')
df['totalfreq'] = customer_totalfreq['totalfreq']
print(df.head(20))

df.to_csv('finalproj/data/custID_artID_freqlist_2019fall.csv')


#################################################################################################################

trans_data = pd.read_csv('finalproj/data/transactions_train/transactions_train_2020summer.csv', dtype = {'article_id': str})
trans_data['article_id'] = trans_data['article_id'].apply(lambda x: x.zfill(10))
# print(trans_data.head())


customer_totalfreq = trans_data.groupby(['customer_id'])['article_id'].count().reset_index(name='totalfreq')
# print(customer_totalfreq.head(10))

trans_data_freq = trans_data.groupby(['customer_id', 'article_id'])['article_id'].count().reset_index(name='freq')
# print(trans_data_freq.head(10))
trans_data_freq['merged'] = trans_data_freq.apply(lambda row: {'article_id': row['article_id'], 'freq': row['freq']}, axis=1)
# print(trans_data_freq.head(10))

df = trans_data_freq.groupby('customer_id')['merged'].apply(list).reset_index(name='article_id_freqlist')
df['article_id_freqlist'] = df['article_id_freqlist'].astype('object')
df['totalfreq'] = customer_totalfreq['totalfreq']
print(df.head(20))

df.to_csv('finalproj/data/custID_artID_freqlist_2020summer.csv')


