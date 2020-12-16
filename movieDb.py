"""
    Movies: holds the database of movies
    ["godfather", "a quiet place", "the shawshank redemption"]
"""
import random
random.seed(12345)
class Movies(object):
    def __init__(self, movies):
        # movies: List[str]
        self.movies = movies
    def addMovie(self, movie:str):
        self.movies.append(movie)
    def getMovieDb(self):
        return self.movies
    def totalNumberOfMovies(self):
        return len(self.movies)
    def getRandomMovie(self):
        return random.choice(self.movies)
    def getLastAddedMovie(self):
        return self.movies[-1] if self.movies else None

"""
    Test the above class
"""
def testMovies():
    listOfMovies = ["godfather", "a quiet place", "the shawshank redemption"]
    movies = Movies(listOfMovies)
    movieDb = movies.getMovieDb()
    assert movies.totalNumberOfMovies()==len(listOfMovies), "movies database length doesn't match.."
    newMovie = "titanic"
    listOfMovies.append(newMovie)
    movies.addMovie(newMovie)
    assert movies.totalNumberOfMovies()==len(listOfMovies), "size of db doesn't match after adding new movie.."
    lastMovieAddedInDb = movies.getLastAddedMovie()
    if lastMovieAddedInDb:
        assert lastMovieAddedInDb==newMovie, "the last movie added in db doesn't match the new movie.."
    randomMovieFromDb = movies.getRandomMovie()
    print("random movie from db: ", randomMovieFromDb)
    assert randomMovieFromDb in listOfMovies, "random movie not found in original list of movies.."
    print("all functions tested and passed..")

#testMovies()


