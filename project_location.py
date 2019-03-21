#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'my_project1'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
from function_creation import draw_chart,draw_chart2, print_label, calc_means, calc_sems, count_sample


#%%
df2 = pd.read_csv("FANG_plus.csv", encoding="utf-8")


#%%
#remove all the 'none' value of rows from the 'location' variable--total 42441 left
#df2['location'].value_counts()
df2_1=df2[df2['location']!='none']
df2_1.head()
#df2_1['location'].value_counts() # none 25085 are removed--total 42441


#%%
#separate the location by ','
c= df2_1['location'].str.split( ",", expand=True)
df2_1['city']=c[0]
df2_1['state']=c[1]

df3_1=df2_1[['0','location','city','state']]
df3_1['co1']='USA'

e1=df2_1['state'].str.replace('(',',').str.replace(')','')
e= e1.str.split( ",", expand=True)
df3_1['state']=e[0]
df3_1['co2']=e[1]
df3_1.loc[df3_1['co2']==e[1],'co1']='no usa'


d1=df2_1['city'].str.replace('(',',').str.replace(')','')
d= d1.str.split( ",", expand=True)
df3_1['city']=d[0]
df3_1['co3']=d[1]
df3_1.loc[df3_1['co3']==d[1],'co1']='no usa'

df3_a=df3_1[df3_1['co1']=='USA'].rename(columns={'co1':'country'})

#df3=df3_1.replace('None','')
df3_1['co2'].fillna("No co2", inplace = True)
df3_1['co3'].fillna("No co3", inplace = True)
df3_b=df3_1[df3_1['co2']!='No co2'].rename(columns={'co2':'country'})
df3_c=df3_1[df3_1['co3']!='No co3'].rename(columns={'co3':'country'})

result1 = df3_a.append([df3_b, df3_c])
result=result1.drop(['co1','co2','co3'], axis=1)
result

df_locn = pd.merge(df2_1, result, on="0",how="outer").drop(['state_y','city_y','location_y'],axis=1)
df_locn=df_locn.rename(columns={'location_x':'location', 'city_x':'city','state_x':'state' })
df_locn=df_locn[['0','company', 'location','city','state','country','year','status','position',                 'overall','wk_bal','culture_val','career_opp','comp_benefit','Sr_mgmt']]


df_locn.to_csv('location_data.csv', encoding="utf-8")
df_locn


#%%



