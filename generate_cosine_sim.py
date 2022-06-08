import pandas as pd
import numpy as np
import os
import sys
import time

from requests import head

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import linear_kernel


t0 = time.time()

tfidf = TfidfVectorizer(stop_words='english')
article_data = pd.read_csv('finalproj/data/art_data_new-withtext-desc.csv', dtype = {'article_id': str})
tfidf_matrix = tfidf.fit_transform(article_data['detail_desc'])

# print(f'tfidf_matrix.shape = {tfidf_matrix.shape}') # (105126, 3607)
# print(tfidf.get_feature_names())
# print(tfidf_matrix[0,:])

n_clus=2
kmeans = KMeans(n_clusters=n_clus, random_state=0).fit(tfidf_matrix)
t1=time.time()
print(f'clustertime={t1-t0}')

sample=[[] for i in range(n_clus)]
aid_lookup=[[] for i in range(n_clus)]
idxcount=[0]*n_clus
for i, tfidf_row in enumerate(tfidf_matrix.toarray().tolist()):
    cluster_num = kmeans.labels_.tolist()[i]
    sample[cluster_num].append(tfidf_row)
    aid_lookup[cluster_num].append( (idxcount[cluster_num], article_data['article_id'][i]) ) # sample[clusterX] aid lookup -> (cosine_sim_matrix[clusterX] index, article_id)
    idxcount[cluster_num]+=1

print(f'aid_lookup[0][0:2]: {aid_lookup[1][0:2]}')

from numpy.random import default_rng
for i, s in enumerate(sample):
    t0=time.time()
    print(len(s))
    if len(s)<45000:
        cosine_sim = linear_kernel(s, s) # calculating the dot product between each tfidf vector will directly give the cosine similarity score. 
        print(f'cosine_sim{i}.shape = {cosine_sim.shape}')
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'.npy', cosine_sim)
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'_aidlookup.npy', np.array(aid_lookup[i]))
    elif len(s)>80000:
        sys.exit('one of the clusters is too large, need more clusters?')
    else:
        rng = default_rng()
        sample_indexes = set(rng.choice(len(s), size=40000, replace=False)) # non-repetitive random number
        all_indexes = set(range(len(s)))
        sample_indexes2 = all_indexes.difference(sample_indexes)
        
        tmp_s = []
        tmp_aidlu = []
        for idx, s_idx in enumerate(sample_indexes):
            tmp_s.append(s[s_idx])
            tmp_aidlu.append((idx, aid_lookup[i][s_idx][1]))
        cosine_sim = linear_kernel(tmp_s, tmp_s) 
        print(f'cosine_sim{i}.shape = {cosine_sim.shape}')
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'.npy', cosine_sim)
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'_aidlookup.npy', np.array(tmp_aidlu))

        tmp_s = []
        tmp_aidlu = []
        for idx, s_idx in enumerate(sample_indexes2):
            tmp_s.append(s[s_idx])
            tmp_aidlu.append((idx, aid_lookup[i][s_idx][1]))
        cosine_sim = linear_kernel(tmp_s, tmp_s) 
        print(f'cosine_sim{i}_2.shape = {cosine_sim.shape}')
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'_2.npy', cosine_sim)
        np.save('finalproj/data/cosine_sim/cosine_sim'+str(i)+'_2_aidlookup.npy', np.array(tmp_aidlu))

    
    t1=time.time()
    print(f'linear_kerneltime{i}={t1-t0}')    




print(f'totaltime={time.time()-t0}')