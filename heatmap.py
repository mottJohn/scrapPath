from __future__ import division
from functools import reduce

##############################
# USER INPUTS

# reference
#https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g5.html
#https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g1.html
##############################

path_cmaq = r'C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\cmaqAll'

#comment out if not use
#pollutants = 1 #TSP
#pollutants = 2 #RSP (PM10) daily
#pollutants = 3 #RSP (PM10) annual
#pollutants = 4 #FSP (PM2.5) daily
#pollutants = 5 #FSP (PM2.5) annual
#pollutants = 6 #NO2 hourly
#pollutants = 7 #NO2 Annual
#pollutants = 8 #Ozone 8-hourly

##############################
#CODES DO NOT MODIFY
##############################

import time
start_time = time.time()

from joblib import Parallel, delayed
import multiprocessing

import pandas as pd
from pandas import ExcelWriter
import math
import numpy as np

import glob

def getFiles (path, type):
    filteredFiles = []
    allFiles = glob.glob(path + "/*.{}".format(type))
    
    return allFiles

def get_nlargest(df, n, adj):
    result = {}
    for cols in df.columns[1:]: #skip index
        tem = df[cols].nlargest(n).tolist()[-1] + adj
        result[cols] = tem
    return result

#merge = pd.DataFrame()
def calculate(i):
    pollutants = i
    print(i)
    if pollutants == 1: #TSP
        factor_annual = 1
        factor_daily = 1
        factor_aermod = 1
        
        RSP_an_adj = 0
        RSP_10_adj = 0

    elif pollutants == 2: #RSP daily
        factor_annual = 1
        factor_daily = 1 
        factor_aermod = 1
        
        RSP_an_adj = 15.6
        RSP_10_adj = 26.5
        
    elif pollutants == 3: #RSP annual
        factor_annual = 1
        factor_daily = 1 
        factor_aermod = 1
        
        RSP_an_adj = 15.6
        RSP_10_adj = 26.5
        

    elif pollutants == 4: #FSP daily
        factor_annual = 0.71
        factor_daily = 0.75
        factor_aermod = 1
        
        RSP_an_adj = 15.6*factor_annual
        RSP_10_adj = 26.5*factor_daily
        
    elif pollutants == 5: #FSP annaul
        factor_annual = 0.71
        factor_daily = 0.75
        factor_aermod = 1
        
        RSP_an_adj = 15.6*factor_annual
        RSP_10_adj = 26.5*factor_daily
        

    elif pollutants == 6: #NO2 hourly
        factor_annual = 1
        factor_daily = 1
        factor_aermod = 1
        
        RSP_an_adj = 0*factor_annual
        RSP_10_adj = 0*factor_daily
        
    elif pollutants == 7: #NO2 Annual
        factor_annual = 1
        factor_daily = 1
        factor_aermod = 1
        
        RSP_an_adj = 0*factor_annual
        RSP_10_adj = 0*factor_daily
        
    elif pollutants == 8: #Ozone 8-hourly
        factor_annual = 1
        factor_daily = 1
        factor_aermod = 1
        
        RSP_an_adj = 0*factor_annual
        RSP_10_adj = 0*factor_daily

    output = pd.DataFrame()
    files_cmaq = getFiles(path_cmaq, 'txt')
    for cmaq in files_cmaq:
        xy = cmaq.replace(".txt", "").split('_')
        x = xy[-2]
        y = xy[-1]
        #print("({},{})".format(x,y))

        data = pd.read_csv(cmaq, sep='\s+')
        data = data.drop([0,1], axis = 0)
        data = data.apply(pd.to_numeric)

        """
        index = data.index.tolist()
        re_index = index[-8:] + index[:-8]
        data = data.reindex(re_index) #move the last 7 rows to the top
        #data = data.drop(data.index[0:9])
        print(data)
        for a in list(range(7)): #set YYYY to be the year in the 9th row
                data.iloc[a,0] = data.iloc[7,0]
        
        data = data.reset_index(drop=True)
        """

        data = data[16:-8]
        data_an = data*factor_annual
        data_24 = data.groupby(np.arange(len(data))//24).mean()
        data_24.iloc[:,1:] = data_24.iloc[:,1:]*factor_daily + RSP_10_adj

        """
        data_8 = data.groupby(np.arange(len(data))//8).mean()
        data_8.iloc[:,1:] = data_8.iloc[:,1:]
        """
        data_8 = data.rolling(8).mean()
        #print(data_8)

        lst = []
        lst.append(get_nlargest(data, 1, 0)) #Max Hourly
        lst.append(get_nlargest(data_24, 10,0)) #10th Max Daily
        lst.append(get_nlargest(data_8, 10,0)) #10th Max 8-hour
        lst.append(get_nlargest(data, 19, 0)) #19th Max Hourly
        lst.append((data_an.mean() + RSP_an_adj).to_dict()) #annual average

        summary = pd.DataFrame(lst)
        summary['Index'] = ['Max hourly','10th Max Daily','10th Max 8 hour average','19th Max hourly','Annual average']
        summary = summary.drop(columns = ['Year', 'dd', 'mm', 'hh'])
        summary['i'] = x
        summary['j'] = y

        if pollutants == 1:
            lst_rows = ['Max hourly']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','RSP','Index']]
            summary = summary.rename(columns = {'RSP':'TSP Max hourly'})
            summary = summary.drop(['Index'], axis = 1)

        elif pollutants == 2:
            lst_rows = ['10th Max Daily']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','RSP','Index']]
            summary = summary.rename(columns = {'RSP':'RSP 10th Max daily'})
            summary = summary.drop(['Index'], axis = 1)

        elif pollutants == 3:
            lst_rows = ['Annual average']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','RSP','Index']]
            summary = summary.rename(columns = {'RSP':'RSP Annual average'})
            summary = summary.drop(['Index'], axis = 1)
            
        elif pollutants == 4:
            lst_rows = ['10th Max Daily']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','RSP','Index']]
            summary = summary.rename(columns = {'RSP':'FSP 10th Max Daily'})
            summary = summary.drop(['Index'], axis = 1)

        elif pollutants == 5:
            lst_rows = ['Annual average']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','RSP','Index']]
            summary = summary.rename(columns = {'RSP':'FSP Annual average'})
            summary = summary.drop(['Index'], axis = 1)
        
        elif pollutants == 6: #NO2 hourly
            lst_rows = ['19th Max hourly']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','NO2','Index']]
            summary = summary.rename(columns = {'NO2':'NO2 19th Max hourly'})
            summary = summary.drop(['Index'], axis = 1)

        elif pollutants == 7: #NO2 Annual
            lst_rows = ['Annual average']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','NO2','Index']]
            summary = summary.rename(columns = {'NO2':'NO2 Annual average'})
            summary = summary.drop(['Index'], axis = 1)

        elif pollutants == 8: #Ozone 8-hourly
            lst_rows = ['10th Max 8 hour average']
            summary = summary[summary['Index'].isin(lst_rows)]
            summary = summary[['i','j','O3','Index']]
            summary = summary.rename(columns = {'O3':'O3 10th Max 8 hour average'})
            summary = summary.drop(['Index'], axis = 1)
        
        try:
            output = pd.concat([output, summary])
        except:
            output = summary

    output = output.sort_values(['i','j'])

    return output

#merge = merge.apply(pd.to_numeric)
#merge = merge.sort_values(['i','j'])
#merge.to_csv('PATH_AQO.csv') 

num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(calculate)(i) for i in range(2,9))

merge = reduce(lambda x, y: pd.merge(x, y, on = ['i','j']), results)
merge.to_csv('PATH_AQO_concurrent_fixed.csv')
#print(merge)
print("--- %s seconds ---" % (time.time() - start_time))