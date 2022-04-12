from numpy import * 
from pandas import * 


data = read_csv("/Users/jonathanprince/python/litecoin_data/5_year_data/LTC2017_2021_data.csv")

#Sets the index to "Date" within the data dataframe defined above this line 

new_data=data.set_index('Date')
#print(new_data)

#2017 Data Starts Here 

#January 2017 Data

Jan17_data=new_data.loc['Jan 31, 2017': 'Jan 01, 2017'].copy()
Jan17_data['Average'] = ((Jan17_data['Close'] + Jan17_data['Open'])/2)
Jan17_avg=round(Jan17_data['Average'].mean(),2)

#Febuary 2017 Data

Feb17_data=new_data.loc['Feb 28, 2017': 'Feb 01, 2017'].copy()
Feb17_data['Average'] = ((Feb17_data['Close'] + Feb17_data['Open'])/2)
Feb17_avg=round(Feb17_data['Average'].mean(),2)

#March 2017 Data 

March17_data=new_data.loc['Mar 31, 2017': 'Mar 01, 2017'].copy()
March17_data['Average'] = ((March17_data['Close'] + March17_data['Open'])/2)
March17_avg=round(March17_data['Average'].mean(),2)

#April 2017 Data

April17_data=new_data.loc['Apr 30, 2017': 'Apr 01, 2017'].copy()
April17_data['Average'] = ((April17_data['Close'] + April17_data['Open'])/2)
April17_avg=round(April17_data['Average'].mean(),2)

#May 2017 Data 

May17_data=new_data.loc['May 31, 2017': 'May 01, 2017'].copy()
May17_data['Average'] = ((May17_data['Close'] + May17_data['Open'])/2)
May17_avg=round(May17_data['Average'].mean(),2)


#June 2017 Data 

June17_data=new_data.loc['Jun 30, 2017': 'Jun 01, 2017'].copy()
June17_data['Average'] = ((June17_data['Close'] + June17_data['Open'])/2)
June17_avg=round(June17_data['Average'].mean(),2)


#July 2017 Data 

July17_data=new_data.loc['Jul 31, 2017': 'Jul 01, 2017'].copy()
July17_data['Average'] = ((July17_data['Close'] + July17_data['Open'])/2)
July17_avg=round(July17_data['Average'].mean(),2)


#August 2017 Data 

August17_data=new_data.loc['Aug 31, 2017': 'Aug 01, 2017'].copy()
August17_data['Average'] = ((August17_data['Close'] + August17_data['Open'])/2)
August17_avg=round(August17_data['Average'].mean(),2)


#September 2017 Data 

Sept17_data=new_data.loc['Sep 30, 2017': 'Sep 01, 2017'].copy()
Sept17_data['Average'] = ((Sept17_data['Close'] + Sept17_data['Open'])/2)
Sept17_avg=round(Sept17_data['Average'].mean(),2)


#October 2017 Data 

Oct17_data=new_data.loc['Oct 31, 2017': 'Oct 01, 2017'].copy()
Oct17_data['Average'] = ((Oct17_data['Close'] + Oct17_data['Open'])/2)
Oct17_avg=round(Oct17_data['Average'].mean(),2)


#Novemebr 2017 Data 

Nov17_data=new_data.loc['Nov 30, 2017': 'Nov 01, 2017'].copy()
Nov17_data['Average'] = ((Nov17_data['Close'] + Nov17_data['Open'])/2)
Nov17_avg=round(Nov17_data['Average'].mean(),2)


#December 2017 Data 

Dec17_data=new_data.loc['Dec 31, 2017': 'Dec 01, 2017'].copy()
Dec17_data['Average'] = ((Dec17_data['Close'] + Dec17_data['Open'])/2)
Dec17_avg=round(Dec17_data['Average'].mean(),2)
#print(Dec17_data)
#print(Dec17_avg)


#December 2021 Data

#dec21_data=new_data.loc['Dec 31, 2021': 'Dec 01, 2021'].copy()
#dec21_data['Average'] = ((dec21_data['Close'] + dec21_data['Open'])/2) 
#print(dec21_data) 
