from numpy import * 
from pandas import * 


data = read_csv("/Users/jonathanprince/python/litecoin_data/5_year_data/LTC2017_2021_data.csv")

#Sets the index to "Date" within the data dataframe defined above this line 

new_data=data.set_index('Date')
#print(new_data)

#2019 Data Starts Here 

#January 2019 Data

Jan19_data=new_data.loc['Jan 31, 2019': 'Jan 01, 2019'].copy()
Jan19_data['Average'] = ((Jan19_data['Close'] + Jan19_data['Open'])/2)
Jan19_avg=round(Jan19_data['Average'].mean(),2)

#Febuary 2019 Data

Feb19_data=new_data.loc['Feb 28, 2019': 'Feb 01, 2019'].copy()
Feb19_data['Average'] = ((Feb19_data['Close'] + Feb19_data['Open'])/2)
Feb19_avg=round(Feb19_data['Average'].mean(),2)

#March 2019 Data 

March19_data=new_data.loc['Mar 31, 2019': 'Mar 01, 2019'].copy()
March19_data['Average'] = ((March19_data['Close'] + March19_data['Open'])/2)
March19_avg=round(March19_data['Average'].mean(),2)

#April 2019 Data

April19_data=new_data.loc['Apr 30, 2019': 'Apr 01, 2019'].copy()
April19_data['Average'] = ((April19_data['Close'] + April19_data['Open'])/2)
April19_avg=round(April19_data['Average'].mean(),2)

#May 2019 Data 

May19_data=new_data.loc['May 31, 2019': 'May 01, 2019'].copy()
May19_data['Average'] = ((May19_data['Close'] + May19_data['Open'])/2)
May19_avg=round(May19_data['Average'].mean(),2)


#June 2019 Data 

June19_data=new_data.loc['Jun 30, 2019': 'Jun 01, 2019'].copy()
June19_data['Average'] = ((June19_data['Close'] + June19_data['Open'])/2)
June19_avg=round(June19_data['Average'].mean(),2)


#July 2019 Data 

July19_data=new_data.loc['Jul 31, 2019': 'Jul 01, 2019'].copy()
July19_data['Average'] = ((July19_data['Close'] + July19_data['Open'])/2)
July19_avg=round(July19_data['Average'].mean(),2)


#August 2019 Data 

August19_data=new_data.loc['Aug 31, 2019': 'Aug 01, 2019'].copy()
August19_data['Average'] = ((August19_data['Close'] + August19_data['Open'])/2)
August19_avg=round(August19_data['Average'].mean(),2)


#September 2019 Data 

Sept19_data=new_data.loc['Sep 30, 2019': 'Sep 01, 2019'].copy()
Sept19_data['Average'] = ((Sept19_data['Close'] + Sept19_data['Open'])/2)
Sept19_avg=round(Sept19_data['Average'].mean(),2)


#October 2019 Data 

Oct19_data=new_data.loc['Oct 31, 2019': 'Oct 01, 2019'].copy()
Oct19_data['Average'] = ((Oct19_data['Close'] + Oct19_data['Open'])/2)
Oct19_avg=round(Oct19_data['Average'].mean(),2)


#Novemebr 2019 Data 

Nov19_data=new_data.loc['Nov 30, 2019': 'Nov 01, 2019'].copy()
Nov19_data['Average'] = ((Nov19_data['Close'] + Nov19_data['Open'])/2)
Nov19_avg=round(Nov19_data['Average'].mean(),2)


#December 2019 Data 

Dec19_data=new_data.loc['Dec 31, 2019': 'Dec 01, 2019'].copy()
Dec19_data['Average'] = ((Dec19_data['Close'] + Dec19_data['Open'])/2)
Dec19_avg=round(Dec19_data['Average'].mean(),2)

