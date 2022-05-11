#!/usr/bin/env python
# coding: utf-8

# In[65]:


import os
import urllib
from urllib.request import urlopen
import json
from datetime import datetime
import pandas as pd


# In[46]:


def myFunction(forexticker, multiplier, timespan, timefrom, timeto, apikey):
    myurl = "https://api.polygon.io/v2/aggs/ticker/" + forexticker + "/range/" + multiplier + "/" + timespan + "/" + timefrom + "/" + timeto + "?apiKey=" + apikey
    with urlopen(myurl) as response:
        responsebody = response.read()
    return json.loads(responsebody)


# In[77]:


forexticker = "C:USDCAD" # the currency pair to return. Good options are dollar to euro USDEUR, 
                         # US dollar to Canadaian dollar USDCAD, dollar to yen USDJPY
multiplier = "1"
timespan = "week"
timefrom = "2021-04-19"
timeto = "2022-04-19"
apikey = "XtZtNQCOEtrjxrsh8uKbYhK2VExPaeWb"
myjson = myFunction(forexticker, multiplier, timespan, timefrom, timeto, apikey)
date, volume = [], []
print(date, volume)


for i in range(len(myjson["results"])):
    #for the length of the list returned by the api, do the loop
    
    t = int((myjson["results"][i]['t'])/1000 )    
    #datetime is returned in miliseconds which I kept getting errors when converting to a date. 
    #so dividing by 1000 and casting to interger puts it in the correct length and format when using datetime.fromtimestamp
    
    date.append(datetime.fromtimestamp(t).strftime("%m-%d-%y"))
    volume.append(myjson["results"][i]['v'])
    
print(date)
print(volume)


# In[78]:


#creating a pandas dataframe to export as a csv
myFrame = {
    'date': date,
    'volume': volume
}

polygonIO = pd.DataFrame(myFrame)
print(polygonIO)


# In[79]:


polygonIO.to_csv(r'C:\Users\Jordan\Documents\Masters Degree\Spring\Hyowon\polygonIO_USDCAD.csv')


# In[ ]:




