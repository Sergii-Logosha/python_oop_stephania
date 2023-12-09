# 09.12.23. Sergii Logosha sergiilogosha@gmail.com

class Movie:

    id_counter = 1

    def __init__(self, title, year, language, rating):
        self._id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1


movie_1 = Movie("Titanic", 1999, "English", 5.5)
movie_2 = Movie("Mask", 2000, "French", 5.6)

print(movie_1._id)
print(movie_2._id)
