import pandas as pd
import sys
import time
import numpy as np

t0 = time.time()

# all fall transactions
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




# generate top N seasonal aIDs

N = 12 # top N seasonal aIDs
aID_totalfreq = pd.DataFrame(columns=['totalfreq'])
aID_totalfreq['totalfreq'] = trans_data.groupby(['article_id'])['article_id'].count()
aID_totalfreq_sorted = aID_totalfreq.sort_values('totalfreq', ascending=False)
print(f'{np.array(list(aID_totalfreq_sorted.head(12).index))}')
np.save('finalproj/data/top12_aID_fall.npy', np.array(list(aID_totalfreq_sorted.head(12).index)))
# aID_totalfreq_sorted.head(12).to_csv('aID_totalfreq_top12.csv')

print(f'totaltime = {time.time()-t0}')