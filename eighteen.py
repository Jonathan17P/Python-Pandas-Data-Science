from numpy import * 
from pandas import * 


data = read_csv("/Users/jonathanprince/python/litecoin_data/5_year_data/LTC2017_2021_data.csv")

#Sets the index to "Date" within the data dataframe defined above this line 

new_data=data.set_index('Date')
#print(new_data)

#2018 Data Starts Here 

#January 2018 Data

Jan18_data=new_data.loc['Jan 31, 2018': 'Jan 01, 2018'].copy()
Jan18_data['Average'] = ((Jan18_data['Close'] + Jan18_data['Open'])/2)
Jan18_avg=round(Jan18_data['Average'].mean(),2)

#Febuary 2018 Data

Feb18_data=new_data.loc['Feb 28, 2018': 'Feb 01, 2018'].copy()
Feb18_data['Average'] = ((Feb18_data['Close'] + Feb18_data['Open'])/2)
Feb18_avg=round(Feb18_data['Average'].mean(),2)

#March 2018 Data 

March18_data=new_data.loc['Mar 31, 2018': 'Mar 01, 2018'].copy()
March18_data['Average'] = ((March18_data['Close'] + March18_data['Open'])/2)
March18_avg=round(March18_data['Average'].mean(),2)

#April 2018 Data

April18_data=new_data.loc['Apr 30, 2018': 'Apr 01, 2018'].copy()
April18_data['Average'] = ((April18_data['Close'] + April18_data['Open'])/2)
April18_avg=round(April18_data['Average'].mean(),2)

#May 2018 Data 

May18_data=new_data.loc['May 31, 2018': 'May 01, 2018'].copy()
May18_data['Average'] = ((May18_data['Close'] + May18_data['Open'])/2)
May18_avg=round(May18_data['Average'].mean(),2)


#June 2018 Data 

June18_data=new_data.loc['Jun 30, 2018': 'Jun 01, 2018'].copy()
June18_data['Average'] = ((June18_data['Close'] + June18_data['Open'])/2)
June18_avg=round(June18_data['Average'].mean(),2)


#July 2018 Data 

July18_data=new_data.loc['Jul 31, 2018': 'Jul 01, 2018'].copy()
July18_data['Average'] = ((July18_data['Close'] + July18_data['Open'])/2)
July18_avg=round(July18_data['Average'].mean(),2)


#August 2018 Data 

August18_data=new_data.loc['Aug 31, 2018': 'Aug 01, 2018'].copy()
August18_data['Average'] = ((August18_data['Close'] + August18_data['Open'])/2)
August18_avg=round(August18_data['Average'].mean(),2)


#September 2018 Data 

Sept18_data=new_data.loc['Sep 30, 2018': 'Sep 01, 2018'].copy()
Sept18_data['Average'] = ((Sept18_data['Close'] + Sept18_data['Open'])/2)
Sept18_avg=round(Sept18_data['Average'].mean(),2)


#October 2018 Data 

Oct18_data=new_data.loc['Oct 31, 2018': 'Oct 01, 2018'].copy()
Oct18_data['Average'] = ((Oct18_data['Close'] + Oct18_data['Open'])/2)
Oct18_avg=round(Oct18_data['Average'].mean(),2)


#Novemebr 2018 Data 

Nov18_data=new_data.loc['Nov 30, 2018': 'Nov 01, 2018'].copy()
Nov18_data['Average'] = ((Nov18_data['Close'] + Nov18_data['Open'])/2)
Nov18_avg=round(Nov18_data['Average'].mean(),2)


#December 2018 Data 

Dec18_data=new_data.loc['Dec 31, 2018': 'Dec 01, 2018'].copy()
Dec18_data['Average'] = ((Dec18_data['Close'] + Dec18_data['Open'])/2)
Dec18_avg=round(Dec18_data['Average'].mean(),2)


#December 2021 Data

#dec21_data=new_data.loc['Dec 31, 2021': 'Dec 01, 2021'].copy()
#dec21_data['Average'] = ((dec21_data['Close'] + dec21_data['Open'])/2) 
#print(dec21_data) 
