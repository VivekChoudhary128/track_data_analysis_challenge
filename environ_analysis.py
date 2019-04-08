
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sns
import requests as req
import json
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


class TrackAnalysis:
    
    
    def __init__(self, entities_limit=100, pages=0, api='tracks'):
        self.endpoint_ = 'https://envirocar.org/api/stable/'
        self.entities_limit = entities_limit
        self.page_limit = pages
        self.avail_apis = req.get('https://envirocar.org/api/stable/').json()
        self.api = api
        
        if api not in self.avail_apis.keys():
            raise Exception('ValueError: Attepmt to call non-extistent api must be from *{f}')

#     def get_data(self):
#         dat = req.get('https://envirocar.org/api/stable/' + self.api + '?', params={'limit': self.entities_limit, 'page': self.page_limit})
#         print(dat)
        
    def plot_(self):
        dat = req.get('https://envirocar.org/api/stable/' + self.api, params={'limit': self.entities_limit, 'page': self.page_limit})
        print(dat.json())

#         dat = req.get('https://envirocar.org/api/stable/' + self.api + '1.csv')
        
    def set_page_lim(self, n=None):
        if not num:
            pass
        else:
            self.page_limit = n
            
    def set_data_lim(self, n=None):
        
        if not num:
            pass
        if num > 100:
            raise Exception('DataError: lim must be < 100')
        else:
            self.entities_limit = n
                
TrackAnalysis().plot_()


# In[ ]:


track_data

