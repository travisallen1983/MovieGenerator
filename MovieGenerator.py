import random
from datetime import date, time, datetime


def main():
    today = date.today()
    seed = today.strftime('%d') * today.weekday()
    number_list = []
    for number in range(0, 101):
        num = random.randint(0, 101)
        if num not in number_list:
            number_list.append(num)
    daily_numbers = []
    for number in range(0, 1):
        num = number_list[number]
        daily_numbers.append(num)
    daily_movies = []
    yesterdays_movies = []
    rm = open("DailyMovieList.txt", "r")
    rm_read = rm.readlines()
    for movie in rm_read:
        movie = movie.strip()
        yesterdays_movies.append(movie)
    mb = open("AllMoviesList.txt", "r")
    mb_read = mb.readlines()
    for movie in mb_read:
        movie = movie.strip()
        for number in daily_numbers:
            movie_1 = movie[0:2].rstrip(".")
            try:
                if int(movie_1) < 10:
                    if int(movie_1) == number:
                        if movie in yesterdays_movies:
                            daily_movies.append((mb_read[random.randrange(1, 63)]).strip())
                        else:
                            daily_movies.append(movie)
                elif int(movie_1) >= 10:
                    if int(movie_1) == number:
                        if movie in yesterdays_movies:
                            daily_movies.append((mb_read[random.randrange(1, 63)]).strip())
                        else:
                            daily_movies.append(movie)
            except ValueError:
                pass
    rmb = open("DailyMovieList.txt", "w")
    for movies in daily_movies:
        rmb.write(movies + "\n")

    rmb.close()
    mb.close()


if __name__ == "__main__":
    main()
