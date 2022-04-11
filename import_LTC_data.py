from numpy import *
from pandas import * 
from seventeen import * 
from eighteen import *
from nineteen import *
from twenty import * 
from twentyone import * 

#2017 Data

average2017=Series([Jan17_avg,Feb17_avg,March17_avg,April17_avg,May17_avg,June17_avg,July17_avg,August17_avg,Sept17_avg,Oct17_avg,Nov17_avg,Dec17_avg],index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])

average2017_min=round(average2017.min(),2)
average2017_25th=round(percentile(average2017,25),2)
average2017_mean=round(average2017.mean(),2)
average2017_med=round(average2017.median(),2)
average2017_75th=round(percentile(average2017,75),2)
average2017_max=round(average2017.max(),2)

average2017_stats=Series([average2017_min,average2017_25th,average2017_mean,average2017_med,average2017_75th,average2017_max],index=['Min','25th percentile','Mean','Median','75th percentile','Max'])


#2018 Data 

average2018=Series([Jan18_avg,Feb18_avg,March18_avg,April18_avg,May18_avg,June18_avg,July18_avg,August18_avg,Sept18_avg,Oct18_avg,Nov18_avg,Dec18_avg],index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])

average2018_min=round(average2018.min(),2)
average2018_25th=round(percentile(average2018,25),2)
average2018_mean=round(average2018.mean(),2)
average2018_med=round(average2018.median(),2)
average2018_75th=round(percentile(average2018,75),2)
average2018_max=round(average2018.max(),2)

average2018_stats=Series([average2018_min,average2018_25th,average2018_mean,average2018_med,average2018_75th,average2018_max],index=['Min','25th percentile','Mean','Median','75th percentile','Max'])

#2019 Data

average2019=Series([Jan19_avg,Feb19_avg,March19_avg,April19_avg,May19_avg,June19_avg,July19_avg,August19_avg,Sept19_avg,Oct19_avg,Nov19_avg,Dec19_avg],index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])

average2019_min=round(average2019.min(),2)
average2019_25th=round(percentile(average2019,25),2)
average2019_mean=round(average2019.mean(),2)
average2019_med=round(average2019.median(),2)
average2019_75th=round(percentile(average2019,75),2)
average2019_max=round(average2019.max(),2)

average2019_stats=Series([average2019_min,average2019_25th,average2019_mean,average2019_med,average2019_75th,average2019_max],index=['Min','25th percentile','Mean','Median','75th percentile','Max'])


#2020 Data

average2020=Series([Jan20_avg,Feb20_avg,March20_avg,April20_avg,May20_avg,June20_avg,July20_avg,August20_avg,Sept20_avg,Oct20_avg,Nov20_avg,Dec20_avg],index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])

average2020_min=round(average2020.min(),2)
average2020_25th=round(percentile(average2020,25),2)
average2020_mean=round(average2020.mean(),2)
average2020_med=round(average2020.median(),2)
average2020_75th=round(percentile(average2020,75),2)
average2020_max=round(average2020.max(),2)

average2020_stats=Series([average2020_min,average2020_25th,average2020_mean,average2020_med,average2020_75th,average2020_max],index=['Min','25th percentile','Mean','Median','75th percentile','Max'])


#2021 Data

average2021=Series([Jan21_avg,Feb21_avg,March21_avg,April21_avg,May21_avg,June21_avg,July21_avg,August21_avg,Sept21_avg,Oct21_avg,Nov21_avg,Dec21_avg],index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])

average2021_min=round(average2021.min(),2)
average2021_25th=round(percentile(average2021,25),2)
average2021_mean=round(average2021.mean(),2)
average2021_med=round(average2021.median(),2)
average2021_75th=round(percentile(average2021,75),2)
average2021_max=round(average2021.max(),2)

average2021_stats=Series([average2021_min,average2021_25th,average2021_mean,average2021_med,average2021_75th,average2021_max],index=['Min','25th percentile','Mean','Median','75th percentile','Max'])

#5 Year DataFrame

totaldata=DataFrame({'2017':average2017,'2018':average2018,'2019':average2019,'2020':average2020,'2021':average2021})

print(totaldata)

#5 Year Yearly Statistics DataFrame

totaldata_stats=DataFrame({'2017':average2017_stats, '2018':average2018_stats, '2019':average2019_stats, '2020':average2020_stats, '2021':average2021_stats})

print(totaldata_stats)
