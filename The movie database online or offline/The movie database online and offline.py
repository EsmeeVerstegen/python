# import of python modules
import configparser
import time
import requests

# import of the movie database module
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import TV
from tmdbv3api import Person

# variables for the movie database module
tmdb = TMDb()
movie = Movie()
tv = TV()
person = Person()

# reading the ini files for the offline genres of movies and series
config = configparser.ConfigParser()
config.read("moviegenre.ini")
config.read("seriegenre.ini")

# start by asking The movie database account or not
def start():
    TMDB_or_not = input("Do you have an account for The movie database? type 'y' for yes and 'n' for no   ")
    if(TMDB_or_not == "y"):
        print("You selected yes, you will be directed to The movie database login.")
        print("")
        time.sleep(3)
        TMDB_account()

    if(TMDB_or_not == "n"):
        print("You selected no, you will be directed to a offline movies or series list.")
        print("")
        time.sleep(3)
        movie_or_serie()

    else:
        print("Error you didn't type 'y' for yes or 'n' for no, Please check if you used lower case letters and try again. (example: y)")
        time.sleep(2)
        start()


# Do you want to watch a Movie or serie or go back to the last question?
def movie_or_serie():
    movie_serie = input("Would you like to search for a movie or a serie? If you want to go back type back. (example: movie)   ")
    if (movie_serie == "movie"):
        print("You selected movie! Here is a list with genres.")
        print("")
        time.sleep(3)
        movie_genre()

    if(movie_serie == "serie"):
        print("You selected serie! Here is a list with genres.")
        print("")
        time.sleep(3)
        serie_genre()

    if(movie_serie == "back"):
        print("You will go back to the last question.")
        print("")
        time.sleep(3)
        start()

    else:
        print("Error you didn't type movie, serie or back, please check if you used lower case letters and try again.")
        time.sleep(2)
        movie_or_serie()


# Pick the genre of movies you would like to watch
def movie_genre():
    print("Type 0 to go back to the last question.")
    print("Type 1 for Action movies")
    print("Type 2 for Comedy movies")
    print("Type 3 for Horror movies")
    print("Type 4 for LGBTQ+ movies")
    print("Type 5 for Drama movies")
    print("Type 6 for Fantasy movies")
    print("Type 7 for Kids movies")
    print("")
    genre_movie = input("What genre would you like to watch? (Type the number of the genre)  ")
    if(genre_movie == "0"):
        print("You selected 0 to go back to the last question.")
        time.sleep(2)
        movie_or_serie()
    
    if(genre_movie == "1"):
        print("You selected 1 to see a list of the top 5 Action movies.")
        time.sleep(2)
        movie1 = config['Action']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Action']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Action']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Action']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Action']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "2"):
        print("You selected 2 to see a list of the top 5 Comedy movies.")
        time.sleep(2)
        movie1 = config['Comedy']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Comedy']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Comedy']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Comedy']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Comedy']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "3"):
        print("You selected 3 to see a list of the top 5 Horror movies.")
        time.sleep(2)
        movie1 = config['Horror']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Horror']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Horror']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Horror']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Horror']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "4"):
        print("You selected 4 to see a list of the top 5 LGBTQ+ movies.")
        time.sleep(2)
        movie1 = config['LGBTQ+']['movie 1']
        print(movie1)
        print("")
        movie2 = config['LGBTQ+']['movie 2']
        print(movie2)
        print("")
        movie3 = config['LGBTQ+']['movie 3']
        print(movie3)
        print("")
        movie4 = config['LGBTQ+']['movie 4']
        print(movie4)
        print("")
        movie5 = config['LGBTQ+']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "5"):
        print("You selected 5 to see a list of the top 5 Drama movies.")
        time.sleep(2)
        movie1 = config['Drama']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Drama']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Drama']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Drama']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Drama']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "6"):
        print("You selected 6 to see a list of the top 5 Fantasy movies.")
        time.sleep(2)
        movie1 = config['Fantasy']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Fantasy']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Fantasy']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Fantasy']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Fantasy']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_movie == "7"):
        print("You selected 7 to see a list of the top 5 Kids movies.")
        time.sleep(2)
        movie1 = config['Kids']['movie 1']
        print(movie1)
        print("")
        movie2 = config['Kids']['movie 2']
        print(movie2)
        print("")
        movie3 = config['Kids']['movie 3']
        print(movie3)
        print("")
        movie4 = config['Kids']['movie 4']
        print(movie4)
        print("")
        movie5 = config['Kids']['movie 5']
        print(movie5)
        print("")
        time.sleep(2)
        restart()

    else:
        print("You didn't type in one of the numbers in the list, Please try again.")
        time.sleep(2)
        movie_genre()


# Pick the genre of series you would like to watch.
def serie_genre():
    print("Type 0 to go back to the last question.")
    print("Type 1 for Action series")
    print("Type 2 for Comedy series")
    print("Type 3 for Horror series")
    print("Type 4 for LGBTQ+ series")
    print("Type 5 for Drama series")
    print("Type 6 for Fantasy series")
    print("Type 7 for Kids series")
    print("")
    genre_serie = input("What genre would you like to watch?  ")
    if(genre_serie == "0"):
        print("You selected 0 to go back to the last question.")
        time.sleep(2)
        movie_or_serie()
    
    if(genre_serie == "1"):
        print("You selected 1 to see a list of the top 5 Action series.")
        time.sleep(2)
        serie1 = config['Action']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Action']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Action']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Action']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Action']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "2"):
        print("You selected 2 to see a list of the top 5 Comedy series.")
        time.sleep(2)
        serie1 = config['Comedy']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Comedy']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Comedy']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Comedy']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Comedy']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "3"):
        print("You selected 3 to see a list of the top 5 Horror series.")
        time.sleep(2)
        serie1 = config['Horror']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Horror']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Horror']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Horror']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Horror']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "4"):
        print("You selected 4 to see a list of the top 5 LGBTQ+ series.")
        time.sleep(2)
        serie1 = config['LGBTQ+']['serie 1']
        print(serie1)
        print("")
        serie2 = config['LGBTQ+']['serie 2']
        print(serie2)
        print("")
        serie3 = config['LGBTQ+']['serie 3']
        print(serie3)
        print("")
        serie4 = config['LGBTQ+']['serie 4']
        print(serie4)
        print("")
        serie5 = config['LGBTQ+']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "5"):
        print("You selected 5 to see a list of the top 5 Drama series.")
        time.sleep(2)
        serie1 = config['Drama']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Drama']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Drama']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Drama']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Drama']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "6"):
        print("You selected 5 to see a list of the top 5 Fantasy series.")
        time.sleep(2)
        serie1 = config['Fantasy']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Fantasy']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Fantasy']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Fantasy']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Fantasy']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()
    
    if(genre_serie == "7"):
        print("You selected 7 to see a list of the top 5 Kids series.")
        time.sleep(2)
        serie1 = config['Kids']['serie 1']
        print(serie1)
        print("")
        serie2 = config['Kids']['serie 2']
        print(serie2)
        print("")
        serie3 = config['Kids']['serie 3']
        print(serie3)
        print("")
        serie4 = config['Kids']['serie 4']
        print(serie4)
        print("")
        serie5 = config['Kids']['serie 5']
        print(serie5)
        print("")
        time.sleep(2)
        restart()

    else:
        print("You didn't type in one of the numbers in the list, Please try again.")
        time.sleep(2)
        serie_genre()

# Do you want to restart the program to see a different genre?
def restart():
    start_again = input("Would you like to see a different genre? type y for yes and n for no.     ")
    if(start_again == "y"):
        start()

    if(start_again == "n"):
        exit()

    else:
        print("You didn't type y or n, please check if you used lower case letters and try again.")
        restart()


# The movie database account login
def TMDB_account():
    TMDB_inlog = input("Are you sure you have an account for The movie database? type y to go to the login and n to go to the offline list.   ")
    print("")
    if(TMDB_inlog == "y"):
        tmdb.api_key = input("Fill in your personal login token (api key):   ")
        options_tmdb()
    
    if(TMDB_inlog == "n"):
        print("You will be directed to our offline list of movies and series.")
        print("")
        time.sleep(2)
        movie_or_serie()

    else:
        print("Error you didn't type 'y' for yes or 'n' for no, Please check if you used lower case letters and try again. (example: y).")
        time.sleep(2)
        TMDB_account()


# List of options you can choose to see online
def options_tmdb():
    print("")
    print("Type 0 to go exit the program.")
    print("Type 1 to get a list of the top 20 popular movies.")
    print("Type 2 to search for a movie.")
    print("Type 3 to see movie details by ID.")
    print("Type 4 to search for a serie.")
    print("Type 5 to search for information about a actor or actress.")
    TMDB_options = input("What do you want to do on The movie database? Type a number from one of the options above.    ")
    print("")
    if(TMDB_options == "0"):
        exit()

    if(TMDB_options == "1"):
        popular = movie.popular()
        for p in popular:
            print("ID:", p.id)
            print("Title:", p.title)
            print("__________________________________________________")
            print("")
        time.sleep(3)
        options_tmdb()

    if(TMDB_options == "2"):
        search_input = input("Type here the name of the movie you want to search:   ")
        search_movie = movie.search(search_input)
        for res in search_movie:
            print("Movie ID:", res.id)
            print("Movie Title:", res.title)
            print("Average rating movie:", res.vote_average)
            print("__________________________________________________")
            print("")
        time.sleep(3)
        options_tmdb()

    if(TMDB_options == "3"):
        input_id = input("What is the ID of the movie you want to know more about?   ")
        m = movie.details(input_id)
        print("Movie title:", m.title)
        print("")
        print("Movie description:")
        print(m.overview)
        print("__________________________________________________")
        print("")
        time.sleep(3)
        options_tmdb()
    
    if(TMDB_options == "4"):
        show_input = input("Type here the name of the serie you want to search:   ")
        show = tv.search(show_input)
        for result in show:
            print("Serie title:", result.name)
            print("")
            print("Serie description:")
            print(result.overview)
            print("__________________________________________________")
            print("")
        time.sleep(3)
        options_tmdb()

    if(TMDB_options == "5"):
        print("Who do you want to search? Please fill in the firstname and surname of the actor or actress.")
        firstname = input("Firstname:  ")
        surname = input("Surname:  ")
        print("")
        fullname = firstname + "+" + surname
        url = "https://api.themoviedb.org/3/search/person?api_key="+tmdb.api_key+"&query="+fullname

        actordata = requests.get(url) 
        x = actordata.text

        idfront = x.index("id") + 4 
        idback = x.index("known") -2
        id = x[idfront:idback]

        person = Person()
        p = person.details(id)
        print("Name actor/actress:", p.name)
        print("")
        print("Biography actor/actress:")
        print(p.biography)
        print("")
        time.sleep(3)
        options_tmdb()

    else:
        print("You didn't type in one of the numbers in the list, Please try again.")
        options_tmdb()

start()
