# 15.12.23. Sergii Logosha sergiilogosha@gmail.com

class Movie:

    def __init__(self, title, year):
        self.title = title
        self._year = year

    @property
    def year(self):
        print('Calling the year getter')
        return self._year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, int) and 1980 <= new_year <= 2020:
            self._year = new_year
        else:
            print('The year must be between 1980 and 2020')


movie = Movie("Titanic", 1998)
print(movie.year)
movie.year = 2000
print(movie.year)
