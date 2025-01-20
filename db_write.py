#!/usr/bin/env python
# coding: utf-8

# In[2]:


from envar import get_db_config
import mysql.connector

connection = mysql.connector.connect(**get_db_config())

def write_keywords_to_table(connection, parameter: str) -> str:
    
    with connection.cursor(dictionary=True) as cursor:
        query = '''INSERT INTO search_history 
                    	(key_words) 
                    VALUES 
                    	(%s);'''
        cursor.execute(query, (parameter,))
        connection.commit()  # Подтверждение изменений
    return f"Keyword '{parameter}' successfully inserted."

def show_popular_keywords(connection) -> list[dict]:
    
    with connection.cursor(dictionary=True) as cursor:
        query = '''SELECT 
                        key_words, COUNT(*) AS count_of_key_words
                    FROM
                        search_history
                    GROUP BY key_words
                    ORDER BY count_of_key_words DESC;'''
        cursor.execute(query)
        result = cursor.fetchall() 
    return result


# print(write_keywords_to_table(connection, 'Johnny_2024'))
# print(show_popular_keywords(connection))


# In[ ]:




