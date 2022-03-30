from numpy import *
from pandas import *

nov_open=read_csv('/Users/jonathanprince/python/november21_litecoin_data.csv')['Open'].values      #Transforms data from csv file within the "open"column into an array, called "open".

nov_close=read_csv('/Users/jonathanprince/python/november21_litecoin_data.csv')['Close'].values    #Transforms data from csv file within the "close"column into an array, called "close".

dec_open=read_csv('/Users/jonathanprince/python/december21_litecoin_data.csv')['Open'].values

dec_close=read_csv('/Users/jonathanprince/python/december21_litecoin_data.csv')['Close'].values  

jan_open22=read_csv('/Users/jonathanprince/python/litecoin_data/Jan22_data.csv')['Open'].values

jan_close22=read_csv('/Users/jonathanprince/python/litecoin_data/Jan22_data.csv')['Close'].values



#November 2021 Data

A=[]
for i in arange(0,15):
  y=(nov_open[i]+nov_close[i])/2
  r=round(y,2)
  A.append(r)

oc=[]
for i in arange(0,14):
  e=(nov_open[i+1]-nov_close[i])
  eq=round(e,2)
  oc.append(eq)


O=Series(nov_open,index=['11.16.21','11.17.21','11.18.21','11.19.21','11.20.21','11.21.21','11.22.21','11.23.21','11.24.21','11.25.21','11.26.21','11.27.21','11.28.21','11.29.21','11.30.21'])
C=Series(nov_close,index=['11.16.21','11.17.21','11.18.21','11.19.21','11.20.21','11.21.21','11.22.21','11.23.21','11.24.21','11.25.21','11.26.21','11.27.21','11.28.21','11.29.21','11.30.21'])
Avg=Series(A,index=['11.16.21','11.17.21','11.18.21','11.19.21','11.20.21','11.21.21','11.22.21','11.23.21','11.24.21','11.25.21','11.26.21','11.27.21','11.28.21','11.29.21','11.30.21'])
close_open_diff_nov=Series(oc,index=['11.17.21','11.18.21','11.19.21','11.20.21','11.21.21','11.22.21','11.23.21','11.24.21','11.25.21','11.26.21','11.27.21','11.28.21','11.29.21','11.30.21'])
nov21_1st_avg=Avg.loc['11.16.21':'11.23.21']
nov21_2nd_avg=Avg.loc['11.24.21':'11.30.21']

nov21_1st_avg=round(nov21_1st_avg.mean(),2)
nov21_2nd_avg=round(nov21_2nd_avg.mean(),2)

tot_data=DataFrame({'Open':O, 'Close':C, 'Average':Avg, 'Open(n+1)-Close(n) Difference':close_open_diff_nov})
replaced_tot_data=tot_data.fillna(0.00)
print(replaced_tot_data)
print("The average price of Litecoin during the 90 days analyzed in November 2021 was:   ", round(mean(A),2))
print("The median price of Litecoin during the 90 days analyzed in November 2021 was:   ", round(median(A),2))
nov_avg=round(mean(A),2)

#December 2021 Data

B=[]
for i in arange(0,31):
  m=(dec_open[i]+dec_close[i])/2
  j=round(m,2)
  B.append(j)

dec_diff=[]
for i in arange(0,30):
  dd=(dec_open[i+1]-dec_close[i])
  ddd=round(dd,2)
  dec_diff.append(ddd)


O_Dec21=Series(dec_open,index=['12.01.21','12.02.21','12.03.21','12.04.21','12.05.21','12.06.21','12.07.21','12.08.21','12.09.21','12.10.21','12.11.21','12.12.21','12.13.21','12.14.21','12.15.21','12.16.21','12.17.21','12.18.21','12.19.21','12.20.21','12.21.21','12.22.21','12.23.21','12.24.21','12.25.21','12.26.21','12.27.21','12.28.21','12.29.21','12.30.21','12.31.21'])
C_Dec21=Series(dec_close,index=['12.01.21','12.02.21','12.03.21','12.04.21','12.05.21','12.06.21','12.07.21','12.08.21','12.09.21','12.10.21','12.11.21','12.12.21','12.13.21','12.14.21','12.15.21','12.16.21','12.17.21','12.18.21','12.19.21','12.20.21','12.21.21','12.22.21','12.23.21','12.24.21','12.25.21','12.26.21','12.27.21','12.28.21','12.29.21','12.30.21','12.31.21'])
Avg_Dec21=Series(B,index=['12.01.21','12.02.21','12.03.21','12.04.21','12.05.21','12.06.21','12.07.21','12.08.21','12.09.21','12.10.21','12.11.21','12.12.21','12.13.21','12.14.21','12.15.21','12.16.21','12.17.21','12.18.21','12.19.21','12.20.21','12.21.21','12.22.21','12.23.21','12.24.21','12.25.21','12.26.21','12.27.21','12.28.21','12.29.21','12.30.21','12.31.21'])
close_open_diff_dec=Series(dec_diff,index=['12.02.21','12.03.21','12.04.21','12.05.21','12.06.21','12.07.21','12.08.21','12.09.21','12.10.21','12.11.21','12.12.21','12.13.21','12.14.21','12.15.21','12.16.21','12.17.21','12.18.21','12.19.21','12.20.21','12.21.21','12.22.21','12.23.21','12.24.21','12.25.21','12.26.21','12.27.21','12.28.21','12.29.21','12.30.21','12.31.21'])
dec21_1st_avg=Avg_Dec21.loc['12.01.21':'12.16.21']
dec21_2nd_avg=Avg_Dec21.loc['12.17.21':'12.31.21']

dec21_1st_avg=round(dec21_1st_avg.mean(),2)
dec21_2nd_avg=round(dec21_2nd_avg.mean(),2)

tot_data_dec=DataFrame({'Open':O_Dec21, 'Close':C_Dec21, 'Average':Avg_Dec21, 'Open(n+1)-Close(n) Difference':close_open_diff_dec})
replaced_tot_data_dec=tot_data_dec.fillna(0.00)
print(replaced_tot_data_dec)
print("The average price of Litecoin during the 90 days analyzed in December 2021 was:   ", round(mean(B),2)) 
print("The median price of Litecoin during the 90 days analyzed in November 2021 was:   ", round(median(B),2))
dec_avg=round(mean(B),2)

#January 2022 Data
 
D=[]
for i in arange(0,31):
  q=(jan_open22[i]+jan_close22[i])/2
  w=round(q,2)
  D.append(w)

jan_diff=[]
for i in arange(0,30):
  jj=(jan_open22[i+1]-jan_close22[i])
  jjj=round(jj,2)
  jan_diff.append(jjj)


O_Jan22=Series(jan_open22,index=['1.01.22','1.02.22','1.03.22','1.04.22','1.05.22','1.06.22','1.07.22','1.08.22','1.09.22','1.10.22','1.11.22','1.12.22','1.13.22','1.14.22','1.15.22','1.16.22','1.17.22','1.18.22','1.19.22','1.20.22','1.21.22','1.22.22','1.23.22','1.24.22','1.25.22','1.26.22','1.27.22','1.28.22','1.29.22','1.30.22','1.31.22'])
C_Jan22=Series(jan_close22,index=['1.01.22','1.02.22','1.03.22','1.04.22','1.05.22','1.06.22','1.07.22','1.08.22','1.09.22','1.10.22','1.11.22','1.12.22','1.13.22','1.14.22','1.15.22','1.16.22','1.17.22','1.18.22','1.19.22','1.20.22','1.21.22','1.22.22','1.23.22','1.24.22','1.25.22','1.26.22','1.27.22','1.28.22','1.29.22','1.30.22','1.31.22'])
Avg_Jan22=Series(D,index=['1.01.22','1.02.22','1.03.22','1.04.22','1.05.22','1.06.22','1.07.22','1.08.22','1.09.22','1.10.22','1.11.22','1.12.22','1.13.22','1.14.22','1.15.22','1.16.22','1.17.22','1.18.22','1.19.22','1.20.22','1.21.22','1.22.22','1.23.22','1.24.22','1.25.22','1.26.22','1.27.22','1.28.22','1.29.22','1.30.22','1.31.22'])
close_open_diff_jan=Series(jan_diff,index=['1.02.22','1.03.22','1.04.22','1.05.22','1.06.22','1.07.22','1.08.22','1.09.22','1.10.22','1.11.22','1.12.22','1.13.22','1.14.22','1.15.22','1.16.22','1.17.22','1.18.22','1.19.22','1.20.22','1.21.22','1.22.22','1.23.22','1.24.22','1.25.22','1.26.22','1.27.22','1.28.22','1.29.22','1.30.22','1.31.22'])
jan22_1st_avg=Avg_Jan22.loc['1.01.22':'1.16.22']
jan22_2nd_avg=Avg_Jan22.loc['1.17.22':'1.31.22']

jan22_1st_avg=round(jan22_1st_avg.mean(),2)
jan22_2nd_avg=round(jan22_2nd_avg.mean(),2)


tot_data_jan=DataFrame({'Open':O_Jan22, 'Close':C_Jan22, 'Average':Avg_Jan22, 'Open(n+1)-Close(n) Difference':close_open_diff_jan})
replaced_tot_data_jan=tot_data_jan.fillna(0.00)
print(replaced_tot_data_jan)
print("The average price of Litecoin during the 90 days analyzed in January 2022 was:   ", round(mean(D),2))
print("The median price of Litecoin during the 90 days analyzed in November 2021 was:   ", round(median(D),2))
jan_avg=round(mean(D),2)

avg_21=Series([nov_avg,dec_avg,jan_avg],index=['November','December','January'])
data=DataFrame(avg_21, columns=['90 Day Average Monthly Price'])
print("Of course, we can put the montly averages in a table, for easy viewing. For example, the following table displays the monthly averages for Novemebr 2021, December 2021 and January 2022.")
print(data)

monthly_split={('November',1):nov21_1st_avg,('November',2):nov21_2nd_avg,('November','Difference'):nov21_2nd_avg-nov21_1st_avg,('December',1):dec21_1st_avg,('December',2):dec21_2nd_avg,('December','Difference'):dec21_2nd_avg-dec21_1st_avg,('January',1):jan22_1st_avg,('January',2):jan22_2nd_avg,('January','Difference'):jan22_2nd_avg-jan22_1st_avg}
indx_monthly_split=Series(monthly_split)
print("Or we can take this analysis one step further and analyze each half of the month. For example, the following table displays the average price of Litecoin for each half, ofeach month analyzed. Here the index 'Difference' represents the difference in average price between the second half of the month and the first half of the month") 
print(indx_monthly_split)
