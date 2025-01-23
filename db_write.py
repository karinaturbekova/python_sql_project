#!/usr/bin/env python
# coding: utf-8

# In[1]:


from envar import get_db_config
import mysql.connector
from typing import List, Dict
from my_exceptions import validate_string_input, validate_integer_input, validate_db_connection, QueryExecutionError, InvalidInputError, DatabaseConnectionError

class DatabaseWriter:
    def __init__(self, db_config: Dict[str, str]):
        self.connection = mysql.connector.connect(**db_config)

    def write_keywords_to_table(self, parameter: str) -> str:
        # Insert a keyword into the search history table
        try:
            parameter = validate_string_input(parameter, "Keyword")
            
            with self.connection.cursor(dictionary=True) as cursor:
                query = '''INSERT INTO search_history 
                            	(key_words)
                            VALUES
                            	(%s);'''
                cursor.execute(query, (parameter,))
                self.connection.commit()
            return f"Keyword '{parameter}' successfully inserted."
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the insert query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

# In[ ]:




