# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


movie = Movie('Godfather', 4.8)
print(movie.get_title())
