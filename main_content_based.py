import enum
import os
import sys
import time
import pandas as pd
import numpy as np
import ast


# from requests import head

t0 = time.time()
##########################################
print('load data...')
cosine_sim0 = np.load('finalproj/data/cosine_sim/cosine_sim0.npy')
cosine_sim0_lu = pd.DataFrame(np.load('finalproj/data/cosine_sim/cosine_sim0_aidlookup.npy'), columns=['idx', 'article_id'])

cosine_sim1 = np.load('finalproj/data/cosine_sim/cosine_sim0_2.npy')
cosine_sim1_lu = pd.DataFrame(np.load('finalproj/data/cosine_sim/cosine_sim0_2_aidlookup.npy'), columns=['idx', 'article_id'])

cosine_sim2 = np.load('finalproj/data/cosine_sim/cosine_sim1.npy')
cosine_sim2_lu = pd.DataFrame(np.load('finalproj/data/cosine_sim/cosine_sim1_aidlookup.npy'), columns=['idx', 'article_id'])


cID_aID_freqlist = pd.read_csv('finalproj/data/custID_artID_freqlist_FALL.csv', dtype = {'customer_id': str, 'article_id_freqlist': object, 'totalfreq': int})
print(f'len of cID_aID_freqlist: {len(cID_aID_freqlist.index)}')

# cID_aID_freqlist['article_id_freqlist'] = cID_aID_freqlist['article_id_freqlist'].apply(lambda x: ast.literal_eval(x))

top12_aID_fall = np.load('finalproj/data/top12_aID_fall.npy')

samplesubmit_data = pd.read_csv('finalproj/data/sample_submission.csv', dtype = {'customer_id': str}) # 1371980 cIDs
print(f'finish data loading, time={time.time()-t0}')






recommendation_list = []
total_recomms = 12
total_rows = len(samplesubmit_data.index)
time_start_recommendation = time.time()
missing_articleIDs = [] # .....why?????

fallcustomer_count = 0
nonfallcustomer_count = 0 

#####################################################################################
# for s_idx, sample_cID in enumerate(samplesubmit_data['customer_id']):
#     if s_idx < 50:
#         print(f'###########################\nsampleCID = {sample_cID}, s_idx={s_idx}')
#         if sample_cID in set(cID_aID_freqlist['customer_id']):
#             selected_row = cID_aID_freqlist[cID_aID_freqlist['customer_id']==sample_cID].values[0]
#             print(type(selected_row))
#             print(selected_row)
#             print('selected_row[0] = ')
#             print(type(selected_row[0]))
#             print(selected_row[0])
#             print('selected_row[1] = ')
#             print(type(selected_row[1]))
#             print(selected_row[1])
#             print('selected_row[2] = ')
#             print(type(selected_row[2]))
#             print(selected_row[2])
#             print('ast.literal_eval(selected_row[2]) =')
#             print(type((ast.literal_eval(selected_row[2]))[0]))
#             print((ast.literal_eval(selected_row[2]))[0])
#             print(f'######################################################\n')
            
#####################################################################################




for s_idx, sample_cID in enumerate(samplesubmit_data['customer_id']):
    if sample_cID in set(cID_aID_freqlist['customer_id']):
        fallcustomer_count+=1
        selected_row = cID_aID_freqlist[cID_aID_freqlist['customer_id']==sample_cID].values[0]
        assert selected_row[1]==sample_cID
        
        cid, aif_list, totalfreq = selected_row[1], ast.literal_eval(selected_row[2]), selected_row[3] # because aif_list is object type, it has one more list bracket on the outside?????
        rlist = []

        aif_list_sorted = sorted(aif_list, key=lambda d: d['freq'], reverse=True) # sorted by freq
        for aif_idx, aif in enumerate(aif_list_sorted): # aif is dictionary(aid: freq)
            aid = aif['article_id']
            freq = aif['freq']
            # loopthrough all cosine_sim_lu
            if aid in cosine_sim0_lu['article_id'].tolist():            
                idx = cosine_sim0_lu.index[cosine_sim0_lu['article_id']==aid].astype(int)
                similarity_vec = cosine_sim0[idx][0]
                similarity_vec_idx_sorted = sorted(range(len(similarity_vec)), key=lambda k: similarity_vec[k], reverse=True) # large to small
                
                if aif_idx==len(aif_list_sorted)-1:
                    recommend_count = total_recomms - len(rlist)
                else:
                    recommend_count = int(total_recomms * freq/totalfreq)
                for cnt in range(recommend_count):
                    try:
                        if similarity_vec[similarity_vec_idx_sorted[cnt+1]] != 0: 
                            rec_aID = cosine_sim0_lu['article_id'][similarity_vec_idx_sorted[cnt+1]]
                            rlist.append(rec_aID)
                    except Exception as e:
                        print(f'Error at cossim0: {e}')
                        print(f'similarity_vec = {similarity_vec}')
                        sys.exit(f'cnt={cnt}, \n similarity_vec_idx_sorted={similarity_vec_idx_sorted} \n time={time.time()-t0}')
                
            elif aid in cosine_sim1_lu['article_id'].tolist():
                idx = cosine_sim1_lu.index[cosine_sim1_lu['article_id']==aid].astype(int)
                similarity_vec = cosine_sim1[idx][0]
                similarity_vec_idx_sorted = sorted(range(len(similarity_vec)), key=lambda k: similarity_vec[k], reverse=True) # large to small
                
                if aif_idx==len(aif_list_sorted)-1:
                    recommend_count = total_recomms - len(rlist)
                else:
                    recommend_count = int(total_recomms * freq/totalfreq)
                for cnt in range(recommend_count):
                    try:
                        if similarity_vec[similarity_vec_idx_sorted[cnt+1]] != 0: 
                            rec_aID = cosine_sim1_lu['article_id'][similarity_vec_idx_sorted[cnt+1]]
                            rlist.append(rec_aID)
                    except Exception as e:
                        print(f'Error at cossim1: {e}')
                        print(f'similarity_vec = {similarity_vec}')
                        sys.exit(f'cnt={cnt}, \n similarity_vec_idx_sorted={similarity_vec_idx_sorted} \n time={time.time()-t0}')
                
            elif aid in cosine_sim2_lu['article_id'].tolist():            
                # .index[] outputs index "list", and the type is "non-numerical" ??
                idx = cosine_sim2_lu.index[cosine_sim2_lu['article_id']==aid].astype(int) # non-numerical index of the article_id that correspond with the similarity matrix
                similarity_vec = cosine_sim2[idx][0] # Get the similarity vector of aid.  
                # for the next line of code:
                # idx(where all indexes can be generated by range(len(sim_vec))) that later corresponds to the actual article_id(by lookup table) is sorted using sim_vec[idx] value from large to small. 
                # len(sim_vec) is just the amount of all article_ids
                similarity_vec_idx_sorted = sorted(range(len(similarity_vec)), key=lambda k: similarity_vec[k], reverse=True)
                
                if aif_idx==len(aif_list_sorted)-1:
                    recommend_count = total_recomms - len(rlist)
                else:
                    recommend_count = int(total_recomms * freq/totalfreq)
                for cnt in range(recommend_count):
                    try:
                        if similarity_vec[similarity_vec_idx_sorted[cnt+1]] != 0: # cnt+1 because the first one is itselfm of course has highest similarity. 
                            rec_aID = cosine_sim2_lu['article_id'][similarity_vec_idx_sorted[cnt+1]] # get the recommendation aID corresponding to the similarity
                            rlist.append(rec_aID)
                    except Exception as e:
                        print(f'Error at cossim2: {e}')
                        print(f'similarity_vec = {similarity_vec}')
                        sys.exit(f'cnt={cnt}, \n similarity_vec_idx_sorted={similarity_vec_idx_sorted} \n time={time.time()-t0}')
                
            else:
                missing_articleIDs.append(aid)
                # sys.exit(f'never seen article_id {aid} in any of the cosine similarity matrices \n timespent: {time.time()-t0}')
        
        # start filling up if recommendation count is less than total_recomms. Fill it up using the top12 aIDs of fall
        if len(rlist)<total_recomms:
            for fillerID in top12_aID_fall: 
                if fillerID not in rlist:
                    rlist.append(fillerID)

        recommendation_list.append(rlist)

        if s_idx in range(10) or s_idx%1000==0: # first 10 rows or every 10 rows
            print(f'{s_idx}:  {cid} -> {rlist}')
            
            time_spent = time.time()-time_start_recommendation
            rows_remain_count = total_rows - (s_idx + 1)
            print(f'recommending time spent: {time_spent}')
            print(f'{rows_remain_count} rows left \n estimated recommending time remain: {time_spent/(s_idx+1)*rows_remain_count}')
            
            df_result_tmp = pd.DataFrame({'customer_id': samplesubmit_data['customer_id'][0:s_idx+1] , 'recommendation': recommendation_list})
            print(df_result_tmp.tail(min(s_idx+1,10)))

            print(f'missing_articleIDs: len={len(missing_articleIDs)}\n{missing_articleIDs}')

        if s_idx==1000 or (s_idx%20000==0 and s_idx>0):
            print(f'fallcustomer_count={fallcustomer_count}, \nnonfallcustomer_count={nonfallcustomer_count}')
            df_result_tmp = pd.DataFrame({'customer_id': samplesubmit_data['customer_id'][0:s_idx+1], 'recommendation': recommendation_list})
            print(df_result_tmp.head(20))
            df_result_tmp.to_csv(f'results/result{s_idx}.csv')
    else:
        nonfallcustomer_count+=1
        recommendation_list.append(top12_aID_fall.tolist())



print(f'fallcustomer_count={fallcustomer_count}, \fnonfallcustomer_count={nonfallcustomer_count}')
df_result = pd.DataFrame({'customer_id': samplesubmit_data['customer_id'], 'recommendation': recommendation_list})
print(df_result.head(20))
df_result.to_csv('results/result.csv')
np.save('results/missing_articleIDs.npy', np.array(missing_articleIDs))















##########################################
print(f'totaltime={time.time()-t0}')









# trash that might be useful

# for index, (cid, aif_list, totalfreq) in enumerate(zip(cID_aID_freqlist['customer_id'], cID_aID_freqlist['article_id_freqlist'], cID_aID_freqlist['totalfreq'])):
    # # for index, row in cID_aID_freqlist.iterrows():
    #     # cid, aif_list, totalfreq = row[1], row[2], row[3] # row[0] is the rowID.....ok to row['article_id_freqlist']?
    #     # print(f'cid{type(cid)} \n aiflist {type(aif_list)} \n aiflist[0] {type(aif_list[0])} \n totalfreq{type(totalfreq)}')