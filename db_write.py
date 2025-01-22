#!/usr/bin/env python
# coding: utf-8

# In[1]:


from envar import get_db_config
import mysql.connector
from typing import List, Dict

class DatabaseWriter:
    def __init__(self, db_config: Dict[str, str]):
        self.connection = mysql.connector.connect(**db_config)

    def write_keywords_to_table(self, parameter: str) -> str:
        
        with self.connection.cursor(dictionary=True) as cursor:
            query = '''INSERT INTO search_history 
                        	(key_words)
                        VALUES
                        	(%s);'''
            cursor.execute(query, (parameter,))
            self.connection.commit() 
        return f"Keyword '{parameter}' successfully inserted."


# In[ ]:




