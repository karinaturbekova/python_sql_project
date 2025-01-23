from envar import get_db_config
import mysql.connector
import db, db_write
import service
from typing import List, Tuple
from tabulate import tabulate
from my_exceptions import InvalidInputError, QueryExecutionError

class MovieSearchUI:
    def __init__(self, movie_service: service.MovieService):
        # Initialize the UI with a MovieService instance
        self.movie_service = movie_service

    def display_menu(self) -> None:
        options = [
            "Search movies by title",
            "Search movies by description",
            "Search movies by actor",
            "Search movies by genre",
            "Search movies by release year",
            "Search movies by genre and release year",
            "Popular Searches",
            "Stop"
        ]
        
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def search_by_keyword(self, option_name: str) -> List[Tuple]:
        # Search for movies based on a keyword (e.g., title, description, or actor)
        keyword = input(f"Enter a keyword for {option_name}: ")
        try:  
            print(f"Searching movies by {option_name} with keyword: '{keyword}'")
            movies = self.movie_service.search_by_keyword(option_name, keyword)
            return movies
        except InvalidInputError as e:  
            print(f"Error: {e}")  
        except QueryExecutionError as e:  
            print(f"Error during search: {e}")  
        return []  

    def search_by_genre(self) -> List[Tuple]:
        # Search for movies by genre
        try:  
            genres = self.movie_service.genre_list()
            print("Select a genre:")
            print_genre = map(lambda item: f"{item[0]}. {item[1]}", genres)
            print(*print_genre, sep="\n")
            
            choice = input("Enter the genre number or name: ")
            keyword = self.select_genre(genres, choice)
        
            print(f"Searching movies by genre: '{keyword}'")
            movies = self.movie_service.search_by_genre(keyword)
            return movies
        except InvalidInputError as e:  
            print(f"Error: {e}")  
        except QueryExecutionError as e:  
            print(f"Error during search: {e}")  
        return []  

    def select_genre(self, genres: List[Tuple], choice: str) -> str:
        # Helper method to select a genre based on user input
        try:  
            if choice.isdigit():
                choice_int = int(choice)
                if 1 <= choice_int <= len(genres):
                    return genres[choice_int - 1][1]
            return choice.strip()
        except Exception:  
            raise InvalidInputError("Invalid genre selection.")  

    def search_by_year(self) -> List[Tuple]:
         # Search for movies by release year
        year = input("Enter a release year: ")
        try:  
            print(f"Searching movies by release year: '{year}'")
            movies = self.movie_service.search_by_year(year)
            return movies
        except InvalidInputError as e:  
            print(f"Error: {e}")  
        except QueryExecutionError as e:  
            print(f"Error during search: {e}")  
        return []  

    def search_by_genre_and_year(self) -> List[Tuple]:
        # Search for movies by both genre and release year
        try:  
            print("First, choose a genre.")  
            genres = self.movie_service.genre_list()
            print("Select a genre:")
            print_genre = map(lambda item: f"{item[0]}. {item[1]}", genres)
            print(*print_genre, sep="\n")
            choice = input("Enter the genre number or name: ")
            genre_keyword = self.select_genre(genres, choice)
            
            year_keyword = input("Enter a release year: ") 
            print(f"Searching movies by genre and year: '{genre_keyword} {year_keyword}'")
            movies = self.movie_service.search_by_genre_and_year(genre_keyword, year_keyword)
            return movies
        except InvalidInputError as e:  
            print(f"Error: {e}")  
        except QueryExecutionError as e:  
            print(f"Error during search: {e}")  
        return []  

    def show_popular_searches(self) -> List[Tuple]:
        # Display the most popular searches
        try:  
            print("Popular Searches:")
            popular_searches = self.movie_service.show_popular_searches()
            return popular_searches
        except QueryExecutionError as e:  
            print(f"Error during search: {e}")  
        return []  

    def display_results(self, movies: List[Tuple]) -> None:
        # Display movies in a tabular format
        if not movies:
            print("No results found.\n")
            return

        headers = ["Title", "Genre", "Description", "Release Year", "Actor"]
        print(tabulate(movies, headers=headers, tablefmt="grid"))
        
    def start(self) -> None:
        # Start the UI and handle user menu selection
        self.display_menu()
        choice = input("\nEnter your choice (1-8): ")
        movies = []
        if choice == "1":
            movies = self.search_by_keyword("title")
        elif choice == "2":
            movies = self.search_by_keyword("description")
        elif choice == "3":
            movies = self.search_by_keyword("actor")
        elif choice == "4":
            movies = self.search_by_genre()
        elif choice == "5":
            movies = self.search_by_year()
        elif choice == "6":
            movies = self.search_by_genre_and_year()
        elif choice == "7":
            movies = self.show_popular_searches()
        elif choice == "8":
            print("Goodbye!") # Exit the program
            return 'stop'
        else:
            print("Invalid choice. Please try again.")
            return
        
        self.display_results(movies) # Display search results


