from bs4 import BeautifulSoup
import requests as req


# PROPERTIES
URL = "https://www.empireonline.com/movies/features/best-movies-2/"
PATH_WRITE = "./movies.txt"

res = req.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

movies = soup.find_all(name="div", class_="listicle-item-image")
movie_imgs = [movie.find(name="img") for movie in movies]
movie_titles = [title.get("alt") for title in movie_imgs]
movie_titles_asc = movie_titles[::-1]


# METHODS
def create_movies_file(path_write, titles):
    with open(path_write, "w") as file:
        for i, title in enumerate(titles):
            file.write(f"{i + 1} {title}\n")


# MAIN
create_movies_file(PATH_WRITE, movie_titles_asc)
