import pandas as pd

df = pd.read_csv('articles.csv', dtype = {'article_id': str})
df1 = df.iloc[:,[0,-1]].dropna()
print(f'type(df1[0,1])={type(df1.iloc[0,0])}')
print(f'nrow={df1.shape[0]}')
cnt=0
for i, data in df1.iterrows():
    if not isinstance(data[0], str) or not isinstance(data[1], str):
        print(f'{data}')
        cnt+=1
        df1.drop([i], axis=0)

print(f'cnt={cnt}')

print(df1.head())
df1.to_csv('articles_onlyid_desc.csv')

df_articles_withtext = pd.read_csv('art_data_new-withtext.csv', dtype = {'article_id': str})
df_artilces_withtext_desc = pd.merge(df_articles_withtext, df1, on="article_id")
df_artilces_withtext_desc.to_csv('art_data_new-withtext-desc.csv')
print(df_artilces_withtext_desc.head()) # 105126



df_artilces_withtext_desc = pd.read_csv('art_data_new-withtext-desc.csv', dtype = {'article_id': str})
mydata_ct = pd.read_csv('mydata_ct.csv', dtype = {'article_id': str})

mydata = pd.merge(df_artilces_withtext_desc, mydata_ct, on="article_id")
mydata.to_csv('finaldata.csv')