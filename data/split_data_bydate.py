import pandas as pd
import os
import pathlib
import time

print(pathlib.Path(__file__).parent.resolve())
t0 = time.time()
# #####################split by date########################
transactions_train = pd.read_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train.csv', dtype = {'article_id': str})
transactions_train['article_id'] = transactions_train['article_id'].apply(lambda x: x.zfill(10))
# 2018
transactions_train_2018fall = transactions_train[(transactions_train['t_dat'] >= '2018-09-18') & (transactions_train['t_dat'] <= '2018-11-30')]
transactions_train_2018fall.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2018fall.csv')
print(transactions_train_2018fall.head())

transactions_train_2018winter = transactions_train[(transactions_train['t_dat'] > '2018-11-30') & (transactions_train['t_dat'] <= '2019-02-28')]
transactions_train_2018winter.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2018winter.csv')
print(transactions_train_2018winter.head())

# 2019
transactions_train_2019spring = transactions_train[(transactions_train['t_dat'] > '2019-02-28') & (transactions_train['t_dat'] <= '2019-05-31')]
transactions_train_2019spring.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2019spring.csv')
print(transactions_train_2019spring.head())

transactions_train_2019summer = transactions_train[(transactions_train['t_dat'] > '2019-05-31') & (transactions_train['t_dat'] <= '2019-08-31')]
transactions_train_2019summer.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2019summer.csv')
print(transactions_train_2019summer.head())

transactions_train_2019fall = transactions_train[(transactions_train['t_dat'] > '2019-08-31') & (transactions_train['t_dat'] <= '2019-11-30')]
transactions_train_2019fall.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2019fall.csv')
print(transactions_train_2019fall.head())

transactions_train_2019winter = transactions_train[(transactions_train['t_dat'] > '2019-11-30') & (transactions_train['t_dat'] <= '2020-02-29')]
transactions_train_2019winter.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2019winter.csv')
print(transactions_train_2019winter.head())

# 2020
transactions_train_2020spring = transactions_train[(transactions_train['t_dat'] > '2020-02-28') & (transactions_train['t_dat'] <= '2020-05-31')]
transactions_train_2020spring.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2020spring.csv')
print(transactions_train_2020spring.head())

transactions_train_2020summer = transactions_train[(transactions_train['t_dat'] > '2020-05-31') & (transactions_train['t_dat'] <= '2020-09-21')] # end of data, so its 2020-09-21
transactions_train_2020summer.to_csv(R'C:\Users\joe_c\OneDrive - Indiana University\Documents\ABROAD_INDIANA\2022Spring\DataMining\FinalProj\finalproj\data\transactions_train/transactions_train_2020summer.csv')
print(transactions_train_2020summer.head())

# #############################################...


# # #####################split by date########################
# finaldata = pd.read_csv('finaldata.csv')

# # 2018
# finaldata_2018fall = finaldata[(finaldata['t_dat'] >= '2018-09-18') & (finaldata['t_dat'] <= '2018-11-30')]
# finaldata_2018fall.to_csv('finaldata/finaldata_2018fall.csv')
# print(finaldata_2018fall.head())

# finaldata_2018winter = finaldata[(finaldata['t_dat'] > '2018-11-30') & (finaldata['t_dat'] <= '2019-02-28')]
# finaldata_2018winter.to_csv('finaldata/finaldata_2018winter.csv')
# print(finaldata_2018winter.head())

# # 2019
# finaldata_2019spring = finaldata[(finaldata['t_dat'] > '2019-02-28') & (finaldata['t_dat'] <= '2019-05-31')]
# finaldata_2019spring.to_csv('finaldata/finaldata_2019spring.csv')
# print(finaldata_2019spring.head())

# finaldata_2019summer = finaldata[(finaldata['t_dat'] > '2019-05-31') & (finaldata['t_dat'] <= '2019-08-31')]
# finaldata_2019summer.to_csv('finaldata/finaldata_2019summer.csv')
# print(finaldata_2019summer.head())

# finaldata_2019fall = finaldata[(finaldata['t_dat'] > '2019-08-31') & (finaldata['t_dat'] <= '2019-11-30')]
# finaldata_2019fall.to_csv('finaldata/finaldata_2019fall.csv')
# print(finaldata_2019fall.head())

# finaldata_2019winter = finaldata[(finaldata['t_dat'] > '2019-11-30') & (finaldata['t_dat'] <= '2020-02-29')]
# finaldata_2019winter.to_csv('finaldata/finaldata_2019winter.csv')
# print(finaldata_2019winter.head())

# # 2020
# finaldata_2020spring = finaldata[(finaldata['t_dat'] > '2020-02-28') & (finaldata['t_dat'] <= '2020-05-31')]
# finaldata_2020spring.to_csv('finaldata/finaldata_2020spring.csv')
# print(finaldata_2020spring.head())

# finaldata_2020summer = finaldata[(finaldata['t_dat'] > '2020-05-31') & (finaldata['t_dat'] <= '2020-09-21')] # end of data, so its 2020-09-21
# finaldata_2020summer.to_csv('finaldata/finaldata_2020summer.csv')
# print(finaldata_2020summer.head())

# # #############################################...1170sec

print(f'time: {time.time()-t0}')