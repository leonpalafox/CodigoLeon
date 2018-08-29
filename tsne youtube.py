import numpy asimport numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.manifold import TSNE

from sklearn.datasets import fetch_mldata 


#leemos la base de datos 

b=pd.read_csv('USvideos.csv',header=0)

print (b.shape)

ba=pd.DataFrame(b)

x=ba.drop(['description','ratings_disabled','video_error_or_removed','thumbnail_link','comments_disabled','tags','publish_time','channel_title','title','video_id','trending_date'],axis=1)

print (x)

X_train , X_test = train_test_split ( x, test_size = 0.05 , random_state = 42 ) 


T_re= TSNE ( n_components = 2 ) .fit_transform ( X_test) 

print (X_embedded .shape)
#aqui es donde sale el error
df_tsne = df.loc[rndperm[:n_sne],:].copy()
#no entiendo q sería  “df. loc" para mi

df_tsne['x-tsne'] = T_re[:,0]
df_tsne['y-tsne'] = T_re[:,1]

chart = ggplot( df_tsne, aes(x='x-tsne', y='y-tsne', color='label') ) \
+ geom_point(size=70,alpha=0.1) \
+ ggtitle("tSNE dimensions colored by digit")
chart
