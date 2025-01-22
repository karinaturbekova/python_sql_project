#!/usr/bin/env python
# coding: utf-8

# In[3]:


from envar import get_db_config
import mysql.connector
import db, db_write
from typing import List, Tuple

class MovieService:
    def __init__(self, db_reader: db.DatabaseReader, db_writer: db_write.DatabaseWriter):
        self.db_reader = db_reader
        self.db_writer = db_writer

    def search_by_keyword(self, option_name: str, keyword: str) -> List[Tuple]:
        self.db_writer.write_keywords_to_table(keyword) 
        movies: List[Tuple] = []
        if option_name == 'title':
            movies = self.db_reader.search_movie_by_title(keyword)
    
        elif option_name == 'description':
            movies = self.db_reader.search_movie_by_description(keyword)
    
        elif option_name == 'actor':
            movies = self.db_reader.search_movie_by_actor(keyword)
    
        return movies

    def genre_list(self) -> List[Tuple]:
        genres = self.db_reader.genre_list()
        return genres

    def search_by_genre(self, keyword: str) -> List[Tuple]:      
        self.db_writer.write_keywords_to_table(keyword)
        movies = self.db_reader.search_movie_by_genre(keyword)    
        return movies

    def search_by_year(self, year: str) -> List[Tuple]:    
        self.db_writer.write_keywords_to_table(year)
        movies = self.db_reader.search_movie_by_release_year(year)      
        return movies

    def search_by_genre_and_year(self, genre_keyword: str, year_keyword: str) -> List[Tuple]:
        self.db_writer.write_keywords_to_table(f'{genre_keyword} {year_keyword}')
        movies = self.db_reader.search_movie_by_genre_release_year(genre_keyword, year_keyword)
        return movies

    def show_popular_searches(self) -> List[Tuple]:    
        popular_searches = self.db_reader.get_popular_searches()
        return popular_searches


# In[ ]:




