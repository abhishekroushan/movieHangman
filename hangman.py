import movieDb as mdb
import random
random.seed(12345)

class Hangman(object):
    def __init__(self, movie:str):
        self.movie = movie
        self.movieDict = {}
        self.incorrect = []
        self.populateMovieDict(movie)

    def getCharToDisplay(self, ch:str):
        return ch+" " if ch in self.movieDict and self.movieDict[ch] else "_ "

    def displayMovie(self):
        # Note: only called in the beginging OR after self.validateCharacter()
        # for each character, show _ or the actual character
        # depending on whether charcter in self.movieDict in false or true
        movieStrToList = [ch for ch in self.movie]
        displayStr = "".join(list(map(lambda x: self.getCharToDisplay(x), movieStrToList)))
        print("Movie:", displayStr)
        print("Incorrect", self.getIncorrect())
        print()

    def populateMovieDict(self, randomMovie:str):
        for ch in randomMovie: 
            self.movieDict[ch] = False # we'll modify the values to true as the correct guesses progress
            if ch==" ": self.movieDict[ch] = True

    def validateCharacter(self, ch:str):
        if ch not in self.movieDict: self.incorrect.append(ch)
        # ch in self.movieDict
        self.movieDict[ch] = True
    
    def getIncorrect(self):
        return self.incorrect
    
    def movieGuessed(self):
        for k,v in self.movieDict.items():
            if not self.movieDict[k]: return False
        return True

def playHangman():
    incorrectThreshold = 5
    listOfMovies = ["godfather", "titanic", "batman", "a quiet place", "the shawshank redemption"]
    movieDb = mdb.Movies(listOfMovies)
    randomMovie = movieDb.getRandomMovie()
    print("random movie selected = ", randomMovie)
    hangman = Hangman(randomMovie)
    hangman.displayMovie()
    while len(hangman.getIncorrect())<incorrectThreshold and not hangman.movieGuessed():
        inputChar = input("Enter next character..\n")
        hangman.validateCharacter(inputChar)
        hangman.displayMovie()
    if hangman.movieGuessed():
        print(randomMovie, "- correctly guessed!\n")
        return
    print("the movie was..", randomMovie)

playHangman()
        



