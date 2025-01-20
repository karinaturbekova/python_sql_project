#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv
from typing import Dict



load_dotenv()

def get_db_config() -> Dict:
    config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME'),
    }
    return config
    


# config = get_db_config()

# print(config)


# In[ ]:





# In[ ]:




