from envar import get_db_config
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import List, Tuple, Dict
from my_exceptions import validate_string_input, validate_integer_input, validate_db_connection, QueryExecutionError, QueryExecutionError, InvalidInputError, DatabaseConnectionError

class DatabaseReader:
    def __init__(self, db_config: Dict[str, str]):
        self.connection = mysql.connector.connect(**db_config)

    def search_movie_by_title(self, parameter: str) -> List[Tuple]:
        try:
            parameter = validate_string_input(parameter, "Movie Title")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def search_movie_by_description(self, parameter: str) -> List[Tuple]:
        try:
            parameter = validate_string_input(parameter, "Movie Description")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def search_movie_by_actor(self, parameter: str) -> List[Tuple]:
        try:
            parameter = validate_string_input(parameter, "Actor Name")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def search_movie_by_genre(self, parameter: str) -> List[Tuple]:
        try:
            parameter = validate_string_input(parameter, "Genre")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def search_movie_by_release_year(self, parameter: str) -> List[Tuple]:
        try:
            parameter = validate_integer_input(parameter, "Release Year")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def search_movie_by_genre_release_year(self, parameter1: str, parameter2: str) -> List[Tuple]:
        try:
            parameter1 = validate_string_input(parameter1, "Genre")
            parameter2 = validate_integer_input(parameter2, "Release Year")
            with self.connection.cursor() as cursor:
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
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")
        except InvalidInputError as e:
            raise InvalidInputError(f"Validation failed for input: {e}")

    def genre_list(self) -> List[Tuple]:
        try:
            validate_db_connection(self.connection)
            with self.connection.cursor() as cursor:
                base_query = '''SELECT 
                                    category_id, name
                                FROM
                                    category;'''
                cursor.execute(base_query)
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")

    def get_popular_searches(self) -> List[Tuple]:
        try:
            validate_db_connection(self.connection)
            with self.connection.cursor() as cursor:
                base_query = '''SELECT 
                                    key_words
                                FROM
                                    search_history
                                GROUP BY key_words
                                ORDER BY COUNT(*) DESC
                                LIMIT 10;'''
                cursor.execute(base_query)
                result: List[Tuple] = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryExecutionError(f"An error occurred while executing the query: {e}")

