from numpy import * 
from pandas import * 


data = read_csv("/Users/jonathanprince/python/litecoin_data/5_year_data/LTC2017_2021_data.csv")

#Sets the index to "Date" within the data dataframe defined above this line 

new_data=data.set_index('Date')
#print(new_data)

#2021 Data Starts Here 

#January 2021 Data

Jan21_data=new_data.loc['Jan 31, 2021': 'Jan 01, 2021'].copy()
Jan21_data['Average'] = ((Jan21_data['Close'] + Jan21_data['Open'])/2)
Jan21_avg=round(Jan21_data['Average'].mean(),2)

#Febuary 2021 Data

Feb21_data=new_data.loc['Feb 28, 2021': 'Feb 01, 2021'].copy()
Feb21_data['Average'] = ((Feb21_data['Close'] + Feb21_data['Open'])/2)
Feb21_avg=round(Feb21_data['Average'].mean(),2)

#March 2021 Data 

March21_data=new_data.loc['Mar 31, 2021': 'Mar 01, 2021'].copy()
March21_data['Average'] = ((March21_data['Close'] + March21_data['Open'])/2)
March21_avg=round(March21_data['Average'].mean(),2)

#April 2021 Data

April21_data=new_data.loc['Apr 30, 2021': 'Apr 01, 2021'].copy()
April21_data['Average'] = ((April21_data['Close'] + April21_data['Open'])/2)
April21_avg=round(April21_data['Average'].mean(),2)

#May 2021 Data 

May21_data=new_data.loc['May 31, 2021': 'May 01, 2021'].copy()
May21_data['Average'] = ((May21_data['Close'] + May21_data['Open'])/2)
May21_avg=round(May21_data['Average'].mean(),2)


#June 2021 Data 

June21_data=new_data.loc['Jun 30, 2021': 'Jun 01, 2021'].copy()
June21_data['Average'] = ((June21_data['Close'] + June21_data['Open'])/2)
June21_avg=round(June21_data['Average'].mean(),2)


#July 2021 Data 

July21_data=new_data.loc['Jul 31, 2021': 'Jul 01, 2021'].copy()
July21_data['Average'] = ((July21_data['Close'] + July21_data['Open'])/2)
July21_avg=round(July21_data['Average'].mean(),2)


#August 2021 Data 

August21_data=new_data.loc['Aug 31, 2021': 'Aug 01, 2021'].copy()
August21_data['Average'] = ((August21_data['Close'] + August21_data['Open'])/2)
August21_avg=round(August21_data['Average'].mean(),2)


#September 2021 Data 

Sept21_data=new_data.loc['Sep 30, 2021': 'Sep 01, 2021'].copy()
Sept21_data['Average'] = ((Sept21_data['Close'] + Sept21_data['Open'])/2)
Sept21_avg=round(Sept21_data['Average'].mean(),2)


#October 2021 Data 

Oct21_data=new_data.loc['Oct 31, 2021': 'Oct 01, 2021'].copy()
Oct21_data['Average'] = ((Oct21_data['Close'] + Oct21_data['Open'])/2)
Oct21_avg=round(Oct21_data['Average'].mean(),2)


#Novemebr 2021 Data 

Nov21_data=new_data.loc['Nov 30, 2021': 'Nov 01, 2021'].copy()
Nov21_data['Average'] = ((Nov21_data['Close'] + Nov21_data['Open'])/2)
Nov21_avg=round(Nov21_data['Average'].mean(),2)


#December 2021 Data 

Dec21_data=new_data.loc['Dec 31, 2021': 'Dec 01, 2021'].copy()
Dec21_data['Average'] = ((Dec21_data['Close'] + Dec21_data['Open'])/2)
Dec21_avg=round(Dec21_data['Average'].mean(),2)

