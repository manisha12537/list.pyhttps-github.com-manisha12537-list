import re
import requests
from bs4 import BeautifulSoup
def scrap_top_movie():
    url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    get_url=requests.get(url)
    soup=BeautifulSoup(get_url.text,"html.parser")
    main_div=soup.find("table",class_="chart full-width")
    tr=main_div.find_all("tr")
    Movie_Rank=[]
    for i in tr[1:]:
       movie=i.find("td",class_="titleColumn")
       year=movie.find("span",class_="secondaryInfo").text
       name=movie.find("href",title_="Hrishikesh Mukherjee (dir.), Amol Palekar, Bindiya Goswami").get_text
       
    #    Movie_Rank.append(movie_rank)
    #    movie_name=re.split('(\d+)',name)
       print(name)

scrap_top_movie()

#  movie_rank=i.find("td",class_="bold").text
        # movie_ranks.append(movie_rank)