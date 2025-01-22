#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv
from typing import Dict

def get_db_config() -> Dict[str, str]:
    load_dotenv()
    config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME'),
    }
    return config


# In[ ]:





# In[ ]:




