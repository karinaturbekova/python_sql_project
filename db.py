#!/usr/bin/env python
# coding: utf-8

# In[2]:


from envar import get_db_config
import mysql.connector
from mysql.connector.connection import MySQLConnection

connection = mysql.connector.connect(**get_db_config())

def search_movie_by_title(connection: MySQLConnection, parameter: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    WHERE
                    	f.title LIKE %s
                    GROUP BY
                        f.film_id
                    LIMIT 10;'''
        cursor.execute(query, (f'%{parameter}%',))
        result = cursor.fetchall()
            
    return result

def search_movie_by_description(connection: MySQLConnection, parameter: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    WHERE
                        description LIKE %s
                    GROUP BY
                        f.film_id
                    LIMIT 10;'''
        cursor.execute(query, (f'%{parameter}%',))
        result = cursor.fetchall()
            
    return result

def search_movie_by_actor(connection: MySQLConnection, parameter: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    GROUP BY
                        f.film_id
                    HAVING 
                        SUM(CONCAT(a.first_name, ' ', a.last_name) LIKE %s) > 0
                    LIMIT 10;'''
        cursor.execute(query, (f'%{parameter}%',))
        result = cursor.fetchall()
            
    return result

def search_movie_by_genre(connection: MySQLConnection, parameter: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    WHERE
                        c.name = %s
                    GROUP BY
                        f.film_id
                    LIMIT 10;'''
        cursor.execute(query, (parameter,))
        result = cursor.fetchall()

    return result

def search_movie_by_release_year(connection: MySQLConnection, parameter: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    WHERE
                        f.release_year = %s
                    GROUP BY
                        f.film_id
                    LIMIT 10;'''
        cursor.execute(query, (parameter,))
        result = cursor.fetchall()
            
    return result

def search_movie_by_genre_release_year(connection: MySQLConnection, parameter1: str, parameter2: str) -> list[tuple]:
    
    with connection.cursor() as cursor:
        query = '''SELECT 
                        f.title AS film_title,
                        c.name AS genre,
                        f.description AS description,
                        f.release_year AS release_year,
                        GROUP_CONCAT(CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
                    FROM
                        film f
                            JOIN
                        film_actor fa ON f.film_id = fa.film_id
                            JOIN
                        actor a ON fa.actor_id = a.actor_id
                            JOIN
                        film_category fc ON f.film_id = fc.film_id
                            JOIN
                        category c ON fc.category_id = c.category_id
                    WHERE
                        c.name = %s AND f.release_year = %s 
                    GROUP BY
                        f.film_id
                    LIMIT 10;'''
        cursor.execute(query, (parameter1, parameter2,))
        result = cursor.fetchall()
            
    return result

def genre_list(connection: MySQLConnection) -> list[tuple]:

    with connection.cursor() as cursor:
        base_query = '''SELECT 
                            category_id, name
                        FROM
                            category;'''
        cursor.execute(base_query)
        result = cursor.fetchall()
        
    return result

def get_popular_searches(connection: MySQLConnection) -> list[tuple]:

    with connection.cursor() as cursor:
        base_query = '''SELECT 
                            key_words
                        FROM
                            search_history
                        GROUP BY key_words
                        ORDER BY COUNT(*) DESC
                        LIMIT 10;'''
        cursor.execute(base_query)
        result = cursor.fetchall()
        
    return result

# print(get_popular_searches(connection))


# if connection.is_connected():
    
#     print(search_movie_by_title(connection, 'academy'))
#     print(search_movie_by_description(connection, 'drama'))
#     print(search_movie_by_actor(connection, 'JOHNNY'))
#     print(search_movie_by_genre(connection, 'Action'))
#     print(search_movie_by_release_year(connection, '2006'))
#     print(search_movie_by_genre_release_year(connection, 'Action', '2006'))
    # for row in results:
    #         print(row) 
    
    # connection.close()

# try:
#     if connection.is_connected():
#         print("Search by title:")
#         results = search_movie_by_title(connection, 'academy')
#         for row in results:
#             print(row)

#         print("\nSearch by description:")
#         results = search_movie_by_description(connection, 'drama')
#         for row in results:
#             print(row)

#         print("\nSearch by actor:")
#         results = search_movie_by_actor(connection, 'JOHNNY')
#         for row in results:
#             print(row)

        # print("\nSearch by genre:")
        # results = search_movie_by_genre(connection, 'Action')
        # for row in results:
        #     print(row)

#         print("\nSearch by release year:")
#         results = search_movie_by_release_year(connection, '2006')
#         for row in results:
#             print(row)

#         print("\nSearch by genre and release year:")
#         results = search_movie_by_genre_release_year(connection, 'Action', '2006')
#         for row in results:
#             print(row)

#         print("\n Genre list:")
#         categories = genre_list(connection)
#         categories = map(lambda item: f"{item[0]}. {item[1]}", categories)
#         print(*categories, sep="\n")

# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     if connection.is_connected():
#         connection.close()
#         print("\nConnection closed.")





# In[ ]:




