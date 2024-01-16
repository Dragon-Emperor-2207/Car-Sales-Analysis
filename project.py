# importing the modules
from os import path
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import datetime
# giving a suitable heading to the streamlit module
st.title('CARS SURVEY 2011-2012')
st.write('THE CARSALES ARE AS FOLLOWS ')
st.balloons()
# importing the excel file and displaying the table on the screen
df = pd.read_excel('1CARSALE.xlsx',
 usecols='A,c,D:F,I,J,K,L,M,N,P',
 header=0)
st.write('the survey is as follows')
st.dataframe(df)
# displaying a pie chart on the basis of total cars sold by different manufacturers in year 2011 and 
2012
pie_chart = px.pie(df,
 title='TOTAL NUMBER OF MANUFACTURERS',
 values='Sales_in_thousands',
 names='Manufacturer')
# plotting the pie chart
st.plotly_chart(pie_chart,figsize=(20,20))
# to find the total manufactures in the year 2011 and 2012
Manufacturer = df['Manufacturer'].unique().tolist()
sales = df['Fuel_efficiency'].unique().tolist()
#horsepower = df['Horspower'].unique().tolist()
# adding a slider in our streamlit project on fuel_efficiency and different manufactures
sales_selection = st.slider('Fuel_efficiency:',
 min_value= min(sales),
 max_value= max(sales),
 value=(min(sales),max(sales)))
# adding a multi select bar with the slider
# so that the user can find therir suitable car by selecting the fuel efficiency and the manufacturer
department_selection = st.multiselect('Manufacturer:',
 options=df["Manufacturer"].unique(),
 default=df["Manufacturer"].unique())
20 
# executing the slider and multiselect
mask = (df['Fuel_efficiency'].between(*sales_selection)) & 
(df['Manufacturer'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')
df_grouped = df[mask].groupby(by=['Manufacturer']).count()[['Fuel_efficiency']]
df_grouped = df_grouped.reset_index()
df[mask]
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import datetime
df=pd.read_excel('1CARSALE.xlsx')
df['Latest_Launch']=pd.to_datetime(df['Latest_Launch'])
#STARTING OF THE PROGRAMME
#Adding a header and sub header to the if code
st.header("If you wish to pick a car for yourself, enter Y")
st.subheader("If you do not wish to pick a car for yourself, enter N")
#starting of the code
a=(st.text_input("Enter your choice from Y/N : "))
if a=='Y':
 
 b=(st.selectbox("CAR SURVEY FOR THE YEAR YOU WANTED TO SEE: ",
 ['A) Do you wish to see the performane of cars of year 2011...',
 'B) Do you wish to see the performane of cars of year 2012...',
 'Do you wish to see the performane of cars of years 2011 and 2012 combined...']))
 
 
 
 if b=='A) Do you wish to see the performane of cars of year 2011...':
 C=(st.selectbox("Enter your choice to see the performance of cars in 2011 in various aspects ",
 [ 'Enter 1 if you wish to see the 10 leading fuel efficient cars :', 'Enter 2 if you wish to 
see the Leading power Performance Stats : ',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 if C=='Enter 1 if you wish to see the 10 leading fuel efficient cars :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_effici
ency']]
 pd.set_option('expand_frame_repr', False)
21 
 
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 if C=='Enter 2 if you wish to see the Leading power Performance Stats:':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_per
f_factor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if C=='Enter 3 if you wish to see the Best HorsePower Engine :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepow
er']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars with best horsepower engine : \n ",ai)
 if C=='Enter 4 if you wish to see the price list of cars (from highest to lowest) :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aj=df.sort_values(by='Price_in_thousands',ascending=False)
 ak=aj[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",ak)
 if C=='Enter 5 if you wish to see the information regarding the most sold car :':
 filter1=df["Latest_Launch"]<datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 aw=al.head(1)
 am=aw[['Manufacturer','Model','Latest_Launch','Vehicle_type','Sales_in_thousands','Price_in
_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
22 
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 elif b=='B) Do you wish to see the performane of cars of year 2012...':
 d=(st.selectbox("Enter your choice to see the performance of cars in 2012 in various aspects ",
 ['Enter 1 if you wish to see the 10 leading fuel efficient cars :','Enter 2 if you wish to see 
the Leading power Performance Stats :',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 if(d=='Enter 1 if you wish to see the 10 leading fuel efficient cars :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_efficie
ncy']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 if(d=='Enter 2 if you wish to see the Leading power Performance Stats :'):
 
 filter1=df["Latest_Launch"]> datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_perf_f
actor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if(d=='Enter 3 if you wish to see the Best HorsePower Engine :'):
 filter1=df["Latest_Launch"]> datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars with best horsepower engine : \n ",ai)
 if(d=='Enter 4 if you wish to see the price list of cars (from highest to lowest) :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
23 
 aj=df.sort_values(by='Price_in_thousands',ascending=False)
 ak=aj[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",ak)
 st.bar_chart(data=ak,use_container_width=True)
 if(d=='Enter 5 if you wish to see the information regarding the most sold car :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 ay=al.head(1)
 am=ay[['Manufacturer','Model','Latest_Launch','Vehicle_type','Sales_in_thousands','Price_in_th
ousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 elif b=="Do you wish to see the performane of cars of years 2011 and 2012 combined...":
 
 t=(st.selectbox("Enter your choice to see the performance of cars in 2011 AND 2012 in various 
aspects ",
 ['Enter 1 if you wish to see the 10 leading fuel efficient cars :','Enter 2 if you wish to see 
the Leading power Performance Stats :',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 
 if(t=='Enter 1 if you wish to see the 10 leading fuel efficient cars :'):
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_efficien
cy']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 
 
 if(t=='Enter 2 if you wish to see the Leading power Performance Stats :'):
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_perf_f
actor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
24 
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if(t=='Enter 3 if you wish to see the Best HorsePower Engine :'):
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars with best horsepower engine : \n ",ai)
 if(t==' Enter 4 if you wish to see the price list of cars (from highest to lowest) :'):
 aj=df.sort_values(by='Price_in_thousands',ascending=True)
 AX=aj.head(10)
 CC=AX[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",CC)
 
 
 
 if(t=='Enter 5 if you wish to see the information regarding the most sold car :'):
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 az=al.head(1)
 am=az[['Manufacturer','Model','Vehicle_type','Sales_in_thousands','Price_in_thousands','Horse
power']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 
if a=='N':
 st.write('IF YOU WANT TO SEE DATA OF A PARTICULAR MANUFACTURE')
 
 s=(st.selectbox("SELECT THE MANUFACTURER:",
 (df['Manufacturer'].unique().tolist())))
 
 df_selection=df.query('Manufacturer == @s')
 st.write("the cars are :\n",df_selection )
 
 
25 
st.sidebar.header('THE DATA FOR THE SALES OF VECHILES FROM 2011 TO 2012 ARE GIVE IN 
THE WEB PAGE. YOU CAN ALSO CHOOSE THE MOST SUITABLE VECHILE AS PER YOUR 
CHOICE BY SELECTINGTHE SUITABLE OPTION FROM THE DATAFRAME HOPE YOU LIKED IT 
THANK YOU !')
#hello = df.
Horsepower = df["Latest_Launch"]>datetime.datetime(2011,12,31) 
st.bar_chart(data=Horsepower,use_container_width=True)
# importing the modules
from os import path
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import datetime
# giving a suitable heading to the streamlit module
st.title('CARS SURVEY 2011-2012')
st.write('THE CARSALES ARE AS FOLLOWS ')
st.balloons()
# importing the excel file and displaying the table on the screen
df = pd.read_excel('1CARSALE.xlsx',
 usecols='A,c,D:F,I,J,K,L,M,N,P',
 header=0)
st.write('the survey is as follows')
st.dataframe(df)
# displaying a pie chart on the basis of total cars sold by different manufacturers in year 2011 and 
2012
pie_chart = px.pie(df,
 title='TOTAL NUMBER OF MANUFACTURERS',
 values='Sales_in_thousands',
 names='Manufacturer')
# plotting the pie chart
st.plotly_chart(pie_chart,figsize=(20,20))
# to find the total manufactures in the year 2011 and 2012
Manufacturer = df['Manufacturer'].unique().tolist()
sales = df['Fuel_efficiency'].unique().tolist()
#horsepower = df['Horspower'].unique().tolist()
# adding a slider in our streamlit project on fuel_efficiency and different manufactures
sales_selection = st.slider('Fuel_efficiency:',
 min_value= min(sales),
 max_value= max(sales),
 value=(min(sales),max(sales)))
# adding a multi select bar with the slider
# so that the user can find therir suitable car by selecting the fuel efficiency and the manufacturer
26 
department_selection = st.multiselect('Manufacturer:',
 options=df["Manufacturer"].unique(),
 default=df["Manufacturer"].unique())
# executing the slider and multiselect
mask = (df['Fuel_efficiency'].between(*sales_selection)) & 
(df['Manufacturer'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')
df_grouped = df[mask].groupby(by=['Manufacturer']).count()[['Fuel_efficiency']]
df_grouped = df_grouped.reset_index()
df[mask]
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import datetime
df=pd.read_excel('1CARSALE.xlsx')
df['Latest_Launch']=pd.to_datetime(df['Latest_Launch'])
#STARTING OF THE PROGRAMME
#Adding a header and sub header to the if code
st.header("If you wish to pick a car for yourself, enter Y")
st.subheader("If you do not wish to pick a car for yourself, enter N")
#starting of the code
a=(st.text_input("Enter your choice from Y/N : "))
if a=='Y':
 
 b=(st.selectbox("CAR SURVEY FOR THE YEAR YOU WANTED TO SEE: ",
 ['A) Do you wish to see the performane of cars of year 2011...',
 'B) Do you wish to see the performane of cars of year 2012...',
 'Do you wish to see the performane of cars of years 2011 and 2012 combined...']))
 
 
 
 if b=='A) Do you wish to see the performane of cars of year 2011...':
 C=(st.selectbox("Enter your choice to see the performance of cars in 2011 in various aspects ",
 [ 'Enter 1 if you wish to see the 10 leading fuel efficient cars :', 'Enter 2 if you wish to 
see the Leading power Performance Stats : ',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 if C=='Enter 1 if you wish to see the 10 leading fuel efficient cars :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
27 
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_effici
ency']]
 pd.set_option('expand_frame_repr', False)
 
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 if C=='Enter 2 if you wish to see the Leading power Performance Stats:':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_per
f_factor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if C=='Enter 3 if you wish to see the Best HorsePower Engine :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepow
er']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars with best horsepower engine : \n ",ai)
 if C=='Enter 4 if you wish to see the price list of cars (from highest to lowest) :':
 filter1=df["Latest_Launch"]< datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aj=df.sort_values(by='Price_in_thousands',ascending=False)
 ak=aj[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",ak)
 if C=='Enter 5 if you wish to see the information regarding the most sold car :':
 filter1=df["Latest_Launch"]<datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 aw=al.head(1)
28 
 am=aw[['Manufacturer','Model','Latest_Launch','Vehicle_type','Sales_in_thousands','Price_in
_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 elif b=='B) Do you wish to see the performane of cars of year 2012...':
 d=(st.selectbox("Enter your choice to see the performance of cars in 2012 in various aspects ",
 ['Enter 1 if you wish to see the 10 leading fuel efficient cars :','Enter 2 if you wish to see 
the Leading power Performance Stats :',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 if(d=='Enter 1 if you wish to see the 10 leading fuel efficient cars :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_efficie
ncy']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 if(d=='Enter 2 if you wish to see the Leading power Performance Stats :'):
 
 filter1=df["Latest_Launch"]> datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_perf_f
actor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if(d=='Enter 3 if you wish to see the Best HorsePower Engine :'):
 filter1=df["Latest_Launch"]> datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
29 
 st.write("Cars with best horsepower engine : \n ",ai)
 if(d=='Enter 4 if you wish to see the price list of cars (from highest to lowest) :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 aj=df.sort_values(by='Price_in_thousands',ascending=False)
 ak=aj[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",ak)
 st.bar_chart(data=ak,use_container_width=True)
 if(d=='Enter 5 if you wish to see the information regarding the most sold car :'):
 filter1=df["Latest_Launch"]>datetime.datetime(2011,12,31)
 kk=df.where(filter1,inplace=True)
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 ay=al.head(1)
 am=ay[['Manufacturer','Model','Latest_Launch','Vehicle_type','Sales_in_thousands','Price_in_th
ousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 elif b=="Do you wish to see the performane of cars of years 2011 and 2012 combined...":
 
 t=(st.selectbox("Enter your choice to see the performance of cars in 2011 AND 2012 in various 
aspects ",
 ['Enter 1 if you wish to see the 10 leading fuel efficient cars :','Enter 2 if you wish to see 
the Leading power Performance Stats :',
 'Enter 3 if you wish to see the Best HorsePower Engine :','Enter 4 if you wish to see 
the price list of cars (from highest to lowest) :',
 'Enter 5 if you wish to see the information regarding the most sold car :']))
 
 
 if(t=='Enter 1 if you wish to see the 10 leading fuel efficient cars :'):
 aa=df.sort_values(by='Fuel_efficiency',ascending=False)
 ab=aa.head(10)
 ac=ab[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Fuel_efficien
cy']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("10 leading fuel efficient cars are : \n ",ac)
 
 
 if(t=='Enter 2 if you wish to see the Leading power Performance Stats :'):
 ad=df.sort_values(by='Power_perf_factor',ascending=False)
30 
 ae=ad.head(1)
 af=ae[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Power_perf_f
actor']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars for leading Power performance stats are : \n ",af)
 if(t=='Enter 3 if you wish to see the Best HorsePower Engine :'):
 ag=df.sort_values(by='Horsepower',ascending=False)
 ah=ag.head(1)
 ai=ah[['Manufacturer','Model','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("Cars with best horsepower engine : \n ",ai)
 if(t==' Enter 4 if you wish to see the price list of cars (from highest to lowest) :'):
 aj=df.sort_values(by='Price_in_thousands',ascending=True)
 AX=aj.head(10)
 CC=AX[['Manufacturer','Latest_Launch','Vehicle_type','Price_in_thousands','Horsepower']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",CC)
 
 
 
 if(t=='Enter 5 if you wish to see the information regarding the most sold car :'):
 al=df.sort_values(by='Sales_in_thousands',ascending=False)
 az=al.head(1)
 am=az[['Manufacturer','Model','Vehicle_type','Sales_in_thousands','Price_in_thousands','Horse
power']]
 pd.set_option('expand_frame_repr', False)
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.max_colwidth', None)
 st.write("price list of the cars : \n ",am)
 
if a=='N':
 st.write('IF YOU WANT TO SEE DATA OF A PARTICULAR MANUFACTURE')
 
 s=(st.selectbox("SELECT THE MANUFACTURER:",
 (df['Manufacturer'].unique().tolist())))
 
 df_selection=df.query('Manufacturer == @s')
31 
 st.write("the cars are :\n",df_selection )
 
 
st.sidebar.header('THE DATA FOR THE SALES OF VECHILES FROM 2011 TO 2012 ARE GIVE IN 
THE WEB PAGE. YOU CAN ALSO CHOOSE THE MOST SUITABLE VECHILE AS PER YOUR 
CHOICE BY SELECTINGTHE SUITABLE OPTION FROM THE DATAFRAME HOPE YOU LIKED IT 
THANK YOU !')
#hello = df.
Horsepower = df["Latest_Launch"]>datetime.datetime(2011,12,31) 
st.bar_chart(data=Horsepower,use_container_width=True