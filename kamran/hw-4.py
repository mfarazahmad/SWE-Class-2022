"""
HW 4: Create a Data Generator Function
Create several mock detailed Data Models representing data for the following Categories: Purchase History, IMDB Database, Cooking
Use the random module in Python to generate any unique numbers, values, names, prices etc.
Use loops to traverse your data structures and practice if statements
Create smaller functions to create each repeatable part of data

"""


""" Data Model

MOVIE DATABASE (IMDB rating, genre, Movie Title, review description,Year, votes, movie rating, release date, US box office )
IMDB Charts
    Box office
    Most popular movies
    Top 250 movies
    Top rated english movies
    Most popular Tv shows
    Top 250 Tv shows
    Top rated indian movies
    Lowest rated movies
    MOST POPULAR 
IMDB Rating SYSTEM
  User Rating
    Votes (Scale of 1-10)
        Demographics
           gender
           age range
  External Rating
  Metacritic Rating
MOVIE Title
    Genre
    Awards
        Academy Awards, BAFTA Awards
            Nominee
            Oscar
    IMDB Rating
    Votes
    Release Date
    Year
    Cast
    Trailers/Videos/photos
    Storyline
    Parent's Guide
CAST
    Director
    Writers
    Stars

"""
"Generating Movie name"

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','v','x','y','z']

randomNum = random.randint(0, len(letters))

def movieName():
    for i in range(0, len(letters)) : 
        print(letters[randomNum])
   

movieName()
    





