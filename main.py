#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from envar import get_db_config
import mysql.connector
import db, db_write
import service
import ui
from my_exceptions import InvalidInputError, DatabaseConnectionError, QueryExecutionError

def main():
    db_reader = db.DatabaseReader(get_db_config())
    db_writer = db_write.DatabaseWriter(get_db_config())
    movie_service = service.MovieService(db_reader, db_writer)
    movie_ui = ui.MovieSearchUI(movie_service)
    while True:
        stop = movie_ui.start()
        if stop == 'stop':
            break 

if __name__ == '__main__':
    main()
    

