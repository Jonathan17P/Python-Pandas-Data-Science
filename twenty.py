from numpy import * 
from pandas import * 


data = read_csv("/Users/jonathanprince/python/litecoin_data/5_year_data/LTC2017_2021_data.csv")

#Sets the index to "Date" within the data dataframe defined above this line 

new_data=data.set_index('Date')
#print(new_data)

#2020 Data Starts Here 

#January 2020 Data

Jan20_data=new_data.loc['Jan 31, 2020': 'Jan 01, 2020'].copy()
Jan20_data['Average'] = ((Jan20_data['Close'] + Jan20_data['Open'])/2)
Jan20_avg=round(Jan20_data['Average'].mean(),2)

#Febuary 2020 Data

Feb20_data=new_data.loc['Feb 28, 2020': 'Feb 01, 2020'].copy()
Feb20_data['Average'] = ((Feb20_data['Close'] + Feb20_data['Open'])/2)
Feb20_avg=round(Feb20_data['Average'].mean(),2)

#March 2020 Data 

March20_data=new_data.loc['Mar 31, 2020': 'Mar 01, 2020'].copy()
March20_data['Average'] = ((March20_data['Close'] + March20_data['Open'])/2)
March20_avg=round(March20_data['Average'].mean(),2)

#April 2020 Data

April20_data=new_data.loc['Apr 30, 2020': 'Apr 01, 2020'].copy()
April20_data['Average'] = ((April20_data['Close'] + April20_data['Open'])/2)
April20_avg=round(April20_data['Average'].mean(),2)

#May 2020 Data 

May20_data=new_data.loc['May 31, 2020': 'May 01, 2020'].copy()
May20_data['Average'] = ((May20_data['Close'] + May20_data['Open'])/2)
May20_avg=round(May20_data['Average'].mean(),2)


#June 2020 Data 

June20_data=new_data.loc['Jun 30, 2020': 'Jun 01, 2020'].copy()
June20_data['Average'] = ((June20_data['Close'] + June20_data['Open'])/2)
June20_avg=round(June20_data['Average'].mean(),2)


#July 2020 Data 

July20_data=new_data.loc['Jul 31, 2020': 'Jul 01, 2020'].copy()
July20_data['Average'] = ((July20_data['Close'] + July20_data['Open'])/2)
July20_avg=round(July20_data['Average'].mean(),2)


#August 2020 Data 

August20_data=new_data.loc['Aug 31, 2020': 'Aug 01, 2020'].copy()
August20_data['Average'] = ((August20_data['Close'] + August20_data['Open'])/2)
August20_avg=round(August20_data['Average'].mean(),2)


#September 2020 Data 

Sept20_data=new_data.loc['Sep 30, 2020': 'Sep 01, 2020'].copy()
Sept20_data['Average'] = ((Sept20_data['Close'] + Sept20_data['Open'])/2)
Sept20_avg=round(Sept20_data['Average'].mean(),2)


#October 2020 Data 

Oct20_data=new_data.loc['Oct 31, 2020': 'Oct 01, 2020'].copy()
Oct20_data['Average'] = ((Oct20_data['Close'] + Oct20_data['Open'])/2)
Oct20_avg=round(Oct20_data['Average'].mean(),2)


#Novemebr 2020 Data 

Nov20_data=new_data.loc['Nov 30, 2020': 'Nov 01, 2020'].copy()
Nov20_data['Average'] = ((Nov20_data['Close'] + Nov20_data['Open'])/2)
Nov20_avg=round(Nov20_data['Average'].mean(),2)


#December 2020 Data 

Dec20_data=new_data.loc['Dec 31, 2020': 'Dec 01, 2020'].copy()
Dec20_data['Average'] = ((Dec20_data['Close'] + Dec20_data['Open'])/2)
Dec20_avg=round(Dec20_data['Average'].mean(),2)

