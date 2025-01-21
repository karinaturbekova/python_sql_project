#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from envar import get_db_config
import mysql.connector
import db, db_write
from typing import List, Tuple

connection = mysql.connector.connect(**get_db_config())

def search_by_keyword(option_name: str, keyword: str) -> List[Tuple]:
    db_write.write_keywords_to_table(connection, keyword) 
    movies: List[Tuple] = []
    if option_name == 'title':
        movies = db.search_movie_by_title(connection, keyword)

    elif option_name == 'description':
        movies = db.search_movie_by_description(connection, keyword)

    elif option_name == 'actor':
        movies = db.search_movie_by_actor(connection, keyword)

    return movies

def genre_list() -> List[Tuple]:
    genres = db.genre_list(connection)
    return genres

def search_by_genre(keyword: str) -> List[Tuple]:      
    db_write.write_keywords_to_table(connection, keyword)
    movies = db.search_movie_by_genre(connection, keyword)    
    return movies   

def search_by_year(year: str) -> List[Tuple]:    
    db_write.write_keywords_to_table(connection, year)
    movies = db.search_movie_by_release_year(connection, year)      
    return movies

def search_by_genre_and_year(genre_keyword: str, year_keyword: str) -> List[Tuple]:
    db_write.write_keywords_to_table(connection, f'{genre_keyword} {year_keyword}')
    movies = db.search_movie_by_genre_release_year(connection, genre_keyword, year_keyword)
    return movies

def show_popular_searches() -> List[Tuple]:    
    popular_searches = db.get_popular_searches(connection)
    return popular_searches


    