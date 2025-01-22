#!/usr/bin/env python
# coding: utf-8

# In[8]:


from envar import get_db_config
import mysql.connector
import db, db_write
import service
from typing import List, Tuple

db_reader = db.DatabaseReader(get_db_config())
db_writer = db_write.DatabaseWriter(get_db_config())
movie_service = service.MovieService(db_reader, db_writer)


def display_menu() -> None:
    print("Choose an option:")
    print("1. Search movies by title")
    print("2. Search movies by description")
    print("3. Search movies by actor")
    print("4. Search movies by genre")
    print("5. Search movies by release year")
    print("6. Search movies by genre and release year")
    print("7. Popular Searches")

def search_by_keyword(option_name: str) -> List[Tuple]:
    keyword = input(f"Enter a keyword for {option_name}: ")
    print(f"Searching movies by {option_name} with keyword: '{keyword}'")
    movies = movie_service.search_by_keyword(option_name, keyword)

    return movies

def search_by_genre() -> List[Tuple]:
    genres = movie_service.genre_list()
    print("Select a genre:")
    print_genre = map(lambda item: f"{item[0]}. {item[1]}", genres)
    print(*print_genre, sep="\n")
    
    choice = input("Enter the genre number or name: ")
    keyword = select_genre(genres, choice)

    print(f"Searching movies by genre: '{keyword}'")
    movies = movie_service.search_by_genre(keyword)
    return movies


def select_genre(genres: List[Tuple], choice: str) -> str:
    keyword = ''
    if choice.isdigit() and 1 <= int(choice) <= len(genres):
        keyword = genres[int(choice) - 1]
        keyword = keyword[1]
    else:
        keyword = choice

    return keyword

def search_by_year() -> List[Tuple]:    
    year = input("Enter a release year: ")
    # try 
    #     year_int = int(year)
    # except Exception as e:
    #     print(e)
    print(f"Searching movies by release year: '{year}'")
    movies = movie_service.search_by_year(year)
    return movies

def search_by_genre_and_year() -> List[Tuple]:
    print("First, choose a genre.")  
    genres = movie_service.genre_list()
    print("Select a genre:")
    print_genre = map(lambda item: f"{item[0]}. {item[1]}", genres)
    print(*print_genre, sep="\n")
    choice = input("Enter the genre number or name: ")
    genre_keyword = select_genre(genres, choice)
    year_keyword = input("Enter a release year: ") 
    print(f"Searching movies by genre and year: '{genre_keyword} {year_keyword}'")
    movies = movie_service.search_by_genre_and_year(genre_keyword, year_keyword)
    return movies

def show_popular_searches() -> List[Tuple]:
    print("Popular Searches:")
    popular_searches = movie_service.show_popular_searches()
    return popular_searches

def main() -> None:
    display_menu()
    choice = input("Enter your choice (1-7): ")
    movies = list[tuple]
    if choice == "1":
        movies = search_by_keyword("title")
    elif choice == "2":
        movies = search_by_keyword("description")
    elif choice == "3":
        movies = search_by_keyword("actor")
    elif choice == "4":
        movies = search_by_genre()
    elif choice == "5":
        movies = search_by_year()
    elif choice == "6":
        movies = search_by_genre_and_year()
    elif choice == "7":
        movies = show_popular_searches()
    else:
        print('error')
        return

    
    lengths = [len(movie) for movie in movies]
    if lengths[0] == 1:
        movies = map(lambda item: f"{item[0]}", movies)
        print(*movies, sep="\n")
    elif lengths[0] == 5:
        movies = map(lambda item: f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}", movies)
        print(*movies, sep="\n")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




