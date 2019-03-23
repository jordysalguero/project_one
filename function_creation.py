
import pandas as pd
import numpy as np
from scipy.stats import sem

def draw_chart(plt, input_data1, input_data2):
    vm_df =input_data1
    vsem_df=input_data2
    
    # plot the graph
    x = np.arange(0, len(vm_df), 1)

    ax1= plt.errorbar(x, vm_df['amazon'], yerr=vsem_df['amazon'], color="darkorange", linewidth=0.5, marker='*' )
    ax2= plt.errorbar(x, vm_df['apple'],  yerr=vsem_df['apple'], color="grey",linewidth=0.5, marker='*')
    ax3= plt.errorbar(x, vm_df['facebook'],yerr=vsem_df['facebook'], color="royalblue",linewidth=0.5, marker='*' )
    ax4= plt.errorbar(x, vm_df['google'],  yerr=vsem_df['google'], color="gold",linewidth=0.5, marker='*' )
    ax5= plt.errorbar(x, vm_df['microsoft'],yerr=vsem_df['microsoft'], color="green", linewidth=0.5, marker='*' )
    ax6= plt.errorbar(x, vm_df['netflix'], yerr=vsem_df['netflix'], color="red",linewidth=0.5, marker='*')

    #year = np.arange(2008,2019,1)
    year=['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    x_ticks=[value for value in x]
    plt.xticks(x_ticks, year, rotation='30')
    
def draw_chart2(plt, input_data1, input_data2):
    vm_df =input_data1
    vsem_df=input_data2
    
    # plot the graph
    x = np.arange(0, len(vm_df), 1)

    ax1= plt.errorbar(x, vm_df['amazon'], yerr=vsem_df['amazon'], color="darkorange", linewidth=0.5, marker='*' )
    ax2= plt.errorbar(x, vm_df['apple'],  yerr=vsem_df['apple'], color="grey",linewidth=0.5, marker='*')
    ax3= plt.errorbar(x, vm_df['facebook'],yerr=vsem_df['facebook'], color="royalblue",linewidth=0.5, marker='*' )
    ax4= plt.errorbar(x, vm_df['google'],  yerr=vsem_df['google'], color="gold",linewidth=0.5, marker='*' )
    ax5= plt.errorbar(x, vm_df['microsoft'],yerr=vsem_df['microsoft'], color="green", linewidth=0.5, marker='*' )
    ax6= plt.errorbar(x, vm_df['netflix'], yerr=vsem_df['netflix'], color="red",linewidth=0.5, marker='*')


    #year = np.arange(2008,2019,1)
    year= ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
    x_ticks=[value for value in x] 
    plt.xticks(x_ticks, year, rotation='30')
    
def print_label(plt, col_name):
    plt.ylim(2.0, 5.9)
    plt.title(f"{col_name} over Time")
    plt.xlabel("Time (years)")
    plt.ylabel(f"{col_name}(1-5)")

    plt.legend(loc="upper right", fontsize="small", fancybox=True)
    plt.show()


    plt.tight_layout()
    plt.savefig(f"./Images/Data_Visualization/{col_name}.png")

def calc_means(input_data, col_name):
    data=input_data
    m_data = data.groupby(['company','year'])[col_name].mean()
    m_data
    m1_data = m_data.to_frame(name=None) # change to the dataframeculture_val
    m1_data.head()
    vm_data  = m1_data.unstack('company').loc[:,col_name]
    return vm_data
    
def calc_sems(input_data, col_name):
    data=input_data
    sem_data = data.groupby(['company','year'])[col_name].sem()
    sem1_data = sem_data.to_frame(name=None) # change to the dataframe
    vsem_data  = sem1_data.unstack('company').loc[:,col_name]
    return vsem_data 

def count_sample(input_data, col_name):
    data=input_data
    s_data = data.sort_values(by=['year'])  
    final_data=s_data[['company','year',col_name]]
    final=final_data.groupby(['company','year'])[col_name].count()
    return  final.unstack('company')









    
    