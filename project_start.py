
#%%
import pandas as pd
from function_creation import draw_chart,draw_chart2, print_label, calc_means, calc_sems, count_sample


#%%
#read, select, and rename the columns
df = pd.read_csv("employee_reviews.csv",encoding="utf-8")
df=df[['Unnamed: 0','company', 'location','dates','job-title','overall-ratings','work-balance-stars','culture-values-stars','carrer-opportunities-stars','comp-benefit-stars','senior-mangemnet-stars']]
df=df.rename(columns={'Unnamed: 0':'0','job-title':'title','overall-ratings':'overall', 'work-balance-stars':'wk_bal','culture-values-stars':'culture_val','carrer-opportunities-stars':'career_opp','comp-benefit-stars':'comp_benefit', 'senior-mangemnet-stars':'Sr_mgmt'})
df.head()

#%% [markdown]
# ####   <'dates' column> 
# #####    i)  clean, split, and keep only the 'year' of 'dates' column
# #####    ii) clean the non-valid data of the 'year' column-- dropped :  '0000's & 'None', total (67526)

#%%
# clean, split, and keep only the year of 'dates' column
df['overall'].value_counts()
df['dates'].dropna(inplace = True) 
df[['date','year']]=df['dates'].str.split( ", ", expand=True)
df1=df.drop(['dates','date'], axis=1)

df1=df1[df1['year'] != '0000'] 
df1=df1[df1['year'] !=  None]  

#df1.head() 

#%% [markdown]
# #####   <'title' coulmn>  :total (67529)
# #####  i) 'status': Current Emplyee (42540), Former Employee (24989)
# #####  ii) "position' : Anonymous Emplyee (27002)

#%%
# split the 'title' column into 'status' and 'position' columns
# drop the 'title' column
a= df1['title'].str.split( " - ", expand=True)
df1['status']=a[0]
df1['position']=a[1]
df2=df1.drop(['title'], axis=1)
df2.head()


#%%
#  reorder the columns (dropped '0' column)
df2=df2[['0','company', 'location','year','status','position','overall',         'wk_bal','culture_val','career_opp','comp_benefit','Sr_mgmt']]
df2.to_csv("FANG_plus.csv", encoding="utf-8", index=False)# 'overall' column is the only float64
df2.head()

#%% [markdown]
# ##  a) work_balance_ratings
#%% [markdown]
# #####  final sample size (60366) after removal of 'none' (7160) 

#%%
df_a=df2[df2['wk_bal'] !='none'] #7160 counts of 'none'
df_a["wk_bal"] = pd.to_numeric(df_a['wk_bal'], errors='coerce')# do not fill the NaN  with 0's

#df_a['wk_bal'].dtype
#df_a.dtypes
#df_a["wk_bal"].unique()


#%%
# count the sample by company
count_sample(df_a, 'wk_bal')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart(calc_means(df_a, 'wk_bal'), calc_sems(df_a, 'wk_bal'))
print_label("Work Balance Ratings")

#%% [markdown]
# ##   b)  Culture_value ratings
#%% [markdown]
# #####  i) final sample size (53980) after removal of 'none' (13546)
# #####  ii) no data in 2008-2011

#%%
df_b=df2[df2['culture_val'] !='none'] # 13546 counts of 'none'
df_b['culture_val'] = pd.to_numeric(df_b['culture_val'], errors='coerce') # do not fill the NaN  with 0's

#df2[df2['culture_val'] =='none'].count()
#df_b['culture_val'].value_counts()
 #5.0    21536
 #4.0    13683
 #3.0     9192
 #1.0     4839
 #2.0     4730


#%%
# count the samples by company
count_sample(df_b, 'culture_val')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart2(calc_means(df_b, 'culture_val'), calc_sems(df_b, 'culture_val'))
print_label("Culture Value Ratings")

#%% [markdown]
# ##   c) Career-opportunity ratings
#%% [markdown]
# #####    final sample size (60418) after removal of 'none' (7108)

#%%
df_c=df2[df2['career_opp'] !='none'] # 7108 counts of 'none'
df_c['career_opp'] = pd.to_numeric(df_c['career_opp'], errors='coerce') # do not fill the NaN  with 0's


#%%
# count the samples by company
count_sample(df_c, 'career_opp')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart(calc_means(df_c, 'career_opp'), calc_sems(df_c, 'career_opp'))
print_label("Career Opportunity Ratings")

#%% [markdown]
# ##  d) comp_benefit Ratings
#%% [markdown]
# ##### final sample size (60365) after removal of 'none' (7161)

#%%
df_d=df2[df2['comp_benefit'] !='none'] #7161 counts of 'none'
df_d['comp_benefit'] = pd.to_numeric(df_d['comp_benefit'], errors='coerce') # do not fill the NaN  with 0's


#%%
# count the samples by company
count_sample(df_d, 'comp_benefit')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart(calc_means(df_d, 'comp_benefit'), calc_sems(df_d, 'comp_benefit'))
print_label("Comp benefit Ratings")

#%% [markdown]
# ##   e) Senior Management Ratings
#%% [markdown]
# ##### final sample size (59751) after removal of 'none' (7775)

#%%
df_e=df2[df2['Sr_mgmt'] !='none'] # 7775 counts of 'none'
df_e['Sr_mgmt'] = pd.to_numeric(df_e['Sr_mgmt'], errors='coerce') # do not fill the NaN  with 0's


#%%
# count the samples by company
count_sample(df_e, 'Sr_mgmt')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart(calc_means(df_e, 'Sr_mgmt'), calc_sems(df_e, 'Sr_mgmt'))
print_label("Senior Management Ratings")

#%% [markdown]
# ##   f) Overall Ratings
#%% [markdown]
# #####  final size (67526) -- originally float64 type with 0 'none' value-- no need to be converted to numeric form

#%%
#df2.dtypes
#df2['overall'].dtypes
#df2['overall'].value_counts()


#%%
# count the samples by company
df_f = df2
count_sample(df_f, 'overall')


#%%
# calculate means and sems, and draw a chart
get_ipython().run_line_magic('matplotlib', 'notebook')
draw_chart(calc_means(df_f, 'overall'), calc_sems(df_f, 'overall'))
print_label("Over-All Ratings")


#%%



#%%



